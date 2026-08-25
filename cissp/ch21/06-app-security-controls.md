# 应用安全控制：输入校验、WAF、参数化查询（Application Security Controls）

> 来源：Chapter 21 · Application Security Controls
> 域：Domain 8 Security and Risk Management（安全与风险管理）
> 模板：原书定义+对比表 / 真实案例 / 考试怎么考

## ① 一句话秒懂
防应用攻击靠"纵深"：**白名单输入校验 + 转义 + 参数化查询**打底，WAF 在前方再拦一层，数据库用令牌化/哈希护敏感数据。

## ② 原书核心定义 + 对比表

**输入校验两策略**：

| 策略 | 做法 | 适用 |
|---|---|---|
| Whitelisting（白名单/允许列表） | 描述期望的精确输入并校验 | 年龄（0–123 整数）等规则明确字段 |
| Blacklisting（黑名单/阻止列表） | 描述须阻断的恶意输入 | 分类广告等难定规则字段 |

**关键原则**：输入校验**必须在服务端**（server-side），客户端校验易被绕过。

**参数污染（Parameter Pollution）**：同一变量发两个值（如 `account=12345&account=12345'OR 1=1`），利用平台只校验第一个、执行第二个的缺陷绕过过滤。

**WAF（Web 应用防火墙）**：工作于 OSI 应用层，坐镇 Web 服务器前，对输入做白/黑名单校验，恶意流量不到服务器。

**数据库防护**：参数化查询（Parameterized queries，Java `PreparedStatement` / PHP `bindParam`）/ 存储过程（stored procedures，SQL 存于服务端）；数据模糊化：数据最小化 / 令牌化（tokenization）/ 哈希加盐（抗彩虹表）。

## ③ 生活类比（精炼）
白名单像"只放行持邀请函者"；黑名单像"拉黑已知坏人但漏新面孔"。WAF 像小区门卫在楼前再查一遍。参数化查询像"填空模板"——用户填的只是参数，塞不进 SQL 结构。参数污染像交两份表格，门卫查第一份、执行第二份的漏洞。

## ④ 真实案例
- **令牌化保护标识**：学生 ID 换随机 10 位数 +  lookup 表，泄露也难反推身份（需保护好 lookup 表）。
- **哈希加盐抗彩虹表**：敏感标识经加盐哈希不可逆，即使库泄也难还原。
- **数据最小化**：不收集不需要的敏感信息、到期即销毁——"没有的信息不会丢"。

## ⑤ 相关概念梳理 + 对比表

**元字符（Metacharacters）**：具特殊程序含义的字符（`' " [ ] \ ; & ^ $ . | ? * + { } ( )`）；转义（escaping，如 `\&`）可剥夺其特殊能力。

**代码安全**：代码签名（code signing，私钥签、公钥证验，但**不保证代码无恶意**）、代码复用（library/SDK/外包须同测）、软件多样性（避免单点依赖）、代码仓库（version control + 审计）、完整性度量（哈希校验投产代码 = 批准代码）。

**应用弹性**：可扩展性（scalability：垂直 scaling up / 水平 scaling out）/ 弹性（elasticity：自动伸缩降本）——云核心卖点。

## ⑥ 考试怎么考（题干样式 + 常见混淆项）
- 题干："Describing exact expected input and rejecting all else is?" → 答 **Input whitelisting**。混淆：blacklisting 只封已知恶意。
- 题干："WAF operates at which OSI layer?" → 答 **Application layer（应用层）**。混淆：非网络层（那是普通防火墙）。
- 题干："Using a prepared statement with bound variables to prevent injection is?" → 答 **Parameterized query**。混淆：stored procedure 是 SQL 存服务端。
- 题干："Code signing guarantees the code is?" → 答 **authentic & unmodified（来源真且未改），但不保证无恶意**。混淆：签名不审内容。

## ⑦ 自测（改编自原书 Review Questions，附解析）
1. 最有效的输入校验方式是？
   - A. 黑名单
   - B. 白名单（允许列表）
   - C. 完全不校验
   - D. 仅客户端校验
   - **答案：B**。解析：白名单明确期望输入并校验，优于只封已知的黑名单；且校验须服务端。

2. 关于代码签名，正确的是？
   - A. 保证代码无恶意
   - B. 保证来源真实且未被篡改，但不保证无恶意
   - C. 替代输入校验
   - D. 仅用于开源
   - **答案：B**。解析：code signing 验来源与完整性，但开发者若签恶意代码也能通过验证。

3. 应用层、坐镇 Web 服务器前拦截恶意输入的防护是？
   - A. 网络防火墙
   - B. WAF
   - C. IDS
   - D. VPN
   - **答案：B**。解析：WAF 工作于 OSI 应用层，在流量到 Web 服务器前做输入校验。
