---
name: learning-kb
description: 把一本电子书、一个网址或一份资料，读透后按知识主题拆成多篇通俗易懂、含知识点详细讲解的小文章，落到同一主题的文件夹下，自动搭好 Jekyll(just-the-docs) 站点并用 GitHub Pages 随时可读；支持后续增量追加。触发："学习这本 PDF""把这篇网址做成知识库""reading-kb <素材> <主题>""生成 cissp 系列"。
version: 1.0.0
metadata:
  openclaw:
    requires:
      anyBins:
        - git
---

# Learning KB — 资料 → 多主题知识库

把任意材料（PDF 电子书 / 网页 URL / 其它可提取文本）读透、分析，生成**按知识主题拆分**的
多篇通俗讲解文章，放入仓库根的 `<theme>/` 文件夹，自动生成 Jekyll(just-the-docs) 站点，
用 GitHub Pages 随时随地阅读。同一主题可多次追加，绝不覆盖已生成内容。

## 输入（从用户消息解析）

- `source` —— 必填。PDF 路径（如 `source-files/CISSP.pdf`）或网页 URL。
- `theme`  —— 必填。主题 slug，用作文件夹名与 front matter 的 `parent`，如 `cissp`。
- `--title "<中文名>"` —— 可选。主题显示名，如 "CISSP 认证安全工程师知识库"；缺省用 `theme`。
- `--with-images` —— 可选开关。开启后用 baoyu-cover-image / baoyu-diagram 配图（默认纯文字）。
- `--extract-images` —— 可选。提取 PDF 内嵌图片（去重后）落到 `<theme>/imgs/` 并嵌入相关段落；
  仅对允许转载的开放素材（如 OWASP）使用，版权素材（如 CISSP）默认不加原图。

## 环境依赖

- 复用本仓库 `baoyu-skills` 工具链做配图（仅 `--with-images` 时需要）。
- PDF 文本提取用随附 venv：`python3 -m venv .agents/venv && .agents/venv/bin/pip install pypdf`
  （已就绪）。提取脚本：`<skill>/scripts/extract_pdf.py`。
- URL 提取直接用本 agent 的 `WebFetch` / `websearch` 工具读取页面正文。

---

## 流水线（严格按顺序）

### 1. 脚手架（若不存在则创建）
- 若当前目录不是 git 仓库：`git init`（仅本地，不建远程、不推送）。
- 确保仓库根有这些文件（缺哪个建哪个，不破坏已有）：
- `.nojekyll`：空文件，禁用 GitHub Pages 的 Jekyll，确保 `_sidebar.md` 等 `_` 开头文件被正常服务。
- `index.html`：docsify 引导页（见下方"脚手架片段"），从 CDN 加载 docsify + 搜索插件。
- `_sidebar.md`：根导航（见步骤 5）。
- `README.md`：站点首页/总目录（见步骤 5）。
- `.gitignore`：`.agents/venv/`、`source-files/`、`**/node_modules/`、`**/.env`。

> 不用 Jekyll、无构建步骤：push 后 GitHub Pages 直接服务静态文件，阅读时由浏览器渲染 Markdown。

### 2. 提取素材
- **PDF**：`.agents/venv/bin/python <skill>/scripts/extract_pdf.py <source> --out /tmp/<theme>.txt`
  输出纯文本 + 打印页数。若失败，回退：用 Read 工具分页读取（每次 ≤50 页）拼接。
- **URL**：`WebFetch` 取正文；多页则用 `websearch` 补充，汇成一份文本。

### 2b. 提取图片（仅当传 `--extract-images`）
`.agents/venv/bin/python <skill>/scripts/extract_images.py <source> --out <theme>`
- 按像素内容去重，落到 `<theme>/imgs/`，并生成 `imgs/manifest.json`（记录每张图出现在哪些页）。
- **判废规则**：若去重后每张唯一图都出现在"每一页"（典型 = 页眉/页脚/Logo 等页面装饰），
  说明无独有内容图 → **不嵌入、删除 `imgs/`**，并在大纲确认时告知用户"该 PDF 无可用配图"。
- 写正文时，把与某概念相关的唯一图用 `![alt](imgs/xxx.png)` 嵌到对应段落，文末来源补注"含原文档配图"。
- 版权红线：CISSP 等版权素材即便有图也不提取；仅 OWASP 等开放许可素材启用。

