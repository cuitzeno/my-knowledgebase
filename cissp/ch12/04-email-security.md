---
title: 04 · 邮件安全（Email Security）
parent: 第 12 章 · 安全通信与网络攻击
grand_parent: CISSP 认证安全工程师知识库
nav_order: 4
---

# 04 · 邮件安全（Email Security）

## 一句话秒懂
普通邮件像明信片——谁都能看、能改、能伪造。S/MIME、PGP、SPF/DKIM/DMARC 这套组合拳，分别解决加密、签名、防伪造三件事。

> 对应原书：Chapter 12 — "Manage Email Security"

## 生活类比
明信片（SMTP 明文）寄出去，邮局分拣员、路人都能瞄一眼；S/MIME 像把明信片装进带锁信封；DKIM/SPF 像邮局在信封上盖"确实出自本局"的官方章，假章一眼识破。

## 核心概念（大白话 + 原书定义）

**邮件协议**：SMTP（TCP 25，发信/中继）、POP3（TCP 110，下载到本地）、IMAP（TCP 143，服务器保留）。X.400 是地址与消息处理标准。**关键缺陷：SMTP/POP3/IMAP 原生不加密、不认证来源、不校验完整性** → 易拦截、易伪造、易篡改。

**Open Relay（开放中继）**：SMTP 服务器不认证发件人就转发 → 垃圾邮件放大器，必须关掉，改成需认证的 closed/authenticated relay。

**邮件安全目标**：机密性、完整性、源认证、不可否认、送达确认、敏感内容分类。**可用性无法绝对保证**（只能靠多接入路径补偿）。

**安全方案**：
- **S/MIME**：基于 X.509 证书 + 公钥加密。签名邮件（signed）= 完整性+源认证+不可否认；封装邮件（enveloped）= 收件人认证+机密性。
- **PGP / OpenPGP（GnuPG）**：点对点公钥邮件系统，非标准但事实标准。
- **SPF（Sender Policy Framework）**：声明"哪些主机被授权代本域发信"，收件方查 DNS 验证。
- **DKIM（DomainKeys Identified Mail）**：用域名私钥签名邮件，收件方验签确认"确实来自该域"，防伪造/钓鱼。
- **DMARC**：在 SPF+DKIM 之上，由域名主规定"验证失败怎么处理（丢弃/隔离/放行）"并接收反馈，专门防 BEC（商业邮件泄露）/钓鱼。
- **STARTTLS（显式/机会性 TLS）**：SMTP 命令，端口 587，对方支持就加密否则明文。
- **Implicit SMTPS**：端口 465，假设对方必支持 TLS，不支持就断（不接受明文）。

**垃圾/泛洪对策**：block list（封禁已知滥用源）、challenge/response（新发件人需人工确认）、reputation filtering（Sender Score、Spamhaus 等信誉评分）、网关拦附件（禁 exe/脚本类）、培训用户 + 反恶意软件。

**邮件炸弹（mail-bombing）**：海量邮件灌爆邮箱/服务器 = DoS；**邮件风暴（mail storm）**：Reply All 链式回复炸群。

> 口诀：**"SPF 查谁准发、DKIM 验章真、DMARC 定罚则；S/MIME 锁信封、PGP 走草根。"**

## 真实案例
某公司域名配置了 SPF+DKIM+DMARC，攻击者伪造 `ceo@公司.com` 要求财务转账的钓鱼邮件，因 DMARC 策略为"失败即隔离"，邮件直接进垃圾箱，BEC 诈骗未遂。

## 考试怎么考
- 基础邮件协议端口（25/110/143）及原生缺陷。
- S/MIME（证书、签名 vs 封装）vs PGP（非标准）区别。
- SPF / DKIM / DMARC 各自解决什么、如何配合。
- STARTTLS（587，机会性）vs SMTPS（465，强制）。
- Open relay 的危害。

## 记忆口诀
> **"SMTP 25 发、POP3 110 收、IMAP 143 留；SPF/DKIM/DMARC 三件套，防伪钓鱼是一绝。"**

## 自测
1. 基础邮件协议（SMTP/POP3/IMAP）的三个原生缺陷是什么？
2. S/MIME 的 signed 与 enveloped 邮件各提供哪些安全属性？
3. SPF、DKIM、DMARC 分别解决什么？
4. STARTTLS 与 Implicit SMTPS 的区别？端口各是？
5. 什么是 open relay？为什么必须关闭？
