"""
报告提示词生成器 - 生成日报/周报/月报提示词文件
"""
import json
import re
from pathlib import Path
from datetime import datetime, timedelta, date
from platform_compat import setup_stdio_encoding

# 跨平台兼容性设置
setup_stdio_encoding()


def get_report_type(days: int) -> str:
    """根据天数判断报告类型"""
    if days == 1:
        return '日报'
    elif days == 7:
        return '周报'
    elif days >= 28:
        return '月报'
    else:
        return f'{days}天报告'


def get_report_filename(days: int) -> str:
    """生成报告文件名：2026-D-02-14 / 2026-W-07 / 2026-M-02"""
    today = date.today()

    if days == 1:
        # Daily: 2026-D-02-14.md
        return today.strftime('%Y-D-%m-%d.md')
    elif days == 7:
        # Weekly: 2026-W-07.md
        week_num = today.isocalendar()[1]
        return f"{today.strftime('%Y')}-W-{week_num:02d}.md"
    elif days >= 28:
        # Monthly: 2026-M-02.md
        return today.strftime('%Y-M-%m.md')
    else:
        # Custom: 2026-C-02-14.md (C for Custom)
        return today.strftime('%Y-C-%m-%d.md')


def load_config():
    """加载产品配置"""
    config_path = Path(__file__).parent / 'config' / 'products.json'
    with open(config_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def filter_recent_updates(content: str, days: int = 7) -> str:
    """
    过滤最近N天的更新（基于日期比较，不涉及时分秒）

    Args:
        content: 更新日志内容
        days: 天数

    Returns:
        过滤后的内容
    """
    lines = content.split('\n')
    result = []
    # 使用 date 对象，只比较日期，不涉及时分秒
    cutoff_date = date.today() - timedelta(days=days)

    current_version = []
    in_version = False
    version_date = None
    should_include = False

    for line in lines:
        # 检测版本标题
        if line.startswith('## ['):
            # 保存上一个版本
            if in_version and should_include:
                result.extend(current_version)

            # 开始新版本
            current_version = [line]
            in_version = True
            should_include = False
            version_date = None

            # 尝试提取日期
            if ' - ' in line:
                date_str = line.split(' - ')[1].strip()
                try:
                    # 解析为 date 对象（不含时分秒）
                    version_date = datetime.strptime(date_str, '%Y-%m-%d').date()
                    # 日期比较：简洁清晰
                    if version_date >= cutoff_date:
                        should_include = True
                except:
                    # 如果无法解析日期，默认包含
                    should_include = True
            else:
                # 没有日期的版本，默认包含
                should_include = True
        else:
            if in_version:
                current_version.append(line)

    # 保存最后一个版本
    if in_version and should_include:
        result.extend(current_version)

    return '\n'.join(result)


def collect_all_updates(days: int = 7) -> str:
    """
    收集所有产品的最近更新

    Args:
        days: 最近N天

    Returns:
        整合后的更新内容
    """
    config = load_config()
    data_dir = Path(__file__).parent / 'data' / 'raw'

    all_content = []
    all_content.append("# 所有产品更新日志\n")
    all_content.append(f"数据范围: 最近 {days} 天\n\n")

    for product in config['products']:
        product_name = product['name']
        product_file = data_dir / f"{product_name}.md"

        if not product_file.exists():
            print(f"⚠️  文件不存在: {product_file}")
            continue

        print(f"📂 读取 {product_name}...")
        content = product_file.read_text(encoding='utf-8')

        # 过滤最近N天的更新
        recent_content = filter_recent_updates(content, days=days)

        if recent_content.strip():
            all_content.append(f"\n## {product_name}\n")
            all_content.append(recent_content)

    return '\n'.join(all_content)


def generate_report_prompt(days: int = 1):
    """
    生成报告提示词文件（用于 skill 使用）

    Args:
        days: 周期天数（默认1天）
    """
    report_type = get_report_type(days)
    print("=" * 60)
    print(f"报告提示词生成器 - 最近 {days} 天 ({report_type})")
    print("=" * 60)

    # 创建报告目录
    reports_dir = Path(__file__).parent / 'data' / 'reports'
    reports_dir.mkdir(parents=True, exist_ok=True)

    # 生成报告文件名
    report_filename = get_report_filename(days)

    # 收集所有产品更新
    print(f"\n📊 收集所有产品更新...")
    all_updates = collect_all_updates(days=days)

    # 计算周期显示的起止日期（基于 date 对象）
    start_date = (date.today() - timedelta(days=days)).strftime('%Y-%m-%d')
    end_date = date.today().strftime('%Y-%m-%d')

    # 生成报告提示词（用于让Claude处理）
    print(f"\n📝 生成{report_type}提示词...")
    report_prompt = f"""你是一个专业的产品更新报告编辑。请从以下更新日志中提取最近{days}天的关键更新，生成一份简洁的{report_type}。

要求：

1. 一句话总结：包含最核心的更新、发展趋势和重要价值点（重点是准确，不需要严格限制字数）
2. 重点提炼：列出新功能、价值点、用户感知强烈的地方（3-5条，带图标）
3. 各产品更新：按产品分组，提炼新功能和重要改进，忽略常规修复
4. 每个产品列出最重要的3-5个更新点，不标注版本号和时间
5. 使用emoji图标增强可读性（✨新功能、🚀重要更新、⚡改进）
6. 先结论再逐级展开

报告格式：

```markdown
# AI产品更新{report_type}

**周期：{start_date} 至 {end_date}**

**一句话总结：** 本周期最核心的更新、发展趋势和重要价值点（重点是准确）

## 重点提炼

🚀 新功能或重要更新
✨ 新功能
🧠 新功能

## 各产品更新

### Claude

✨ 功能1
✨ 功能2
⚡ 功能3

### Cline

✨ 功能1

...
```

请基于以下数据生成{report_type}：

{all_updates}
"""

    # 保存提示词到临时文件
    temp_prompt_file = Path(__file__).parent / 'data' / '_temp_prompt.txt'
    temp_prompt_file.write_text(report_prompt, encoding='utf-8')

    print(f"✅ {report_type}提示词已准备好\n")
    print(f"📄 提示词位置: {temp_prompt_file}\n")
    print(f"💡 请将提示词内容发送给Claude，让Claude生成最终的{report_type}")
    print(f"   {report_type}将保存到: {reports_dir / report_filename}")

    return {
        'prompt_file': str(temp_prompt_file),
        'expected_report': str(reports_dir / report_filename),
        'report_type': report_type,
        'filename': report_filename
    }


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='生成AI产品更新报告提示词')
    parser.add_argument('--days', type=int, default=1, help='周期天数（默认：1）')

    args = parser.parse_args()
    generate_report_prompt(days=args.days)
