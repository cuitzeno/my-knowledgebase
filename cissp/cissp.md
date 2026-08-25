# CISSP 通俗考点短文库

> 教材：*ISC2 CISSP Official Study Guide, 10th Edition (2024, Sybex)* · 共 1899 页 / 21 章
> 目标：把手册「全面消化」成**多篇通俗短文**，对每个考点用大白话讲清楚。
> 学习方式：滚动周计划，每周 6–8 小时（无考试死线，按节奏兜底）。

---

## 一、已锁定方案（设计树已共识）

| 项 | 决策 |
|---|---|
| 范围 | 全 8 域（按书本章节顺序 Ch1→Ch21） |
| 粒度 | 按「小节 / 单个考点」拆成多篇短文（**加厚版每篇 800–1200 字**，含原书定义+对比表 / 真实案例 / 考试怎么考） |
| 单篇结构（加厚版） | ①一句话秒懂 ②原书核心定义+对比表 ③生活类比(精简) ④真实案例 ⑤相关概念梳理(+表) ⑥考试怎么考(题型+混淆项) ⑦自测(附解析) |
| 术语 | 中文为主，关键英文术语括注（CISSP 题为英文） |
| 自测题 | 改编自原书每章 Review Questions，附解析 |
| 交付 | 本目录 `cissp-notes/`，每篇一个 `.md` + 本总索引 |
| 排期 | 完整周计划（见 `cissp-study-plan.md`，已覆盖 8 域 21 章 + 总复盘） |

> **加厚标准定型说明（2026-08-23）**：初版（300–600 字、偏类比）经用户反馈"太简单"后，用 grilling 校准并确认样品（原 `02-security-concepts-PROTOTYPE.md`，已转正）。定型为上方加厚版：保留口语开头，但补「原书精确定义 + 对比表 / 真实案例 / 考试怎么考」三块干货，篇幅 800–1200 字。后续 Ch2 起直接套用，不再每篇征询。

## 二、文章模板（加厚版，每篇统一）

```
# <考点名>（中英）
> 来源：Chapter X · <小节>
> 域：Domain N <名称>
> 模板：原书定义+对比表 / 真实案例 / 考试怎么考
① 一句话秒懂
② 原书核心定义 + 对比表（引 Sybex 措辞，考试常考定义对应）
③ 生活类比（精炼，不当主角）
④ 真实案例（概念落地，知名事件）
⑤ 相关概念梳理 + 对比表
⑥ 考试怎么考（题干样式 + 常见混淆项）
⑦ 自测（改编自原书 Review Questions，附解析）
```

## 三、章节 → 域 映射与进度

| 章 | 标题 | 域 | 状态 |
|---|---|---|---|
| Ch1 | Security Governance Through Principles and Policies | D1 | ✅ 8 篇已生成（**加厚标准**） |
| Ch2 | Personnel Security and Risk Management Concepts | D1 | ✅ 7 篇已生成（加厚版） |
| Ch3 | Business Continuity Planning | D1 | ✅ 4 篇已生成（加厚版） |
| Ch4 | Laws, Regulations, and Compliance | D1 | ✅ 6 篇已生成（加厚版） |
| Ch5 | Protecting Security of Assets | D1 | ✅ 5 篇已生成（加厚版） |
| Ch6 | Cryptography and Symmetric Key Algorithms | D3 | ✅ 4 篇已生成（加厚版） |
| Ch7 | PKI and Cryptographic Applications | D3 | ✅ 6 篇已生成（加厚版） |
| Ch8 | Principles of Security Models, Design, and Capabilities | D3 | ✅ 6 篇已生成（加厚版） |
| Ch9 | Security Vulnerabilities, Threats, and Countermeasures | D3 | ✅ 9 篇已生成（加厚版） |
| Ch10 | Implementing Physical Security | D3 | ✅ 8 篇已生成（加厚版） |
| Ch11 | Secure Network Architecture and Components | D4 | ✅ 10 篇已生成（加厚版） |
| Ch12 | Secure Communications / Network Components | D4 | ✅ 9 篇已生成（加厚版） |
| Ch13 | Security Network Management | D4 | ✅ 8 篇已生成（加厚版） |
| Ch14 | Controlling and Monitoring Access | D5 | ✅ 8 篇已生成（加厚版） |
| Ch15 | Security Assessment and Testing | D6 | ✅ 5 篇已生成（加厚版） |
| Ch16 | Foundational Security Operations | D7 | ✅ 6 篇已生成（加厚版） |
| Ch17 | Incident Response / Detection & Prevention | D7 | ✅ 6 篇已生成（加厚版） |
| Ch18 | Disaster Recovery / BCP | D7 | ✅ 6 篇已生成（加厚版） |
| Ch19 | Investigations, Ethics (Software Dev Security) | D8 | ✅ 3 篇已生成（加厚版） |
| Ch20 | Systems Development Controls / Databases | D8 | ✅ 3 篇已生成（加厚版） |
| Ch21 | Malicious Code and Application Attacks | D8 | ✅ 7 篇已生成（加厚版） |

