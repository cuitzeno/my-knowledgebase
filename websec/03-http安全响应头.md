---
title: "HTTP 安全响应头（OWASP Secure Headers）"
parent: "Web 安全与开发基础实战知识库"
nav_order: 3
---

# Web 基础｜HTTP 安全响应头（OWASP Secure Headers）

很多防护不用改代码，只要在响应里加对 HTTP 头。OWASP Secure Headers 项目给出了一套推荐清单。

## ① 是什么

**安全响应头** 是服务器在响应里返回的指令，告诉浏览器"该怎么对待这个页面"。常见：`Content-Security-Policy`、`Strict-Transport-Security`、`X-Content-Type-Options`、`X-Frame-Options`、`Referrer-Policy`、`Permissions-Policy` 等。

## ② 为什么重要

- 正确配置头能挡掉一大批 XSS、点击劫持、MIME 嗅探、降级攻击。
- 缺失头不是"功能问题"，而是明确的安全短板，扫描器与合规都会查。

## ③ 核心概念拆解

- **HSTS（Strict-Transport-Security）**：强制后续用 HTTPS，防 SSL Strip 降级。
- **CSP（见第 8 篇）**：限制可加载资源的来源，抗 XSS。
- **X-Content-Type-Options: nosniff**：禁止浏览器猜测 MIME 类型，防 MIME 嗅探 XSS。
- **X-Frame-Options / CSP frame-ancestors**：禁止被 iframe 嵌套，抗点击劫持。
- **Referrer-Policy**：控制 `Referer` 泄露多少路径信息。
- **Permissions-Policy**：限制摄像头/麦克风等敏感 API 可用性。

## ④ 常见误区

- **误区 1**：有 HTTPS 就够。HSTS 才防止首次/后续降级。
- **误区 2**：CSP 配了就万事大吉。配置过宽（`default-src *`）等于没配。
- **误区 3**：靠框架默认头。很多默认缺失或宽松，需显式加固。

## ⑤ 一句话小结

安全响应头是"零代码改动"的低成本防护；按 OWASP Secure Headers 清单补齐 HSTS/CSP/nosniff/anti-frame 等，能挡掉一大类攻击。

*下一篇：Cookie 与会话管理（Secure/HttpOnly/SameSite）*

> 参考来源：https://owasp.org/www-project-secure-headers/
