---
title: 04 · 多层协议与融合/汇聚协议（Ch11 · Domain 4）
parent: 第 11 章
grand_parent: CISSP 认证安全工程师知识库
nav_order: 4
---

# 04 · 多层协议与融合/汇聚协议（Ch11 · Domain 4）

> 多层协议用「封装套娃」带来灵活与加密能力，但也被攻击者用来开隐蔽通道；融合协议则把专用协议塞进标准 TCP/IP，省硬件又扩能力。

## ① 一句话秒懂
封装就像俄罗斯套娃：一层套一层。好处是能在任意层加加密；坏处是攻击者能把禁用的协议（如 FTP）藏进允许的协议（如 HTTP）偷运过去——这叫隐蔽通道。

## ② 生活类比
公司规定「不准寄包裹（FTP），只能寄信（HTTP）」。攻击者把包裹塞进信信封里寄出去（HTTPTunnel），门卫只看是「信」就放行了——这就是利用多层封装绕过过滤。

## ③ 核心概念（大白话 + 原书定义）

**多层封装（Multilayer Encapsulation）**：
- 经典 Web 通信：`[ Ethernet [ IP [ TCP [ HTTP [数据] ] ] ] ]`
- 加 TLS：`[ Ethernet [ IP [ TCP [ TLS [ HTTP [数据] ] ] ] ] ]`
- 再加 IPSec（网络层加密，即 VPN）：`[ Ethernet [ IPSec [ IP [ TCP [ TLS [ HTTP [数据] ] ] ] ] ] ]`

**多层协议的优缺点**：
- 优点：高层可用多种协议；可在各层加加密；复杂拓扑下更灵活 resilient。
- 缺点（原书直引）：*"Covert channels are allowed. Filters can be bypassed. Logically imposed network segment boundaries can be overstepped."*（允许隐蔽通道、可绕过过滤器、可跨越逻辑网段边界。）

**隐蔽通道（Covert Channel）示例**：
- HTTPTunnel：把 FTP 藏进 HTTP（`[ Ethernet [ IP [ TCP [ HTTP [ FTP [数据] ] ] ] ] ]`）。
- Loki：把 TCP 藏进 ICMP（`[ Ethernet [ IP [ ICMP [ TCP [ HTTP [数据] ] ] ] ] ]`），ICMP 本是探活用，被改成隧道。

**融合/汇聚协议（Converged Protocols）**：把专用/私有协议合并进标准 TCP/IP，复用现有基础设施。
- **SAN（存储区域网）**：独立二级网络整合存储，单一故障点，需冗余；去重可能致数据丢失。
- **iSCSI**：基于 IP 的存储标准，工作在 Layer 5（会话层），被视为 Fibre Channel 低成本替代。
- **IBoE（InfiniBand over Ethernet）**：把 InfiniBand 封装进以太网帧。
- **CXL（Compute Express Link）**：高速互联 CPU/GPU/内存/加速器。
- **VoIP**：把音视频封装进 IP 包，替代 PSTN。风险：Caller ID 伪造（vishing/SPIT）、AitM、未加密可被窃听；SRTP 提供加密。
- 其他融合概念：VPN、SDN、云、虚拟化、SOA、微服务、serverless。

**SDN（软件定义网络）**：分离控制平面（决定往哪发）与数据平面（决定转不转发），集中可编程、厂商中立。南向接口（控制器→设备）、北向接口（控制器→应用）。与 NFV（网络功能虚拟化）结合实现网络虚拟化。关联概念：VSAN、SDS、SD-WAN。

## ④ 真实案例
某隔离网禁止 FTP 但允许 HTTP。运维为图方便用 HTTPTunnel 把数据库备份（本应走加密通道）伪装成 HTTP 流量传走，绕过了 DLP 检测。审计发现后，改用明令允许的加密 VPN 通道并部署应用层防火墙，堵住隐蔽通道。

## ⑤ 考试怎么考
- 给一个封装结构，判断哪层加了加密、是否构成 VPN/隐蔽通道。
- 多层协议三大缺点（隐蔽通道、绕过过滤、越界）几乎必考。
- 融合协议举例：SAN/iSCSI/IBoE/VoIP/SDN 各自作用与所在层（iSCSI 在 L5）。
- VoIP 安全风险与 SRTP 防护。

## ⑥ 记忆口诀
> **「套娃能加密，也能偷运货；隐蔽通道三宗罪：偷传、绕过滤、越边界」**
> **「iSCSI 在五层，SAN 存数据，VoIP 替电话，SRTP 保安全」**

## ⑦ 自测
1. 多层协议被攻击者利用的主要风险是哪三点？（答：隐蔽通道、绕过过滤器、跨越逻辑网段边界）
2. iSCSI 工作在 OSI 哪一层？（答：Layer 5 会话层）
3. 用 Loki 工具把 TCP 藏进哪种协议做隧道？（答：ICMP）
