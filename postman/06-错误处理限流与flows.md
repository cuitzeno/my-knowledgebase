---
title: "错误处理、限流与 Postman Flows 编排"
parent: "Postman 接口测试实战知识库"
nav_order: 6
---

# 错误处理、限流与 Postman Flows 编排

## 一句话定义
**错误处理**统一响应结构不泄露堆栈，**限流**保护服务不被打挂，**Flows**用可视化拖拽把多请求串成业务流程(登录→取Token→查数据→断言)。

## 核心架构 / 工作原理

```mermaid
graph TD
  A[API 治理三件套] --> B[统一错误处理]
  B --> B1[全局异常捕获 -> 统一结构]
  B --> B2[错误码分层: 业务码+HTTP 码+用户提示+内部追踪ID]
  B --> B3[敏感信息脱敏: 不返回堆栈/SQL/密钥]
  
  A --> C[限流 Rate Limiting]
  C --> C1[算法: 固定窗口/滑动窗口/令牌桶/漏桶]
  C --> C2[维度: IP/用户/API Key/租户/端点]
  C --> C3[响应: 429 + Retry-After + X-RateLimit-* 头]
  C --> C4[分布式: Redis + Lua 脚本/Redis Cell]
  
  A --> D[Postman Flows 可视化编排]
  D --> D1[块: Send Request / Variable / Condition / Loop / Script / Output]
  D --> D2[连线: 数据流(变量传递) + 控制流(条件/循环)]
  D --> D3[运行: 本地/云端/定时/CLI]
  D --> D4[用例: 登录链、数据清洗、端到端业务流、报告生成]
```

| 组件 | 核心配置 | Postman 实现 |
|------|----------|--------------|
| **错误处理** | Flask: `@app.errorhandler` / FastAPI: `exception_handler` / Spring: `@ControllerAdvice` | 测试脚本断言 `pm.response.to.have.status(400)` + `pm.response.json().error.code === 'VALIDATION_ERROR'` |
| **限流** | Flask-Limiter / Express-rate-limit / Spring Cloud Gateway / Nginx limit_req | 测试：并发跑 Runner/Newman → 看 429 + `Retry-After` → 验证限流生效 |
| **Flows 块** | Send Request(选集合请求) / Variable(存取变量) / Condition(if/else) / Loop(遍历数组) / Script(JS 逻辑) / Output(导出结果) | Flows 标签 → Create Flow → 拖拽块 → 连线 → Run → 看执行日志/变量面板 |

## 快速上手步骤

1. **后端统一错误处理 (Flask 示例)**：
   ```python
   from flask import jsonify
   import traceback, uuid
   
   class APIError(Exception):
       def __init__(self, code, message, status=400, details=None):
           self.code, self.message, self.status, self.details = code, message, status, details
   
   @app.errorhandler(APIError)
   def handle_api_error(e):
       trace_id = str(uuid.uuid4())[:8]
       app.logger.error(f"[{trace_id}] {e.code}: {e.message}\n{traceback.format_exc()}")
       return jsonify({
           'error': {'code': e.code, 'message': e.message, 'details': e.details, 'trace_id': trace_id}
       }), e.status
   
   @app.errorhandler(500)
   def handle_500(e):
       trace_id = str(uuid.uuid4())[:8]
       app.logger.exception(f"[{trace_id}] Internal Server Error")
       return jsonify({'error': {'code': 'INTERNAL_ERROR', 'message': '服务器内部错误', 'trace_id': trace_id}}), 500
   ```
2. **限流 (Flask-Limiter)**：
   ```python
   from flask_limiter import Limiter
   from flask_limiter.util import get_remote_address
   
   limiter = Limiter(get_remote_address, app=app, default_limits=["200 per day", "50 per hour"])
   # 单端点精细限流
   @app.route('/api/sensitive')
   @limiter.limit("10 per minute")
   def sensitive(): ...
   ```
3. **Postman 测试限流**：
   - Collection Runner → Iterations: 100 → Delay: 0 → Run → 看 429 比例
   - Tests: `pm.test('rate limited', () => { if (pm.response.code === 429) pm.expect(pm.response.headers.get('Retry-After')).to.exist })`
4. **建第一个 Flow**：
   - Flows 标签 → Create Flow → 命名 `Login and Get Books`
   - 拖 **Send Request** 块 → 选 `POST {{base_url}}/login` → 命名 `Login`
   - 拖 **Variable** 块 → Name `access_token` → Value 连 `Login` 响应的 `body.access_token`
   - 拖 **Send Request** → 选 `GET {{base_url}}/books` → Auth: Bearer Token `{{access_token}}` → 命名 `GetBooks`
   - 拖 **Output** → 连 `GetBooks` 响应 → Run → 看输出面板

```json
// 统一错误响应示例
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "请求参数校验失败",
    "details": [{"field": "isbn", "issue": "必须为 13 位数字"}],
    "trace_id": "a1b2c3d4"
  }
}

// 限流响应头
HTTP/1.1 429 Too Many Requests
Retry-After: 45
X-RateLimit-Limit: 50
X-RateLimit-Remaining: 0
X-RateLimit-Reset: 1700000000
```

## 踩坑避坑指南

| 场景 | 问题现象 | 原因 | 解决/最佳实践 |
|------|----------|------|---------------|
| 直接返回异常堆栈 | 前端/攻击者看到内部路径/SQL/版本 | 无全局捕获 | **统一错误包装**：只返回 `code/message/trace_id`，堆栈只进日志 |
| 限流只限 IP | 攻击者用代理池/共享 IP 误伤 | 维度单一 | **多维限流**：API Key/用户 ID/租户 ID + IP；登录接口加验证码/设备指纹 |
| Flow 变量不传递 | 下游块读不到上游值 | 连线/变量名错 | **连线必须从上游输出口 → 下游输入口**；变量名大小写一致；用面板调试看实时值 |
| Flow 跑不通/卡死 | 无报错/无输出 | 死循环/条件永假/请求超时 | **加超时/断点调试**；Condition 块检查分支；Loop 设最大次数 |
| 线上跑 Flow 改了数据 | 误用生产环境 | 环境变量选错 | **Flow 专用 Environment(Stage/Test)**；生产只读 Monitor |

## 替代方案对比

| 维度 | Postman Flows | 代码编排(Python/JS) | n8n / Zapier | Airflow / Temporal |
|------|---------------|---------------------|--------------|-------------------|
| 可视化程度 | ✅ 拖拽连线 | ❌ 代码 | ✅ 节点式 | ✅ DAG 图 |
| 适合场景 | API 级编排/测试/演示 | 复杂业务逻辑/数据管道 | 低代码集成/自动化 | 重调度/数据工程 |
| 版本控制 | ✅ 集合版本/PR | ✅ Git 原生 | ⚠️ 导入导出 | ✅ 代码即配置 |
| 运行环境 | Postman 云/本地/CLI | 任意 | 云/自建 | 集群 |
| 学习成本 | 低 | 中(需懂语言) | 低 | 高 |

---

> 参考来源：*Mastering Postman, Second Edition*（本文为原创讲解，非转载原文）

*下一篇：[API 测试类型与 Postman 测试能力](07-api测试类型与postman能力.md)*