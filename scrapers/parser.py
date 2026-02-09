import re
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional


class ChangelogParser:
    """解析各产品的 changelog 并提取版本和时间信息"""

    def __init__(self, days: int = 7):
        """
        Args:
            days: 提取最近几天的更新，默认7天
        """
        self.days = days
        self.cutoff_date = datetime.now() - timedelta(days=days)

    def parse(self, product_name: str, content: str) -> List[Dict[str, Any]]:
        """
        解析 changelog 内容

        Args:
            product_name: 产品名称
            content: changelog 原始内容

        Returns:
            解析后的更新列表，每个更新包含 version, date, content
        """
        parser_map = {
            'Claude': self._parse_github_with_date,
            'Cline': self._parse_github_with_date,
            'RooCode': self._parse_github_with_date,
            'OpenClaw': self._parse_github_with_date,  # 现在也用 releases，格式相同
            'Trae': self._parse_trae,
        }

        parser_func = parser_map.get(product_name, self._parse_generic)
        updates = parser_func(content)

        # 过滤指定天数内的更新
        filtered_updates = []
        for update in updates:
            if update['date']:
                # 有日期的，检查是否在范围内
                if update['date'] >= self.cutoff_date:
                    filtered_updates.append(update)
            else:
                # 没有日期的，只保留最近5个版本
                if len(filtered_updates) < 5:
                    filtered_updates.append(update)

        return filtered_updates

    def _parse_github_simple(self, content: str) -> List[Dict[str, Any]]:
        """解析格式: ## 2.1.36"""
        updates = []
        pattern = r'^## (\d+\.\d+\.\d+)\s*$'

        current_version = None
        current_content = []

        lines = content.split('\n')
        for i, line in enumerate(lines):
            match = re.match(pattern, line)
            if match:
                # 保存上一个版本
                if current_version:
                    updates.append({
                        'version': current_version,
                        'date': None,  # 无日期信息
                        'content': '\n'.join(current_content).strip()
                    })

                current_version = match.group(1)
                current_content = []
            elif current_version:
                current_content.append(line)

        # 保存最后一个版本
        if current_version:
            updates.append({
                'version': current_version,
                'date': None,
                'content': '\n'.join(current_content).strip()
            })

        return updates

    def _parse_github_brackets(self, content: str) -> List[Dict[str, Any]]:
        """解析格式: ## [3.57.1]"""
        updates = []
        pattern = r'^## \[(\d+\.\d+\.\d+)\]\s*$'

        current_version = None
        current_content = []

        lines = content.split('\n')
        for line in lines:
            match = re.match(pattern, line)
            if match:
                if current_version:
                    updates.append({
                        'version': current_version,
                        'date': None,
                        'content': '\n'.join(current_content).strip()
                    })

                current_version = match.group(1)
                current_content = []
            elif current_version:
                current_content.append(line)

        if current_version:
            updates.append({
                'version': current_version,
                'date': None,
                'content': '\n'.join(current_content).strip()
            })

        return updates

    def _parse_github_with_date(self, content: str) -> List[Dict[str, Any]]:
        """解析格式: ## [3.47.3] - 2026-02-06"""
        updates = []
        pattern = r'^## \[(\d+\.\d+\.\d+)\]\s*-\s*(\d{4}-\d{2}-\d{2})\s*$'

        current_version = None
        current_date = None
        current_content = []

        lines = content.split('\n')
        for line in lines:
            match = re.match(pattern, line)
            if match:
                if current_version:
                    updates.append({
                        'version': current_version,
                        'date': current_date,
                        'content': '\n'.join(current_content).strip()
                    })

                current_version = match.group(1)
                current_date = datetime.strptime(match.group(2), '%Y-%m-%d')
                current_content = []
            elif current_version:
                current_content.append(line)

        if current_version:
            updates.append({
                'version': current_version,
                'date': current_date,
                'content': '\n'.join(current_content).strip()
            })

        return updates

    def _parse_openclaw(self, content: str) -> List[Dict[str, Any]]:
        """解析格式: ## 2026.2.6 (年.月.日)"""
        updates = []
        pattern = r'^## (\d+)\.(\d+)\.(\d+)\s*$'

        current_version = None
        current_date = None
        current_content = []

        lines = content.split('\n')
        for line in lines:
            match = re.match(pattern, line)
            if match:
                if current_version:
                    updates.append({
                        'version': current_version,
                        'date': current_date,
                        'content': '\n'.join(current_content).strip()
                    })

                year, month, day = match.groups()
                current_version = f"{year}.{month}.{day}"
                current_date = datetime(int(year), int(month), int(day))
                current_content = []
            elif current_version:
                current_content.append(line)

        if current_version:
            updates.append({
                'version': current_version,
                'date': current_date,
                'content': '\n'.join(current_content).strip()
            })

        return updates

    def _parse_trae(self, content: str) -> List[Dict[str, Any]]:
        """解析 Trae changelog（支持中文和英文格式）"""
        updates = []

        # 中文格式: 2026 年 02 月 02 日（Hotfix）
        pattern_cn = r'^(\d{4})\s*年\s*(\d{1,2})\s*月\s*(\d{1,2})\s*日'
        # 英文格式: January 23, 2026 (Feature Release)
        pattern_en = r'^(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{1,2}),\s*(\d{4})'

        # 月份映射
        month_map = {
            'January': 1, 'February': 2, 'March': 3, 'April': 4,
            'May': 5, 'June': 6, 'July': 7, 'August': 8,
            'September': 9, 'October': 10, 'November': 11, 'December': 12
        }

        current_date = None
        current_version = None
        current_content = []
        skip_headers = True

        lines = content.split('\n')
        for line in lines:
            # 跳过开头的内容，直到遇到第一个日期
            if skip_headers:
                if re.match(pattern_cn, line) or re.match(pattern_en, line):
                    skip_headers = False
                else:
                    continue

            # 尝试匹配中文日期
            match_cn = re.match(pattern_cn, line)
            match_en = re.match(pattern_en, line)

            if match_cn or match_en:
                # 保存上一个版本
                if current_date:
                    content_str = '\n'.join(current_content).strip()
                    if content_str:
                        updates.append({
                            'version': current_version or '未知版本',
                            'date': current_date,
                            'content': content_str
                        })

                # 解析日期
                if match_cn:
                    year, month, day = match_cn.groups()
                    current_date = datetime(int(year), int(month), int(day))
                else:
                    month_str, day, year = match_en.groups()
                    current_date = datetime(int(year), month_map[month_str], int(day))

                current_version = None
                current_content = []
            elif current_date:
                # 尝试提取版本号
                if not current_version:
                    version_match = re.search(r'v?(\d+\.\d+\.\d+)', line)
                    if version_match:
                        current_version = version_match.group(1)
                # 跳过空行和重复的标题
                line = line.strip()
                if line and not line.startswith('TRAE v'):
                    current_content.append(line)

        # 保存最后一个版本
        if current_date:
            content_str = '\n'.join(current_content).strip()
            if content_str:
                updates.append({
                    'version': current_version or '未知版本',
                    'date': current_date,
                    'content': content_str
                })

        return updates

    def _parse_generic(self, content: str) -> List[Dict[str, Any]]:
        """通用解析器"""
        return [{
            'version': 'unknown',
            'date': None,
            'content': content[:500]
        }]


def format_updates(updates: List[Dict[str, Any]], product_name: str) -> str:
    """格式化更新信息为可读文本"""
    if not updates:
        return f"## {product_name}\n暂无最近一周的更新\n"

    result = [f"## {product_name}"]
    result.append(f"来源: {product_name} 更新日志\n")

    for update in updates:
        version_str = update['version']
        if update['date']:
            date_str = update['date'].strftime('%Y-%m-%d')
            result.append(f"### {version_str} ({date_str})")
        else:
            result.append(f"### {version_str} (日期未知)")

        # 只取前500字符作为预览
        content = update['content']
        if len(content) > 500:
            content = content[:500] + '\n...(内容过长)'
        result.append(content)
        result.append('')

    return '\n'.join(result)