### 3. 分析 → 出大纲（质量闸门前）
读提取文本，按**知识主题/知识点**拆分（非死板按章节），产出大纲：
```
预计 N 篇。主题《<title>》大纲：
1. <标题> — 知识点：A、B
2. <标题> — 知识点：C
...
```
每篇 1–3 概念、目标 800–1500 字。同时给一句主题简介（用于总目录）。

### 4. 与你交互确认（必须在生成前）
把大纲打印出来，问你："确认 / 改第 X 篇为 Y / 增减篇数？"
- 你回"确认"或微调后，再继续。
- 未确认不得生成正文。

### 5. 逐篇生成
对大纲每篇，按 `references/article-template.md` 生成 `./<theme>/NN-<中文标题>.md`：
- **不要写 Jekyll front matter**（docsify 会把 `---` 块当正文显示）。文章首行直接是 `# 标题`；排序由 `_sidebar.md` 链接顺序 + `NN-` 文件名决定。
- `NN` = 主题内递增两位序号。**先扫描 `<theme>/` 现有最大 NN，从其后续编**（见步骤 6）。
- 末行"下一篇：…"先留占位，全部生成后回填（`references/article-template.md` 末句规则）。"下一篇"用相对链接，如 `(02-xxx.md)`。
- `--with-images` 时：每篇配套 `imgs/NN-cover.jpg` + 封面 prompt（风格复用 baoyu 模板），并嵌入 `![alt](imgs/xxx.png)`。

### 6. 增量规则（核心）
- 运行前扫描 `./<theme>/` 现有 `NN-*.md`，取最大序号 `M`；新文章从 `M+1` 起编。
- **绝不覆盖、重号、重命名已有文件**。
- 新 `theme`：建文件夹即可，根 `index.md` 重算。

### 7. 生成索引 / 导航
- 每主题父页 `./<theme>/<theme>.md`：正文放主题简介 + "本系列共 N 篇"列表（相对链接到各篇）；作为 docsify 侧边栏里该主题的分组入口。
- 根 `_sidebar.md`：列出全部主题（链接到各自父页）+ 其下各篇文章（相对链接），按 `NN-` 顺序；docsify 据此渲染左侧导航。
- 根 `README.md`：站点首页，列全部主题入口 + 一句话简介。
- 回填每篇"下一篇"指针；最后一篇写"系列完"。

### 8. 提交（不推送）
```bash
git add <theme>/ index.md _config.yml .gitignore
git commit -m "feat(<theme>): add NN-<slug> …"
```
- 脚手架首次：`chore: scaffold jekyll site`；仅刷新索引：`docs(<theme>): update index`。
- **不执行 `git push`**，也不开启 Pages（由用户来做）。

---

## 脚手架片段

`index.html`（docsify 引导页，CDN 加载，零构建）：
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <title>我的知识库</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/docsify@4/lib/themes/vue.css">
</head>
<body>
  <div id="app"></div>
  <script>
    window.$docsify = {
      name: '我的知识库', repo: 'cuitzeno/mykb',
      loadSidebar: true, subMaxLevel: 2, search: 'auto', homepage: 'README.md'
    }
  </script>
  <script src="https://cdn.jsdelivr.net/npm/docsify@4"></script>
  <script src="https://cdn.jsdelivr.net/npm/docsify@4/lib/plugins/search.min.js"></script>
</body>
</html>
```

`_sidebar.md`（根导航，按主题分组）：
```markdown
- [我的知识库](/)
- [CISSP 认证安全工程师知识库](cissp/cissp.md)
  - [CIA 三要素](cissp/01-CIA三要素.md)
  - [安全治理与合规驱动](cissp/02-安全治理与合规驱动.md)
```

> 无需 Jekyll、无构建。用户首次开启 Pages：仓库 Settings → Pages → Source 选主分支根目录；
> 因有 `.nojekyll`，GitHub 直接以静态文件服务，`_sidebar.md` 等正常生效。阅读时浏览器从 CDN 加载 docsify 渲染 Markdown。

## 版权
文章仅标注"参考来源"，做原创讲解，**不复制素材原文**（尤其 CISSP 等版权资料）。
原始素材（`source-files/`）不入库（已在 `.gitignore`）。
