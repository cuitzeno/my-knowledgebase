---
title: "HTTP 方法与语义"
parent: "协议与架构"
grand_parent: "Web 安全与开发基础实战知识库"
nav_order: 2
---

# 概念｜HTTP 方法与语义

GET 和 POST 不只是"两种请求"。方法表达"想对资源做什么"，语义错了就是安全漏洞。

## ① 是什么

**HTTP 方法** 标识操作类型：常见 `GET`（取）、`POST`（建）、`PUT`（整体改）、`PATCH`（局部改）、`DELETE`（删）、`HEAD`、`OPTIONS`。REST 风格用方法对应 CRUD。

## ② 为什么重要

- 方法决定"动作"，混淆方法会绕过校验或触发非预期操作（如把 GET 当删除用）。
- 服务器若对 `PUT/DELETE` 等未禁用，可能被滥用。

## ③ 核心概念拆解（带示例）

- **安全/幂等**：`GET`、`HEAD` 应只读、无副作用；`PUT`、`DELETE` 幂等；`POST` 不幂等。
- **语义约定**：改数据用 POST/PUT，删用 DELETE，查用 GET；前端隐藏按钮≠后端校验方法。
- **真实请求示例**（用 Postman/Burp 发出）：

```
POST /api/books HTTP/1.1
Host: api.example.com
Content-Type: application/json
Authorization: Bearer <token>

{"title":"SecBook","author":"A"}

HTTP/1.1 201 Created
{"id":102,"title":"SecBook"}
```

改成 `GET /api/books` 就是"只读取"；若服务器对 GET 也执行删除逻辑，就是方法校验缺失。
- **测试角度**：用 Burp/Postman 改方法（动词篡改）看服务器是否真校验（呼应 WSTG 4.7.3）。

## ④ 常见误区

- GET 就安全？GET 带敏感参数会进日志/历史；它应无副作用但不等于无风险。
- 前端只给 POST 按钮就安全？攻击者可用工具任意改方法。
- 方法限制靠前端？必须在服务端校验允许的方法集合。

## ⑤ 一句话小结

HTTP 方法表达"对资源做什么"；守住安全/幂等语义、并在服务端校验允许方法，才能避免方法被滥用。

*下一篇：[HTTP 安全响应头（OWASP Secure Headers）](03-http安全头.md)*

> 参考来源：https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods
