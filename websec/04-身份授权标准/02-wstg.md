---
title: "OWASP WSTG 测试方法论（v5.0）"
parent: "身份、授权与标准"
grand_parent: "Web 安全与开发基础实战知识库"
nav_order: 2
---

# 概念｜OWASP WSTG 测试方法论（v5.0）

Top 10 告诉你"测什么风险"，WSTG 告诉你"怎么系统地测"。本库已有完整 [WSTG 知识库](../../wstg/wstg.md)，这里做总览衔接。**当前最新版为 v5.0（2026 开发线）。**

## ① 是什么

**WSTG（Web Security Testing Guide）** 是 OWASP 的 Web/API 安全测试标准清单，按 **12 个测试大类**组织，每类下列具体测试项，并用 `WSTG-<类别>-<编号>` 标识。

### WSTG v5.0 的 12 个测试大类（对比 v4.2 主要扩展）

| 大类 | v5.0 关键变化 |
|------|---------------|
| **4.1 信息收集** (INFO) | 10 项，新增攻击面识别、执行路径映射、架构测绘 |
| **4.2 配置和部署管理** (CONF) | **14 项**（v4.2 仅 8 项），新增 HSTS、CSP、路径混淆、云存储、子域接管、HTTP 安全头 |
| **4.3 身份管理** (IDNT) | 5 项，角色/注册/开通/枚举/用户名策略 |
| **4.4 认证测试** (ATHN) | **11 项**（v4.2 9 项），新增 MFA、备用通道、弱安全问题 |
| **4.5 授权测试** (ATHZ) | **7 项**，新增 OAuth 授权服务器/客户端弱点细分 |
| **4.6 会话管理** (SESS) | **11 项**（v4.2 9 项），新增 JWT、并发会话测试 |
| **4.7 输入验证** (INPV) | **23 项**（v4.2 约 15 项），大幅扩展：NoSQL/ORM/客户端注入、SSTI、SSRF、原型污染、不安全反序列化、CSV 注入、大规模赋值、格式化字符串、HTTP 走私、Host 头注入 |
| **4.8 错误处理** (ERRH) | 2 项 |
| **4.9 弱密码学** (CRYP) | 4 项 |
| **4.10 业务逻辑测试** (BUSL) | **10 项**（含支付功能），流程/时序/完整性/滥用/文件上传 |
| **4.11 客户端测试** (CLNT) | **15 项**（v4.2 约 10 项），新增 DOM XSS 子类、CSS 注入、WebSocket、Web Messaging、反向标签劫持、客户端模板注入 |
| **4.12 API 测试** (APIT) | **5 项**（v4.2 仅 GraphQL），对齐 OWASP API Top 10：侦察、BOLA、过度数据暴露、BFLA、GraphQL |

## ② 为什么重要

- 把"该测什么"固化成可复用目录，避免凭感觉漏项。
- 与 Top 10 互补：Top 10 排优先级，WSTG 做验证。
- 与 Burp/ZAP 等工具互补：WSTG 定清单，工具做执行。

## ③ 核心概念拆解

### 场景 ID 体系

- 每个测试场景都有唯一 ID: `WSTG-<类别>-<编号>`
- **引用建议带版本**: `WSTG-v50-<类别>-<编号>` (例如 `WSTG-v50-INFO-02`)
- 版本格式：`WSTG-<version>-<category>-<number>`，其中 `<version>` 去除版本号后缀 (如 v5.0 → `v50`)

### 测试框架

- 包含 **5 个开发阶段**:
  - Phase 1: 开发前 (Before Development Begins) —— 定义 SDLC、评审策略、度量指标
  - Phase 2: 定义和设计 (During Definition and Design) —— 评审安全需求、设计/架构、UML、威胁建模
  - Phase 3: 开发 (During Development) —— 代码走查、静态代码审查（业务需求、Top 10、语言/框架清单、法规）
  - Phase 4: 部署 (During Deployment) —— 应用渗透测试、配置管理测试
  - Phase 5: 维护 (During Maintenance and Operations) —— 运营评审、健康检查、变更验证

### 测试技术谱系

- 手动审查/评审、威胁建模、源码审计、渗透测试——强调**平衡组合**
- 自动化（SAST/DAST/SCA）用于广度覆盖，人工测试覆盖业务逻辑、授权绕过、上下文相关风险

### 与 OWASP 其他标准的关系

- **Top 10** → 风险优先级
- **WSTG** → 测试方法学
- **ASVS** (Application Security Verification Standard) → 验证要求
- **SAMM** (Software Assurance Maturity Model) → 成熟度模型

## ④ 常见误区

- WSTG 是书，照念即可？它是活清单，需按目标裁剪。
- 只跑扫描对照 ID？业务逻辑/业务规则项仍需人工。
- 与 Top 10 二选一？应"Top 10 排优先级 + WSTG 做验证"。
- 版本不标明？ID 可能随版本变更。

## ⑤ 一句话小结

OWASP WSTG v5.0 是 Web 安全测试的"标准清单与 ID 体系"，12 大类 100+ 测试项，与 Top 10 互补：一个排优先级，一个做验证；配合工具落地。

*下一篇：[JWT（含 Scopes）](03-jwt.md)*

> 参考来源：[OWASP WSTG v5.0](https://owasp.org/www-project-web-security-testing-guide/v50/) | [GitHub](https://github.com/OWASP/wstg) | [完整知识库](../../wstg/wstg.md)