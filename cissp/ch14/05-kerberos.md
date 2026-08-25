---
title: 05 · Kerberos 认证（Ticket-Based SSO）
parent: 第 14 章
grand_parent: CISSP 认证安全工程师知识库
nav_order: 5
---

# 05 · Kerberos 认证（Ticket-Based SSO）

## 一句话秒懂
Kerberos 是内网 SSO 标配：靠 KDC（密钥分发中心）发"票据"证明身份，**密码从不明文传**，抗窃听与重放；但 KDC 是单点故障、且要求全网时间同步（±5 分钟）。

> 对应原书：Chapter 14 — "Kerberos"

## 生活类比
进园区：你先在前台（KDC）凭工牌换一张"通票"（TGT），之后去各楼（服务）出示通票换"楼层票"（service ticket）即可，不用每楼重新查工牌。通票有时效，过期重换。

## 核心概念（大白话 + 原书定义）

**Kerberos 本质**：基于票据（ticket）的第三方认证系统，主用途是**认证**；认证后发票据，访问资源时出示。CISSP 名源于希腊神话三头犬（守门）。

**关键元素**：
- **KDC（Key Distribution Center）**：可信第三方，存所有成员密钥，用对称加密认证。
- **AS（Authentication Server）/ TGS（Ticket-Granting Service）**：KDC 的两大功能（AS 验证+TGS 发票），可同服或分离。
- **Ticket（票据/ST）**：加密消息，证明主体有权访问对象。
- **TGT（Ticket-Granting Ticket）**：证明已通过 KDC 认证、可请求其他票据；含对称密钥、过期时间、用户 IP。
- **Principal**：请求票据的实体（多为用户）。
- **Realm**：KDC 管辖的逻辑域（如域/网络）。

**技术特征**：Kerberos v5 用 **AES 对称加密**，提供认证流量的机密性+完整性，抗窃听/重放；用 **UDP 88 端口**；依赖目录（如 AD）存账号。

**登录流程**：输用户名密码 → 客户端发明文用户名（**不含密码**）给 AS → AS 查库 → KDC 用密码哈希加密 session key + 时间戳 TGT 回传 → 客户端用密码哈希解密得 session key 并存 TGT。

**访问资源流程**：客户端持 TGT 向 KDC 请求资源票据 → KDC 验 TGT 有效并查访问控制矩阵 → TGS 发 service ticket → 客户端把 ST 给资源服务器 → 服务器与 KDC 验 ST → 建立会话。

**两大弱点**：
- **单点故障**：KDC 被攻破＝全网密钥泄露；KDC 宕机＝无法认证。
- **严格时间同步**：默认所有系统须 ±5 分钟同步（AD 用 NTP 层级同步），否则 TGT 失效、无法领新票。

> 口诀：**"Kerberos 三头犬守门，KDC 发票据；密码不明传、AES 抗重放；KDC 单点、时间须同步。"**

## 真实案例
企业 AD 域用 Kerberos 做 SSO：员工登录域后访问文件/打印/邮件都不用重输密码（持 TGT 换 service ticket）。运维配置 NTP 层级同步，并为 KDC 做冗余（多 DC），缓解单点故障。

## 考试怎么考
- Kerberos 用途（认证 + SSO）与 KDC/AS/TGS/TGT/ST/Realm 角色。
- 密码**不明文传输**（用密码哈希加解密）。
- 抗窃听/重放；用 AES、端口 88。
- 单点故障（KDC）与 ±5 分钟时间同步要求。
- 登录与访问资源的两段流程。

## 记忆口诀
> **"Kerberos 靠 KDC，TGT 换 ST；密码哈希传、AES 守门；单点故障、五分同步。"**

## 自测
1. Kerberos 中 KDC、AS、TGS、TGT、ST 各是什么？
2. 为什么 Kerberos 中用户密码不会在网络上明文传输？
3. Kerberos 的两个主要弱点？
4. Kerberos 默认要求系统时间同步在多少分钟内？为何？
5. Kerberos 用哪种加密？端口是多少？
