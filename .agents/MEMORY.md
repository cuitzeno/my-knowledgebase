# MEMORY — 本仓库（mykb / my-knowledgebase）协作约定

> 供后续会话快速对齐的非显而易见约定。若与代码现状冲突，以代码为准。

## 1. 仓库与构建事实
- 远程仓库：`cuitzeno/my-knowledgebase`（分支 `main`）；本地 `/root/workspace/mykb`，本地分支 `master` 跟踪 `origin/main`。
- 构建：**GitHub Pages 原生 Jekyll + just-the-docs**（`remote_theme: just-the-docs/just-the-docs`，插件 `jekyll-remote-theme`）。
- **不要** `.nojekyll`；不要本地构建。阅读时不依赖外部 CDN，折叠与搜索稳定。
- 排除项：`_config.yml` 用 `exclude: [.agents, source-files]`；`.gitignore` 含 `.agents/venv/`、`source-files/`、`**/node_modules/`、`**/.env`。
- 素材放 `source-files/`（不入库）；提取用 `.agents/venv`（pypdf+pillow）：`scripts/extract_pdf.py`、`./scripts/extract_images.py`（位于 `.agents/skills/learning-kb/scripts/`）。

## 2. front matter 红线（曾踩坑）
- **`title` 含冒号必须加双引号**：如 `title: "Malware: Viruses…"`。否则 Jekyll 把 `: ` 当键值分隔符，整段 front matter 解析失败 → `parent` 丢失 → 文章掉到侧边栏顶层。
- 三级结构写法：文章 `parent: <章节页 title>` + `grand_parent: <主题父页 title>` + `nav_order: NN`；章节页需 `has_children: true`。所有 `title` 一律双引号包裹。
- 父页：`has_children: true` + `nav_order`（主题序：cissp=2, zap=3, postman=4, burp=5, wstg=6, websec=7）。

## 3. 主题与结构约定
- 每个主题 = 仓库根 `<theme>/` 文件夹 + `<theme>/<theme>.md` 父页；根 `index.md` 列全部主题入口。
- 二级结构（zap/postman/burp）：父页 + 文章（`parent` 指向父页）。
- 三级结构（cissp/websec）：父页 → 章节页（`parent`=父页,`has_children`）→ 文章（`parent`=章节,`grand_parent`=父页）。
- **websec 特殊约定（最新重构）**：三级 + 三类写法——
  - 概念篇：是什么/为什么/拆解（拆解必带最小示例：真实请求、JWT 三段、OData `$filter`、CORS 响应片段）。
  - 实操 Lab：目标→环境→分步（点击路径/命令/真实请求响应片段）→现象→结论。
  - 速查篇：清单 + 配置片段（如 Nginx 头、Spring Security 片段）。
  - 工具类（Postman/Burp/ZAP）走 Lab 实操，并与各自专属 KB 互补不重复。

## 4. 版权红线
- 版权书（CISSP / Postman / Burp 等）：仅做原创讲解，**不复制原文、不提取内嵌图**。
- 开放资料（ZAP / WSTG 等）：按规定处理；WSTG 最新为 5.0 开发线（场景 ID `WSTG-<类别码>-<编号>`，12 码：INFO/CONF/IDNT/ATHN/AUTHZ/SESS/INPV/ERRH/CRYP/BUSL/CLNT/APIT），v4.2 为上一稳定版。

## 5. 生成与提交流程（learning-kb 技能）
- 流水线：脚手架 → 提取 → 分析出大纲 → **交互确认** → 逐篇生成 → 增量（扫最大 NN 续编，不覆盖）→ 索引/导航 → 提交。
- 提交惯例：生成后 `git add <theme>/ index.md` → `git commit -m "feat(<theme>): ..."` → `git push origin HEAD:main`（技能模板写"不推送"，但实际按用户节奏一直推送）。
- 参考来源：每篇末尾 `> 参考来源：<素材/URL>（本文为原创讲解，非转载原文）`。

## 6. 当前主题清单
cissp(21章) · zap(6) · postman(14) · burp(12) · wstg(13) · websec(6章21篇)。最新提交见 `git log`。
