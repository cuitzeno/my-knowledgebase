---
title: 08 · 身份生命周期与权限审查（Provisioning Life Cycle）
parent: 第 13 章 · 身份与认证管理
grand_parent: CISSP 认证安全工程师知识库
nav_order: 8
---

# 08 · 身份生命周期与权限审查（Provisioning Life Cycle）

## 一句话秒懂
账号有生老病死：**入职开通（provisioning）→ 在职调整 → 离职注销（deprovisioning）**。两大毒瘤是"权限过多（excessive privilege）"和"权限蠕变（privilege creep）"，靠定期账户审查发现。

> 对应原书：Chapter 13 — "Managing the Identity and Access Provisioning Life Cycle"

## 生活类比
员工入职发门禁卡（开通），调岗要加减权限（调整），离职立刻收卡删号（注销）。最怕的是：人调走了老权限没撤（权限蠕变），或者给的权限远超岗位需要（权限过多）——都等于把不该开的门一直开着。

## 核心概念（大白话 + 原书定义）

**生命周期四阶段**：创建、管理、审查/审计、删除。无良好账户管理就无法准确标识、认证、授权、问责。

**入职开通（Provisioning & Onboarding）**：
- 先**证明身份**（照片 ID/出生证/背调/信用查/政审/FBI 库等）再注册。
- 自动化开通：HR 转请求给 IT，按规则建账号（如重名加 2：`suziejones2`），按部门/角色自动加组（组已预赋权）。
- 发放硬件（笔记本/手机/令牌/智能卡）并**准确记录**。
- Onboarding：签 AUP、安全培训、配密码管理器、配 2FA、教访问资源。

**离职注销（Deprovisioning & Offboarding）**：
- 最简单是删账号（account revocation），但可能丢掉用户加密数据的唯一解密密钥。
- 多数组织先**禁用账号**，主管复查数据后再删；禁用账号通常 **30 天内删**（可调整）。
- 离职后仍留账号 → **破坏（sabotage）风险高**；且他人可用其账号作案、日志却记在离职者名下。
- 收回发放的所有硬件；终止员工福利（曾有大学漏停 924 人医保、白付 800 万美元）。

**角色定义与转换（Role Definition & Transition）**：新建岗位须定义角色与所需权限（用组赋权）。

**账户维护与审查（Account Maintenance & Access Review）**：
- 定期检查**用户/特权/系统/服务**账号，防权限过剩。
- 脚本查**闲置账号**（如 30 天未登自动禁用）、查特权组成员。
- **特权监控（privilege monitoring）**：盯管理员/root/服务等高权账号。

**两大问题**：
- **Excessive Privilege（权限过多）**：权限超过岗位所需 → 撤销多余。
- **Privilege Creep（权限蠕变）**：岗位变动后旧权限未收回，新权限又加，越积越多（如 Karen 从会计调销售，会计权限没撤）。两者都违反**最小特权原则**，靠账户审查发现。

> 口诀：**"开转禁删四步走，证明身份才注册；权限多、蠕变两毒瘤，定期审查除隐患。"**

## 真实案例
员工从财务调岗到市场，HR 未及时撤财务系统权限（privilege creep），三年后该账号被盗，攻击者用残留财务权限转移资金。事后公司上线季度账户审查 + 自动闲置禁用脚本。

## 考试怎么考
- 生命周期四阶段；provisioning/deprovisioning 定义。
- 为何先禁用而非直接删（防丢解密密钥、留复查）。
- 离职账号保留风险；30 天删除惯例。
- excessive privilege vs privilege creep 区别，均违反最小特权。
- 账户访问审查覆盖哪些账号类型。

## 记忆口诀
> **"开禁删、证身份；权限蠕变悄悄积，审查常态莫大意。"**

## 自测
1. 身份与访问生命周期包含哪几个阶段？
2. 为什么离职时通常先"禁用"而非直接"删除"账号？
3. Excessive privilege 与 privilege creep 的区别？都违反了什么原则？
4. 账户访问审查（account access review）应覆盖哪些账号类型？
5. 自动化开通（automated provisioning）如何减少人为错误？
