# 08 · 零信任与访问控制攻击（Zero-Trust & Attacks）

## 一句话秒懂
零信任＝"从不信任、持续验证"，没有内外部边界，每次访问都按身份/设备/威胁情报动态判。访问攻击的核心是**偷凭据→冒名/提权/横向移动**；防护靠最小特权、MFA、日志。

> 对应原书：Chapter 14 — "Zero-Trust Access Policy Enforcement" / "Understanding Access Control Attacks"

## 生活类比
传统安全像城堡护城河（进了门就信你）；零信任像每次进每个房间都要重新刷脸+查健康码+看设备是否合规，且随时可能收回权限。

## 核心概念（大白话 + 原书定义）

**零信任（Zero-Trust，NIST SP 800-207）**：
- 不同于"城堡护城河"或纵深防御，假定**无信任边界、无网络边缘**。
- 每次请求都作为**持续认证**一部分验证，访问前须过策略检查：身份、权限、系统配置与安全状态、威胁情报、安全姿态。
- 核心组件：
  - **Subject（主体）**：用户/服务/系统请求访问者。
  - **Policy Engine（策略引擎）**：基于规则+外部系统（威胁情报/IdM/SIEM）用信任算法决定授予/拒绝/撤销。
  - **Policy Administrator（策略管理员）**：建立/切断主体与资源间通信路径，发会话令牌；拒绝时通知 PEP 结束会话。
  - **Policy Engine + Administrator = Policy Decision Point（PDP，策略决策点）**。
  - **Policy Enforcement Point（PEP，策略执行点）**：转发请求、接收指令允许/结束连接。

**访问控制攻击基础**：
- **Cracker（骇客/恶意者）** vs **Hacker（原指无恶意技术爱好者，现媒体混用）**；书里用 **attacker** 指恶意入侵者。**Attack**＝利用漏洞损害 CIA 的任何尝试。
- **Risk Elements**：风险＝威胁利用漏洞致损；威胁（自然/人为/意外）、漏洞（弱点/缺控制）。风险管理无法消除只能降险。

**常见访问攻击**：
- 多从**偷凭据**开始 → 在线冒名（impersonation）登录取资源；或绕过认证直接偷数据。
- **Privilege Escalation（权限提升）**：
  - **Vertical（纵向）**：从普通用户提到管理员（如 phishing 中招后用 Mimikatz 提权）。
  - **Horizontal（横向）**：拿到同级别其他账户同等权限。
  - 两者结合＝**Lateral Movement（横向移动）**：普通账户→提权→横向扩到其他机→再提权，最终常获域管（domain admin）。
  - **Mimikatz**：从内存抓凭据逐步提权的工具。
- **Managed Service Accounts**：须只给服务所需权限，勿图省事用 LocalSystem（全权）。
- **su / sudo（Linux）**：`su` 切 root（日志记 su 账户）；`sudo` 用自己凭据以 root 跑命令（日志记用户本人，有审计）。推荐 sudo 而非直接 root 登录。

> 口诀：**"零信任无边界、持续验；PEP 执行、PDP 决策（引擎+管理员）；攻击偷凭据、提权横移 Mimikatz，sudo 审计胜 su。"**

## 真实案例
某网被钓鱼拿到普通员工账号，攻击者用 Mimikatz 提权到本地管理员，再横向移动至多台服务器，最终夺取域控。若部署零信任（持续验证+设备合规+异常即撤权）并在 Linux 强制 sudo 审计，攻击链可被早期掐断。

## 考试怎么考
- 零信任核心（无边界、持续验证、PEP/PDP 组件）。
- PDP = Policy Engine + Policy Administrator；PEP 执行。
- privilege escalation 纵向/横向区别；lateral movement 与 Mimikatz。
- attacker/cracker/hacker 术语区分。
- su vs sudo（审计差异）。

## 记忆口诀
> **"零信任无边界持续验，PEP 执行 PDP 决；提权纵上横平移，Mimikatz 步步高，sudo 留痕 su 不留。"**

## 自测
1. 零信任与传统边界安全的核心区别？NIST 文档号？
2. 零信任架构中 PEP、Policy Engine、Policy Administrator、PDP 各是什么？PDP 包含哪两个？
3. Vertical 与 horizontal privilege escalation 区别？lateral movement 是什么？
4. 为什么 Mimikatz 在攻击链中关键？
5. su 与 sudo 在 Linux 审计上的区别？
