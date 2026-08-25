---
title: 调查、取证与证据（Investigations, Forensics & Evidence）
parent: 第 19 章 · 调查与道德
grand_parent: CISSP 认证安全工程师知识库
nav_order: 1
---

# 调查、取证与证据（Investigations, Forensics & Evidence）

> 来源：Chapter 19 · Investigations（部分）
> 域：Domain 8 Security and Risk Management（安全与风险管理）
> 模板：原书定义+对比表 / 真实案例 / 考试怎么考

## ① 一句话秒懂
当安全事件发生后，光"修好"不够，还得**按法律和规矩把真相查清楚、把证据留得住**——这就是调查与取证（forensics）要做的事。

## ② 原书核心定义 + 对比表

**调查类型（Types of Investigations）**——Sybex 明确指出，调查按"谁发起、按什么规则"分为五类，CISSP 常考区分：

| 调查类型 | 发起方 | 目的 | 关键特征 |
|---|---|---|---|
| Administrative（行政调查） | 组织内部 | 违反内部政策 | 不必然违法，但违反公司规章 |
| Criminal（刑事调查） | 执法机关 | 追究刑事责任 | 需"排除合理怀疑 beyond reasonable doubt" |
| Civil（民事调查） | 个人/企业 | 索赔/救济 | 标准较低："优势证据 preponderance of evidence" |
| Regulatory（监管调查） | 监管机构（如 SEC/FTC） | 违反行业法规 | 依特定法规授权 |
| Industry standards（行业标准调查） | 自律组织/标准体 | 违反行业标准 | 如 PCI DSS 合规调查 |

**证据四类型（Four Types of Evidence）**：

| 类型 | 说明 | 例子 |
|---|---|---|
| Real（实物证据） |  tangible 物体本身 | 被扣押的硬盘、U 盘 |
| Documentary（文书证据） | 书面/记录材料 | 日志、合同、邮件 |
| Testimonial（证言证据） | 人证口头陈述 | 证人证词、供词 |
| Demonstrative（示意证据） | 帮助理解的展示 | 重建动画、图表 |

**可采性三要件（Admissible Evidence）**：证据要在法庭被接受，须满足——①相关性（relevant）；②真实性/可靠性（authentic）；③合法性（legally obtained，非法取得会被排除）。

**关键证据规则**：
- **最佳证据规则（Best Evidence Rule）**：要证明文书内容，应提供原件；复印件仅在原件不可用时才可。
- **口头证据规则（Parol Evidence Rule）**：书面合同签署后，签署前的口头约定通常不能用来推翻书面条款。
- **传闻例外（Hearsay Exception – Business Records）**：正常业务过程中及时制作的记录，可作为例外被采纳。

## ③ 生活类比（精炼）
取证像"交警处理事故"：先保护现场（防止破坏）、拍照量尺（哈希固定）、记录谁碰过证物（chain of custody 监管链），最后出具报告。随便动一下现场，证据就"作废"了。

## ④ 真实案例
- **Duane 取证案（书中引例）**：调查人员若未用写保护（write blocker）直接复制嫌疑人硬盘，辩方即可主张证据被篡改，整盘数据可能被法庭排除。
- **IOCE 原则落地**：国际经合组织（IOCE）五原则要求"不损毁原始证据、全程记录、可复现"——现代取证软件（如 EnCase、FTK）正是据此设计。

## ⑤ 相关概念梳理 + 对比表

**监管链（Chain of Custody）**：从证据收集→存储→分析→呈堂，每一步谁经手、何时、为何，必须连续记录。断链即可能失效。

**取证五原则（IOCE）**：①最小化处理原始；②全程记录；③可独立验证；④责任人明确；⑤符合法律规定。

**取证技术分类**：

| 取证对象 | 方法 | 要点 |
|---|---|---|
| 介质分析 Media | 写阻断器 + 哈希校验 | 先做 bit-stream 镜像，绝不直接分析原盘 |
| 内存分析 In-memory | 抓取 RAM 镜像 | 断电即失，故事件响应要"保持通电" |
| 网络分析 Network | SPAN 端口 / TAP 分流 | 抓包还原会话 |
| 软件分析 Software | 比对 NSRL 白名单 | 快速识别已知系统文件 |

**洛卡德交换原理（Locard's Exchange Principle）**：犯罪者每一次接触都会留下/带走微量痕迹——数字世界同理，攻击者必留日志、文件时间戳等"数字尘埃"。

## ⑥ 考试怎么考（题干样式 + 常见混淆项）
- 题干："Which type of investigation requires proof beyond a reasonable doubt?" → 答 **Criminal**。混淆：Civil 用 preponderance of evidence（更低标准）。
- 题干："What rule requires the original document?" → 答 **Best Evidence Rule**。混淆：Parol Evidence Rule 是关于口头约定 vs 书面合同。
- 题干："Forensic copy must use a __ to prevent alteration." → 答 **write blocker**。
- 题干："What principle states every contact leaves a trace?" → 答 **Locard's Exchange Principle**。

## ⑦ 自测（改编自原书 Review Questions，附解析）
1. 刑事调查与民事调查在证明标准上的主要区别是？
   - A. 刑事用 preponderance，民事用 beyond reasonable doubt
   - B. 刑事用 beyond reasonable doubt，民事用 preponderance
   - C. 两者都用 beyond reasonable doubt
   - D. 两者都不需要证明标准
   - **答案：B**。解析：刑事定罪需"排除合理怀疑"（更高标准），民事只需"优势证据"（51% 即可）。

2. 下列哪项是"实物证据（real evidence）"？
   - A. 证人证词
   - B. 被扣押的硬盘
   - C. 系统日志
   - D. 重建动画
   - **答案：B**。解析：硬盘是 tangible 物体本身；C 是 documentary，A 是 testimonial，D 是 demonstrative。

3. 取证时为保证不改动原始介质，应首先使用？
   - A.  antivirus 软件
   - B.  write blocker
   - C.  disk defragmenter
   - D.  compression tool
   - **答案：B**。解析：写阻断器阻止任何写操作，确保镜像与原件逐比特一致（哈希验证）。
