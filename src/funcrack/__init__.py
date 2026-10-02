"""funcrack：软件激活与下载资源链接清单（内容见仓库 README）。

本包不提供功能性 API，仅暴露 ``__version__``。版本号的唯一来源是
``pyproject.toml`` 的 ``[project].version``，这里通过发行元数据读取，
避免两处硬编码产生漂移。
"""

from importlib.metadata import PackageNotFoundError
from importlib.metadata import version as _metadata_version

__all__ = ["__version__"]

try:
    __version__: str = _metadata_version("funcrack")
except PackageNotFoundError:  # 直接从源码树导入、包未安装时
    __version__ = "0.0.0+unknown"
