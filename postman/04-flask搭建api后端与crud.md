---
title: "用 Flask 搭建 API 后端与 CRUD"
parent: "Postman 接口测试实战知识库"
nav_order: 4
---

# Postman 实战｜用 Flask 搭建 API 后端与 CRUD

设计完契约，这篇用一个最小 Flask 例子把后端跑起来，并用 Postman 把增删改查（CRUD）全测一遍。

## ① 是什么

**Flask** 是 Python 的轻量 Web 框架；**CRUD** 指对资源的创建(Create)、读取(Read)、更新(Update)、删除(Delete)四种操作，对应 POST/GET/PUT/DELETE。

## ② 为什么重要

- 只有真后端才能验证设计是否落地；用 Postman 打这套接口，能立刻看到请求/响应是否符契约。
- 本地起服务 + Postman 联调，是日常最高频的开发闭环。

## ③ 核心概念拆解

- **最小应用**：`app = Flask(__name__)`，用 `@app.route("/books", methods=["GET"])` 定义端点；`flask run` 启动，默认 `http://127.0.0.1:5000`。
- **示例数据集**：用内存列表存几本书（id、title、author），省去接数据库，聚焦接口本身。
- **四个端点**：
  - `GET /books` 取全部；`GET /books/<id>` 取一本。
  - `POST /books` 新增（Body 传 JSON）。
  - `PUT /books/<id>` 整本替换更新。
  - `DELETE /books/<id>` 删除。
- **Postman 联调**：每个方法建一个请求，Body 选 raw → JSON，发完看响应码（200/201）和返回体。

## ④ 常见误区

- **误区 1**：忘了开 CORS。前端跨域调用会失败，开发期可用 `flask-cors` 放开。
- **误区 2**：PUT 和 POST 混用。新增用 POST、整体更新用 PUT，语义别乱。
- **误区 3**：直接改生产数据做实验。联调用内存/测试库，别碰真数据。

## ⑤ 一句话小结

Flask 起服务、Postman 打 CRUD，是验证 API 设计是否成立的"最小可用闭环"。

*下一篇：API 认证与授权：Basic / API Key / OAuth 2.0*

> 参考来源：*Mastering Postman, Second Edition*（本文为原创讲解，非转载原文）
