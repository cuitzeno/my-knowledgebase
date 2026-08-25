---
title: 计算机犯罪的主要类别（Major Categories of Computer Crime）
parent: 第 19 章 · 调查与道德
grand_parent: CISSP 认证安全工程师知识库
nav_order: 2
---

# 计算机犯罪的主要类别（Major Categories of Computer Crime）

> 来源：Chapter 19 · Major Categories of Computer Crime
> 域：Domain 8 Security and Risk Management（安全与风险管理）
> 模板：原书定义+对比表 / 真实案例 / 考试怎么考

## ① 一句话秒懂
按"攻击者图什么"给网络犯罪分七类——知道对手的**动机**，才能预判他怎么打、留下什么痕迹。

## ② 原书核心定义 + 对比表

Sybex 将计算机犯罪（computer crime = 涉及计算机、或利用计算机实施的违法/违规行为）按**目的与结果**分为七大类：

| 类别 | 动机 | 典型目标/手段 | 证据特征 |
|---|---|---|---|
| Military & Intelligence（军事与情报） | 窃取机密情报 | 部署/战备信息、秘密情报、证据位置 | 专业攻击者，痕迹极少 |
| Business（商业攻击） | 损害对手 CIA 或窃密 | 商业间谍/工业间谍、勒索软件 | 信息泄露损害 > 攻击本身 |
| Financial（金融攻击） | 非法获利 | 盗刷、转账欺诈、DDoS 雇佣 | 金额大小反映攻击者水平 |
| Terrorist（恐怖攻击） | 制造恐慌、破坏正常生活 | 电力/通信/工控系统 | 常先情报收集后实质打击 |
| Grudge（报复攻击） | 怨恨、泄愤 | 前员工/被拒者破坏数据 | 内部人威胁，最危险 |
| Thrill（刺激攻击） | 纯粹图爽 | 改网页（defacement）、script kiddie | 多为服务中断 |
| Hacktivist（黑客行动主义） | 政治+刺激 | Anonymous/LulzSec、大规模 DoS | 借自动化工具，门槛低 |

## ③ 生活类比（精炼）
七类犯罪像"七种小偷"：有人专偷国家机密（军事）、有人偷对手配方（商业）、有人直接抢钱（金融）、有人炸电厂（恐怖）、有人被开除回来砸场子（报复）、有人闲着无聊撬锁玩（刺激）、有人为了"正义"搞破坏（黑客行动）。

## ④ 真实案例
- **2017 WordPress 大规模改页**：自动化工具一周内篡改超 180 万网页——典型 **Thrill / Hacktivist** 类，门槛极低、危害扩散快。
- **内部人报复案（书中引例）**：某公司前系统管理员因不满离职，公司离职流程不成熟未回收其 VPN 账号，他借残留权限窃取资金并销毁敏感数据。教训：**离职即停权**是防 grudge 攻击的第一道防线。
- **Mirai 僵尸网络（关联 Ch17）**：租用 botnet 发起 DDoS，属于 financial "cybercrime for hire" 模式——攻击者无政治动机，只收钱。

## ⑤ 相关概念梳理 + 对比表

**高级持续性威胁（APT, Advanced Persistent Threat）**：国家支持的、资金充足、技术高超的攻击者，针对特定目标长期潜伏。本质是 military/intelligence 类的"升级版"。

**内部人威胁（Insider Threat）**：常被忽视却最危险。分恶意（故意破坏/窃密）与无意（特权误操作给外部可乘之机）。对策：及时 deprovisioning（停权）、最小权限、离职审计。

**Grudge vs Thrill 易混点**：

| 维度 | Grudge | Thrill |
|---|---|---|
| 动机 | 怨恨/报复 | 单纯图刺激 |
| 攻击者 | 多为内部/前员工 | script kiddie（外行） |
| 危害 | 可能极重（知根知底） | 多为服务中断 |

## ⑥ 考试怎么考（题干样式 + 常见混淆项）
- 题干："An attack launched by a disgruntled former employee to destroy data is an example of?" → 答 **Grudge attack**。混淆：Thrill（无怨恨动机）。
- 题干："A state-sponsored, well-funded attack against a specific target over time is a(n)?" → 答 **APT**。混淆：普通 business attack 未必有国家背景。
- 题干："Renting a botnet to perform DDoS for a client is an example of?" → 答 **Financial / cybercrime for hire**。混淆：Terrorist（无恐慌动机）。
- 题干："Which category leaves the least evidence?" → 答 **Military & Intelligence**（专业覆盖痕迹）。

## ⑦ 自测（改编自原书 Review Questions，附解析）
1. 被解雇的前系统管理员利用未回收的 VPN 账号破坏公司数据，这属于？
   - A. Thrill attack
   - B. Grudge attack
   - C. Hacktivist attack
   - D. Terrorist attack
   - **答案：B**。解析：核心动机是怨恨报复；且典型内部人威胁，凸显离职即停权的重要性。

2. 由国家支持、资金充足、针对特定目标长期攻击，称为？
   - A. Script kiddie
   - B. APT
   - C. Hacktivist
   - D. Business attacker
   - **答案：B**。解析：APT 的特征就是 nation-state sponsor + 资源 + 持久性。

3. 以下哪项最可能不是 professional military attacker 留下的？
   - A. 大量日志
   - B. 极少证据
   - C. 覆盖痕迹
   - D. 隐蔽通道
   - **答案：A**。解析：专业军事/情报攻击者会竭力清除痕迹，留下"极少证据"才是其特征。
