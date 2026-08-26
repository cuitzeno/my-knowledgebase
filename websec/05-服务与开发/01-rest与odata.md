---
title: "REST 与 OData 服务"
parent: "服务与开发安全"
grand_parent: "Web 安全与开发基础实战知识库"
nav_order: 1
---

# REST 与 OData 服务

## 一句话定义
现代 Web/API 多基于 REST 与 OData。理解模型，才能正确设计与测试接口安全：**REST 用资源+方法建模，OData 在其上加查询协议**；两者安全都归结为——鉴权、对象级授权、查询注入防护与最小字段暴露。

## 核心架构 / 工作原理

```mermaid
graph TD
  A[REST 核心] --> B[资源: 名词 URL (/books /books/123)]
  A --> C[方法: GET/POST/PUT/PATCH/DELETE 表达 CRUD]
  A --> D[无状态: 每请求带凭证，服务端不存会话上下文]
  A --> E[统一接口: 标准状态码/内容协商/超媒体(HATEOAS)]
  
  F[OData v2/v4 在 REST 之上] --> G[$metadata: 暴露实体模型/类型/导航属性]
  F --> H[$filter: 过滤 (Price lt 100, Category eq 'Book')]
  F --> I[$expand: 关联展开 (/Orders?$expand=Items)]
  F --> J[$select: 投影 (/Products?$select=Name,Price)]
  F --> K[$top/$skip/$orderby: 分页排序]
  F --> L[$count/$inlinecount: 总数]
  
  M[安全关注点] --> M1[越权/BOLA: 改 ID/查询条件访问他人数据]
  M --> M2[注入: $filter 拼接未校验输入 -> OData/后端注入]
  M --> M3[过度暴露: 默认返回全字段/关联数据]
  M --> M4[元数据泄露: $metadata 暴露模型，助攻击者构造请求]
```

| OData 查询选项 | 示例 | 风险 |
|----------------|------|------|
| `$filter` | `Price lt 100 and Category eq 'Book'` | 注入/越权/性能(全表扫描) |
| `$expand` | `/Orders?$expand=Items($expand=Product)` | 过度数据暴露/深度嵌套 DoS |
| `$select` | `/Users?$select=Id,Name,Email` | 字段级越权(若未授权过滤) |
| `$top/$skip` | `?$top=1000&$skip=0` | 大分页性能/枚举风险 |
| `$metadata` | `GET /odata/$metadata` | 模型泄露 → 构造精准攻击 |

## 快速上手步骤

1. **识别 OData 端点**：
   ```bash
   # 看 $metadata
   curl https://api.example.com/odata/$metadata
   # 看响应头
   curl -I https://api.example.com/odata/Products | grep -i "odata\|content-type"
   ```
2. **测试越权 (BOLA, WSTG APIT-03)**：
   ```bash
   # 改 ID 访问他人订单
   curl "https://api.example.com/odata/Orders(999)" -H "Authorization: Bearer <token>"
   # 改 $filter 越权
   curl "https://api.example.com/odata/Orders?$filter=CustomerId eq 'other-user'" -H "Authorization: Bearer <token>"
   ```
3. **测试注入**：
   ```bash
   # $filter 注入尝试 (视后端实现)
   curl "https://api.example.com/odata/Products?$filter=Name eq 'test' or 1=1" -H "Authorization: Bearer <token>"
   ```
4. **测试过度暴露**：
   ```bash
   # 默认返回全字段 vs $select 限制
   curl "https://api.example.com/odata/Users" -H "Authorization: Bearer <token>"
   curl "https://api.example.com/odata/Users?$select=Id,Name" -H "Authorization: Bearer <token>"
   # 看是否含密码哈希/内部 ID/敏感字段
   ```
5. **防御清单**：
   - ✅ 对象级授权：每请求校验"当前用户能否访问该资源/字段"
   - ✅ 查询注入防护：`$filter` 参数化/白名单/深度限制/复杂度限制
   - ✅ 最小字段暴露：默认 `$select` 必填字段；敏感字段默认不返回
   - ✅ 限制 `$expand` 深度/广度/循环检测
   - ✅ `$metadata` 仅内网/开发环境暴露，或需鉴权

```bash
# 快速测试 OData 安全
# 1. 枚举实体集
curl https://api.example.com/odata/$metadata | grep -oP 'EntitySet Name="\K[^"]+'

# 2. 测试各实体集越权/注入
for entity in Orders Products Users; do
  echo "Testing $entity..."
  curl "https://api.example.com/odata/$entity(999)" -H "Auth: Bearer <token>" -w "\n%{http_code}\n"
done
```

## 踩坑避坑指南

| 场景 | 问题现象 | 原因 | 解决/最佳实践 |
|------|----------|------|---------------|
| REST 无状态=不用管会话 | 鉴权令牌仍须每请求校验 | 误解无状态 | **无状态≠无鉴权**；每请求必带有效凭证(JWT/Token/Session) |
| OData 查询"内部用"就安全 | 未校验 $filter/$expand 权限 | 信任内部调用 | **服务端必须校验**：用户能否访问该实体/字段/关联；限制展开深度 |
| 关掉 $metadata 就安全 | 字段级越权/查询注入仍在 | 元数据只是辅助攻击 | **核心是授权逻辑**；$metadata 仅辅助攻击者构造请求 |
| 默认返回全字段 | 密码哈希/内部 ID/敏感字段泄露 | 无字段级授权/过滤 | **默认最小字段集**；敏感字段显式 opt-in；$select 强制指定 |
| $expand 无限制 | 深度嵌套导致 DoS/数据泄露 | 无深度/广度限制 | **限制展开层级(如 max 2 层)**；检测循环引用；配额限制 |

## 替代方案对比

| 维度 | REST + OData | GraphQL | gRPC | 传统 RPC |
|------|--------------|---------|------|----------|
| 查询灵活性 | OData 高/REST 低 | 极高(客户端定义) | 低(契约固定) | 低 |
| 类型安全 | OData 有 $metadata | Schema 强类型 | Protobuf 强类型 | 弱/无 |
| 越权风险 | 高(参数可控) | 高(字段级授权难) | 中(方法级授权) | 中 |
| 注入风险 | $filter/$expand 注入 | 查询注入/深度 DoS | 反序列化/参数校验 | 参数校验 |
| 适用场景 | 企业数据服务/ERP/CRM | 灵活前端/聚合查询 | 微服务内部/高性能 | 遗留/特定领域 |

---

> 参考来源：https://www.codecademy.com/article/what-is-rest · https://www.odata.org/documentation/odata-version-2-0/

*下一篇：[UI5/JavaScript 与 MVC 绑定安全](02-ui5与mvc.md)*