---
title: 知识型 AI 系统与存储威胁（AI/Expert Systems & Storage Threats）
parent: 第 20 章
grand_parent: CISSP 认证安全工程师知识库
nav_order: 3
---

# 知识型 AI 系统与存储威胁（AI/Expert Systems & Storage Threats）

> 来源：Chapter 20 · Understanding Knowledge-Based Systems / Storage Threats
> 域：Domain 8 Security and Risk Management（安全与风险管理）
> 模板：原书定义+对比表 / 真实案例 / 考试怎么考

## ① 一句话秒懂
三类"会思考"的系统（专家系统 / 机器学习 / 神经网络）能帮安全人员秒级分析海量日志；但存储侧别只顾"前门"，**后门（存储介质、隐蔽通道）**也得锁好。

## ② 原书核心定义 + 对比表

**知识型 AI 三类系统**：

| 系统 | 核心组成 / 机制 | 特点 |
|---|---|---|
| Expert System（专家系统） | 知识库（if/then 规则）+ 推理引擎（inference engine） | 决策不受情绪干扰；优于常规重复决策 |
| Machine Learning（机器学习） | 从数据自动建模 | 监督（有标签）/ 无监督（无标签） |
| Neural Network（神经网络） | 多层计算单元链式求和 | 深度学习子集；训练用 Delta rule 定权重 |

**存储两大威胁（Storage Threats）**：

| 威胁 | 说明 | 对策 |
|---|---|---|
| 非法访问存储资源 | 绕过 OS 直读物理介质 | 加密文件系统（EFS）、云 S3 强默认策略 |
| Covert storage channel（隐蔽存储通道） | 借共享存储跨密级传数据 | 隐蔽通道分析（见 Ch8） |

## ③ 生活类比（精炼）
专家系统像老法师的"经验手册"（if/then）+ "判案大脑"（推理引擎）；ML 像学生从例题（标签）学规律，或自己摸索（无监督）；神经网络像模仿人脑的一串"加权投票"。存储威胁像家里只锁了正门，后院篱笆破洞任人钻。

## ④ 真实案例
- **信贷决策专家系统**：银行用专家系统替代信贷员，避免"Jim 虽欠费但人挺好"的情绪化误判。
- **云存储误配置暴露**：AWS S3 一个默认公开的策略错误，即可把敏感数据暴露公网——强调强默认 + 监控变更。

## ⑤ 相关概念梳理 + 对比表

**监督 vs 无监督学习**：

| 类型 | 训练数据 | 例子 |
|---|---|---|
| 监督 Supervised | 带"正确答案"标签 | 标好恶意登录→学模型 |
| 无监督 Unsupervised | 无标签 | 算法自聚类，人再甄别异常群 |

**多层安全环境**：共享内存/存储须设分级控制，防低密级读高密级数据。

**AI 在安全中的应用**：快速一致地处理海量日志/审计数据，发现异常——"天作之合"。

## ⑥ 考试怎么考（题干样式 + 常见混淆项）
- 题干："An AI system with a knowledge base of if/then rules and an inference engine is a(n)?" → 答 **Expert System**。混淆：神经网络无显式规则库。
- 题干："Training a model with unlabeled data is?" → 答 **Unsupervised learning**。混淆：监督学习需标签。
- 题干："Covertly transmitting data between security levels via shared storage is a?" → 答 **Covert storage channel**。混淆：covert timing channel 借时序而非存储。
- 题干："The component of an expert system that draws conclusions is the?" → 答 **Inference engine**。混淆：knowledge base 只存规则。

## ⑦ 自测（改编自原书 Review Questions，附解析）
1. 专家系统由哪两大部分组成？
   - A. 数据集 + 算法
   - B. 知识库 + 推理引擎
   - C. 神经网络 + 权重
   - D. 输入 + 输出
   - **答案：B**。解析：知识库存 if/then 规则，推理引擎据此推导结论，是专家系统两大核心。

2. 使用无标签数据训练模型属于？
   - A. 监督学习
   - B. 无监督学习
   - C. 强化学习
   - D. 深度学习
   - **答案：B**。解析：无监督学习不给"正确答案"，算法自行建模；监督才需标签。

3. 通过操纵磁盘剩余空间大小跨密级传递信息，属于？
   - A. 聚合攻击
   - B. 隐蔽存储通道
   - C. 推理攻击
   - D. 后门
   - **答案：B**。解析：covert storage channel 借共享存储介质（如空闲空间大小）传数据；属隐蔽通道一类。
