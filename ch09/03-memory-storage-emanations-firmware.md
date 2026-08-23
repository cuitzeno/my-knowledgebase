# Ch9-03 内存、存储安全、电磁泄漏与固件

> 所属域：Domain 3 Security Architecture and Engineering
> 对应原书：Chapter 9 — Memory / Secondary Memory / Memory Security / Emanation / I-O / Firmware

## ① 一句话秒懂
内存与存储分**易失/非易失、随机/顺序**；敏感数据留存（data remanence）和冷启动攻击是隐患；设备还会**电磁辐射（emanations）**泄露信息，靠 TEMPEST/EMSEC 防护；固件层有 secure boot 与 phlashing 攻防。

## ② 生活类比
RAM 像黑板，断电就擦；ROM 像刻在石头上的字，掉电也不丢。电磁泄漏像隔着墙能"听"到隔壁打字声——法拉第笼就是给房间裹层金属屏蔽罩。

## ③ 核心概念（大白话 + 原书定义）

**内存类型**
- **ROM 系列**（非易失，掉电不丢）：ROM（出厂烧死）、PROM（一次写死）、EPROM（紫外擦）、EEPROM（电擦）、Flash（EEPROM 衍生，按块擦写，NAND 最常见，用于 U 盘/SSD）。
- **RAM**（易失，掉电清空，仅临时用）：Real memory（主存，由 DRAM 组成，需 CPU 周期刷新）、Cache RAM（L1–L4 高速缓存）、Registers（CPU 内寄存器，ALU 直接用的极快内存）。
  - DRAM（电容存位，需刷新，便宜）/ SRAM（触发器，不需刷新，快但贵）。
- **内存寻址**：Register、Immediate、Direct、Indirect、Base+Offset 五种；指针存地址，解引用（dereferencing）读该地址；竞争条件（race condition）可致空指针崩溃。

**虚拟内存（Virtual Memory）**
用 pagefile/swapfile 扩展地址空间；数据在 RAM 与磁盘间 paging 交换，慢。大物理 RAM 可减少依赖。

**存储分类**
- 主存（RAM）/ 辅存（HDD/SSD/磁带/光盘/闪存卡）。
- 易失 vs 非易失；随机访问（RAM、磁盘）vs 顺序访问（磁带）。
- SSD 用保留块 + 磨损均衡（wear leveling）延长寿命；传统清零擦除（zeroization）对 SSD 效果差（坏块未被覆盖）。

**内存与存储安全**
- **Data remanence（数据残留）**：删除/格式化后仍可恢复，须用 sanitizing（覆写）或物理销毁。
- **冷启动攻击（Cold boot attack）**：冷冻内存延缓电荷衰减，拔出 RAM 提取密钥；还有内存镜像/崩溃转储提取密钥。
- 辅存易被盗，建议全盘加密；可移动介质风险高，应加密。

**电磁泄漏（Emanation）与 TEMPEST/EMSEC**
设备运行时辐射电磁/射频信号，可被拦截提取机密。防护源自 **TEMPEST**（现多称 **EMSEC 发射安全**）：
- **Faraday cage（法拉第笼）**：金属外壳/网罩，吸收 EM，防信号进出。
- **White noise（白噪声）**：广播假流量掩盖真实发射。
- **Control zone（控制区）**：对特定区域用法拉第笼+白噪声保护。
- 其他：屏蔽线缆（STP）、光纤替代铜缆、访问控制、天线管理。Van Eck phreaking 即远距离读取辐射。

**I/O 设备风险**：显示器（TEMPEST、肩窥 shoulder surfing）、打印机/多功能机（存本地硬盘、遗忘取件）、键鼠（TEMPEST、按键记录）、电话 Modem（制造非受控入口，应禁用）、双网卡（有线+无线并存应禁用以防绕过边界）。

**固件（Firmware / microcode）**
存于 ROM/EEPROM 的底层软件。BIOS（ legacy）→ **UEFI**（支持大硬盘、安全启动、measured boot、启动 attestation）。更新固件叫 **flashing**。
- **Secure boot（安全启动/启动 attestation）**：只加载经预批数字证书签名的驱动/OS，挡住 rootkit/后门等底层恶意。
- **Phlashing**：刷入恶意伪造 BIOS/固件，植入远控等。

## ④ 真实案例
- 老旧 ATM/工控设备用未签名固件，易被 phlashing 植入恶意代码。
- 打印机硬盘残留敏感复印件，处置不当致数据泄露。
- 使用 STP 屏蔽线缆或光纤替代普通网线，降低电磁泄漏风险。

## ⑤ 考试怎么考
- 易失 vs 非易失（RAM 易失，ROM/闪存/磁盘非易失）。
- Data remanence 与 sanitization/销毁；SSD 清零擦除效果差。
- 冷启动攻击原理；全盘加密降低可移动/辅存风险。
- TEMPEST/EMSEC 三对策：法拉第笼、白噪声、控制区。
- UEFI secure boot 挡底层恶意；phlashing 是固件级攻击。

## ⑥ 记忆口诀
- RAM 易失如黑板，ROM 非易失如石刻；SSD 磨损均衡+保留块，清零擦除不彻底。
- 残留要 sanitize，冷启动冻内存；辐射防 TEMPEST，笼罩+白噪+控制区。
- UEFI 有 secure boot，phlashing 刷恶意。

## ⑦ 自测
1. 哪些存储器是易失的？哪些是非易失的？
2. 什么是 data remanence？如何彻底清除辅存数据？为何 SSD 清零擦除效果差？
3. TEMPEST/EMSEC 的三种主要对策是什么？
4. Secure boot 与 phlashing 分别是什么？
