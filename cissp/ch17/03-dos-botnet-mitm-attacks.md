---
title: ① 一句话秒懂
parent: 第 17 章
grand_parent: CISSP 认证安全工程师知识库
nav_order: 3
---

# ① 一句话秒懂

本章集中讲三类高频攻击手法：**拒绝服务（DoS/DDoS）** 把系统冲瘫、**僵尸网络（Botnet）** 提供攻击兵力、**中间人/On-path 攻击** 偷偷截获篡改通信——以及对应的 SYN Flood、Smurf、MITM 等经典招式。

# ② 生活类比

- **DoS** = 一个人堵在店门口，真客人进不去。
- **DDoS** = 雇了几万人（僵尸网络）一起堵门，老板根本拦不住。
- **Botnet** = 黑客远程控制的"僵尸军团"，成员（你的电脑）自己都不知道被征用了。
- **MITM/On-path** = 黑客坐在你和银行之间当"邮差"，你以为直接跟银行说话，其实每封信他都拆看甚至篡改。

# ③ 核心概念

## Botnets（僵尸网络）
- 被恶意代码感染的电脑（bots/zombies）受 **bot herder（僵尸牧人）** 通过 **C&C / C2 服务器** 指挥。
- 用途：DDoS、发垃圾/钓鱼邮件、出租给别的罪犯。规模可达数万至数百万。
- 防御：纵深防御、更新反恶意软件、打补丁、教育用户（钓鱼）、浏览器/插件更新、勿关沙箱。
- **IoT/嵌入式系统**成新目标（Mirai 用摄像头/路由器组成僵尸网络打瘫 Dyn DNS，Twitter/Netflix/Reddit 等中断）。

## DoS / DDoS
- **DoS**：单系统攻击单系统，常 spoof 源地址隐藏自己。耗尽资源致崩溃/降速。
- **DDoS**：多系统同时打单目标，常用 botnet。
- **DRDoS（分布式反射 DoS）**：不直接打受害者，而是操纵流量/服务让攻击"反射"回受害者（DNS 投毒、Smurf、Fraggle）。

### 经典 DoS 招式
- **SYN Flood**：利用 TCP 三次握手，发大量 SYN 不回 ACK，耗尽服务器等待资源。防护：**SYN cookies**、缩短 ACK 等待时间（默认 3 分钟）、防火墙/IPS 检测。
- **TCP Reset 攻击**：spoof RST 包断开活跃会话（对需持久会话的系统威胁大）。
- **Smurf**：spoof 受害者 IP 发广播 ping，全网回 ICMP 洪水。RFC 2644（1999）默认路由器不转发定向广播 + 防火墙禁 ICMP 已基本遏制。
- **Fraggle**：类似 Smurf，但用 UDP 7（echo）/19（chargen）。
- **Ping Flood**：大量 ping 请求，常见于 botnet DDoS；禁 ICMP echo 可挡。
- **遗留攻击**：Ping of Death（超大 ping 包）、Teardrop（IP 分片重组崩溃）、LAND（源=目的 IP 的 SYN）。

## Zero-Day Exploit（零日漏洞）
- 利用"厂商/公众尚不知或尚无补丁"的漏洞的攻击。三种语境：攻击者先发现、厂商已知未发补丁、发补丁后 24h 内被逆向利用（Exploit Wednesday）。
- **注意**：厂商发补丁数周/月后仍未打的补丁系统被攻 = 不是零日，是"未打补丁系统被攻"。

## Man-in-the-Middle / On-path（中间人）
- 攻击者在两通信端点间建立位置，可嗅探或充当 store-and-forward 代理篡改内容。
- 需更高技术（伪造路由/DNS、装证书破加密隧道、伪造 ARP）。VPN 可规避；IDS 难检测 MITM 但能发现链路异常。

## Sabotage（员工破坏）
- 知情且有权限的不满员工（disgruntled employee）破坏。防范：离职 swift 处理、立即禁用账户、强化审计/监控异常、保持沟通、合理补偿。

# ④ 真实案例

**2016 Mirai DDoS 攻击 Dyn**：攻击者感染海量 IoT 设备（摄像头、DVR、家用路由器）组成僵尸网络，向 Dyn 的 DNS 服务器洪水攻击，导致 Twitter、Netflix、Amazon、Reddit、Spotify 等大面积无法访问。Gartner 估计 2020 年有 200 亿 IoT 设备——攻击面巨大，且很多 IoT 设备厂商根本不发补丁。

# ⑤ 考试怎么考

- **DoS vs DDoS** 区别（单源 vs 多源/botnet）。
- **SYN Flood** 原理与防护（SYN cookies、缩短等待）。
- **Smurf/Fraggle** 用 ICMP/UDP 广播反射；RFC 2644 禁定向广播。
- **Zero-day** 三种语境；发补丁很久后未打被攻 ≠ 零日。
- **MITM = On-path**，VPN 可缓解。
- **Mirai/IoT** 是 botnet 新战场。

# ⑥ 记忆口诀

> **"DoS 单打 DDoS 群，botnet 僵尸听 C2 令；SYN 洪泛 cookies 防，Smurf Fraggle 广播镜；零日无补丁才叫零，补丁拖久非零日；MITM 改名 on-path，VPN 破之加密行。"**

# ⑦ 自测

1. DoS 与 DDoS 的根本区别是什么？DRDoS 又是如何运作的？
2. SYN Flood 攻击利用了 TCP 三次握手的什么弱点？列出两种防护方法。
3. Smurf 和 Fraggle 攻击分别利用什么协议？RFC 2644 如何缓解 Smurf？
4. 什么是 zero-day exploit？为什么"系统很久没打补丁被攻"不算零日？
5. Man-in-the-Middle 攻击为何又称 on-path 攻击？用户应如何防范？
6. Mirai 僵尸网络攻击说明了什么安全趋势？
