# PPT Agent Skill 生态地图

- 主流 PPT Skill 不是单一路线，而是一组面向不同任务的 Agent workflow。
- 更稳定的方案是先路由，再生成结构化 plan，最后渲染和 QA。

# 主流协作模式

- Native PPTX 适合可编辑交付。
- HTML / Markdown 适合网页演示和技术分享。
- Image-first 适合视觉探索。
- Reconstruction 适合把截图、PDF 或图片式 deck 还原成可编辑 PPT。
- Google Slides 适合云端协作。

# All-in-One Skill 设计

- 默认走 editable PPTX。
- 使用 `deck_brief.json` 和 `slide_plan.json` 作为中间契约。
- 按 `native-pptx`、`edit-existing`、`template-extract`、`image-first`、`reconstruct`、`html-markdown`、`google-slides`、`qa-audit` 路由。
- 用 `academic` 和 `business` 模式补充场景叙事规则。

# 交付质量门槛

- 交付前必须渲染预览。
- QA 至少覆盖文本密度、对象可编辑性、页码顺序和潜在重叠。
- 发现 blocker 或 major issue 时，先局部修复再交付。
