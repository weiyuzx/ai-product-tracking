#!/usr/bin/env python3
"""
AI 产品更新日志自动收集系统（累积模式）
- 一个产品一个固定文件
- 按版本号去重和覆盖
- 时间逆序排列
"""

import json
import os
import time
from pathlib import Path
from datetime import datetime
from scrapers import create_scraper
from scrapers.parser import ChangelogParser
from platform_compat import setup_stdio_encoding

# 跨平台兼容性设置
setup_stdio_encoding()


# 配置路径
CONFIG_FILE = Path(__file__).parent / 'config' / 'products.json'
DATA_DIR = Path(__file__).parent / 'data' / 'raw'


def load_config():
    """加载产品配置"""
    with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)


def read_existing_versions(product_name: str, content: str) -> set:
    """
    从现有文件中提取已存在的版本号

    Returns:
        版本号集合，如 {"2.1.37", "2.1.36", ...}
    """
    parser = ChangelogParser(days=30)

    # 使用通用解析器提取版本号
    versions = set()
    pattern = r'^## \[([^\]]+)\]'

    import re
    for line in content.split('\n'):
        match = re.match(pattern, line)
        if match:
            versions.add(match.group(1))

    return versions


def merge_and_save_updates(product_name: str, existing_versions: set, new_content: str):
    """
    合并新旧数据，按时间逆序保存

    Args:
        product_name: 产品名称
        existing_versions: 已存在的版本号集合
        new_content: 新爬取的完整内容
    """
    # 解析新数据中的版本
    parser = ChangelogParser(days=30)
    new_updates = parser.parse(product_name, new_content)

    # 读取旧数据
    data_file = DATA_DIR / f"{product_name}.md"
    old_updates = []

    if data_file.exists():
        old_content = data_file.read_text(encoding='utf-8')
        old_updates = parser.parse(product_name, old_content)

    # 构建版本到内容的映射（旧数据）
    version_map = {}
    for update in old_updates:
        version = update['version']
        version_map[version] = update

    # 用新数据更新/添加版本
    for update in new_updates:
        version = update['version']
        version_map[version] = update  # 新版本覆盖，已存在版本也用新数据覆盖

    # 按日期排序（时间逆序）
    all_updates = list(version_map.values())
    all_updates.sort(key=lambda x: x['date'] or datetime.min, reverse=True)

    # 确保目录存在
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    # 写入文件
    lines = []
    lines.append(f"# {product_name} Changelog\n")
    lines.append(f"最后更新: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    lines.append("")

    for update in all_updates:
        version = update['version']
        date = update['date']
        content = update['content']

        if date:
            date_str = date.strftime('%Y-%m-%d')
            lines.append(f"## [{version}] - {date_str}")
        else:
            lines.append(f"## [{version}]")

        lines.append("")
        lines.append(content)
        lines.append("")
        lines.append("")

    output = '\n'.join(lines)

    with open(data_file, 'w', encoding='utf-8') as f:
        f.write(output)

    print(f"  ✓ 已更新文件: {data_file}")
    print(f"    总版本数: {len(all_updates)}")
    print(f"    新增版本: {len(new_updates)}")

    return data_file


def main():
    """主函数"""
    print("=" * 60)
    print("AI 产品更新日志收集系统（累积模式）")
    print("=" * 60)
    print()

    # 加载配置
    config = load_config()
    products = config['products']

    print(f"找到 {len(products)} 个产品需要追踪")
    print()

    # 收集所有产品的更新日志
    results = []

    for product in products:
        try:
            product_name = product['name']

            # 读取现有文件
            data_file = DATA_DIR / f"{product_name}.md"
            existing_versions = set()

            if data_file.exists():
                print(f"📂 {product_name}: 发现现有文件")
                existing_content = data_file.read_text(encoding='utf-8')
                existing_versions = read_existing_versions(product_name, existing_content)
                print(f"   已有 {len(existing_versions)} 个版本")
            else:
                print(f"🆕 {product_name}: 首次爬取")

            # 创建爬虫并获取新数据
            scraper = create_scraper(product)
            new_content = scraper.fetch()

            # 合并并保存
            filepath = merge_and_save_updates(product_name, existing_versions, new_content)

            results.append({
                'name': product_name,
                'url': product.get('url', ''),
                'status': 'success',
                'file': str(filepath)
            })

            print()

            # 产品之间添加0.5秒延迟，避免触发API限流
            time.sleep(0.5)

        except Exception as e:
            print(f"  ✗ 失败: {e}")
            print()
            results.append({
                'name': product['name'],
                'url': product.get('url', ''),
                'status': 'failed',
                'error': str(e)
            })

    # 汇总报告
    print("=" * 60)
    print("爬取完成！")
    print("=" * 60)
    print()

    success_count = sum(1 for r in results if r['status'] == 'success')
    print(f"成功: {success_count}/{len(results)}")

    for r in results:
        if r['status'] == 'success':
            print(f"  ✅ {r['name']}: {r['file']}")
        else:
            print(f"  ❌ {r['name']}: {r.get('error', 'Unknown error')}")


if __name__ == '__main__':
    main()
