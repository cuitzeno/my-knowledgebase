# 07 · 应用层协议与流量分析（Ch11 · Domain 4）

> 应用层协议是你每天用的 HTTP/FTP/邮件；流量分析（协议分析器/嗅探器）则是网管和安全人员的「听诊器」——但也可能被攻击者用来偷听。

## ① 一句话秒懂
应用层协议是「说话的内容格式」（网页用 HTTP、传文件用 FTP）；流量分析器是把网线里的「电波」录下来逐帧翻译的录音笔。

## ② 生活类比
- **应用层协议**：像不同业务的话术规范（点餐说 HTTP、寄件说 FTP）。
- **协议分析器（sniffer）**：像在电话线上并联的录音机，把经过的每句话（帧）都录下来拆开看。

## ③ 核心概念（大白话 + 原书定义）

**常见应用层协议与端口（考试高频表）**：
| 协议 | 端口 | 说明 / 安全建议 |
|------|------|----------------|
| Telnet | TCP 23 | 明文终端，**禁用**，用 SSH 替代 |
| FTP | 20/21 | 明文传文件，**禁用**，用 SFTP/FTPS |
| TFTP | UDP 69 | 无认证，存设备配置，**不应使用** |
| SMTP | TCP 25 | 发邮件，须 TLS→SMTPS（587/465） |
| POP3 | TCP 110 | 拉邮件（客户端归档），TLS→POPS 995 |
| IMAP4 | TCP 143 | 拉邮件（服务端归档），TLS→IMAPS 993 |
| DHCP | UDP 67/68 | 启动分配 IP |
| HTTP | TCP 80 | 明文网页 |
| HTTPS | TCP 443 | TLS 加密 HTTP |
| LPD | TCP 515 | 打印队列，建议 VPN 封装 |
| X Window | TCP 6000–6063 | GUI API，建议 VPN 封装 |

**协议分析器（Protocol Analyzer / Sniffer）**：
- 把 NIC 置为**混杂模式（promiscuous mode）**，忽略目的 MAC、抓取本网段所有帧。
- 能逐帧解析到二进制，payload 常以十六进制+ASCII 显示。
- 有**捕获过滤器（capture filter）**（决定存哪些帧）和**显示过滤器（display filter）**（决定显示哪些）。
- 开源：Wireshark；商业：Omnipeek、NetWitness、NetScout。
- 原书区分：sniffer 主要是抓包工具，protocol analyzer 还能解码解释内容。

> 注意：TCP/IP 栈漏洞多（缓冲区溢出、SYN flood、分片/超大包攻击、欺骗、AitM、劫持），且易遭被动监听（sniffing/eavesdropping）——流量分析工具本身是双刃剑。

## ④ 真实案例
某运维用 Telnet 管理核心交换机，攻击者在内网部署 sniffer 抓包，直接读到明文口令并接管设备。整改：全面禁用 Telnet/FTP，改用 SSH/SFTP，并在敏感网段部署 NIDS 监控异常抓包行为。

## ⑤ 考试怎么考
- 协议-端口-明文风险配对（Telnet 23 明文、FTP 20/21 明文、SMTP 25 等）。
- 哪些协议应禁用/须加密（Telnet、FTP、TFTP 禁用；SMTP/POP/IMAP 用 TLS）。
- 混杂模式、capture vs display filter 区别。
- Sniffer 与安全审计/攻击的双面性。

## ⑥ 记忆口诀
> **「Telnet FTP 明文危，SSH SFTP 替；邮件三兄弟 25/110/143，加 TLS 才安心」**
> **「抓包进混杂，存用捕获滤、看用显示滤」**

## ⑦ 自测
1. 为什么 Telnet 应该被禁用？（答：明文传输，口令可被嗅探）
2. 协议分析器的 capture filter 和 display filter 有什么不同？（答：前者决定哪些帧存入文件，后者决定从已存文件中显示哪些）
3. IMAP4 用 TLS 加密后端口变多少？（答：993，即 IMAPS）
