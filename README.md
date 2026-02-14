# AI 产品追踪系统

自动追踪 AI 产品的更新日志，用 Claude AI 一键生成中文周报。

## 🎯 这个项目做什么？

帮你自动收集多个 AI 产品的更新日志，然后用 AI 提炼重点、翻译成中文，生成格式化的周报。

**支持的产品**：
- Claude Code
- OpenCode
- Oh My OpenCode
- OpenClaw
- Cline
- RooCode
- Trae

**生成的周报包括**：
- 一句话总结本周核心更新
- 本周要点（3-5条重要更新）
- 各产品的详细更新列表

## 📖 如何使用

在 Claude Code 中运行：

```bash
/tracking-report --days 7
```

skill 会自动完成：
1. ✅ **爬取更新**：从各产品网站获取最新日志
2. ✅ **过滤数据**：只保留最近7天的更新
3. ✅ **AI 处理**：提炼重点 + 翻译成中文
4. ✅ **生成周报**：保存到 `data/reports/`

## 🤖 为什么需要 Claude Code？

这个项目依赖 **Claude Code 的 AI 能力**：
- 🧠 **提炼重点**：从大量更新中筛选重要内容
- 🌐 **翻译成中文**：将英文更新翻译成专业中文
- 📝 **格式化**：生成统一的周报格式

不是自己搭建 AI 服务，而是直接用 Claude Code 的能力。

## ⚙️ 配置产品清单

编辑 `config/products.json` 文件添加新产品：

```json
{
  "products": [
    {
      "name": "产品名称",
      "type": "github-releases",
      "url": "GitHub Releases 页面地址"
    }
  ]
}
```

**支持的类型**：
- `github-releases`：GitHub Releases 页面（推荐）
- `web-js`：需要 JavaScript 渲染的网页

## 📊 输出文件

生成的周报保存在：`data/reports/weekly_report_时间戳.md`

## 🚀 快速开始

1. **克隆项目**：
   ```bash
   git clone https://github.com/weiyuzx/ai-product-tracking.git
   cd ai-product-tracking
   ```

2. **生成周报**：
   ```bash
   /tracking-report --days 7
   ```

第一次使用时，skill 会自动检查并提示安装依赖。

## 💻 跨平台支持

本项目支持在以下操作系统上运行：

- **Windows** (Windows 10/11)
- **macOS** (macOS 10.15+)
- **Linux** (Ubuntu, Debian, Fedora 等)

无需额外配置，自动适配各平台的编码、路径和命令差异。
