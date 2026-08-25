---
title: Ch2-01 人事安全（上）：雇佣生命周期——筛选、入职、离职
parent: 第 2 章
grand_parent: CISSP 认证安全工程师知识库
nav_order: 1
---

# Ch2-01 人事安全（上）：雇佣生命周期——筛选、入职、离职

> 所属：Chapter 2 Personnel Security and Risk Management Concepts（Domain 1 安全与风险管理）
> 加厚标准：原书定义 + 对比表 / 真实案例 / 考试怎么考，约 800–1200 字

## ① 一句话秒懂
安全圈有句老话：**人是最薄弱的环节**。再强的防火墙，也挡不住员工把密码写在便利贴上——所以人事安全（Personnel Security）管的是"人从进公司到离开"的全过程。

## ② 生活类比
把公司想成一座城堡。技术控制（墙、门、锁）是砖石，但**每天开城门放人进出的，是卫兵和规矩**。人事安全就是"选卫兵、定规矩、换了卫兵就立刻收钥匙"的一整套流程。选错人、规矩松、离职不收钥匙——城堡就从内部破了。

## ③ 核心概念（大白话 + 原书定义）

人事安全覆盖一个人在组织的**完整生命周期**：招聘 → 入职 → 在职 → 离职/转岗。每一段都有安全动作：

| 阶段 | 关键动作 | 原书要点 |
|---|---|---|
| **工作描述 Job Description** | 定义角色与职责 | 职责决定"该给什么权限"，是权限分配的依据；需持续维护、定期审计 |
| **筛选 Screening** | 背景调查 | 严格程度应与**职位敏感度**匹配：教育核实、推荐人、犯罪记录、指纹/证件；在线背景检查要注意**反歧视法律** |
| **入职 Onboarding** | 发放身份与签协议 | 经 IAM 系统开通账户，按**最小权限**赋权；签署雇佣协议、AUP、NDA、NCA |
| **离职 Offboarding** | 收回身份 | 从 IAM **移除身份**，停用/删除账户（常先停用保留数月以备查）；收回所有公司财产 |

**三个核心法律文档（考试常考）：**
- **AUP（可接受使用策略）**：规定公司设备/资源"什么能用、什么不能用"，违者可能警告、处分乃至解雇。
- **NDA（保密协议）**：防止在职/离职员工泄露机密。分三类——**单边（one-way）**一方保护；**双边（mutual）**双方互保；**多边（multilateral）**三方及以上互保。
- **NCA（竞业限制，non-compete）**：限制离职后一段时间内去竞争对手处，执行力因地区法律而异。

**最小权限原则（Principle of Least Privilege）**：只给用户"完成工作所必需的最小权限"。这是人事安全与访问控制共通的铁律。

**离职的黄金顺序**：先**当面通知**员工 → 当场提醒其 NDA/协议义务、收回门禁卡/设备/钥匙 → 再停用账户。关键陷阱见下文。

## ④ 考试怎么考（题型 + 必记混淆）
- **题型 A（排序/流程）**：问"termination 的正确步骤顺序"——答案一定是**先通知、再收财产、最后禁用账户**，而非反过来。
- **题型 B（匹配）**：给场景选 NDA 类型（单边/双边/多边）。
- **5 个必记混淆项**：
  1. **NDA vs AUP**：NDA 防"泄密"，AUP 管"怎么用设备"，两者不同。
  2. **离职前禁用账户是大忌**：在通知前就停用账号/收回设备/发新组织架构图，等于给员工"提前预警"，可能引发破坏。
  3. **Offboarding 常先"停用"而非立即"删除"**：保留身份数月以便审计追溯；过早删除会让安全事件日志失去指向。
  4. **内部转岗 ≠ 甩锅**：不应把"问题员工"调到别的部门代替解雇。
  5. **NCA 可执行性因地而异**：不是所有地区都强制有效，需法律确认。

## ⑤ 真实案例
某公司在解雇一名运维前，IT 先把他的门禁卡停用、账号冻结——员工察觉后，在正式通知前远程删除了部分日志并带走配置文档。这就是"提前动作泄露终止意图"的反面教材。正确做法：终止会议当场、证人（经理/保安）在场、收齐财产、最后才由 IT 停用账户。

## ⑥ 自测
1. （单选）Which is the correct sequence for a termination?
   A. Disable account → notify employee → collect property
   B. Notify employee → collect property → disable account
   C. Collect property → disable account → notify employee
   D. Disable account → collect property → notify employee
   **答案：B**
2. （单选）A contract where both parties agree to protect each other's confidential info is a:
   A. Unilateral NDA  B. Bilateral NDA  C. AUP  D. NCA
   **答案：B**

---
*注：本篇定义以 Sybex CISSP OSG 10th (2024) Chapter 2 原书为准；NDA 三分类、最小权限、offboarding 顺序为考试高频点。*
