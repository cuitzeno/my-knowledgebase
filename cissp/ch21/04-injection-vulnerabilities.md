---
title: "注入漏洞全解（Injection: SQL/LDAP/Command/Code）"
parent: 第 21 章 · 恶意代码与应用攻击
grand_parent: CISSP 认证安全工程师知识库
nav_order: 4
---

# 注入漏洞全解（Injection: SQL/LDAP/Command/Code）

> 来源：Chapter 21 · Injection Vulnerabilities
> 域：Domain 8 Security and Risk Management（安全与风险管理）
> 模板：原书定义+对比表 / 真实案例 / 考试怎么考

## ① 一句话秒懂
把用户输入当"代码"执行——最经典是 **SQL 注入**：在搜索框里塞进分号+第二条查询，数据库乖乖吐出信用卡号。

## ② 原书核心定义 + 对比表

**注入家族**：SQL / LDAP / XML / Command / HTML / Code / File injection。本质是"把攻击者代码掺进合法代码"。

**SQL 注入示例**：输入 `orange'; SELECT CustomerName, CreditCardNumber FROM Orders; --` → 数据库执行两条查询，泄露客户卡号。

**盲注（Blind SQLi）两类**：

| 类型 | 信道 | 例子 |
|---|---|---|
| Content-based（基于内容） | 页面返回有无结果 | `52019' OR 1=1;--` 看是否返回全部 |
| Timing-based（基于时序） | 响应延迟 | `WAITFOR DELAY '00:00:15'` 看是否延迟 15 秒 |

**Command Injection 例**：输入 `mchapple & rm -rf /home` → 系统执行两条命令，删光 home 目录（& 分隔命令）。

## ③ 生活类比（精炼）
SQL 注入像在"点菜单"里夹带"把保险柜也打开"的指令，厨房（数据库）照做。盲注像问暗号：回答"有/无"或"等 15 秒"来逐位套密码。命令注入像在"建文件夹"指令后偷偷加"顺便删光硬盘"。

## ④ 真实案例
- **电商搜索框 SQLi**：正常搜 `orange tiger pillow`，攻击者追加 `'; SELECT ... FROM Orders; --` 直接拖库。
- **定时盲注拖密码**：用 `WAITFOR DELAY` 逐字符比对，自动化工具（sqlmap / Metasploit）让这种攻击变简单。
- **命令注入删目录**：Linux `system('mkdir ... & rm -rf /home')` 借 & 执行额外破坏命令。

## ⑤ 相关概念梳理 + 对比表

**防御核心**：输入校验（whitelist）+ 转义（escaping）+ 参数化查询（parameterized queries）/ 存储过程（stored procedures）。

**其他注入**：LDAP 注入（后端目录服务）、XML 注入（后端 XML 应用）、DLL 注入（加载恶意动态库）、XSS（插脚本到页面，详见下篇）。

**`--` 注释技巧**：注入时末尾加 `--` 注释掉模板里残留的单引号，避免语法错暴露攻击。

## ⑥ 考试怎么考（题干样式 + 常见混淆项）
- 题干："Injecting `OR 1=1` and observing whether all rows return is?" → 答 **Content-based blind SQLi**。混淆：Timing-based 看延迟。
- 题干："Using `WAITFOR DELAY` to extract data character-by-character is?" → 答 **Timing-based blind SQLi**。
- 题干："Input `& rm -rf /home` executed as extra OS command is?" → 答 **Command injection**。混淆：非 SQL 注入（目标是 OS）。
- 题干："Best defense against SQL injection?" → 答 **Parameterized queries / input validation + escaping**。

## ⑦ 自测（改编自原书 Review Questions，附解析）
1. 攻击者用 `52019' OR 1=1;--` 看页面是否返回全部记录来判断漏洞，属于？
   - A. 定时盲注
   - B. 基于内容的盲注
   - C. 普通 SQL 注入（可见结果）
   - D. 命令注入
   - **答案：B**。解析：无法直看结果时，用返回"有无"来探漏洞即 content-based blind。

2. 利用数据库 `WAITFOR DELAY` 让响应延迟以逐位窃取数据，是？
   - A. 基于内容的盲注
   - B. 基于时序的盲注
   - C. LDAP 注入
   - D. XSS
   - **答案：B**。解析：timing-based blind SQLi 借延迟作信道提取信息。

3. 输入 `name & rm -rf /home` 让系统额外执行删除命令，属于？
   - A. SQL 注入
   - B. 命令注入
   - C. XML 注入
   - D. 目录遍历
   - **答案：B**。解析：应用把用户输入拼进 OS 命令，& 分隔出恶意第二条命令，即 command injection。
