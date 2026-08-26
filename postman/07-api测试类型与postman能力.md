---
title: "API 测试类型与 Postman 测试能力"
parent: "Postman 接口测试实战知识库"
nav_order: 7
---

# API 测试类型与 Postman 测试能力

## 一句话定义
API 测试不止功能测试：还要覆盖**性能/安全/可靠性/兼容性/文档**六大类型；Postman 提供 **Test Scripts / Runner / Mock / Monitor / Integrations** 五件套原生支持 REST/GraphQL/gRPC/WebSocket/SOAP 多协议。

## 核心架构 / 工作原理

```mermaid
graph TD
  A[API 测试六大类型] --> B[功能测试 Functional]
  B --> B1[正向/逆向/边界/业务流]
  B --> B2[Postman: pm.test() 断言状态码/字段/Schema/响应时间]
  
  A --> C[契约测试 Contract]
  C --> C1[请求/响应符合 OpenAPI Schema]
  C --> C2[Postman: pm.response.to.have.jsonSchema() + Mock Server 验证]
  
  A --> D[性能测试 Performance]
  D --> D1[基准/负载/压力/尖峰/稳定性]
  D --> D2[Postman 11: Load Test(虚拟用户/并发/阶梯加压) / Newman 并行跑近似]
  
  A --> E[安全测试 Security]
  E --> E1[认证/授权/注入/敏感信息/配置错误]
  E --> E2[Postman: 安全测试集合(注入Payload/越权/弱鉴权) + CI 门禁]
  
  A --> F[可靠性/混沌 Reliability]
  F --> F1[超时/重试/熔断/降级/网络分区]
  F --> F2[Postman: 测试脚本模拟故障注入 + Monitor 长期观测]
  
  A --> G[兼容性/版本 Compatibility]
  G --> G1[协议版本/数据格式/客户端版本向前/向后兼容]
  G --> G2[Postman: 多 Environment 跑同一集合 + 版本化 Collection]
```

| 测试类型 | 目标 | Postman 核心工具 | 典型指标 |
|----------|------|------------------|----------|
| **功能** | 业务逻辑正确 | Test Scripts + Runner + Data-driven | 通过率、覆盖率、缺陷密度 |
| **契约** | 接口符合规范 | Schema 校验 + Mock Server | Schema 通过率、破坏性变更拦截数 |
| **性能** | 满足 SLA | **Load Test (Postman 11)** / Newman 并行 | p50/p95/p99 延时、吞吐 QPS、错误率、资源利用率 |
| **安全** | 无高危漏洞 | 安全测试集合 + CI 集成 | 高危漏洞 0、中危可接受、扫描覆盖率 |
| **可靠性** | 故障下可用/自愈 | 故障注入脚本 + Monitor | 可用性 99.9%+、MTTR、熔断触发率 |
| **兼容性** | 版本平滑迁移 | 多版本集合 + 环境矩阵 | 旧客户端通过率、破坏性变更零发布 |

## 快速上手步骤

1. **功能/契约测试 (Tests 标签)**：
   ```javascript
   // 状态码
   pm.test("Status 200", () => pm.response.to.have.status(200));
   // 响应时间
   pm.test("Response time < 200ms", () => pm.expect(pm.response.responseTime).to.be.below(200));
   // 字段存在/类型
   pm.test("Has id & title", () => {
     const json = pm.response.json();
     pm.expect(json).to.have.property('id').that.is.a('string');
     pm.expect(json).to.have.property('title').that.is.a('string');
   });
   // Schema 校验 (需先定义 schema 变量或引用)
   pm.test("Schema valid", () => pm.response.to.have.jsonSchema(schemaObj));
   // 从响应提取变量供下一请求用
   pm.environment.set('book_id', pm.response.json().id);
   ```
2. **数据驱动 (Runner)**：
   - 准备 `data.csv`：`name,author,isbn` / `"Clean Code","Robert Martin","9780132350884"`
   - Runner → Select File → Data: `data.csv` → Run → 每行跑一遍请求
   - 脚本取值：`pm.iterationData.get('name')`
3. **多协议测试**：
   - **REST**：原生
   - **GraphQL**：Body → GraphQL → Query 写 query/mutation → Variables 传变量
   - **gRPC**：Improt `.proto` → 选服务/方法 → 填消息体 → Invoke
   - **WebSocket**：New → WebSocket Request → Connect → Send frames → 看消息流
   - **SOAP**：Body → raw → XML → Header `Content-Type: text/xml`
4. **性能 Load Test (Postman 11)**：
   - Collection 右键 → **Run Load Test** → 配置：虚拟用户数、阶梯加压曲线、持续时间、地域
   - 看实时图表：Throughput、Latency(p50/95/99)、Error Rate、VUs
5. **Monitor 长期观测**：
   - Monitors → Create → 选 Collection/Environment → 频率/地域 → 告警阈值(错误率/延时)

```bash
# Newman 并行近似负载 (轻量场景)
newman run coll.json -e env.json -n 100 --parallel 10 --reporters cli,json
```

## 踩坑避坑指南

| 场景 | 问题现象 | 原因 | 解决/最佳实践 |
|------|----------|------|---------------|
| 只断言 200 | 业务字段错/空/类型错全漏测 | 测试太浅 | **最小断言集**：状态码 + 关键字段存在/类型/非空 + Schema 校验 + 响应时间 |
| Schema 校验太严 | 可选字段新增/字段顺序变就红 | required 全勾、additionalProperties: false | **只校验核心必填字段**；`additionalProperties: true`；用 `minProperties` 而非枚举所有 |
| 数据文件含真实密钥 | CI 日志/制品泄露 | 未脱敏 | **CSV/JSON 只放测试数据**；敏感值用 Environment/Secrets 注入 |
| Load Test 打挂共享环境 | 影响其他团队/生产数据污染 | 环境隔离不够 | **专用性能测试环境**；数据隔离/只读/可重置；加压前清理、跑完归档 |
| 只测 Happy Path | 逆向/边界/异常分支全无覆盖 | 只写正向用例 | **每端点最少 3 例**：正向、逆向(400/401/404)、边界(空/超长/特殊字符) |

## 替代方案对比

| 维度 | Postman 全套 | JMeter | k6 | Playwright / Cypress | 专用安全扫描器 |
|------|--------------|--------|----|---------------------|----------------|
| 协议支持 | REST/GraphQL/gRPC/WS/SOAP | HTTP/JDBC/JMS 等 | HTTP/gRPC/WS | HTTP/浏览器 | HTTP/特定协议 |
| 脚本语言 | JavaScript | Groovy/JS/Java | JavaScript (ES6) | TypeScript/JS | 领域规则/自定义 |
| CI/CD 集成 | ✅ Newman/CLI/GitHub Actions | ✅ Jenkins/插件 | ✅ 原生 CLI | ✅ 原生 | ✅ CLI/API |
| 可视化报告 | ✅ 内置/HTML | ✅ HTML/图表 | ✅ 内置/控制台 | ✅ Trace/视频 | ✅ 专业报告 |
| 团队协作 | ✅ Workspace/云同步 | ❌ 文件共享 | ❌ 代码库 | ✅ 代码库 | ⚠️ 导出报告 |
| 适合阶段 | 功能/契约/轻量性能/安全/监控 | 重性能/压测 | 现代性能/开发者友好 | E2E/浏览器级 | 专项安全审计 |

---

> 参考来源：*Mastering Postman, Second Edition*（本文为原创讲解，非转载原文）

*下一篇：[测试脚本进阶：数据驱动、请求链与 Schema 校验](08-测试脚本进阶数据驱动schema校验.md)*