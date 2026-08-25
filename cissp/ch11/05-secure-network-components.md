---
title: 05 · 安全网络组件（Ch11 · Domain 4）
parent: 第 11 章 · 安全网络架构与组件
grand_parent: CISSP 认证安全工程师知识库
nav_order: 5
---

# 05 · 安全网络组件（Ch11 · Domain 4）

> 内网、外网、DMZ 怎么划？Hub/Switch/Router 各管什么域？跳板机、传感器、收集器是什么角色？这一篇把「网络里的硬件与逻辑部件」梳理清楚。

## ① 一句话秒懂
Intranet 是自家庭院，Extranet 是给合作伙伴开的侧门，Screened Subnet（DMZ）是大门口的会客室——低信任客人只能进会客室，进不了内院。

## ② 生活类比
- **Intranet（内网）**：只家人进的私宅。
- **Extranet（外网/伙伴网）**：给固定供应商开的偏门，特定人能进特定房间。
- **Screened Subnet / DMZ（屏蔽子网/隔离区）**：大门口会客室，外人（公共用户）只能在这见 Web 服务器，进不了内宅。

## ③ 核心概念（大白话 + 原书定义）

**私网分段两类**：
- **Intranet**：私有 LAN，托管内部 Web/邮件等，外部不可达。
- **Extranet**：组织网络划出一段，既像内网又服务授权外部实体（伙伴、供应商、远程销售）。公用的 extranet 通常叫 screened subnet / perimeter network。
- **Screened Subnet（旧称 DMZ）**：专用 extranet，给低信任/未知用户访问特定系统（如公共 Web 服务器）。部署方式：双防火墙（Internet↔子网↔Intranet）或单多宿主防火墙（三个接口）。
- **Screened Host**：防火墙保护、逻辑上位于网段内侧的系统，所有入站流量经它代理，隐藏内部身份。

> 原书补充：*"East-west traffic refers to traffic within a network/data center/cloud; North-south traffic refers to inbound/outbound between internal and external systems."*（东西向=内部横向流量；南北向=内外进出流量。）

**常见网络设备与层级**：
- **RCA（中继器/集中器/放大器）**：L1，同冲突域同广播域。
- **Hub（集线器）**：多端口中继器，L1，同冲突域同广播域。
- **Bridge（网桥）**：L2，连不同拓扑网段，存储转发（store-and-forward）。
- **Switch（交换机）**：基于 MAC 转发帧，主 L2，划 VLAN 可造广播域；三层交换机可路由（L3）。
- **Router（路由器）**：基于 IP 路由，L3，分割广播域。
- **MPLS**：用短标签而非长地址路由，高效。
- **Jumpbox/Jump Server（跳板机）**：部署在 extranet/DMZ/云中，便于安全访问特定系统，应只用加密连接（常为带外 out-of-band）。
- **Sensor（传感器）**：采集信息回传中心，常见于雾计算/ICS/IoT/IDS/SOAR，多基于 SoC。
- **Collector（收集器）**：把数据汇成日志/记录文件。

**碰撞域 vs 广播域**：
- 碰撞域（collision domain）：可能同时发送导致冲突的一组设备，任何 L2+ 设备可分割。
- 广播域（broadcast domain）：一个成员广播、其他都收到的一组设备，任何 L3+ 设备可分割。

**硬件安全运行**：冗余电源（failover，常各承担一半、坏一个顶 100%）、保修/退换政策、厂商技术支持（VPN 设备/防火墙/交换机配置常需认证）。

## ④ 真实案例
某企业把对外 Web 服务器直接放在内网，黑客拿下 Web 后横向移动（东西向流量无隔离）直达数据库。整改后把 Web 放入 DMZ（双防火墙隔离），内部数据库只在 Intranet，即使 Web 失陷也无法直连内网——这就是 screened subnet 的隔离价值。

## ⑤ 考试怎么考
- Intranet/Extranet/DMZ/Screened Host 定义与区别。
- 设备分层（Hub L1 / Switch L2 / Router L3）及域分割能力。
- 东西向 vs 南北向流量。
- Jumpbox 用途与安全要求（加密、常带外）。
- 碰撞域 vs 广播域由哪层设备分割。

## ⑥ 记忆口诀
> **「内网自家庭院，外网开偏门，DMZ 会客室，跳板机管远程」**
> **「Hub 一层、交换二层、路由三层；L2 分碰撞、L3 分广播」**

## ⑦ 自测
1. 想把广播域分割开，至少需要什么层级的设备？（答：L3 或更高，如路由器或三层交换机）
2. 双防火墙部署 DMZ 时，两个防火墙分别隔在哪之间？（答：Internet↔DMZ、DMZ↔Intranet）
3. 东西向流量指什么？（答：网络/数据中心/云内部的横向流量）
