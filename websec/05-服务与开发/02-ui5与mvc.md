---
title: "UI5/JavaScript 与 MVC 绑定安全"
parent: "服务与开发安全"
grand_parent: "Web 安全与开发基础实战知识库"
nav_order: 2
---

# 概念｜UI5/JavaScript 与 MVC 绑定安全

前端框架（如 SAPUI5）用数据绑定把模型渲染到视图。绑定若不当，会把不可信数据直接变成代码执行。

## ① 是什么

**SAPUI5** 是 MVC 框架：Model（数据）→ View（XML/HTML 模板）→ Controller（逻辑），通过**数据绑定**把模型字段显示到控件。其 "Securing Apps" 主题强调客户端安全实践。

## ② 为什么重要

- 绑定表达式或模板若拼接不可信数据，可能触发 XSS（尤其 DOM XSS，见 [DOM XSS 实操](../03-浏览器安全/03-domxss实操.md)）。
- 前端"隐藏"字段并不安全，敏感逻辑/鉴权必须放服务端。

## ③ 核心概念拆解

- **输出编码是默认防线**：UI5 绑定渲染通常对文本做编码；但使用 `innerHTML` 类 API、或 `formattedText` 等会渲染 HTML 的控件时，需明确净化（sanitize）。
- **危险模式**：把用户输入拼进绑定表达式、用 `innerHTML` 注入、在客户端做权限判断。
- **Securing Apps 要点**：不在客户端做授权决策；对第三方/用户内容做净化；避免把敏感数据塞进前端模型；对路由/组件做输入校验。
- **MVC 绑定**：区分单向/双向绑定，警惕"模型变→视图自动重渲染"中被注入恶意标记。

## ④ 常见误区

- 框架自动安全？默认编码能挡大部分，但 `innerHTML`/HTML 控件仍会绕过。
- 前端隐藏字段=权限控制？必须用服务端鉴权。
- 只用 `textContent` 等价物就够？第三方富文本/HTML 渲染仍需净化。

## ⑤ 一句话小结

UI5/MVC 绑定默认有输出编码护体，但 HTML 渲染控件与表达式拼接会绕过；授权决策永远放服务端，用户输入须净化。

*下一篇：[Java/Spring Boot Security 实战](03-spring-security.md)*

> 参考来源：https://sapui5.hana.ondemand.com/#/topic/ec699e0817fb46a0817b0fa276a249f8 · https://sapui5.hana.ondemand.com/#/topic/91f3d8706f4d1014b6dd926db0e91070
