---
title: "HTTP 方法与语义"
parent: "协议与架构"
grand_parent: "Web 安全与开发基础实战知识库"
nav_order: 2
---

# HTTP 方法与语义

## 一句话定义
GET 和 POST 不只是"两种请求"。方法表达"想对资源做什么"，语义错了就是安全漏洞——服务端若对 `PUT/DELETE` 等未禁用，可能被滥用；前端隐藏按钮≠后端校验方法。

## 核心架构 / 工作原理

```mermaid
graph TD
  A[HTTP 方法] --> B[安全方法 Safe Methods]
  B --> B1[GET: 只读、幂等、可缓存]
  B --> B2[HEAD: 只取头、无 Body]
  B --> B3[OPTIONS: 探测能力]
  B --> B4[TRACE: 回环测试(常禁用)]
  
  A --> C[非安全方法 Unsafe Methods]
  C --> C1[POST: 创建/提交、非幂等]
  C --> C2[PUT: 整体替换、幂等]
  C --> C3[PATCH: 部分更新、非幂等]
  C --> C4[DELETE: 删除、幂等]
  
  C --> D[语义约定]
  D --> D1[查用 GET/HEAD]
  D --> D2[增用 POST]
  D --> D3[全改用 PUT]
  D --> D4[删用 DELETE]
```

| 方法 | 语义 | 安全/幂等 | 典型风险 | 测试点 |
|------|------|-----------|----------|--------|
| **GET** | 取资源 | ✅/✅ | 敏感参数进日志/历史 | 参数注入、缓存投毒 |
| **POST** | 建/提交 | ❌/❌ | CSRF、重放、参数污染 | 动词篡改、HPP |
| **PUT** | 整体改 | ❌/✅ | 覆盖他人数据、幂等被滥用 | 越权、幂等验证 |
| **PATCH** | 部分改 | ❌/❌ | 字段级越权、类型混淆 | 字段级授权 |
| **DELETE** | 删资源 | ❌/✅ | 未授权删除、幂等被滥用 | 授权校验 |
| **OPTIONS** | 探测 | ✅/✅ | 信息泄露 | CORS 预检 |

## 快速上手步骤

1. **抓正常请求**：用 Burp/Postman 抓业务流程 → 看每步用什么方法
2. **动词篡改测试**：Repeater 改方法（GET→POST/DELETE/PUT）→ 看是否绕过校验/触发非预期操作
3. **幂等性验证**：对 PUT/DELETE 重复发 3 次 → 看效果是否等同单次（幂等=多次=单次）
4. **方法枚举**：对敏感端点发 OPTIONS → 看 `Allow` 头是否泄露过多方法
5. **前端/后端一致性**：前端只给 POST 按钮 → 后端是否真只允许 POST

```bash
# 快速测试方法篡改
curl -X DELETE https://api.example.com/books/1 -H "Authorization: Bearer <token>"
curl -X PUT https://api.example.com/books/1 -H "Content-Type: application/json" -d '{"title":"hacked"}'
curl -X OPTIONS https://api.example.com/books -v
```

## 踩坑避坑指南

| 场景 | 问题现象 | 原因 | 解决/最佳实践 |
|------|----------|------|---------------|
| GET 以为安全 | GET 带敏感参数进日志/历史/Referer | 误以为只读即安全 | **敏感数据勿放 URL**；GET 应无副作用但不等于无风险 |
| 前端限制方法 | 以为前端只给 POST 按钮就安全 | 攻击者可用工具任意改方法 | **服务端必须白名单校验允许的方法集合** |
| PUT/DELETE 开放 | 服务端对 PUT/DELETE 未禁用/未鉴权 | 默认配置/遗留接口 | **禁用无用方法**；启用的必须鉴权+授权+幂等校验 |
| POST 当 GET 用 | 查询接口用 POST 带 Body | 设计不规范 | **查询用 GET + Query 参数**；复杂查询可用 POST 但语义要清晰 |
| PATCH 当 PUT 用 | 部分更新接口要求全字段 | 语义混淆 | **PATCH 只传变更字段**；PUT 需全字段（幂等） |

## 替代方案对比

| 维度 | RESTful 风格 | RPC 风格 (gRPC/Thrift) | GraphQL |
|------|--------------|------------------------|---------|
| 方法映射 | HTTP 方法表达 CRUD | 方法名表达动作 (GetUser/DeleteUser) | 统一 POST + query/mutation |
| 幂等性 | 显式 (GET/PUT/DELETE 幂等) | 由方法定义决定 | mutation 默认非幂等 |
| 缓存 | 原生支持 GET/HEAD 缓存 | 需自行实现 | 客户端缓存/HTTP 缓存均可 |
| 语义清晰度 | 高 (标准化) | 高 (契约化) | 中 (需看 Schema) |
| 安全测试 | 动词篡改/幂等测试 | 契约测试/参数测试 | Query 深度/批量/字段级授权 |

---

> 参考来源：https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods

*下一篇：[HTTP 安全响应头（OWASP Secure Headers）](03-http安全头.md)*