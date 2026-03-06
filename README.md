# AI 产品追踪系统

自动追踪 AI 产品的更新日志，按周期汇总原始更新内容。

## 🎯 这个项目做什么？

帮你自动收集多个 AI 产品的更新日志，并按指定周期（日报/周报/月报）汇总到一个文件中。

**支持的产品**：
- Claude Code
- OpenCode
- Oh My OpenCode
- OpenClaw
- Cline
- RooCode
- Trae

**项目功能**：
1. **爬取更新日志**：从各产品官网自动获取最新更新
2. **周期汇总**：按天/周/月汇总原始更新内容到一个文件

## 📖 如何使用

### 步骤 1：爬取最新数据

```bash
# Windows
python collect_raw_updates.py

# macOS/Linux
python3 collect_raw_updates.py
```

这会将各产品的最新更新保存到 `data/raw/*.md`

### 步骤 2：按周期汇总

```bash
# 默认生成日报（最近1天）
python compile_summary.py          # Windows
python3 compile_summary.py         # macOS/Linux

# 生成其他周期
python compile_summary.py --days 7    # 周报
python compile_summary.py --days 28   # 月报
```

汇总文件会保存到 `data/summary/*.md`

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

### 原始数据：`data/raw/*.md`

每个产品一个文件，包含所有历史更新，时间逆序排列：
- `data/raw/Claude Code.md`
- `data/raw/OpenCode.md`
- ...

### 汇总数据：`data/summary/*.md`

按周期汇总的原始更新日志：

**文件命名格式**：
- 日报：`2026-D-02-14.md`
- 周报：`2026-W-07.md`
- 月报：`2026-M-02.md`

## 🚀 快速开始

1. **克隆项目**：
   ```bash
   git clone https://github.com/weiyuzx/ai-product-tracking.git
   cd ai-product-tracking
   ```

2. **安装依赖**（首次使用）：
   ```bash
   # Windows
   pip install -r requirements.txt

   # macOS/Linux
   pip3 install -r requirements.txt
   ```

3. **爬取数据**：
   ```bash
   python collect_raw_updates.py
   ```

4. **生成汇总**（默认最近1天）：
   ```bash
   python compile_summary.py          # Windows
   python3 compile_summary.py         # macOS/Linux
   ```

## 💻 跨平台支持

本项目支持在以下操作系统上运行：

- **Windows** (Windows 10/11)
- **macOS** (macOS 10.15+)
- **Linux** (Ubuntu, Debian, Fedora 等)

无需额外配置，自动适配各平台的编码、路径和命令差异。
