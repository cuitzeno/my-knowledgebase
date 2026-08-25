# 06 · RADIUS 与 TACACS+（AAA 远程访问协议）

## 一句话秒懂
RADIUS 和 TACACS+ 都是给 VPN/拨号等远程访问做集中式 AAA 的协议。RADIUS 用 UDP、只加密密码；TACACS+ 用 TCP、加密全部认证信息，且把 AAA 三功能分离——Cisco 系偏爱后者。

> 对应原书：Chapter 14 — "RADIUS" / "TACACS+"

## 生活类比
两地分公司要连总部 VPN：员工在本地网关（NAS）输凭据，网关把凭据转给总部的"认证大本营"（RADIUS/TACACS+ 服务器）核验，通过才放。NAS 是客户端，认证服务器是服务端。

## 核心概念（大白话 + 原书定义）

**AAA 协议作用**：为 VPN、NAS 等远程访问提供集中式标识/认证/授权/记账，保护内网认证系统；远程系统被攻只影响远程用户，不波及内网账号。

**RADIUS（Remote Authentication Dial-in User Service）**：
- 集中认证远程连接（VPN/拨号）；NAS 是 RADIUS 客户端，RADIUS 服务器是认证服务器，给多个 NAS 提供 AAA。
- ISP 常用；可配 **callback security（回拨）**：用户拨入认证后，服务器挂断并回拨预存号码，凭证泄露也防滥用。
- 默认 **UDP**；**只加密密码交换**，不加密整会话（可借 TLS 加密）。
- 端口：认证授权 **UDP 1812**，记账 **UDP 1813**；用 TLS 时 TCP 2083（RFC 6614）。
- RFC 2865 定义。

**TACACS+（Terminal Access Controller Access Control System Plus）**：
- Cisco 开发后开源；比 RADIUS 有改进。
- **分离 AAA 为独立过程**（可各跑不同服务器）。
- **加密全部认证信息**（不只密码）。
- 用 **TCP 49**，传输更可靠。

**对比要点**：RADIUS=UDP/只密密码/AAA 一体；TACACS+=TCP/全加密/AAA 分离。考试常考此差异。

> 口诀：**"RADIUS UDP 只密密码 1812/1813，TACACS+ TCP 49 全加密 AAA 分；远程接入靠它俩，回拨防凭证滥。"**

## 真实案例
企业 VPN 用 RADIUS（对接 AD）做远程员工 AAA，并启 callback 防凭证被盗后用。核心网络设备（路由器/交换机）管理登录用 TACACS+，因需加密全部交互且分离授权审计，满足合规审计要求。

## 考试怎么考
- RADIUS 与 TACACS+ 的核心差异（UDP vs TCP、只密密码 vs 全加密、AAA 一体 vs 分离）。
- RADIUS 端口（1812 认证 / 1813 记账；TLS 2083）。
- TACACS+ 端口 49、Cisco 来源。
- callback security 的作用。
- NAS 是 RADIUS 客户端这一概念。

## 记忆口诀
> **"RADIUS 1812/1813 UDP 密密码，TACACS+ 49 TCP 全加密；AAA 分与合，远程接入各显能。"**

## 自测
1. RADIUS 与 TACACS+ 在传输协议、加密范围、AAA 结构上各有什么区别？
2. RADIUS 的默认端口（认证/记账）？用 TLS 时端口？
3. TACACS+ 的端口？它把 AAA 分成什么？
4. 什么是 callback security？防什么？
5. 在 RADIUS 架构中，NAS（网络访问服务器）扮演什么角色？
