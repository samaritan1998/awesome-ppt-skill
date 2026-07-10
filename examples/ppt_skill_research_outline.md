# PPT Agent Skill 生态地图

- 主流 PPT Skill 不是单一路线，而是一组面向不同任务的 Agent workflow。
- 更稳定的方案是先路由，再生成结构化 plan，最后渲染和 QA。

# 可编辑 PPTX 的主线

- Native PPTX 适合可编辑交付。
- 模板审计与复用适合品牌化交付。
- Reconstruction 负责把截图、PDF 或图片式 deck 还原成原生对象。
- HTML、Markdown 和 Google Slides 是输入或后续适配，不是默认输出路线。

# All-in-One Skill 设计

- 默认交付 editable PPTX。
- 使用 `deck_brief.json` 和 `slide_plan.json` 作为中间契约。
- 按 `create`、`edit`、`reconstruct`、`audit-repair` 路由。
- 用 `template`、`academic` 和 `business` modifier 补充模板和叙事规则。
- 生图只用于可替换视觉素材，文字、图表、表格和结构图保持原生可编辑。

# 交付质量门槛

- 交付前必须渲染预览。
- QA 至少覆盖内容数据、视觉渲染、对象可编辑性和 PPTX 内部结构。
- 发现 blocker 或 major issue 时，先局部修复再交付。
