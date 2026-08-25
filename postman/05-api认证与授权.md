---
title: "API 认证与授权：Basic / API Key / OAuth 2.0"
parent: "Postman 接口测试实战知识库"
nav_order: 5
---

# Postman 实战｜API 认证与授权：Basic / API Key / OAuth 2.0

接口谁都能调就完了。这篇讲三种最常见的"验明正身"方式，以及怎么在 Postman 里配置它们。

## ① 是什么

- **认证（Authentication）**：你是谁（登录）。
- **授权（Authorization）**：你能干什么（权限）。
- 常见机制：**Basic Auth**（账号密码）、**API Key**（固定密钥）、**OAuth 2.0**（令牌授权）。

## ② 为什么重要

- 不认证=任何人都能删库；授权不当=普通用户能调管理员接口。
- Postman 的 Authorization 标签页能一键拼接各种鉴权头，省去手算。

## ③ 核心概念拆解

- **Basic Auth**：把 `用户名:密码` 用 Base64 编码塞进 `Authorization: Basic xxx` 头。简单但不安全，必须配合 HTTPS。
  - Postman：Authorization → Basic Auth → 填 username/password，自动生成头。
- **API Key**：服务端发一个固定密钥，客户端放在 Header（如 `X-API-Key`）或 Query。
  - Postman：Authorization → API Key → 选 Key/Value 位置。
- **OAuth 2.0**：用 access token 调接口，token 有时效、可限权限。Postman 支持 Authorization Code、Client Credentials 等流程，填好 client id/secret 和 token URL 即可自动拿 token。

## ④ 常见误区

- **误区 1**：Basic Auth 明文传密码。必须走 HTTPS，否则被截获即泄露。
- **误区 2**：API Key 放 URL 参数。容易被日志、代理记录，放 Header 更安全。
- **误区 3**：token 永久有效。应设短期 access token + 刷新机制。

## ⑤ 一句话小结

Basic/API Key 适合内部或简单场景，对外开放优先 OAuth 2.0；Postman 的 Authorization 标签能替你拼好鉴权头。

*下一篇：错误处理、限流与 Postman Flows 编排*

> 参考来源：*Mastering Postman, Second Edition*（本文为原创讲解，非转载原文）
