# 07 · SAML / OAuth / OIDC（互联网联合认证三剑客）

## 一句话秒懂
SAML 用 XML 断言在联盟间传认证+授权；OAuth 是**授权**框架（不是认证）；OIDC 在 OAuth 上**加认证层**用 JWT。三者都让你"用 A 站身份进 B 站"而不把密码交给第三方。

> 对应原书：Chapter 14 — "SAML" / "OAuth" / "OpenID Connect"

## 生活类比
- SAML：你拿学校开的"在读证明"（XML 断言）去图书馆联盟，对方信这个证明就放你进。
- OAuth：你授权某 App"可以读我的社交账号日程"，但不把账号密码给它——它拿到的是"门禁令牌"不是钥匙。
- OIDC：在 OAuth 基础上加了"这是张三本人"的身份证（JWT），既授权又认证。

## 核心概念（大白话 + 原书定义）

**为何需要**：绝不该把 A 站凭据交给 B 站（如把 Bank A 密码给 Bank B 转账）。SAML/OAuth/OIDC 解决"共享认证/授权/档案信息而不共享凭据"。

**SAML（Security Assertion Markup Language）**：
- 开放 **XML 标准**，OASIS 2005 采纳（SAML 2.0），交换认证+授权（AA）信息，给浏览器 SSO。
- 三实体：**Principal（用户）**、**SP（Service Provider/依赖方）**、**IdP（Identity Provider/断言方，存认证授权信息）**。
- 流程：用户访问 SP → SP 重定向到 IdP → 用户输凭据 → IdP 用 **SAML assertions（XML 消息）** 回 SP（含认证/属性/授权三型语句）→ SP 放行。
- 提供认证、属性、授权三类语句。

**OAuth 2.0（开放授权）**：RFC 6749，IETF 维护的**授权框架（非认证协议）**。例：Acme App 要排期发社交帖 → 重定向到社交站 → 你登录并授权 → 社交站给 App **access token** → App 带 token 调 API。**你从没把社交密码给 App**；即使 App 被黑也不泄露凭据。用 API 消息 + token 表授权。OAuth 2.0 不向后兼容 1.0。

**OIDC（OpenID Connect）**：在 OAuth 2.0 授权框架上的**认证层**，由 OpenID Foundation 维护。用 **JWT（JSON Web Token，ID token）** 表身份，可含用户档案。既认证又授权。例：用 Google 账号登 eBay。OAuth 提供授权，OIDC 用 OAuth 框架 + OpenID 技术做认证，用 JWT。

**三者对比速记**：
- SAML：XML、三实体（Principal/SP/IdP）、认证+授权+属性。
- OAuth：授权框架、RFC 6749、API+token、非认证。
- OIDC：OAuth 上的认证层、JWT、既认证又授权。

> 口诀：**"SAML XML 断言传三语，OAuth 授权非认证、token 不交密；OIDC 叠认证、JWT 表身份，三剑客不共密。"**

## 真实案例
员工用企业 Google Workspace（IdP）登录内部 SaaS：SAML 断言传给各 SP；某第三方排期工具用 OAuth 仅获"读取日历"授权（拿不到密码）；对外服务用 OIDC（Google 登录）既认证身份又授权访问。

## 考试怎么考
- SAML 三实体（Principal/SP/IdP）与断言类型。
- **OAuth 是授权框架不是认证协议**（高频考点）。
- OIDC 在 OAuth 上叠加认证层、用 JWT。
- 三者都不共享用户凭据的核心安全价值。
- SAML 基于 XML、OASIS 2005。

## 记忆口诀
> **"SAML 三实体断言走 XML，OAuth 授权不认证、token 代密；OIDC 叠认证 JWT，三不交密码保安全。"**

## 自测
1. SAML 的三个实体是什么？断言（assertion）含哪三类语句？
2. 为什么 OAuth 2.0 被称为"授权框架"而非"认证协议"？
3. OIDC 与 OAuth 的关系？它用什么令牌？
4. 用 OAuth 授权第三方 App 时，用户密码是否会交给该 App？为什么安全？
5. SAML 基于什么格式？由谁在何年采纳为标准？
