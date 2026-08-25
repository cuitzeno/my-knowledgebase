---
title: "HTTP 安全响应头（OWASP Secure Headers）"
parent: "协议与架构"
grand_parent: "Web 安全与开发基础实战知识库"
nav_order: 3
---

# 速查｜HTTP 安全响应头（OWASP Secure Headers）

很多防护不用改代码，只要在响应里加对头。下方为按需勾选的清单与推荐值。

## 必配清单

| 响应头 | 推荐值 | 作用 | 防 |
|---|---|---|---|
| `Strict-Transport-Security` | `max-age=63072000; includeSubDomains; preload` | 强制 HTTPS | SSL Strip 降级 |
| `Content-Security-Policy` | 见 [CSP 篇](../03-浏览器安全/02-csp.md) | 限制资源来源 | XSS |
| `X-Content-Type-Options` | `nosniff` | 禁止 MIME 嗅探 | MIME 嗅探 XSS |
| `X-Frame-Options` | `DENY` 或 `SAMEORIGIN` | 禁止被 iframe 嵌套 | 点击劫持 |
| `Referrer-Policy` | `strict-origin-when-cross-origin` | 控制 Referer 泄露 | 信息泄露 |
| `Permissions-Policy` | 按需关闭敏感 API（如 `camera=()`） | 限制浏览器特性 | 滥用设备能力 |

> 新项目可直接用 `Content-Security-Policy` 的 `frame-ancestors` 替代 `X-Frame-Options`（二者并存更稳）。

## 示例（Nginx）

```nginx
add_header Strict-Transport-Security "max-age=63072000; includeSubDomains; preload" always;
add_header X-Content-Type-Options "nosniff" always;
add_header X-Frame-Options "DENY" always;
add_header Referrer-Policy "strict-origin-when-cross-origin" always;
```

## 常见误区

- 有 HTTPS 就够？HSTS 才防止首次/后续降级。
- CSP 配了就万事大吉？`default-src *` 等于没配。
- 靠框架默认头？很多默认缺失或宽松，需显式加固。

## 一句话小结

安全响应头是"零代码改动"的低成本防护；按 OWASP Secure Headers 清单补齐 HSTS/CSP/nosniff/anti-frame 等，挡掉一大类攻击。

> 参考来源：https://owasp.org/www-project-secure-headers/
