---
title: "CSP 内容安全策略"
parent: "浏览器安全机制"
grand_parent: "Web 安全与开发基础实战知识库"
nav_order: 2
---

# CSP 内容安全策略

## 一句话定义
XSS 防不住时，CSP 是兜底：即使有恶意脚本，也不让它加载执行。用白名单限制可加载资源来源，尤其收紧 `script-src`、禁用 `unsafe-inline` 并配合 nonce，是 XSS 的强力兜底防线。

## 核心架构 / 工作原理

```mermaid
graph TD
  A[CSP 指令族] --> B[资源加载控制]
  B --> B1[default-src: 兜底]
  B --> B2[script-src: 脚本来源(最关键)]
  B --> B3[style-src: 样式来源]
  B --> B4[img-src: 图片来源]
  B --> B5[connect-src: fetch/XHR/WS 连接目标]
  B --> B6[font-src/object-src/media-src/frame-src...]
  
  A --> C[文档/导航控制]
  C --> C1[base-uri: <base> 标签限制]
  C --> C2[form-action: 表单提交目标]
  C --> C3[frame-ancestors: 允许嵌套的父页面(替代 X-Frame-Options)]
  
  A --> D[报告与模式]
  D --> D1[Content-Security-Policy: 强制模式(拦截+报告)]
  D --> D2[Content-Security-Policy-Report-Only: 仅报告(调优用)]
  D --> D3[report-to / report-uri: 违规上报端点]
```

| 关键指令 | 推荐值 | 说明 |
|----------|--------|------|
| `default-src` | `'self'` | 兜底：同源 |
| `script-src` | `'self' 'nonce-<random>'` | **核心**：禁 `unsafe-inline`，用 nonce/哈希白名单内联 |
| `style-src` | `'self' 'nonce-<random>'` | 同理，禁 `unsafe-inline` |
| `img-src` | `'self' data: https:` | 允许 data URI 和 HTTPS 图片 |
| `connect-src` | `'self' https://api.example.com` | 控制 fetch/XHR/WebSocket 目标 |
| `frame-ancestors` | `'none'` 或 `'self'` | 反点击劫持，替代 X-Frame-Options |
| `base-uri` | `'self'` | 防 `<base href="evil.com">` 劫持相对链接 |
| `object-src` | `'none'` | 禁 Flash/插件(已废弃但防老漏洞) |

## 快速上手步骤

1. **报告先行调优 (Report-Only)**：
   ```http
   Content-Security-Policy-Report-Only:
     default-src 'self';
     script-src 'self' 'unsafe-inline';  <- 先允许内联收集违规
     report-to csp-endpoint;
   ```
   - 观察违规报告 → 逐步收紧 → 移除 `unsafe-inline` → 上 nonce/哈希
2. **正式策略示例**：
   ```http
   Content-Security-Policy:
     default-src 'self';
     script-src 'self' 'nonce-abc123def456';
     style-src 'self' 'nonce-abc123def456';
     img-src 'self' data: https:;
     connect-src 'self' https://api.example.com;
     font-src 'self';
     object-src 'none';
     frame-ancestors 'none';
     base-uri 'self';
     form-action 'self';
   ```
   - 服务端每响应生成随机 nonce → 模板 `<script nonce="{{nonce}}">` → CSP 带同 nonce
3. **Nginx 配置**：
   ```nginx
   add_header Content-Security-Policy "default-src 'self'; script-src 'self' 'nonce-$request_id'; ..." always;
   ```
4. **验证**：
   ```bash
   curl -I https://target.com/ | grep -i content-security-policy
   # 或浏览器 DevTools -> Console 看 CSP 违规报告
   ```

## 踩坑避坑指南

| 场景 | 问题现象 | 原因 | 解决/最佳实践 |
|------|----------|------|---------------|
| CSP 配了以为安全 | `script-src *` 等于没配 | 策略过宽 | **最小授权**：`default-src 'self'`；脚本/样式用 nonce/哈希 |
| 用 `unsafe-inline` 省事 | 放行内联脚本，大幅削弱防护 | 不想改模板加 nonce | **必须用 nonce/哈希**；模板引擎支持自动注入 nonce |
| CSP 替代输入校验 | 它是兜底，编码仍是根本 | 误以为 CSP 万能 | **编码是根本，CSP 是兜底**；两者叠加(见 DOM XSS 篇) |
| `Report-Only` 久不转正式 | 违规日志堆积不处理 | 缺收敛流程 | **设定截止日期**：收集 1-2 周 → 清理违规 → 转正式 |
| 第三方脚本/分析工具被拦 | 业务指标丢失/功能挂 | 策略未含第三方域 | **显式加第三方域**到 `script-src/connect-src`；或用子资源完整性 SRI |

## 替代方案对比

| 维度 | CSP | 输出编码 | WAF | 代码审计/SAST |
|------|-----|----------|-----|---------------|
| 防御层 | 浏览器执行层(兜底) | 代码根治层 | 流量特征匹配 | 静态分析层 |
| XSS 覆盖 | 反射/存储/DOM(限制加载) | 反射/存储/DOM(根治输出) | 反射/存储(特征匹配) | 全类型(模式匹配) |
| 部署成本 | 中(需改模板/配 nonce) | 高(全输出点编码) | 中(规则维护) | 高(工具/人工) |
| 误报/误拦 | 策略过严报错/功能挂 | 无(若编码正确) | 有(规则误判) | 低(模式匹配) |
| 维护 | 中(新功能加域名) | 高(新输出点需编码) | 高(规则更新) | 中 |

---

> 参考来源：https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP

*下一篇：[输出编码与 DOM XSS 实战](03-domxss实操.md)*