"""
周期汇总编译工具 - 按周期汇总各产品的更新日志

使用方法：
    python compile_summary.py --days 1   # 日报
    python compile_summary.py --days 7   # 周报
    python compile_summary.py --days 28  # 月报
"""
import json
import argparse
from pathlib import Path
from datetime import datetime, timedelta, date
from platform_compat import setup_stdio_encoding

# 跨平台兼容性设置
setup_stdio_encoding()


def get_summary_type(days: int) -> str:
    """根据天数判断汇总类型"""
    if days == 1:
        return '日报'
    elif days == 7:
        return '周报'
    elif days >= 28:
        return '月报'
    else:
        return f'{days}天报告'


def get_summary_filename(days: int) -> str:
    """生成汇总文件名：2026-D-02-14 / 2026-W-07 / 2026-M-02"""
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


def main():
    """主函数"""
    parser = argparse.ArgumentParser(description='编译周期汇总')
    parser.add_argument('--days', type=int, default=1, help='周期天数（默认：1）')

    args = parser.parse_args()
    days = args.days

    summary_type = get_summary_type(days)
    print("=" * 60)
    print(f"周期汇总编译工具 - 最近 {days} 天 ({summary_type})")
    print("=" * 60)

    # 确保汇总目录存在
    summary_dir = Path(__file__).parent / 'data' / 'summary'
    summary_dir.mkdir(parents=True, exist_ok=True)

    # 生成汇总文件名
    summary_filename = get_summary_filename(days)
    output_path = summary_dir / summary_filename

    # 收集所有产品更新
    print(f"\n📊 收集所有产品更新...")
    all_updates = collect_all_updates(days=days)

    # 计算周期显示的起止日期
    start_date = (date.today() - timedelta(days=days)).strftime('%Y-%m-%d')
    end_date = date.today().strftime('%Y-%m-%d')

    # 添加周期信息到文件开头
    header = f"""# AI产品更新日志汇总

**周期：{start_date} 至 {end_date}**
**数据范围：最近 {days} 天**

"""

    # 保存汇总文件
    full_content = header + all_updates
    output_path.write_text(full_content, encoding='utf-8')

    print(f"\n✅ 汇总文件已生成")
    print(f"📄 保存位置: {output_path}")
    print(f"📊 包含产品数: {len(load_config()['products'])}")


if __name__ == "__main__":
    main()
