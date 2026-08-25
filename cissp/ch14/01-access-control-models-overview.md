---
title: 01 · 访问控制模型总览（DAC / MAC / RBAC / ABAC / 规则 / 风险）
parent: 第 14 章
grand_parent: CISSP 认证安全工程师知识库
nav_order: 1
---

# 01 · 访问控制模型总览（DAC / MAC / RBAC / ABAC / 规则 / 风险）

## 一句话秒懂
授权（authorization）有一堆现成"模型"可选：**自主 DAC**（主人说了算）、**强制 MAC**（标签说了算）、**角色 RBAC**（岗位说了算）、**属性 ABAC**（条件说了算）、**规则**（全局规则）、**风险基**（动态评估）。还有隐式拒绝、ACL、能力表等机制。

> 对应原书：Chapter 14 — "Comparing Access Control Models"

## 生活类比
- DAC = 你家的东西，你（主人）决定借谁。
- MAC = 军方保密室，标签不匹配（你没对应密级）一律进不去，不由你说了算。
- RBAC = 公司按岗位发门禁卡，调岗就换卡。
- ABAC = 不只看岗位，还要"你是经理 + 用平板 + 上班时间"才放行。

## 核心概念（大白话 + 原书定义）

**权限相关术语**：
- **Permission（权限）**：对对象的访问（读/写/删/执行文件，或库里检索/更新）。
- **Right（权利）**：在对象上采取某动作的能力（如改系统时间、恢复备份）——微妙区分。
- **Privilege（特权）**：提升的 rights + permissions 组合（如管理员全权）。

**核心机制**：
- **Implicit Deny（隐式拒绝 / 默认拒绝）**：除非显式授权否则拒绝——"deny by default"。几乎所有授权机制都用。
- **Access Control Matrix（访问控制矩阵）**：集中表，列主体/客体/权限；系统查表定权（比单 ACL 范围大，每对象还有独立 ACL）。
- **Capability List（能力表）**：**以主体为中心**，列该主体能访问哪些对象（vs ACL 以对象为中心）。
- **Constrained Interface（受限接口）**：按权限隐藏/禁用菜单项（Clark-Wilson 模型用）。
- **Content-Dependent（内容相关）**：按对象内容限制（如数据库 view 只显姓名邮箱，看不到底层表信用卡）。
- **Context-Dependent（上下文相关）**：需特定前置活动（如先结账才能下下载页）或日期/时间限制。

**六大模型**：
1. **DAC（自主访问控制）**：每对象有主人，主人可授予/拒绝他人。NTFS 用 DAC（ACL/DACL）。灵活但无集中管控。
2. **RBAC（基于角色）**：用角色/组，权限赋给角色，用户进组即得权。Windows 用组实现。易撤销（移出组即撤权），防 privilege creep，符合最小特权。相关 **TBAC（基于任务）** 按任务而非角色。
3. **Rule-Based（基于规则）**：全局规则对所有主体平等（如防火墙 ACL，末尾隐式拒绝）。注意：role-based 与 rule-based 都缩写 RBAC，CISSP 大纲区分二者。
4. **ABAC（基于属性）**：规则含多属性（用户/网络/设备），极灵活（如"允许经理用平板访问 WAN"）。SDN、MDM 常用。
5. **MAC（强制访问控制）**：主体与客体都贴**分类标签**，匹配才放行；格点模型（lattice），分等级/隔离/混合环境；比 DAC 更安全但不灵活。
6. **Risk-Based（基于风险）**：评估环境/情境/策略动态决策，可用机器学习；可要求 MFA、合规设备。

**原则**：**Need to Know（需知）**（有密级也须工作确实需要）、**Least Privilege（最小特权）**（含行动权）、**Separation of Duties（职责分离）**（敏感功能拆分防欺诈）。

> 口诀：**"DAC 主人定、MAC 标签定、RBAC 岗位定、ABAC 条件定；隐式拒绝是底线，需知最小职责分。"**

## 真实案例
公司文件服务器用 NTFS（DAC）员工自管权限，但核心财务系统用 RBAC（按岗位组赋权），调岗自动撤权；边界防火墙用 rule-based（隐式拒绝）；内部 SD-WAN 用 ABAC（"经理+公司设备+工作时间"才放行）。

## 考试怎么考
- 六大模型的核心特征与例子（DAC=NTFS，MAC=标签/格点，RBAC=组，ABAC=属性，Rule=防火墙，Risk=动态）。
- implicit deny / ACL vs capability list 区别。
- need to know vs least privilege 区别（后者含行动权）。
- 职责分离目的。
- role-based 与 rule-based 都缩 RBAC 但不同。

## 记忆口诀
> **"DAC 灵活主人管，MAC 严恪标签锁；RBAC 组赋权、ABAC 属性灵，规则全局风险动。"**

## 自测
1. 六大访问控制模型各的核心特征？举一个实现例子。
2. Implicit deny（隐式拒绝）是什么？为什么重要？
3. ACL（以对象为中心）与 capability list（以主体为中心）的区别？
4. Need to know 与 least privilege 的细微差别？
5. Separation of duties 的作用？
