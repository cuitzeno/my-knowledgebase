# Ch8-02 十一条安全设计原则（CISSP 目标 3.1）

> 所属域：Domain 3 Security Architecture and Engineering
> 对应原书：Chapter 8 — Secure Design Principles（后半，11 条原则）

## ① 一句话秒懂
CISSP 目标 3.1 列出 **11 条安全设计原则**：本章讲 6 条（安全默认、安全失败、KISS、零信任、隐私内建、SASE），其余 5 条分散在其他章节。

## ② 生活类比
买新车，出厂**默认设置**往往为"好开"而非"安全"——自动解锁、默认密码就像车商为了让你容易上手。真正安全得自己改：锁死车门、设强密码。这就是"安全默认"。

## ③ 核心概念（大白话 + 原书定义）

**本章覆盖的 6 条：**

1. **安全默认（Secure / Restrictive Defaults）**：默认配置应最严格。绝不假设出厂设置安全——它们通常为了降低技术支持成本而宽松。管理员必须按策略改配置。趋势是安全产品开始"默认最严"，但会牺牲易用性。

2. **安全失败（Fail Securely）**：出错时应落到安全状态。区分**物理**与**数字**语境：
   - 物理：fail-safe（保人，如紧急门自动开）、fail-secure（保资产，如金库门自动锁）。
   - 数字：fail-open（保**可用性**，继续通信）、fail-closed / fail-secure（保**保密性与完整性**，切断通信）。
   - fail-soft：组件坏了系统还能跑（如一个 app 崩了其他继续）。
   - IETF 建议数字语境**别用 fail-safe**，以免引入人安暗示。

3. **保持简单小巧（KISS / Keep It Simple and Small）**：系统越复杂越难安全。相关概念：DRY（不重复代码）、计算极简主义、Rule of Least Power（用最弱合适的语言）、Worse Is Better（功能少反而更好）、YAGNI（不到需要时不写）。

4. **零信任（Zero Trust）**："永不信任，始终验证（never trust, always verify）"。假设已被攻破（assume breach），每次请求都认证、授权、加密。需微隔离（microsegmentation）、最小权限、持续实时监控。标准：NIST SP 800-207。

5. **信任但验证（Trust but Verify）**：传统"内网默信任"做法，已被证明不够，专家推荐转向零信任。

6. **隐私内建（Privacy by Design, PbD）**：早期设计阶段就嵌入隐私保护。7 原则：主动非被动、默认隐私、嵌入设计、正和（positive-sum）、端到端保护、透明、尊重用户。GDPR 有体现；衍生出 Global Privacy Standard（GPS）。

7. **SASE（Secure Access Service Edge）**：云原生框架，把网络安全与 WAN 能力合一，以**身份为中心**，用 ZTNA 实现零信任，靠边缘计算降延迟。常作为服务订阅。

**其余 5 条（在其他章节）：**
- 威胁建模（Threat Modeling）、纵深防御（Defense in Depth）→ Chapter 1
- 最小权限（Least Privilege）、职责分离（Segregation of Duties）→ Chapter 16
- 共同责任（Shared Responsibility）→ Chapter 9

> 原书提示："It is essential to read questions carefully" —— 因为 open/closed 与 open-source/closed-source 术语极易混淆。

## ④ 真实案例
- **Mirai 僵尸网络**：大量摄像头 / 路由器用出厂默认密码，被组成僵尸网络——"默认设置不安全"的代价。
- **零信任实践（Google BeyondCorp）**：取消内网 VPN 信任，所有访问基于"设备 + 用户身份"持续验证。
- **震网（Stuxnet）**：利用了硬编码 / 默认密码与"信任内部网络"的假设。

## ⑤ 考试怎么考
- 给失败场景选 fail-open 还是 fail-closed：问"保可用性" → fail-open；问"保 C/I" → fail-closed。
- 物理 fail-safe vs fail-secure 区别（保人 vs 保资产）。
- 零信任核心：never trust always verify、assume breach、microsegmentation。
- KISS 相关概念（DRY / YAGNI 等）作为干扰项。
- PbD 的 7 原则、GPS；SASE 的"身份为中心 + ZTNA"。

## ⑥ 记忆口诀
- 六原则：默认严、失败稳、简单小、零信任、隐私嵌、SASE 云。
- 失败分语境：物理保人 safe 开、保产 secure 锁；数字保用 open 通、保密闭切断。
- 其余五条在别章：威胁建模纵深防（Ch1）、最小权职责分（Ch16）、共担责（Ch9）。

## ⑦ 自测
1. 为什么"默认设置通常不安全"？管理员应持什么假设？
2. 数字语境下，保可用性与保保密性 / 完整性分别对应 fail-open 还是 fail-closed？
3. 零信任的 three 关键词是什么？（never trust always verify / assume breach / microsegmentation）
4. PbD 的 7 条原则你能说出几条？
