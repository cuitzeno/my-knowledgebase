---
title: "UI5/JavaScript 与 MVC 绑定安全"
parent: "服务与开发安全"
grand_parent: "Web 安全与开发基础实战知识库"
nav_order: 2
---

# UI5/JavaScript 与 MVC 绑定安全

## 一句话定义
前端框架(如 SAPUI5)用数据绑定把模型渲染到视图。绑定若不当，会把不可信数据直接变成代码执行。**输出编码是默认防线，但 `innerHTML`/HTML 控件会绕过；授权决策永远放服务端，用户输入须净化**。

## 核心架构 / 工作原理

```mermaid
graph TD
  A[MVC 绑定流] --> B[Model (数据/状态)]
  B --> C[Binding (单向/双向/表达式)]
  C --> D[View (XML/HTML/JS 模板/控件)]
  D --> E[渲染输出]
  
  A --> F[安全风险点]
  F --> F1[表达式拼接不可信数据: {path: 'userInput', formatter: '.dangerousFormatter'}]
  F --> F2[HTML 渲染控件: sap.m.FormattedText / sap.ui.core.HTML / innerHTML]
  F --> F3[客户端授权判断: visible="{= ${model>/role} === 'admin' }"]
  F --> F4[敏感数据进前端模型: 密码/Token/内部 ID 存 JSONModel]
  
  A --> G[Securing Apps 要点]
  G --> G1[输出编码默认开启: 文本绑定自动 HTML 编码]
  G --> G2[HTML 控件需显式净化: DOMPurify / sap.ui.core.util.sanitize]
  G --> G3[授权决策仅服务端: 前端隐藏≠权限控制]
  G --> G5[敏感数据不进前端: 密码/Token/Key 仅后端持有]
  G --> G6[CSP/Trusted Types 兜底: 见浏览器安全组]
```

| 绑定场景 | 默认行为 | 风险 | 修复 |
|----------|----------|------|------|
| 文本绑定 `<Text text="{/userName}">` | 自动 HTML 编码 | 低 | 无需额外处理 |
| 格式化文本 `<FormattedText htmlText="{/userBio}">` | **直接渲染 HTML** | **高 (XSS)** | DOMPurify 净化 / 禁用 HTML / 用纯文本控件 |
| 表达式绑定 `visible="{= ${/role} === 'admin' }"` | 客户端求值 | 授权绕过(前端可改模型) | **服务端返回可见性标记** / 仅做 UI 提示 |
| 双向绑定 `value="{/password}"` | 模型同步输入 | 敏感数据驻留前端 | **敏感字段勿双向绑定** / 输入即发后端不存模型 |

## 快速上手步骤

1. **审计模板/控件**：
   - 搜 `FormattedText` `sap.ui.core.HTML` `innerHTML` `htmlText` `dangerousFormatter`
   - 确认每处 HTML 渲染源：是否受信/已净化
2. **净化 HTML 输入**：
   ```javascript
   // SAPUI5 推荐 DOMPurify
   import DOMPurify from 'dompurify';
   const cleanHtml = DOMPurify.sanitize(dirtyHtml, {ALLOWED_TAGS: ['b','i','u','a']});
   // 或用框架内置(若有)
   // sap.ui.core.util.sanitize.html(dirtyHtml);
   ```
3. **移除客户端授权判断**：
   ```xml
   <!-- 危险: 前端判断角色 -->
   <Button visible="{= ${/userModel/role} === 'admin' }" ...>
   
   <!-- 安全: 服务端返回 isAdminVisible 标记 -->
   <Button visible="{/authModel/isAdminVisible}" ...>
   ```
4. **敏感数据不进前端模型**：
   - 登录响应只返回 `access_token` → 存内存/HttpOnly Cookie，**勿存 JSONModel**
   - 密码/旧密码/OTP 等：输入即发后端，`onSubmit` 后立即清空输入框模型值
5. **配置 CSP + Trusted Types**：见 [CSP 篇](../03-浏览器安全/02-csp.md) + [DOM XSS 篇](../03-浏览器安全/03-domxss实操.md)

## 踩坑避坑指南

| 场景 | 问题现象 | 原因 | 解决/最佳实践 |
|------|----------|------|---------------|
| 以为框架自动安全 | 默认编码能挡大部分，但 `innerHTML`/HTML 控件仍会绕过 | 过度信任框架 | **显式审计所有 HTML 渲染点**；配置 ESLint 规则禁 `innerHTML`/`htmlText` |
| 前端隐藏字段=权限控制 | `visible="{= ${/role}==='admin' }"` 可被前端绕过 | 授权前置 | **服务端返回可见性/权限标记**；前端仅做 UI 提示 |
| 只用 `textContent` 等价物就够 | 第三方富文本/HTML 渲染场景仍需渲染 HTML | 业务需求 | **DOMPurify 白名单净化** + **Trusted Types 强制** + **CSP 兜底** |
| 敏感数据存前端模型 | `JSONModel` 含 Token/密码/内部 ID → DevTools 可见/内存泄露 | 图省事 | **Token 仅内存/ HttpOnly Cookie**；密码/OTP 输入即发即清 |
| 双向绑定敏感字段 | `<Input value="{/password}"/>` 模型驻留明文 | 双向绑定机制 | **敏感字段单向绑定/受控组件**；提交即清模型值 |

## 替代方案对比

| 维度 | SAPUI5 / OpenUI5 | React | Vue 3 | Angular |
|------|------------------|-------|-------|---------|
| 默认输出编码 | 文本绑定✅ / HTML控件❌ | JSX 自动编码✅ / dangerouslySetInnerHTML❌ | 插值 `{{}}` 编码✅ / v-html❌ | 插值编码✅ / innerHTML❌ |
| HTML 净化 | DOMPurify / 内置 sanitize | DOMPurify / sanitize-html | DOMPurify / vue-sanitize | DomSanitizer |
| 客户端授权风险 | 表达式绑定易绕过 | 条件渲染易绕过 | v-if/v-show 易绕过 | *ngIf 易绕过 |
| Trusted Types 支持 | 需配合 CSP | 原生支持 | 原生支持 | 原生支持 |
| 生态成熟度 | 企业级/长期支持 | 极高 | 高 | 高 |

---

> 参考来源：https://sapui5.hana.ondemand.com/#/topic/ec699e0817fb46a0817b0fa276a249f8 · https://sapui5.hana.ondemand.com/#/topic/91f3d8706f4d1014b6dd926db0e91070

*下一篇：[Java/Spring Boot Security 实战](03-spring-security.md)*