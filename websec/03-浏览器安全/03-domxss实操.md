---
title: "输出编码与 DOM XSS 实战"
parent: "浏览器安全机制"
grand_parent: "Web 安全与开发基础实战知识库"
nav_order: 3
---

# 实操（Lab）｜输出编码与 DOM XSS

XSS 的根因是"把不可信数据当代码渲染"。本 Lab 用一段漏洞代码 + Burp DOM Invader 复现 DOM XSS，体会 source→sink 链路。

## 目标

- 理解 DOM XSS 与反射/存储 XSS 的区别（载荷只在浏览器内流动，服务器从没见过）。
- 用 Burp 内置浏览器的 DOM Invader 找出 source→sink。

## 环境

- 任意含如下前端代码的页面（或实验室如 PortSwigger Web Security Academy 的 DOM XSS 题）。
- Burp Suite Community（见 [Burp 上手](../06-工具实操/02-burp上手.md)）。

## 漏洞代码（示例）

```html
<!-- 危险：把 URL 片段直接写进页面 -->
<script>
  var name = location.hash.slice(1);
  document.getElementById("greet").innerHTML = "Hello " + name;
</script>
<div id="greet"></div>
```

`innerHTML` 是**危险 sink**，`location.hash` 是**污染 source**。

## 分步

1. 浏览器配置为通过 Burp 代理（见 [Burp 上手](../06-工具实操/02-burp上手.md)），并开启 **DOM Invader**（Settings → DOM Invader → Enable）。
2. 访问 `vulnerable.com/#<img src=x onerror=alert(1)>`。
3. 在 DOM Invader 面板查看 **Sources**（来自 `location.hash`）与 **Sinks**（流入 `innerHTML` 的链路）。
4. 触发后观察弹窗/控制台，确认利用成立。
5. 修复：改用 `textContent` 而非 `innerHTML`，或对接入值做编码/白名单。

## 现象与结论

- 弹窗出现即证明：不可信数据经 source 流入危险 sink 即执行——这就是 DOM XSS。
- **治本**：按上下文输出编码；避免危险 sink；必要时用 CSP 兜底（见 [CSP 篇](02-csp.md)）。

> 参考来源：https://owasp.org/www-community/attacks/DOM_Based_XSS
