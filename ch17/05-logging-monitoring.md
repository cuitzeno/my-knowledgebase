# ① 一句话秒懂

日志与监控（Logging & Monitoring）是"让一切行为可追溯、可问责"的基础：日志记录谁在何时做了什么，监控+审计 trail 让内鬼无处隐藏、让事故可重建、让起诉有证据。SIEM 把全网信源汇总智能分析。

# ② 生活类比

- **日志（Log）** = 银行的每一笔交易凭条：谁、何时、取了多少。
- **审计 Trail** = 把凭条按时间串起来，能正向/反向还原整件事。
- **SIEM** = 总行监控中心，把各分行凭条实时汇总，发现异常（同人短时间内多地取钱）立刻报警。
- **Clipping Level** = 设阈值，输错两次密码不报警，连错 5 次才响——避免被正常手滑淹没。

# ③ 核心概念

## 常见日志类型
- **Security Logs**：访问文件/文件夹/打印机等（如谁在何时访问了机密表）。需安全认证作前提才能问责。
- **System Logs**：系统启停、服务启停/属性变更。攻击者停监控服务或改属性（Disabled→Manual）会留下痕迹。
- **Application Logs**：应用开发者自定义记录。
- **Firewall Logs**：记录放行/阻断流量（源目的 IP、端口，不含包内容）。
- **Proxy Logs**：用户访问了哪些网站、时长、尝试访问禁站。
- **Change Logs**：变更请求/批准/实际修改，属变更管理，DR 时用来复原到最后已知状态。

## 保护日志数据
- 攻击者会改/删日志抹痕迹（APT 标准操作），故须保护。
- 集中存到 **SIEM** 留副本；设只读、权限控制、物理安全；严格备份与**保留期（retention）**政策（政府可能要求无限期）。
- 保留过久反成负担：法规要求 1 年却留 10 年，法院令一出得翻 10 年日志。
- **FIPS 200** 规定审计数据最低要求：创建/保护/保留审计记录；个体行为可唯一追溯问责。

## 监控的作用
- **Audit Trails（审计 Trail）**：被动检测控制，威慑（如 CCTV/保安），可正/反向追踪，是起诉关键证据。
- **Accountability（问责）**：身份+认证+审计 trail 三位一体。立法要求：SOX、HIPAA、GDPR。
- **Investigations**：重建事件前后状态。
- **Problem Identification**：记录系统故障/OS bug/崩溃转储，区分攻击与硬件故障。
- **Tuning（调优）**：持续调整控制降误报；太敏感→管理员不信/忽略，太不敏感→漏入侵。

## NTP 时间同步（关键）
- 日志须**准确一致时间戳**。建内部 **NTP 服务器** 同步可信时间源（如 NIST 认证时间服务器），其他系统再同步内部 NTP。

## SIEM / SEM / SIM
- 集中式日志 + 实时分析。含远程 **agents** 监控"alarm triggers"并上报中央。
- **关联与聚合（correlation & aggregation）** 引擎把异构数据转有用信息，高级分析 raise alerts / 触发响应。
- 还能做资产清点（系统名、IP、OS、补丁、软件），识别缺补丁/未授权软件。
- 含 ML/AI 技术辅助检索。

## Syslog
- RFC 5424 定义 syslog 协议发事件通知，集中 syslog 服务器接收。Unix/Linux 用 syslogd；扩展 syslog-ng/Rsyslog 可接受任何源。

## Sampling（抽样）与 Clipping Levels
- **Statistical Sampling（统计抽样）**：数学函数提取，有误差边际，更可靠可辩护。
- **Clipping Level（裁剪阈值）**：非统计抽样，只处理超阈值的事件。如 30 分钟内 5 次失败登录才报警；账户锁定的阈值同理。建立常规活动基线，超基线才响。

## 其他监控工具
- **Keystroke Monitoring（按键监控/keylogger）**：记录键盘输入，多用于恶意，企业用须**告知员工**（类比窃听）。
- **Traffic/Trend Analysis（流量/趋势分析）**：看包流向而非内容（network flow），可发现 botnet 外发巨量邮件、内鬼泄密。

## Log Management（日志管理）
- SIEM 收集聚合分析。转发后可删本地，但通常用 **rollover/circular logging（滚动日志）**：到上限覆盖最旧。Windows 可 archive 存新文件（小心塞满盘）；或 PowerShell 脚本定期归档到备份服务器。

## Egress Monitoring（出口监控）
- 监控**出网流量**防 **data exfiltration（数据外泄）**。
- **DLP（数据防泄漏）**：检测/阻断敏感数据外传、识别水印。对加密外泄数据无法看内容，但可监控**加密流量体积异常**。
- **Steganography（隐写术）检测**：对比原文件与可疑文件 **SHA-3 哈希**，不同 = 被改过可能藏密；数字水印（watermarking）可溯源泄密分发渠道。

# ④ 真实案例

某 QA 主管 Duane 每天经手高度敏感文件，他的每次操作都在工作站留下电子轨迹，主管 Nicole 可在质疑时审查"他从哪拿、放哪去、何时改"。这既保护公司（防 Duane 滥用），也保护 Duane（防被诬陷）。这就是**监控与问责**的双刃价值——前提是身份认证的Secure，否则会错怪人。

# ⑤ 考试怎么考

- **日志类型**对应内容（Security/System/Application/Firewall/Proxy/Change）。
- **NTP** 同步确保时间戳一致（日志分析前提）。
- **SIEM** 功能：集中、关联聚合、agents、实时告警、资产清点。
- **Clipping Level** 定义与举例（失败登录阈值）；统计 vs 非统计抽样。
- **Egress monitoring / DLP / 隐写检测（哈希比对）**。
- **密钥/按键监控须告知员工**。
- **FIPS 200** 审计记录最低要求。

# ⑥ 记忆口诀

> **"六类日志安系应防代变，集中 SIEM 留副本；NTP 同步时间戳，clipping 超阈才报警；出口监控防外泄，DLP 水印哈希照；按键监控须告知，FIPS200 留证责。"**

# ⑦ 自测

1. 列出常见的六类日志并简述各自记录什么。
2. 为什么日志需要 NTP 时间同步？如何部署？
3. SIEM 系统的主要能力有哪些（至少 4 点）？
4. 什么是 clipping level？它属于统计还是非统计抽样？
5. 出口监控（egress monitoring）如何帮助发现数据外泄？DLP 对加密外泄数据有什么局限？
6. 使用 keystroke monitoring 时组织应注意什么法律/伦理要求？
