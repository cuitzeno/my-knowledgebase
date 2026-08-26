---
title: "用 Flask 搭建 API 后端与 CRUD"
parent: "Postman 接口测试实战知识库"
nav_order: 4
---

# 用 Flask 搭建 API 后端与 CRUD

## 一句话定义
用最小 **Flask** 应用跑起真后端，配合 Postman 验证 **CRUD**(Create/Read/Update/Delete) 全流程——这是验证 API 设计是否落地的"最小可用闭环"。

## 核心架构 / 工作原理

```mermaid
graph LR
  A[Postman 请求] --> B[Flask 路由分发]
  B --> C[内存存储 / 数据库]
  C --> D[业务逻辑]
  D --> E[JSON 响应]
  E --> A
  
  subgraph Flask 最小应用
    F[app = Flask(__name__)]
    G[@app.route('/books', methods=['GET','POST'])]
    H[@app.route('/books/<id>', methods=['GET','PUT','DELETE'])]
    I[内存列表 books = []]
  end
```

| CRUD 操作 | HTTP 方法 | 端点 | 请求 Body | 成功响应 |
|-----------|-----------|------|-----------|----------|
| **Create** 创建 | POST | `/books` | `{title, author, isbn}` | 201 + 创建对象 |
| **Read All** 列表 | GET | `/books` | Query: page/size/sort/filter | 200 + 分页对象 |
| **Read One** 详情 | GET | `/books/<id>` | — | 200 + 单对象 |
| **Update** 全量更新 | PUT | `/books/<id>` | 完整对象 | 200 + 更新后对象 |
| **Delete** 删除 | DELETE | `/books/<id>` | — | 204 No Content |

## 快速上手步骤

1. **装依赖 & 起服务**：
   ```bash
   pip install flask flask-cors
   ```
2. **写最小 `app.py`**：
   ```python
   from flask import Flask, request, jsonify, abort
   from flask_cors import CORS
   import uuid, datetime

   app = Flask(__name__)
   CORS(app)  # 开发期允许跨域

   books = []  # 内存存储，重启丢失

   # 列表 + 分页/过滤
   @app.route('/books', methods=['GET'])
   def list_books():
       page = int(request.args.get('page', 1))
       size = int(request.args.get('size', 20))
       start, end = (page-1)*size, page*size
       return jsonify({
           'data': books[start:end],
           'pagination': {'page': page, 'size': size, 'total': len(books)}
       })

   # 创建
   @app.route('/books', methods=['POST'])
   def create_book():
       data = request.get_json()
       if not data or not all(k in data for k in ('title','author','isbn')):
           abort(400, 'Missing required fields')
       book = {
           'id': str(uuid.uuid4()),
           'title': data['title'],
           'author': data['author'],
           'isbn': data['isbn'],
           'created_at': datetime.datetime.utcnow().isoformat() + 'Z'
       }
       books.append(book)
       return jsonify(book), 201

   # 详情
   @app.route('/books/<id>', methods=['GET'])
   def get_book(id):
       book = next((b for b in books if b['id'] == id), None)
       if not book: abort(404)
       return jsonify(book)

   # 全量更新
   @app.route('/books/<id>', methods=['PUT'])
   def update_book(id):
       book = next((b for b in books if b['id'] == id), None)
       if not book: abort(404)
       data = request.get_json()
       book.update({k: data[k] for k in ('title','author','isbn') if k in data})
       return jsonify(book)

   # 删除
   @app.route('/books/<id>', methods=['DELETE'])
   def delete_book(id):
       global books
       books = [b for b in books if b['id'] != id]
       return '', 204

   if __name__ == '__main__':
       app.run(debug=True, port=5000)
   ```
3. **启动**：`python app.py` → 监听 `http://127.0.0.1:5000`
4. **Postman 验证 CRUD**：
   - 建 Collection `Bookstore API` → 环境变量 `base_url=http://127.0.0.1:5000`
   - 5 个请求：GET/POST `/books`、GET/PUT/DELETE `/books/{{id}}`
   - POST Body: raw JSON `{title, author, isbn}` → Send → Tests 提取 `pm.environment.set('id', pm.response.json().id)`
   - 依次跑：Create → List → Get One → Update → Delete → List 验证

```bash
# 快速验证 curl 版
curl -X POST http://127.0.0.1:5000/books -H "Content-Type: application/json" -d '{"title":"Clean Code","author":"Robert Martin","isbn":"9780132350884"}'
curl http://127.0.0.1:5000/books
```

## 踩坑避坑指南

| 场景 | 问题现象 | 原因 | 解决/最佳实践 |
|------|----------|------|---------------|
| 前端调本地报 CORS | `Access-Control-Allow-Origin` 缺失 | 浏览器同源策略 | **开发期 `flask-cors` 全开**；生产配具体域名 |
| PUT 和 POST 混用 | 语义混淆、幂等性破坏 | 不懂 REST 规范 | **POST=创建(非幂等)**、**PUT=全量替换(幂等)**、**PATCH=部分更新** |
| 直接操作生产库验证 | 数据污染/丢失 | 无隔离环境 | **本地内存/测试库**；用 `pytest` + `testcontainers` 起临时 DB |
| 响应无 `Content-Type: application/json` | Postman 不自动 Pretty/解析 | Flask 默认 text/html | `jsonify()` 或 `Response(json.dumps(), mimetype='application/json')` |
| 并发请求内存列表丢数据 | 多线程下列表操作不安全 | Flask dev server 多线程 | 开发期可忽略；压测用 Gunicorn + 真 DB |

## 替代方案对比

| 维度 | Flask 最小后端 | FastAPI | Express.js | Spring Boot | Mock Server Only |
|------|---------------|---------|------------|-------------|------------------|
| 启动速度 | 极快(秒) | 极快 | 快 | 慢(分钟) | 即时 |
| 代码量 | 极少(~50 行) | 少(类型提示) | 少 | 多(配置/注解) | 无代码 |
| 自动文档 | 无(需插件) | ✅ OpenAPI 自动 | ⚠️ 需插件 | ✅ SpringDoc | ✅ 契约即文档 |
| 类型安全 | 无 | ✅ Pydantic | TypeScript 可选 | ✅ Java 强类型 | 无 |
| 适合场景 | 快速验证契约/教学 | 现代 Python 生产 | Node 团队 | Java 企业 | 纯前端并行开发 |

---

> 参考来源：*Mastering Postman, Second Edition*（本文为原创讲解，非转载原文）

*下一篇：[API 认证与授权：Basic / API Key / OAuth 2.0](05-api认证与授权.md)*