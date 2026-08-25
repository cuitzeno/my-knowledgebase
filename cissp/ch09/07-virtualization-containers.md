---
title: Ch9-07 虚拟化与容器化
parent: 第 9 章 · 安全漏洞、威胁与对策
grand_parent: CISSP 认证安全工程师知识库
nav_order: 7
---

# Ch9-07 虚拟化与容器化

> 所属域：Domain 3 Security Architecture and Engineering
> 对应原书：Chapter 9 — Virtualized Systems / Containerization / SDx

## ① 一句话秒懂
虚拟化用**虚拟机监控器（hypervisor）**在一台物理机上跑多台虚拟机；容器更轻量共享 OS 内核。二者都带来弹性/隔离好处，但也引入**VM 逃逸、VM 蔓延、影子 IT** 等新风险。

## ② 生活类比
Type I 裸金属 hypervisor 像直接在空地上盖楼（无 Host OS 中介）；Type II 托管型像在商场里隔出商铺（先有 OS 再装 hypervisor）。容器像在同一栋楼里用隔板分出的独立房间——共享地基（OS 内核）但彼此隔离。

## ③ 核心概念（大白话 + 原书定义）

**虚拟化（Virtualization）**
在单台主机内存中托管一个或多个 OS，或运行不兼容主机 OS 的应用。可大幅省成本（如 100 台物理机→10 台物理机各跑 10 个 VM）。

**Hypervisor（虚拟机监控器/VMM）**
创建、管理、运行 VM 的组件。跑 hypervisor 的叫 **Host OS**，VM 内的叫 **Guest OS / 虚拟化系统**。
- **Type I（原生/裸金属）**：无 Host OS，hypervisor 直接装硬件（常用于服务器虚拟化，最大化资源、无 Host OS 开销/风险）。
- **Type II（托管型）**：先有常规 OS，再装 hypervisor 作应用（常用于桌面，提供沙箱测代码、跑遗留应用）。

**弹性 vs 可扩展性（Elasticity vs Scalability）**
- **Elasticity（弹性）**：按当前需求扩/缩资源（尤其云），短期、平台/硬件特征（如 VM 按需占用闲置 CPU）。
- **Scalability（可扩展性）**：长期承担更多任务的能力，软硬件特征。
- 关系：可扩展系统须弹性，但弹性系统不一定可扩展。

**虚拟化安全收益**
VM 备份/快照（snapshot/checkpoint）易做；出错分钟级用快照恢复；恶意感染很少影响 Host（VM-VM、VM-Host 隔离）；可安全测可疑代码；支撑 EOL/EOS 遗留 OS。

**虚拟化安全要点**
- Hypervisor 是额外攻击面；攻陷 Host 即可触所有 Guest——须**加固主机**。
- 补丁管理仍必要：Guest OS 各自更新（更新 Host 不更新 Guest），Hypervisor 也要更新。
- Host 只做托管，保 Host 稳定即保 VM 可用。
- 备份 VM + 定期快照做时间点恢复。
- 虚拟化 OS 同硬件 OS 一样做漏洞评估/渗透测试。

**VM 蔓延（VM Sprawl）**：无管控地大量建 VM，导致许可/安全管理跟不上、虚拟影子 IT。对策：建 VM 开发部署策略 + 基础镜像库。
**服务器蔓延（Server Sprawl）/ 影子 IT（Shadow IT）**：部门绕过 IT 自部署组件（物理/虚拟/云），不守策略、无补丁、无文档、不可靠，大幅增泄露风险。别名：embedded IT、feral IT、stealth IT 等。
**VM 逃逸（VM Escape）**：Guest 内软件突破 hypervisor 隔离，侵入其他 Guest 或 Host。例：VENOM（CVE-2015-3456）借恶意虚拟软驱跨 VM 乃至触 Host。厂商通常快速补丁。

**容器化（Containerization）**
虚拟化的衍生：应用容器（application cells/containers）虚拟化软件使之可移植到几乎任何 OS。有的容器允许多应用并发，有的限每容器一个。比 hypervisor 密度更高。

**SDx（软件定义一切）**：虚拟化服务器/网络之外，以软件替硬件。含 SDN、VSAN、SDS、VDI、VMI、SDV、SDDC、IaaS、XaaS、IaC 等。

## ④ 真实案例
- VENOM 漏洞使多家 hypervisor 的 VM 可跨机逃逸，厂商紧急发补丁。
- 企业用 Type I 将百台服务器整合为十台，省电省空间，但 Host 加固成重点。
- 影子 IT：部门私自开云实例跑业务，漏在安全视野外致数据泄露。

## ⑤ 考试怎么考
- Type I vs Type II hypervisor 区别（裸金属 vs 托管）。
- Elasticity（短期按需）vs Scalability（长期承载）。
- 虚拟化新风险：VM 蔓延、影子 IT、VM 逃逸（VENOM 例）。
- 攻陷 Host 即触所有 Guest——须加固 Host、各自补丁 Guest 与 Hypervisor。
- 容器比 hypervisor 密度更高。

## ⑥ 记忆口诀
- Type I 裸金属直接装，Type II 先 OS 后装；Host 被控全 Guest 危。
- 弹性短期按需变，扩展长期承载多；可扩展必弹性，弹性未必扩。
- VM 蔓延影子 IT，逃逸 VENOM 是警钟；容器更密共享核。

## ⑦ 自测
1. Type I 与 Type II hypervisor 的核心区别？
2. Elasticity 与 Scalability 有何不同？二者关系？
3. 什么是 VM 逃逸？举一个真实漏洞例子。
4. 虚拟化环境下补丁管理的三个层面（Guest / Host / Hypervisor）为何各自独立？
