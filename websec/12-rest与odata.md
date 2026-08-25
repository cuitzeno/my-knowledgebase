---
title: "REST 与 OData 服务"
parent: "Web 安全与开发基础实战知识库"
nav_order: 12
---

# 开发｜REST 与 OData 服务

现代 Web/API 多基于 REST 与 OData。理解它们的模型，才能正确设计与测试接口安全。

## ① 是什么

**REST** 是一种用 HTTP 风格设计 API 的架构：资源用 URL 标识，用 HTTP 方法表达操作，无状态、可缓存。**OData** 是在 REST 之上的数据查询协议（v2/v4），用统一查询选项（`$filter`、`$select`、`$expand`、`$orderby` 等）操作数据。

## ② 为什么重要

- 接口是"无界面"的高权限入口，设计不当直接暴露数据。
- OData 的查询表达式若未约束，可能成为注入、越权与信息泄露的温床。

## ③ 核心概念拆解

- **REST 核心**：资源（名词 URL）、HTTP 方法（动作）、无状态（每次带凭证）、统一接口。
- **OData v2 要点**：`$filter` 过滤、`$expand` 关联展开、`$select` 投影字段、`$top/$skip` 分页；服务常暴露 EDM 元数据（`$metadata`）。
- **安全关注点**：
  - *越权*：改 ID/查询条件访问他人数据（BOLA，呼应 WSTG APIT）。
  - *注入*：`$filter` 里拼接未校验输入 → OData/后端注入。
  - *过度暴露*：默认返回全字段（呼应 API 测试第 17 篇 / WSTG APIT-04）。
  - *元数据泄露*：`$metadata` 暴露数据模型，助攻击者构造请求。

## ④ 常见误区

- **误区 1**：REST 无状态=不用管会话。鉴权令牌仍须每请求校验。
- **误区 2**：OData 查询"内部用"就安全。需服务端校验 `$filter` 与权限。
- **误区 3**：关掉 `$metadata` 就安全。字段级越权仍在。

## ⑤ 一句话小结

REST 用资源+方法建模、OData 在其上加查询协议；两者安全都归结为：鉴权、对象级授权、查询注入防护与最小字段暴露。

*下一篇：UI5/JavaScript 与 MVC 绑定安全*

> 参考来源：https://www.codecademy.com/article/what-is-rest · https://www.odata.org/documentation/odata-version-2-0/
