from typing import Dict, Any
import requests
import re
import time
from datetime import datetime

class GitHubReleasesScraper:
    """GitHub Releases 爬虫"""

    def __init__(self, product: Dict[str, Any]):
        self.name = product['name']
        self.type = product.get('type', 'github-releases')
        self.url = product['url']

        # 从 URL 中提取 owner 和 repo
        # https://github.com/anthropics/claude-code/releases
        match = re.search(r'github\.com/([^/]+)/([^/]+)/releases', self.url)
        if not match:
            raise ValueError(f"无法从 URL 中提取 owner/repo: {self.url}")

        self.owner = match.group(1)
        self.repo = match.group(2)

    def _get_headers(self) -> Dict[str, str]:
        """获取请求头"""
        return {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'application/vnd.github.v3+json'
        }

    def fetch(self) -> str:
        """从 GitHub Releases 获取更新日志（带重试机制）"""
        print(f"正在爬取 {self.name} 的 Releases...")
        print(f"  URL: {self.url}")

        # 获取最近100个 releases（然后过滤）
        api_url = f"https://api.github.com/repos/{self.owner}/{self.repo}/releases?per_page=100"

        # 重试机制：最多2次
        max_retries = 2
        timeout = 60  # 固定60秒超时

        for attempt in range(max_retries):
            try:
                print(f"  尝试 {attempt + 1}/{max_retries} (超时: {timeout}秒)...")

                response = requests.get(api_url, headers=self._get_headers(), timeout=timeout)
                response.raise_for_status()

                releases = response.json()

                if not releases:
                    raise Exception(f"未找到 {self.name} 的 releases")

                # 过滤掉自动构建版本（如 cli-build-xxx）
                filtered_releases = []
                for release in releases:
                    tag_name = release.get('tag_name', '')
                    # 跳过自动构建版本
                    if not tag_name or 'cli-build-' in tag_name or 'build-' in tag_name:
                        continue
                    filtered_releases.append(release)

                    # 只保留前30个有效的 release
                    if len(filtered_releases) >= 30:
                        break

                if not filtered_releases:
                    raise Exception(f"未找到 {self.name} 的有效 releases")

                # 格式化为 CHANGELOG 格式
                content = self._format_releases(filtered_releases)

                print(f"  ✓ 成功获取 {len(content)} 字符")
                return content

            except requests.exceptions.Timeout as e:
                if attempt < max_retries - 1:
                    print(f"  ⏱ 超时，3秒后重试...")
                    time.sleep(3)
                else:
                    raise Exception(f"请求超时（已重试{max_retries}次）: {str(e)}")
            except requests.exceptions.ConnectionError as e:
                if attempt < max_retries - 1:
                    print(f"  🔌 连接错误，3秒后重试...")
                    time.sleep(3)
                else:
                    raise Exception(f"连接失败（已重试{max_retries}次）: {str(e)}")
            except requests.exceptions.HTTPError as e:
                # HTTP错误不重试（如404、403等）
                raise Exception(f"HTTP错误: {str(e)}")
            except Exception as e:
                if attempt < max_retries - 1:
                    print(f"  ⚠️ 未知错误，3秒后重试: {str(e)}")
                    time.sleep(3)
                else:
                    raise Exception(f"获取失败（已重试{max_retries}次）: {str(e)}")

    def _format_releases(self, releases: list) -> str:
        """将 releases 格式化为 CHANGELOG 格式"""
        lines = []
        lines.append(f"# {self.name} Changelog\n")

        for release in releases:
            tag_name = release.get('tag_name', '')
            published_at = release.get('published_at', '')
            body = release.get('body', '')

            # 移除 tag 前的 'v'
            version = tag_name.lstrip('v') if tag_name else 'Unknown'

            # 解析日期
            if published_at:
                dt = datetime.fromisoformat(published_at.replace('Z', '+00:00'))
                date_str = dt.strftime('%Y-%m-%d')
            else:
                date_str = 'Unknown'

            # 格式化输出
            lines.append(f"## [{version}] - {date_str}")
            lines.append("")

            if body:
                # 清理 body
                body = body.strip()
                lines.append(body)
            else:
                lines.append("No release notes.")

            lines.append("")

        return '\n'.join(lines)
