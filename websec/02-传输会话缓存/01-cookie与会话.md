---
title: "Cookie 与会话管理"
parent: "传输、会话与缓存"
grand_parent: "Web 安全与开发基础实战知识库"
nav_order: 1
---

# Cookie 与会话管理

## 一句话定义
HTTP 无状态，靠 Cookie 记住"你是谁"。Cookie 的三个属性直接决定会话安全：**Secure（仅 HTTPS 传）**、**HttpOnly（防 JS 偷）**、**SameSite（抗 CSRF）**——配错即成高危。

## 核心架构 / 工作原理

```mermaid
sequenceDiagram
  participant Browser as 浏览器
  participant Server as 服务器
  
  Browser->>Server: HTTP 请求 (无 Cookie)
  Server-->>Browser: Set-Cookie: session=xyz; Secure; HttpOnly; SameSite=Lax; Path=/; Max-Age=3600
  Browser->>Browser: 存 Cookie (符合属性)
  Browser->>Server: 后续请求自动带 Cookie: session=xyz
  Server-->>Server: 校验 Session → 识别用户
```

| 属性 | 作用 | 推荐值 | 缺失后果 |
|------|------|--------|----------|
| **Secure** | 仅 HTTPS 传输 | `Secure` | 明文 HTTP 被截获令牌 |
| **HttpOnly** | 禁止 JS 读 `document.cookie` | `HttpOnly` | XSS 窃取会话令牌 |
| **SameSite** | 限制跨站请求携带 Cookie | `Lax` (默认) / `Strict` | CSRF 攻击 |
| **Path/Domain** | 作用域最小化 | `Path=/` `Domain=.example.com` | 令牌泄露到无关子域/路径 |
| **Expires/Max-Age** | 生命周期控制 | 会话级或短时(如 1h) | 令牌永久有效、登出不失效 |

## 快速上手步骤

1. **检查现有 Cookie**：
   ```bash
   curl -I https://target.com/login | grep -i set-cookie
   # 或浏览器 DevTools → Application → Cookies
   ```
2. **验证三件套**：每个会话 Cookie 必有 `Secure; HttpOnly; SameSite=Lax/Strict`
3. **测 SameSite 行为**：
   - `Lax`：顶级导航/GET 表单带 Cookie
   - `Strict`：仅同站请求带 Cookie
   - `None; Secure`：跨站带 Cookie(需配合 Secure)
4. **测登出销毁**：登出后 → 检查 `Set-Cookie: session=; Max-Age=0` + 服务端 Session 失效

```bash
# 快速测试 Cookie 属性
curl -v https://target.com/login -c cookies.txt -d "user=test&pass=123" 2>&1 | grep -i set-cookie
```

## 踩坑避坑指南

| 场景 | 问题现象 | 原因 | 解决/最佳实践 |
|------|----------|------|---------------|
| 只设 HttpOnly 不设 Secure | HTTPS 下仍可能被降级明文传 | 缺 Secure | **三件套全配**：`Secure; HttpOnly; SameSite=Lax` |
| SameSite=None 又不开 Secure | 跨站请求被浏览器拦截/中间人拿到 | 缺 Secure | **SameSite=None 必须配 Secure**；或改 Lax/Strict |
| 前端登出以为安全 | 服务端 Session 未失效，令牌仍可复用 | 仅清前端 Cookie | **登出必须双端**：前端删 Cookie + 后端销毁 Session + 令牌加入黑名单/短期失效 |
| 会话 Cookie 无过期 | 关浏览器失效，但会话级仍可被偷用 | 未设 Max-Age | **敏感业务用短时持久 Cookie(如 1h)**；关键操作二次验证 |
| 子域共享会话泄露 | `Domain=.example.com` 泄露到不安全子域 | 作用域过宽 | **最小化 Domain**；不需共享的子域勿设父域 |

## 替代方案对比

| 维度 | Cookie 会话 | JWT (Authorization Header) | 双 Token (Access+Refresh) |
|------|-------------|----------------------------|---------------------------|
| 存储位置 | 浏览器 Cookie | 内存/LocalStorage | 内存 + HttpOnly Cookie |
| CSRF 防护 | SameSite/Lax | 需额外 CSRF Token | Refresh 在 Cookie(抗 CSRF) |
| XSS 抗性 | HttpOnly 防窃 | LocalStorage 易被 XSS 偷 | Access Token 在内存(较安全) |
| 服务端状态 | 有状态(Session 存服务端) | 无状态(自包含) | 混合(Access 无状态/Refresh 有状态) |
| 撤销/轮换 | 服务端直接删 Session | 需黑名单/短期+轮换 | Refresh Token 轮换+撤销链 |
| 适用场景 | 传统 Web/SSR | SPA/移动端/微服务 | 高安全要求/长会话 |

---

> 参考来源：https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies

*下一篇：[TLS 握手与 HTTPS](02-tls与https.md)*