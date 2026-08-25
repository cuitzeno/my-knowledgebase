---
title: 03 · 交换、VLAN 与 NAT
parent: 第 12 章 · 安全通信与网络攻击
grand_parent: CISSP 认证安全工程师知识库
nav_order: 3
---

# 03 · 交换、VLAN 与 NAT

## 一句话秒懂
交换机用 MAC 表决定"往哪发"；VLAN 是交换机划出的逻辑隔离区；NAT 把一堆内网私有地址"伪装"成一个公网地址上网——三者都是网络分段与隐藏内部结构的利器。

> 对应原书：Chapter 12 — "Switching and Virtual LANs" / "Network Address Translation"

## 生活类比
- **交换机/CAM 表**：快递员记住"每户门牌对应哪条楼道"，新来的查不到就全楼道喊一声（flooding）。
- **VLAN**：同一栋楼里用防火门把财务层和访客层隔开，互不串门，除非走楼梯（路由）。
- **NAT**：整栋楼共用一个对外门牌号，外面只知道这个号，不知道里面谁是谁。

## 核心概念（大白话 + 原书定义）

**交换机四功能**：learning（学源 MAC 进 CAM 表）、forwarding（目的 MAC 在表且端口不同则转发）、dropping（同端口丢弃）、flooding（目的 MAC 不在表则全端口发）。交换机主要工作在 L2，带 L3 功能叫多层交换机。

**VLAN（Virtual LAN）**：交换机强制实现的**硬件网络分段**。默认所有端口在 VLAN 1（通常作为管理 VLAN）。同 VLAN 通信无阻，跨 VLAN 需路由（外部路由器或 L3 交换机）。VLAN 是**逻辑**分段，不改物理拓扑，易实施、开销小。可按端口/MAC/IP 子网/协议/认证划分。**"默认拒绝、例外允许"**不仅适用于防火墙，也适用于 VLAN 间策略。

**VLAN 安全价值**：限制广播域、抑制广播风暴、降低嗅探面。端口隔离（private VLAN / port isolation）常见于酒店：每间房独立 VLAN，只能互访+上联互联网。

**端口镜像（SPAN）**：把指定端口流量复制出来做分析/抓包/IDS——注意这是**被动监控**，不改动流量。端口分流器（port tap）则在 SPAN 不够用时物理串接抓包。

**攻击与防御**：
- **VLAN hopping（双层标签攻击）**：攻击者构造双 VLAN 标签，老交换机只认第二个标签而被骗跨 VLAN → 防御：所有非 trunk 端口设为 access 模式、禁止原生 VLAN 混用。
- **MAC flooding**：狂发随机源 MAC 把 CAM 表填满，交换机退化为集线器（全端口 flood）→ 防御：**MAC limiting**（每端口限制 MAC 数）+ NIDS。
- **MAC spoofing/cloning**：改软件层 MAC 冒充授权设备绕过端口安全/MAC 过滤 → 防御：智能交换机监测 + 设备 MAC 资产清单。

**NAT（Network Address Translation）**：把内网私有 IPv4 换成出口公网 IP，**隐藏内部拓扑**、节省公网地址、并充当"单向防火墙"（只允许内部发起的回包进来）。RFC 1918 私有地址：10.0.0.0/8、172.16.0.0/12、192.168.0.0/16。**默认路由器不路由这些私有地址**。

**PAT（端口地址转换，aka 过载 NAT / NAPT）**：用传输层端口号让**一个公网 IP 支撑约 65536 个并发会话**（实际建议 ≤4000）。业界说的"NAT"多半指 PAT。SNAT=源 NAT；静态 NAT/DNAT/端口转发=允许外部主动连入内网（一般不推荐，仅 screened subnet/extranet 可用）。

**NAT-T（NAT 穿越，RFC 3947）**：传统 NAT 破坏 IPSec 包头，NAT-T 让 IPSec/L2TP 与 NAT 共存于同一边界设备。

**NAT66**：IPv6 版本的地址转换，主要用于地址节约与隐藏内部，但 IPv6 设计本意是端到端无需转换，存在争议。

> 口诀：**"VLAN 逻辑隔，trunk 用 802.1q；CAM 满就 flood，MAC 限量防；NAT 藏内网，PAT 多路复用一个公网。"**

## 真实案例
某园区网按部门划 VLAN（财务 VLAN、研发 VLAN、访客 VLAN），访客 VLAN 无法访问内部服务器；出口路由器做 PAT，整公司几百人共用 2 个公网 IP 上网，外部扫描只能看到路由器，摸不到内网。

## 考试怎么考
- VLAN 是逻辑分段、非子网；跨 VLAN 必须路由。
- VLAN hopping / MAC flooding / MAC spoofing 的攻击原理与对策。
- NAT 的三大好处 + 单向防火墙特性；PAT 与 NAT 区别；RFC 1918 三段地址。
- 静态 NAT（DNAT）的风险。
- NAT-T 的作用。

## 记忆口诀
> **"交换机四动作：学转丢泛；VLAN 隔广播、跨域要路由；NAT 藏内网、PAT 一公网带千会话。"**

## 自测
1. 同 VLAN 与跨 VLAN 通信的区别？跨 VLAN 靠什么？
2. VLAN hopping 攻击利用了什么？如何防御？
3. MAC flooding 攻击如何让交换机变"集线器"？
4. NAT 与 PAT 的核心区别？RFC 1918 私有地址有哪三段？
5. 静态 NAT（端口转发）为什么一般不建议用于内网？
