# 安全编码实践（Secure Coding Practices）

> 来源：Chapter 21 · Secure Coding Practices
> 域：Domain 8 Security and Risk Management（安全与风险管理）
> 模板：原书定义+对比表 / 真实案例 / 考试怎么考

## ① 一句话秒懂
再好的框架也挡不住老毛病：**注释泄密、verbose 报错、硬编码密码、内存管理差**——安全编码就是把这些"随手坑"提前堵上。

## ② 原书核心定义 + 对比表

**四大安全编码要点**：

| 要点 | 风险 | 正确做法 |
|---|---|---|
| 源码注释 Comments | 暴露设计/密钥 | 生产版移除非必要注释（编译型自动去；Web 暴露型须手动删） |
| 错误处理 Error Handling | 详错泄结构 / 整数溢出 | try…catch；最少信息给用户、最多记日志 |
| 硬编码凭证 Hard-coded Credentials | 后门 / 公开仓库泄密 | 禁硬编码；API key 勿入公共 repo |
| 内存管理 Memory | 资源耗尽 / 溢出 | 边界检查；防 resource exhaustion |

**错误处理两难**：不当处理（如除法未防 0）会崩；但**过度 verbose** 报错（暴露 SQL 查询、MySQL 引擎）给攻击者递刀——黄金准则：给用户最少必要信息，给日志最多信息。

**防御纵深**：输入校验是第一道，错误处理是第二道（校验自身可能有 flaw）。

## ③ 生活类比（精炼）
注释像施工图纸——给内部人看没问题，但挂网上等于给小偷画地图。硬编码密码像把大门钥匙焊在门上写着"备用"。verbose 报错像陌生人问路你连保险柜位置都说了。

## ④ 真实案例
- **公开仓库泄露 API key**：开发者把含 AWS API key 的代码推到 GitHub，机器人秒扫到，用你的信用卡开海量资源——务必密钥出仓即轮换。
- **法语网站 SQL 错误泄露**：错误页直接显示 SQL 查询与 MySQL 引擎，攻击者据此构造注入——例证"详错即漏洞"。

## ⑤ 相关概念梳理 + 对比表

**Integer Overflow**：输入 50000 位整数试图触发整数溢出——开发者须 anticipate 意外输入。

**try…catch 示例**（Java）：`try { quotient = numerator/denominator; } catch (ArithmeticException e) { ... }` 安全处理除零。

**Resource Exhaustion**：内存/有限资源被有意无意耗尽，须防。

**Dead Code**：无人维护、不知源码所在的在用代码——代码仓库（repo）可避免此问题，兼做版本控制与审计。

## ⑥ 考试怎么考（题干样式 + 常见混淆项）
- 题干："Exposing SQL query details in an error message is a risk because it enables?" → 答 **SQL injection / reconnaissance**。混淆：不是直接漏洞而是辅助。
- 题干："Storing API keys or passwords directly in source code is called?" → 答 **Hard-coded credentials**。混淆：与 backdoor 相关但特指凭证写死。
- 题干："Error messages should display ___ to users and log ___?" → 答 **minimum necessary / maximum detail**。混淆：verbose 给用户是风险。
- 题干："Removing comments from production web code prevents?" → 答 **attackers mapping the code（注释泄密）**。

## ⑦ 自测（改编自原书 Review Questions，附解析）
1. 关于错误处理，正确的是？
   - A. 报错越详细给用户越好
   - B. 给用户最少必要信息、给日志最多信息
   - C. 不需要 try…catch
   - D. 详错可防注入
   - **答案：B**。解析：黄金准则——用户看最少、日志记最多；verbose 报错反而助攻击。

2. 把密码或 API key 直接写进源代码，称为？
   - A. 后门
   - B. 硬编码凭证
   - C. 令牌化
   - D. 代码签名
   - **答案：B**。解析：hard-coded credentials 含维护账号后门或第三方凭证，公开仓库泄露是常见事故。

3. 为何生产环境 Web 代码应移除注释？
   - A. 减小体积
   - B. 防攻击者借注释地图理解代码/泄密
   - C. 提升性能
   - D. 编译器要求
   - **答案：B**。解析：暴露型代码（如 Web）的注释可能含安全细节，须部署前移除；编译型自动去注释。
