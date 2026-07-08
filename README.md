# Awesome PPT Skill

这个仓库只做两件事：

1. 整理一个 **PPT Skill 列表**，收集明确面向 PPT / PowerPoint / PPTX / Slides / Presentation / Deck 的 Agent Skill、Claude Skill、Codex Skill、`SKILL.md`、GitHub Skill 仓库和 marketplace Skill 页面。
2. 基于这些 Skill 的共性，整理出一个 **集大成的 All-in-One PPT Skill**：先路由任务，再生成结构化计划，最后按可编辑 PPTX、HTML/Markdown、图片/PDF 重建、Google Slides、学术/商业模式和 QA 修复等路径执行。

这不是博客，也不是泛 AI 工具索引。主线就是：**PPT Skill 列表 -> 从列表总结能力 -> All-in-One PPT Skill**。

## PPT Skill 列表

整理日期：2026-07-08

来源对话：[ChatGPT 调研窗口](https://chatgpt.com/c/6a4de5f8-eedc-83ee-99a5-557c0a34e336)

筛选口径：只保留明确指向 PPT / PowerPoint / PPTX / Slides / Presentation / Deck 的具体 Skill 或 Skill 仓库；剔除泛索引站、泛 Office 工具、泛写作/图表工具和非 PPT 专项资源。

总数：121

### 分类统计

| 分类 | 数量 |
| --- | ---: |
| HTML/Markdown Slides | 39 |
| PPTX 创建/编辑 | 19 |
| PPT 设计 | 13 |
| 学术/论文 PPT | 12 |
| PPT 生成 | 11 |
| 图像/PDF 转 PPT | 9 |
| 官方/核心 | 5 |
| 商业/Deck | 4 |
| 质量检查 | 3 |
| Google Slides | 3 |
| 可编辑 PPT | 2 |
| LibreOffice Impress | 1 |

### 优先级统计

| 优先级 | 数量 |
| --- | ---: |
| 可看 | 53 |
| 优先 | 45 |
| 强烈优先 | 22 |
| 审计 | 1 |

### 完整列表

| # | Skill | 分类 | 描述 | 入口类型 | 优先级 |
| ---: | --- | --- | --- | --- | --- |
| 1 | [OpenAI slides](https://mcpservers.org/agent-skills/openai/slides) | 官方/核心 | OpenAI slides Agent Skill：创建和编辑 .pptx slide decks，基于 PptxGenJS 与渲染/校验工具。 | Agent Skill 页面 | 强烈优先 |
| 2 | [Anthropic pptx](https://github.com/anthropics/skills/blob/main/skills/pptx/SKILL.md) | 官方/核心 | Anthropic 官方 PPTX Skill：创建、编辑、分析 .pptx，含模板、布局、speaker notes、视觉 QA。 | GitHub SKILL.md | 强烈优先 |
| 3 | [Anthropic ppt-template-creator](https://mcpservers.org/agent-skills/anthropic/ppt-template-creator) | 官方/核心 | 把用户提供的 PowerPoint 模板转成可复用的 PPT 模板 Skill。 | Agent Skill 页面 | 强烈优先 |
| 4 | [Anthropic pptx-author](https://mcpservers.org/agent-skills/anthropic/pptx-author) | 官方/核心 | 在无 PowerPoint GUI 的托管 Agent 环境中，直接在磁盘生成 .pptx 文件。 | Agent Skill 页面 | 强烈优先 |
| 5 | [Anthropic pitch-deck](https://mcpservers.org/agent-skills/anthropic/pitch-deck) | 商业/Deck | 投资银行 pitch deck 模板填充、格式校验和数据叙事一致性工作流。 | Agent Skill 页面 | 优先 |
| 6 | [Anthropic ib-check-deck](https://mcpservers.org/agent-skills/anthropic/ib-check-deck) | 质量检查 | 投行/客户展示 deck 质量检查，关注跨页数字一致性、数据叙事、格式问题。 | Agent Skill 页面 | 优先 |
| 7 | [Microsoft powerpoint](https://mcpservers.org/agent-skills/microsoft/powerpoint) | 官方/核心 | Microsoft hve-core 的 PowerPoint Skill：用 python-pptx 和 YAML 内容/样式定义生成、更新、管理 deck。 | Agent Skill 页面 | 强烈优先 |
| 8 | [Microsoft customer-card-render](https://mcpservers.org/agent-skills/microsoft/customer-card-render) | 商业/Deck | 把 Design Thinking canonical artifacts 映射成 PowerPoint slide YAML，并调用 PowerPoint skill pipeline 构建 deck。 | Agent Skill 页面 | 可看 |
| 9 | [Google Workspace gws-slides](https://github.com/googleworkspace/cli/blob/main/skills/gws-slides/SKILL.md) | Google Slides | Google Workspace CLI 的 gws-slides Skill：读写 Google Slides presentations。 | GitHub SKILL.md | 强烈优先 |
| 10 | [Google Workspace recipe-create-presentation](https://github.com/googleworkspace/cli/blob/main/skills/recipe-create-presentation/SKILL.md) | Google Slides | Google Slides 创建演示文稿 recipe：创建 presentation、获取 ID、分享权限等流程。 | GitHub SKILL.md | 强烈优先 |
| 11 | [Google Slides Automation](https://github.com/sickn33/antigravity-awesome-skills/blob/main/plugins/antigravity-bundle-documents-presentations/skills/google-slides-automation/SKILL.md) | Google Slides | 本地自动化创建、检查和修改 Google Slides presentations。 | GitHub SKILL.md | 优先 |
| 12 | [awesome-claude-skills / pptx](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/document-skills/pptx/SKILL.md?plain=1) | PPTX 创建/编辑 | 通用 PowerPoint / PPTX 创建、编辑、分析 Skill，直接指向 document-skills/pptx/SKILL.md。 | GitHub SKILL.md | 强烈优先 |
| 13 | [claude-cortex / pptx](https://awesomeskill.ai/skill/claude-cortex-pptx) | PPTX 创建/编辑 | PPTX 创建、编辑、分析 Skill 的直接页面，可查看 SKILL.md 与安装方式。 | Marketplace Skill | 优先 |
| 14 | [ai-agent-skills / pptx](https://awesomeskill.ai/skill/ai-agent-skills-pptx) | PPTX 创建/编辑 | 使用 python-pptx 风格的通用 PPTX Skill 页面。 | Marketplace Skill | 可看 |
| 15 | [cam10001110101 / pptx](https://lobehub.com/skills/cam10001110101-claude-skills-base-pptx) | PPTX 创建/编辑 | PPTX creation/editing/analysis Skill 的镜像 Skill 页面。 | Marketplace Skill | 可看 |
| 16 | [tfriedel / claude-office-skills / pptx](https://lobehub.com/vi-VN/skills/tfriedel-claude-office-skills-pptx) | PPTX 创建/编辑 | Office 技能集中的 PowerPoint/PPTX Skill，支持 scratch/template/HTML-to-PPTX 工作流。 | Marketplace Skill | 优先 |
| 17 | [davila7 / pptx-official](https://github.com/davila7/claude-code-templates/blob/main/cli-tool/components/skills/document-processing/pptx-official/SKILL.md) | PPTX 创建/编辑 | Claude Code templates 中的 pptx-official Skill，触发 deck、slides、presentation、.pptx 场景。 | GitHub SKILL.md | 优先 |
| 18 | [enuno / pptx skill template](https://github.com/enuno/claude-command-and-control/blob/main/skills-templates/document-skills/pptx/SKILL.md) | PPTX 创建/编辑 | Claude command/control 模板中的 document-skills/pptx Skill。 | GitHub SKILL.md | 可看 |
| 19 | [pptx-manipulation](https://awesomeskill.ai/skill/claude-office-skills-skills-pptx-manipulation) | PPTX 创建/编辑 | 基于 python-pptx 的 PPTX 创建、修改、提取内容 Skill。 | Marketplace Skill | 强烈优先 |
| 20 | [pptx-generator](https://github.com/MiniMax-AI/skills/blob/main/skills/pptx-generator/SKILL.md) | PPTX 创建/编辑 | MiniMax-AI 的 PPTX Generator & Editor：PptxGenJS 创建、XML 编辑、markitdown 提取。 | GitHub SKILL.md | 强烈优先 |
| 21 | [PptxGenJS Slide Making Skill](https://github.com/MiniMax-AI/skills/blob/main/plugins/pptx-plugin/skills/slide-making-skill/SKILL.md) | PPTX 创建/编辑 | MiniMax-AI 插件中的原生 .pptx slide-making Skill，专注 PptxGenJS。 | GitHub SKILL.md | 强烈优先 |
| 22 | [documents-pptx](https://awesomeskill.ai/skill/dotfiles-pptx) | PPTX 创建/编辑 | 围绕 PPTX、OOXML、html2pptx 的文档生成 Skill 页面。 | Marketplace Skill | 优先 |
| 23 | [pptx-from-layouts-skill](https://github.com/tristan-mcinnis/pptx-from-layouts-skill) | PPTX 创建/编辑 | 使用 PowerPoint 模板 slide master/layout，从 Markdown 生成咨询级 PPTX。 | GitHub repo | 优先 |
| 24 | [presentation-skill / pptx-skill](https://github.com/sirilsengolraj-source/pptx-skill) | PPTX 创建/编辑 | 把 deck 当代码：结构化源文件 → editable PowerPoint decks → QA loop。 | GitHub repo | 优先 |
| 25 | [PowerPoint Slides Skill](https://github.com/Noi1r/powerpoint-skill) | PPTX 创建/编辑 | Noi1r 的 PowerPoint skill：从论文、笔记、结构化内容生成富视觉 .pptx，含数学公式和图表管线。 | GitHub repo | 优先 |
| 26 | [ClaudePowerPointSkill](https://github.com/PeterKalmstrom/ClaudePowerPointSkill) | PPTX 创建/编辑 | 面向 Claude 的 PowerPoint Skill 社区仓库。 | GitHub repo | 可看 |
| 27 | [powerpoint-skill](https://github.com/Shimonimposed141/powerpoint-skill) | PPTX 创建/编辑 | PowerPoint 创建/处理方向社区 Skill。 | GitHub repo | 可看 |
| 28 | [bruce-pptx-generator](https://github.com/bruc3van/bruce-pptx-generator) | PPTX 创建/编辑 | PPTX 生成社区 Skill。 | GitHub repo | 可看 |
| 29 | [OpenClaw Medical pptx](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills/blob/main/skills/pptx/SKILL.md) | PPTX 创建/编辑 | OpenClaw Medical Skills 中的 pptx/SKILL.md，面向医疗/科研类 PPTX 工作流。 | GitHub SKILL.md | 可看 |
| 30 | [codex-ppt-skill](https://github.com/ningzimu/codex-ppt-skill) | PPT 生成 | Codex PPT skill：从文章、报告、论文、笔记、大纲生成视觉统一 PPT/PPTX。 | GitHub repo | 强烈优先 |
| 31 | [qybaihe / codex-ppt](https://github.com/qybaihe/codex-ppt) | PPT 生成 | Codex Skill：image mode 与 editable PPTX mode 两种路径，先生成 slide image，再重建可编辑 PowerPoint。 | GitHub repo | 优先 |
| 32 | [awesome-ppt-skills](https://github.com/stevenjinlong/awesome-ppt-skills) | PPT 生成 | Awesome PPT Codex Skill：image-first presentation generation，并可配合 ppt-master 生成 editable PPTX。 | GitHub repo | 优先 |
| 33 | [editable-leadership-pptx](https://github.com/CamelKing1997/editable-leadership-pptx) | 商业/Deck | Codex PPT Skill：生成 editable leadership、executive、project update .pptx。 | GitHub repo | 优先 |
| 34 | [ppt-master](https://github.com/hugohe3/ppt-master/blob/main/skills/ppt-master/SKILL.md) | PPT 生成 | 生成真实、可编辑 PowerPoint 的 PPT Master Skill，强调 native shapes、charts、speaker notes、QA。 | GitHub SKILL.md | 强烈优先 |
| 35 | [guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | PPT 生成 | 归藏 PPT Skill：中文社区高星 HTML/PPT 风格 deck 生成。 | GitHub repo | 强烈优先 |
| 36 | [future-ppt-skill](https://github.com/TonyLTalentexe/future-ppt-skill) | PPT 生成 | Codex Skill：通过设计契约、SVG 输出、PPTX 导出和 QA report 生成 editable PowerPoint。 | GitHub repo | 优先 |
| 37 | [ppt-agent-skills](https://github.com/Hafiz3369/ppt-agent-skills) | PPT 生成 | 围绕 PPT 生成/编辑的 Agent Skills 集合。 | GitHub repo | 可看 |
| 38 | [codex-visual-ppt-deck-builder](https://github.com/DwDestiny/codex-visual-ppt-deck-builder) | PPT 生成 | Codex 视觉型 PPT deck 构建 Skill。 | GitHub repo | 可看 |
| 39 | [ppt-deck-builder-skill](https://github.com/Richard-2718/ppt-deck-builder-skill) | PPT 生成 | PPT deck builder 社区 Skill。 | GitHub repo | 可看 |
| 40 | [PPT-builder-textbook](https://github.com/FangCD-zju/PPT-builder-textbook) | PPT 生成 | 教材/文本转 PPT 的 Skill。 | GitHub repo | 可看 |
| 41 | [nanobanana-ppt](https://awesomeskill.ai/skill/nanobanana-ppt-skills-) | PPT 生成 | PPT Generator Pro Skill；公开索引曾标注高风险，建议只做审计观察，不要直接安装。 | Marketplace Skill | 审计 |
| 42 | [ai-editable-ppt-skill](https://github.com/iwbaga724-Hinda/ai-editable-ppt-skill) | 可编辑 PPT | AI 生成可编辑 PPT 的社区 Skill。 | GitHub repo | 优先 |
| 43 | [editable-pptx-skill](https://github.com/Liuguanyi2125/editable-pptx-skill) | 可编辑 PPT | 可直接放入 Codex / Claude skills 目录的分层可编辑 PPTX Skill。 | GitHub repo | 优先 |
| 44 | [image-to-editable-ppt-skill](https://github.com/ningzimu/image-to-editable-ppt-skill) | 图像/PDF 转 PPT | 将 slide images、PDF、image-based PPTX 转成 editable PowerPoint decks 的 Codex Skill。 | GitHub repo | 强烈优先 |
| 45 | [slide-image-to-editable-pptx](https://github.com/w1163222589-coder/slide-image-to-editable-pptx) | 图像/PDF 转 PPT | 将 slide screenshots 转成 editable PowerPoint decks 的 Codex Skill。 | GitHub repo | 优先 |
| 46 | [EditableImage2PPTSkill](https://github.com/soulmujoco/EditableImage2PPTSkill) | 图像/PDF 转 PPT | 从 slide screenshots 或 exported slide images 重建 editable PowerPoint decks。 | GitHub repo | 优先 |
| 47 | [knight-imagetopptx-skill](https://github.com/knight6669/knight-imagetopptx-skill) | 图像/PDF 转 PPT | 图片到 PPTX 的转换/重建 Skill。 | GitHub repo | 可看 |
| 48 | [gpt-image-ppt-creator-skill](https://github.com/LueXxxxxxx/gpt-image-ppt-creator-skill) | 图像/PDF 转 PPT | 结合图像生成与 PPT 组装的 Skill。 | GitHub repo | 可看 |
| 49 | [gpt-image2-ppt-skills](https://github.com/JuneYaooo/gpt-image2-ppt-skills) | 图像/PDF 转 PPT | 从 GPT 图像/素材到 PPT 的生成 Skills 集合。 | GitHub repo | 可看 |
| 50 | [ppt-image-workflow](https://github.com/realfamousfrog-pixel/ppt-image-workflow) | 图像/PDF 转 PPT | PPT 图片生成、嵌入、工作流 Skill。 | GitHub repo | 可看 |
| 51 | [ppt-image-share-builder](https://github.com/uuoov/ppt-image-share-builder) | 图像/PDF 转 PPT | 构建可分享图片式 PPT/演示素材的 Skill。 | GitHub repo | 可看 |
| 52 | [imagegen-scene-ppt](https://github.com/jojoxiaocai/imagegen-scene-ppt) | 图像/PDF 转 PPT | 用图像生成场景辅助构建 PPT 的 Skill。 | GitHub repo | 可看 |
| 53 | [ppt-visual](https://awesomeskill.ai/skill/claude-office-skills-skills-ppt-visual) | PPT 设计 | 为 PPT/Slides 提供视觉布局、颜色、字体、图标、线框和 before/after 设计指导。 | Marketplace Skill | 强烈优先 |
| 54 | [elite-powerpoint-designer](https://awesomeskill.ai/skill/willem4130-claude-code-skills-elite-powerpoint-designer) | PPT 设计 | 专业 PowerPoint 设计 Skill：品牌一致性、视觉层级、动画、Markdown 转专业 PPT。 | Marketplace Skill | 强烈优先 |
| 55 | [PPT-Design-Skill](https://github.com/billLiao/PPT-Design-Skill) | PPT 设计 | 融合多种 PPT 设计风格，直接生成 PPT 文件而不是 HTML。 | GitHub repo | 优先 |
| 56 | [Mck-ppt-design-skill](https://github.com/likaku/Mck-ppt-design-skill) | PPT 设计 | 麦肯锡/BCG 风格 PPT 设计系统：layout patterns、flat design、python-pptx。 | GitHub repo | 优先 |
| 57 | [PPT-Design-DNA](https://github.com/dakjdakd/PPT-Design-DNA) | PPT 设计 | 围绕 PPT 设计 DNA、风格与版式的 Skill。 | GitHub repo | 可看 |
| 58 | [polished-ppt-skill](https://github.com/jiadong111-debug/polished-ppt-skill) | PPT 设计 | PPT 打磨、美化、专业化处理 Skill。 | GitHub repo | 可看 |
| 59 | [PPT Design Style System](https://mcpmarket.com/tools/skills/ppt-design-style-system) | PPT 设计 | 四种 PowerPoint design recipes：Sharp、Soft、Rounded、Pill，针对 PptxGenJS token 化设计。 | Marketplace Skill | 可看 |
| 60 | [KingDee-PPT-Skill](https://github.com/WayneZhon/KingDee-PPT-Skill) | PPT 设计 | 金蝶官方风格 .pptx / HTML 幻灯片 Skill，复刻企业模板语言。 | GitHub repo | 可看 |
| 61 | [huawei-style-ppt-skill](https://github.com/zuiho-kai/huawei-style-ppt-skill) | PPT 设计 | 华为风高密度信息 PPT 制作工作流 Skill。 | GitHub repo | 可看 |
| 62 | [Powerpoint-fancy-design](https://github.com/Phlegonlabs/Powerpoint-fancy-design) | PPT 设计 | Markdown → styled HTML slides、PNG renders、exportable PPTX decks 的 presentation-design Skill。 | GitHub repo | 可看 |
| 63 | [ppt-agent-skill](https://github.com/Akxan/ppt-agent-skill) | PPT 设计 | 世界级 AI presentation generator，强调样式、图表、全局视觉一致性。 | GitHub repo | 可看 |
| 64 | [ppt-svg-generator](https://github.com/vigorX777/ppt-svg-generator) | PPT 设计 | 将 Markdown 文稿转为 HTML/PDF 演示文稿，支持多预设风格和 SVG 视觉。 | GitHub repo | 可看 |
| 65 | [PPT-sense-deck-skill](https://github.com/xhshow2025/-PPT-sense-deck-skill-) | PPT 设计 | 鲸格 PPT：Codex Skill，用于高质量浏览器原生演示文稿。 | GitHub repo | 可看 |
| 66 | [academic-pptx-skill](https://github.com/Gabberflast/academic-pptx-skill) | 学术/论文 PPT | Academic PPTX Skill：配合 Anthropic PPTX 技术生成，处理学术内容、论证结构和设计标准。 | GitHub repo | 优先 |
| 67 | [claude-skill-academic-ppt](https://github.com/PHY041/claude-skill-academic-ppt) | 学术/论文 PPT | 生成完整学术 PPT 的 Claude Code Skill，支持中英文说明。 | GitHub repo | 优先 |
| 68 | [scholar-ppt-cn](https://github.com/deathcats4/scholar-ppt-cn) | 学术/论文 PPT | 中文学术 PPT 工作流 Skill：paper-to-editable PowerPoint、planning table、mockup family、PPTX generation。 | GitHub repo | 优先 |
| 69 | [codex-skill-academic-slides](https://github.com/FA-T-T/codex-skill-academic-slides) | 学术/论文 PPT | 面向 Codex 的学术演示/论文汇报幻灯片 Skill。 | GitHub repo | 优先 |
| 70 | [nature-paper2ppt](https://awesomeskill.ai/skill/yuan1z0825-nature-skills-nature-paper2ppt) | 学术/论文 PPT | 从科学论文、preprint、PDF、abstract、figure legends 等生成中文 Nature-style PPTX。 | Marketplace Skill | 优先 |
| 71 | [literature-report-ppt-builder](https://github.com/fangyuanopus/literature-report-ppt-builder) | 学术/论文 PPT | 文献报告/学术汇报 PPT 构建 Skill。 | GitHub repo | 优先 |
| 72 | [Aut_Sci_ppt](https://github.com/ShZhao27208/Aut_Sci_ppt) | 学术/论文 PPT | 自动科学/学术 PPT 方向社区 Skill。 | GitHub repo | 可看 |
| 73 | [scientific-slides](https://github.com/k-dense-ai/claude-scientific-writer/blob/main/skills/scientific-slides/SKILL.md) | 学术/论文 PPT | 科研 presentation slides Skill，支持 research talks、conference、seminar、thesis defense 等。 | GitHub SKILL.md | 优先 |
| 74 | [scientific-slides / Kosmos](https://awesomeskill.ai/skill/kosmos-scientific-slides) | 学术/论文 PPT | 会议、论文、答辩等科研演示 Skill 页面。 | Marketplace Skill | 优先 |
| 75 | [claude-scientific-skills / scientific-slides](https://awesomeskill.ai/skill/claude-scientific-skills-scientific-slides) | 学术/论文 PPT | 科研演示、PowerPoint/Beamer 相关 Skill。 | Marketplace Skill | 优先 |
| 76 | [paper-slides](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/main/skills/paper-slides/SKILL.md) | 学术/论文 PPT | 从论文生成 Beamer/PDF/可编辑 PPTX，含讲稿和 speaker notes。 | GitHub SKILL.md | 优先 |
| 77 | [slide-script-tex-generator](https://github.com/Qrzzzz/slide-script-tex-generator) | 学术/论文 PPT | 生成幻灯片脚本与 TeX/学术演示相关内容。 | GitHub repo | 可看 |
| 78 | [ai-slides](https://awesomeskill.ai/skill/claude-office-skills-skills-ai-slides) | HTML/Markdown Slides | AI-powered presentation generation：从主题或大纲生成完整演示。 | Marketplace Skill | 优先 |
| 79 | [md-slides](https://github.com/zl190/md-slides) | HTML/Markdown Slides | Markdown → slides 的 Claude Code Skill，可生成幻灯片、图示和插图。 | GitHub repo | 强烈优先 |
| 80 | [dev-slides](https://github.com/claude-office-skills/skills/blob/main/dev-slides/SKILL.md) | HTML/Markdown Slides | 面向技术演讲的 Slidev / developer slides Skill，可导出 PPTX。 | GitHub SKILL.md | 优先 |
| 81 | [html-to-ppt](https://awesomeskill.ai/skill/claude-office-skills-skills-html-to-ppt) | HTML/Markdown Slides | HTML / Markdown → PowerPoint presentations，使用 Marp 工作流。 | Marketplace Skill | 强烈优先 |
| 82 | [html-ppt-skill](https://github.com/lewislulu/html-ppt-skill) | HTML/Markdown Slides | HTML PPT Studio：专业 HTML presentations Skill，含 presenter mode、主题、模板、动画。 | GitHub repo | 强烈优先 |
| 83 | [html-ppt](https://awesomeskill.ai/skill/lewislulu-html-ppt-skill-html-ppt) | HTML/Markdown Slides | HTML 到 PPT/PPTX 方向的转换 Skill 页面。 | Marketplace Skill | 可看 |
| 84 | [Rao-HTML-to-PPT](https://github.com/raoqiu29-bot/Rao-HTML-to-PPT) | HTML/Markdown Slides | HTML 到 PPT 工作流，适合前端式版面转演示稿。 | GitHub repo | 可看 |
| 85 | [html-ppt-picker](https://github.com/pakco77/html-ppt-picker) | HTML/Markdown Slides | HTML/PPT 选择与转换相关 Skill。 | GitHub repo | 可看 |
| 86 | [pptx-html-fidelity-audit](https://awesomeskill.ai/skill/nexu-io-open-design-pptx-html-fidelity-audit) | 质量检查 | 审计 HTML deck 到 PPTX 导出后的布局漂移，并辅助修复。 | Marketplace Skill | 优先 |
| 87 | [slides-skill](https://github.com/whq217/slides-skill) | HTML/Markdown Slides | 通用 slides 生成/编辑 Skill。 | GitHub repo | 可看 |
| 88 | [slide-wright-skill](https://github.com/arifszn/slide-wright-skill) | HTML/Markdown Slides | Slide deck 写作/生成 Skill。 | GitHub repo | 可看 |
| 89 | [starry-slides](https://github.com/StarryKit/starry-slides) | HTML/Markdown Slides | Starry 风格/通用 slides 生成 Skill。 | GitHub repo | 可看 |
| 90 | [high-quality-slides](https://github.com/andyqiu847-ai/high-quality-slides) | HTML/Markdown Slides | 高质量 slides 生成/设计 Skill。 | GitHub repo | 优先 |
| 91 | [deck-factory](https://github.com/kimsh-1/deck-factory) | HTML/Markdown Slides | 演示 deck 生成工厂型 Skill。 | GitHub repo | 可看 |
| 92 | [build-presentation-skill](https://github.com/sheli-kohan/build-presentation-skill) | HTML/Markdown Slides | Story-driven presentation + editable PPTX Skill。 | GitHub repo | 强烈优先 |
| 93 | [client-proposal-slide](https://github.com/wan-huiyan/claude-client-proposal-slide) | 商业/Deck | 客户提案/销售方案类幻灯片生成 Skill。 | GitHub repo | 优先 |
| 94 | [document-interactive-slides-skill](https://github.com/wuxiao00j/document-interactive-slides-skill) | HTML/Markdown Slides | 从文档生成交互式幻灯片/演示体验。 | GitHub repo | 优先 |
| 95 | [ai-native-slides](https://github.com/OpenClaudex/ai-native-slides) | HTML/Markdown Slides | AI-native slide deck 生成 Skill。 | GitHub repo | 可看 |
| 96 | [vela-slides](https://github.com/AgentiaPT/vela-slides) | HTML/Markdown Slides | Vela slides 生成/编辑 Skill。 | GitHub repo | 可看 |
| 97 | [html-slides](https://github.com/mitchelfletcher11/html-slides) | HTML/Markdown Slides | HTML 风格幻灯片生成 Skill。 | GitHub repo | 优先 |
| 98 | [bluedusk / html-slides](https://github.com/bluedusk/html-slides) | HTML/Markdown Slides | HTML slides Skill，使用 progressive disclosure，支持 PowerPoint-to-HTML 方向。 | GitHub repo | 可看 |
| 99 | [frontend-slides](https://github.com/zarazhangrui/frontend-slides) | HTML/Markdown Slides | 用 Claude frontend skills 创建 beautiful web slides，支持将 PPT/PPTX 转为 HTML presentations。 | GitHub repo | 强烈优先 |
| 100 | [frontend-slides-editable](https://github.com/archlizheng/frontend-slides-editable) | HTML/Markdown Slides | 可编辑 HTML presentation Skill，含拖拽缩放、slide reorder、local save/export、PPTX-to-web conversion。 | GitHub repo | 优先 |
| 101 | [magic-slides](https://github.com/lolacolafola/magic-slides) | HTML/Markdown Slides | Magic Slides 社区 Skill。 | GitHub repo | 可看 |
| 102 | [html-presentation-skill](https://github.com/qaz1230sp/html-presentation-skill) | HTML/Markdown Slides | HTML presentation 生成 Skill。 | GitHub repo | 优先 |
| 103 | [marp-slide](https://github.com/softaworks/agent-toolkit/blob/main/skills/marp-slide/README.md) | HTML/Markdown Slides | Marp Slide Creator：用 Marp/Marpit 创建专业演示 slides。 | GitHub README/SKILL | 优先 |
| 104 | [marp-slide-quality](https://github.com/nibzard/marp-slide-quality) | 质量检查 | Marp slide 质量分析 Skill，用于拆分过载 slide、简化代码示例、改善内容结构。 | GitHub repo | 可看 |
| 105 | [create-marp-deck](https://claudemarketplaces.com/skills/omerr/claude-skills/create-marp-deck) | HTML/Markdown Slides | 结构化访谈后生成完整 Marp slide deck 的 Skill。 | Marketplace Skill | 可看 |
| 106 | [slidedown](https://github.com/Viniciuscarvalho/slidedown) | HTML/Markdown Slides | Markdown → PPTX/Slides 的 Claude Skill，含 md2pptx.js 和主题提取脚本。 | GitHub repo | 优先 |
| 107 | [impress](https://skillsmp.com/skills/andruia-antigravity-awesome-skills-skills-libreoffice-impress-skill-md) | LibreOffice Impress | LibreOffice Impress Skill：创建 presentation、ODP/PPTX/PDF 格式转换和 slide automation。 | Marketplace Skill | 可看 |
| 108 | [gamma-2](https://lobehub.com/skills/sundial-org-awesome-openclaw-skills-gamma-2) | HTML/Markdown Slides | Gamma 风格 presentation / PPTX 相关 Skill 页面。 | Marketplace Skill | 可看 |
| 109 | [baoyu-slide-deck](https://awesomeskill.ai/skill/baoyu-skills-baoyu-slide-deck) | HTML/Markdown Slides | 宝玉社区 slide deck 生成 Skill。 | Marketplace Skill | 优先 |
| 110 | [jack-tar-deckhand](https://github.com/SteveGJones/jack-tar-deckhand) | HTML/Markdown Slides | Deckhand / 演示 deck 生成辅助 Skill。 | GitHub repo | 可看 |
| 111 | [presentation-creator](https://claudemarketplaces.com/skills/getsentry/skills/presentation-creator) | HTML/Markdown Slides | Sentry design system 风格的交互式 HTML slide deck 创建 Skill。 | Marketplace Skill | 可看 |
| 112 | [open-slide](https://github.com/1weiho/open-slide) | HTML/Markdown Slides | Agent-native slide framework，内置 create-slide / slide-authoring 相关 skill 工作流。 | GitHub repo | 优先 |
| 113 | [huashu-design](https://github.com/alchaincyf/huashu-design) | HTML/Markdown Slides | HTML-native design Skill，支持一句话生成 slide decks、HTML deck 与 editable PPTX。 | GitHub repo | 优先 |
| 114 | [visual-explainer](https://github.com/nicobailon/visual-explainer) | HTML/Markdown Slides | 可生成 rich HTML pages 或 slide decks，适合图解、diff review、计划审计、项目复盘。 | GitHub repo | 可看 |
| 115 | [ppt-agent-workflow-san](https://github.com/mucsbr/ppt-agent-workflow-san) | HTML/Markdown Slides | 渐进交互式 PPT 生成 Skill，含 PPT 内容规划与 HTML slide to PPTX 工作流。 | GitHub repo | 优先 |
| 116 | [future-slide-skill](https://github.com/bytonylee/future-slide-skill) | HTML/Markdown Slides | image-based 与 HTML-based AI workflows 共用的 reusable slide-generation Skill。 | GitHub repo | 可看 |
| 117 | [visual-cognition-slides](https://github.com/edu-ai-builders/visual-cognition-slides) | HTML/Markdown Slides | 基于认知科学与教学设计的 HTML slides 生成 Skill。 | GitHub repo | 可看 |
| 118 | [slide-creator](https://github.com/kaisersong/slide-creator) | HTML/Markdown Slides | Claude Code / OpenClaw Skill：生成 zero-dependency HTML presentations。 | GitHub repo | 可看 |
| 119 | [slide-writer](https://github.com/FeeiCN/slide-writer) | HTML/Markdown Slides | 从 ideas、outlines、documents、speech drafts 生成企业 HTML presentations。 | GitHub repo | 可看 |
| 120 | [next-slide](https://github.com/codesstar/next-slide) | HTML/Markdown Slides | AI-powered HTML presentations，26+ styles，zero dependencies，bilingual。 | GitHub repo | 可看 |
| 121 | [slide](https://github.com/phodal/routa/blob/main/tools/office-skills/.agents/skills/slide/SKILL.md) | PPTX 创建/编辑 | phodal/routa office skills 中的 slide/SKILL.md：用 PptxGenJS 创建/编辑 presentation slide decks。 | GitHub SKILL.md | 可看 |

## 从这些 Skill 总结出的能力图谱

看完上面的列表后，能看到 PPT Skill 生态并不是一个单点能力，而是几条路线的组合。一个真正好用的 PPT Agent Skill 应该吸收这些路线的优点，而不是只押注一种生成方式。

| 能力路线 | 代表来源 | 应该吸收的能力 | 需要规避的问题 |
| --- | --- | --- | --- |
| 原生 PPTX 创建/编辑 | OpenAI slides、Anthropic pptx、Microsoft powerpoint、MiniMax pptx-generator | 用 PptxGenJS、python-pptx、OOXML 或 Office API 生成可编辑文本、形状、表格、图表。 | 不能只生成“看起来像 PPT”的图片；必须保留可编辑对象。 |
| 模板/品牌复用 | ppt-template-creator、pptx-from-layouts-skill、企业风格 PPT Skill | 从参考 deck 中抽取母版、配色、字体、版式和组件。 | 不能每次重新发明设计系统，容易风格漂移。 |
| 图片优先视觉生成 | awesome-ppt-skills、codex-ppt、guizang-ppt-skill、future-ppt-skill | 用 image-first/HTML-first 路线做高视觉探索。 | 不能把正式交付默认变成整页图片，编辑性会差。 |
| 图片/PDF 到可编辑 PPT | image-to-editable-ppt-skill、slide-image-to-editable-pptx、EditableImage2PPTSkill | OCR、版面理解、几何重建，把不可编辑材料还原成 native objects。 | 复杂图形可能只能近似，必须做视觉对比和 QA。 |
| HTML/Markdown Slides | html-to-ppt、html-ppt-skill、Slidev/Marp 类 Skill | 快速从 Markdown/HTML 生成网页演示或导出 PPTX。 | HTML 到 PPTX 经常有保真度漂移，不能跳过检查。 |
| Google Slides 自动化 | gws-slides、recipe-create-presentation、Google Slides Automation | 云端协作、Drive 分享、权限管理和 Slides API。 | 只有需要协作和云端权限时才走这条路。 |
| 学术/商业垂直场景 | academic-pptx-skill、scientific-slides、pitch-deck、ib-check-deck | 学术汇报、论文答辩、pitch deck、board update 的叙事结构和检查项。 | 场景规则不能和底层构建路线混在一起。 |
| QA/修复 | ib-check-deck、pptx-html-fidelity-audit、Marp QA 类 Skill | 渲染预览、检查溢出/错位/字体/编号/数据一致性，再局部修复。 | 没有 QA 的 PPT Skill 只能算“能生成”，不能算“可交付”。 |

结论：集大成 PPT Skill 的核心不应该是一个更长的 prompt，而应该是一个 **PPT Router + 结构化 slide plan + 多后端构建 + 可编辑对象策略 + 渲染 QA + 定点修复循环**。

## 集大成 All-in-One PPT Skill

完整实现放在：[all-in-one-ppt/SKILL.md](all-in-one-ppt/SKILL.md)

### 定位

`all-in-one-ppt` 是一个上层 Agent Skill。它不替代 PptxGenJS、python-pptx、HTML slide framework、Google Slides API 或图像生成工具，而是负责在 Agent 执行 PPT 任务时做编排：

```text
用户请求
  -> 判断任务类型
  -> 生成 deck_brief.json
  -> 生成 slide_plan.json
  -> 选择构建/编辑/重建/HTML/Google Slides/QA 路线
  -> 渲染预览
  -> QA 报告
  -> 定点修复
  -> 交付 PPTX / 预览 / 源计划 / QA 记录
```

### 核心原则

- 默认生成 **可编辑 PPTX**，文本、简单形状、表格、图表尽量保留为 native editable objects。
- 图片优先只用于视觉探索、海报式页面、或输入本身是图片/PDF 的重建任务。
- 每个非平凡 deck 都必须保留 `deck_brief.json` 和 `slide_plan.json`，避免 Agent 只靠自然语言临场发挥。
- `academic` 和 `business` 是场景模式，不是主构建路线；主路线仍然是 native PPTX、reconstruct、html-markdown 等。
- 交付前必须预览和 QA，发现 blocker / major issue 后局部修复。

### 主路由

| Route | 适用任务 | 输出倾向 |
| --- | --- | --- |
| `native-pptx` | 从主题、文档、笔记、大纲生成新 PPT。 | 可编辑 PPTX。 |
| `edit-existing` | 修改已有 `.pptx`，补页、改版、统一样式。 | 保留原模板和可编辑对象。 |
| `template-extract` | 从参考 deck 提取母版、配色、字体、版式。 | 可复用模板/设计约束。 |
| `image-first` | 高视觉冲击页面、概念稿、风格探索。 | slide image + 尽量保留 editable text。 |
| `reconstruct` | 截图、PDF、图片式 PPT 转可编辑 PPT。 | native shapes/text/tables/charts。 |
| `html-markdown` | Marp、Slidev、Reveal.js、HTML/CSS 演示。 | HTML/Markdown，可选导出 PPTX。 |
| `google-slides` | 云端协作、Drive 分享、Slides API。 | Google Slides presentation。 |
| `qa-audit` | 检查已有 deck 的格式、可读性、数据和可编辑性。 | QA report + 修复建议/补丁。 |

### 场景模式

| Mode | 作用 |
| --- | --- |
| `academic` | 论文汇报、文献综述、答辩、科研进展，强调论证结构、图表解释和引用可靠性。 |
| `business` | Pitch deck、board update、客户提案、咨询报告，强调结论先行、数字一致性和商业叙事。 |

### 压缩版 SKILL.md

```markdown
---
name: all-in-one-ppt
description: End-to-end PowerPoint and slides production skill for planning, creating, editing, reconstructing, QA-checking, and repairing presentations.
---

# All-in-One PPT

Default to editable PPTX. Keep text, simple shapes, tables, and charts as native editable objects whenever practical.

Every nontrivial deck must go through:
route selection -> brief extraction -> slide_plan.json -> build/edit -> rendered preview -> QA report -> targeted repair -> final delivery package.

Choose one primary route:
- native-pptx
- edit-existing
- template-extract
- image-first
- reconstruct
- html-markdown
- google-slides
- qa-audit

Add optional modes:
- academic
- business

Quality bar: do not deliver a deck with known text overflow, unreadable charts, missing fonts, distorted images, broken links, mismatched page sizes, inconsistent title placement, incorrect numbering, unexplained data, or unintended full-slide rasterization.
```

## 使用

安装：

```bash
git clone https://github.com/samaritan1998/awesome-ppt-skill.git
cd awesome-ppt-skill
mkdir -p ~/.codex/skills
ln -s "$PWD/all-in-one-ppt" ~/.codex/skills/all-in-one-ppt
```

调用：

```text
Use $all-in-one-ppt to turn this report into an editable, QA-checked PPTX.
```

本地验证：

```bash
python3 quick_validate.py all-in-one-ppt
python3 all-in-one-ppt/scripts/plan_from_markdown.py examples/ppt_skill_research_outline.md --out out/demo
python3 all-in-one-ppt/scripts/validate_plan.py out/demo/slide_plan.json --brief out/demo/deck_brief.json
python3 all-in-one-ppt/scripts/qa_report.py out/demo/slide_plan.json --out out/demo/qa_report.json
python3 all-in-one-ppt/scripts/html_preview.py out/demo/slide_plan.json --out out/demo/preview.html
```

可选 PPTX smoke builder：

```bash
npm --prefix all-in-one-ppt install
node all-in-one-ppt/scripts/build_pptx_pptxgenjs.mjs out/demo/slide_plan.json out/demo/deck.pptx
```

## 文件

- [all-in-one-ppt/SKILL.md](all-in-one-ppt/SKILL.md)：集大成 PPT Skill 主文件。
- [all-in-one-ppt/references/router.md](all-in-one-ppt/references/router.md)：路由规则。
- [all-in-one-ppt/references/workflows.md](all-in-one-ppt/references/workflows.md)：各路线工作流。
- [all-in-one-ppt/references/qa_checklist.md](all-in-one-ppt/references/qa_checklist.md)：QA 清单。
- [research/ppt_skill_list_2026_07_08.md](research/ppt_skill_list_2026_07_08.md)：Markdown 调研清单。
- [research/ppt_skill_list_2026_07_08.csv](research/ppt_skill_list_2026_07_08.csv)：CSV 调研清单。
- [research/ppt_skill_list_2026_07_08.json](research/ppt_skill_list_2026_07_08.json)：JSON 调研清单。
