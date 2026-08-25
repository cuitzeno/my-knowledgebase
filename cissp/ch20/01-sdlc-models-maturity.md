---
title: 系统开发生命周期与成熟度模型（SDLC, Models & Maturity）
parent: 第 20 章
grand_parent: CISSP 认证安全工程师知识库
nav_order: 1
---

# 系统开发生命周期与成熟度模型（SDLC, Models & Maturity）

> 来源：Chapter 20 · Introducing Systems Development Controls（部分）
> 域：Domain 8 Security and Risk Management（安全与风险管理）
> 模板：原书定义+对比表 / 真实案例 / 考试怎么考

## ① 一句话秒懂
想让软件"生来安全"，就得把安全塞进**从需求到退役的整个生命周期（SDLC）**，而不是等上线了再打补丁。

## ② 原书核心定义 + 对比表

**SDLC 通用核心活动**（无论哪种模型，都跑这些环节）：概念定义 → 功能需求 → 控制规格 → 设计评审 → 编码 → 代码走查 → 系统测试 → 维护与变更管理。

**三大经典模型对比**：

| 模型 | 特点 | 关键考点 |
|---|---|---|
| Waterfall（瀑布） | 顺序七阶段，发现错误只能回退**一步** | 反馈环有限；改良版加 V&V（验证/确认） |
| Spiral（螺旋） | 多次迭代瀑布，每圈产出原型 P1/P2/P3 | 元模型（model of models），解决瀑布"只能回退一步"的缺陷 |
| Agile（敏捷） | 客户导向、快速迭代；哲学非方法论 | Scrum 每日站会 + Sprint（1–4 周）；宣言四条价值观 |

**成熟度模型**：

| 模型 | 层级 | 要点 |
|---|---|---|
| SW-CMM / CMMI | L1 初始→L5 优化 | 质量取决于过程质量；CMMI 把 L4 叫"Quantitatively Managed" |
| IDEAL | Initiating/Diagnosing/Establishing/Acting/Learning | SEI 提出，落实 SW-CMM 属性 |
| SAMM | Governance/Design/Implementation/Verification/Ops | OWASP 开源，专攻软件安全成熟度 |

**记忆口诀**：SW-CMM + IDEAL 十级首字母 "I I D R E D A M L O" → "I…I, Dr. Ed, am lo(w)"（ psychiatrist 办公室场景）。

## ③ 生活类比（精炼）
SDLC 像盖楼：先想清楚要盖啥（概念）→ 画功能图（需求）→ 设计安防（控制规格）→ 评审图纸 → 施工（编码）→ 监理巡查（走查）→ 验收（测试）→ 物业维护。瀑布是"一层盖完再盖下一层"，螺旋是"先盖样板间再逐步完善"，敏捷是"边住边改、每周小改"。

## ④ 真实案例
- **Heartbleed（CVE-2014-0160）**：OpenSSL 库漏洞影响数千系统——典型**第三方共享库（library）**风险，凸显"不知情也在用"的依赖隐患。
- **DevSecOps / CI/CD**：传统年度大部署 → DevOps 每日多次部署，甚至 CI/CD 一天数十次，安全要求同步敏捷，催生"软件定义安全"。

## ⑤ 相关概念梳理 + 对比表

**编译型 vs 解释型语言安全对比**：

| 类型 | 例子 | 安全优劣 |
|---|---|---|
| 编译 Compiled | C/Java | 第三方难改，但开发者可藏后门难被发现 |
| 解释 Interpreted | Python/JS | 用户可看源码查错，但任何人可改代码藏恶意 |

**OOP 关键术语**：封装（encapsulation）、继承（inheritance）、多态（polymorphism）、高内聚（high cohesion，优）/低耦合（low coupling，优）。

**变更与配置管理**：Request Control / Change Control / Release Control 三件套；Release Control 必须**移除调试代码与后门**再上线。SCM 四组件：配置标识/控制/状态记账/审计。

## ⑥ 考试怎么考（题干样式 + 常见混淆项）
- 题干："Which SDLC model allows returning to planning as requirements change?" → 答 **Spiral**。混淆：Waterfall 只能回退一步。
- 题干："A philosophy emphasizing customer collaboration over contract negotiation is?" → 答 **Agile**。混淆：它是哲学不是具体方法论（Scrum 才是方法论）。
- 题干："SW-CMM level with continuous process improvement?" → 答 **Level 5 Optimizing**。混淆：L4 Managed/Quantitatively Managed。
- 题干："Before releasing software, debug code and backdoors should be removed during?" → 答 **Release Control**。

## ⑦ 自测（改编自原书 Review Questions，附解析）
1. 与传统瀑布模型相比，螺旋模型的主要改进是？
   - A. 完全不要规划
   - B. 允许多次迭代、可回到规划阶段
   - C. 只做一步编码
   - D. 取消测试
   - **答案：B**。解析：螺旋是瀑布的元模型，每圈产原型，解决了瀑布"只能回退一步"的批评。

2. 以下哪项不是 SDLC 的通用核心活动？
   - A. 概念定义
   - B. 编码
   - C. 市场营销
   - D. 维护与变更管理
   - **答案：C**。解析：营销不在开发生命周期核心活动中；其余均为通用环节。

3. 在 Release Control 阶段必须确保完成的是？
   - A. 增加更多后门方便维护
   - B. 移除调试代码与后门
   - C. 推迟测试
   - D. 取消版本控制
   - **答案：B**。解析：发布控制要点之一是确认调试代码/后门已在投产前移除，仅放行已批准变更。