> 说明：Sybex 章节顺序大体对应 8 大域顺序，生成按 Ch1→Ch21 推进；精确的「章→域」以原书 Objective Map 为准，生成到对应章时再校准。

## 四、已生成文章索引

### Domain 1 · Ch1 Security Governance Through Principles and Policies（加厚版）
- [01 Security 101](cissp/ch01/01-security-101.md)
- [02 Understand and Apply Security Concepts](cissp/ch01/02-security-concepts.md)
- [03 Security Boundaries](cissp/ch01/03-security-boundaries.md)
- [04 Evaluate and Apply Security Governance Principles](cissp/ch01/04-governance-principles.md)
- [05 Manage the Security Function](cissp/ch01/05-manage-security-function.md)
- [06 Security Policy, Standards, Procedures, and Guidelines](cissp/ch01/06-policy-standards.md)
- [07 Threat Modeling](cissp/ch01/07-threat-modeling.md)
- [08 Supply Chain Risk Management](cissp/ch01/08-supply-chain-rm.md)

### Domain 1 · Ch2 Personnel Security and Risk Management Concepts（加厚版）
- [01 Personnel Security Lifecycle（雇佣生命周期）](cissp/ch02/01-personnel-lifecycle.md)
- [02 Ongoing Oversight & Third-Party Controls（持续监督与第三方）](cissp/ch02/02-oversight-thirdparty.md)
- [03 Risk Core Concepts（威胁/漏洞/暴露/资产估值）](cissp/ch02/03-risk-core-concepts.md)
- [04 Risk Assessment（定性/定量与 SLE/ARO/ALE）](cissp/ch02/04-risk-assessment.md)
- [05 Risk Response（风险应对策略）](cissp/ch02/05-risk-response.md)
- [06 Social Engineering（社会工程）](cissp/ch02/06-social-engineering.md)
- [07 Security Awareness, Training & Education（安全意识/教育/培训）](cissp/ch02/07-awareness-training.md)

### Domain 1 · Ch3 Business Continuity Planning（加厚版）
- [01 BCP Planning & Scope（BCP 规划与范围）](cissp/ch03/01-planning-scope.md)
- [02 Business Impact Analysis（BIA 业务影响分析）](cissp/ch03/02-bia.md)
- [03 Continuity Planning（连续性计划）](cissp/ch03/03-continuity-planning.md)
- [04 Plan Approval, Implementation & Training（审批/实施/演练）](cissp/ch03/04-approval-implementation.md)

### Domain 1 · Ch4 Laws, Regulations, and Compliance（加厚版）
- [01 Legal System & Computer Crime（法律体系与计算机犯罪法）](cissp/ch04/01-legal-system.md)
- [02 Major US Cyber/Privacy Laws（主要联邦网络安全与隐私法）](cissp/ch04/02-major-laws.md)
- [03 Intellectual Property（知识产权）](cissp/ch04/03-intellectual-property.md)
- [04 Privacy Laws（隐私法）](cissp/ch04/04-privacy-laws.md)
- [05 Software Licensing & Import/Export（软件许可与进出口管制）](cissp/ch04/05-software-licensing-import-export.md)
- [06 State Privacy, PCI DSS & Vendor Governance（州隐私/PCI DSS/供应商治理）](cissp/ch04/06-state-compliance-vendor.md)

