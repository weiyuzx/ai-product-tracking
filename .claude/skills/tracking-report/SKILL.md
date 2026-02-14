---
name: tracking-report
description: 生成AI产品更新报告（日报/周报/月报）
parameters:
  days:
    description: "统计周期（天数），默认1天（1=日报，7=周报，28+=月报）"
    default: 1
---

你是一个AI产品更新报告生成助手。请按以下步骤生成报告：

## 步骤 0：环境检查

### 0.1 检测操作系统

首先检测当前操作系统，然后执行相应的安装步骤：

**检测命令（跨平台）：**
```bash
# 自动检测操作系统
python3 -c "import platform; os_name = platform.system(); print('Windows' if os_name == 'Windows' else 'macOS' if os_name == 'Darwin' else 'Linux')" 2>/dev/null || python -c "import platform; os_name = platform.system(); print('Windows' if os_name == 'Windows' else 'macOS' if os_name == 'Darwin' else 'Linux')"
```

### 0.2 安装 Python 依赖

**Windows:**
```bash
python -c "from platform_compat import setup_stdio_encoding; setup_stdio_encoding(); import requests, bs4; print('✅ 依赖已安装')" 2>&1 || pip install -r requirements.txt
```

**macOS/Linux:**
```bash
python3 -c "from platform_compat import setup_stdio_encoding; setup_stdio_encoding(); import requests, bs4; print('✅ 依赖已安装')" 2>&1 || pip3 install -r requirements.txt
```

### 0.3 安装 Playwright 浏览器（按需）

检查是否需要安装 Playwright（配置中有 `web-js` 类型产品时需要）：

**Windows:**
```bash
python -c "from platform_compat import setup_stdio_encoding; setup_stdio_encoding(); import playwright; print('✅ Playwright 已安装')" 2>&1 || (echo "安装 Playwright..." && pip install playwright && python -m playwright install chromium)
```

**macOS/Linux:**
```bash
python3 -c "from platform_compat import setup_stdio_encoding; setup_stdio_encoding(); import playwright; print('✅ Playwright 已安装')" 2>&1 || (echo "安装 Playwright..." && pip3 install playwright && python3 -m playwright install chromium)
```

**💡 提示**：项目已包含 `platform_compat.py` 模块，所有 Python 脚本会自动处理编码和路径差异，无需额外配置。

## 步骤 1：更新产品数据

运行增量爬虫，更新 data/raw/ 目录下的产品数据：

**Windows:**
```bash
python main_incremental.py
```

**macOS/Linux:**
```bash
python3 main_incremental.py
```

## 步骤 2：生成报告提示词

基于最新数据生成报告提示词：

**Windows:**
```bash
python generate_report_prompt.py --days {{days}}
```

**macOS/Linux:**
```bash
python3 generate_report_prompt.py --days {{days}}
```

## 步骤 3：读取提示词

读取生成的提示词文件：

**Windows (PowerShell):**
```powershell
Get-Content data\_temp_prompt.txt
```

**Windows (CMD):**
```cmd
type data\_temp_prompt.txt
```

**macOS/Linux:**
```bash
cat data/_temp_prompt.txt
```

## 步骤 4：生成报告

基于提示词生成报告，要求：

1. **内容要求**：
   - 使用提示词中定义的报告模板
   - 提炼新功能和重要改进，忽略常规修复
   - 一句话总结要包含核心更新和趋势分析（重点是准确，不需要严格限制字数）
   - 重点提炼列出3-5条最重要的更新

2. **格式要求**：
   - 使用 emoji 图标（✨新功能、🚀重要更新、⚡改进）
   - 按产品分组展示
   - 每个产品列出3-5个更新点
   - 不标注版本号和时间

3. **保存要求**：
   - 保存到 data/reports/{{report_filename}}
   - 文件名格式：2026-D-02-14.md（日报）/ 2026-W-07.md（周报）/ 2026-M-02.md（月报）
   - 使用 Write 工具保存

4. **输出要求**：
   - 在对话中显示报告预览
   - 告知用户保存的文件路径

## 📝 跨平台兼容性说明

本项目已通过 `platform_compat.py` 模块实现跨平台兼容：

- ✅ **编码处理**：Windows 环境自动设置 UTF-8 编码，支持中文和 emoji 显示
- ✅ **命令适配**：Windows 使用 `python`，macOS/Linux 使用 `python3`
- ✅ **路径处理**：Chrome 浏览器路径自动检测（Windows/macOS/Linux）
- ✅ **Playwright 集成**：自动查找系统 Chrome 或使用 Playwright 内置浏览器

**🔧 技术实现：**
- 所有 Python 脚本导入 `platform_compat` 模块
- 自动调用 `setup_stdio_encoding()` 修复编码问题
- Chrome 路径检测支持：
  - Windows: `C:\Program Files\Google\Chrome\...`
  - macOS: `/Applications/Google Chrome.app/...`
  - Linux: 通过 `which google-chrome` 自动查找

请开始执行。
