---
title: 01 · VPN 与隧道技术（VPN & Tunneling）
parent: 第 12 章
grand_parent: CISSP 认证安全工程师知识库
nav_order: 1
---

# 01 · VPN 与隧道技术（VPN & Tunneling）

## 一句话秒懂
VPN（虚拟专用网络）就是在一条你不信任的公共网络（比如互联网）上，挖出一条加密的"私管隧道"，让两个端点之间像在自家局域网一样安全通信。

> 对应原书：Chapter 12 *Communication and Network Security* — "Virtual Private Network" / "Tunneling"

## 生活类比
寄信给奶奶：你写好的信（原始数据包）塞进信封（隧道协议），邮局（不可信的中间网络）只看到信封外面的地址，看不到信里写了啥。信封到了奶奶手里才拆开。VPN 干的就是"套信封 + 加锁"这件事。

## 核心概念（大白话 + 原书定义）

**什么是 VPN**（原书定义）：*A VPN is a communication channel between two entities across an intermediary untrusted network.* VPN 能提供访问控制、认证、机密性、完整性。注意——**VPN 不保证可用性（Availability）**，它解决不了网络不通的问题。

**隧道（Tunneling）**：把一种协议的数据包"套"进另一种协议的数据包里传输。加密的隧道能在不可信网络上保护内层数据的机密性与完整性。代价是：开销更大、带宽更耗、且是点对点、不能处理广播流量；而且加密后防火墙/IDS 看不到包内容，所以这些安全设备必须放在隧道"外面"（解密后）才能扫描。

**VPN 两种模式**（以 IPSec 为例）：
- **传输模式（Transport Mode）**：只加密**载荷（payload）**，原始包头不动 → 主机到主机（host-to-host），适合可信内网。
- **隧道模式（Tunnel Mode）**：连包头一起加密，整包封装后再加 IPSec 头 → 站点到站点（site-to-site）或远程接入（remote access），适合跨不可信网络。

**Always-On VPN**：网络一通就自动连 VPN，多用于移动设备，防止用开放公共网络时裸奔。

**Split Tunnel（分流隧道）vs Full Tunnel（全隧道）**：
- 分流：客户端同时直连互联网和走组织 VPN → **不安全**（互联网→客户端→内网的开放通道，恶意代码易横向移动）。
- 全隧道：所有流量先回组织网络，再由其代理/防火墙出去 → 所有流量都受组织安全策略管控。

### 常见 VPN 协议（考试常考对比）

| 协议 | 层 | 端口 | 加密 | 备注 |
|---|---|---|---|---|
| PPTP | L2 | TCP 1723 | MPPE（MS-CHAPv2） | **已淘汰**，初始协商不加密 |
| L2TP | L2 | UDP 1701 | 无原生加密，常与 IPSec 配合（L2TP/IPSec） | RFC 2661 标准 |
| SSH | — | TCP 22 | 是 | 只能做传输模式（host-to-host）VPN |
| OpenVPN | — | — | 基于 TLS | 开源，可用预共享密码或证书 |
| IPSec | L3 | — | AH/ESP/AES | 标准套件，VPN 主力 |

**IPSec 组件**：AH（认证头，完整性+不可否认+防重放）、ESP（封装安全载荷，机密性+完整性，可独立建链）、HMAC（完整性哈希）、IPComp（压缩）、IKE（密钥交换，含 OAKLEY+SKEME+ISAKMP）。每个 IPSec VPN 用**两个安全关联（SA）**：一个发、一个收，所以是两条独立加密的单工通道。

> 记忆小技巧：**名字里 S 在前（SFTP）→ SSH 加密；S 在后（HTTPS）→ TLS 加密**。

## 真实案例
某公司用 site-to-site IPSec VPN 把北京和上海两个办公室连起来，取代昂贵的专线，一年省下几十万。员工出差用 remote-access VPN（全隧道）连回公司，所有上网流量先过公司防火墙，防数据泄露。

## 考试怎么考
- 区分传输模式 vs 隧道模式加密的对象（payload only vs payload+header）。
- PPTP/L2TP/SSH/OpenVPN/IPSec 的特点与端口。
- Split tunnel 的风险（开放通道），Full tunnel 的优势。
- IPSec 的 AH（无 confidentiality）与 ESP（有 confidentiality）职责区别。
- VPN 不提供 Availability。

## 记忆口诀
> **"隧道套信封，传输只包肉，隧道连皮带骨；分流有缝，全通最稳；PPTP 老、L2TP 借 IPSec、OpenVPN 靠 TLS、IPSec 双 SA。"**

## 自测
1. 传输模式和隧道模式分别加密了什么？
2. 为什么 split tunnel 被认为有安全风险？
3. IPSec 中 AH 和 ESP 的核心区别是什么？
4. 为什么防火墙/IDS 要放在 VPN 隧道"外面"？
5. 说出至少 3 个 VPN 协议及其对应端口（如记得）。
