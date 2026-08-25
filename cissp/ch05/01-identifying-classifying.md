---
title: 01 识别与分类信息资产（Identifying & Classifying Information and Assets）
parent: 第 5 章 · 保护资产安全
grand_parent: CISSP 认证安全工程师知识库
nav_order: 1
---

# 01 识别与分类信息资产（Identifying & Classifying Information and Assets）

> Domain 1 收尾篇 · 资产安全（Asset Security）的起点

## 一句话秒懂
分类就是给数据"贴标签、定身价"——标签越高，保护越狠。所有后续的安全控制都跟着分类走。

## 生活类比
给资产分类，就像机场给行李分级：普通托运行李（公开）随便放；笔记本电脑（敏感）要过 X 光；装有机密文件的公文包（机密/专有）得专人押运、全程不离视线。分类决定了"谁能碰、怎么运、丢了的后果多大"。

## 核心概念（大白话 + 原书定义）

### 1. 什么是敏感数据（Sensitive Data）
原书定义：任何非公开、非未分类的数据，组织因其价值或合规要求必须保护。包括 confidential、proprietary、protected 等。

三类最常见的"敏感"：
- **PII（个人可识别信息，Personally Identifiable Information）**：能识别某个人的信息。NIST SP 800-122 定义：①能区分或追踪个人身份的信息（姓名、SSN、生日、母亲娘家姓、生物特征）；②与之关联或可关联的信息（医疗、教育、财务、雇佣记录）。组织有保护 PII 的法定义务，泄露通常要通知当事人。
- **PHI（受保护健康信息，Protected Health Information）**：美国 HIPAA 规定的健康信息——只要是以电子形式传输或存储的健康信息都算（含电子病历、保险支付记录）。注意：教育记录、雇主营记录、死者超 50 年的记录**不算** PHI。HIPAA 不只管医院，还管保险公司、清算所及其"业务伙伴（business associate）"，所以美国大量企业都适用。
- **专有数据（Proprietary Data）**：帮组织保持竞争力的数据——源码、产品设计、内部流程、商业秘密、知识产权。竞争者拿到会重创组织使命。

### 2. 数据分类标签（Classification Labels）
**政府体系**（按泄露损害递增）：
| 等级 | 泄露损害措辞 | 说明 |
|---|---|---|
| Top Secret | exceptionally grave damage（特别严重损害） | 最高 |
| Secret | serious damage（严重损害） | 中高 |
| Confidential | damage（损害） | 中 |
| Unclassified | 不符合以上 | 公开可索取（FOIA） |

还有 FOUO / SBU / CUI 等"未分类的子类"，分发受控。

**民用/企业体系**（无强制标准，组织自选标签，常见）：
| 标签 | 泄露损害 | 典型例子 |
|---|---|---|
| Confidential / Proprietary（最高） | exceptionally grave damage | 未发布电影、核心源码（如索尼被窃 100+ TB 数据） |
| Private | serious damage | PII、PHI、员工薪资数据 |
| Sensitive | damage | 内部网络拓扑、IP 地址 |
| Public | 无 | 官网内容（但需保护完整性防篡改） |

> 关键：无论用哪套标签，组织都有义务保护敏感信息。**资产分类要与数据分类匹配**——跑 Top Secret 数据的电脑，本身也得标 Top Secret，并贴醒目标签。

### 3. 数据三态（Data States）—— 保护要覆盖全程
| 状态 | 含义 | 保护手段 |
|---|---|---|
| **At rest（静止）** | 存在硬盘/SSD/U 盘/磁带/SAN 上 | 强对称加密（如 AES-256） |
| **In transit（传输）** | 经有线/无线/公网传输 | 对称+非对称加密组合（TLS） |
| **In use（使用）** | 在内存/临时缓冲区被应用处理 | 用后 flush 缓冲区；同态加密可在密文上运算 |

## 真实案例
- **索尼影业**：攻击者窃走 100+ TB 数据（含未上映电影），迅速流入文件共享站，专家估计被下载近百万次，直接冲击票房——这就是"专有数据"泄露造成 exceptionally grave damage 的实例。
- **ITRC 统计**：2023 年全球 3,205 起数据泄露，波及 3.53 亿人——足见分类与保护缺失的普遍代价。

## 考试怎么考
- 题型 A：给一段场景（"某组织泄露了员工薪资表"），问属于哪种分类标签 → 通常是 **Private**。
- 题型 B：问"数据在内存中被应用处理"属于哪种状态 → **In use**；问"数据在数据库里" → **At rest**；问"经互联网发送" → **In transit**。
- 必记混淆项：① PII 与 PHI 的区别——PHI 是健康信息且受 HIPAA 约束，PII 更广；② 资产分类**必须匹配**其处理的数据分类；③ 政府体系最高是 Top Secret，企业体系最高通常是 Confidential/Proprietary。

## 记忆口诀
> **"敏分三类：人(PII)病(PHI)秘(专有)；标签四级：高私敏公；三态：静传用。"**

## 自测
1. 一家美国医院把患者电子病历卖给第三方分析公司，这违反了哪部法律对 PHI 的保护？（答：HIPAA）
2. 信用卡数据正被 Web 应用放在内存缓冲区里做交易校验，这属于数据的哪种状态？（答：In use）
