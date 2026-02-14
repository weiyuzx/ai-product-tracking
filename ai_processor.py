"""
AI处理器 - 使用Claude内置能力进行提炼和翻译
"""
import os
import json
from pathlib import Path
from datetime import datetime, timedelta
from typing import List, Dict, Any
from platform_compat import setup_stdio_encoding

# 跨平台兼容性设置（在导入后立即执行）
setup_stdio_encoding()


class AIProcessor:
    """AI处理器，用于提炼和翻译"""

    def __init__(self, prompts_path: str = None):
        """
        初始化AI处理器

        Args:
            prompts_path: 提示词配置文件路径
        """
        if prompts_path is None:
            prompts_path = Path(__file__).parent / "config" / "prompts.json"

        with open(prompts_path, 'r', encoding='utf-8') as f:
            self.prompts = json.load(f)

    def translate(self, text: str) -> str:
        """
        翻译文本到中文

        Args:
            text: 待翻译的文本

        Returns:
            翻译后的文本
        """
        prompt = self.prompts['translation']['prompt'].format(text=text)
        # 这里返回提示词，实际使用时会在skill中调用Claude
        return prompt

    def generate_weekly_report(self, text: str, days: int = 7) -> str:
        """
        生成周报

        Args:
            text: 更新日志内容
            days: 周期天数

        Returns:
            周报提示词
        """
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)

        prompt = self.prompts['weekly_report']['prompt'].format(
            text=text,
            start_date=start_date.strftime('%Y-%m-%d'),
            end_date=end_date.strftime('%Y-%m-%d')
        )

        return prompt

    def filter_recent_updates(self, content: str, days: int = 7) -> str:
        """
        过滤最近N天的更新

        Args:
            content: 更新日志内容
            days: 天数

        Returns:
            过滤后的内容
        """
        lines = content.split('\n')
        result = []
        cutoff_date = datetime.now() - timedelta(days=days)

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
                        version_date = datetime.strptime(date_str, '%Y-%m-%d')
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


def test_ai_processor():
    """测试AI处理器"""
    print("=" * 60)
    print("AI处理器测试")
    print("=" * 60)

    # 初始化处理器
    processor = AIProcessor()

    # 读取测试数据
    data_dir = Path(__file__).parent / "data" / "raw"
    claude_file = data_dir / "Claude Code.md"

    print(f"\n📂 读取文件: {claude_file.name}")
    content = claude_file.read_text(encoding='utf-8')

    # 测试过滤最近7天的更新
    print(f"\n🔍 过滤最近7天的更新...")
    recent_content = processor.filter_recent_updates(content, days=7)

    print(f"\n原始内容长度: {len(content)} 字符")
    print(f"过滤后长度: {len(recent_content)} 字符")

    # 显示部分内容
    print(f"\n📄 过滤后的内容预览:")
    print("-" * 60)
    lines = recent_content.split('\n')
    for line in lines[:20]:
        print(line)
    if len(lines) > 20:
        print(f"... (共 {len(lines)} 行)")
    print("-" * 60)

    # 生成周报提示词
    print(f"\n📝 生成周报提示词...")
    report_prompt = processor.generate_weekly_report(recent_content, days=7)

    # 保存提示词到文件供查看
    prompt_file = Path(__file__).parent / "data" / "weekly_report_prompt.txt"
    prompt_file.write_text(report_prompt, encoding='utf-8')
    print(f"✅ 周报提示词已保存到: {prompt_file}")

    # 测试翻译提示词
    print(f"\n🌐 生成翻译提示词...")
    translate_prompt = processor.translate(recent_content[:500])  # 只翻译前500字符

    # 保存提示词到文件供查看
    translate_file = Path(__file__).parent / "data" / "translate_prompt.txt"
    translate_file.write_text(translate_prompt, encoding='utf-8')
    print(f"✅ 翻译提示词已保存到: {translate_file}")

    print(f"\n✅ 测试完成！")
    print(f"\n💡 下一步: 查看生成的提示词文件，然后在Claude中使用这些提示词进行实际处理")


if __name__ == "__main__":
    test_ai_processor()
