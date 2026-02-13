from typing import Dict, Any, Optional
from .base import BaseScraper
import sys
from pathlib import Path

# 导入 platform_compat 模块
sys.path.insert(0, str(Path(__file__).parent.parent))
from platform_compat import is_windows, is_macos, is_linux


class JSRendererScraper(BaseScraper):
    """支持 JavaScript 渲染的网页爬虫（使用 Playwright）"""

    def __init__(self, product: Dict[str, Any]):
        # 不调用父类 __init__，因为配置结构不同
        self.name = product['name']
        self.type = product.get('type', 'web-js')
        self.url = product['url']
        self._browser = None
        self._playwright = None

    def _find_chrome_path(self) -> Optional[str]:
        """
        查找系统 Chrome 浏览器的可执行文件路径

        Returns:
            Chrome 可执行文件路径，如果找不到则返回 None
        """
        import os
        import shutil

        # Windows Chrome 路径
        if is_windows():
            possible_paths = [
                r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
                os.path.expandvars(r"%LocalAppData%\Google\Chrome\Application\chrome.exe"),
            ]
            for path in possible_paths:
                if os.path.exists(path):
                    return path

        # macOS Chrome 路径
        elif is_macos():
            possible_paths = [
                "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
                "/Applications/Google Chrome Beta.app/Contents/MacOS/Google Chrome Beta",
                "/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary",
            ]
            for path in possible_paths:
                if os.path.exists(path):
                    return path

        # Linux Chrome 路径
        elif is_linux():
            # 尝试通过命令查找
            chrome_commands = ['google-chrome', 'google-chrome-stable', 'chromium', 'chromium-browser']
            for cmd in chrome_commands:
                chrome_path = shutil.which(cmd)
                if chrome_path:
                    return chrome_path

        return None

    def _init_playwright(self):
        """初始化 Playwright"""
        if self._playwright is None:
            try:
                from playwright.sync_api import sync_playwright
                self._playwright_ctx = sync_playwright().start()

                # 尝试使用系统 Chrome
                chrome_path = self._find_chrome_path()

                if chrome_path:
                    print(f"  使用系统 Chrome: {chrome_path}")
                    self._browser = self._playwright_ctx.chromium.launch(
                        headless=True,
                        executable_path=chrome_path,
                        args=['--no-sandbox', '--disable-setuid-sandbox']
                    )
                else:
                    # 使用 Playwright 自带的浏览器
                    print(f"  使用 Playwright Chromium...")
                    self._browser = self._playwright_ctx.chromium.launch(
                        headless=True,
                        args=['--no-sandbox', '--disable-setuid-sandbox']
                    )

            except ImportError:
                raise ImportError(
                    "Playwright 未安装。请运行: pip install playwright"
                )
            except Exception as e:
                raise Exception(f"Playwright 初始化失败: {e}")

    def fetch(self) -> str:
        """从需要 JavaScript 渲染的网页获取内容"""
        print(f"正在爬取 {self.name} 的更新日志（使用 Playwright JS 渲染）...")
        print(f"  URL: {self.url}")

        self._init_playwright()

        try:
            page = self._browser.new_page()

            # 设置超时和用户代理
            page.set_default_timeout(60000)
            page.set_extra_http_headers({
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
            })

            # 访问页面并等待加载
            page.goto(self.url, wait_until="networkidle", timeout=60000)

            # 等待内容加载
            page.wait_for_load_state("domcontentloaded")

            # 滚动页面触发懒加载
            page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            import time
            time.sleep(2)

            # 获取页面文本
            content = page.inner_text("body")

            page.close()

            # 限制长度
            if len(content) > 100000:
                content = content[:100000] + "\n\n... (内容过长，已截断)"

            print(f"  ✓ 成功获取 {len(content)} 字符")

            return content

        except Exception as e:
            raise Exception(f"Playwright 渲染失败: {e}")

    def __del__(self):
        """清理资源"""
        if self._browser:
            try:
                self._browser.close()
            except:
                pass
        if hasattr(self, '_playwright_ctx') and self._playwright_ctx:
            try:
                self._playwright_ctx.stop()
            except:
                pass
