---
title: "OWASP WSTG 测试方法论"
parent: "Web 安全与开发基础实战知识库"
nav_order: 11
---

# 标准｜OWASP WSTG 测试方法论

Top 10 告诉你"测什么风险"，WSTG 告诉你"怎么系统地测"。本库已有完整的 [WSTG 知识库](../wstg/wstg.md)，这里做总览衔接。

## ① 是什么

**WSTG（Web Security Testing Guide）** 是 OWASP 的 Web/API 安全测试标准清单，按 12 个测试大类（信息收集→配置→身份→认证→授权→会话→输入→错误→密码学→逻辑→客户端→API）组织，每类下列具体测试项，并用 `WSTG-<类别>-<编号>` 标识。

## ② 为什么重要

- 它把"该测什么"固化成可复用的目录，避免凭感觉漏项。
- 与 Burp/ZAP 等工具互补：WSTG 定清单，工具做执行。

## ③ 核心概念拆解

- **12 大类（4.1–4.12）**：覆盖从侦察到 API 的完整面（详见 [WSTG 知识库](../wstg/wstg.md)）。
- **场景 ID 体系**：`WSTG-ATHN-01` 等，引用建议带版本如 `WSTG-v42-ATHN-01`。
- **与 Top 10 的关系**：Top 10 是风险优先级，WSTG 是验证这些风险的测试方法学——两者配合形成"定范围→逐项测→出报告"。
- **落地**：用 [Burp 知识库](../burp/burp.md) / [ZAP 知识库](../zap/zap.md) 执行具体测试手法。

## ④ 常见误区

- **误区 1**：WSTG 是书，照念即可。它是活清单，需按目标裁剪。
- **误区 2**：只跑扫描对照 ID。逻辑/业务项仍需人工。
- **误区 3**：与 Top 10 二选一。应"Top 10 排优先级 + WSTG 做验证"。

## ⑤ 一句话小结

WSTG 是 Web 安全测试的"标准清单与 ID 体系"，与 OWASP Top 10 互补：一个排优先级，一个做验证；配合工具落地。

*下一篇：REST 与 OData 服务*

> 参考来源：https://owasp.org/www-project-web-security-testing-guide/
