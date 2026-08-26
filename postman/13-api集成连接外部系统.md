---
title: "API 集成：连接外部平台与系统"
parent: "Postman 接口测试实战知识库"
nav_order: 13
---

# API 集成：连接外部平台与系统

## 一句话定义
**API 集成**是把两个及以上系统通过接口连起来，让数据和动作自动流转；在 Postman 里先把集成链路验证通(每系统一集合、环境变量隔离、请求链串数据流)，再写代码，大幅减少联调扯皮。

## 核心架构 / 工作原理

```mermaid
graph TD
  A[集成验证三板斧] --> B[每系统一集合]
  B --> B1[外部系统 A: 支付/短信/地图/CRM/ERP]
  B --> B2[内部微服务 B: 用户/订单/库存/通知]
  B --> B3[统一管理: 端点/认证/Schema/测试/文档]
  
  A --> C[环境变量隔离]
  C --> C1[dev/stage/prod 各一套 Environment]
  C --> C2[变量: base_url / client_id / client_secret / api_key / webhook_secret]
  C --> C3[CI Secrets 注入 → 运行时替换占位符]
  
  A --> D[请求链串数据流]
  D --> D1[上游响应 → 提取关键字段 → pm.variables.set()]
  D --> D2[下游请求 → 引用变量 {{var}}]
  D --> D3[典型链: 下单 → 支付回调 → 扣库存 → 发通知 → 回调确认]
  
  A --> E[Webhook 双向验证]
  E --> E1[出站: Monitor 向你的 Webhook 发请求 → 验证签名/幂等/重试]
  E --> E2[入站: 本地起接收端(ngrok/Cloudflare Tunnel) → 验证回调格式/签名/处理逻辑]
  
  A --> F[Flows 可视化编排]
  F --> F1[拖拽 Send Request/Variable/Condition/Loop/Script]
  F --> F2[作为集成演示/轻量编排/非开发同事评审]
  F --> F3[可导出为集合/在 CI 跑]
```

| 集成场景 | 典型链路 | Postman 验证重点 |
|----------|----------|------------------|
| **第三方支付** | 下单 → 创建支付单 → 用户支付 → **异步回调/轮询** → 标记支付成功 → 发货 | 签名验证/幂等键/金额一致性/失败重试/回调超时 |
| **短信/邮件/推送** | 触发事件 → 调通道 API → **回执回调** → 记录送达状态 | 模板变量渲染/频率限制/黑名单/回执解析/重试策略 |
| **地图/地理编码** | 地址 → 标准化 → 坐标 → 逆地理编码 → 距离/路线规划 | 配额/精度/降级(离线库)/批量接口/缓存策略 |
| **内部微服务** | 服务 A → 服务 B → 服务 C (同步/异步) | 契约测试/超时/熔断/重试/链路追踪/Trace ID 透传 |
| **ERP/CRM 同步** | 定时/增量 → 拉数据 → 转换 → 推目标系统 → 确认回写 | 字段映射/增量标记(UpdatedAt)/冲突解决/幂等/全量补偿 |

## 快速上手步骤

1. **建系统级集合**：
   - `Payment Gateway` 集合：`/oauth/token` `/payments` `/refunds` `/webhooks/verify`
   - `SMS Provider` 集合：`/send` `/templates` `/callbacks`
   - `Internal Order Service` 集合：`/orders` `/inventory` `/notifications`
2. **环境变量矩阵**：
   ```json
   // environment-payment-dev.json
   {
     "values": [
       {"key": "base_url", "value": "https://api-sandbox.pay.com/v1", "enabled": true},
       {"key": "client_id", "value": "dev_client_123", "enabled": true},
       {"key": "client_secret", "value": "", "enabled": true},  // CI Secrets 注入
       {"key": "webhook_secret", "value": "", "enabled": true}
     ]
   }
   ```
