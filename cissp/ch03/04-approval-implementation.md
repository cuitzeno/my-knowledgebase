---
title: Ch3-04 计划批准与实施（Plan Approval & Implementation）
parent: 第 3 章
grand_parent: CISSP 认证安全工程师知识库
nav_order: 4
---

# Ch3-04 计划批准与实施（Plan Approval & Implementation）

> 一句话秒懂：连续性方案写完了，得让 CEO 签字撑腰、全员培训演习、落到纸面文档——否则只是一份没人认的 PPT。

## ① 生活类比
你制定了家庭逃生计划，但没跟家人说、没演练过、也没贴出来。真起火时大家各跑各的——计划等于白写。BCP 也一样：**高管背书 + 培训演练 + 成文存档**，三者缺一不可。

## ② 核心概念（忠于 Sybex 第10版）
### 计划批准（Plan Approval）
- 尽量争取**最高执行官**（CEO/董事长/总裁）签署——向其权威背书，让其他高管不敢当"琐碎 IT 事"敷衍。
- **高管 buy-in（支持）是 BCP 成功的关键**。

### 计划实施（Plan Implementation）
- 制定实施时间表，调配资源。
- 部署后建立 **BCP 维护程序**，确保计划随业务演进而更新。

### 沟通、培训与教育（Communication, Training, Education）
- **全员**：至少接受计划概览 briefing（建立信心）。
- **直接责任人员**：针对其 BCP 任务受训并考核；**每个任务至少 1 名备份人员**（redundancy）。

### BCP 文档要素（必考清单）
书面计划应包含：
1. **Continuity Planning Goals 连续性目标**：最常见即"紧急时业务持续运营"；可量化（如呼叫中心连续停机 ≤15 分钟）。
2. **Statement of Importance 重要性声明**：常以致员工信形式，说明投入资源的理由，争取全员配合。
3. **Statement of Priorities 优先级声明**：直接来自 BIA，列出关键业务优先级（注明仅用于 BCP，防政治斗争挪用）。
4. **Statement of Organizational Responsibility 组织责任声明**：高管签署，重申"业务连续性人人有责"。
5. **Statement of Urgency and Timing 紧迫性声明**：表达实施关键性 + 时间表。
6. **Risk Assessment 风险评估**：复述 BIA 决策，含实际 AV/EF/ARO/SLE/ALE 数值。
7. **Risk Acceptance/Mitigation 风险接受/缓解**：记录每个风险"可接受（及未来重审条件）"或"不可接受（已上措施）"。

> 文档化的好处：应急时有纸面可依、留历史记录、逼团队暴露计划缺陷（草稿可分发"sanity check"）。

## ③ 真实案例
某企业的 BCP 由中层经理签署推行，跨出本部门时遭 resist（阻力）。后改为 CEO 联名签署"重要性声明 + 组织责任声明"，推行顺畅。印证"高管背书权重"的考点。

## ④ 记忆口诀
- **文档七要素**："目·重·先·责·急·评·缓"（目标/重要性/优先级/责任/紧迫性/风险评估/风险缓解）。
- **批准铁律**：要 **CEO 级签名**；**高管 buy-in** 决定成败。
- **培训底线**：每个 BCP 任务**至少一名备份**。

## ⑤ 考试怎么考（陷阱）
- 问"哪份声明由高管签署、强调人人有责"→ **Statement of Organizational Responsibility**。
- 问"哪个文档要素含实际 AV/EF/SLE/ALE 数字"→ **Risk Assessment**。
- "BCP 只由 IT 经理签批即可"是**错误**的——需要高管背书。
- 培训题：直接责任人须有**备份人员**，否则单点失效。

## ⑥ 自测
1. （题型：匹配）下列描述分别对应 BCP 文档七要素中的哪一项：(a) 列出关键业务按重要性排序清单；(b) 包含实际 ALE 数值的定量分析；(c) 高管署名强调"连续性人人有责"。
2. （题型：原则）为什么 BCP 计划必须争取 CEO 而非仅 IT 总监的签署？

> 关键定义以原书（Sybex 10th, Ch3）为准。
