---
title: "API 设计原则与 OpenAPI 规范"
parent: "Postman 接口测试实战知识库"
nav_order: 3
---

# Postman 实战｜API 设计原则与 OpenAPI 规范

在写一行后端代码之前，先把 API 的"契约"定好。这篇讲设计期的核心原则，以及用 OpenAPI + Mock Server 让前后端并行开工。

## ① 是什么

**API 设计** 是定义"有哪些端点、请求长什么样、响应长什么样"的过程，而不急于实现逻辑。
**OpenAPI** 是用一份 YAML/JSON 描述这套契约的标准；**Mock Server** 则是按契约自动生成的假接口，前端不用等后端就能调。

## ② 为什么重要

- 设计先行能及早发现歧义，避免后端写完前端才发现字段对不上。
- 用 Mock Server，前后端可以同一天开工：前端打 mock，后端写真逻辑，最后一接就通。
- OpenAPI 还是后面自动文档、Schema 校验的共同源头。

## ③ 核心概念拆解

- **端点设计原则**：用名词而非动词（用 `/books` 而非 `/getBooks`）；用 HTTP 方法表达动作（GET 查、POST 增、PUT 改、DELETE 删）；版本放路径或 Header（如 `/v1/books`）。
- **请求/响应 Schema**：明确每个字段的类型、是否必填、示例值。类比合同里的"甲乙双方各交什么"。
- **用 OpenAPI 描述**：在 Postman 里定义 API Specification，自动生成文档骨架。
- **Mock Server**：基于 Schema 返回示例数据，前端本地就能联调。

## ④ 常见误区

- **误区 1**：设计=写代码。错，设计阶段只定契约，不写业务。
- **误区 2**：Mock 是可有可无。其实它是前后端解耦的关键。
- **误区 3**：字段类型随便写。类型不对，后面 Schema 校验会全红。

## ⑤ 一句话小结

先定契约（OpenAPI）、再发 Mock、最后实现，API 设计期就把"对不齐"的风险掐灭在摇篮里。

*下一篇：用 Flask 搭建 API 后端与 CRUD*

> 参考来源：*Mastering Postman, Second Edition*（本文为原创讲解，非转载原文）