> **Domain 1 进度（Ch1–Ch4）**：共 **25 篇**加厚短文已落地。

### Domain 2 · Ch5 Protecting Security of Assets（加厚版）
- [01 Identifying and Classifying Information and Assets（数据/资产识别与分级）](cissp/ch05/01-identifying-classifying.md)
- [02 Establishing Information and Asset Handling Requirements（留存/销毁/净化）](cissp/ch05/02-handling-requirements.md)
- [03 Data Protection Methods（DRM/CASB/匿名化/令牌化）](cissp/ch05/03-data-protection-methods.md)
- [04 Understanding Data Roles（数据角色/GDPR 角色）](cissp/ch05/04-data-roles.md)
- [05 Security Baselines（NIST SP 800-53B/Scoping/Tailoring）](cissp/ch05/05-security-baselines.md)

### Domain 3 · Ch6 Cryptography and Symmetric Key Algorithms（加厚版）
- [01 Crypto Goals & Foundations（CIA+不可否认/混淆扩散/XOR）](cissp/ch06/01-crypto-goals-foundations.md)
- [02 Symmetric vs Asymmetric（对称/非对称对比）](cissp/ch06/02-symmetric-vs-asymmetric.md)
- [03 Symmetric Algorithms & Modes（DES/3DES/AES/分组模式）](cissp/ch06/03-symmetric-algorithms-modes.md)
- [04 Crypto Lifecycle & Key Management（生命周期/M-of-N）](cissp/ch06/04-crypto-lifecycle-key-mgmt.md)

### Domain 3 · Ch7 PKI and Cryptographic Applications（加厚版）
- [01 Asymmetric Algorithms（RSA/DH/ECC/后量子）](cissp/ch07/01-asymmetric-algorithms.md)
- [02 Hash Functions（MD5/SHA 家族/RIPEMD）](cissp/ch07/02-hash-functions.md)
- [03 Digital Signatures & HMAC（数字签名/哈希消息认证码）](cissp/ch07/03-digital-signatures-hmac.md)
- [04 PKI & Certificates（X.509/CA/RA/CRL/OCSP）](cissp/ch07/04-pki-certificates.md)
- [05 Cryptographic Attacks（暴力/旁路/生日/重放等）](cissp/ch07/05-cryptographic-attacks.md)
- [06 Applied Crypto & Key Management（PGP/S-MIME/TLS/HSM）](cissp/ch07/06-applied-crypto-key-mgmt.md)

### Domain 3 · Ch8 Principles of Security Models, Design, and Capabilities（加厚版）
- [01 Secure Design Foundations（主体/客体/传递信任/开放封闭）](cissp/ch08/01-secure-design-foundations.md)
- [02 Eleven Secure Design Principles（11 条安全设计原则）](cissp/ch08/02-eleven-secure-design-principles.md)
- [03 Techniques for Ensuring CIA（限制/边界/隔离）](cissp/ch08/03-techniques-for-ensuring-cia.md)
- [04 Security Models（TCB/BLP/Biba/Clark-Wilson/Brewer-Nash）](cissp/ch08/04-security-models.md)
- [05 Common Criteria & ATO（EAL1–7/PP/ST/ATO）](cissp/ch08/05-common-criteria-and-ato.md)
- [06 Security Capabilities of Information Systems（TPM/HSM/容错/生命周期）](cissp/ch08/06-security-capabilities.md)

