---
title: "CSP 内容安全策略"
parent: "Web 安全与开发基础实战知识库"
nav_order: 8
---

# 浏览器安全｜CSP 内容安全策略

XSS 防不住时，CSP 是兜底：即使有恶意脚本，也不让它加载执行。

## ① 是什么

**CSP（Content Security Policy）** 是响应头（或 `<meta>`），声明"本页允许从哪些来源加载脚本/样式/图片/连接"等。违反策略的资源会被浏览器拦截。

## ② 为什么重要

- XSS 是头号客户端漏洞；CSP 能在代码层漏防时，阻止外链恶意脚本执行、阻断数据外发。
- 是纵深防御的关键一环，而非取代输入校验。

## ③ 核心概念拆解

- **指令族**：`default-src`（默认）、`script-src`、`style-src`、`img-src`、`connect-src`、`frame-ancestors` 等。
- **`script-src` 关键**：避免 `unsafe-inline`（允许内联脚本=给 XSS 开后门）；用 nonce/哈希白名单内联可信脚本。
- **`frame-ancestors`**：替代 `X-Frame-Options` 防点击劫持。
- **报告**：`report-uri`/`report-to` 收集违规，先"仅报告"模式调优再强制。

## ④ 常见误区

- **误区 1**：CSP 配了就安全。配置过宽（`script-src *`）等于没配。
- **误区 2**：用 `unsafe-inline` 省事。这会放行内联脚本，大幅削弱防护。
- **误区 3**：CSP 替代输入校验。它是兜底，输入/输出编码（第 9 篇）仍必须做。

## ⑤ 一句话小结

CSP 用白名单限制可加载的资源来源，尤其收紧 `script-src`、禁用 `unsafe-inline` 并配合 nonce，是 XSS 的强力兜底防线。

*下一篇：输出编码与 DOM XSS*

> 参考来源：https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP
