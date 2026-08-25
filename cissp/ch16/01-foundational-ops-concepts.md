---
title: ① 一句话秒懂
parent: 第 16 章 · 安全运维管理
grand_parent: CISSP 认证安全工程师知识库
nav_order: 1
---

# ① 一句话秒懂

安全运营基础概念（Foundational Security Operations Concepts）是一套"管人管权"的底层原则：该尽的义务要尽（due care/diligence），权限给最少（least privilege），秘密按需要知（need-to-know），关键操作分人做（SoD），再用轮岗、强制休假、双人控制把内鬼风险压到最低。

# ② 生活类比

想象一家金库：
- **Due Care / Due Diligence（应有的注意/尽职调查）**：老板平时就得装监控、定规矩、定期查——不是出事后才补救，而是"持续合理地保护资产"，这样出事时老板能少担责。
- **Least Privilege（最小权限）**：每个员工只发够干活用的钥匙，绝不给万能钥匙。连清洁工都给管理员权限，他手滑或中招木马就全完了。
- **Need-to-Know（需者方知）**：你有"机密级"通行证，不代表你能看所有机密文件——只看你工作真正需要的那份。
- **SoD（职责分离）**：卖票的和检票的分两个人，谁都没法既收钱又放人进，想偷钱得两人合谋（collusion）。
- **双人控制（Two-person control）**：开保险箱要两把钥匙同时在场。
- **强制休假 / 轮岗**：让员工休一两周假或换岗，接手的人容易发现前任的猫腻。

# ③ 核心概念

## Due Care 与 Due Diligence
高管对员工资产保护负有直接责任。落实安全运营概念 + 定期审计 = 体现 due care and due diligence，可在损失发生时减轻高管责任。

## Need-to-Know vs Least Privilege
- **Need-to-Know**：只授予执行工作所需数据的访问权，**目的是保密**（keep secret secret）。常见于安全许可（clearance）——有 Secret 许可 ≠ 自动能看所有 Secret 数据，还要有 job 相关的 need-to-know。
- **Least Privilege**：主体只获"完成工作职责所必需"的权限（含数据权限与系统操作权），保护机密性与完整性。依赖清晰的岗位描述（job description）。不仅约束人，也约束**应用和服务账户**（历史常给服务账户全管理员权限，是重大错误）。

> 两者常被混用，但区别在：need-to-know 偏"信息保密"，least privilege 偏"权限最小化"。

## Segregation of Duties (SoD) / Separation of Duties
确保**没有单个人**对关键功能有完全控制。两人以上须合谋才能搞破坏，提高被发现风险。原书经典例子：审批发票与付款分离，防一人虚报冒领。

## Two-Person Control（双人控制 / Two-man rule）
关键任务需两人批准。如银行保险箱两把钥匙；PAM 把应急密码拆两半，需两人各输一半。

## Split Knowledge（知识分割）
把 SoD 与双人控制合并：执行操作所需的信息/权限分给两人以上，无人能单独 compromising 安全。

## Job Rotation（轮岗）
员工轮换岗位/职责，提供同事互查、减少欺诈、交叉培训（降低对单人的依赖）。既是威慑也是检测机制。

## Mandatory Vacations（强制休假）
通常 1–2 周，让他人接手职责，易发现 irregularities。金融业的标配反欺诈组合：SoD + 轮岗 + 强制休假。

## Privileged Account Management (PAM)
限制/监控特权账户（域管理员、企业管理员、root/sudo）。微软 PAM 基于 **JIT（Just-in-Time）管理**：用户平时不在特权组，需要时申请，秒级发放限时票据（如 15 分钟），票据过期即失效——可挫败 Kerberos 票据窃取攻击。PAM 还监控特权操作（建账户、改路由、改防火墙、访日志）并告警；SIEM 可检测恶意 PowerShell（如 Event ID 4104）。

# ④ 真实案例

**DHS/FBI 技术警报 TA17-239A（APT 攻击）**：攻击者用钓鱼邮件或漏洞攻陷单台系统后，提权并做一系列特权操作——删日志、把新账户加进 Administrators 组、开 3389 端口启用 RDP、关主机防火墙、跑脚本、建定时任务伪装正常用户。监控这些"常见特权操作"能在攻击早期就发现 APT，否则它能在网络里潜伏数年。

# ⑤ 考试怎么考

- **Need-to-Know vs Least Privilege** 的核心区别（保密 vs 权限最小化）。
- **SoD**  synonym = separation of duties；目的是防单人独控、需合谋。
- **Two-person control / Split knowledge** 定义。
- **Job rotation / Mandatory vacations** 既是威慑也是检测机制。
- **PAM 的 JIT** 原理（限时票据挫败 Kerberos 攻击）。
- Due care 与 due diligence 由**高管**负责。

# ⑥ 记忆口诀

> **"高管尽责 due care，最小权限 least 抓；需者方知保秘密，SoD 分权防独霸；双人控制拆密码，轮岗休假查欺诈；PAM 限时 JIT 卡，特权操作 SIEM 察。"**

# ⑦ 自测

1. Need-to-Know 与 Least Privilege 的本质区别是什么？
2. 为什么把"审批付款"和"执行付款"分给两个人能减少欺诈？（用 collusion 解释）
3. 什么是双人控制（Two-person control）和知识分割（Split knowledge）？
4. 轮岗和强制休假在安全上起到哪两类作用？
5. 微软 PAM 的 JIT 原则是如何挫败 Kerberos 票据攻击的？
