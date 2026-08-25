---
title: 数据库与数据仓库安全（Databases, Data Warehousing & Security）
parent: 第 20 章
grand_parent: CISSP 认证安全工程师知识库
nav_order: 2
---

# 数据库与数据仓库安全（Databases, Data Warehousing & Security）

> 来源：Chapter 20 · Establishing Databases and Data Warehousing
> 域：Domain 8 Security and Risk Management（安全与风险管理）
> 模板：原书定义+对比表 / 真实案例 / 考试怎么考

## ① 一句话秒懂
数据库是组织的"金库"，安全重点不只是锁门，还要防人用**聚合（aggregation）**和**推理（inference）**把低密级信息拼出高密级秘密。

## ② 原书核心定义 + 对比表

**关系型数据库（RDBMS）基本结构**：表（table/relation）= 行（record/tuple）+ 列（field/attribute）。基数（cardinality）= 行数；度（degree）= 列数。

**四类键（Keys）**：

| 键 | 定义 | 数量 |
|---|---|---|
| Candidate（候选键） | 能唯一标识记录的最小属性集 | 一个或多个 |
| Primary（主键） | 从候选键中选定的唯一标识 | 每表仅一个 |
| Alternate（候补键） | 未被选为主键的候选键 | 零或多个 |
| Foreign（外键） | 引用另一表主键，保证参照完整性 | 多对一关系 |

**ACID 事务四特性**：Atomicity（原子性，全或无）/ Consistency（一致性）/ Isolation（隔离性）/ Durability（持久性）。

**多级安全与防推断机制**：

| 概念 | 含义 | 防御 |
|---|---|---|
| Aggregation | 汇集大量低价值项合成高价值信息 | 严格控制聚合函数权限 |
| Inference | 用人类演绎从非敏感信息推敏感信息 | 数据模糊化、分区 |
| Polyinstantiation | 同一主键存不同密级副本 | 防推理，但增存储成本 |
| Covert storage channel | 借共享存储媒介跨密级传数据 | 隐蔽通道分析 |

## ③ 生活类比（精炼）
Aggregation 像拼图：单片（调职记录）不涉密，但拼出"各基地兵力"就是军事秘密。Inference 像会计：能看某天总薪资，又知道某人唯一那天入职，就能反推出他个人工资。Polyinstantiation 像"善意的谎言"：对秘密权限者说真位置，对普通权限者说"在例行巡逻"。

## ④ 真实案例
- **军事记录员聚合攻击**：低级别文员有更新调职记录权限，却能用聚合函数数出各基地驻军数（本属机密）——说明需严格控聚合函数。
- **会计推理攻击**：能查历史任意一天总薪资 + 知雇佣/离职日期，即可推断某员工个人薪资（本无权限直看）。

## ⑤ 相关概念梳理 + 对比表

**并发控制（Concurrency）**防两类问题：Lost Updates（两进程同时改，互相覆盖）/ Dirty Reads（读了未提交事务的中间错误值）。用锁（lock/unlock）机制解决。

**数据库架构类型**：层级（hierarchical，树形一对多）/ 分布式（distributed，多对多逻辑统一）/ 关系型（relational，主流）/ 对象关系 / NoSQL（键值/图/文档存储）。

**其他安全机制**：视图（views，限制用户只见子集）、单元格抑制（cell suppression）、内容依赖/上下文依赖访问控制、ODBC（异构库统一接口）、噪声与扰动（noise & perturbation）。

## ⑥ 考试怎么考（题干样式 + 常见混淆项）
- 题干："Combining many low-level records to deduce classified totals is?" → 答 **Aggregation**。混淆：Inference 靠人脑演绎而非数学聚合。
- 题干："Two records with same primary key but different data at different clearance levels?" → 答 **Polyinstantiation**。混淆：它不是普通重复，是刻意防推理。
- 题干："A transaction must be all-or-nothing. This is?" → 答 **Atomicity**。混淆：Isolation 是事务间互不干扰。
- 题干："Preventing a user from reading partially committed data is the role of?" → 答 **Isolation / Concurrency control**。

## ⑦ 自测（改编自原书 Review Questions，附解析）
1. 下列哪种攻击通过数学聚合低密级数据得到高密级信息？
   - A. Inference
   - B. Aggregation
   - C. Polyinstantiation
   - D. Covert channel
   - **答案：B**。解析：aggregation 用聚合函数汇集低价值项合成高价值；inference 依赖人的演绎。

2. 关系数据库中用于保证参照完整性的是？
   - A. 主键
   - B. 外键
   - C. 候选键
   - D. 交替键
   - **答案：B**。解析：外键引用另一表主键，确保无悬空引用，即参照完整性。

3. 同一主键为不同密级存不同数据以对抗推理攻击，称为？
   - A. 视图
   - B. 多实例化 Polyinstantiation
   - C. 噪声
   - D. 单元格抑制
   - **答案：B**。解析：polyinstantiation 是同主键多副本，按权限返回不同内容，代价是额外存储。
