from abc import ABC, abstractmethod
from typing import Dict, Any
import requests


class BaseScraper(ABC):
    """爬虫基类"""

    def __init__(self, product: Dict[str, Any]):
        self.name = product['name']
        self.url = product['url']
        self.type = product['type']

    @abstractmethod
    def fetch(self) -> str:
        """获取更新日志内容"""
        pass

    def _get_headers(self) -> Dict[str, str]:
        """获取请求头"""
        return {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
