---
title: "API 认证与授权：Basic / API Key / OAuth 2.0"
parent: "Postman 接口测试实战知识库"
nav_order: 5
---

# API 认证与授权：Basic / API Key / OAuth 2.0

## 一句话定义
**认证**解决"你是谁"，**授权**解决"你能干什么"；Postman Authorization 标签页原生支持 **Basic Auth**、**API Key**、**OAuth 2.0**(含 PKCE/Client Credentials/Device Code) 一键生成鉴权头。

## 核心架构 / 工作原理

```mermaid
graph TD
  A[API 鉴权三大类] --> B[Basic Auth]
  B --> B1[用户名:密码 -> Base64 -> Authorization: Basic xxx]
  B --> B2[简单但明文等价，必须 HTTPS]
  B --> B3[Postman: Auth标签 -> Basic Auth -> 填账号密码 -> 自动生成头]
  
  A --> C[API Key]
  C --> C1[服务端颁发固定密钥]
  C --> C2[位置: Header(如 X-API-Key) / Query / Cookie]
  C --> C3[Postman: Auth标签 -> API Key -> Key/Value/位置 -> 自动注入]
  
  A --> D[OAuth 2.0 / OIDC]
  D --> D1[Authorization Code + PKCE: 公共客户端(SPA/移动端)标配]
  D --> D2[Client Credentials: 服务间/机器对机器]
  D --> D3[Device Code: 无浏览器设备(TV/CLI)]
  D --> D4[Resource Owner Password: 遗留/测试慎用]
  D --> D5[Postman: Auth标签 -> OAuth 2.0 -> 选流程 -> 填端点/Client ID/Secret -> Get New Access Token]
```

| 鉴权方式 | 适用场景 | 安全性 | Postman 配置要点 |
|----------|----------|--------|------------------|
| **Basic Auth** | 内部/测试/简单服务端 | 低(仅 Base64) | **必须 HTTPS**；勿用于生产对外 API |
| **API Key** | 服务端间调用/第三方集成/简单场景 | 中(密钥泄露=全权) | 放 **Header** 而非 Query(防日志泄露)；支持轮换/撤销 |
| **OAuth 2.0 Auth Code + PKCE** | SPA/移动端/公共客户端 | 高(无 Client Secret、防授权码劫持) | **Postman 11+ 原生支持 PKCE**；Auth URL/Token URL/Redirect URI/Client ID/Scopes/PKCE 勾选 |
| **OAuth 2.0 Client Credentials** | 后端服务调用/定时任务 | 高(机器身份) | Token URL + Client ID/Secret + Scopes；无用户交互 |
| **OAuth 2.0 Device Code** | CLI/TV/IoT 设备 | 高(用户在别设备授权) | Device Auth URL + Token URL + Client ID；轮询 Token URL |

## 快速上手步骤

1. **Basic Auth**：
   - 请求 Authorization 标签 → Type: **Basic Auth** → Username / Password → 发送 → Header 自动带 `Authorization: Basic base64(user:pass)`
2. **API Key**：
   - Type: **API Key** → Key: `X-API-Key` / Value: `sk_live_xxx` → Add to: **Header** → 发送
3. **OAuth 2.0 Authorization Code + PKCE (最常用)**：
   - Type: **OAuth 2.0** → Grant Type: **Authorization Code (with PKCE)**
   - 填入：
     - Auth URL: `https://auth.example.com/oauth/authorize`
     - Access Token URL: `https://auth.example.com/oauth/token`
     - Client ID: `postman-client`
     - Client Secret: (公共客户端可留空/填)
     - Scope: `read write`
     - Redirect URI: `https://oauth.pstmn.io/v1/callback` (Postman 云回调) 或 `http://127.0.0.1:5555/callback` (本地)
     - ☑ **PKCE** (强制开启)
   - 点 **Get New Access Token** → 浏览器弹窗登录/授权 → 返回 Token → **Use Token**
4. **Client Credentials (服务间)**：
   - Grant Type: **Client Credentials** → Token URL + Client ID/Secret + Scope → Get Token
5. **环境变量复用**：
   - Environment 设 `access_token` → Tests: `pm.environment.set('access_token', pm.response.json().access_token)`
   - 后续请求 Auth: **Bearer Token** → Token: `{{access_token}}`

```bash
# 手工获取 Token (curl 版，对照理解流程)
# 1. 授权码 + PKCE
code_verifier=$(openssl rand -base64 32 | tr -d '=+/')
code_challenge=$(echo -n "$code_verifier" | openssl dgst -sha256 -binary | openssl base64 | tr -d '=+/')
# 浏览器打开: https://auth.example.com/oauth/authorize?client_id=xxx&redirect_uri=...&code_challenge=$code_challenge&code_challenge_method=S256&response_type=code&scope=read
# 2. 换 Token
curl -X POST https://auth.example.com/oauth/token \
  -d "grant_type=authorization_code&code=AUTH_CODE&redirect_uri=...&code_verifier=$code_verifier&client_id=xxx"
```

## 踩坑避坑指南

| 场景 | 问题现象 | 原因 | 解决/最佳实践 |
|------|----------|------|---------------|
| Basic Auth 用 HTTP | 密码等效明文传输 | Base64 非加密 | **生产强制 HTTPS**；或改用 OAuth/API Key |
| API Key 放 Query 参数 | `?api_key=xxx` 进服务器日志/代理/浏览器历史 | 位置选错 | **必须放 Header**(如 `X-API-Key` `Authorization: ApiKey xxx`) |
| 公共客户端存 Client Secret | 反编译/源码泄露即失控 | SPA/移动端无法保密 | **必须用 PKCE**，不存 Secret；Postman 勾选 PKCE 自动处理 |
| Token 永不过期 | 泄露后永久有效、无法撤销 | 未设过期/刷新机制 | **Access Token 短时(15-60min)** + **Refresh Token 轮换** + 撤销端点 |
| 忽略 State 参数 | CSRF 攻击者诱导授权绑定其账号 | 未防跨站请求伪造 | **Authorization Request 带随机 `state`** → 回调校验一致 |
| Postman 回调地址不匹配 | `redirect_uri_mismatch` | 授权服务器白名单未加 | 授权服务器加 `https://oauth.pstmn.io/v1/callback` 和 `http://127.0.0.1:5555/callback` |

## 替代方案对比

| 维度 | Postman 内置 OAuth | 手写 curl/代码 | Insomnia | 专用 OAuth 工具 |
|------|-------------------|----------------|----------|----------------|
| PKCE 支持 | ✅ 原生 (11+) | 手工实现复杂 | ✅ 原生 | ✅ 专业 |
| 多流程覆盖 | ✅ Auth Code/Client Cred/Device/ROPC/Implicit | 全靠自己 | ✅ 主流 | ✅ 全 |
| Token 自动刷新 | ✅ 过期自动刷新(设置) | 手工/库支持 | ✅ 自动 | ✅ 自动 |
| 团队共享 Token | ✅ 环境变量/保险箱 | ❌ 手工分发 | ✅ 同步 | ❌ 无 |
| 学习成本 | 低(图形化) | 高(需懂协议细节) | 低 | 中 |

---

> 参考来源：*Mastering Postman, Second Edition*（本文为原创讲解，非转载原文）

*下一篇：[错误处理、限流与 Postman Flows 编排](06-错误处理限流与flows.md)*