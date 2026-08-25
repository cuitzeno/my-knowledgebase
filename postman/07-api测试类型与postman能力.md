---
title: "API 测试类型与 Postman 测试能力"
parent: "Postman 接口测试实战知识库"
nav_order: 7
---

# Postman 实战｜API 测试类型与 Postman 测试能力

"测试"不是只点一下看返回。这篇先分清要测什么类型，再看 Postman 用哪些武器覆盖它们，包括对 REST/SOAP/GraphQL/gRPC/WebSocket 的支持。

## ① 是什么

API 测试按目标分多类：**功能**（对不对）、**性能**（快不快）、**安全**（稳不稳）、**可靠性**（挂不挂）、**兼容性**（版本/客户端）、**文档**（说明跟不跟手）。

Postman 的测试能力：Test Scripts（脚本断言）、Runner（批量跑集合）、Mock、Monitor（监控）、Integrations（集成）。

## ② 为什么重要

- 只做功能测试，上线后可能被慢查询拖死（性能）或被越权调用（安全）。
- 弄清 Postman 能测哪些协议，才能把不同接口统一收进一个集合管理。

## ③ 核心概念拆解

- **要测的协议**：
  - *REST*：最常用，Postman 原生支持。
  - *SOAP*：XML 报文，Body 选 raw+XML。
  - *GraphQL*：在 Body 里写 query，Postman 有专门标签。
  - *gRPC / WebSocket*：较新版本支持，可发流式/双向消息。
- **Postman 四件套**：
  - *Test Scripts*：用 `pm.test()` 写断言，如检查状态码、响应字段。
  - *Runner*：批量顺序跑一个集合里的所有请求。
  - *Mock*：返回假数据，隔离后端依赖。
  - *Monitor*：定时云端跑集合，失败告警。

## ④ 常见误区

- **误区 1**：测试=看返回 200。还要断言业务字段、状态码、耗时。
- **误区 2**：只测 REST。若系统有 GraphQL/gRPC，也要进同一套集合。
- **误区 3**：Mock 当真后端。Mock 只验证契约，不验证逻辑。

## ⑤ 一句话小结

先按"功能/性能/安全…"列清测试目标，再用 Postman 的脚本、Runner、Mock、Monitor 四件套一把抓。

*下一篇：测试脚本进阶：数据驱动、请求链与 Schema 校验*

> 参考来源：*Mastering Postman, Second Edition*（本文为原创讲解，非转载原文）
