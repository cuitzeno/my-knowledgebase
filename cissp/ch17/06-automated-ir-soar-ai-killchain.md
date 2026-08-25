---
title: ① 一句话秒懂
parent: 第 17 章 · 事件预防与响应
grand_parent: CISSP 认证安全工程师知识库
nav_order: 6
---

# ① 一句话秒懂

自动化事件响应（Automating IR）用 SOAR 把"重复的救火动作"编成剧本自动执行，再借 AI/ML 提升检测智能，用威胁情报（Kill Chain、MITRE ATT&CK）理解攻击全链条——让响应更快、更准、更少靠人。

# ② 生活类比

- **Playbook（剧本）** = 消防手册，写清楚"确认火情→拉闸→喷水"每一步。
- **Runbook（运行手册）** = 把手册编进自动灭火系统，火一探到就自动执行。
- **Kill Chain（杀伤链）** = 把"敌人进攻"拆成找目标→定位→跟踪→选武器→开火→评估 六步，只要打断任意一步，攻击就失败。
- **MITRE ATT&CK** = 攻击手法的大字典（战术×技术），活文档每半年更新。

# ③ 核心概念

## SOAR（安全编排、自动化与响应）
- 让组织**自动响应**部分事件，减少人工重复操作。
- **Playbook（剧本）**：文档/清单，定义如何**验证**事件 + 响应细节（如 SYN flood 的验证与缓解步骤）。可作 SOAR 失效时的手动备份。
- **Runbook（运行手册）**：把 playbook 实现进自动化工具，按条件步骤自动验证+缓解。
> 业界对两词定义不完全统一，但 IR 语境：playbook 定义动作，runbook 自动执行。

## AI 与 ML（厘清区别）
- **Machine Learning（机器学习）**：AI 的子集，系统通过经验**自动改进**。先给规则/基线（如行为检测的网络基线），运行中检测异常，管理员反馈 false positive 后自我修正基线。
- **Artificial Intelligence（人工智能）**：更广领域包含 ML，让机器做原需人类智能的事。AI 系统**从零开始**自己学规则（如不知围棋怎么走，靠外部算法给反馈，自创算法+ML 学策略）。
- 简记：**ML 起步有规则，AI 起步无规则自己建**。行为检测系统就是 ML/AI 在安全的应用。

## Threat Intelligence（威胁情报）
- 收集潜在威胁数据，用多源获取及时威胁信息，主动"狩猎"威胁。

## Cyber Kill Chain（网络杀伤链，Lockheed Martin）
七阶段有序攻击链，打断任一阶段即失败：
1. **Reconnaissance（侦察）**
2. **Weaponization（武器化）**：找目标易感的漏洞 + 投递方法。
3. **Delivery（投递）**：钓鱼/恶意附件/挂马网站等。
4. **Exploitation（利用）**：武器触发漏洞。
5. **Installation（安装）**：装恶意软件（含后门，远程控制）。
6. **Command and Control（C2）**：维持指挥控制。
7. **Actions on Objectives（达成目标）**：偷钱/偷数据/销毁/勒索。
> 防御思路：用户在投递阶段不上当，链就断。

## MITRE ATT&CK Matrix
- MITRE 创建的 **TTPs（战术/技术/过程）** 知识库，与 Kill Chain 互补但**战术不分先后**（矩阵形式）。
- 战术列：Reconnaissance、Resource Development、Initial Access、Execution、Persistence、Privilege Escalation、Defense Evasion、Credential Access、Discovery、Lateral Movement、Collection、Command and Control、Exfiltration、Impact。
- 活文档，至少每年更新两次；点进战术看技术、缓解与检测建议。

# ④ 真实案例

设想 SYN flood 打向 DMZ 服务器：传统做法——工具报警→管理员人工确认→手动改服务器 ACK 等待时间→攻击停后再手动改回。SOAR 下，playbook 写清验证与响应步骤，runbook 让 IDS 检测到流量自动按剧本验证并缓解，全程无需人工熬夜。这就是 SOAR 把"人肉重复劳动"变成"自动编排"的价值。

# ⑤ 考试怎么考

- **SOAR** 定义；**Playbook（定义/验证/手动备份）vs Runbook（自动执行）**。
- **ML vs AI**：ML 属 AI、起步有规则靠经验改进；AI 更广、从零自学。
- **Cyber Kill Chain 七阶段**顺序；防御=打断任一阶段。
- **MITRE ATT&CK**：战术矩阵、不分先后、TTPs、活的（半年更）。
- 行为检测系统 = ML/AI 应用实例。

# ⑥ 记忆口诀

> **"SOAR 编排自动化，playbook 写 runbook 跑；ML 有规则 AI 自学，行为检测是其招；杀伤链七步序，断一环则攻击消；ATT&CK 矩阵战术列，TTP 活典半年调。"**

# ⑦ 自测

1. SOAR 中 playbook 与 runbook 的区别是什么？playbook 还有什么额外作用？
2. 机器学习（ML）与人工智能（AI）的根本区别是什么？行为检测系统属于哪类？
3. Lockheed Martin 网络杀伤链的七个阶段按顺序是什么？防御的核心思路是什么？
4. MITRE ATT&CK 与 Kill Chain 模型的主要区别是什么？（提示：顺序 vs 矩阵、TTPs）
5. 举出至少 5 个 MITRE ATT&CK 的战术名称。
