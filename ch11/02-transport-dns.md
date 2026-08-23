# 02 · 传输层协议与域名系统 DNS（Ch11 · Domain 4）

> 传输层负责「端到端」把数据送到对的应用进程，DNS 则负责把人友好的名字翻译成机器用的 IP。两者是网络通信的「门牌号 + 快递员」组合。

## ① 一句话秒懂
TCP 是「打电话」（先接通、确认收到、不乱序），UDP 是「发传单」（扔出去就完、不管你收没收到）；DNS 是「查通讯录」，把 www.xxx.com 翻译成 1.2.3.4。

## ② 生活类比
- **TCP** 像挂号信：寄之前先确认对方在、每封信编号、丢了重发、对方按顺序拼好。
- **UDP** 像广场喊话：喊完就走，爱听不听，但快。
- **DNS** 像手机通讯录：你只记「老妈」，手机帮你查出她的号码（IP）才能拨通。

## ③ 核心概念（大白话 + 原书定义）

**TCP（Transmission Control Protocol）**：
- 面向连接、可靠、有序、有流量控制和拥塞控制。
- 三次握手建立连接，用序列号保证顺序，确认重传保证可靠。
- 端口示例：TCP 22(SSH)、80(HTTP)、443(HTTPS)、25(SMTP)、110(POP3)、143(IMAP)、21(FTP 控制)。

**UDP（User Datagram Protocol）**：
- 无连接、不可靠、低开销、速度快。原书：*"does not use sequencing, does not use flow control... considered unreliable. UDP has very low overhead."*
- 适合实时音视频。端口：UDP 53(DNS 查询)、69(TFTP)、67/68(DHCP)、1812/1813(RADIUS)。

**DNS（Domain Name System）**：
- 层次化命名系统，把 FQDN 解析为 IP。FQDN 三部分：TLD（如 com）+ 注册域名（如 google）+ 子域/主机（如 www）。
- 资源记录（RR）：A(IPv4)、AAAA(IPv6, aka DNSv6)、PTR(反向)、CNAME(别名)、MX(邮件)、NS(名称服务器)、SOA(起始授权)。
- 解析流程：先查本地缓存（含 hosts 文件）→ 否则问配置的 DNS 服务器。DNS 用 TCP/UDP 53，UDP 53 用于普通查询，TCP 53 用于区域传送（zone transfer）或响应 >512 字节。

**MAC 与 IP 的「永久/临时」**：
- MAC 是「永久」物理地址（但可被 MAC 欺骗/spoofing 修改）；IP 是「临时」逻辑地址（DHCP 或手动改）；主机名/DNS 名也是逻辑、可变。

## ④ 真实案例
2018 年某公共 Wi-Fi 下，攻击者搭建恶意 DNS 服务器监听查询，用正确 QID（16 位查询 ID）抢先回复假 IP，把用户 `bank.com` 引到钓鱼站点——这就是 DNS 缓存投毒 + AitM 的组合利用。防御靠 DNSSEC + DoH。

## ⑤ 考试怎么考
- 给场景问该用 TCP 还是 UDP（可靠选 TCP，实时选 UDP）。
- DNS 记录类型配对（A/AAAA/PTR/MX/CNAME 各自做什么）。
- TCP 53 vs UDP 53 的用途区别（区域传送用 TCP）。
- 端口号对应（尤其 53、443、22、25、67/68 等）。
- MAC 欺骗、DNS 缓存投毒的攻击原理与防御。

## ⑥ 记忆口诀
> **「TCP 可靠 UDP 快，DNS 53 把名解」**
> **「A 配四、AAAA 配六、PTR 反向、MX 管邮」**——资源记录一句话。
> **「UDP 查、TCP 传（区域传送）」**——53 端口双身份。

## ⑦ 自测
1. 视频会议用 TCP 还是 UDP 更合适？为什么？（答：UDP，实时性优先、丢包可容忍）
2. 一台 DNS 从另一台拉取全量 zone 文件，走哪个端口和协议？（答：TCP 53，区域传送）
3. 攻击者改了本机 MAC 地址伪装成另一台设备，这叫什么？（答：MAC spoofing / MAC cloning）
