---
title: "JWT（含 Scopes）"
parent: "身份、授权与标准"
grand_parent: "Web 安全与开发基础实战知识库"
nav_order: 3
---

# JWT（含 Scopes）

## 一句话定义
JWT 是现代 API 鉴权主流令牌：三段 `header.payload.signature` (Base64Url 编码)，服务端用签名验证"内容未被篡改"，无需查库即可信任声明。安全要点：**固定算法(禁 none)、强密钥/非对称、校验过期、用 scope 做服务端授权**。

## 核心架构 / 工作原理

```mermaid
graph LR
  A[JWT 结构] --> B[Header]
  B --> B1[alg: HS256/RS256/ES256...]
  B --> B2[typ: JWT]
  
  A --> C[Payload Claims]
  C --> C1[注册声明: sub/iss/exp/nbf/iat/aud/jti]
  C --> C2[公共声明: role/scope/permissions/email...]
  C --> C3[私有声明: 业务自定义]
  
  A --> D[Signature]
  D --> D1[HS256: HMAC-SHA256(key, base64(header)+"."+base64(payload))]
  D --> D2[RS256: RSA-SHA256(private_key, ...)]
  D --> D3[验证: 服务端用 key/public_key 验签 -> 信任 payload]
  
  A --> E[Scopes 授权]
  E --> E1[payload: {"scope":"read:profile write:orders"}]
  E --> E2[服务端按 scope 校验: 访问 /api/orders 需 write:orders]
  E --> E3[最小授权: 用户同意/收缩 scope -> 令牌仅含所需权限]
```

| 算法类型 | 典型算法 | 密钥管理 | 适用场景 |
|----------|----------|----------|----------|
| **对称** | HS256/HS384/HS512 | 共享密钥(需极强随机/轮换) | 单体/内部服务间 |
| **非对称** | RS256/RS384/RS512/ES256/EdDSA | 私钥签/公钥验(公钥可公开/JWKS) | 微服务/联邦/多方信任 |
| **无签名** | `alg: none` | 无 | **严禁**/仅测试 |

## 快速上手步骤

1. **解码观察 (jwt.io / CLI)**：
   ```bash
   # Base64Url 解码 (去掉 padding 再解)
   echo "eyJhbGc..." | cut -d. -f1 | tr '_-' '/+' | base64 -d | jq .
   echo "eyJhbGc..." | cut -d. -f2 | tr '_-' '/+' | base64 -d | jq .
   ```
2. **验证签名 (在线/代码)**：
   - jwt.io 粘贴 Token + 密钥/公钥 → 看"Signature Verified"
   - 代码：`jose` / `jsonwebtoken` / `jjwt` / `PyJWT` 等库
3. **服务端安全配置清单**：
   - ✅ 白名单固定算法：`['RS256']` / `['HS256']`，**拒绝 `none`**
   - ✅ HS256 用强随机密钥(≥256 bits) + 定期轮换
   - ✅ RS256 用 JWKS 端点动态获取公钥 / 缓存公钥
   - ✅ 必校验 `exp` `nbf` `iss` `aud` (若多租户)
   - ✅ **按 `scope`/`role` 做服务端授权**，不能只验签名
4. **Token 安全实验**：见 [JWT 安全实验](04-jwt实验.md)

```javascript
// Node jsonwebtoken 安全验证示例
const jwt = require('jsonwebtoken');
const jwksClient = require('jwks-rsa');

const client = jwksClient({jwksUri: 'https://auth.example.com/.well-known/jwks.json'});

function verifyToken(token) {
  return new Promise((resolve, reject) => {
    const decoded = jwt.decode(token, {complete: true});
    if (!decoded || !['RS256'].includes(decoded.header.alg)) {
      return reject(new Error('Algorithm not allowed'));
    }
    const key = client.getSigningKey(decoded.header.kid);
    jwt.verify(token, key.getPublicKey(), {
      algorithms: ['RS256'],
      issuer: 'https://auth.example.com',
      audience: 'my-api'
    }, (err, payload) => err ? reject(err) : resolve(payload));
  });
}
```

## 踩坑避坑指南

| 场景 | 问题现象 | 原因 | 解决/最佳实践 |
|------|----------|------|---------------|
| JWT 以为加密 | 默认只签名不加密，payload 可被解码读 | 认知偏差 | **敏感数据别放 payload**；需加密用 JWE (JSON Web Encryption) |
| 改了算法就安全 | 服务端仍接受 `none`/弱算法 | 白名单缺失 | **服务端白名单固定算法**；拒绝 `none`/不在白名单内的算法 |
| 有 JWT 就有权限 | 只验签名、不校验 scope/role | 授权逻辑缺失 | **必须按 `scope`/`role` 做服务端授权**；资源级/功能级校验 |
| HS256 弱密钥 | `secret`/`123456` 被离线爆破 | 密钥管理缺失 | **≥256 bits 强随机密钥**；定期轮换；或改非对称 RS256 |
| 过期不校验 | 忽略 `exp` 导致令牌永久有效 | 校验逻辑缺失 | **强制校验 `exp` `nbf`**；短时 Access Token(15-30min) + Refresh 轮换 |
| `kid` 注入 | JWKS `kid` 指向恶意密钥/路径遍历 | `kid` 未校验 | **白名单 `kid`**；JWKS 仅信任自有域名；拒绝外部 URL |

## 替代方案对比

| 维度 | JWT (无状态) | Session/Cookie (有状态) | OAuth 2.0 Access Token | API Key |
|------|--------------|------------------------|------------------------|---------|
| 状态 | 无状态(自包含) | 有状态(服务端存 Session) | 无状态/有状态均可 | 无状态 |
| 撤销/轮换 | 需黑名单/短期+轮换 | 服务端直接删 Session | Refresh Token 轮换/撤销链 | 吊销/重发 Key |
| 适用场景 | 微服务/单点登录/联邦 | 传统 Web/单体 | 委托授权/第三方 | 服务间/简单场景 |
| 体积 | 较大(含所有声明) | 小(仅 Session ID) | 中等 | 极小 |
| 传输 | Header/Body/Cookie | Cookie | Header Bearer | Header/Query |

---

> 参考来源：https://jwt.io/introduction

*下一篇：[JWT 安全实验](04-jwt实验.md)*