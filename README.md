# AI 产品更新日志自动收集系统

自动追踪 AI 产品的更新日志，支持按时间范围生成周报。

## 📦 支持的产品

| 产品 | 数据源 | 状态 |
|------|--------|------|
| Claude | GitHub Releases | ✅ |
| OpenClaw | GitHub Releases | ✅ |
| Cline | GitHub Releases | ✅ |
| RooCode | GitHub Releases | ✅ |
| Trae | 官网（JS渲染） | ✅ |

## 🚀 快速开始

### 安装依赖

```bash
pip install -r requirements.txt
playwright install chromium  # Trae 需要
```

### 运行爬虫

```bash
python main.py              # 爬取所有产品的更新日志
python test_weekly.py        # 生成一周内的更新汇总
```

## ⚙️ 配置文件

### 通用配置格式

`config/products.json` 支持以下爬取类型：

#### 1. GitHub Releases（推荐）

适用于有 GitHub releases 的产品，**自动包含发布日期**。

```json
{
  "name": "Claude",
  "type": "github-releases",
  "source": {
    "owner": "anthropics",
    "repo": "claude-code"
  }
}
```

#### 2. 普通网页

适用于无需 JS 渲染的网页。

```json
{
  "name": "Example",
  "type": "web",
  "source": {
    "url": "https://example.com/changelog"
  }
}
```

#### 3. JS 渲染网页

适用于需要 JavaScript 渲染的网页（使用 Playwright）。

```json
{
  "name": "Trae",
  "type": "web-js",
  "source": {
    "url": "https://docs.trae.ai/ide/changelog"
  }
}
```

### 配置字段说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `name` | string | ✅ | 产品名称 |
| `type` | string | ✅ | 爬取类型：`github-releases`、`web`、`web-js` |
| `source` | object | ✅ | 数据源配置 |
| `source.owner` | string | GitHub | GitHub 仓库所有者 |
| `source.repo` | string | GitHub | GitHub 仓库名称 |
| `source.url` | string | Web | 网页 URL |

## 📂 项目结构

```
auto-tracking/
├── config/
│   └── products.json          # 产品配置
├── scrapers/
│   ├── __init__.py            # 爬虫工厂
│   ├── base.py                # 基类
│   ├── github_releases.py     # GitHub Releases 爬虫
│   ├── web.py                 # 普通网页爬虫
│   ├── js_renderer.py         # JS 渲染爬虫
│   └── parser.py              # 更新日志解析器
├── data/
│   └── raw/                   # 原始数据存储
├── main.py                    # 主程序
├── test_weekly.py             # 一周汇总测试
└── requirements.txt           # 依赖
```

## 🔧 依赖说明

### 基础依赖（所有产品）

- `requests`: HTTP 请求
- `beautifulsoup4`: HTML 解析
- `lxml`: 解析器

### GitHub Releases

- 无额外依赖

### JS 渲染网页（Trae）

- `playwright`: 浏览器自动化
- 系统 Chrome 浏览器（headless 运行，无窗口）

## 📊 输出示例

```bash
$ python test_weekly.py

最近一周产品更新汇总

Claude (6个版本更新):
- 2.1.36 (2026-02-07): Fast mode for Opus 4.6
- 2.1.34 (2026-02-06): Fixed crash when agent teams setting changed
- ...

OpenClaw (4个版本更新):
- 2026.2.6 (2026-02-07): Models: support Anthropic Opus 4.6
- 2026.2.3 (2026-02-05): Telegram: remove @ts-nocheck
- ...
```

## 🎯 下一步

- [ ] 实现 Prompt 模板系统
- [ ] 实现 AI 提炼要点功能
- [ ] 实现翻译功能
- [ ] 生成 Markdown 周报
