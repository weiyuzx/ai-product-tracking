"""
跨平台兼容性模块

统一处理不同操作系统间的差异，包括：
- Windows: 需要设置 UTF-8 编码，使用 `python` 命令
- macOS/Linux: 默认 UTF-8 编码，使用 `python3` 命令

用法：
    from platform_compat import setup_stdio_encoding, get_python_command

    # 在脚本开头调用
    setup_stdio_encoding()

    # 获取适合当前系统的 Python 命令
    python_cmd = get_python_command()
"""

import sys
import platform
from pathlib import Path


def is_windows() -> bool:
    """检测是否为 Windows 系统"""
    return sys.platform == 'win32' or platform.system() == 'Windows'


def is_macos() -> bool:
    """检测是否为 macOS 系统"""
    return sys.platform == 'darwin' or platform.system() == 'Darwin'


def is_linux() -> bool:
    """检测是否为 Linux 系统"""
    return sys.platform.startswith('linux') or platform.system() == 'Linux'


def setup_stdio_encoding():
    """
    设置标准输入输出的编码为 UTF-8

    Windows 终端默认使用 GBK 编码，会导致 emoji 和中文字符显示错误
    macOS/Linux 默认已使用 UTF-8，无需额外设置

    应该在所有脚本的开头调用此函数
    """
    if is_windows():
        try:
            sys.stdout.reconfigure(encoding='utf-8')
            sys.stderr.reconfigure(encoding='utf-8')
        except Exception:
            # 如果配置失败，忽略错误（某些环境可能不支持）
            pass


def get_python_command() -> str:
    """
    获取适合当前系统的 Python 命令

    Returns:
        Windows: 'python'
        macOS/Linux: 'python3'
    """
    if is_windows():
        return 'python'
    else:
        return 'python3'


def get_pip_command() -> str:
    """
    获取适合当前系统的 pip 命令

    Returns:
        Windows: 'pip'
        macOS/Linux: 'pip3'
    """
    if is_windows():
        return 'pip'
    else:
        return 'pip3'


def get_playwright_install_command() -> str:
    """
    获取适合当前系统的 Playwright 浏览器安装命令

    Returns:
        完整的安装命令字符串
    """
    python_cmd = get_python_command()
    return f'{python_cmd} -m playwright install chromium'


def format_system_info() -> str:
    """
    获取格式化的系统信息，用于调试

    Returns:
        系统信息字符串
    """
    return (
        f"Platform: {platform.system()} {platform.release()}\n"
        f"Python: {platform.python_version()}\n"
        f"Platform module: {sys.platform}\n"
        f"Detected OS: {'Windows' if is_windows() else 'macOS' if is_macos() else 'Linux'}"
    )


def ensure_utf8_env():
    """
    确保环境变量设置正确的编码

    主要用于 Windows 系统，设置 PYTHONIOENCODING 环境变量
    """
    if is_windows():
        import os
        os.environ['PYTHONIOENCODING'] = 'utf-8'


# 自动执行（可选）
# setup_stdio_encoding()
