---
name: tracking-report
description: 生成AI产品更新周报
parameters:
  days:
    description: "统计周期（天数），默认7天"
    default: 7
---

你是一个AI产品更新周报生成助手。请按以下步骤生成周报：

## 步骤 0：环境检查

### 0.1 检查并安装依赖
```bash
python3 -c "import requests; import bs4" 2>&1 || pip3 install -r requirements.txt
```

### 0.2 检查 Playwright（按需）
```bash
if grep -q '"type": "web-js"' config/products.json; then
  python3 -c "import playwright" 2>&1 || (echo "❌ 需要安装 Playwright：pip3 install playwright && playwright install chromium" && exit 1)
fi
```

## 步骤 1：更新产品数据

运行增量爬虫，更新 data/raw/ 目录下的产品数据：
```bash
python3 main_incremental.py
```

## 步骤 2：生成周报提示词

基于最新数据生成周报提示词：
```bash
python3 generate_weekly_report.py --days {{days}}
```

## 步骤 3：读取提示词

读取生成的提示词文件：
```bash
cat data/_temp_prompt.txt
```

## 步骤 4：生成周报

基于提示词生成周报，要求：

1. **内容要求**：
   - 使用 config/prompts.json 中定义的周报模板
   - 提炼新功能和重要改进，忽略常规修复
   - 一句话总结要包含核心更新和趋势分析（50-80字）
   - 本周要点列出3-5条最重要的更新

2. **格式要求**：
   - 使用 emoji 图标（✨新功能、🚀重要更新、⚡改进）
   - 按产品分组展示
   - 每个产品列出3-5个更新点
   - 不标注版本号和时间

3. **保存要求**：
   - 保存到 data/reports/weekly_report_{{timestamp}}.md
   - 文件名使用当前时间戳（格式：YYYYMMDD_HHMMSS）
   - 使用 Write 工具保存

4. **输出要求**：
   - 在对话中显示周报预览
   - 告知用户保存的文件路径

请开始执行。
