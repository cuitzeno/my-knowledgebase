---
title: Ch8-04 安全模型：TCB、BLP、Biba、Clark-Wilson、Brewer-Nash
parent: 第 8 章
grand_parent: CISSP 认证安全工程师知识库
nav_order: 4
---

# Ch8-04 安全模型：TCB、BLP、Biba、Clark-Wilson、Brewer-Nash

> 所属域：Domain 3 Security Architecture and Engineering
> 对应原书：Chapter 8 — Understanding the Fundamental Concepts of Security Models

## ① 一句话秒懂
安全模型把抽象的安全策略变成计算机可执行的具体规则。核心是 **TCB + 引用监视器**，以及 BLP（保保密）、Biba（保完整）、Clark-Wilson（商业保完整）等经典模型。

## ② 生活类比
TCB 像金库的核心保险库——**越小越好审计**；security perimeter 是金库墙；reference monitor 是门口安检，每次进出都查。Bell-LaPadula 像"绝密文件不能抄给低密级"的保密规则；Biba 像"脏数据不能污染干净数据库"的纯度规则。

## ③ 核心概念（大白话 + 原书定义）

**安全属性的三种描述方式**
- Token（令牌）：随资源走，访问前先沟通安全信息。
- Capabilities list（能力表）：按主体成行，查询快。
- Security label（安全标签）：永久附着客体，防篡改（token / 能力表都不具备）。

**TCB 与周边**
- TCB（Trusted Computing Base）：软硬件控组合形成的可信基，是系统子集，**越小越好审计**，只有它被信任来执行安全策略。
- Security Perimeter：想象边界，分隔 TCB 与其余部分；TCB 经**可信路径（trusted path）**通信。
- Reference Monitor：TCB 中每次访问前校验的主体-客体守门员。
- Security Kernel：实现 reference monitor 的软硬组件集合，仲裁所有资源访问。

**基础模型**
- State Machine Model（状态机）：系统任何状态都安全；next state = F(input, current state)。安全状态机：开机即安全、所有转换保持安全、仅以符合策略方式访问。
- Information Flow Model（信息流）：基于状态机，控信息流向，防未授权流（含 covert channel 隐蔽信道）。
- Noninterference Model（非干涉）：高级主体行为不影响 / 不被低级主体察觉，防隐蔽信道与特洛伊木马。
- Composition Theories：Cascading（级联）、Feedback（反馈）、Hookup。
- Take-Grant Model：有向图，4 规则 Take / Grant / Create / Remove，决定权限如何传递与泄露。

**访问控制矩阵（Access Control Matrix）**
主体 × 客体矩阵；列 = ACL（随客体），行 = capabilities list（随主体）。管理上用 ACL 更易（按客体删权限比逐用户删容易）。

**Bell-LaPadula（BLP）—— 保保密（C）**
基于格（lattice）、状态机、信息流、MAC。三性质：
- Simple Security (ss)：主体不能读更高级 → **no read-up**
- *-Property（star）：主体不能写更低级 → **no write-down**
- Discretionary Security：用访问矩阵做 DAC
- 例外：**trusted subject** 不受 *-Property 约束（可做降级 / 重分类 declassification）。

**Biba —— 保完整（I），BLP 的倒影**
- Simple Integrity：不能读更低完整级 → **no read-down**
- *-Integrity：不能写更高级 → **no write-up**
- Invocation：低层进程不能请求更高访问
- 记忆捷径：**simple 永远管读，star 永远管写**；规则说"不能"的，反方向即允许。Biba 依赖数据分类来定完整级。

**Clark-Wilson —— 保完整（商业常用）**
三元组 subject / program / object（access control triplet）。主体只能通过受控程序（Transformation Procedures, TP）访问对象，配合职责分离。
- CDI（受保护数据项）、UDI（未受控数据项）、IVP（完整性验证过程）、TP（唯一可改 CDI 的程序）。
- 通过受限接口（restricted interface）实现——不同密级用户看到不同功能 / 数据。

**Brewer and Nash（Chinese Wall / 道德墙 / cone of silence）**
基于**利益冲突**动态变访问：同一冲突类（conflict class）内隔离，防止同时看竞争公司机密。管理员操作某数据时临时封锁冲突数据，完成后恢复。

> ⚠️ "Star" 一词：BLP / Biba 的 star-property 是模型属性；CSA 的 STAR 是云安全计划；Galbraith's Star Model 是商业组织模型——三者**不同**，别混淆。

## ④ 真实案例
- **BLP**：绝密备忘录不能粘贴进非密文件（no write-down）。
- **Biba**：不把吸烟区空气（低纯）泵入洁净室（高纯）；数据上不把未校验输入读进已验证文档。
- **Clark-Wilson**：银行转账必须经受控交易程序，出纳不能同时做记账与审批（职责分离）。
- **Brewer-Nash**：顾问看了公司 A 的并购机密，就不能再看竞争对手公司 B 的同类数据。

## ⑤ 考试怎么考
- BLP vs Biba 对照：BLP 保 C（no read-up / no write-down），Biba 保 I（no read-down / no write-up）。**simple = 读，star = 写**。
- TCB / reference monitor / security kernel / security perimeter 的关系。
- Clark-Wilson 三元组与 CDI / UDI / TP / IVP。
- trusted subject 例外（可做 write-down 降级）。
- 各模型保障目标：BLP = 保密、Biba = 完整、Clark-Wilson = 完整（商业）、Brewer-Nash = 利益冲突。

## ⑥ 记忆口诀
- BLP 保密：上不去读、下不去写；Biba 完整：下不去读、上不去写。
- 简读星写：simple 管读、star 管写。
- TCB 小而可信核，reference monitor 安检门，security kernel 执行体，perimeter 是墙。
- Clark-Wilson 三件套：主体经程序碰对象；CDI 受 TP 改，UDI 随便，IVP 查。

## ⑦ 自测
1. BLP 的 ss 性质和 *-property 分别禁止什么？（no read-up / no write-down）
2. Biba 为什么禁止"读更低完整级"？用"空气纯度"类比解释。
3. Clark-Wilson 中 CDI、UDI、TP、IVP 各是什么？
4. 什么是 trusted subject？它为何能违反 *-property？
