---
title: 应用层攻击：缓冲区溢出、TOC/TOU、后门、提权（Application Attacks）
parent: 第 21 章 · 恶意代码与应用攻击
grand_parent: CISSP 认证安全工程师知识库
nav_order: 3
---

# 应用层攻击：缓冲区溢出、TOC/TOU、后门、提权（Application Attacks）

> 来源：Chapter 21 · Application Attacks
> 域：Domain 8 Security and Risk Management（安全与风险管理）
> 模板：原书定义+对比表 / 真实案例 / 考试怎么考

## ① 一句话秒懂
糟糕的编码留下"门缝"：输入不校验 → 缓冲区溢出；检查与使用的空档 → 竞态；留后门 → 绕过认证；拿到普通账号 → 提权成管理员。

## ② 原书核心定义 + 对比表

**四类应用攻击**：

| 攻击 | 成因 | 后果 |
|---|---|---|
| Buffer Overflow（缓冲区溢出） | 未校验输入长度，写入越界内存 | 崩溃 / 执行攻击者命令 |
| TOC/TOU（检查-使用竞态） | 检查与使用间被替换对象 | 用伪对象骗过程；race condition |
| Backdoor（后门） | 未文档化的命令序列 | 绕过访问控制 |
| Privilege Escalation（提权） | rootkit 等提普通→管理员 | 全面控制 |

**缓冲区溢出三必查**：① 输入不超缓冲区大小；② 类型合法（字母不进数字变量）；③ 不越参数范围。多数靠补丁缓解 → 系统及时更新至关重要。

**TOC/TOU 别名**：TOCTTOU / race condition；归为"状态攻击（state attacks）"——攻击时序与状态转换。

## ③ 生活类比（精炼）
缓冲区溢出像小盒子塞进大物件，挤坏隔壁；TOC/TOU 像验完身份证、进门前一瞬被换人（你和门卫的空档被钻）；后门像开发商偷偷留的"万能钥匙"；提权像从普通员工卡刷成老板权限。

## ④ 真实案例
- **CGI 快速 Web 开发**：用 CGI 等语言赶工，程序员常不做边界检查 → 缓冲区溢出高发，凸显"及时打补丁"价值。
- **Siemens 逻辑炸弹（2019）**：承包商在软件埋逻辑炸弹，定期让系统坏，逼公司回雇他——虽非本小节但说明恶意开发风险；提权/后门同理需防。

## ⑤ 相关概念梳理 + 对比表

**Rootkit**：利用已知 OS 漏洞，把普通用户一提成为 root/admin；自由可得。

**Fileless malware / 恶意脚本**：PowerShell/Bash 脚本自动化提权与 C2 接入，常无文件落地。

**防御核心**：开发者须对一切用户输入做边界检查；保持补丁更新可挡几乎全部 rootkit。

## ⑥ 考试怎么考（题干样式 + 常见混淆项）
- 题干："Attack exploiting gap between check and use of a resource?" → 答 **TOC/TOU (race condition)**。混淆：不是 buffer overflow。
- 题干："Undocumented command sequence bypassing access controls?" → 答 **Backdoor**。混淆：与 logic bomb 不同，backdoor 是访问旁路。
- 题干："Overflow caused by not validating input length is?" → 答 **Buffer overflow**。混淆：常需补丁缓解。
- 题干："Gaining admin from standard account via rootkit is?" → 答 **Privilege escalation**。

## ⑦ 自测（改编自原书 Review Questions，附解析）
1. 检查资源状态与真正使用之间被攻击者替换对象，称为？
   - A. 缓冲区溢出
   - B. TOC/TOU 竞态条件
   - C. 后门
   - D. 提权
   - **答案：B**。解析：time-of-check to time-of-use，又称 race condition / 状态攻击。

2. 未文档化的命令序列可绕过正常访问控制，这是？
   - A. 逻辑炸弹
   - B. 后门
   - C. 蠕虫
   - D. rootkit
   - **答案：B**。解析：backdoor 是隐秘访问旁路；rootkit 是提权工具，非同概念。

3. 防范缓冲区溢出的首要开发措施是？
   - A. 关闭网络
   - B. 对所有用户输入做边界/类型校验
   - C. 仅用解释型语言
   - D. 删除日志
   - **答案：B**。解析：开发者须确保输入不超缓冲、类型合法、不越参；多数溢出靠补丁缓解。
