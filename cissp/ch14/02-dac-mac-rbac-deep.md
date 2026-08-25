---
title: 02 · DAC / MAC / RBAC 深入（三种主力模型）
parent: 第 14 章
grand_parent: CISSP 认证安全工程师知识库
nav_order: 2
---

# 02 · DAC / MAC / RBAC 深入（三种主力模型）

## 一句话秒懂
DAC 灵活但易乱（每人自管）；MAC 最严（标签+格点，政府军用）；RBAC 最实用（按组赋权，企业标配）。三者是考试最高频。

> 对应原书：Chapter 14 — "Discretionary / Mandatory / Role-Based Access Control"

## 生活类比
- DAC：你新建文档，自己决定共享给谁——方便但同事乱授权会失控。
- MAC：保密文件贴"机密"标签，你没"机密" clearance 物理上拿不到，系统替你决定。
- RBAC：公司把"贷款专员"组配好权限，新人入组即生效、调走移出即失效。

## 核心概念（大白话 + 原书定义）

**DAC（自主访问控制）**：
- 对象有主人（owner/creator/custodian），主人定义访问。NTFS 用 DAC，每文件/文件夹有 ACL（DACL）列用户/组权限，主人可改。
- **Identity-based access control 是 DAC 子集**（按身份标识 + 资源归属）。
- 优点：极灵活，改权限容易。缺点：无集中管控，权限易蔓延。

**Nondiscretionary（非自主，含 MAC/RBAC/Rule/ABAC）**：管理员集中管控，改一处影响全局；不聚焦用户身份而用静态规则集；更易管理审计，但不灵活。

**RBAC（基于角色）**：
- 按岗位/工作任务定义角色，权限赋角色，用户进组即得。银行例：Loan Officers / Tellers / Managers 三组。
- **防 privilege creep**：直接赋权难找全，移出组即秒撤。动态环境（人事变动频繁）特别适合。
- 用户可属多角色（经理可同时属三个组）。Windows 用组实现；严格 RBAC 不直接给用户赋权，只通过角色。
- **DAC 与 RBAC 易混**（都用组）：DAC 中对象有主人决定访问；RBAC 中管理员决定主体权限并赋给角色/组。
- 相关 **TBAC（基于任务）**：按任务数组而非角色（如 MS Project 每人管自己任务）。

**MAC（强制访问控制）**：
- 主体/客体都贴**分类标签**（政府：Top Secret/Secret/Confidential/Unclassified；私营：Confidential/Proprietary/Private/Sensitive/Public）。
- **Lattice-based（格点模型）**：如图表边界（Public→Sensitive→Private→Confidential），标敏感等级；还可**隔间（compartment）**细分（如 Confidential 下 Lentil/Foil/Crimson/Matterhorn），需"等级标签 + 隔间标签"双匹配 → 强制 need-to-know。
- 环境三型：**Hierarchical（等级）**（高级 clearance 含低级，如 TS 可看 S）、**Compartmentalized（隔离）**（域间无关，须特定 clearance）、**Hybrid（混合）**（等级内含隔离，最细但难管）。
- 性质：**prohibitive 而非 permissive**，隐式拒绝；比 DAC 安全但不灵活可扩展。

> 口诀：**"DAC 主人改 ACL，灵活无序；MAC 标签配格点、隔间强制需知；RBAC 组赋权、移出即撤防蠕变。"**

## 真实案例
军工单位用 MAC：文档贴 Secret 标签，员工须有对应 clearance + 对应 compartment 标签才能看（强制需知）。民企用 RBAC：HR 系统按"招聘/薪酬/员工关系"角色组赋权，员工转岗移组即撤旧权，杜绝权限蠕变。

## 考试怎么考
- DAC 的实现（NTFS/ACL）与优劣。
- MAC 的标签机制、lattice、compartment、hierarchical/compartmentalized/hybrid 环境。
- RBAC 如何防 privilege creep、与 DAC 的区别。
- 政府标签等级（TS>S>C>U），高级 clearance 含低级（hierarchical）。
- TBAC 概念。

## 记忆口诀
> **"DAC 灵活主人管，MAC 标签格点严；RBAC 组赋权、撤组即收权，隔间强制需知念。"**

## 自测
1. DAC 与 RBAC 都用"组"，本质区别在哪？
2. MAC 中 lattice-based 与 compartment 各是什么？如何强制 need-to-know？
3. MAC 的三种环境（hierarchical/compartmentalized/hybrid）区别？
4. RBAC 如何防止 privilege creep？
5. 政府 MAC 标签等级从高到低？高级 clearance 是否自动含低级（hierarchical 下）？