### Domain 3 · Ch9 Security Vulnerabilities, Threats, and Countermeasures（加厚版）
- [01 Shared Responsibility & Data Sovereignty（共同责任/数据本地化主权）](cissp/ch09/01-shared-responsibility-data-sovereignty.md)
- [02 Computer Architecture Hardware（CPU/保护环/进程状态）](cissp/ch09/02-computer-architecture-hardware.md)
- [03 Memory, Storage, Emanations & Firmware（内存/辐射/TEMPEST/固件）](cissp/ch09/03-memory-storage-emanations-firmware.md)
- [04 System Architecture Types（客户端/服务器/分布式/ICS/RTOS）](cissp/ch09/04-system-architecture-types.md)
- [05 IoT, Edge, Embedded & CPS（物联网/嵌入式/信息物理系统）](cissp/ch09/05-iot-edge-embedded-cps.md)
- [06 Microservices, IaC & Immutable Architecture（微服务/IaC/不可变架构）](cissp/ch09/06-microservices-iac-immutable.md)
- [07 Virtualization & Containers（虚拟化/容器/VM 逃逸）](cissp/ch09/07-virtualization-containers.md)
- [08 Mobile Devices（移动设备安全/MDM/FDE/远程擦除）](cissp/ch09/08-mobile-devices.md)
- [09 Protection Mechanisms & Architecture Flaws（进程隔离/隐蔽信道/rootkit）](cissp/ch09/09-protection-mechanisms-flaws.md)

> **Domain 3 进度**：Ch6–Ch10 共 **33 篇**加厚短文已落地；Ch8（安全模型与设计）、Ch9（漏洞/威胁/对策）、Ch10（物理安全）已补全，**Domain 3（安全架构与工程）全 5 章走完**。下一批进入 **Domain 4（通信与网络安全）**，自 **Ch11（安全网络架构与组件）** 起。

### Domain 3 · Ch10 Implementing Physical Security（加厚版）
- [01 Secure Facility Plan, Site Selection & CPTED（设施规划/选址/CPTED）](cissp/ch10/01-secure-facility-plan-site-design-cpted.md)
- [02 Physical Controls, Order of Operations & Equipment Failure（控制分类/动作顺序/MTTF·MTTR·MTBF）](cissp/ch10/02-physical-controls-order-operations-equipment.md)
- [03 Wiring Closets, Server Rooms & SCIF（布线间/机房/敏感隔离信息设施）](cissp/ch10/03-wiring-closets-server-rooms-scif.md)
- [04 Access Controls: Badges, Smartcards & Proximity（工牌/智能卡/近程设备/访问滥用）](cissp/ch10/04-access-controls-badges-proximity.md)
- [05 Intrusion Detection, Alarms & Cameras（入侵检测/警报/摄像头）](cissp/ch10/05-intrusion-detection-alarms-cameras.md)
- [06 Media, Evidence Storage & Work Area Security（介质/证据/工作区安全）](cissp/ch10/06-media-evidence-workarea-security.md)
- [07 Utilities & Fire Suppression（供电/噪声/温湿/水患/火灾抑制）](cissp/ch10/07-utilities-fire-suppression.md)
- [08 Perimeter Security: Fencing, Lighting & More（周界/围栏/转闸/人阱/照明）](cissp/ch10/08-perimeter-security-fencing-lighting.md)

> **Domain 3 收官**：Ch6–Ch10 共 **33 篇**。注：Ch10 在 Sybex 中属 Domain 3（安全架构与工程），虽名为"物理安全"，但考纲将其归入该域。

