---
title: "Burp Suite 上手"
parent: "工具实操"
grand_parent: "Web 安全与开发基础实战知识库"
nav_order: 2
---

# 实操（Lab）｜Burp Suite 上手

本 Lab 用 Burp 完成"代理抓包 → 改包 → Repeater 手测 → Intruder 爆破"最小闭环。（更完整见 [Burp 知识库](../../burp/burp.md)）

## 目标

- 浏览器流量过 Burp，能拦截并修改请求。
- 用 Repeater 手测、Intruder 做参数爆破。

## 环境

- 下载 Burp Community：https://portswigger.net/burp/communitydownload，启动。
- 浏览器装 FoxyProxy 或直接在设置里把 HTTP/HTTPS 代理指向 `127.0.0.1:8080`。

## 分步

1. **装 CA 证书**：浏览器访问 `http://burp` → 下载 CA 证书 → 导入"受信任的根证书颁发机构"，否则 HTTPS 看不到明文。
2. **拦截**：Burp `Proxy` → `Intercept` 开 `On`；浏览器访问目标，请求会卡住。
3. **改包**：在拦截里改参数（如 `id=1001`→`id=1002`），点 `Forward` 放行，观察响应差异（测 IDOR）。
4. **Repeater 手测**：右键请求 → `Send to Repeater`；在 `Repeater` 里反复改/发，对比响应。
5. **Intruder 爆破**：右键 → `Send to Intruder`；`Positions` 标 `id` 为 payload 位（Sniper）；`Payloads` 载入字典 → `Start attack`，看长度/状态码差异找异常。
6. **关拦截**：不需要时把 Intercept 设 `Off`，否则页面打不开。

## 现象与结论

- 站中间人后能精确改每个参数，是手测越权/注入的核心手段。
- Repeater 用于精细单点，Intruder 用于批量枚举；二者都不替代逻辑思考。

> 参考来源：https://portswigger.net/burp/documentation/desktop/tutorials
