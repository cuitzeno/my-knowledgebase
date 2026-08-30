---
title: "API 安全测试（4.12 / APIT）"
parent: "OWASP WSTG Web 安全测试指南知识库"
nav_order: 13
---

# WSTG 实战｜API 安全测试（4.12 / APIT）

现代应用大量用 API。WSTG v5.0 把 API 测试（APIT）从"仅 GraphQL"扩成了完整一段，对齐 OWASP API Security Top 10。

## ① 是什么

**API 测试（4.12 / APIT）** 把前面各大类的思路落到 REST/GraphQL/SOAP 等接口：侦察、对象级授权（BOLA）、数据暴露、功能级授权（BFLA）等。

**WSTG 类别码：`APIT`**

## ② 为什么重要

- API 常是"无界面"的高权限入口，绕过了传统页面的防护，是攻击与赏金的高频目标。
- 对象级越权（BOLA）是 API 头号风险，传统 Web 的 IDOR 思路在 API 下更易大规模出现。

## ③ 核心概念拆解（对应 4.12.x / WSTG-APIT-00 到 -99）

| ID | 测试项 | 关键点 |
|----|--------|--------|
| 4.12.0 / WSTG-APIT-00 | API 测试概述 | API 类型、认证/授权模式、威胁模型、测试范围、工具集 |
| 4.12.1 / WSTG-APIT-01 | API 侦察 | 端点枚举、参数/Schema 发现、OpenAPI/Swagger/Postman/GraphQL Introspection、JS 分析、Fuzzing、版本管理 |
| 4.12.2 / WSTG-APIT-02 | API 对象级授权破坏 (BOLA) | 改对象 ID（`/users/123/orders`→`/users/456/orders`）、集合/单体/嵌套资源、UUID/可预测 ID、跨租户隔离 |
| 4.12.3 / WSTG-APIT-03 | 测试过度数据暴露 | 响应含敏感字段（密码哈希、token、内部标记、PII）、GraphQL 字段级暴露、分页/批量接口泄露、调试/内部端点 |
| 4.12.4 / WSTG-APIT-04 | API 功能级授权破坏 (BFLA) | 普通用户调用管理端点（`POST /admin/*`）、角色/权限矩阵缺失、HTTP 方法越权、微服务内部 API 越权 |
| 4.12.99 / WSTG-APIT-99 | 测试 GraphQL | Introspection 开启、深度/复杂度 DoS、批量查询、字段级授权、别名重命名、指令滥用、上传/订阅、Schema 泄露 |

## ④ 常见误区

- **误区 1**：API 有鉴权就安全。对象级越权（BOLA）是 API 头号风险，鉴权≠授权。
- **误区 2**：GraphQL 关了 introspection 就安全。字段级越权、深度 DoS、批量查询仍在。
- **误区 3**：响应里"前端不显示"= 安全。过度数据暴露照样泄露敏感字段。
- **误区 4**：只测 REST。GraphQL、gRPC、WebSocket、MQTT 等同样需要覆盖。

## ⑤ 一句话小结

API 测试把大类思路落到接口，重点查 BOLA/过度暴露/BFLA/GraphQL（对应 OWASP API Top 10）；鉴权≠授权，对象级检查是核心。

*下一篇：报告与附录*

> 参考来源：OWASP Web Security Testing Guide（最新 v5.0 / 2026 开发线）（本文为原创讲解，非转载原文）