### Domain 4 · Ch11 Secure Network Architecture and Components（加厚版）
- [01 OSI & TCP/IP Models（OSI 七层 / TCP-IP 模型 / 封装）](cissp/ch11/01-osi-tcpip-models.md)
- [02 Transport Layer & DNS（TCP/UDP / 域名系统 / 资源记录）](cissp/ch11/02-transport-dns.md)
- [03 IP Networking, ARP & ICMP（IPv4 分类 / CIDR / ARP 投毒 / ICMP）](cissp/ch11/03-ip-arp-icmp.md)
- [04 Multilayer & Converged Protocols（多层封装 / 隐蔽通道 / SAN·iSCSI·VoIP·SDN）](cissp/ch11/04-multilayer-converged-protocols.md)
- [05 Secure Network Components（Intranet/Extranet/DMZ / 设备分层 / 东西向·南北向）](cissp/ch11/05-secure-network-components.md)
- [06 Segmentation & Micro-segmentation（物理/逻辑分段 / VRF / VPC / VXLAN / 零信任）](cissp/ch11/06-segmentation-microsegmentation.md)
- [07 Application Layer Protocols & Traffic Analysis（端口表 / sniffer / 混杂模式）](cissp/ch11/07-app-layer-protocols-traffic-analysis.md)
- [08 Wireless Basics & Encryption（802.11 演进 / WEP·WPA·WPA2·WPA3 / SAE / WPS）](cissp/ch11/08-wireless-basics-encryption.md)
- [09 Wireless Attacks & Defense（rogue AP / evil twin / 解除关联 / 干扰 / 蓝牙六害）](cissp/ch11/09-wireless-attacks-defense.md)
- [10 Satellite, Cellular, Edge, CDN & Secure Protocols（卫星/4G·5G / 边缘 / CDN / IPSec·SSH）](cissp/ch11/10-satellite-cellular-edge-cdn-secure-proto.md)

> **Domain 4 进度**：Ch11 共 **10 篇**加厚短文已落地，开启 Domain 4（通信与网络安全）。下一批继续 **Ch12（安全网络组件与通信信道）** → Ch13（网络攻击与防御），走完 Domain 4。

### Domain 4 · Ch12 Secure Communications / Network Components（加厚版）
- [01 VPN & Secure Tunneling（VPN/隧道/IPSec 模式）](cissp/ch12/01-vpn-secure-tunneling.md)
- [02 TLS / SSL & HTTPS（握手/版本/ cert pinning）](cissp/ch12/02-tls-ssl-https.md)
- [03 IPSec & SSH（AH/ESP/传输·隧道/SSH 安全）](cissp/ch12/03-ipsec-ssh.md)
- [04 VLAN & Network Segmentation（VLAN/Trunk/隔离）](cissp/ch12/04-vlan-segmentation.md)
- [05 NAC & 802.1X（网络访问控制/端口安全）](cissp/ch12/05-nac-8021x.md)
- [06 Secure Network Design Principles（纵深/零信任/收敛）](cissp/ch12/06-secure-network-design.md)
- [07 Network Management & Monitoring（SNMP/NetFlow/遥测）](cissp/ch12/07-network-management-monitoring.md)
- [08 Secure Communications Summary（信道安全汇总）](cissp/ch12/08-secure-communications-summary.md)
- [09 Communications Security Controls（信道安全控制）](cissp/ch12/09-communications-security-controls.md)

### Domain 4 · Ch13 Security Network Management（加厚版）
- [01 Network Monitoring & Logging（监控/日志/SNMP）](cissp/ch13/01-network-monitoring-logging.md)
- [02 IDS / IPS Deep Dive（IDS·IPS/特征·行为）](cissp/ch13/02-ids-ips-deep-dive.md)
- [03 SIEM & Log Analytics（SIEM/关联/UEBA）](cissp/ch13/03-siem-log-analytics.md)
- [04 Network Access Control & Management（NAC 运维）](cissp/ch13/04-network-access-control-mgmt.md)
- [05 Traffic Analysis & Visibility（流量分析/包捕获）](cissp/ch13/05-traffic-analysis-visibility.md)
- [06 Network Defense Architecture（防御架构/分层）](cissp/ch13/06-network-defense-architecture.md)
- [07 Secure Network Operations（安全网络运维）](cissp/ch13/07-secure-network-operations.md)
- [08 Network Management Best Practices（管理最佳实践）](cissp/ch13/08-network-management-best-practices.md)

> **Domain 4 收官**：Ch11–Ch13 共 **27 篇**，Domain 4（通信与网络安全）全 3 章走完。下一批进入 **Domain 5（身份与访问管理）Ch14**。

