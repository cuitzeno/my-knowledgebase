---
title: 03 数据保护方法（Data Protection Methods）
parent: 第 5 章
grand_parent: CISSP 认证安全工程师知识库
nav_order: 3
---

# 03 数据保护方法（Data Protection Methods）

> Domain 1 收尾篇 · 在加密之外，还有这些"去标识化"与"边界代理"手段

## 一句话秒懂
除了加密，保护数据还有 DRM（管版权）、CASB（管云）、以及把"能认出你是谁"的信息藏起来的三件套：假名化、令牌化、匿名化。

## 生活类比
- **DRM**＝给电子书加了"只能在你买的设备上看、不能转卖"的锁。
- **假名化/令牌化/匿名化**＝快递单上写"顾客 23456"而不是你的真名——收件人仍能收到，但泄露了也认不出你。

## 核心概念（大白话 + 原书定义）

### 1. 数字版权管理（DRM, Digital Rights Management）
保护**版权作品**（如电子书、音乐、软件）不被未授权使用/修改/分发。常见机制：
- **DRM License**：小文件，含使用条款+解密密钥。
- **Persistent Online Authentication（常连 DRM）**：必须联网定期认证，失败即锁。
- **Continuous Audit Trail**：持续记录使用，可发现异地并发滥用。
- **Automatic Expiration**：订阅到期自动失效（如租片 30 天）。
- 数字水印（steganography 藏入）/元数据可追踪买家、辅助维权。
- 注意：DRM 护**版权**，不护商标/专利/商业秘密。有人反对 DRM，认为它限制正当 Fair Use、只给合法用户添麻烦。

### 2. 云访问安全代理（CASB, Cloud Access Security Broker）
逻辑上位于**用户与云资源之间**的软件（可在本地或云内）。所有访问流经它，它据此：
- 强制策略（如"存云的数据必须加密"——CASB 校验到达/存储时是否已加密）；
- 做认证授权、记录日志、告警异常；
- 复制内部 DLP 等功能；
- **探测影子 IT（Shadow IT）**：员工未经 IT 批准私自用的云服务，CASB 通过防火墙/代理日志发现。

### 3. 去标识化三件套（GDPR 重点关注）
| 方法 | 原理 | 可否还原 | 典型场景 |
|---|---|---|---|
| **Pseudonymization（假名化）** | 用别名(pseudonym)代替真实数据，如"Patient 23456" | **可还原**（另库存映射） | 把去标识病历给科研方，不泄露隐私 |
| **Tokenization（令牌化）** | 用随机 token 字符串替代真实数据（如信用卡号） | 仅令牌库持有方可还原 | 移动支付/电商 recurring 扣款，POS 只见 token 不见卡号 |
| **Anonymization（匿名化）** | 彻底移除可识别信息，理论上无法识别个人 | **不可逆** | 科研/统计聚合数据 |

- **Tokenization vs Pseudonymization**：都用"替身"代替原数据，且替身本身无意义；区别在——令牌化时**支付方**同时掌握 token 与原数据，假名化时第三方（如研究者）**只拿**假名、原数据在别处。
- **Anonymization 难点**：去标识后仍可能被"数据推断(reidentification)"还原（如演员 Gene Hackman 参演电影组合唯一，删名也能锁定）；随机化掩码(randomized masking)打乱列内数据可缓解，但保留聚合值（如平均年龄不变）。

## 真实案例
- **信用卡 tokenization**：Becky 用手机钱包绑卡，实际卡号只在支付网络金库里加密保存，POS 全程只见 token——即便 POS 被入侵也拿不到卡号。
- **《布谷鸟的呼唤》**：J.K.罗琳用 Robert Galbraith 假名出版，泄露后读者才知真相——这就是"假名"的现实版。

## 考试怎么考
- 题型 A：场景问"电商不想存信用卡号、又想重复扣款，该用什么" → **Tokenization**。
- 题型 B：问"把患者姓名换成编号给研究者、仍能还原" → **Pseudonymization**；"彻底无法识别个人" → **Anonymization**。
- 必记混淆项：① 三者都可护隐私，但**只有 Anonymization 不可逆**；② 假名化/令牌化都依赖一个"另存的映射库"；③ CASB 管云边界与影子 IT；④ DRM 只管版权类。

## 记忆口诀
> **"DRM 锁版权，CASB 守云边；假名可还原、令牌付方知、匿名永不可逆。"**

## 自测
1. 某支付系统用一串随机字符代替真实信用卡号，原卡号仅保存在支付网络金库——这是哪种保护方法？（答：Tokenization 令牌化）
2. 与假名化（pseudonymization）相比，匿名化（anonymization）最关键的区别是什么？（答：匿名化不可逆，无法还原到原始个人）
