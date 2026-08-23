# ① 一句话秒懂

软件测试（Software Testing）就是在代码上线前，用"静态查、动态跑、乱输入、测接口、防滥用"等一整套手段，把程序里的后门和 Bug 提前揪出来——毕竟软件天生拿着高权限、处理敏感数据。

# ② 生活类比

把软件想象成一辆出厂前的汽车：
- **代码审查（Code Review）** = 老师傅逐零件检查装配。
- **静态测试（SAST）** = 不发动引擎，光看图纸和零件找设计缺陷。
- **动态测试（DAST）** = 真把车开上赛道跑一圈看会不会抛锚。
- **模糊测试（Fuzz）** = 往油箱乱加奇怪燃料，看发动机会不会爆。
- **接口测试** = 检查各部件之间的"接头"是否严丝合缝。
- **误用案例测试** = 故意按错误方式操作，看车会不会被骗着失灵。

# ③ 核心概念

## 核心设计原则：永远别信用户
软件不应依赖用户"行为正确"，而要预期意外、优雅处理非法输入、乱序操作——这个过程叫 **Exception Handling（异常处理）**。

## 代码审查（Code Review / Peer Review）
开发之外的人审查代码缺陷。最严谨的是 **Fagan Inspection（范根检查）**，六步：Planning → Overview → Preparation → Inspection → Rework → Follow-up，每步有严格进入/退出标准。多数组织用轻量方式：走查（walkthrough）、资深开发签字、自动化工具辅助。

## 静态与动态测试
- **SAST（Static Application Security Testing）**：不运行代码，分析源码或编译产物找缓冲区溢出等缺陷。开发全程可用。
- **DAST（Dynamic Application Security Testing）**：在运行环境测，常是没源码时的唯一选择（如 Web 应用扫描 XSS/SQL 注入）。生产环境跑 DAST 须谨慎协调避免中断。

补充概念：
- **IAST（Interactive AST）**：实时分析运行时行为、HTTP 流量、组件连接。
- **RASP（Runtime Application Self-Protection）**：跑在服务器上，拦截并校验进出应用的调用。
- **Synthetic Transactions（合成事务）**：带已知预期结果的脚本化交易，对比输出找偏差。
- **Benchmarks（基准）**：预定义性能基线（响应时间、吞吐、错误率、资源占用）。

## 模糊测试（Fuzz Testing）
向软件灌入大量非法/畸形输入，监控崩溃、溢出。两类：
- **Mutation（Dumb）Fuzzing**：基于真实输入做变异（如 bit flipping 比特翻转），工具如 `zzuf`。
- **Generational（Intelligent）Fuzzing**：先建数据模型，按程序数据类型智能生成输入。
局限：覆盖率不全，难测复杂业务逻辑漏洞。

## 接口测试（四类接口）
- **API**：模块间标准交互，须验证安全需求。
- **UI**（GUI/CLI）：终端用户交互界面。
- **Network**：LAN/WAN/Internet 通信网关，验证连接健壮性、加密、认证、错误处理。
- **Physical**：操控机械/控制器的物理接口，失败后果严重须重点测。

## 误用案例测试（Misuse/Abuse Case Testing）
枚举已知滥用场景（如尝试访问他人账户、超额取款），再手动/自动尝试利用。

## 测试覆盖率分析（Test Coverage Analysis）
不可能 100% 测全。常用五类覆盖标准：
- **Branch（分支）**：每个 if 的 true/false 都跑过。
- **Condition（条件）**：每个逻辑判断在所有输入组合下都执行。
- **Function（函数）**：每个函数被调用并返回。
- **Loop（循环）**：循环跑多次/一次/零次。
- **Statement（语句）**：每行代码被执行。

## 网站监控（两种）
- **Passive（被动/RUM）**：抓取真实用户流量，出问题后才发现，利于排障。
- **Synthetic（主动）**：发假交易测性能，能在问题发生前发现。
两者常结合使用。

## 伦理披露（Ethical Disclosure）
发现第三方产品漏洞时，应先** privately 报告厂商**给其修补时间，超时未修再公开披露，让同业知情。

# ④ 真实案例

银行软件测试人员用**误用案例测试**，专门模拟"用户篡改输入字符串试图访问他人账户""从已透支账户提款"等场景，提前堵住业务逻辑漏洞——这类漏洞模糊测试和简单扫描往往抓不到，必须靠针对性的滥用建模。

# ⑤ 考试怎么考

- **SAST vs DAST**：是否运行代码（静态不跑、动态跑）。
- **Fagan Inspection 六步**、以及它是"最正式"的代码审查。
- **Fuzz 两类**：Mutation（变异/傻糊）vs Generational（生成/智能）。
- 四种接口（API/UI/Network/Physical）及各自测试重点。
- 五类覆盖率（Branch/Condition/Function/Loop/Statement）含义。
- **IAST / RASP** 定义。
- 伦理披露：先私报厂商，给合理修补期，再公开。

# ⑥ 记忆口诀

> **"静不跑动跑，Fagan 六步严；模糊两派变与智，四口 API 网物界面；覆盖五标分支条，伦理先私后公开。"**

- SAST 静态不运行、DAST 动态运行。
- 模糊：变异（mutation）与生成（generational）。
- 四接口：API、UI、网络、物理。
- 覆盖五标：分支、条件、函数、循环、语句。

# ⑦ 自测

1. SAST 与 DAST 的根本区别是什么？没有源码时通常用哪种？
2. Fagan Inspection 的六个步骤是什么？它属于代码审查的哪种级别？
3. 模糊测试分为哪两类？各有什么特点？
4. 软件测试应覆盖哪四种接口？
5. 测试覆盖率分析中常见的五类标准是什么？
6. 伦理披露（Ethical Disclosure）的正确流程是怎样的？
