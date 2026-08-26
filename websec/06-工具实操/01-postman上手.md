---
title: "Postman 上手"
parent: "工具实操"
grand_parent: "Web 安全与开发基础实战知识库"
nav_order: 1
---

# Postman 上手

## 一句话定义
本 Lab 用 Postman 完成"建集合 → 设变量 → 写测试 → 串 OAuth2"，把接口调试跑通。**更完整见 [Postman 知识库](../../postman/postman.md)**。

## 核心架构 / 工作原理

```mermaid
graph TD
  A[Postman 核心模型] --> B[Workspace: 项目隔离/团队协作]
  A --> C[Collection: 请求分组+测试脚本+文档]
  A --> D[Environment: 变量键值对(dev/stage/prod)]
  A --> E[Variables 作用域链: Local > Data > Environment > Collection > Global]
  A --> F[Tests/Scripts: pm.test/pm.expect/pm.variables.set/get]
  A --> G[Runner/Monitor: 批量跑/定时监控/CI 集成]
  A --> H[OAuth 2.0: Authorization Code/Client Credentials/Device Code/PKCE 原生支持]
```

## 快速上手步骤

1. **安装与登录**：
   - 下载：https://www.postman.com/downloads/ (桌面版推荐，支持本地服务/代理/离线)
   - 登录免费账号 → 云同步开启
2. **建 Workspace 与 Collection**：
   - 左侧 `Workspaces` → `Create Workspace` → 命名 `WebSec-Lab` → Team/Private
   - `Collections` → `New Collection` → 命名 `API-Tests`
3. **设环境变量**：
   - `Environments` → `Add` → 命名 `dev` → 加变量：
     - `baseUrl` = `https://api.github.com`
     - `token` = `""` (留空，后面 OAuth2 拿)
   - 右上角环境下拉切到 `dev`
4. **建请求 + 写测试脚本**：
   - Collection 里 `Add Request` → 命名 `Get User` → `GET {{baseUrl}}/user`
   - `Authorization` 标签 → `Bearer Token` → Token 填 `{{token}}`
   - `Tests` 标签写：
     ```javascript
     pm.test("状态码 200", () => pm.response.to.have.status(200));
     pm.test("返回 login 字段", () => pm.expect(pm.response.json().login).to.be.a('string'));
     // 把 token 存环境，供后续请求复用
     const t = pm.response.json().token;
     if (t) pm.environment.set("token", t);
     ```
5. **跑通请求链**：
   - 点 `Send` → 绿勾即通过
   - `Collection Runner` → 选 Collection + Environment + Data File(可选) → `Run` → 批量跑多请求
6. **OAuth 2.0 拿 Token (见 [Postman 调 OAuth2](../../04-身份授权标准/06-postman调oauth2.md))**：
   - Authorization 标签 → Type `OAuth 2.0` → `Get New Access Token` → 配置 Authorization Code + PKCE → 拿 Token → `Use Token`

```bash
# CLI 验证 (Newman/Postman CLI)
newman run collection.json -e environment.json --reporters cli,json
postman collection run <collection-id> -e <env-id>
```

## 踩坑避坑指南

| 场景 | 问题现象 | 原因 | 解决/最佳实践 |
|------|----------|------|---------------|
| 不登录直接用 | 集合只存本地、换机器丢失、无法协作 | 未关联账号 | **首启动即登录**；免费版同步无限制 Personal Workspace |
| 全部请求塞默认 Workspace | 项目多后找不到、权限混乱 | 无隔离规范 | **一项目一 Workspace**；Team Workspace 给成员角色(Viewer/Editor/Admin) |
| 变量不生效/值不对 | `{{var}}` 没替换/值旧 | 不懂变量优先级链 | **优先级**：Local(迭代) > Data(CSV) > Environment > Collection > Global；用 `pm.variables.get()` 统一读取 |
| 敏感信息提交 Git | Collection/Environment 含真实 Token/密钥 | 导出时未脱敏 | **CI 用 Secrets 注入**；本地用 `.postman-env` 不入库；导出前脚本脱敏 |
| Web 版调本地 `localhost` 失败 | CORS 报错/连接拒绝 | 浏览器沙箱限制 | **装 Postman Desktop Agent** 或直接用桌面版 |

## 替代方案对比

| 维度 | Postman Desktop | Postman Web | Insomnia | HTTPie / curl |
|------|-----------------|-------------|----------|---------------|
| 本地服务调用 | ✅ 原生 | ⚠️ 需 Agent | ✅ 原生 | ✅ 原生 |
| 离线工作 | ✅ 完全 | ❌ 需网 | ✅ 完全 | ✅ 完全 |
| 代理抓包/证书 | ✅ 完善 | ❌ 无 | ⚠️ 基础 | ❌ 无 |
| 团队协作/同步 | ✅ 云同步 | ✅ 云优先 | ✅ 同步(付费) | ❌ 手动 |
| 界面可视化 | ✅ 丰富 | ✅ 丰富 | ✅ 简洁 | ❌ CLI |
| 资源占用 | 较高(Electron) | 低(浏览器) | 中等 | 极低 |

---

> 参考来源：https://learning.postman.com/docs/getting-started/introduction/

*下一篇：[Burp Suite 上手](02-burp上手.md)*