3. **请求链验证支付全流程**：
   - **步骤 1 创建支付单** Tests:
     ```javascript
     pm.test("Create payment ok", () => pm.response.to.have.status(201));
     pm.collectionVariables.set('payment_id', pm.response.json().id);
     pm.collectionVariables.set('pay_url', pm.response.json().pay_url);
     ```
   - **步骤 2 模拟用户支付** (手工/自动化) → 回调 Webhook
   - **步骤 3 验证回调** (新建请求 `POST /webhooks/payment` Tests):
     ```javascript
     // 验证签名
     const payload = pm.request.body.raw;
     const signature = pm.request.headers.get('X-Pay-Signature');
     const expected = CryptoJS.HmacSHA256(payload, pm.variables.get('webhook_secret')).toString();
     pm.test("Signature valid", () => pm.expect(signature).to.equal(expected));
     
     pm.test("Payment success", () => {
       const data = pm.response.json();
       pm.expect(data.payment_id).to.equal(pm.collectionVariables.get('payment_id'));
       pm.expect(data.status).to.equal('PAID');
     });
     ```
4. **Webhook 入站测试 (本地接收)**：
   - 终端：`ngrok http 3000` → 得到 `https://xxx.ngrok-free.app`
   - 支付沙箱配置回调 `https://xxx.ngrok-free.app/webhooks/payment`
   - 本地起简易服务(或用 Postman Mock Server 作为回调端) → 验证签名/解析/入库
5. **Flows 编排演示**：
   - Flows → Create Flow → 拖拽上述请求块 → 连线传 `payment_id` → Run → 演示给产品/运营看

```bash
# ngrok 暴露本地 Webhook 接收端
ngrok http 3000
# 或 Cloudflare Tunnel (更稳)
cloudflared tunnel --url http://localhost:3000
```

## 踩坑避坑指南

| 场景 | 问题现象 | 原因 | 解决/最佳实践 |
|------|----------|------|---------------|
| 硬编码第三方 URL | 切环境要改代码/集合 | 无变量隔离 | **全链路变量化**：`{{base_url}}/payments`；Environment 矩阵一键切换 |
| 忽略错误处理与重试 | 外部系统超时/5xx 导致主流程挂 | 乐观假设 | **集成层必须容错**：指数退避重试(3次)、熔断(失败率>50%断路)、死信队列、人工补单 |
| 凭证散落各处/提交 Git | 泄露 Client Secret/Webhook Secret | 无统一管理 | **CI Secrets 统一注入**；集合里只放占位符 `""`；本地用 `.env` 不入库 |
| Webhook 签名不验/验错 | 伪造回调/重放攻击 | 安全意识欠缺 | **每个回调必验签名+时间戳+幂等键**；拒绝过期/重复请求 |
| 只测 Happy Path | 失败分支/超时/部分成功未覆盖 | 只验正向 | **每集成必测**：网络超时/5xx/签名错/金额不符/重复回调/并发回调 |

## 替代方案对比

| 维度 | Postman 验证集成 | 代码级集成测试 | 契约测试 | 真实环境联调 |
|------|------------------|----------------|----------|--------------|
| 速度 | 快(分钟级) | 中(需起服务) | 快(无网络) | 慢(需协调) |
| 真实度 | 高(真网络/真外部) | 中(Mock/Testcontainers) | 低(仅契约) | 最高 |
| 非开发参与 | ✅ Flows 可视化 | ❌ 代码 | ❌ 代码 | ⚠️ 需部署 |
| 维护成本 | 低(图形化) | 高(代码/基建) | 中(契约维护) | 高(环境/数据) |
| 适合阶段 | 设计期/开发期/联调前 | 开发期/测试期 | 设计期/变更期 | 预发/生产验收 |

---

> 参考来源：*Mastering Postman, Second Edition*（本文为原创讲解，非转载原文）

*下一篇：[API 性能：负载压测与实时监控](14-api性能压测与实时监控.md)*