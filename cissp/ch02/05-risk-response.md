---
title: Ch2-05 风险应对策略与风险偏好
parent: 第 2 章 · 人员安全与风险管理概念
grand_parent: CISSP 认证安全工程师知识库
nav_order: 5
---

# Ch2-05 风险应对策略与风险偏好

> 所属：Chapter 2 Personnel Security and Risk Management Concepts（Domain 1）
> 加厚标准：原书定义 + 对比表 / 真实案例 / 考试怎么考

## ① 一句话秒懂
评估完风险，就要选"怎么办"：**降（缓解）/ 转（转移）/ 吓（威慑）/ 躲（规避）/ 忍（接受）**——唯独不能"装没看见（拒绝）"。

## ② 生活类比
家门口有坑（风险）。你可以：填平它（**缓解**）、买保险转嫁损失（**转移**）、立警示牌+装监控（**威慑**）、干脆绕路走（**规避**）、或明知有坑但懒得管（**接受**）；但你不能"假装坑不存在还骂摔跤的人"——那就是**拒绝风险**，法律上算疏忽。

## ③ 核心概念（大白话 + 原书定义）

**A. 六种风险响应（六选一，但 rejection 不可接受）**
| 响应 | 原书定义 | 例子 |
|---|---|---|
| **Mitigation/Reduction 缓解** | 部署防护、安全控制、对策以**降低或消除漏洞**、阻断威胁 | 加密、防火墙 |
| **Assignment/Transfer 转移** | 将损失责任**转嫁给**另一实体 | 购买网络/传统保险、外包 |
| **Deterrence 威慑** | 对潜在违规者实施**威慑**，使其不敢攻击 | 审计、摄像头、警告横幅、保安、表示愿配合追诉 |
| **Avoidance 规避** | 选择**风险更低的替代方案**，从根源消除风险原因 | 坐飞机而非开车；在 Arizona 而非 Florida 建厂避飓风；因高风险放弃某业务 |
| **Acceptance 接受** | 成本/收益显示防护成本**超过**潜在损失，管理层同意承担后果 | 需**书面声明**为何不部署、谁决策、谁担责（高管签署） |
| **Rejection/Ignore 拒绝** | 否认风险存在、指望它不发生 | **不可接受**，法庭上可能构成疏忽（negligence） |

**B. 风险偏好相关概念（一组易混词）**
- **Risk Appetite 风险偏好**：组织在所有资产上**总体愿意**承担的风险量。
- **Risk Capacity 风险容量**：组织**能够**承担的风险水平（期望偏好可能 > 实际容量）。
- **Risk Tolerance 风险容忍度**：对**单个资产—威胁对**能接受的水平，常关联 risk target。
- **Risk Target 风险目标**：某资产—威胁对偏好的风险水平。
- **Risk Limit 风险上限**：超过 target 后、在采取进一步动作前容忍的最大水平。

**C. 迭代性**
风险处理不是一次性工程。安全需持续维护、周期性重评，以评估防护的完整性与有效性、发现变化与缺陷（control risk：控制本身引入的新风险）。

## ④ 考试怎么考（题型 + 必记混淆）
- **题型 A（匹配）**：给场景选响应——买保险→Transfer；绕路→Avoidance；装摄像头→Deterrence；填坑→Mitigation；签接受书→Acceptance。
- **题型 B（判断）**：问"哪种响应不可接受"→ Rejection/Ignore。
- **5 个必记混淆项**：
  1. **Transfer ≠ Mitigation**：转移是"转嫁损失责任"（保险/外包），风险本身未必降低。
  2. **Avoidance 消除风险源**，Mitigation 降低但未消除。
  3. **Acceptance 必须书面化**（高管签署），不是"懒得管"。
  4. **Rejection 在法律上=疏忽**，绝不是有效响应。
  5. **Appetite（总）≠ Tolerance（单对）≠ Capacity（能承受）**。

## ⑤ 真实案例
某 SaaS 公司面对"勒索软件"风险：部署 EDR+备份（**Mitigation**），购买网络安全保险（**Transfer**），终端挂警告横幅并告知将追诉（**Deterrence**），对核心研发数据迁至隔离网（部分 **Avoidance**）。剩余低频低损风险，经成本/收益分析后**书面接受**。全程未"否认风险存在"——避免了疏忽指控。

## ⑥ 自测
1. （单选）Purchasing cybersecurity insurance is an example of:
   A. Mitigation  B. Transfer  C. Avoidance  D. Deterrence
   **答案：B**
2. （单选）Which risk response is considered unacceptable / negligence?
   A. Acceptance  B. Avoidance  C. Rejection  D. Transfer
   **答案：C**

---
*注：本篇定义以 Sybex CISSP OSG 10th (2024) Chapter 2 原书为准；六类响应定义、Rejection=疏忽、Transfer vs Mitigation 区别为高频考点。*
