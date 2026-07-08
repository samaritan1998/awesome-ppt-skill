# Security

`awesome-ppt-skill` 默认不需要云 API，也不会自动安装第三方 Skill。执行任何外部仓库里的脚本、模板或 Skill 之前，应先检查来源、依赖和文件写入范围。

## 使用建议

- 不要直接运行不可信仓库中的安装脚本。
- 生成或重建 PPT 时，先把输入文件放在明确的工作目录中。
- 处理公司模板、客户资料、论文草稿或未公开数据时，不要默认上传到第三方服务。
- 使用 Google Slides、Drive 或其他云 API 时，先确认账号、权限和共享范围。
- 对需要发布的 deck，交付前至少运行结构 QA；正式交付建议渲染预览后再检查。

Skill 内部安全说明见 [`all-in-one-ppt/references/security.md`](all-in-one-ppt/references/security.md)。
