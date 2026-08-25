---
title: "OAuth 2.0（含 Scopes）"
parent: "身份、授权与标准"
grand_parent: "Web 安全与开发基础实战知识库"
nav_order: 5
---

# 概念｜OAuth 2.0（含 Scopes）

OAuth 2.0 解决"授权第三方访问"的问题，是现代登录/对接的事实标准。

## ① 是什么

**OAuth 2.0** 是授权框架：资源拥有者通过"授权"让第三方应用代表自己访问资源，而不把密码交给第三方。核心是**访问令牌（access token）** + **授权码流程**。

## ② 为什么重要

- 不当实现会导致令牌泄露、账号冒用、scope 越权。
- 公开客户端（SPA/移动端）必须用 PKCE 防拦截（见 [Burp OAuth 篇](../../burp/10-客户端攻击.md) 与 [JWT 篇](03-jwt.md)）。

## ③ 核心概念拆解（带流程）

- **Authorization Code + PKCE 流程**：

```
1) 浏览器 → 授权服务器: GET /authorize?response_type=code&client_id=...&redirect_uri=...&scope=read:email&state=xyz&code_challenge=...
2) 用户登录并同意 scope
3) 授权服务器 → redirect_uri?code=AUTHCODE&state=xyz
4) 客户端用 AUTHCODE + code_verifier 换 token: POST /token → {access_token, refresh_token, scope}
```

- **关键角色**：资源拥有者、客户端、授权服务器、资源服务器。
- **Scopes**：授权时申请的权限范围（如 `read:email`），用户可同意/收缩；服务端按 scope 发放与校验令牌。
- **令牌安全**：access token 短期有效，refresh token 轮换（见 [Burp OAuth 2.1 篇](../../burp/10-客户端攻击.md)）；`state` 防 CSRF；全程 HTTPS。

## ④ 常见误区

- OAuth 是认证协议？它是授权框架；"用第三方登录"还需授权后做身份认证（OpenID Connect）。
- 公开客户端能藏密钥？藏不住，必须上 PKCE。
- scope 申请多少给多少？应最小授权、用户确认、服务端校验。

## ⑤ 一句话小结

OAuth 2.0 用授权码+令牌实现"delegated access"；安全关键在 PKCE、短期令牌+刷新轮换、state 防 CSRF，并用 scope 做最小授权。

*下一篇：[用 Postman 调 OAuth2 接口](06-postman调oauth2.md)*

> 参考来源：https://www.digitalocean.com/community/tutorials/an-introduction-to-oauth-2
