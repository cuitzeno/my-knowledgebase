---
title: "JWT（含 Scopes）"
parent: "身份、授权与标准"
grand_parent: "Web 安全与开发基础实战知识库"
nav_order: 3
---

# 概念｜JWT（含 Scopes）

JWT 是现代 API 鉴权主流令牌。理解结构与陷阱，才能安全使用。

## ① 是什么

**JWT** 是自包含令牌：三段 `header.payload.signature`（Base64Url 编码）。服务端用签名验证"内容未被篡改"，无需查库即可信任声明（claims）。

## ② 为什么重要

- 签名可被绕过或密钥可爆破 → 攻击者可伪造任意身份/权限。
- `scope` 声明决定"能访问什么"，是 API 授权关键。

## ③ 核心概念拆解（带示例）

- **结构示例**（解码后）：

```
header:  {"alg":"HS256","typ":"JWT"}
payload: {"sub":"alice","role":"user","scope":"read:profile","exp":1700000000}
signature: HMAC-SHA256(base64(header)+"."+base64(payload), key)
```
实际令牌形如 `eyJhbGc...eyJzdWI...签名`。
- **算法**：对称 `HS256`（共享密钥）或非对称 `RS256`（私钥签、公钥验）。
- **经典漏洞**：
  - *alg=none*：服务端若接受"无签名"，令牌可被任意篡改。
  - *密钥可爆破*：HS256 弱密钥时离线爆破并伪造。
  - *过期不校验*：忽略 `exp` 导致令牌永久有效。
- **Scopes**：payload 里声明权限范围（如 `read:profile`），服务端据此做对象/功能级授权（呼应 WSTG APIT-03/05）。

## ④ 常见误区

- JWT 加密？默认只签名不加密，payload 可被解码读（敏感数据别放 payload）。
- 改了算法就安全？必须服务端白名单固定算法（禁用 none）。
- 有 JWT 就有权限？仍要服务端按 scope/角色校验，不能只验签名。

## ⑤ 一句话小结

JWT 用签名保证声明不被篡改；安全要点是固定算法（禁 none）、强密钥、校验过期，并用 scope 做服务端授权。

*下一篇：[JWT 安全实验](04-jwt实验.md)*

> 参考来源：https://jwt.io/introduction
