---
title: "OWASP ZAP 上手"
parent: "工具实操"
grand_parent: "Web 安全与开发基础实战知识库"
nav_order: 3
---

# OWASP ZAP 上手

## 一句话定义
本 Lab 用 ZAP 完成"代理 → 爬取 → 主动扫描 → 看告警"最小闭环。**更完整见 [ZAP 知识库](../../zap/zap.md)**。

## 核心架构 / 工作原理

```mermaid
graph TD
  A[ZAP 核心流程] --> B[代理配置: 127.0.0.1:8080 + CA 证书]
  A --> C[爬取 Spider: 传统/AJAX 发现端点]
  A --> D[被动扫描: 流量经过即分析，安全无副作用]
  A --> E[主动扫描 Active Scan: 发攻击包验证漏洞(需授权)]
  A --> F[告警 Alerts: High/Medium/Low/Info 分级 + 证据]
  A --> G[报告导出: HTML/JSON/Markdown]
  
  B --> H[Safe Mode: 仅被动，防误伤]
  C --> I[传统 Spider: 读 HTML 链接，快]
  C --> J[AJAX Spider: 真浏览器渲染 JS，慢、需配置]
  E --> K[扫描策略: 强度/速度/排除项/自定义规则]
  F --> L[证据: 请求/响应/触发片段高亮]
```

## 快速上手步骤

1. **下载启动**：
   - https://www.zaproxy.org/download/ → 跨平台/安装包/Docker
   - 首次弹窗选 `No` (不持久化会话，新手推荐) 或 `Yes` 命名会话文件
2. **配置代理与证书**：
   - 浏览器代理 → `127.0.0.1:8080` (同 Burp)
   - 访问 `http://zap` → 下载 CA 证书 → 导入"受信任的根证书颁发机构"
   - 验证：访问 HTTPS 站点 → Sites 树出现目标
3. **快速自动扫描 (Quick Start)**：
   - `Quick Start` 标签 → `Automated Scan` → 填目标 URL → 选 Context(可选) → `Attack`
   - ZAP 自动：Spider 爬 → 被动扫 → 主动扫描所有发现的页面/参数
4. **或分步手动**：
   - Sites 树右键目标 → `Attack` → `Spider` / `AJAX Spider` → 爬取
   - 爬完 → 右键 → `Attack` → `Active Scan` → 调策略(强度/速度/排除)
4. **看告警与证据**：
   - `Alerts` 标签按风险分级 → 双击看请求/响应/触发片段高亮
   - 误报右键 → `False Positive` 标记
5. **导出报告**：
   - `Report` → `Generate HTML Report` → 选范围/模板 → 导出

```bash
# Docker 无头自动扫描
docker run -t owasp/zap2docker-stable zap-full-scan.py \
  -t https://target.com -r report.html -J scan.yaml
```

## 踩坑避坑指南

| 场景 | 问题现象 | 原因 | 解决/最佳实践 |
|------|----------|------|---------------|
| 忘开 Safe Mode 就扫 | 对无授权站点发起攻击 | 疏忽/不懂模式区别 | **养成习惯：启动即开 Safe Mode，拿到授权再关** |
| 爬不到登录后页面 | Sites 树只有登录页 | Spider 无法处理认证 | Context 配置 Authentication(Form-based/Script-based) 或手动登录后再爬 |
| AJAX Spider 起不来 | 报错/浏览器闪退 | 无头环境缺依赖 | Docker 需 `--cap-add=SYS_ADMIN`；或装 `libnss3 libatk-bridge2.0-0 libgtk-3-0` |
| 主动扫描把站打挂 | 目标宕机/锁账号/脏数据 | 强度过大/无节制 | 降低强度、限速、排除登录/支付/删除类接口、用 Scope 圈范围 |
| 误报太多吵开发 | 告警全是低风险/信息泄露 | 被动规则宽泛 | 关注高/中危；用 Alert Filters 隐藏信息级；人工复核高危项 |

## 替代方案对比

| 维度 | OWASP ZAP | Burp Suite Pro | Nuclei | 自建扫描器 |
|------|-----------|----------------|--------|------------|
| 规则质量 | 社区规则、较基础 | 商业级、更新快、IAST 增强 | 社区模板、极丰富、更新极快 | 完全自控、维护成本高 |
| 爬取能力 | AJAX Spider 配置繁琐 | 登录宏/AJAX/表单填充强 | 无(需外部爬虫) | 需自己写 |
| 误报率 | 中等 | 低 | 低(模板精确) | 可控 |
| CI/CD 集成 | Docker/GitHub Actions/API | CLI/Bamboo/Jenkins 插件 | 原生 CLI 极简 | 灵活 |
| 价格 | 免费 | $449/年 | 免费 | 人力高 |

---

> 参考来源：https://www.zaproxy.org/

*下一篇：[综合：Burp + Postman 串一次完整测试](04-综合实战.md)*