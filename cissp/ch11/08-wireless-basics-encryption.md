---
title: 08 · 无线网络基础与加密（Ch11 · Domain 4）
parent: 第 11 章 · 安全网络架构与组件
grand_parent: CISSP 认证安全工程师知识库
nav_order: 8
---

# 08 · 无线网络基础与加密（Ch11 · Domain 4）

> 无线让部署变简单、成本低，但信号「溢出墙外」带来距离窃听、新 DoS 与入侵风险。Wi-Fi 加密从 WEP 一路烂到 WPA3，这一篇讲清演进与安全部署步骤。

## ① 一句话秒懂
无线网是「没有围墙的网」（unbounded），谁在墙外拿个接收器都能蹭信号。WEP 像纸锁一捅就破，WPA2/WPA3 才是不锈钢门。

## ② 生活类比
- **Ad hoc / Wi-Fi Direct**：两人直接喊话，不需要基站（对等式）。
- **Infrastructure 模式**：大家都通过基站（WAP）中转，基站定规矩。
- **SSID**：Wi-Fi 的「房名」；**BSSID**：基站的 MAC，像房号。
- **WEP→WPA→WPA2→WPA3**：锁的代际，越往后越结实。

## ③ 核心概念（大白话 + 原书定义）

**802.11 标准演进（部分）**：
|  amendment | Wi-Fi 名 | 速率 | 频率 |
|-----------|---------|------|------|
| 802.11b | Wi-Fi 1 | 11 Mbps | 2.4 GHz |
| 802.11g | Wi-Fi 3 | 54 Mbps | 2.4 GHz |
| 802.11n | Wi-Fi 4 | 600 Mbps | 2.4/5 GHz |
| 802.11ac | Wi-Fi 5 | 3.5 Gbps | 5 GHz |
| 802.11ax | Wi-Fi 6/6E | 9.6 Gbps | 1–7.125 GHz |
| 802.11be | Wi-Fi 7 | 40 Gbps | 1–7.25 GHz |

> 注意：802.11x 易与 802.1X（端口认证）混淆，原书建议用 802.11 统称。

**部署模式**：
- **Ad hoc（对等）/ Wi-Fi Direct**（支持 WPA2/WPA3，旧 ad hoc 仅 WEP）。
- **Infrastructure**：stand-alone（只连无线客户端）、wired extension（接有线网）、enterprise extended（多 WAP 同 ESSID 漫游）、bridge（无线连两段有线网）。
- **Fat AP**（全功能单机）vs **Thin AP / Controller-based**（受中央无线控制器管理）。

**SSID/ESSID/BSSID/ISSID**：房名/大院名/基站 MAC/对等设备标识。

**无线加密演进**（考试重点）：
- **WEP**：RC4 静态共享密钥，实现缺陷，<1 分钟可破，**绝不能用**。
- **WPA**：过渡方案，RC4+TKIP 或 LEAP；已被 coWPAtty/GPU 破解，**不安全**。
- **WPA2（802.11i）**：AES-CCMP（CCMP=Counter-Mode/CBC-MAC），至今 AES-CCMP 未被攻破，但密钥交换有 KRACK 漏洞。认证：PSK/PER（静态密码）或 802.1X/ENT（RADIUS/TACACS+）。AAA 端口：RADIUS UDP 1812/1813、TACACS+ TCP 49。
- **WPA3**（2018）：WPA3-ENT 用 192 位 AES-CCMP，WPA3-PER 128 位；PER 用 **SAE（Simultaneous Authentication of Equals）** 替代 PSK，基于 Dragonfly（DH 衍生）零知识证明，不再明文传密码；并实现 802.11w 管理帧保护。

**WPS**：简化加设备，PIN 两段可分段爆破（<6 小时攻破），多数 WAP 默认开，**部署前应关闭**。

**MAC 过滤**：白名单限制设备，但以太网头明文可被嗅探伪造 MAC，且现代手机随机 MAC，已不实用。

**天线**：全向（omni，如橡胶鸭）vs 定向（Yagi/cantenna/panel/parabolic）。部署原则：居中、避遮挡/金属/电器，小步调功率。

**通用 Wi-Fi 安全部署 15 步**（原书精简）：更新固件→改管理员密码→启 WPA2/WPA3→ENT 或长复杂 PSK/SAE→改 SSID→改 MAC→按需关广播→小环境开 MAC 过滤→静态 IP/DHCP 保留→WAP 与有线网用防火墙隔离→NIDS 监控→部署 WIDS/WIPS→考虑强制 VPN→captive portal→记录日志。

## ④ 真实案例
某咖啡店 WAP 出厂默认开 WPS、SSID 还是厂商名、用 WPA（TKIP）。攻击者用 Reaver 类工具 4 小时爆出 WPS PIN 连入，再抓 WPA 握手包离线破解。整改：关 WPS、升 WPA3、改复杂 SSID、强制 captive portal + VPN。

## ⑤ 考试怎么考
- WEP/WPA/WPA2/WPA3 加密算法与安全性（WEP 秒破、WPA 不安全、WPA2 AES-CCMP、WPA3 SAE）。
- WPA3 的 SAE 与 802.11w 管理帧保护。
- KRACK 攻击针对 WPA2 密钥交换；WPS PIN 可被爆破。
- 802.1X/EAP 企业认证、RADIUS/TACACS+ 端口。
- 关 SSID 广播≠真正安全（仍可在帧中嗅到）。

## ⑥ 记忆口诀
> **「WEP 纸锁、WPA 破、WPA2 用 AES、WPA3 上 SAE」**
> **「WPS 默认开，部署先关掉；SSID 广播关了也白关」**
> **「RADIUS 一八一二、TACACS 四十九」**

## ⑦ 自测
1. WPA3-PER 用什么机制替代了 WPA2 的预共享密钥（PSK）？（答：SAE 同时等值认证，基于 Dragonfly/零知识证明）
2. KRACK 攻击针对的是哪个 Wi-Fi 标准的哪部分？（答：WPA2 的密钥重安装/密钥交换过程）
3. 关闭 SSID 广播能否真正隐藏无线网？（答：不能，SSID 仍出现在已连客户端与 WAP 的帧中，可被嗅探发现）
