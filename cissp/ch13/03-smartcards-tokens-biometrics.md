# 03 · 智能卡、令牌与生物识别

## 一句话秒懂
"你有的"靠智能卡和动态令牌（OTP）；"你是的"靠生物特征。生物识别看两个错误率：**认错人（FAR）**和**误拒自己人（FRR）**，交汇点 CER 用来比精度。

> 对应原书：Chapter 13 — "Something You Have" / "Something You Are" / "Biometric Factor Error Ratings"

## 生活类比
- 智能卡 = 带芯片的门禁卡，插卡+输 PIN 才开门（卡是你有的，PIN 是你知的 → MFA）。
- 令牌 = 每 60 秒变一次的 6 位码，像随时走动的保险箱密码。
- 生物识别 = 用身体当钥匙，但机器太敏感会误拒你（FRR），太松会放错人（FAR）。

## 核心概念（大白话 + 原书定义）

**智能卡（Smartcard）**：信用卡大小、嵌芯片，含微处理器与证书，用于非对称加密/数字签名（见 Ch7）。防篡改、便携。用户插入读卡器**通常还要输 PIN/密码**作第二因素。注意：卡可共享/互换，单独不能有效标识，故多需配合其他因素。

**令牌/认证器（Authenticator/Token）**：生成 OTP（6–8 位）的设备或 App（如 RSA 硬件、Google Authenticator）。常与密码组合成 MFA。两种 OTP：
- **TOTP（基于时间）**：与服务器时钟同步，每约 60 秒换新 → 又称**同步认证器（synchronous）**。
- **HOTP（基于哈希/计数器）**：按算法+递增计数器生成，按键才变、用完前不变 → 又称**异步认证器（asynchronous）**。
- 缺点：电池耗尽/损坏/丢失则无法登录。

**生物识别（Biometric，Type 3）**：可作标识、认证或两者，但**不提供授权或问责**。作为标识需"一对多"搜索数据库；作为认证需"一对一"比对声称身份。生理特征：指纹（看 minutiae 细节/分叉）、脸（几何模式）、视网膜（眼底血管，最准确、能区分同卵双胞胎，但近 3 英寸且暴露健康）、虹膜（第二准，20–40 英尺远，可被高清图骗）、掌静脉（近红外测血管）、声纹（voiceprint，常作辅助）。注意**语音识别（speech recognition）≠ 声纹识别（voice pattern）**：前者辨词、后者辨人。

**错误率**：
- **FRR（False Rejection Rate，拒真/Type I）**：合法用户被拒。
- **FAR（False Acceptance Rate，纳伪/Type II）**：冒充者被接受。
- **CER/ERR（交叉错误率/等错误率）**：FRR=FAR 时的点，用作**比较不同设备精度的标准值**——CER 越低越准。
- 敏感度调节：太敏感→FRR 多；不够敏感→FAR 多。安全区（如金库）会把敏感度调很高宁可多拒（FRR 可接受，FAR 不可接受）。

**注册要素**：enrollment time（>2 分钟通常不可接受）、throughput rate（约 ≤6 秒可接受）、acceptance（用户接受度）。

> 口诀：**"卡+PIN 是 MFA，TOTP 同步、HOTP 异步；FAR 纳伪、FRR 拒真，CER 低者更精准。"**

## 真实案例
数据中心门禁用虹膜识别，为防冒充把敏感度调高，偶尔误拒员工（需保安复核），但从不放错人。另：某系统用 SMS 发 OTP 做 2FA，被 SIM 交换诈骗拦截，升级为 Authenticator App（TOTP）。

## 考试怎么考
- 智能卡特点 + 为何需配合 PIN（可共享）。
- TOTP vs HOTP（同步/异步、时钟 vs 计数器）。
- FAR / FRR / CER 定义与关系；CER 越低越好。
- 安全场景偏向高敏感度（宁可 FRR）。
- 语音识别 vs 声纹识别区别。

## 记忆口诀
> **"智能卡配 PIN，令牌走 OTP；FAR 错放人、FRR 错拒人，CER 交汇比精度。"**

## 自测
1. 为什么智能卡单独使用不是有效的标识手段？
2. TOTP 与 HOTP 的根本区别？各称什么认证器？
3. FAR 与 FRR 分别是什么错误？CER 怎么用？
4. 金库门禁为何把生物识别敏感度调很高？
5. 语音识别（speech recognition）与声纹识别（voice pattern recognition）有何不同？
