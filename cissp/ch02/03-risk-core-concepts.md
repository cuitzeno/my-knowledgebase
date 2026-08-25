---
title: Ch2-03 风险管理核心概念与公式
parent: 第 2 章
grand_parent: CISSP 认证安全工程师知识库
nav_order: 3
---

# Ch2-03 风险管理核心概念与公式

> 所属：Chapter 2 Personnel Security and Risk Management Concepts（Domain 1）
> 加厚标准：原书定义 + 对比表 / 真实案例 / 考试怎么考

## ① 一句话秒懂
风险管理（Risk Management）不是"消灭风险"——而是**把风险降到组织能接受的水平**。它的两半是：先**评估**风险（Risk Assessment），再**响应**风险（Risk Response）。

## ② 生活类比
给房子买保险前，你要先想清楚：房子值多少（资产）、可能遭什么灾（威胁：火灾/盗窃）、哪里不结实（漏洞：旧锁/木窗）、受灾会损失几成（暴露）。这套"盘点—算账—决定买不买锁"的流程，就是风险管理。

## ③ 核心概念（大白话 + 原书定义）

**A. 风险管理的两大组成**
| 组成 | 原书定义 | 产出 |
|---|---|---|
| **Risk Assessment 风险评估** | 检查环境找风险，评估每个威胁发生的**可能性**与造成损失的**严重程度**，并核算各对策成本 | 按严重性排序的风险清单 |
| **Risk Response 风险响应** | 用成本/收益分析评估控制，向高层提案并落地 | 实际部署的防护 |

**B. 关键术语（考试必背，易混）**
| 术语 | 原书定义 | 一句话 |
|---|---|---|
| **Asset 资产** | 任何用于业务过程的人/地/物，有形或无形 | 你要保护的东西 |
| **Threat 威胁** | 可能造成不良后果的潜在事件，可故意/意外、内部/外部 | "武器" |
| **Threat Agent/Actor** | 故意利用漏洞者（人/程序/系统），aka attacker | "拿武器的人" |
| **Vulnerability 脆弱性** | 资产或防护中的弱点/缺陷/疏忽 | "锁不牢" |
| **Exposure 暴露** | 因威胁而易受损失的状态（有被利用可能，但未必已发生） | "门户大开的可能性" |
| **Risk 风险** | 威胁利用漏洞造成损害的可能性与严重程度 | 风险 = 威胁 × 脆弱性 = 概率 × 严重度 |
| **Safeguard 防护** | 消除/降低漏洞、抵御威胁的任何措施（不一定要买新产品，重配置也算） | 对策 |

**关系链**：Threats 利用 Vulnerabilities → 产生 Exposure → 即 Risk → 由 Safeguards 缓解。Safeguards 保护受 Threats 威胁的 Assets。

**C. 三类"风险"级别公式（高频计算/概念题）**
- **Total Risk（总风险）**= threats × vulnerabilities × asset value（即**完全不部署任何防护**时的风险）。
- **Controls Gap（控制缺口）**= Total Risk − Residual Risk（靠防护降下来的那部分）。
- **Residual Risk（残余风险）**= Total Risk − Controls Gap（管理层**选择接受**、不再缓解的部分；通常因成本效益不合算）。
- **Inherent Risk（固有风险）**= 实施任何控制前的原生/默认风险，aka initial/starting risk。
- **Control Risk（控制风险）**= 引入控制本身带来的新风险（没有技术是完美的）。

**资产估值铁律**：保护成本不应超过资产价值——"花 $100,000 保护只值 $1,000 的资产"不合理；年度防护成本不应超年度资产损失成本。

## ④ 考试怎么考（题型 + 必记混淆）
- **题型 A（公式匹配）**：给场景问 total/residual/controls gap 的关系——记住 **Residual = Total − Gap**。
- **题型 B（术语辨析）**：区分 threat（事件）vs vulnerability（弱点）vs exposure（状态）vs risk（可能性×严重度）。
- **5 个必记混淆项**：
  1. **Risk = Threat × Vulnerability**，不是单纯"威胁"。
  2. **Exposure 是"可能被利用的状态"，不等于已发生损失**。
  3. **Residual risk 是"管理层主动接受的"**，不是"忘掉的"。
  4. **Inherent risk 在控制之前；Residual risk 在控制之后**。
  5. **资产估值指导防护投入上限**：年度防护成本 ≤ 资产年损失预期（ALE）。

## ⑤ 真实案例
某电商评估"数据库泄露"风险：资产（客户库）估值高、漏洞（弱加密）明显、威胁（外部黑客）真实 → 总风险高。部署加密+访问控制后，控制缺口大，残余风险降到可接受。但若再要"零泄露"需投入千万级，成本效益不合算——剩余部分作为残余风险书面接受，而非无限砸钱。

## ⑥ 自测
1. （单选）Residual risk is best described as:
   A. Risk before any controls  B. Risk accepted after controls
   C. The control gap  D. Inherent risk
   **答案：B**
2. （单选）Formula: Risk = ?
   A. Threat + Vulnerability  B. Threat × Vulnerability
   C. Asset × Threat  D. Exposure × Safeguard
   **答案：B**

---
*注：本篇定义以 Sybex CISSP OSG 10th (2024) Chapter 2 原书为准；risk=threat×vulnerability、total/residual/controls gap、资产估值上限为高频考点。*
