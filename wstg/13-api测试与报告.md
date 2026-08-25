---
title: "API 安全测试与报告（4.12 / APIT）"
parent: "OWASP WSTG Web 安全测试指南知识库"
nav_order: 13
---

# WSTG 实战｜API 安全测试与报告（4.12 / APIT）

现代应用大量用 API。WSTG 5.0 把 API 测试（APIT）从"仅 GraphQL"扩成了完整一段，对齐 OWASP API Security Top 10。这篇先讲 API 测试项，再讲怎么出报告。

## ① 是什么

- **API 测试（4.12 / APIT）** 把前面各大类的思路落到 REST/GraphQL/SOAP 等接口：侦察、对象级授权（BOLA）、数据暴露、功能级授权（BFLA）等。
- **报告（5）**：把结果整理成带风险评级、复现步骤、修复建议的交付物。

5.0 的 APIT 场景：`WSTG-APIT-01` 概述、`APIT-02` API 侦察、`APIT-03` BOLA（对象级越权）、`APIT-04` 过度数据暴露、`APIT-05` BFLA（功能级越权）、`APIT-99` GraphQL。

## ② 为什么重要

- API 常是"无界面"的高权限入口，绕过了传统页面的防护，是攻击与赏金的高频目标。
- 对象级越权（BOLA）是 API 头号风险，传统 Web 的 IDOR 思路在 API 下更易大规模出现。

## ③ 核心概念拆解（对应 4.12.x / APIT）

- **API 侦察（APIT-02）**：收集端点、参数、鉴权方式；读 OpenAPI/Swagger、文档、JS 里的接口线索。
- **BOLA 对象级越权（APIT-03）**：改对象 ID（如 `?user_id=其他`）访问他人数据——API 版 IDOR，最常见也最危。
- **过度数据暴露（APIT-04）**：响应塞了不该给的字段（密码哈希、内部标记），靠客户端"不显示"来遮掩。
- **BFLA 功能级越权（APIT-05）**：普通用户调用本属管理员的函数/端点（如 `POST /admin/...`）。
- **GraphQL（APIT-99）**：introspection 暴露全 schema；深嵌套/批量查询打 DoS；字段级越权。
- **API 通用检查**：令牌泄露/过期、速率限制缺失、批量端点泄露、错误响应过详。
- **报告要素（5）**：摘要（范围/方法/总体风险）+ 发现列表（严重度、位置、复现、证据、影响、修复）+ 风险定级（如 OWASP Risk Rating）。

## ④ 常见误区

- **误区 1**：API 有鉴权就安全。对象级越权（BOLA）是 API 头号风险，鉴权≠授权。
- **误区 2**：GraphQL 关了 introspection 就安全。字段级越权仍在。
- **误区 3**：响应里"前端不显示"= 安全。过度数据暴露照样泄露敏感字段。
- **误区 4**：报告只贴"有漏洞"。要带复现与修复优先级。

## ⑤ 一句话小结

API 测试把大类思路落到接口，重点查 BOLA/过度暴露/BFLA（对应 OWASP API Top 10）；报告把发现变成"可修的交付物"——这是 WSTG 的终点。

*系列完*

> 参考来源：*OWASP Web Security Testing Guide*（最新 5.0 开发线；上一稳定版 v4.2）（本文为原创讲解，非转载原文）
