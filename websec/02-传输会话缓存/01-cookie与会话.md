---
title: "Cookie 与会话管理"
parent: "传输、会话与缓存"
grand_parent: "Web 安全与开发基础实战知识库"
nav_order: 1
---

# 概念｜Cookie 与会话管理（Secure/HttpOnly/SameSite）

HTTP 无状态，靠 Cookie 记住"你是谁"。Cookie 的三个属性直接决定会话安全。

## ① 是什么

**Cookie** 是服务器通过 `Set-Cookie` 让浏览器存的小数据，之后每次请求自动带上，用来维持登录态（会话）。关键属性：`Secure`、`HttpOnly`、`SameSite`、`Path/Domain`、`Expires/Max-Age`。

## ② 为什么重要

- 会话令牌若被偷（JS 读走、明文传走、跨站带走），攻击者可"顶替你"。
- 三个属性是防窃取的第一道闸门，配错即成高危。

## ③ 核心概念拆解

- **Secure**：只在 HTTPS 下传输，防明文 HTTP 被截获令牌。
- **HttpOnly**：禁止 JS 通过 `document.cookie` 读取，抗 XSS 偷 Cookie。
- **SameSite**：`Strict`/`Lax` 限制跨站请求携带 Cookie，缓解 CSRF；`None` 需配合 Secure。
- **生命周期**：会话 Cookie（关浏览器失效）vs 持久 Cookie；超时/登出要真销毁服务端会话。
- **与令牌关系**：现代也常用 `Authorization: Bearer <JWT>`（见④组 JWT 篇），但 Cookie 仍是主力会话机制。

## ④ 常见误区

- 只设 HttpOnly 不设 Secure：HTTPS 下仍可能被降级明文传。
- SameSite=None 又不开 Secure：会被中间人拿到。
- 前端登出=安全：必须服务端使会话失效，否则令牌仍可复用。

## ⑤ 一句话小结

Cookie 会话安全三件套：Secure（仅 HTTPS 传）、HttpOnly（防 JS 偷）、SameSite（抗 CSRF）；再配合正确超时与登出销毁。

*下一篇：[TLS 握手与 HTTPS](02-tls与https.md)*

> 参考来源：https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies
