---
title: Ch2-02 人事安全（下）：持续监督与第三方控件
parent: 第 2 章
grand_parent: CISSP 认证安全工程师知识库
nav_order: 2
---

# Ch2-02 人事安全（下）：持续监督与第三方控件

> 所属：Chapter 2 Personnel Security and Risk Management Concepts（Domain 1）
> 加厚标准：原书定义 + 对比表 / 真实案例 / 考试怎么考

## ① 一句话秒懂
人在职期间，权限会"越长越多"（ privilege creep），风险也随之累积。人事安全不是"招进来的时候查一次"就完事，而是要**持续盯、定期转、管好外部人**。

## ② 生活类比
给员工权限像发公司信用卡：刚发时额度刚好够出差。但几年后，他兼了三个项目、调了两次岗，额度悄悄涨到能买服务器——这就是"权限漂移"。财务要定期查账单、调额度；安全也要定期审计权限，拉回到"刚好够用"。

## ③ 核心概念（大白话 + 原书定义）

**A. 在职监督（Employee Oversight）**
| 概念 | 原书定义 / 要点 | 考试意义 |
|---|---|---|
| **特权漂移 Privilege Creep** | 工作职责/权限随时间悄悄扩张，超出实际需要 | 增加 CIA 风险；需用**最小权限**回拉 |
| **强制休假 Mandatory Vacations** | 每年 1–2 周离岗且无远程访问，由他人（审计者）代行职责 | 一种**同事审查（peer review）**，易发现欺诈/滥用；不共享密码，而是为审计者建同等权限账户 |
| **职责分离 Separation of Duties** | 关键操作分给多人，无人能独揽全流程 | 直接降低**串谋 Collusion**（多人合谋犯罪）可能性 |
| **工作轮换 Job Rotation** | 定期换岗 | 与交叉培训配合，提升韧性、降低单点依赖与合谋风险 |
| **UBA / UEBA** | 用户行为分析 / 用户+**实体**（设备、系统、网络）行为分析 | 用于检测异常、改进人事安全策略 |

**B. 第三方控件（Vendor / Consultant / Contractor）**
- **多方风险 Multiparty Risk**：多实体参与项目时，因目标/预算/安全优先级不同而生的风险；常需设立治理机构统一约束。
- **SLA（服务等级协议）**：确保服务商维持约定水平；常含**财务救济**（如关键线路中断超 15 分钟，服务商免收一周费用）。适用于线路、应用、云等任何第三方服务。
- **外包 Outsourcing**：用外部第三方替代内部执行，本质是风险**转移（transference）**，但会**扩大攻击面、引入新风险**——需权衡。
- **VMS（供应商管理系统）**：集中管理供应商关系，可保密通信、要求加密认证、留存详细活动日志。

## ④ 考试怎么考（题型 + 必记混淆）
- **题型 A（目的匹配）**：问"强制休假的主要目的是？"——答案是**检测欺诈/滥用（peer review）**，不是惩罚员工。
- **题型 B（防串谋）**：问"用什么降低 collusion？"——**separation of duties + job rotation + mandatory vacation**。
- **5 个必记混淆项**：
  1. **Mandatory vacation ≠ 惩罚**：它是审计/审查机制。
  2. **强制休假期间不共享密码**：应为审计者新建同等权限账户或重设密码。
  3. **外包是 transference 但非零风险**：转移了内部运营风险，却引入第三方风险与更大攻击面。
  4. **SLA 含财务罚则**：中断超约定阈值，服务商需补偿（如免单）。
  5. **UEBA 的 E = Entity**：比 UBA 多了设备/系统/网络等"实体"行为。

## ⑤ 真实案例
某金融机构要求财务岗每年强制休假两周。一名会计常年掌管的转账流程，在其休假、由同事代行时被发现：他通过虚构供应商持续侵吞资金已三年。强制休假的"代行+审查"机制，正是戳破这类长期欺诈的关键设计。

## ⑥ 自测
1. （单选）The primary purpose of mandatory vacations is to:
   A. Punish underperforming employees
   B. Provide peer review to detect fraud/abuse
   C. Reduce training costs
   D. Enforce separation of duties
   **答案：B**
2. （单选）Outsourcing a business function is an example of which risk response?
   A. Mitigation  B. Acceptance  C. Transference  D. Avoidance
   **答案：C**

---
*注：本篇定义以 Sybex CISSP OSG 10th (2024) Chapter 2 原书为准；mandatory vacation 目的、separation of duties 防 collusion、outsourcing=transference 为高频考点。*
