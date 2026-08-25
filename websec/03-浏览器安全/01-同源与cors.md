---
title: "同源策略与 CORS"
parent: "浏览器安全机制"
grand_parent: "Web 安全与开发基础实战知识库"
nav_order: 1
---

# 概念｜同源策略与 CORS

浏览器默认不让 A 站脚本读 B 站数据，这道墙叫同源策略；CORS 是"有控制地开窗"。

## ① 是什么

**同源策略（SOP）**：协议+域名+端口相同才"同源"，不同源页面的脚本默认不能读对方响应。**CORS（跨源资源共享）** 是服务器用响应头声明"允许哪些源跨域访问"的机制。

## ② 为什么重要

- SOP 是浏览器安全基石，阻止恶意站点偷读你的数据。
- CORS 配错（过度放行）会直接击穿 SOP，导致跨域数据泄露。

## ③ 核心概念拆解（带示例）

- **同源判定**：`https://a.com` 与 `https://a.com:8080` 不同源（端口不同）。
- **CORS 头**：`Access-Control-Allow-Origin`（允许源）、`Allow-Credentials`（是否带 Cookie）、`Allow-Methods/Headers`。
- **危险配置示例**（反射任意 Origin 且带凭据）：

```
请求：Origin: https://evil.com
响应：Access-Control-Allow-Origin: https://evil.com
      Access-Control-Allow-Credentials: true
```
浏览器会允许 `evil.com` 的脚本读取本站带 Cookie 的响应——等于对所有站点开放。
- **预检（Preflight）**：非简单请求先发 `OPTIONS` 问权限。

## ④ 常见误区

- CORS 是服务器防攻击？错，CORS 由浏览器执行、保护客户端数据；后端仍需自己鉴权。
- `*` 最方便？带凭据时不能用 `*`，应列明确源。
- 前端报 CORS 错是后端 bug？多是不该跨域/未授权跨域，需设计而非绕过。

## ⑤ 一句话小结

同源策略是浏览器默认隔离墙，CORS 是受控开窗；配 CORS 要最小授权、禁止"反射任意源+凭据"，否则击穿隔离。

*下一篇：[CSP 内容安全策略](02-csp.md)*

> 参考来源：https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS
