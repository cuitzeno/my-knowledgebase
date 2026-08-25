---
title: CISSP 滚动周学习计划（第 1–4 周 · Domain 1 前 4 章）
parent: CISSP 认证安全工程师知识库
nav_order: 90
---

# CISSP 滚动周学习计划（第 1–4 周 · Domain 1 前 4 章）

> 前提（已共识）：无考试死线；每周投入 **6–8 小时**；目标稳过；当前有安全相关基础。
> 节奏：每周覆盖约 1–2 章的考点短文 + 当周自测 + 轻复习。全书约 21 章，一轮约 15–20 周。
> 用法：每周按「读短文 → 做自测 → 复盘错题 → 周末总览」四步推进。

---

## 第 1 周 — Ch1（上）：安全基础概念
**投入：6–8 小时**
- 读考点短文（建议每天 1–2 篇，每篇 15–20 分钟）：
  1. [Security 101](ch01/01-security-101.md)
  2. [Understand and Apply Security Concepts](ch01/02-security-concepts.md)（重点：CIA / DAD / AAA 五要素）
  3. [Security Boundaries](ch01/03-security-boundaries.md)
- 做每篇末尾自测，错题回到「⑤易错&陷阱」巩固。
- **周末总览**：用一句话向自己复述 CIA 三要素与 DAD 三连的对应关系。

## 第 2 周 — Ch1（下）：治理、管理、政策、威胁、供应链
**投入：6–8 小时**
- 读考点短文：
  4. [Evaluate and Apply Security Governance Principles](ch01/04-governance-principles.md)
  5. [Manage the Security Function](ch01/05-manage-security-function.md)
  6. [Security Policy, Standards, Procedures, and Guidelines](ch01/06-policy-standards.md)
  7. [Threat Modeling](ch01/07-threat-modeling.md)（重点：STRIDE）
  8. [Supply Chain Risk Management](ch01/08-supply-chain-rm.md)
- **周末总览**：画出「政策→标准→基线→指南→步骤」金字塔；默写 STRIDE。

## 第 3 周 — Ch2：人事安全与风险管理概念（已生成 7 篇）
**投入：6–8 小时**
- 读考点短文（每天 1–2 篇）：
  1. [Personnel Security Lifecycle](ch02/01-personnel-lifecycle.md)
  2. [Ongoing Oversight & Third-Party Controls](ch02/02-oversight-thirdparty.md)
  3. [Risk Core Concepts](ch02/03-risk-core-concepts.md)（重点：威胁/漏洞/暴露/资产估值）
  4. [Risk Assessment](ch02/04-risk-assessment.md)（重点：SLE/ARO/ALE 公式）
  5. [Risk Response](ch02/05-risk-response.md)（重点：缓解/转移/威慑/规避/接受）
  6. [Social Engineering](ch02/06-social-engineering.md)（重点：七大原则 / 钓鱼/短信钓鱼）
  7. [Security Awareness, Training & Education](ch02/07-awareness-training.md)
- **周末总览**：默写「风险应对五策略」+ 区分 Awareness/Training/Education 三者。

## 第 4 周 — Ch3–Ch4：业务连续性 & 法律法规（已生成 10 篇）
**投入：6–8 小时**
- Ch3（BCP）4 篇：[Planning & Scope](ch03/01-planning-scope.md) / [BIA](ch03/02-bia.md)（重点：RTO/RPO/MTD/MTBF/MTTR）/ [Continuity Planning](ch03/03-continuity-planning.md) / [Approval & Implementation](ch03/04-approval-implementation.md)。
- Ch4（法律）6 篇：[Legal System & Computer Crime](ch04/01-legal-system.md) / [Major US Cyber/Privacy Laws](ch04/02-major-laws.md) / [Intellectual Property](ch04/03-intellectual-property.md) / [Privacy Laws](ch04/04-privacy-laws.md) / [Software Licensing & Import/Export](ch04/05-software-licensing-import-export.md) / [State Privacy, PCI DSS & Vendor Governance](ch04/06-state-compliance-vendor.md)。
- **周末总览**：一页纸总结 BCP 与法律合规关键术语（中英文对照）；重点记 HIPAA/HITECH、版权 vs 商业秘密、ITAR vs EAR。

## 第 5 周 — Ch5：资产保护（Protecting Security of Assets）· Domain 1 收尾 ✅已生成
**投入：6–8 小时**
- 读已生成 5 篇：[Identifying & Classifying](ch05/01-identifying-classifying.md) / [Handling Requirements](ch05/02-handling-requirements.md)（重点：留存/净化/销毁、数据残留）/ [Data Protection Methods](ch05/03-data-protection-methods.md)（DRM/CASB/匿名化/令牌化）/ [Data Roles](ch05/04-data-roles.md) / [Security Baselines](ch05/05-security-baselines.md)（NIST SP 800-53B）。
- 做自测，错题进 `mistakes.md`。
- **周末总览**：Domain 1 全 5 章（Ch1–Ch5）核心术语复盘，准备进入 Domain 3（安全架构与工程）。

## 第 6 周 — Domain 1 综合复盘 & 模拟自测 ✅
**投入：6–8 小时**
- 重做 Ch1–Ch5 全部自测题，统计正确率；低于 80% 的篇目二刷。
- 思维导图连起 D1 知识网（治理→人事/风险→BCP→法律→资产）。
- **里程碑**：Domain 1（权重 16%）一轮走完。

## 第 7 周 — Ch6：密码学与对称密钥算法（Domain 3）✅已生成
**投入：6–8 小时**
- 读已生成 4 篇：[Goals & Foundations](ch06/01-crypto-goals-foundations.md)（CIA+不可否认/混淆扩散/XOR/密钥空间）/ [Symmetric vs Asymmetric](ch06/02-symmetric-vs-asymmetric.md) / [Symmetric Algorithms & Modes](ch06/03-symmetric-algorithms-modes.md)（DES/3DES/AES + ECB/CBC/CTR/GCM 等模式）/ [Crypto Lifecycle & Key Mgmt](ch06/04-crypto-lifecycle-key-mgmt.md)（M-of-N/一次一密）。
- 重点：AES 是标准（DES 弃用、3DES 2024 起禁）；分组模式各自防什么。

## 第 8 周 — Ch7：PKI 与密码应用（Domain 3）✅已生成
**投入：6–8 小时**
- 读已生成 6 篇：[Asymmetric Algorithms](ch07/01-asymmetric-algorithms.md)（RSA/DH/ECC/后量子）/ [Hash Functions](ch07/02-hash-functions.md) / [Digital Signatures & HMAC](ch07/03-digital-signatures-hmac.md) / [PKI & Certificates](ch07/04-pki-certificates.md)（X.509/CA/RA/CRL/OCSP）/ [Crypto Attacks](ch07/05-cryptographic-attacks.md) / [Applied Crypto & Key Mgmt](ch07/06-applied-crypto-key-mgmt.md)（TLS/HSM）。
- 重点：密钥长度等价（RSA 3072 ≈ ECC 256 ≈ 对称 128）；CRL vs OCSP。

## 第 9 周 — Ch8：安全模型、设计与能力（Domain 3）✅已生成
**投入：6–8 小时**
- 读已生成 6 篇：[Secure Design Foundations](ch08/01-secure-design-foundations.md)（主体/客体/传递信任）/ [Eleven Principles](ch08/02-eleven-secure-design-principles.md)（fail-open vs fail-closed、零信任、PbD、SASE）/ [Techniques for CIA](ch08/03-techniques-for-ensuring-cia.md)（限制/边界/隔离）/ [Security Models](ch08/04-security-models.md)（BLP/Biba/Clark-Wilson/Brewer-Nash）/ [Common Criteria & ATO](ch08/05-common-criteria-and-ato.md) / [Security Capabilities](ch08/06-security-capabilities.md)（TPM/HSM/容错）。
- 重点：BLP 保保密（no read-up/no write-down）、Biba 保完整（no read-down/no write-up）；simple=读、star=写。

## 第 10 周 — Ch9：漏洞、威胁与对策（Domain 3）✅已生成
**投入：6–8 小时**
- 读已生成 9 篇：[Shared Responsibility & Sovereignty](ch09/01-shared-responsibility-data-sovereignty.md) / [Architecture Hardware](ch09/02-computer-architecture-hardware.md)（保护环/进程状态）/ [Memory/Emanations/Firmware](ch09/03-memory-storage-emanations-firmware.md)（TEMPEST/secure boot）/ [System Types](ch09/04-system-architecture-types.md)（ICS/SCADA/RTOS）/ [IoT/Embedded/CPS](ch09/05-iot-edge-embedded-cps.md) / [Microservices/IaC](ch09/06-microservices-iac-immutable.md) / [Virtualization](ch09/07-virtualization-containers.md)（VM 逃逸）/ [Mobile](ch09/08-mobile-devices.md) / [Protection Mechanisms & Flaws](ch09/09-protection-mechanisms-flaws.md)（隐蔽信道/rootkit）。
- **里程碑**：Domain 3（Ch6–Ch9）一轮走完（25 篇）。下一批 **Ch10 物理安全** 收尾 Domain 3。

## 第 11 周 — Ch10：物理安全（Domain 3）✅已生成
**投入：6–8 小时**
- 读已生成 8 篇：[Facility Plan & CPTED](ch10/01-secure-facility-plan-site-design-cpted.md)（设施规划/选址/CPTED）/ [Controls & Order of Ops](ch10/02-physical-controls-order-operations-equipment.md)（三类控制/六步动作顺序/MTTF·MTTR·MTBF）/ [Wiring Closets & SCIF](ch10/03-wiring-closets-server-rooms-scif.md) / [Badges & Proximity](ch10/04-access-controls-badges-proximity.md)（智能卡/近程设备/尾随）/ [IDS & Cameras](ch10/05-intrusion-detection-alarms-cameras.md)（运动探测/警报三型/二次验证）/ [Media & Work Area](ch10/06-media-evidence-workarea-security.md)（介质/证据存储/清桌政策）/ [Utilities & Fire](ch10/07-utilities-fire-suppression.md)（UPS/供电术语/灭火器分级/水抑制四型/卤代烷淘汰）/ [Perimeter & Lighting](ch10/08-perimeter-security-fencing-lighting.md)（围栏三档/PIDAS/人阱/防撞柱/照明 2 烛光）。
- 重点：动作六步（deter→deny→detect→delay→determine→decide）；供电四级（浪涌→稳压→UPS→发电机）；水抑制四型中**预作用最适合人机共存**；卤代烷（halon）因破坏臭氧已淘汰。
- **里程碑**：**Domain 3（安全架构与工程）全 5 章（Ch6–Ch10）走完，共 33 篇**。下一批进入 **Domain 4（通信与网络安全）**。

## 第 12 周 — Ch11：安全网络架构与组件（Domain 4）✅已生成
**投入：6–8 小时**
- 读已生成 10 篇：[OSI & TCP/IP](ch11/01-osi-tcpip-models.md)（七层/四层/封装）/ [Transport & DNS](ch11/02-transport-dns.md)（TCP vs UDP、DNS 记录、端口）/ [IP/ARP/ICMP](ch11/03-ip-arp-icmp.md)（IPv4 分类、CIDR、ARP 投毒、ICMP DoS）/ [Multilayer & Converged](ch11/04-multilayer-converged-protocols.md)（隐蔽通道、SAN/iSCSI/VoIP/SDN）/ [Network Components](ch11/05-secure-network-components.md)（Intranet/Extranet/DMZ、设备分层、东西向·南北向）/ [Segmentation](ch11/06-segmentation-microsegmentation.md)（物理/逻辑分段、VXLAN、零信任）/ [App Protocols & Sniffer](ch11/07-app-layer-protocols-traffic-analysis.md)（端口表、混杂模式）/ [Wireless Basics](ch11/08-wireless-basics-encryption.md)（802.11 演进、WEP→WPA3、SAE、WPS）/ [Wireless Attacks](ch11/09-wireless-attacks-defense.md)（rogue AP/evil twin/解除关联/蓝牙六害）/ [Satellite/Cellular/CDN](ch11/10-satellite-cellular-edge-cdn-secure-proto.md)（卫星轨道、4G/5G、IPSec/SSH）。
- 重点：OSI 七层与设备分层；WPA3 用 SAE 替代 PSK；多层协议三大缺点（隐蔽通道/绕过滤/越界）；微隔离是零信任关键。
- **里程碑**：**Domain 4 启动，Ch11 走完（10 篇）**。下一批 **Ch12 安全通信信道** → Ch13 网络管理，走完 Domain 4。

## 第 13 周起 — Domain 4 后续（滚动补充）
- **Ch12** 安全通信信道（Secure Communications）：VPN/TLS/IPSec/SSH/VLAN/NAC/网络访问控制等
- **Ch13** 安全网络管理（Network Management）：监控、日志、IDS/IPS、SIEM
- 生成到哪章，哪章排入下一周；本文件随进度滚动补充。

## 第 13 周 — Ch12–Ch13：通信信道与网络管理（Domain 4 收官）✅已生成
**投入：6–8 小时**
- Ch12（9 篇）：[VPN/隧道](ch12/01-vpn-secure-tunneling.md) / [TLS/SSL](ch12/02-tls-ssl-https.md) / [IPSec/SSH](ch12/03-ipsec-ssh.md) / [VLAN/分段](ch12/04-vlan-segmentation.md) / [NAC/802.1X](ch12/05-nac-8021x.md) / [安全网络设计](ch12/06-secure-network-design.md) / [网络管理监控](ch12/07-network-management-monitoring.md) / [信道安全汇总](ch12/08-secure-communications-summary.md) / [信道安全控制](ch12/09-communications-security-controls.md)。
- Ch13（8 篇）：[监控日志](ch13/01-network-monitoring-logging.md) / [IDS/IPS](ch13/02-ids-ips-deep-dive.md) / [SIEM](ch13/03-siem-log-analytics.md) / [NAC 运维](ch13/04-network-access-control-mgmt.md) / [流量分析](ch13/05-traffic-analysis-visibility.md) / [防御架构](ch13/06-network-defense-architecture.md) / [安全运维](ch13/07-secure-network-operations.md) / [管理实践](ch13/08-network-management-best-practices.md)。
- **里程碑**：**Domain 4（通信与网络安全）全 3 章（Ch11–Ch13）走完，共 27 篇**。下一批进入 **Domain 5（身份与访问管理）**。

## 第 14 周 — Ch14：身份与访问管理（Domain 5）✅已生成
**投入：6–8 小时**
- 读已生成 8 篇：[IAM 概念](ch14/01-iam-concepts.md) / [认证因素/MFA](ch14/02-authentication-factors.md) / [SSO/联邦](ch14/03-sso-federation.md) / [授权模型 RBAC/ABAC/MAC](ch14/04-authorization-models.md) / [权限管理/提权防护](ch14/05-privilege-management.md) / [账户生命周期](ch14/06-account-management.md) / [访问控制威胁 rootkit/后门](ch14/07-access-control-threats.md) / [访问监控审计](ch14/08-monitoring-auditing-access.md)。
- 重点：认证三因素（所知/所有/所是）；RBAC vs ABAC vs MAC；MFA 抗钓鱼。
- **里程碑**：**Domain 5（权重 ~13%）一轮走完**。下一批 **Domain 6（安全评估与测试）Ch15**。

## 第 15 周 — Ch15：安全评估与测试（Domain 6）✅已生成
**投入：6–8 小时**
- 读已生成 5 篇：[评估/测试/审计](ch15/01-security-assessment-testing-program.md)（NIST800-53A 四对象·SOC1/2/3·COBIT）/ [漏洞扫描](ch15/02-vulnerability-assessments-scanning.md)（SCAP·Nmap·误报）/ [渗透测试](ch15/03-penetration-testing-bas.md)（白/灰/黑盒·BAS）/ [软件测试](ch15/04-software-testing.md)（SAST/DAST/Fuzz）/ [演练](ch15/05-training-exercises-mgmt-processes.md)（红蓝紫队·KPI/KRI）。
- 重点：NIST800-53A 四对象（specification/design/implementation/effectiveness）；SOC 2 Type II 最严；渗透测试四阶段（NIST800-115）。
- **里程碑**：**Domain 6（权重 ~12%）一轮走完**。下一批 **Domain 7（安全运营）Ch16–Ch18**。

## 第 16–18 周 — Ch16–Ch18：安全运营（Domain 7）✅已生成
**投入：每周围 6–8 小时**
- **第 16 周 Ch16（6 篇）**：[基础运营](ch16/01-foundational-ops-concepts.md)（应尽/应担责·SoD·两人控制·岗位轮换）/ [人员安全](ch16/02-personnel-safety-security.md) / [资产管理](ch16/03-asset-management-resource-protection.md)（数据拥有者/保管者·MTTF vs MTBF·SSD 不可消磁）/ [云与托管](ch16/04-cloud-managed-services.md)（共享责任·XaaS）/ [配置与变更](ch16/05-configuration-change-management.md)（CAB·回滚）/ [补丁管理](ch16/06-patch-vulnerability-management.md)（Patch Tuesday/Exploit Wednesday·残留风险）。
- **第 17 周 Ch17（6 篇）**：[事件生命周期](ch17/01-incident-management-lifecycle.md)（七步·NIST800-61·不反击）/ [预防vs检测](ch17/02-preventive-detective-controls-overview.md) / [DoS/僵尸/MITM](ch17/03-dos-botnet-mitm-attacks.md) / [IDS/IPS/蜜罐/防火墙](ch17/04-ids-ips-honeypots-firewalls.md) / [日志监控](ch17/05-logging-monitoring.md)（六类日志·SIEM·NTP）/ [SOAR/KillChain](ch17/06-automated-ir-soar-ai-killchain.md)（MITRE ATT&CK）。
- **第 18 周 Ch18（6 篇）**：[灾害本质](ch18/01-nature-of-disaster.md)（BCP/DRP/BCM）/ [弹性HA容错](ch18/02-resilience-ha-fault-tolerance.md)（RAID 0/1/5/6/10·UPS）/ [恢复策略站点](ch18/03-recovery-strategy-sites.md)（冷/温/热站·MAA）/ [备份](ch18/04-recovery-plan-development-backups.md)（全/增/差·归档位）/ [演练](ch18/05-testing-maintenance.md)（六类测试）/ [培训文档](ch18/06-training-documentation.md)。
- 重点：事件七步顺序（Detection→…→Lessons Learned）；RAID 各级容错；备份三型差异；演练六型（read-through→full-interruption）。
- **里程碑**：**Domain 7（权重 ~16%）全 3 章（Ch16–Ch18）走完，共 18 篇**。下一批 **Domain 8（软件开发安全）Ch19–Ch21，全书最后一域**。

