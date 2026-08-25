---
title: Ch9-02 计算机硬件架构：CPU、执行类型、保护环与进程状态
parent: 第 9 章
grand_parent: CISSP 认证安全工程师知识库
nav_order: 2
---

# Ch9-02 计算机硬件架构：CPU、执行类型、保护环与进程状态

> 所属域：Domain 3 Security Architecture and Engineering
> 对应原书：Chapter 9 — Hardware / Processor / Execution Types / Protection Rings / Process States

## ① 一句话秒懂
系统的最底层是硬件与 CPU。理解**多任务/多核/多线程**的区别、**保护环（ring 0 最高特权）**和**进程状态机**，才能明白 OS 如何用特权隔离保护自身。

## ② 生活类比
保护环像一栋办公楼：最里面的核心机房（ring 0）权限最高，能碰所有设备；最外层的访客（ring 3 / 用户态）只能在前台活动，要进机房得先"申请"（系统调用）。

## ③ 核心概念（大白话 + 原书定义）

**硬件（Hardware）**
任何可触摸的有形部分：键盘、显示器、CPU、存储介质、内存芯片。注意：硬盘是硬件，但里面的 0/1 内容属于软件/数据。

**CPU（处理器）**
计算机"神经中枢"，只执行有限的运算/逻辑操作（靠 OS、编译器把高级语言翻译成简单指令）。功能有限是刻意的，为了极速。

**五种"同时做事"的执行类型（极易混）**
- **Multitasking（多任务）**：同时处理多个任务；单核系统靠 OS 快速切换"伪同时"（像杂耍三球，手同一刻只碰一个）。
- **Multicore（多核）**：一个 CPU 内含多个独立执行核，真正同时运行（常见 2/4/8 核，甚至上万核）。
- **Multiprocessing（多处理）**：多颗处理器协同完成多线程应用；把某进程/线程绑定到特定 CPU 叫 **affinity（亲和性）**。
- **Multiprogramming（多道程序）**：单处理器上伪同时执行，靠 OS 批处理/序列化，某进程等 I/O 时换下一个。
- **Multithreading（多线程）**：在**单个进程内**并发执行多个任务；线程是父进程内的指令序列，切换开销比进程小、更高效。

**保护环（Protection Rings）**
把 OS 代码/组件按特权分层（同心圆）。越靠内特权越高。Multics 曾用 7 环（0–6），现代 OS 多用 4 环（0–3）：
- **Ring 0（内核态/特权态）**：内核常驻内存，可访问任何资源，能抢占其他环的代码。
- **Ring 1**：OS 其余常变部分。
- **Ring 2**：I/O 驱动、系统工具（能访问外设/特殊文件）。
- **Ring 3（用户态）**：应用程序，特权最低，需通过系统调用（mediated-access）请低层帮忙。
- 实践中许多 OS 只用两态：ring 0–2 合称内核态，ring 3 即用户态。

**进程状态（Process States）**
OS 任一刻处于两模式之一：
- **Supervisor / Kernel mode（特权态）**：全权访问。
- **Problem / User mode（问题态）**：权限低，每次访问须校验凭证。
进程生命期状态：Ready（就绪）→ Running（运行，耗尽时间片 time slice 或被 I/O 阻塞则回 Ready/Waiting）→ Waiting（等 I/O）→（高特权时 Supervisory）→ Stopped（结束/终止，回收资源）。

> 原书提醒：**系统越复杂，提供的保证（assurance）越低**——复杂度 = 更多漏洞面 = 更难信任。呼应 Ch8 的 KISS。

## ④ 真实案例
- 缓冲区溢出利用常试图从用户态（ring 3）提权到内核态（ring 0）——保护环正是为挡住这种越界。
- 现代 CPU 侧信道（如 Spectre/Meltdown）正是利用推测执行跨特权边界泄露数据，说明硬件层隔离并非绝对。

## ⑤ 考试怎么考
- 五个"multi-"词的区别（尤其 multitasking vs multithreading vs multiprocessing）。
- Ring 0 = 最高特权 = 内核；ring 3 = 用户态；系统调用是低环请求高环服务。
- Supervisor/Kernel mode vs Problem/User mode 对应特权态/用户态。
- 复杂度↑ → assurance↓ 是常考结论。

## ⑥ 记忆口诀
- 多任务单核切，多核真同时；多处理多 CPU，多线程在一程。
- Ring 0 是内核最高权，Ring 3 是用户最外面；要进内核先系统调用。
- 越复杂越不可信（assurance 越低）。

## ⑦ 自测
1. Multitasking 与 Multithreading 的本质区别？（多进程 vs 单进程内多线程）
2. 保护环中 ring 0 与 ring 3 分别是什么态？用户态程序如何访问内核资源？
3. 进程从 Running 到 Waiting 通常因为什么事件？
4. 为什么"系统越复杂，assurance 越低"？
