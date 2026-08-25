---
title: "Java/Spring Boot Security 实战"
parent: "Web 安全与开发基础实战知识库"
nav_order: 16
---

# 开发｜Java/Spring Boot Security 实战

把前面原则落到 Java/Spring Boot：框架替你挡掉很多，但配置错了照样漏。

## ① 是什么

**Spring Security** 是 Spring 生态的安全框架，提供认证、授权、防护（CSRF、CORS、Header）等。它基于**过滤器链（Filter Chain）**，请求依次经过各安全过滤器。

## ② 为什么重要

- 默认安全（如 CSRF 保护、安全头）若被手动关掉或配置宽松，会引入漏洞。
- 理解过滤器链与注解式授权，才能正确实现"最小权限"。

## ③ 核心概念拆解

- **认证与授权**：`AuthenticationManager` 管"你是谁"，`AuthorizationFilter`/`@PreAuthorize` 管"能干什么"。
- **密码存储**：用 `PasswordEncoder`（bcrypt/Argon2）哈希，禁止明文/弱哈希。
- **CSRF 保护**：对状态化（Cookie 会话）应用默认开启；无状态 JWT 方案则要另行设计。
- **方法级安全**：`@PreAuthorize("hasRole('ADMIN')")` 做细粒度授权，别只靠 URL 拦截。
- **CORS/CSP/安全头**：配合（见第 3、7、8 篇）在 Spring 中显式配置。
- **密钥与配置**：把密钥/凭证放配置中心/环境变量，禁用默认口令，关闭多余端点（actuator 等）。

## ④ 常见误区

- **误区 1**：加了 Spring Security 就安全。默认配置仍需按业务收紧（如暴露的 actuator）。
- **误区 2**：只在 URL 层授权。方法级注解才能防内部调用越权。
- **误区 3**：前后端分离就不需要 CSRF。取决于凭证机制（Cookie 会话仍需）。

## ⑤ 一句话小结

Spring Security 用过滤器链统一安全；正确做法是强哈希密码、方法级授权、保留 CSRF/CORS/安全头配置，并把密钥外置。

*下一篇：安全测试工具概览（Postman / Burp / ZAP）*

> 参考来源：https://www.marcobehler.com/guides/spring-security
