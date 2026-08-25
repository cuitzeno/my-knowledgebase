# Ch8-05 通用准则（Common Criteria）与运行授权（ATO）

> 所属域：Domain 3 Security Architecture and Engineering
> 对应原书：Chapter 8 — Select Controls Based on Systems Security Requirements

## ① 一句话秒懂
**Common Criteria 用 EAL1–7 给系统"安全等级"打分（功能 + 保证）**；**ATO 是官方批准系统上线运行的"准生证"**。

## ② 生活类比
买保险箱，CC 像国际通用的防盗等级认证（EAL 越高越难被打）；ATO 像监管批文——就算保险箱再好，没批文也不能正式用。

## ③ 核心概念（大白话 + 原书定义）

**Common Criteria（CC）**
动态、主观的产品评估模型，取代 TCSEC（美"橙皮书"）和 ITSEC（欧）。现为 **ISO/IEC 15408:2022**。1998 年美英法德加五国签署，现 28 国加入。
- 两大元素：
  - **Protection Profile（PP）= "我想要"**：客户定义的安全需求。
  - **Security Target（ST）= "我提供"**：厂商声明在 TOE（评估目标）中内置的安全。
- 目标：增买家信心、避免重复评估、成本效益、一致标准、推评估、评估 TOE 的**功能（functionality）**与**保证（assurance）**。

**EAL1–7（评估保证级）**

| 级别 | 名称 | 要点 |
|---|---|---|
| EAL1 | Functionally tested | 仅需基本正确运行信心，威胁不严重 |
| EAL2 | Structurally tested | 良好商业实践，低至中度保障，适合遗留系统 |
| EAL3 | Methodically tested & checked | 设计阶段始即安全工程，中度保障 |
| EAL4 | Methodically designed, tested & reviewed | 严格安全工程 + 良好商业实践，商业通用高保障 |
| EAL5 | Semi-formally verified designed & tested | 需专家安全技术，计划开发中的高度保障 |
| EAL6 | Semi-formally verified design & tested | 高级保障技术，保护高价值资产抗显著风险 |
| EAL7 | Formally verified design & tested | 仅最高风险 / 高价值资产，形式化分析 |

**CC 的局限**：不保证无漏洞；不管人员 / 组织 / 物理安全；不管电磁辐射；不评密码算法强度；不评 in situ（实际部署）使用。

**ATO（Authorization to Operate）**
RMF（风险管理框架）下官方批准使用特定 IT/IS 系统执行业务并**接受已识别风险**，取代旧称 accreditation。由 **Authorizing Official（AO）** 签发。
- 通常 **3 年**，遇重大泄露 / 重大变更需重取；AO 有裁量权。
- AO 四种决定：
  1. **Authorization to Operate**：风险可控至可接受水平。
  2. **Common Control Authorization**：继承自他方已获 ATO 的通用控制。
  3. **Authorization to Use**：第三方（如云）提供、风险可接受；也用于互认（reciprocity）。
  4. **Denial of Authorization**：风险不可接受。

## ④ 真实案例
- 政府 / 央行采购只认有 CC EAL 认证的产品。
- 云服务商拿 FedRAMP 授权（本质属 ATO 类）才能接政府业务。

## ⑤ 考试怎么考
- EAL 数字越大保证越高，但 **CC 不保证"绝对安全"**。
- PP vs ST 区别（客户想要 vs 厂商提供）。
- ATO 由 AO 签发、通常 3 年、取代 accreditation。
- CC 基于 ISO/IEC 15408。
- 局限中"不对无漏洞背书"是常考点。

## ⑥ 记忆口诀
- EAL 一测二构三查四评，五半六半七形式；数字越高越可靠，CC 不保无漏洞。
- PP 是我要，ST 是我给；ATO 准生证，AO 签三年。

## ⑦ 自测
1. EAL 数字越大代表什么？CC 是否保证系统"绝对无漏洞"？
2. Protection Profile 与 Security Target 的本质区别？
3. ATO 由谁签发？通常有效期多久？取代了哪个旧术语？
4. CC 不评估哪些方面？（人员 / 物理 / 电磁辐射 / 密码强度 / 实际部署）
