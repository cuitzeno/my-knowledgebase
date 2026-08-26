---
title: "Burp Suite 上手"
parent: "工具实操"
grand_parent: "Web 安全与开发基础实战知识库"
nav_order: 2
---

# Burp Suite 上手

## 一句话定义
本 Lab 用 Burp 完成"代理抓包 → 改包 → Repeater 手测 → Intruder 爆破"最小闭环。**更完整见 [Burp 知识库](../../burp/burp.md)**。

## 核心架构 / 工作原理

```mermaid
graph LR
  A[Burp 核心工具链] --> B[Proxy: 拦截/改包/匹配替换/上游代理]
  A --> C[Target: 站点地图/Scope 管理]
  A --> D[Repeater: 单包精细手测]
  A --> E[Intruder: 批量爆破/模糊测试(4种攻击模式)]
  A --> F[Scanner: 被动/主动扫描(Pro)]
  A --> G[Sequencer: 令牌随机性分析]
  A --> H[Decoder/Comparer/Extensions/BApp Store]
  
  B --> I[中间人定位: 浏览器代理 -> 127.0.0.1:8080 -> Burp -> 目标]
  I --> J[HTTPS 解密: Burp CA 证书 -> 导入浏览器根证书存储]
```

## 快速上手步骤

1. **下载启动**：
   - Community: https://portswigger.net/burp/communitydownload
   - 启动参数：`-Xmx4G` 起步(大项 8G+)：`java -jar -Xmx8G burpsuite_community.jar`
2. **配置浏览器代理**：
   - 系统/浏览器代理 → `127.0.0.1:8080`
   - 推荐 **FoxyProxy Standard** 一键切换
3. **装 CA 证书 (HTTPS 明文关键)**：
   - 浏览器访问 `http://burp` → 下载 `cacert.der`
   - 导入系统"受信任的根证书颁发机构" (Firefox 单独导入其证书库)
   - 验证：访问任意 HTTPS 站点 → Burp Proxy HTTP history 出现明文请求/响应
4. **拦截与改包**：
   - Proxy → Intercept → `Intercept is on` (绿按钮)
   - 浏览器访问目标 → 请求卡住 → 改参数(如 `id=1001`→`1002`) → `Forward` 放行
   - 观察响应差异(测 IDOR/越权/注入)
5. **Repeater 精细手测**：
   - HTTP history 右键请求 → `Send to Repeater`
   - Repeater 标签反复改 Header/Body/参数 → `Send` (Ctrl+R) → 对比响应历史
6. **Intruder 批量爆破**：
   - 右键请求 → `Send to Intruder`
   - `Positions` 标签 → `§` 标记 payload 位置(如 `id=§1001§`)
   - `Payloads` → Simple list / Brute forcer / Runtime file → 载入字典
   - 攻击类型选对：Sniper(单点) / Battering ram(同值多位置) / Pitchfork(并行) / Cluster bomb(笛卡尔积)
   - `Start attack` → 看状态码/长度/响应时间/Grep 匹配找异常
7. **圈定 Scope**：
   - Target → Site map → 右键目标宿主 → `Add to scope`
   - 勾选 `Show only in-scope items` 过滤噪音

```bash
# 无头模式启动 (CI/服务器)
java -jar burpsuite_pro.jar --headless --disable-auto-update
```

## 踩坑避坑指南

| 场景 | 问题现象 | 原因 | 解决/最佳实践 |
|------|----------|------|---------------|
| HTTPS 全报错/不显示 | "Certificate Unknown" | CA 证书未装入系统根存储 | **必须导入"受信任的根证书颁发机构"**；Firefox 需单独导入 |
| 流量不过 Burp | Proxy 标签无记录 | 端口冲突/代理未生效/证书不信任 | `netstat -an | grep 8080` 查占用；用 FoxyProxy 强制走代理 |
| 扫描把生产打挂 | 服务宕机/数据脏/账号锁 | 未圈 Scope/强度过大/含破坏性请求 | **先圈 Scope**；扫描配置排除登录/支付/删除接口；用速度滑块限速 |
| 只会点 Scanner | 漏报授权/逻辑/业务漏洞 | 扫描器只覆盖已知特征 | **Repeater 手测核心业务流**；Intruder 遍历 IDOR；Sequencer 测令牌 |
| 协作/换机器配置丢 | 重装后全没了 | 未导出项目配置 | 定期 `Project options → Save project`；团队共享 `.burp` 项目文件 |

## 替代方案对比

| 维度 | Burp Suite Pro | Burp Community | OWASP ZAP | Caido |
|------|----------------|----------------|-----------|-------|
| 价格 | $449/年 | 免费 | 免费 | 免费/商业版 |
| 扫描器 | 商业级规则库/IAST/扩展 | 仅被动扫描 | 社区规则 | 较弱 |
| 手测工具 | Repeater/Intruder/Organizer 强 | Repeater 基础版 | 同级 | 现代 UI、强 |
| 插件生态 | BApp Store 丰富 | 受限 | Marketplace 丰富 | 新兴 |
| 自动化/CI | CLI/API/Bamboo/Jenkins | 无 | Docker/GitHub Actions/API | CLI |
| 学习曲线 | 陡峭 | 中等 | 中等 | 平缓 |
| 适用场景 | 专业渗透/赏金/企业 | 学习/简单测试 | 入门/预算 0 | 现代团队/手测为主 |

---

> 参考来源：https://portswigger.net/burp/documentation/desktop/tutorials

*下一篇：[OWASP ZAP 上手](03-zap上手.md)*