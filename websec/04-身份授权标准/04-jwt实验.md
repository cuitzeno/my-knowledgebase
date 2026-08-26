---
title: "JWT 安全实验"
parent: "身份、授权与标准"
grand_parent: "Web 安全与开发基础实战知识库"
nav_order: 4
---

# JWT 安全实验

## 一句话定义
纸上谈兵不如动手验。用 jwt.io 与一个"故意脆弱"的鉴权逻辑，验证三类经典 JWT 漏洞：**篡改 payload(未校验签名)**、**alg=none 攻击**、**弱密钥爆破**、**过期不校验**——直观看到脆弱服务端如何中招。

## 核心架构 / 工作原理

```mermaid
graph TD
  A[JWT 实验四大漏洞] --> B[篡改 Payload (未校验签名)]
  B --> B1[修改 role/user/exp 等声明]
  B --> B2[不重新签名直接发回服务端]
  B --> B3[脆弱实现: 只 JSON.parse 不验签 -> 越权成功]
  
  A --> C[alg=none 攻击]
  C --> C1[Header 改 {"alg":"none","typ":"JWT"}]
  C --> C2[删除签名段(第三段留空)]
  C --> C3[脆弱实现: 接受无签名令牌]
  
  A --> D[弱密钥爆破 (HS256)]
  D --> D1[用 john/hashcat/在线字典对签名离线爆破]
  D --> D2[密钥为 secret/123456/key 等弱口令 -> 秒破]
  D --> D3[破解后可自签任意 payload]
  
  A --> E[过期不校验]
  E --> E1[把 exp 改成远大于当前时间]
  E --> E2[脆弱实现: 忽略 exp 仍信任]
  
  A --> F[正确防御]
  F --> F1[白名单固定算法(禁 none)]
  F --> F2[强随机密钥/非对称 RS256]
  F --> F3[强制校验 exp/nbf/iss/aud]
  F --> F4[按 scope/role 做服务端授权]
```

## 快速上手步骤

1. **准备环境**：
   - 浏览器打开 https://jwt.io
   - 示例令牌 (HS256, 密钥 `secret`)：
     ```
     eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhbGljZSIsInJvbGUiOiJ1c2VyIiwiZXhwIjoxNzAwMDAwMDAwfQ.签名段
     ```
2. **实验 1：篡改 Payload (未校验签名)**：
   - jwt.io 粘贴令牌 → 右侧解码显示 Payload
   - 修改 Payload：`"role": "user"` → `"role": "admin"`
   - **不重新签名**，直接复制新令牌(签名段不变) → 发给脆弱服务端
   - 观察：若服务端只 `JSON.parse` 不验签 → 越权成功
3. **实验 2：alg=none 攻击**：
   - Header 改：`{"alg":"none","typ":"JWT"}`
   - 签名段留空(或删掉第三段 `.`)
   - 发给脆弱服务端 → 若接受 `none` → 无签名令牌被放行
4. **实验 3：弱密钥爆破**：
   - HS256 场景，密钥为 `secret`
   - jwt.io → 右侧 "Verify Signature" 输入 `secret` → 显示"Signature Verified"
   - 实战用工具：
     ```bash
     # john the ripper
     echo 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhbGljZSJ9.签名' > token.jwt
     john --format=HMAC-SHA256 --wordlist=/usr/share/wordlists/rockyou.txt token.jwt
     
     # hashcat
     hashcat -m 16500 -a 0 token.jwt /usr/share/wordlists/rockyou.txt
     ```
5. **实验 4：过期不校验**：
   - Payload 改 `"exp": 9999999999` (远未来)
   - 用原签名(或爆破出的密钥重签) → 发给脆弱服务端
   - 若忽略 `exp` → 过期令牌仍被信任

## 踩坑避坑指南

| 场景 | 问题现象 | 原因 | 解决/最佳实践 |
|------|----------|------|---------------|
| 以为 jwt.io 能直接攻击生产 | jwt.io 只是编码/解码/签名工具 | 误解工具定位 | **jwt.io 用于构造/验证令牌**；攻击需发给目标服务端 |
| 爆破出密钥以为万事大吉 | 仍需服务端接受 HS256/该 kid | 算法/密钥不匹配 | **确认服务端算法/密钥管理**；若用 RS256 则 HS256 爆破无用 |
| 只测 `alg: none` | 忽略 `alg: HS256` 弱密钥/`RS256` 公钥混淆/`kid` 注入 | 攻击面窄 | **全链路测**：none → HS256 爆破 → RS256 混淆 → JWKS 注入 → kid 遍历 |
| 生产环境直接实验 | 触发告警/封锁/污染日志 | 环境混用 | **仅在隔离测试环境/靶场(PortSwigger/DVWA/自建)实验** |

## 替代方案对比

| 维度 | jwt.io 手工实验 | 自动化工具 | 代码审计/SAST |
|------|-----------------|------------|---------------|
| 直观度 | 高(可视化编码/解码/签名) | 中(命令行输出) | 低(静态分析) |
| 覆盖面 | 手工逐个验证 | 可批量/集成 CI | 源码级全覆盖 |
| 适合阶段 | 学习/调试/靶场 | 测试/回归/预发 | 编码期/MR 阶段 |
| 学习价值 | 极高(亲手验证原理) | 中 | 高(模式匹配) |

---

> 参考来源：https://jwt.io/introduction

*下一篇：[OAuth 2.0（含 Scopes）](05-oauth2.md)*