### Domain 5 · Ch14 Controlling and Monitoring Access（加厚版）
- [01 Identity & Access Management Concepts（IAM 核心/身份治理）](cissp/ch14/01-iam-concepts.md)
- [02 Authentication Factors（认证因素/ MFA）](cissp/ch14/02-authentication-factors.md)
- [03 SSO & Federation（单点登录/联合身份）](cissp/ch14/03-sso-federation.md)
- [04 Authorization Models（授权模型/RBAC/ABAC/MAC）](cissp/ch14/04-authorization-models.md)
- [05 Privilege Management（权限管理/最小权限/提权防护）](cissp/ch14/05-privilege-management.md)
- [06 Account Management（账户生命周期/Provisioning）](cissp/ch14/06-account-management.md)
- [07 Access Control Threats（访问控制威胁/rootkit/后门）](cissp/ch14/07-access-control-threats.md)
- [08 Monitoring & Auditing Access（访问监控与审计）](cissp/ch14/08-monitoring-auditing-access.md)

> **Domain 5 进度**：Ch14 共 **8 篇**，Domain 5（身份与访问管理，权重 ~13%）一轮走完。下一批进入 **Domain 6（安全评估与测试）Ch15**。

### Domain 6 · Ch15 Security Assessment and Testing（加厚版）
- [01 Security Assessment, Testing & Audit（评估/测试/审计·NIST800-53A·SOC）](cissp/ch15/01-security-assessment-testing-program.md)
- [02 Vulnerability Assessments & Scanning（SCAP·Nmap·误报）](cissp/ch15/02-vulnerability-assessments-scanning.md)
- [03 Penetration Testing（渗透测试·白/灰/黑盒·BAS）](cissp/ch15/03-penetration-testing-bas.md)
- [04 Software Testing（SAST·DAST·Fuzz·IAST/RASP）](cissp/ch15/04-software-testing.md)
- [05 Training & Exercises（红蓝紫队·CTF·桌面演练·KPI/KRI）](cissp/ch15/05-training-exercises-mgmt-processes.md)

> **Domain 6 进度**：Ch15 共 **5 篇**，Domain 6（安全评估与测试，权重 ~12%）一轮走完。下一批进入 **Domain 7（安全运营）Ch16–Ch18**。

### Domain 7 · Ch16 Foundational Security Operations（加厚版）
- [01 Foundational Ops Concepts（应尽/应担责·SoD·两人控制）](cissp/ch16/01-foundational-ops-concepts.md)
- [02 Personnel Safety & Security（人员安全/胁迫/2FA疲劳）](cissp/ch16/02-personnel-safety-security.md)
- [03 Asset Management & Resource Protection（资产/媒体/SSD）](cissp/ch16/03-asset-management-resource-protection.md)
- [04 Cloud & Managed Services（共享责任/云部署/XaaS）](cissp/ch16/04-cloud-managed-services.md)
- [05 Configuration & Change Management（配置/变更/CAB）](cissp/ch16/05-configuration-change-management.md)
- [06 Patch & Vulnerability Management（补丁五步/残留风险）](cissp/ch16/06-patch-vulnerability-management.md)

### Domain 7 · Ch17 Incident Response / Detection & Prevention（加厚版）
- [01 Incident Management Lifecycle（事件七步/NIST800-61）](cissp/ch17/01-incident-management-lifecycle.md)
- [02 Preventive vs Detective Controls（预防vs检测）](cissp/ch17/02-preventive-detective-controls-overview.md)
- [03 DoS, Botnet & MITM Attacks（DoS/僵尸/中间人）](cissp/ch17/03-dos-botnet-mitm-attacks.md)
- [04 IDS, IPS, Honeypots & Firewalls（检测/防御/蜜罐/防火墙）](cissp/ch17/04-ids-ips-honeypots-firewalls.md)
- [05 Logging & Monitoring（六类日志/SIEM/NTP）](cissp/ch17/05-logging-monitoring.md)
- [06 Automated IR, SOAR & Kill Chain（SOAR/AI/KillChain/ATT&CK）](cissp/ch17/06-automated-ir-soar-ai-killchain.md)

