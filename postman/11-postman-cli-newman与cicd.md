---
title: "Postman CLI / Newman 与 CI/CD 自动化"
parent: "Postman 接口测试实战知识库"
nav_order: 11
---

# Postman 实战｜Postman CLI / Newman 与 CI/CD 自动化

把集合留在自己电脑上跑，等于没测。这篇讲用命令行把集合搬进 CI/CD，每次提交自动跑测试。

## ① 是什么

- **Newman**：Postman 集合的命令行运行器，可在任意机器/流水线里跑。
- **Postman CLI**：官方新版命令行，体验和界面一致，还能跑云同步的集合。
- **CI/CD**：提交代码 → 自动构建 → 自动跑 API 测试 → 失败则拦下。

## ② 为什么重要

- 手动跑测试会忘、会偷懒；放进流水线才能"每次改动都回归"。
- 测试左移进 CI，Bug 在合并前就爆出来，修复成本最低。

## ③ 核心概念拆解

- **本地用 Newman**：`newman run collection.json -e env.json` 跑集合；可加 `--reporters cli,json` 出报告。
- **Postman CLI 运行集合**：登录后选集合直接跑，支持最新特性。
- **接 GitHub Actions**：
  - 建 `.github/workflows/api-tests.yml`。
  - 步骤：拉代码 → 装 Node/Newman → `newman run` 集合。
  - 每次 push/PR 触发，失败则标红、阻断合并。
- **接 Jenkins**：装 Newman 插件 → 建 Pipeline → 定时或事件触发。

## ④ 常见误区

- **误区 1**：只在本地跑过就算有测试。没进 CI，等于没保障。
- **误区 2**：集合文件不入库。应把集合/环境导出进仓库，流水线才能复现。
- **误区 3**：环境密钥写死在文件。用 CI 的 Secrets 注入，别提交真实 token。

## ⑤ 一句话小结

Newman/Postman CLI 把集合搬进 GitHub Actions、Jenkins，API 测试随每次提交自动回归。

*下一篇：API 文档自动生成与发布*

> 参考来源：*Mastering Postman, Second Edition*（本文为原创讲解，非转载原文）
