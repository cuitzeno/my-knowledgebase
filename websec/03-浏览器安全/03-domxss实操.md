---
title: "输出编码与 DOM XSS 实战"
parent: "浏览器安全机制"
grand_parent: "Web 安全与开发基础实战知识库"
nav_order: 3
---

# 输出编码与 DOM XSS 实战

## 一句话定义
XSS 的根因是"把不可信数据当代码渲染"。DOM XSS 载荷只在浏览器内流动(服务器从没见过)，用 **Burp DOM Invader** 追踪 `Source → Sink` 链路，修复靠**按上下文输出编码** + 避免危险 Sink。

## 核心架构 / 工作原理

```mermaid
graph LR
  A[DOM XSS 攻击链] --> B[Source 污染源]
  B --> B1[location.hash/search/href]
  B --> B2[document.referrer]
  B --> B3[document.cookie/localStorage]
  B --> B4[postMessage 数据]
  
  A --> C[Propagation 传播/转换]
  C --> C1[字符串拼接/模板渲染]
  C --> C2[DOM API 操作]
  
  A --> D[Sink 危险接收器]
  D --> D1[innerHTML/outerHTML]
  D --> D2[document.write/writeln]
  D --> D3[eval/Function/setTimeout/setInterval]
  D --> D4[location.href/assign/replace]
  D --> D5[jQuery.html()/append()/$.parseHTML()]
  
  A --> E[修复策略]
  E --> E1[避免危险 Sink: 用 textContent 代替 innerHTML]
  E --> E2[按上下文编码: HTML/JS/URL/CSS 编码函数]
  E --> E3[CSP 兜底: script-src nonce/哈希]
  E --> E4[可信类型 Trusted Types: 浏览器原生强制]
```

| 类别 | Source 示例 | Sink 示例 | 修复 |
|------|-------------|-----------|------|
| **HTML 注入** | `location.hash` | `element.innerHTML` | `textContent` / DOMPurify |
| **JS 执行** | `location.search` | `eval()` / `new Function()` | 避免 eval / CSP `script-src` |
| **URL 跳转** | `location.hash` | `location.href = ...` | 白名单校验 URL scheme |
| **DOM 属性** | `referrer` | `img.src = ...` | URL 编码 / 白名单 |
| **存储型** | `localStorage.getItem()` | `innerHTML` | 存时编码 / 取时净化 |

## 快速上手步骤

1. **环境准备**：
   - 含漏洞页面(如 PortSwigger Web Security Academy DOM XSS 题)
   - Burp Suite Community/Pro → Settings → DOM Invader → Enable
2. **复现 DOM XSS**：
   - 浏览器配置 Burp 代理 → 访问 `vulnerable.com/#<img src=x onerror=alert(1)>`
   - DOM Invader 面板查看 **Sources**(红=可控) → **Sinks** → **Propagation** 链路
   - 点击 **Generate payload** → 观察弹窗/控制台 → 确认利用成立
3. **代码级修复**：
   ```javascript
   // 危险
   document.getElementById("greet").innerHTML = "Hello " + location.hash.slice(1);
   
   // 修复 1: textContent (仅文本)
   document.getElementById("greet").textContent = "Hello " + location.hash.slice(1);
   
   // 修复 2: DOMPurify (需渲染 HTML)
   import DOMPurify from 'dompurify';
   element.innerHTML = DOMPurify.sanitize(userInput);
   
   // 修复 3: Trusted Types (现代浏览器原生强制)
   // 需配合 CSP: trusted-types myPolicy
   const policy = trustedTypes.createPolicy('myPolicy', {
     createHTML: (s) => DOMPurify.sanitize(s)
   });
   element.innerHTML = policy.createHTML(userInput);
   ```
4. **配合 CSP 兜底**：见 [CSP 篇](02-csp.md) → `script-src 'nonce-xxx'` + `trusted-types myPolicy`

```bash
# 快速检查页面是否启用 Trusted Types
curl -I https://target.com/ | grep -i content-security-policy
# 看是否含 trusted-types 指令
```

## 踩坑避坑指南

| 场景 | 问题现象 | 原因 | 解决/最佳实践 |
|------|----------|------|---------------|
| 以为 CSP 配了就安全 | CSP 只限制加载，不阻止内联执行/已加载脚本内的逻辑 | CSP 是兜底非根治 | **编码是根本，CSP 是兜底**；需结合输出编码/Trusted Types |
| 只用 `textContent` 以为够 | 富文本/HTML 渲染场景无法用 | 业务需渲染 HTML | **DOMPurify 净化** + **Trusted Types 强制**；配置 CSP `trusted-types` |
| 前端框架自动安全 | React `dangerouslySetInnerHTML` / Vue `v-html` 仍危险 | 框架只做默认编码 | **显式净化**：React 用 DOMPurify；Vue 用 `v-html` 前过滤 |
| 只修复反射/存储 XSS | DOM XSS 载荷不进服务器，扫描器易漏 | Source/Sink 全在客户端 | **必须用 Burp DOM Invader/手工审计** 客户端 JS 代码 |
| 信任第三方库/CDN | 库被劫持/供应链投毒 | 引用外部脚本无完整性校验 | **SRI (Subresource Integrity)**：`<script src="..." integrity="sha384-...">` |

## 替代方案对比

| 维度 | 输出编码 (根治) | DOMPurify/净化库 | Trusted Types | CSP 兜底 |
|------|-----------------|------------------|---------------|----------|
| 防御层 | 代码根治 | 运行时净化 | 浏览器原生强制 | 浏览器执行层 |
| DOM XSS 覆盖 | 完全(若全覆盖) | 高(配置得当) | 高(原生强制) | 中(限制加载/执行) |
| 部署成本 | 高(全输出点) | 中(引入库/改调用) | 中(需改代码/配 CSP) | 中(需配 nonce/策略) |
| 遗漏风险 | 低(若规范执行) | 中(配置漏项) | 低(强制模式) | 中(策略漏洞) |
| 适用阶段 | 开发期 | 开发/运行期 | 开发/运行期 | 部署/运行期 |

---

> 参考来源：https://owasp.org/www-community/attacks/DOM_Based_XSS

*系列完：浏览器安全机制*