### Domain 7 · Ch18 Disaster Recovery / BCP（加厚版）
- [01 Nature of Disaster（灾害本质/BCP/DRP/BCM）](cissp/ch18/01-nature-of-disaster.md)
- [02 Resilience, HA & Fault Tolerance（弹性/HA/RAID）](cissp/ch18/02-resilience-ha-fault-tolerance.md)
- [03 Recovery Strategy & Sites（恢复策略/冷热站/云站）](cissp/ch18/03-recovery-strategy-sites.md)
- [04 Recovery Plan & Backups（DRP/全增量差备份/escrow）](cissp/ch18/04-recovery-plan-development-backups.md)
- [05 Testing & Maintenance（六类演练/维护）](cissp/ch18/05-testing-maintenance.md)
- [06 Training & Documentation（培训四层/文档）](cissp/ch18/06-training-documentation.md)

> **Domain 7 收官**：Ch16–Ch18 共 **18 篇**，Domain 7（安全运营，权重 ~16%）全 3 章走完。下一批进入 **Domain 8（软件开发安全）Ch19–Ch21**，即全书最后一域。

### Domain 8 · Ch19 Investigations, Forensics & Ethics（加厚版）
- [01 Investigations, Forensics & Evidence（调查类型/证据四类型/最佳证据规则/IOCE/Locard）](cissp/ch19/01-investigations-forensics-evidence.md)
- [02 Major Categories of Computer Crime（计算机犯罪七类/APT/内部人）](cissp/ch19/02-major-categories-of-computer-crime.md)
- [03 Ethics & Codes of Conduct（(ISC)² 四准则/RFC1087/十诫）](cissp/ch19/03-ethics.md)

### Domain 8 · Ch20 Systems Development Controls / Databases（加厚版）
- [01 SDLC Models & Maturity（瀑布/螺旋/敏捷/CMM/IDEAL/SAMM）](cissp/ch20/01-sdlc-models-maturity.md)
- [02 Databases & Data Warehousing Security（RDBMS/ACID/聚合/推理/多实例化）](cissp/ch20/02-databases-warehousing.md)
- [03 AI Knowledge Systems & Storage Threats（专家系统/ML/NN/隐蔽存储通道）](cissp/ch20/03-ai-knowledge-systems-storage-threats.md)

### Domain 8 · Ch21 Malicious Code and Application Attacks（加厚版）
- [01 Malware Types（病毒/蠕虫/木马/勒索/零日/Stuxnet）](cissp/ch21/01-malware-types.md)
- [02 Malware Prevention & EDR（签名/启发式/EDR/UEBA）](cissp/ch21/02-malware-prevention-edr.md)
- [03 Application Attacks（缓冲区溢出/TOC/后门/提权）](cissp/ch21/03-application-attacks.md)
- [04 Injection Vulnerabilities（SQL/LDAP/命令/盲注）](cissp/ch21/04-injection-vulnerabilities.md)
- [05 Web App Attacks（XSS/CSRF/SSRF/会话劫持）](cissp/ch21/05-web-app-attacks-xss-csrf.md)
- [06 Application Security Controls（输入校验/WAF/参数化查询）](cissp/ch21/06-app-security-controls.md)
- [07 Secure Coding Practices（注释/错误处理/硬编码/内存）](cissp/ch21/07-secure-coding-practices.md)

> **Domain 8 收官 & 全书完成**：Ch19–Ch21 共 **13 篇**，Domain 8（软件开发安全，权重 ~10%）全 3 章走完。**至此全书 8 域 21 章全部覆盖，累计 135 篇加厚短文。** 配套全局思维导图见 `mind-map.html`，打卡清单见 `checklist.md`。

---

*本库由「学习规划师」工作流生成：先 grilling 锁定方案 → 抽取原书小节原文 → 按模板产出通俗短文 → 配滚动周计划。*

---
