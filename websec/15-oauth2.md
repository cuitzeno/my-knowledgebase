---
title: "OAuth 2.0（含 Scopes）"
parent: "Web 安全与开发基础实战知识库"
nav_order: 15
---

# 身份｜OAuth 2.0（含 Scopes）

OAuth 2.0 解决"授权第三方访问"的问题，是现代登录/对接的事实标准。

## ① 是什么

**OAuth 2.0** 是授权框架：资源拥有者通过"授权"让第三方应用代表自己访问资源，而不把密码交给第三方。核心是**访问令牌（access token）** + **授权码流程**。

## ② 为什么重要

- 不当实现会导致令牌泄露、账号被冒用、scope 越权。
- 公开客户端（SPA/移动端）必须用 PKCE 防拦截（见 Burp 知识库第 10 篇）。

## ③ 核心概念拆解

- **主要流程**：Authorization Code（最安全，配合 PKCE）、Client Credentials（服务间）、Implicit（已不推荐）。
- **关键角色**：资源拥有者、客户端、授权服务器、资源服务器。
- **Scopes**：授权时申请的权限范围（如 `read:email`），用户可同意/收缩；服务端按 scope 发放与校验令牌。
- **令牌安全**：access token 短期有效，refresh token 轮换（见 Burp 知识库 OAuth 2.1 篇）；用 `state` 防 CSRF；HTTPS 全程。

## ④ 常见误区

- **误区 1**：OAuth 是认证协议。它是授权框架；"用第三方登录"还需在授权后做身份认证（OpenID Connect）。
- **误区 2**：公开客户端能藏密钥。藏不住，必须上 PKCE。
- **误区 3**：scope 申请多少给多少。应最小授权、用户确认、服务端校验。

## ⑤ 一句话小结

OAuth 2.0 用授权码+令牌实现" delegated access"；安全关键在 PKCE、短期令牌+刷新轮换、state 防 CSRF，并用 scope 做最小授权。

*下一篇：Java/Spring Boot Security 实战*

> 参考来源：https://www.digitalocean.com/community/tutorials/an-introduction-to-oauth-2
