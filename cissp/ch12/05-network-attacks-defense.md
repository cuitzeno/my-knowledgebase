---
title: 05 · 网络攻击与防御（Eavesdropping / Modification / DoS）
parent: 第 12 章
grand_parent: CISSP 认证安全工程师知识库
nav_order: 5
---

# 05 · 网络攻击与防御（Eavesdropping / Modification / DoS）

## 一句话秒懂
通信系统的四大经典威胁：偷听（eavesdropping）、篡改（modification）、拒绝服务（DoS/DDoS）、冒充（impersonation）——对应的防线是加密、完整性校验、冗余与认证。

> 对应原书：Chapter 12 — "Prevent or Mitigate Network Attacks"

## 生活类比
- 偷听 = 有人在电话线旁接了个录音笔（被动，难发现）。
- 篡改 = 把截到的信改了再发（主动攻击）。
- DoS = 不停往你信箱塞垃圾直到爆满，正经信收不进。

## 核心概念（大白话 + 原书定义）

**Eavesdropping（窃听/搭线）**：为复制通信内容而监听流量，可用 sniffer（协议分析仪）或物理搭线/软件记录。通常是**被动攻击**，难检测；一旦篡改或注入，就升级为**主动攻击**。防御：物理访问控制、加密（IPSec/SSH）、一次性认证（OTP/令牌）、应用白名单（防 sniffer 运行）。

**Modification Attacks（篡改攻击）**：截包→改包→重放，绕过认证与会话序列。对策：**数字签名验证 + 包校验和（完整性检查）**。

**其他通信威胁**（原书列举）：DoS/DDoS、impersonation、replay（重放，见 Ch11）、ARP poisoning、DNS poisoning、spoofing、transmission modification、eavesdropping。

**防御体系总览**（结合全书）：
- 机密性 → 加密（IPSec/TLS/SSH）
- 完整性 → HMAC/数字签名/校验和
- 源认证 → 802.1X/EAP/证书
- 可用性 → 负载均衡/冗余链路/限速/清洗

**负载均衡（Load Balancing）**补充：把流量分摊到多台设备/链路，优化利用率、降响应时间、消瓶颈。两种模式：
- **Active-Active**：常态全开，故障时降容量（维持可用性一致性）。
- **Active-Passive**：常态部分休眠，故障时接管（异常时维持容量）。

**第三方连接（Third-Party Connectivity）**：两组织网络直连，风险互相传导，一个被攻破另一个也危险。应先 MOU（谅解备忘录）起步，以 ISA（互联安全协议）收尾，连线前详细规划。

**WAN 技术**：分**专线（dedicated，只连两个固定端点）**与**非专线（nondedicated，需先建连）**；光纤链路（fiber-optic）抗电磁干扰、难搭线。

> 口诀：**"窃听被动难发现，篡改主动靠签名；DoS 灌爆桶，加密校验加冗余。"**

## 真实案例
攻击者用 ARP 毒化 + sniffer 在内网抓明文 Telnet 密码（被动窃听）。防御方改用 SSH（加密）+ 802.1X 端口认证 + 部署 NIDS 检测异常 MAC，窃听失效。

## 考试怎么考
- 被动攻击（窃听）与主动攻击（篡改/注入）的区别。
- 篡改攻击的对策（数字签名 + 校验和）。
- Active-Active vs Active-Passive 负载均衡。
- 第三方互联的风险传导与 MOU/ISA 流程。
- 专线 vs 非专线的区别。

## 记忆口诀
> **"窃听被动、篡改主动；签名校验防改包，冗余负载保可用；第三方连先 MOU 后 ISA。"**

## 自测
1. 被动攻击与主动攻击的根本区别？举例说明。
2. 篡改攻击用什么对策防御？
3. Active-Active 与 Active-Passive 负载均衡在故障时的表现差异？
4. 为什么两个组织网络直连要签 ISA？
5. 专线（dedicated）与非专线（nondedicated）的区别？
