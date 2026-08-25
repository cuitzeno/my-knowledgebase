# 09 · 无线攻击与防御（Ch11 · Domain 4）

> 无线网天生比有线更脆弱：信号外溢、认证由基站说了算。这一篇盘点主流无线攻击（rogue AP、evil twin、解除关联、干扰、IV 滥用）与对应防御。

## ① 一句话秒懂
攻击者要么自己摆个假基站钓鱼（evil twin/rogue AP），要么把你「踢下线」再冒名顶替（disassociation），要么直接「吵死你」让网不可用（jamming）。

## ② 生活类比
- **War driving**：开车拿探测器满街找无线信号，像当年 war dialing 自动拨号找猫。
- **Rogue AP**：有人偷偷在你家装了个没锁的 Wi-Fi 路由器，成了后门。
- **Evil twin**：攻击者克隆你常连 Wi-Fi 的房名和房号，你手机自动连过去，他全程偷听。
- **Disassociation**：攻击者伪造「物业通知」把你从真基站踢掉，再顶替。

## ③ 核心概念（大白话 + 原书定义）

**War driving / 无线扫描**：用检测工具找无线信号（手持、手机、笔记本、甚至无人机 war flying）。任何没关在法拉第笼里的活跃无线网都可被探测，即便关了 SSID 广播。

**Rogue Access Point（流氓/非法 AP）**：
- 员工为方便私装、物理入侵者内装、或攻击者外设。
- 防御：WIDS 监控新出现的、尤其克隆 SSID/MAC 的 AP；用定向天线三角定位后查处。
- 客户端最佳做法：无线链路上连 VPN，且 VPN 成功才用无线。

**Evil Twin（邪恶双胞胎）**：
- 攻击系统监听客户端的重连请求（含原基站 MAC 与 SSID），用相同参数 spoof 身份提供明文连接，客户端因「认证加密由基站管、不由客户端强制」而接受，导致 AitM、会话劫持、窃密。
- 防御：留意连接到的网络是否异常（附近本不该有的网）、清理旧无线 profile、连 VPN。

**Disassociation / Deauthentication（解除关联/解除认证）**：
- 管理帧，用于换 WAP 时断开。恶意使用：伪造 WAP MAC 的 disassociation 发给客户端→客户端掉线并重发含明文 SSID 的 Reassociation Request；反复发致 DoS；配合 rogue AP 做 AitM 或会话劫持。
- 防御：WPA3（802.11w 管理帧保护）和/或 WIDS。

**Jamming（干扰/阻塞）**：发无线电降低信噪比阻断通信。排查：调设备位置、改频率/信道、三角定位来源，外部来源联系执法。

**IV（初始化向量）滥用**：IV 是随机数，过短/明文交换/选得差是弱点。例如用 Aircrack-ng 的 wesside-ng 破解 WEP 的 IV。

**蓝牙（Bluetooth，802.15.1，2.4 GHz，默认明文，配对码常 0000/1234）攻击族**：
- Bluesniffing（抓包）、Bluesmacking（DoS/干扰）、Bluejacking（发未请求消息）、BLUFFS（破前后向保密）、Bluesnarfing（未授权读数据）、Bluebugging（远程控制，如开麦克风当窃听器）。
- 防御：少用蓝牙、不用时彻底关闭。
- **BLE/Zigbee**：低功耗，Zigbee 用 128 位对称加密；iBeacon 基于 BLE 定位。

**RFID / NFC**：
- RFID：磁场景供电读取，可达数百米，隐私隐患（被动 RFID 可被远处读码关联到人）。
- NFC：近场（≤4cm），由 RFID 派生，支持挑战-应答甚至 PKI；非接触支付常用。攻击含 AitM、窃听、篡改、重放。最佳实践：不用时关 NFC。

**通用无线安全流程**（见上一篇 15 步）已涵盖部署期防御；运行期靠 WIDS/WIPS 持续监测。

## ④ 真实案例
员工在办公区私接一台家用无线路由器（rogue AP，默认弱密码），攻击者在大楼外war driving 发现该弱信号 AP 连入内网，横向移动窃取客户数据。事件后部署 WIDS，定期无线扫描+三角定位，并将「禁止私接 AP」写入安全策略。

## ⑤ 考试怎么考
- Rogue AP vs Evil twin 区别（前者冒充吸引新客/克隆诱老客，后者监听重连请求克隆身份）。
- Disassociation/Deauthentication 的管理帧滥用与 WPA3/802.11w 防护。
- 蓝牙六大攻击英文名与含义（尤其 bluesnarfing/bluebugging）。
- War driving 原理、关 SSID 仍可被探测。
- RFID/NFC 距离与隐私风险。

## ⑥ 记忆口诀
> **「流氓 AP 私装的门，邪恶双胞克隆人；解除关联踢下线，干扰阻塞吵死人」**
> **「蓝牙六害：sniff 抓、smack 阻、jack 扰、BLUFF 破密、snarf 偷读、bug 遥控」**
> **「WPA3+WIDS，无线两护盾」**

## ⑦ 自测
1. Evil twin 攻击能成功的关键原因是什么？（答：认证与加密由基站管理、非客户端强制，客户端接受基站提供的任何连接包括明文）
2. 蓝牙中能远程控制设备（如开麦克风窃听）的攻击叫什么？（答：Bluebugging）
3. 防御 disassociation 帧攻击的主要手段？（答：使用 WPA3/802.11w 管理帧保护，并部署 WIDS）
