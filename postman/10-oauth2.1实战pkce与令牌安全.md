---
title: "OAuth 2.1 实战：PKCE 与令牌安全"
parent: "Postman 接口测试实战知识库"
nav_order: 10
---

# Postman 实战｜OAuth 2.1 实战：PKCE 与令牌安全

OAuth 是开放授权的金标准，而 2.1 把历史坑都补上了。这篇讲最关键的升级点：PKCE 防拦截、刷新令牌轮换、用 state 防 CSRF。

## ① 是什么

**OAuth 2.1** 是 OAuth 2.0 的"安全合订本"，废掉了不安全的隐式授权，强制公共客户端使用 **PKCE**，并推荐刷新令牌轮换。
**PKCE**（发音"pixy"）：在授权码流程里加一个一次性随机值，防止授权码被截后被人冒用。

## ② 为什么重要

- 移动端/单页应用没法安全藏密钥，PKCE 让"没有客户端密钥"也安全。
- 刷新令牌轮换意味着旧令牌一旦被盗用就立即作废，大幅缩小泄露窗口。

## ③ 核心概念拆解

- **Authorization Code + PKCE**：客户端先生成 `code_verifier` 并算出 `code_challenge`；授权端点带 challenge；拿到授权码后用 verifier 换 token。截获授权码的人没有 verifier，换不到 token。
- **刷新令牌轮换**：每次用 refresh token 换 access token 时，服务端发新 refresh token、废止旧的。泄露的旧令牌立刻失效。
- **state 参数防 CSRF**：授权请求带随机 state，回调时校验一致，防止攻击者诱导你发起授权。
- **Postman 配置**：Authorization → OAuth 2.0 → 选 Authorization Code（带 PKCE）→ 填 Auth URL、Token URL、client id，点 Get New Access Token。

## ④ 常见误区

- **误区 1**：公共客户端也能藏 client secret。藏不住，必须上 PKCE。
- **误区 2**：刷新令牌长期有效。应轮换 + 绑定设备/作用域。
- **误区 3**：忽略 state。等于给 CSRF 开门。

## ⑤ 一句话小结

OAuth 2.1 = 强制 PKCE + 刷新令牌轮换 + state 防 CSRF；Postman 的 OAuth 2.0 标签可直接跑通这套流程。

*下一篇：Postman CLI / Newman 与 CI/CD 自动化*

> 参考来源：*Mastering Postman, Second Edition*（本文为原创讲解，非转载原文）
