---
title: Understand and Apply Security Concepts（理解并应用安全概念）
parent: 第 1 章 · 安全治理与原则政策
grand_parent: CISSP 认证安全工程师知识库
nav_order: 2
---

# Understand and Apply Security Concepts（理解并应用安全概念）

> 来源：Sybex CISSP 第10版 · Chapter 1 · Understand and Apply Security Concepts
> 域：Domain 1 安全与风险管理（权重 16%，8 域之首）
> 模板：原书定义+对比表 / 真实案例 / 考试怎么考（Ch1 加厚标准）

## ① 一句话秒懂
信息安全的所有控制，最终都在保护**五个支柱**：保密、完整、可用、真实、不可抵赖（后两者常被合称"五大支柱"，前三者即著名的 CIA 三要素）。一切安全设计、一切考题，都绕不开这五个词。

## ② 原书核心定义（忠于 Sybex 措辞）
书里对前三个给了**精确定义**，考试常考"哪个定义对应哪个词"：

- **Confidentiality（保密）**：*measures used to ensure the protection of the secrecy of data, objects, or resources*；目标是 **prevent or minimize unauthorized access**（防止或最小化未授权访问）。注意：泄密不只有黑客攻击，**人为疏忽、配置错误、策略漏洞**同样算违规。
- **Integrity（完整）**：*protecting the reliability and correctness of data*；**prevents unauthorized alterations**（防止未授权篡改）。它要防两类：恶意篡改（病毒、逻辑炸弹、后门）和**授权用户的手误**。完整性从三个角度看：① 防未授权主体修改；② 防授权主体误改；③ 维持内外一致性（数据真实反映现实）。
- **Availability（可用）**：*authorized subjects are granted timely and uninterrupted access to objects*；包含防 **DoS（拒绝服务）**。它依赖底层设施（网络、通信、访问控制）正常运转，并靠**冗余、备份、容错**消除单点故障。书里一句话很关键：*Availability depends on both integrity and confidentiality*——没有完整和保密，可用也守不住。

> 考试常把 definition 当题干："Which concept is defined as preventing unauthorized alteration of data?" → 答案是 **Integrity**。

## ③ 生活类比（精炼，不当主角）
寄快递三要素：
- **保密** = 只有收件人能拆，途中不泄露；
- **完整** = 包裹没被掉包、没被拆改；
- **可用** = 收件人随时能取，不被拒收、不丢件。
这三者对立面就是下面的 DAD。

## ④ 真实案例（概念落地）
- **保密失效 → Equifax 2017**：1.47 亿美国人 PII（姓名、社保号、驾照）被拖库。对应 Confidentiality 破坏，且主因是**未打补丁（人为/流程疏忽）**，而非高深攻击——印证书里"泄密多源于疏忽"。
- **完整失效 → Stuxnet 震网**：恶意代码篡改伊朗核设施离心机的**运行读数**（让监控显示正常、实际在损毁），属于典型的 Integrity 破坏（恶意未授权篡改 + 内外一致性崩坏）。
- **可用失效 → Mirai/Dyn 2016 DDoS**：僵尸物联网击垮 DNS 服务商 Dyn，Twitter、Netflix、Reddit 大面积不可用数小时。典型 Availability 破坏（DoS）。

## ⑤ DAD、Overprotection、真实与不可抵赖、AAA
**DAD 三连 = CIA 的失败态**（书原话：the opposite of the CIA Triad）：

| CIA（目标） | DAD（失败） | 含义 |
|---|---|---|
| Confidentiality | **Disclosure** 泄露 | 敏感数据被未授权方获取 |
| Integrity | **Alteration** 篡改 | 数据被恶意或意外改动 |
| Availability | **Destruction** 破坏（常即 DoS） | 资源损坏或授权者不可达 |

**Overprotection（过度防护的反作用）**：保密过度→可用性下降；完整过度→可用性下降；可用过度→泄密+失完整。安全是平衡，不是越严越好。

**Authenticity（真实）**：数据确实来自声称的来源、传输中未被改。与 Integrity 相关，但更聚焦"来源可信"。

**Nonrepudiation（不可抵赖）**：主体无法否认自己做过的事/发过的消息。靠 **Identification + Authentication + Authorization + Auditing + Accounting** 共同实现（数字证书、会话 ID、交易日志等）。书里强调它是 **accounting 的核心**——若不能 nonrepudiation，就无法追责。

**AAA 实际是 5 要素**（缩写 3 字母，实为 5 步，常考陷阱）：

| 顺序 | 要素 | 原书定义 | 一句话 |
|---|---|---|---|
| 1 | **Identification** 标识 | claiming to be an identity | 报出我是谁（输用户名/刷卡） |
| 2 | **Authentication** 认证 | proving that claimed identity | 证明我真是他（密码/指纹） |
| 3 | **Authorization** 授权 | defines permissions for an identity | 决定我能干啥（读/写/删） |
| 4 | **Auditing** 审计 | recording a log of events | 记录发生了啥 |
| 5 | **Accounting** 问责 | reviewing logs to hold subjects accountable | 查日志、追责 |

> 关键点：标识和认证是**全有或全无**；授权则是**逐对象可变**（同一用户可读文件但不能删）。

## ⑥ 考试怎么考（题干样式 + 常见混淆）
- **题型 A（场景→属性）**：给一段事件，问破坏了哪条。先判断"坏事是什么"→ 泄露=Confidentiality，篡改=Integrity，不可达/DoS=Availability，赖账=Nonrepudiation。
- **题型 B（定义→概念）**：给定义选词（见②）。
- **常见混淆项（必记）**：
  1. **AAA 是 5 个不是 3 个**——漏掉 Identification 与 Accounting 是高频错项。
  2. **Confidentiality ≠ Privacy**——Privacy 特指**个人可识别信息 PII**的保密。
  3. **Integrity vs Authenticity**——完整=内容没被改；真实=确实来自声称来源。
  4. **Nonrepudiation 靠什么实现**——不是单一技术，而是 AAA 全套 + 日志/证书。
  5. **Defense in Depth 是串联（series）**，单层失效不导致全盘崩。

## ⑦ 自测（改编自原书 Review Questions，附解析）
1. 一家电商数据库被入侵，1500 万客户的邮箱与密码被下载外泄。这主要破坏了哪条安全属性？
   A. Integrity　B. Confidentiality　C. Availability　D. Authenticity
   **答案：B**。客户凭据被未授权获取 = Disclosure = 破坏 Confidentiality。（Integrity 没被改、Availability 没中断，故不选 A/C；Authenticity 关注来源可信，不符。）

2. 一名员工通过公司系统发送了违规邮件，事后声称"不是我发的"。要能追究其责任，系统必须保障哪条安全属性？
   A. Authentication　B. Nonrepudiation　C. Integrity　D. Identification
   **答案：B**。无法否认已发生的行为 = Nonrepudiation，它是 accounting/追责的基础。（A/D 只是 AAA 的前两步，单独不足以保证不可抵赖。）
