---
title: "CSP 内容安全策略"
parent: "浏览器安全机制"
grand_parent: "Web 安全与开发基础实战知识库"
nav_order: 2
---

# 概念｜CSP 内容安全策略

XSS 防不住时，CSP 是兜底：即使有恶意脚本，也不让它加载执行。

## ① 是什么

**CSP** 是响应头（或 `<meta>`），声明"本页允许从哪些来源加载脚本/样式/图片/连接"，违反策略的资源被浏览器拦截。

## ② 为什么重要

- XSS 是头号客户端漏洞；CSP 能在代码层漏防时阻止外链恶意脚本执行、阻断数据外发。
- 是纵深防御关键一环，而非取代输入校验。

## ③ 核心概念拆解（带片段）

- **指令族**：`default-src`、`script-src`、`style-src`、`img-src`、`connect-src`、`frame-ancestors`。
- **`script-src` 关键**：避免 `unsafe-inline`（允许内联脚本=给 XSS 开后门）；用 nonce/哈希白名单内联可信脚本。
- **策略示例**（收紧脚本来源、禁内联、防框架嵌套）：

```
Content-Security-Policy:
  default-src 'self';
  script-src 'self' 'nonce-abc123';
  object-src 'none';
  frame-ancestors 'none';
  base-uri 'self'
```
- **报告先行**：`Content-Security-Policy-Report-Only` + `report-to` 先收集违规，调优后再强制。

## ④ 常见误区

- CSP 配了就安全？`script-src *` 等于没配。
- 用 `unsafe-inline` 省事？放行内联脚本，大幅削弱防护。
- CSP 替代输入校验？它是兜底，编码仍是根本（见 [DOM XSS 实操](03-domxss实操.md)）。

## ⑤ 一句话小结

CSP 用白名单限制可加载资源来源，尤其收紧 `script-src`、禁用 `unsafe-inline` 并配合 nonce，是 XSS 的强力兜底防线。

*下一篇：[输出编码与 DOM XSS 实战](03-domxss实操.md)*

> 参考来源：https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP
