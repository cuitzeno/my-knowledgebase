---
title: 04 · 多因子、无密码与 FIDO（MFA / Passwordless / FIDO）
parent: 第 13 章
grand_parent: CISSP 认证安全工程师知识库
nav_order: 4
---

# 04 · 多因子、无密码与 FIDO（MFA / Passwordless / FIDO）

## 一句话秒懂
MFA 是"不同类因素叠加"才更强；无密码认证（刷脸/指纹/passkey）正成趋势；NIST 已**弃用 SMS 做 2FA**（可被 SIM 交换骗）；FIDO 联盟推硬件 passkey 减少密码依赖。

> 对应原书：Chapter 13 — "Multifactor Authentication" / "NIST Deprecates SMS for 2FA" / "Passwordless Authentication"

## 生活类比
MFA 像同时需要"钥匙 + 指纹"开保险箱——小偷偷到钥匙还得剁你手指。无密码是把钥匙彻底换成你的脸；SMS 验证码则像把备用钥匙寄到你家信箱，邮差（或骗子）可能截走。

## 核心概念（大白话 + 原书定义）

**MFA（多因子认证）**：用 **2 种及以上不同类型**因素。2FA 是两因素。规则：**同类两个不算 MFA**（密码+PIN 同属"知道"；两密码一起也不比一个更安全，因一次破解全得）。不同类则需不同攻击同时成功（偷设备+破密码+伪造生物）。

**NIST 弃用 SMS 做 2FA**：短信 OTP 优于纯密码但问题多：
- 锁屏直接显示 OTP，手机被盗即泄露。
- 攻击者可通过 **SIM 交换欺诈（SIM swap）** 让运营商把短信转自己设备 → 拦截 OTP。
- 故 NIST SP 800-63B 已不推荐联邦机构用 SMS 做两步认证。

**无密码认证（Passwordless）**：不用记忆秘密即可登录。常见：手机/平板生物识别（刷脸、按指纹）。应用常"首次保存凭据→之后用生物再认证"。趋势是减少静态密码带来的写纸条/弱密码等风险行为。

**FIDO 联盟（Fast Identity Online）**：开放行业协会，使命是**减少对密码的过度依赖**。制定无密码框架与协议标准，围绕**硬件 passkey**（如 YubiKey）。passkey 把私钥存硬件，钓鱼网站拿不到。

**设备认证（Device Authentication）**：
- **设备指纹（device fingerprinting）**：注册时采集 OS/浏览器/字体/时区/分辨率/HTTP 头等属性，登录时比对。
- **MDM + NAC**：上下文感知识别设备健康，配合 802.1X 端口认证，过不了就不给入网。

**服务认证（Service Authentication）**：服务账号（service account）是给应用而非人用的账号（如 Exchange 扫描邮件的第三方工具、SQL Server 的 `sa` 账号）。高风险点：`sa` 旧版默认空密码、攻击者常试；服务账号密码常设"永不过期"否则服务锁死；应配强复杂密码、手动定期改、设**非交互（noninteractive）**防人登录、做账户访问评审。

> 口诀：**"MFA 跨界才强，SMS 被弃因 SIM 换；无密码靠生物，FIDO 推 passkey 抗钓鱼。"**

## 真实案例
公司原用"密码 + SMS 验证码"2FA，一员工遭 SIM 交换攻击，短信被截，账号被盗。改用 FIDO 硬件 passkey + 生物，钓鱼无法窃取私钥，攻击面大幅缩小；同时把 SQL 的 `sa` 账号设强密码且非交互。

## 考试怎么考
- MFA 定义 + "同类两因素不算 MFA"。
- NIST 弃用 SMS 2FA 的两大原因（锁屏显示、SIM swap）。
- 无密码认证与 FIDO/passkey 概念。
- 服务账号风险（`sa` 空密码、永不过期、非交互）。
- 设备指纹 / MDM+NAC / 802.1X 设备认证。

## 记忆口诀
> **"MFA 要跨界，SMS 因 SIM 换被弃；FIDO passkey 抗钓鱼，服务账号慎空密。"**

## 自测
1. 为什么"密码 + PIN"不是 MFA？
2. NIST 弃用 SMS 做 2FA 的理由？
3. 什么是无密码认证？FIDO 推什么来替代密码？
4. 服务账号（service account）有哪些特有风险？如何应对？
5. 设备指纹如何工作？MDM+NAC 如何配合 802.1X？
