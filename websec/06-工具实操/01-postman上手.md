---
title: "Postman 上手"
parent: "工具实操"
grand_parent: "Web 安全与开发基础实战知识库"
nav_order: 1
---

# 实操（Lab）｜Postman 上手

本 Lab 用 Postman 完成"建集合 → 设变量 → 写测试 → 串 OAuth2"，把接口调试跑通。（更完整见 [Postman 知识库](../../postman/postman.md)）

## 目标

- 创建一个集合，用环境变量管理 base URL 与 token。
- 写一个断言测试脚本，跑通请求链。

## 环境（无需账号）

- 下载安装 Postman：https://www.postman.com/downloads/；或用 Web 版。免费版即可。

## 分步

1. **建集合**：左侧 `Collections` → `New Collection` → 命名 `WebSec-Lab`。
2. **设环境**：`Environments` → `Add` → 加变量 `baseUrl=https://api.github.com`；切到该环境（右上角）。
3. **建请求**：在集合里 `Add Request`，命名 `Get User`，填 `GET {{baseUrl}}/user`。
4. **加鉴权**：切 `Authorization` → `Bearer Token` → Token 填 `{{token}}`（先留空，后面用 OAuth2 篇拿）。
5. **写测试脚本**（请求 `Tests` 标签）：

```javascript
pm.test("状态码 200", () => pm.response.to.have.status(200));
pm.test("返回 login 字段", () => pm.expect(pm.response.json().login).to.be.a('string'));
// 把 token 存到环境，供后续请求复用
const t = pm.response.json().token; if (t) pm.environment.set("token", t);
```

6. **运行**：`Send`。绿勾即通过；`token` 变量被自动保存。
7. 用 `Collection Runner` 批量跑多个请求，验证整条链。

## 现象与结论

- 环境/集合变量让你在不同环境（dev/prod）间切换零改动请求。
- `Tests` 脚本把"人工看响应"变成"自动断言"，是后续接 CI 的基础（见 Postman 知识库 CI/CD 篇）。

> 参考来源：https://learning.postman.com/docs/getting-started/introduction/
