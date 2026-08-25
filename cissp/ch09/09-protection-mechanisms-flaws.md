# Ch9-09 基础安全保护机制与常见架构缺陷

> 所属域：Domain 3 Security Architecture and Engineering
> 对应原书：Chapter 9 — Essential Security Protection Mechanisms / Common Security Architecture Flaws and Issues

## ① 一句话秒懂
OS 必须内置**进程隔离、硬件分段、信任根（RoT）**等保护机制（本质即零信任）；常见架构缺陷有**隐蔽信道、设计/编码缺陷、后门、rootkit、增量攻击**——防御靠审计、代码审查、纵深。

## ② 生活类比
进程隔离像给每个租户独立上锁房间（Ch8 已讲）；rootkit 像潜入大楼装修队，把监控摄像头都调成只拍空墙，让真小偷隐身；隐蔽信道像用灯闪摩斯码绕过门禁通信。

## ③ 核心概念（大白话 + 原书定义）

**为何需要保护机制**
"软件不应被信任"——第三方软件天生不可全信，OS 须用保护机制隔离进程、保环境稳定。这正是零信任的体现（见 Ch8）。设计早期就内建安全，成功与可靠几率最高。

**进程隔离（Process Isolation）**
OS 为每个进程提供独立内存空间并强制边界，防一进程读写他者数据。两大好处：防未授权访问、保进程完整性。现代 OS 常以每用户/每进程的虚拟机实现隔离。

**硬件分段（Hardware Segmentation）**
目的同进程隔离，但用**物理硬件**强制（非 OS 逻辑控制）。罕见，多用于国家安全级，因成本/复杂度高但敏感信息值得。

**信任根（Root of Trust, RoT）**
安全链的起锚点，提供安全可信基础，用于建立/验证完整性、真实性、机密性。
- **Trust anchor（信任锚）**：系统内天生被信的组件，通常是防篡改元素，整体信任源自它的可信度。
- **Hardware-based RoT**：用专用硬件实现（如 TPM/HSM），把关键安全功能与通用计算环境隔离，更抗攻击。

**系统安全策略（System Security Policy）**
针对单一系统实现的定义规则/实践/流程文档，指导其设计、开发、实现、测试、维护。防止高密级流向低密级叫**多级安全策略（multilevel security policy）**。安全须贯穿项目全生命周期，最后才补必失败。

**常见架构缺陷（Common Flaws）**
- **隐蔽信道（Covert Channel）**：用非正常通信路径传信息，绕开安全策略且难被监测。对立面是 overt channel（已知、授权、受控）。两类：
  - *Covert Timing Channel*：通过改变系统组件性能/资源时序传信息（如风扇转速编码 1/0、网速利用率编码）。
  - *Covert Storage Channel*：写数据到另一进程可读的公共存储区（如未分配空间、坏扇区/坏块、slack space 簇尾、未注册的扇区/簇）。
  - 防御：详尽审计所有活动、分析日志找异常。
- **设计/编码缺陷（Design/Coding Flaws）**：差设计、差实现、测试不足；尤其**维护钩子/后门（maintenance hooks/backdoors）**——开发期留的绕开访问控制入口未清除就上线。需大量测试+代码审查。参考 OWASP Top 10。人写不出完全无瑕代码，但源码分析工具+全程测试可大幅减瑕。
- **Rootkit**：深嵌 OS 的恶意软件（rooting=取得完全控制 + kit 工具集）。可替换内核、垫于内核下、替驱动、渗库，从而隐藏自身与同伙，使文件/进程不可见。检测：留意系统文件大小/哈希变化（HIDS 自动或人工）。一旦怀疑，**唯一安全响应是重构/替换整机**（彻底净化存储、从可信源重装、从无毒备份恢复）。最佳是事前防御。
- **增量攻击（Incremental Attacks）**：缓慢渐进，如 data diddling（篡改数据）、salami attack（把小额截留累积成大额，如每笔舍入差抹零入私账）。

## ④ 真实案例
- **Salami attack**：银行程序每笔利息舍入零头悄悄转入攻击者账户，长期累积巨款。
- **Rootkit**（如 Sony BMG 案）隐藏自身致系统难清，只能重装。
- 用风扇噪音/网速时序传递机密即 covert timing channel。

## ⑤ 考试怎么考
- 进程隔离 vs 硬件分段（逻辑 vs 物理强制）。
- RoT / trust anchor 概念；hardware-based RoT 用 TPM/HSM。
- 隐蔽信道两类（timing/storage）与例子；overt vs covert。
- 后门=maintenance hooks；rootkit 最佳响应是重构整机。
- 增量攻击：data diddling、salami attack。

## ⑥ 记忆口诀
- 进程隔离逻辑控，硬件分段物理封；RoT 是信任锚，TPM/HSM 硬件撑。
- 隐蔽信道两兄弟：时序改性能，存储写暗区；防御靠审计。
- 后门维护钩，rootkit 隐身；最佳响应整机换。

## ⑦ 自测
1. 进程隔离与硬件分段的根本区别？
2. 什么是信任根（RoT）与信任锚（trust anchor）？硬件 RoT 常用什么实现？
3. 隐蔽信道的 timing 与 storage 两类各举一个例子。
4. 怀疑系统感染 rootkit，正确的响应是什么？为什么？
