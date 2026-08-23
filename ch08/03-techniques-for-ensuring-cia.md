# Ch8-03 保障 CIA 的技术：限制、边界、隔离

> 所属域：Domain 3 Security Architecture and Engineering
> 对应原书：Chapter 8 — Techniques for Ensuring CIA

## ① 一句话秒懂
用"**限制（confinement）+ 边界（bounds）+ 隔离（isolation）**"三件套把程序关进笼子，保证它只做该做的、一旦出事只影响自己。

## ② 生活类比
化工厂把危险反应釜放在独立防爆间（**隔离**），反应釜只能接触指定管道和原料（**边界**），且被监控不得越界（**限制**）。一个釜爆炸不会殃及全厂。

## ③ 核心概念（大白话 + 原书定义）

**限制（Confinement / Sandboxing）**
进程只能读写特定内存和资源，是把**最小权限原则**应用到进程上。由 OS（进程隔离、内存保护）、沙箱应用（如 Sandboxie）或虚拟化 / 虚拟机监控器（如 VMware、VirtualBox）实现。越界请求被拒，并可能终止 + 记录日志。目标是防止数据泄露给未授权程序 / 用户 / 系统。

**边界（Bounds）**
给进程分配**权限级别（authority level）**，如简单的 user / kernel 两层。边界限定其可访问的内存地址与资源，即"被限制的区域"。
- 逻辑边界（logical bounds）：同内存空间内分段，常见。
- 物理边界（physical bounds）：真正物理隔离不同进程的内存，更安全但昂贵。

**隔离（Isolation）**
通过强制边界，使进程独立运行——任何行为只影响自身内存与资源。是稳定 OS 的关键，支撑 fail-soft（一个进程崩溃不影响其他）。

**三者关系**
- Confinement = 只能访问**特定资源**（如内存）。
- Bounds = 限制授权的**范围**与交互类型。
- Isolation = 用 bounds **实现** confinement 的手段。
- 共同目标：预定资源访问范围不被违反；单进程失败 / 沦陷对其他进程影响最小。

**访问控制（Access Controls）**
限制主体对客体的访问（DAC / RBAC / MAC），详见 Chapter 14。

**信任与保证（Trust & Assurance）**
- 信任（Trust）= 存在安全机制 / 功能 / 能力。
- 保证（Assurance）= 对该机制在真实场景可靠性的**信心程度**。
- 保证需持续维护（变更管理、补丁管理、配置管理）。**"变更常是安全的对立面"**——vendor 补丁或恶意 exploit 都会改变系统，故需重新验证。

## ④ 真实案例
- **浏览器沙箱**：每个标签页 / 网站放在独立沙箱进程，恶意网站想读密码被隔离挡住。
- **内存越界读取（如 Heartbleed 类）**：正是 bounds / confinement 失效的后果，能跨进程偷数据。

## ⑤ 考试怎么考
- confinement / bounds / isolation 三者**定义与关系**，常为连线或排序题。
- 逻辑边界 vs 物理边界的区别与代价（物理更安全但贵）。
- trust vs assurance 的区别（存在机制 vs 信心程度）。
- isolation 与 fail-soft 的支撑关系。

## ⑥ 记忆口诀
- 限制管资源，边界定范围，隔离靠边界，崩了不连累。
- 信任是机制，保证是信心；变更常削弱，管理要跟进。

## ⑦ 自测
1. Confinement、Bounds、Isolation 分别指什么？它们如何互相支撑？
2. 逻辑边界与物理边界在安全强度和成本上有何差异？
3. Trust 和 Assurance 的本质区别是什么？
4. 为什么"变更管理"对维持 Assurance 至关重要？
