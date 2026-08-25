---
title: "输出编码与 DOM XSS"
parent: "Web 安全与开发基础实战知识库"
nav_order: 9
---

# 浏览器安全｜输出编码与 DOM XSS

XSS 的根因常是"把不可信数据当代码渲染"。输出编码是治本，DOM XSS 则考验浏览器内链路。

## ① 是什么

**输出编码（Output Encoding）**：在把数据插入 HTML/JS/URL 上下文前，按上下文转义（如 `<`→`&lt;`），让它被当作"数据"而非"代码"。
**DOM XSS**：漏洞与利用都发生在**浏览器端 JS**——不可信数据（如 URL 片段）被 JS 读入并写入危险"接收器"（sink，如 `innerHTML`、`eval`），服务器从未见过该载荷。

## ② 为什么重要

- 不编码，用户输 `"><script>` 就能在别人浏览器执行脚本（偷 Cookie、钓鱼、蠕虫）。
- DOM XSS 绕过了传统"服务端过滤"思路，必须从源头（source）到接收器（sink）在客户端拦截。

## ③ 核心概念拆解

- **上下文相关编码**：HTML 体、属性、JS 字符串、URL 各自有不同的转义规则，套错等于没转义。
- **source→sink 链路**：`location.hash`、`document.URL` 等是 source；`innerHTML`、`outerHTML`、`eval`、`setTimeout(string)` 是危险 sink。
- **DOM Invader / 浏览器内分析**：用 Burp 内置浏览器追 source→sink（见 Burp 知识库第 10 篇）。
- **与输出编码协同**：服务端模板转义 + 客户端避免危险 sink / 用 `textContent` 而非 `innerHTML`。

## ④ 常见误区

- **误区 1**：服务端过滤了就安全。DOM XSS 数据可能只在客户端流动，服务器从没见过。
- **误区 2**：转义一次通用。不同上下文需不同编码规则。
- **误区 3**：CSP 替代编码。CSP 是兜底，编码才是根本。

## ⑤ 一句话小结

XSS 治本是"按上下文输出编码"；DOM XSS 要追浏览器内 source→sink 链路，避免危险接收器——这是 OWASP 强调的"Secure Programming: Output Encoding"。

*下一篇：OWASP Top 10（2021）总览*

> 参考来源：https://owasp.org/www-community/attacks/DOM_Based_XSS
