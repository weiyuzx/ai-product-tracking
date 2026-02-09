from .base import BaseScraper
from .github_releases import GitHubReleasesScraper
from .js_renderer import JSRendererScraper


def create_scraper(product: dict) -> BaseScraper:
    """工厂函数：根据产品类型创建对应的爬虫"""
    scraper_type = product.get('type', 'github-releases')

    if scraper_type == 'github-releases':
        return GitHubReleasesScraper(product)
    elif scraper_type == 'web-js':
        return JSRendererScraper(product)
    else:
        raise ValueError(f"Unsupported scraper type: {scraper_type}")
