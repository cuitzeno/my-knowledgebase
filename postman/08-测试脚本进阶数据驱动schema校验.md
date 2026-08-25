---
title: "测试脚本进阶：数据驱动、请求链与 Schema 校验"
parent: "Postman 接口测试实战知识库"
nav_order: 8
---

# Postman 实战｜测试脚本进阶：数据驱动、请求链与 Schema 校验

会写一条断言只是入门。这篇讲 Postman 11 新脚本能力里最实用的三招：用一份数据跑多组用例、把请求串成链、以及用 Schema 锁死响应结构。

## ① 是什么

- **数据驱动测试**：同一套请求，用 CSV/JSON 里的多行数据逐条跑，覆盖各种输入输出。
- **请求链（Chaining）**：把一个请求的返回值塞进变量，传给下一个请求。
- **Schema 校验**：用 JSON Schema 定义"响应必须长这样"，自动判断结构是否合法。

## ② 为什么重要

- 手写 20 个几乎一样的请求 = 维护噩梦；数据驱动一行数据一行用例。
- 真实业务多是"登录拿 token → 带 token 查数据"，不串联就测不了。
- Schema 校验能在契约被破坏（字段改名/类型变）时立刻报警。

## ③ 核心概念拆解

- **动态变量与上下文**：`pm.variables.set("token", ...)` 存，`{{token}}` 在后续请求里引用；`pm.environment` 可跨请求。
- **请求链**：在 Test 脚本里 `pm.collectionVariables.set("id", pm.response.json().id)`，下一请求 URL 用 `{{id}}`。
- **数据驱动**：Runner 里选 Data 文件（CSV/JSON），脚本里用 `pm.iterationData.get("name")`。Postman 11 增强了条件请求与循环。
- **Schema 校验**：用 `tv4`/`ajv` 在测试里 `pm.response.to.have.jsonSchema(schema)`，结构不符即失败。Postman 新脚本支持更稳的报错与日志。

## ④ 常见误区

- **误区 1**：变量名拼错还以为没传。先 `console.log(pm.variables.get("x"))` 排查。
- **误区 2**：Schema 写太严。把可选字段标 required，正常变更也会红。
- **误区 3**：数据文件含敏感信息。CSV/JSON 别提交真实账号密码。

## ⑤ 一句话小结

数据驱动扩覆盖、请求链连业务、Schema 锁契约——三招把"能跑"升级成"可信"。

*下一篇：API 安全威胁与防护实践*

> 参考来源：*Mastering Postman, Second Edition*（本文为原创讲解，非转载原文）
