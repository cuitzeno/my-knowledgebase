---
title: "用 Postman 调 OAuth2 接口"
parent: "身份、授权与标准"
grand_parent: "Web 安全与开发基础实战知识库"
nav_order: 6
---

# 用 Postman 调 OAuth2 接口

## 一句话定义
理完 OAuth 2.0 概念，动手用 Postman 走完 **Authorization Code (含 PKCE)** 或 **Client Credentials** 拿 access token，再调受保护接口，体会 scope 与令牌流转。

## 核心架构 / 工作原理

```mermaid
graph TD
  A[Postman OAuth 2.0 支持] --> B[Authorization Code (+ PKCE)]
  B --> B1[Auth URL / Token URL / Client ID / Secret]
  B --> B2[Scope / State / PKCE (S256)]
  B --> B3[Redirect URI: https://oauth.pstmn.io/v1/callback (云) 或 http://127.0.0.1:5555/callback (本地)]
  B --> B4[Get New Access Token -> 浏览器授权 -> 回调 -> Token 列表 -> Use Token]
  
  A --> C[Client Credentials]
  C --> C1[Token URL / Client ID / Secret / Scope]
  C --> C2[Get New Access Token -> 直接拿 Token]
  
  A --> D[Token 使用]
  D --> D1[请求 Authorization 标签 -> Bearer Token -> {{access_token}}]
  D --> D2[Tests 脚本自动存环境变量: pm.environment.set('token', pm.response.json().access_token)]
  D --> D3[后续请求自动带 Token]
```

## 快速上手步骤

1. **准备 OAuth 2.0 客户端 (以 GitHub 为例)**：
   - GitHub → Settings → Developer settings → OAuth Apps → New OAuth App
   - 填：Application name、Homepage URL、Authorization callback URL: `https://oauth.pstmn.io/v1/callback`
   - 得到 `Client ID`、`Client Secret`
2. **Postman 配置 Authorization Code**：
   - 新建请求 `GET https://api.github.com/user`
   - Authorization 标签 → Type: **OAuth 2.0** → **Get New Access Token**
   - 填入：
     - Grant Type: `Authorization Code`
     - Auth URL: `https://github.com/login/oauth/authorize`
     - Access Token URL: `https://github.com/login/oauth/access_token`
     - Client ID / Client Secret: 刚得到的值
     - Scope: `read:user`
     - Redirect URI: `https://oauth.pstmn.io/v1/callback` (Postman 云回调)
     - State: 随机值 (建议填)
     - ☑ **PKCE** (Postman 11+ 原生支持 S256)
   - 点 **Get New Access Token** → 浏览器弹窗登录 GitHub → 授权 → 回调 → Token 列表出现 → **Use Token**
3. **验证 Scope 限制**：
   - 发请求 → 200 返回用户信息
   - 改 Scope 为 `user:email` → 重新 Get Token → 再发 → 观察某些字段可见/不可见
4. **Client Credentials (服务间)**：
   - Grant Type: `Client Credentials`
   - Token URL + Client ID + Secret + Scope → Get Token → Use Token
5. **自动化存 Token (Tests 脚本)**：
   ```javascript
   // 在获取 Token 的请求 Tests 里
   if (pm.response.code === 200) {
     const data = pm.response.json();
     if (data.access_token) pm.environment.set('access_token', data.access_token);
     if (data.refresh_token) pm.environment.set('refresh_token', data.refresh_token);
   }
   ```
   - 后续请求 Auth: **Bearer Token** → Token: `{{access_token}}`

## 踩坑避坑指南

| 场景 | 问题现象 | 原因 | 解决/最佳实践 |
|------|----------|------|---------------|
| Redirect URI 不匹配 | `redirect_uri_mismatch` | 授权服务器白名单未加 Postman 回调 | **授权服务器必加**：`https://oauth.pstmn.io/v1/callback` (云) + `http://127.0.0.1:5555/callback` (本地) |
| PKCE 报错 | `invalid_grant` / `code_verifier` 校验失败 | 授权服务器不支持 PKCE / 配置错 | **确认授权服务器支持 PKCE S256**；Postman 11+ 自动生成 verifier/challenge |
| Token 过期不自动刷新 | 请求突然 401 | 无自动刷新逻辑 | **Pre-request Script 检查过期主动刷新**；或 Postman 11+ 勾选"Auto refresh token" |
| 敏感 Secret 提交 Git | Collection 导出含 Client Secret | 导出未脱敏 | **Collection 里 Secret 留空/占位**；CI Secrets 注入 → 运行时替换；或用 Postman Vault |
| 仅测 Authorization Code | 忽略 Client Credentials/Device Code/Refresh 流程 | 场景覆盖不全 | **按项目类型全测**：SPA=Auth Code+PKCE、服务间=Client Credentials、CLI=Device Code |

## 替代方案对比

| 维度 | Postman 内置 OAuth | 手写 curl/代码 | Insomnia | 专用 OAuth 测试工具 |
|------|-------------------|----------------|----------|---------------------|
| PKCE 支持 | ✅ 原生 (11+) | 手工实现易错 | ✅ 原生 | ✅ 专业 |
| 多流程覆盖 | ✅ Auth Code/Client Cred/Device/Implicit(已废弃) | 全靠自己 | ✅ 主流 | ✅ 全 |
| Token 自动刷新 | ✅ 11+ 支持配置 | 需自己写 | ✅ 自动 | ✅ 支持 |
| 团队共享 Token | ✅ 环境变量/Vault | ❌ 手工分发 | ✅ 同步 | ❌ 无 |
| 学习成本 | 低(图形化) | 高(需懂协议细节) | 低 | 中 |

---

> 参考来源：https://learning.postman.com/docs/getting-started/introduction/

*系列完：身份、授权与标准*