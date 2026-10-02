"""funcrack 占位包的最小行为测试。

重点是防止版本号漂移：`pyproject.toml` 的 `[project].version` 是唯一来源，
`funcrack.__version__` 必须与之一致。
"""

import re
import unittest
from pathlib import Path

import funcrack

PYPROJECT = Path(__file__).resolve().parent.parent / "pyproject.toml"


def _version_from_pyproject() -> str:
    """从 pyproject.toml 的 [project] 段里取出 version（兼容 3.10，不依赖 tomllib）。"""
    text = PYPROJECT.read_text(encoding="utf-8")
    match = re.search(r'^version\s*=\s*"([^"]+)"', text, flags=re.MULTILINE)
    assert match is not None, "pyproject.toml 里找不到 version"
    return match.group(1)


class PackageTests(unittest.TestCase):
    def test_version_is_non_empty_string(self) -> None:
        self.assertIsInstance(funcrack.__version__, str)
        self.assertTrue(funcrack.__version__)

    def test_version_is_resolved_from_metadata(self) -> None:
        # 包已安装（含 editable）时必须拿到真实版本，而不是回退占位值
        self.assertNotEqual(funcrack.__version__, "0.0.0+unknown")

    def test_version_matches_pyproject(self) -> None:
        self.assertTrue(PYPROJECT.is_file(), f"缺少 {PYPROJECT}")
        self.assertEqual(funcrack.__version__, _version_from_pyproject())

    def test_only_exposes_version(self) -> None:
        self.assertEqual(funcrack.__all__, ["__version__"])


if __name__ == "__main__":
    unittest.main()
