# Threat Modeling（威胁建模）

> 来源：Sybex CISSP 第10版 · Chapter 1 · Threat Modeling
> 域：Domain 1 安全与风险管理
> 模板：原书定义+对比表 / 真实案例 / 考试怎么考

## ① 一句话秒懂
威胁建模 = 系统化地找「**可能有什么威胁、概率多大、怎么防**」的过程，越早做越省——设计阶段堵漏比上线后砸墙便宜得多。

## ② 原书核心概念 + STRIDE 对比表
书里区分两种姿态，并给出识别威胁的视角与方法论：

**主动/防御式（Defensive）vs 被动/对抗式（Adversarial）**：

| 姿态 | 时机 | 目标 | 典型手段 |
|---|---|---|---|
| **Threat Modeling 威胁建模（防御式）** | 设计/开发期 | 预测**未发生**威胁，把防御设计进去 | STRIDE、PASTA、VAST |
| **Threat Hunting 威胁狩猎（对抗式）** | 部署后 | 用 **IoC（危害指标）** 找**已发生**的入侵 | 异常检测、IoC 匹配 |

> 关键区分：**威胁建模找"未发生"的 0day；威胁狩猎找"已发生"的入侵**。

**STRIDE 分类法（微软）**——每个字母对应一类威胁：

| 字母 | 威胁 | 破坏的安全属性 |
|---|---|---|
| **S**poofing 伪装身份 | 假冒他人/系统身份 | 真实性 Authenticity |
| **T**ampering 篡改 | 未授权修改数据/代码 | 完整性 Integrity |
| **R**epudiation 抵赖 | 否认做过的行为 | 不可抵赖 Nonrepudiation |
| **I**nformation disclosure 信息泄露 | 未授权披露 | 保密性 Confidentiality |
| **D**enial of Service 拒绝服务 | 资源不可用 | 可用性 Availability |
| **E**levation of Privilege 提权 | 获得本不应有的权限 | 授权 Authorization |

其他方法论：**PASTA**（七阶段、风险导向）、**VAST**（面向敏捷 Agile、可扩展）。

## ③ 生活类比（精炼）
装修前先想「小偷会从哪进、水管在哪爆」——设计阶段堵漏，比住进去再砸墙便宜得多。

## ④ 真实案例（概念落地）
**设计期未建模 → 上线后 SQL 注入致数据泄露**：某 Web 应用在开发时未做威胁建模，没识别"输入处可能被注入（对应 STRIDE 的 Tampering/Information Disclosure）"，上线后被拖库。若在设计阶段用 STRIDE 走一遍，本可在架构层加参数化查询与输入校验，返工成本极低；事后补救则要大改代码、道歉、赔钱。印证：威胁建模应**贯穿全生命周期**，越早越省。

## ⑤ 其余核心要点
- 识别威胁的三种视角：**聚焦资产 Assets / 聚焦攻击者 Attackers / 聚焦软件 Software**。
- 威胁建模不是一次性事件，应**贯穿系统全生命周期**。

## ⑥ 考试怎么考（题干样式 + 常见混淆）
- **题型（字母→威胁 / 场景→姿态）**：STRIDE 各字母含义必考；给"部署后用 IoC 找已发生危害"选 Threat Hunting。
- **常见混淆项（必记）**：
  1. **STRIDE 六字母**：S 伪装、T 篡改、R 抵赖、I 泄露、D 拒服、E 提权——常考两两对应安全属性。
  2. **Threat Modeling（事前找 0day）≠ Threat Hunting（事后用 IoC 找已发生危害）**。
  3. **威胁建模贯穿全生命周期**，非一次性。

## ⑦ 自测（改编自原书 Review Questions，附解析）
1. STRIDE 中的 "T" 代表？
   A. 篡改 Tampering　B. 追踪 Tracking　C. 信任 Trust
   **答案：A**。T = Tampering（篡改），破坏完整性。

2. 系统部署后，利用 IoC 寻找已发生危害的活动称为？
   A. 威胁建模 Threat Modeling　B. 威胁狩猎 Threat Hunting　C. 渗透测试
   **答案：B**。Threat Hunting 是事后用 IoC 找已发生入侵；威胁建模是事前。

---
*说明：本篇据初版要点扩写，关键术语与定义建议以原书为准。*
