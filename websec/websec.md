---
title: Web 安全与开发基础实战知识库
nav_order: 7
has_children: true
---

# Web 安全与开发基础实战知识库

> 参考来源：一份综合学习清单（HTTP / TLS / CORS / CSP / 会话 / JWT / OAuth / OWASP Top 10 / 工具 等公开资料，见各篇链接）（本文为原创讲解，非转载原文）

把一份"Web 安全与开发基础"学习清单读薄：从 HTTP 协议、传输加密、会话与浏览器安全机制，到身份认证（JWT/OAuth）、主流标准（OWASP Top 10 / WSTG）与开发安全（Spring/UI5），最后用 Postman/Burp/ZAP 把理论落到实操。
每篇聚焦一两个概念，配类比与常见误区。其中 Postman、Burp、ZAP 已有专属知识库，本库第 17 篇做"工具概览"并链接过去。

**本系列共 17 篇：**

- **基础协议与架构**
  1. [HTTP 客户端/服务器架构](01-http架构.md)
  2. [HTTP 方法与语义](02-http方法.md)
  3. [HTTP 安全响应头（OWASP Secure Headers）](03-http安全响应头.md)
- **传输、会话与缓存**
  4. [Cookie 与会话管理（Secure/HttpOnly/SameSite）](04-cookie与会话.md)
  5. [TLS 握手与 HTTPS](05-tls与https.md)
  6. [Web 缓存与缓存投毒](06-web缓存与投毒.md)
- **浏览器安全机制**
  7. [同源策略与 CORS](07-同源策略与cors.md)
  8. [CSP 内容安全策略](08-csp.md)
  9. [输出编码与 DOM XSS](09-输出编码与domxss.md)
- **身份、授权与标准**
  10. [OWASP Top 10（2021）总览](10-owasp-top10.md)
  11. [OWASP WSTG 测试方法论](11-wstg方法论.md)
  12. [REST 与 OData 服务](12-rest与odata.md)
  13. [UI5/JavaScript 与 MVC 绑定安全](13-ui5与mvc安全.md)
  14. [JWT（含 Scopes）](14-jwt.md)
  15. [OAuth 2.0（含 Scopes）](15-oauth2.md)
  16. [Java/Spring Boot Security 实战](16-spring-security.md)
- **工具**
  17. [安全测试工具概览（Postman / Burp / ZAP）](17-工具概览.md)
