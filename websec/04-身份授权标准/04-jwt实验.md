---
title: "JWT 安全实验"
parent: "身份、授权与标准"
grand_parent: "Web 安全与开发基础实战知识库"
nav_order: 4
---

# 实操（Lab）｜JWT 安全实验

纸上谈兵不如动手验。本 Lab 用 jwt.io 与一个"故意脆弱"的鉴权逻辑，验证三类经典 JWT 漏洞。

## 目标

- 直观看到：篡改 payload、改算法、用弱密钥，脆弱服务端如何中招。
- 理解"服务端必须固定算法 + 校验过期 + 强密钥"。

## 环境

- 浏览器打开 https://jwt.io （可在线解码/编码/签名）。
- 一段示例令牌（解码后）：

```
header:  {"alg":"HS256","typ":"JWT"}
payload: {"sub":"alice","role":"user","exp":1700000000}
```

## 分步

1. **篡改 payload（未校验签名）**：在 jwt.io 把 `role` 改成 `admin`，不重新签名直接发回服务端。若服务端只 `JSON.parse` 不验签 → 越权成功。
2. **alg=none 攻击**：把 header 改成 `{"alg":"none"}`，删掉签名段，重发。脆弱实现会放行"无签名"令牌。
3. **弱密钥爆破**：HS256 场景，用 `john`/`hashcat` 或在线字典对签名爆破；密钥为 `secret` 时秒破，随后可自己签名任意 payload。
4. **过期不校验**：把 `exp` 改成远大于当前时间，脆弱服务端若忽略 `exp` 仍信任。

## 现象与结论

- 以上任一步"成功"都说明服务端信任了不该信任的内容。
- **正确做法**：服务端白名单固定算法（禁 none）、用强随机密钥（HS256）或非对称 RS256、强制校验 `exp` 与 `aud`/`iss`、按 `scope/role` 做服务端授权。

> 参考来源：https://jwt.io/introduction
