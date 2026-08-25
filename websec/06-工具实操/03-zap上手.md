---
title: "OWASP ZAP 上手"
parent: "工具实操"
grand_parent: "Web 安全与开发基础实战知识库"
nav_order: 3
---

# 实操（Lab）｜OWASP ZAP 上手

本 Lab 用 ZAP 完成"代理 → 爬取 → 主动扫描 → 看告警"最小闭环。（更完整见 [ZAP 知识库](../../zap/zap.md)）

## 目标

- 用 ZAP 自动发现接口并扫出常见漏洞。
- 读懂告警并区分误报。

## 环境

- 下载 ZAP：https://www.zaproxy.org/，启动（选持久/临时会话均可）。

## 分步

1. **配代理**：ZAP 默认监听 `127.0.0.1:8080`；浏览器代理指过去（同 [Burp 上手](02-burp上手.md)）。或直接在 ZAP 内用 `Quick Start` → `Automated Scan` 填目标 URL。
2. **爬取（Spider）**：`Sites` 树右键目标 → `Attack` → `Spider`，让 ZAP 顺链发现端点。
3. **主动扫描（Active Scan）**：右键目标 → `Attack` → `Active Scan`；适度设强度，避免打挂目标。
4. **看告警**：`Alerts` 标签页按风险（High/Medium/Low）列出；点开看请求/响应证据与修复建议。
5. **被动扫描**：你正常浏览时 ZAP 也会静默分析，无需主动攻击即可发现部分问题。
6. **导出**：`Report` → 生成 HTML/JSON 交付物。

## 现象与结论

- ZAP 适合"先广扫一遍"建立资产面与初步风险清单。
- 告警含误报，需结合 [WSTG](../04-身份授权标准/02-wstg.md) 与人工（Burp Repeater）复核。

> 参考来源：https://www.zaproxy.org/
