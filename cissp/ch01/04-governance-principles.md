---
title: Evaluate and Apply Security Governance Principles（评估并应用安全治理原则）
parent: 第 1 章 · 安全治理与原则政策
grand_parent: CISSP 认证安全工程师知识库
nav_order: 4
---

# Evaluate and Apply Security Governance Principles（评估并应用安全治理原则）

> 来源：Sybex CISSP 第10版 · Chapter 1 · Evaluate and Apply Security Governance Principles
> 域：Domain 1 安全与风险管理
> 模板：原书定义+对比表 / 真实案例 / 考试怎么考

## ① 一句话秒懂
**安全治理 Security Governance** = 由董事会/高层主导，指导并监督组织整体安全方向的**管理活动**——定方向的人，不是干活的 IT。

## ② 原书核心定位 + Due Diligence vs Due Care 对比表
书里把治理定位为**高层管理责任**，与公司治理、IT 治理目标交织（维持业务运转 + 增长 + 韧性 resiliency），并受法律、法规、标准、合同强制。两个最易混的概念：

| 概念 | 原书定义 | 关注点 | 作用 |
|---|---|---|---|
| **Due Diligence 尽职调查** | 持续的监督、审查、留痕过程 | "过程"——是否尽到合理注意 | 证明组织**一直**在管 |
| **Due Care 恪尽职责** | 把合理的防护措施**落实为行动** | "行动"——是否实际做了 | 证明组织**确实**采取了措施 |

> 两者配合，才能在损失发生时**免责或减责（avoid/reduce negligence claims）**。只说不做（无 Due Care）或只做不记（无 Due Diligence 留痕）都不行。

## ③ 生活类比（精炼）
就像公司治理：不会让电工（IT）自己决定全楼消防标准，而是董事会定规矩、请外部审计查。安全治理同理——方向由高层定，外部人验证。

## ④ 真实案例（概念落地）
**SolarWinds 2020 供应链事件**：攻击者侵入 SolarWinds 构建系统，在 Orion 软件更新中植入后门，波及大量政府与企业客户。对受害组织而言，这是**第三方治理（Third-Party Governance）失败**的典型——依赖外部供应商却未充分审计其安全姿态，把别人的薄弱变成了自己的风险。书里强调：第三方治理要确保你依赖的外包方也守你的安全姿态，否则带来额外风险。

## ⑤ 其余核心要点
- **执行主体**：治理由**董事会/治理委员会**执行；小公司由 CEO 或 **CISO** 代行。
- **第三方治理 Third-Party Governance**：外部审计/监察，验证外包方安全姿态。
- **文件审查 Documentation Review 先于现场审查（on-site assessment）**：先看纸面材料，再决定现场查什么。
- 受法律、法规、行业标准、合同、许可要求强制。

## ⑥ 考试怎么考（题干样式 + 常见混淆）
- **题型（场景→概念）**：给"董事会定安全方向""损失后证明已尽合理注意""先审文档再现场"等，选对应治理概念。
- **常见混淆项（必记）**：
  1. **安全治理是业务/高层责任，不是 IT 的事**——题干说"IT 负责治理"必错。
  2. **Due Diligence（过程/监督）≠ Due Care（行动/落实）**——高频错项。
  3. **文件审查在现现场审查之前**——顺序不能反。
  4. **第三方治理**关注外包方是否守你的安全姿态。

## ⑦ 自测（改编自原书 Review Questions，附解析）
1. 安全治理（Security Governance）主要由谁执行？
   A. IT 基层员工　B. 董事会/高层　C. 外包商
   **答案：B**。治理是高层管理责任，定方向、做监督。

2. 现场审查（on-site assessment）之前通常先做什么？
   A. 渗透测试　B. 文件审查 Documentation Review　C. 直接断电
   **答案：B**。书里明确文件审查通常在现场审查之前进行。

---
*说明：本篇据初版要点扩写，关键术语与定义建议以原书为准。*
