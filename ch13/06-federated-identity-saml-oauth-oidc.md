# 06 · 联合身份与 SAML / OAuth / OIDC

## 一句话秒懂
联合身份（FIM）让"在 A 公司登录一次，就能进联盟内 B 公司资源"——互联网 SSO。常用协议：SAML（断言）、OAuth（授权）、OIDC（认证层）。云上叫 IDaaS。

> 对应原书：Chapter 13 — "SSO and Federated Identities" / "Cloud-Based/On-Premises/Hybrid Federation" / "Just-In-Time"

## 生活类比
大学联盟：你用本校学号登录，就能去联盟内其他学校的图书馆数据库查文献，不用每家再注册——这就是 FIM。协议就是各校约定的"通用语言"。

## 核心概念（大白话 + 原书定义）

**FIM（联合身份管理）**：把用户在一个系统的身份**链接**到多个身份管理系统，**跨组织**共享身份。用户在本组织登录一次，凭证匹配为联合身份，即可访问联盟内任何成员的资源。注意：**联盟成员资格不自动授予访问所有资源**——各组织自行决定共享哪些，对用户透明（不用再输凭证）。

**部署形态**：
- **云上联邦**：第三方服务共享联合身份（如企业培训网站用联合 SSO）。
- **本地（On-Premises）**：如两公司合并，自建本地联邦共享认证数据（控制最强）。
- **混合（Hybrid）**：云 + 本地组合。

**JIT（Just-In-Time 配置）**：首次访问时自动创建两实体间关系/账号，**无需管理员干预**。常用 **SAML** 交换数据（用户名、姓名、邮箱等）。例：员工首次访问第三方福利网站，JIT 自动建账号。

**IDaaS（身份即服务）**：第三方提供 IAM，本质是云 SSO，特别适合内部访问 SaaS。如"一个 Google 账号通所有 Google 服务"、"Microsoft 365 云认证"。

**关键协议（Ch14 详述，此处先建概念）**：
- **SAML（Security Assertion Markup Language）**：用断言（assertion）在各方间交换身份/认证信息，灵活度高，JIT 常用。
- **OAuth**：**授权**框架（委托权限，如"用 Google 账号授权某 App 读你通讯录"），注意不是认证协议。
- **OAuth 2.0** + **OIDC（OpenID Connect）**：OIDC 在 OAuth 上**加认证层**（用 ID token 证明用户身份）。

**凭证管理**：浏览器/系统（Windows Credential Manager）可存凭据；第三方**密码保险库（password vaults）**如 KeePass（主密码加密库）。脚本化访问（logon scripts）可模拟 SSO，但**脚本含明文凭据须存保护区**。

> 口诀：**"FIM 跨组织、一次登全联盟；SAML 传断言、OAuth 管授权、OIDC 加认证；IDaaS 云 SSO，JIT 自动建账号。"**

## 真实案例
公司用 Azure AD（IDaaS）做云 SSO，员工登域账号后点开 Salesforce、Slack 等 SaaS 无需再登录；与外包福利商配 JIT，首次访问自动建账号，省去批量开号。

## 考试怎么考
- FIM 的定义与"成员不自动获全访问"的要点。
- 云/本地/混合联邦区别。
- JIT 配置与 SAML 的作用。
- IDaaS 概念。
- SAML（断言）/ OAuth（授权）/ OIDC（认证层）三角色区分——OAuth 是授权非认证。

## 记忆口诀
> **"FIM 跨域一次登，SAML 断言、OAuth 授权、OIDC 认证；IDaaS 云托管，JIT 免开号。"**

## 自测
1. 什么是联合身份管理（FIM）？联盟成员是否自动能访问所有资源？
2. 云上、本地、混合联邦各指什么？
3. JIT 配置是什么？常用什么协议交换数据？
4. IDaaS 是什么？举例。
5. SAML、OAuth、OIDC 三者分工有何不同？尤其 OAuth 是认证还是授权？
