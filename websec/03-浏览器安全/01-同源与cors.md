---
title: "同源策略与 CORS"
parent: "浏览器安全机制"
grand_parent: "Web 安全与开发基础实战知识库"
nav_order: 1
---

# 同源策略与 CORS

## 一句话定义
浏览器默认不让 A 站脚本读 B 站数据，这道墙叫**同源策略 (SOP)**；**CORS (跨源资源共享)** 是服务器用响应头声明"允许哪些源跨域访问"的受控开窗机制——配错（过度放行）会直接击穿 SOP，导致跨域数据泄露。

## 核心架构 / 工作原理

```mermaid
graph TD
  A[同源策略 SOP] --> B[同源判定]
  B --> B1[协议+域名+端口 三者全同]
  B --> B2[不同源: 默认禁止读响应/操作 DOM/存 Cookie]
  
  A --> C[CORS 机制]
  C --> C1[简单请求: 直接发 + Origin 头]
  C --> C2[预检请求: 非简单先发 OPTIONS 问权限]
  C --> C3[响应头判定: ACAO/ACAC/ACAM/ACAH]
  
  A --> D[危险配置]
  D --> D1[ACAO 反射任意 Origin + ACAC: true]
  D --> D2[ACAO: * + ACAC: true (非法组合)]
  D --> D3[子域泄露: ACAO: *.example.com]
```

| CORS 头 | 作用 | 安全配置建议 |
|---------|------|--------------|
| `Access-Control-Allow-Origin` (ACAO) | 允许的源 | **明确列域名**，禁止 `*` 配合凭据；禁止反射任意 Origin |
| `Access-Control-Allow-Credentials` (ACAC) | 是否允许携带凭据 | **仅受信源置 true**；带凭据时 ACAO 不能为 `*` |
| `Access-Control-Allow-Methods` (ACAM) | 允许的方法 | 最小集合(如 `GET, POST`) |
| `Access-Control-Allow-Headers` (ACAH) | 允许的头 | 最小集合(如 `Content-Type, Authorization`) |
| `Access-Control-Max-Age` | 预检缓存时间 | 合理值(如 86400)避免频繁预检 |

## 快速上手步骤

1. **判定同源**：
   ```bash
   # 同源 = 协议+域名+端口全同
   # https://a.com 与 https://a.com:8080 不同源(端口不同)
   # https://a.com 与 http://a.com 不同源(协议不同)
   ```
2. **测试 CORS 配置**：
   ```bash
   # 简单请求测试
   curl -H "Origin: https://evil.com" -v https://target.com/api/data
   # 看响应头 ACAO/ACAC
   
   # 预检请求测试
   curl -X OPTIONS -H "Origin: https://evil.com" \
     -H "Access-Control-Request-Method: POST" \
     -H "Access-Control-Request-Headers: Content-Type" \
     -v https://target.com/api/data
   ```
3. **验证危险配置**：
   - 请求 `Origin: https://evil.com` → 响应 `ACAO: https://evil.com` + `ACAC: true` = **高危**
   - 请求 `Origin: null` / `file://` / 子域 → 看是否被放行
4. **修复**：服务端白名单校验 Origin → 仅允许受信域名；ACAC=true 仅配受信源

## 踩坑避坑指南

| 场景 | 问题现象 | 原因 | 解决/最佳实践 |
|------|----------|------|---------------|
| CORS 以为是服务器防攻击 | 实为浏览器执行、保护客户端数据 | 认知偏差 | **CORS 由浏览器强制**；后端仍需自己做鉴权/授权/输入校验 |
| `ACAO: *` 图方便 | 带凭据时不能用 `*`；非凭据也泄露公开数据 | 配置粗心 | **禁止 `*` 配合凭据**；明确列域名；内部 API 亦同 |
| 反射任意 Origin | `Origin: evil.com` -> `ACAO: evil.com` + `ACAC: true` | 白名单校验缺失 | **服务端白名单校验 Origin**；仅允许受信域名 |
| 前端报 CORS 错怪后端 | 多是不该跨域/未授权跨域 | 设计而非实现问题 | **跨域需设计**：同源部署/网关聚合/明确授权域名 |
| 子域通配放行 | `ACAO: *.example.com` 泄露给失控子域 | 过度授权 | **精确列域名**；子域失控不应波及主域 |

## 替代方案对比

| 维度 | CORS | JSONP | 代理/网关聚合 | 同源部署 |
|------|------|-------|---------------|----------|
| 安全性 | 高(浏览器强制/白名单) | 低(脚本注入/无校验) | 高(服务端可控) | 最高(无跨域) |
| 方法支持 | 全方法 | 仅 GET | 全方法 | 全方法 |
| 凭据支持 | 可控(ACAC) | 自动携带 Cookie | 自动携带 | 自动携带 |
| 复杂度 | 中(需配置头) | 低(脚本标签) | 中(网关配置) | 低(架构层面) |
| 适用场景 | 多源协作/第三方 API | 遗留/仅 GET 只读 | 微服务内部聚合 | 单团队/单域 |

---

> 参考来源：https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS

*下一篇：[CSP 内容安全策略](02-csp.md)*