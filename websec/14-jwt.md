---
title: "JWT（含 Scopes）"
parent: "Web 安全与开发基础实战知识库"
nav_order: 14
---

# 身份｜JWT（含 Scopes）

JWT 是现代 API 鉴权的主流令牌。理解它的结构与陷阱，才能安全使用。

## ① 是什么

**JWT（JSON Web Token）** 是自包含的令牌：三段 `header.payload.signature`（Base64Url 编码）。服务端用签名验证"内容未被篡改"，无需查库即可信任声明（claims）。

## ② 为什么重要

- 一旦签名可被绕过或密钥可爆破，攻击者可伪造任意身份/权限。
- `scope` 声明决定"能访问什么"，是 API 授权的关键。

## ③ 核心概念拆解

- **结构**：`header`（算法/类型）、`payload`（sub、exp、scope 等声明）、`signature`（对前两部分的签名）。
- **算法**：对称 `HS256`（共享密钥）或非对称 `RS256`（私钥签、公钥验）。
- **经典漏洞**：
  - *alg=none*：服务端若接受"无签名"，令牌可被任意篡改。
  - *密钥可爆破*：HS256 用弱密钥时，攻击者可离线爆破并伪造。
  - *过期不校验*：忽略 `exp` 导致令牌永久有效。
- **Scopes**：在 payload 里声明权限范围（如 `read:profile`），服务端据此做**对象/功能级授权**（呼应 WSTG APIT-03/05）。

## ④ 常见误区

- **误区 1**：JWT 加密。默认只签名不加密，payload 可被解码读（敏感数据别放 payload）。
- **误区 2**：改了算法就安全。必须服务端白名单固定算法（禁用 none）。
- **误区 3**：有 JWT 就有权限。仍要在服务端按 scope/角色校验，不能只验签名。

## ⑤ 一句话小结

JWT 用签名保证声明不被篡改；安全要点是固定算法（禁 none）、强密钥、校验过期，并用 scope 做服务端授权。

*下一篇：OAuth 2.0（含 Scopes）*

> 参考来源：https://jwt.io/introduction
