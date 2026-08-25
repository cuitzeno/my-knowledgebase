---
title: Web 应用攻击：XSS、CSRF、SSRF、会话劫持（Web App Exploits）
parent: 第 21 章
grand_parent: CISSP 认证安全工程师知识库
nav_order: 5
---

# Web 应用攻击：XSS、CSRF、SSRF、会话劫持（Web App Exploits）

> 来源：Chapter 21 · Exploiting Web Application Vulnerabilities
> 域：Domain 8 Security and Risk Management（安全与风险管理）
> 模板：原书定义+对比表 / 真实案例 / 考试怎么考

## ① 一句话秒懂
Web 应用是公开面，攻击者借 **XSS 偷身份、CSRF 借你信任发指令、SSRF 骗服务器探内网、会话劫持直接顶替你**。

## ② 原书核心定义 + 对比表

**四大 Web 攻击对比**：

| 攻击 | 利用的信任 | 机制 | 防御 |
|---|---|---|---|
| XSS（跨站脚本） | 用户对网站的信任 | 注入 `<SCRIPT>` 到页面 | 输入校验 + 输出编码 |
| CSRF/XSRF（跨站请求伪造） | 网站对用户的信任 | 借已登录状态发指令 | 安全令牌 / 校验 Referer |
| SSRF（服务端请求伪造） | 服务器对内网 URL 的访问 | 诱服务器访问内部 URL | 校验用户提供的 URL |
| Session Hijacking（会话劫持） | 会话凭证 | 截获/复用 cookie | 过期 cookie / 防重放 |

**XSS 两型**：Reflected（反射，输入在链接里骗第三方）/ Stored/Persistent（存储，留在服务器如留言板）。

**XSS 防御**：输入校验（白名单）+ 输出编码（output encoding：HTML/URL/JS/CSS 编码，如 `'` → `&#39;`）。

## ③ 生活类比（精炼）
XSS 像在银行官网留言区塞"自动转账脚本"，别人来看就中招；CSRF 像攻击者借你已登录的网银，偷偷发"转钱给坏人"的请求；SSRF 像骗公司服务器去访问只有它能看的"内网保险柜"；会话劫持像捡到你没退出的门禁卡直接进。

## ④ 真实案例
- **反射 XSS 钓鱼**：攻击者把含脚本的链接伪装成"查 First Bank 账户"，用户点开真网站却执行了恶意脚本。
- **存储 XSS 留言板**：攻击者在帖子末尾插 `<SCRIPT>alert(...)</SCRIPT>`，后续访客加载即触发，可重定向到钓鱼站。
- **CSRF 论坛链接**：论坛贴"转账链接"，已登录网银的用户一点，钱转给攻击者。

## ⑤ 相关概念梳理 + 对比表

**DOM-based XSS**：改浏览器内 DOM 环境，HTML 源码里看不到，仍危险。

**CSRF vs XSS 信任方向相反**：XSS 利用"用户信网站"在用户机执行代码；CSRF 利用"网站信用户"以用户身份发命令。

**SSRF 风险**：应用接受用户 URL 并访问，若服务器能触达非公开 URL，内网信息即泄露。

**会话劫持三手法**：截获认证细节顶替 / 中间人骗客户端 / 复用未妥善管理的 cookie。

## ⑥ 考试怎么考（题干样式 + 常见混淆项）
- 题干："Attack exploiting user's trust in a website to run script in user's browser?" → 答 **XSS**。混淆：CSRF 利用反向信任。
- 题干："Exploiting a site's trust in an authenticated user to issue commands?" → 答 **CSRF**。混淆：与 XSS 信任关系相反。
- 题干："Tricking a server into fetching an internal URL from user input is?" → 答 **SSRF**。混淆：非 CSRF（目标是服务器非用户浏览器）。
- 题干："Stored XSS differs from reflected in that it?" → 答 **persists on server**（持续存在）。混淆：reflected 不存储。

## ⑦ 自测（改编自原书 Review Questions，附解析）
1. 利用网站对用户已登录状态的信任，借用户浏览器发出非自愿指令，是？
   - A. XSS
   - B. CSRF
   - C. SSRF
   - D. 会话劫持
   - **答案：B**。解析：CSRF 利用"网站信用户"，以用户身份执行命令；XSS 利用反向信任。

2. 存储在留言板、对后续访客持续生效的 XSS 称为？
   - A. 反射型
   - B. 存储/持久型
   - C. DOM 型
   - D. 盲目型
   - **答案：B**。解析：stored/persistent XSS 留在服务器，攻击者不在线也持续危害。

3. 诱使服务器基于用户输入去访问内网 URL 泄露信息，是？
   - A. CSRF
   - B. SSRF
   - C. XSS
   - D. 目录遍历
   - **答案：B**。解析：SSRF 骗服务器访问其本可触达的非公开 URL，致内网信息暴露。
