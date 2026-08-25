---
title: "用 Postman 调 OAuth2 接口"
parent: "身份、授权与标准"
grand_parent: "Web 安全与开发基础实战知识库"
nav_order: 6
---

# 实操（Lab）｜用 Postman 调一个需 OAuth2 的 API

理完 OAuth 2.0 概念，动手用 Postman 拿 token 再调受保护接口，体会 scope 与令牌流转。

## 目标

- 在 Postman 里走完 Authorization Code（或 Client Credentials）拿 access token。
- 用 token 调用需鉴权的接口，并验证 scope 限制。

## 环境

- Postman（免费版即可，无需账号，见 [Postman 上手](../06-工具实操/01-postman上手.md)）。
- 一个支持 OAuth2 的测试 API（如 GitHub API，或本地授权服务器）。

## 分步（以 GitHub 为例，Authorization Code 简化示意）

1. 在 GitHub → Settings → Developer settings 建一个 OAuth App，拿到 `client_id`、`client_secret`、`redirect_uri`。
2. Postman 新建请求 `GET https://api.github.com/user`。
3. 切到 **Authorization** 标签 → Type 选 **OAuth 2.0** → 点 **Get New Access Token**。
4. 填：Grant Type=`Authorization Code`、Auth URL、Access Token URL、`client_id`、`client_secret`、`scope=read:user`、`state` 随机值 → 浏览器登录授权 → 拿到 token。
5. 选该 token → Send。响应返回当前用户信息即成功。
6. 改 `scope` 为更小范围重试，观察某些端点返回 403——这就是 scope 在起作用。

## 现象与结论

- token 随请求以 `Authorization: Bearer <token>` 携带；缺失/越权 scope 会被拒。
- 真实集成常用 **Client Credentials**（服务间）或把 token 存环境/集合变量复用；敏感 secret 勿入库。

> 参考来源：https://learning.postman.com/docs/getting-started/introduction/
