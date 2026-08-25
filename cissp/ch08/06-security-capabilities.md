---
title: Ch8-06 信息系统的安全能力
parent: 第 8 章
grand_parent: CISSP 认证安全工程师知识库
nav_order: 6
---

# Ch8-06 信息系统的安全能力

> 所属域：Domain 3 Security Architecture and Engineering
> 对应原书：Chapter 8 — Understand Security Capabilities of Information Systems

## ① 一句话秒懂
信息系统的安全能力包括**内存保护、虚拟化、TPM/HSM、受限接口、容错**，以及贯穿始终的**系统生命周期管理**。

## ② 生活类比
内存保护像给每个租客独立上锁的房间；TPM 是焊在主板上、专门保管钥匙的保险芯片；容错像双发动机飞机——一台坏了还能飞。

## ③ 核心概念（大白话 + 原书定义）

**内存保护（Memory Protection）**
OS 必须实现，防进程访问未分配给它的内存。支撑 isolation、虚拟内存、分段（segmentation）、保护环（protection rings），以及防缓冲区溢出。

**虚拟化（Virtualization）**
单机内存内跑多 OS，用于隔离、测可疑软件。详见 Chapter 9。

**TPM（Trusted Platform Module）**
主板加密处理器芯片的**规范 + 实现**，存 / 处理密钥支持本地磁盘加密。是 **HSM 的一种**。
- **HSM（Hardware Security Module）**：管理存储密钥、加速 crypto、支持数字签名、改善认证。形态：主板芯片 / 外设 / 网络设备 / 扩展卡。含**防篡改（tamper protection）**——即便物理获取也难滥用。

**受限接口（Interfaces）**
按权限限制用户能看 / 做。方法：隐藏无权限命令（不显示）、置灰（显示但不可用）、限制动作。是 **Clark-Wilson 模型的实践**。

**容错（Fault Tolerance）**
故障仍运行。靠冗余：RAID（磁盘冗余阵列）、failover cluster（故障转移集群）。是避免**单点故障（SPOF）**的关键。详见 Chapter 18。

**加解密（Encryption/Decryption）**：详见 Ch6 / Ch7。

**信息系统生命周期（9 阶段）**
1. Stakeholders' Needs（干系人需求）
2. Requirements Analysis（需求分析）
3. Architectural Design（架构设计）
4. Development / Implementation（开发 / 实现）
5. Integration（集成）
6. Verification & Validation（验证与确认：V 确保组件正确实现，V 确保整体达目的）
7. Transition / Deployment（过渡 / 部署）
8. Operations & Maintenance / Sustainment（运维 / 持续保障）
9. Retirement / Disposal（退役 / 处置，含数据处置与合规）

## ④ 真实案例
- **BitLocker**：用 TPM 存密钥，开机测量启动状态，异常则锁盘。
- **银行双活数据中心**：一个机房断电业务不中断（容错 + 免 SPOF）。

## ⑤ 考试怎么考
- **TPM 是 HSM 的一种（特例）**，HSM 更广义——别反了。
- 受限接口对应 **Clark-Wilson**。
- 容错 = 避免 SPOF、靠 RAID / failover。
- 内存保护目的（防越界、支撑隔离）。
- 生命周期阶段顺序（尤其 V&V 区别）。

## ⑥ 记忆口诀
- TPM 是 HSM 一种，焊板存钥防篡改；受限接口 Clark-Wilson，容错冗余免单点。
- 生命周期九步：需分构发集，验部退（需求 / 分析 / 架构 / 开发 / 集成 / 验证 / 部署 / 运维 / 退役）。

## ⑦ 自测
1. TPM 与 HSM 是什么关系？HSM 有哪些形态？
2. 受限接口为何说是 Clark-Wilson 模型的实践？
3. 容错靠什么实现？它主要防范什么？（SPOF）
4. 生命周期中 Verification 与 Validation 的区别？
