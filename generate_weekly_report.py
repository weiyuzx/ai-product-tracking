"""
周报生成器 - 直接生成最终周报文件
"""
import json
from pathlib import Path
from datetime import datetime
from ai_processor import AIProcessor


def load_config():
    """加载产品配置"""
    config_path = Path(__file__).parent / "config" / "products.json"
    with open(config_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def collect_all_updates(days: int = 7) -> str:
    """
    收集所有产品的最近更新

    Args:
        days: 最近N天

    Returns:
        整合后的更新内容
    """
    config = load_config()
    processor = AIProcessor()
    data_dir = Path(__file__).parent / "data" / "raw"

    all_content = []
    all_content.append("# 所有产品更新日志")
    all_content.append(f"\n数据范围: 最近 {days} 天\n")

    for product in config['products']:
        product_name = product['name']
        product_file = data_dir / f"{product_name}.md"

        if not product_file.exists():
            print(f"⚠️  文件不存在: {product_file}")
            continue

        print(f"📂 读取 {product_name}...")
        content = product_file.read_text(encoding='utf-8')

        # 过滤最近N天的更新
        recent_content = processor.filter_recent_updates(content, days=days)

        if recent_content.strip():
            all_content.append(f"\n## {product_name}\n")
            all_content.append(recent_content)

    return '\n'.join(all_content)


def generate_weekly_report(days: int = 7):
    """
    生成周报 markdown 文件

    Args:
        days: 周期天数
    """
    print("=" * 60)
    print(f"周报生成器 - 最近 {days} 天")
    print("=" * 60)

    # 创建报告目录
    reports_dir = Path(__file__).parent / "data" / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)

    # 生成时间戳文件名
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    report_filename = f"weekly_report_{timestamp}.md"

    # 收集所有产品更新
    print(f"\n📊 收集所有产品更新...")
    all_updates = collect_all_updates(days=days)

    # 生成周报提示词（用于让Claude处理）
    print(f"\n📝 生成周报...")
    processor = AIProcessor()
    report_prompt = processor.generate_weekly_report(all_updates, days=days)

    # 保存提示词到临时文件
    temp_prompt_file = Path(__file__).parent / "data" / "_temp_prompt.txt"
    temp_prompt_file.write_text(report_prompt, encoding='utf-8')

    print(f"✅ 周报提示词已准备好")
    print(f"\n📄 提示词位置: {temp_prompt_file}")
    print(f"\n💡 请将提示词内容发送给Claude，让Claude生成最终的周报")
    print(f"   周报将保存到: {reports_dir / report_filename}")

    return {
        'prompt_file': str(temp_prompt_file),
        'expected_report': str(reports_dir / report_filename),
        'timestamp': timestamp
    }


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='生成AI产品更新周报')
    parser.add_argument('--days', type=int, default=7, help='周期天数 (默认: 7)')

    args = parser.parse_args()
    generate_weekly_report(days=args.days)