## 第 19–20 周 — Ch19–Ch21：软件开发安全（Domain 8）✅已生成（全书收官）
**投入：每周围 6–8 小时**
- **第 19 周 Ch19（3 篇）**：[调查/取证/证据](ch19/01-investigations-forensics-evidence.md)（调查五类型·证据四类型·最佳证据规则·IOCE·Locard）/ [计算机犯罪七类](ch19/02-major-categories-of-computer-crime.md)（APT·内部人威胁）/ [职业道德](ch19/03-ethics.md)（(ISC)² 四准则·RFC1087）。
- **第 20 周 Ch20–Ch21（10 篇）**：
  - Ch20（3 篇）：[SDLC 与成熟度](ch20/01-sdlc-models-maturity.md)（瀑布/螺旋/敏捷·CMM/IDEAL/SAMM）/ [数据库安全](ch20/02-databases-warehousing.md)（RDBMS·ACID·聚合·推理·多实例化）/ [AI 与存储威胁](ch20/03-ai-knowledge-systems-storage-threats.md)（专家系统/ML/NN·隐蔽存储通道）。
  - Ch21（7 篇）：[恶意代码类型](ch21/01-malware-types.md)（病毒/蠕虫/木马/勒索/Stuxnet）/ [防护与EDR](ch21/02-malware-prevention-edr.md) / [应用攻击](ch21/03-application-attacks.md)（溢出/TOC/后门/提权）/ [注入漏洞](ch21/04-injection-vulnerabilities.md)（SQL/命令/盲注）/ [Web 攻击](ch21/05-web-app-attacks-xss-csrf.md)（XSS/CSRF/SSRF）/ [应用安全控制](ch21/06-app-security-controls.md)（输入校验/WAF/参数化查询）/ [安全编码](ch21/07-secure-coding-practices.md)（注释/错误处理/硬编码/内存）。
- 重点：(ISC)² 四准则必背（Canon I–IV）；聚合 vs 推理；SQL 注入与参数化查询；XSS vs CSRF 信任方向相反。
- **🏁 全书完成里程碑**：**Domain 8（权重 ~10%）全 3 章走完，CISSP 8 域 21 章全部覆盖，累计 135 篇加厚短文。** 配套全局思维导图 `mind-map.html` + 打卡清单 `checklist.md` 已生成。

## 第 21 周起 — 总复盘与模拟冲刺（建议）
- 重做各域自测，统计正确率；低于 80% 的篇目二刷。
- 用 `mind-map.html` 串起 8 域知识网，按域做横向对比（如各域"控制类型"对比）。
- 按 `checklist.md` 逐项打卡核销，错题入 `mistakes.md`。

---

## 完成标准（铁律）
- 每篇短文：能**不看原文**用自己的话讲出「秒懂 + 类比 + 口诀」。
- 每篇自测：正确率 ≥ 80%；错题进入「错题本」（建议在本目录建 `mistakes.md`）。
- 每周末：能默写当周核心口诀（CIA/DAD/AAA/STRIDE/金字塔）。

## 偏差处理
- 若某周只完成 < 60%：下一周**减半新内容、补旧内容**，并在本文件标注 ⚠️。
- 若连续两周落后：回调节奏为「每 1.5 周 1 章」，优先保 Ch1–Ch5（D1 占分最高）。

> 排期随生成进度滚动补充；生成到哪章，哪章排入下一周。
