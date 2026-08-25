---
title: 04 · 授权机制与安全原则（权限/隐式拒绝/最小特权/职责分离）
parent: 第 14 章
grand_parent: CISSP 认证安全工程师知识库
nav_order: 4
---

# 04 · 授权机制与安全原则（权限/隐式拒绝/最小特权/职责分离）

## 一句话秒懂
授权靠"隐式拒绝 + 矩阵/ACL/能力表 + 受限接口 + 内容/上下文相关"等机制落地；背后是三大原则：需知、最小特权、职责分离。安全策略写明"要做什么"，不写"怎么做"。

> 对应原书：Chapter 14 — "Understanding Authorization Mechanisms" / "Defining Requirements with a Security Policy"

## 生活类比
保险柜：默认上锁（隐式拒绝），授权清单（ACL）写谁可取；柜门界面按权限只显示你能按的按钮（受限接口）；药柜按内容只给护士看自己病人的药（内容相关）；先挂号缴费才能取药（上下文相关）。

## 核心概念（大白话 + 原书定义）

**授权机制回顾**：
- **Implicit Deny**：未显式授权即拒绝（deny by default）。
- **Access Control Matrix**：集中表（主体×客体×权限），覆盖多个 ACL。
- **Capability List**：以主体为中心（该主体能访问哪些对象）。
- **Constrained Interface**：按权限隐藏/禁用功能（Clark-Wilson 用）。
- **Content-Dependent**：按数据内容限制（DB view）。
- **Context-Dependent**：需前置活动或时间/日期限制。

**三大安全原则**：
- **Need to Know（需知）**：即使有 clearance，工作不需要就不给授权。
- **Least Privilege（最小特权）**：只给工作所需的 privileges（含行动权）——常与需知并列，区别在"含 rights 行动"。
- **Separation of Duties（职责分离 / SoD）**：敏感功能拆给 ≥2 人，建立制衡防欺诈与错误。

**Security Policy（安全策略）**：定义组织安全需求的文档，标识需保护的资产及保护程度。**高层批准**，给安全需求总览，但**不写实现细节**（如"要实施职责分离和最小特权"但不说怎么实施）。专业人员据此落地。

> 口诀：**"隐式拒绝打底，矩阵 ACL 能力表；需知最小职责分，策略定调不写法。"**

## 真实案例
银行转账系统实施职责分离：柜员发起、主管复核授权，单人无法完成大额转账；同时所有操作遵循最小特权（柜员看不到后台配置）、需知（只看本网点客户）。安全策略写明"须职责分离"，由 IT 用 RBAC 双角色落地。

## 考试怎么考
- 各授权机制（隐式拒绝/矩阵/能力表/受限接口/内容相关/上下文相关）。
- 需知 vs 最小特权区别。
- 职责分离目的（防欺诈/错误、制衡）。
- 安全策略的定义与"定调不写实现"特征、需高层批准。

## 记忆口诀
> **"隐式拒绝是底线，ACL 能力表两相依；需知最小职责分，策略高层批不写细。"**

## 自测
1. 列出至少 4 种授权机制并简述。
2. Need to know 与 least privilege 的精确区别？
3. Separation of duties 如何防欺诈？
4. 安全策略（security policy）由谁批准？是否写实现细节？
5. Constrained interface 与 content-dependent / context-dependent 控制各举例。
