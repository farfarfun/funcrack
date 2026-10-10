# Changelog

## [0.0.1] - 未发布

### 新增

- 初始化占位包结构（`src/funcrack`、`py.typed`、`tests/`），用于保留 PyPI 包名。
- 补充 MIT LICENSE 与 `[tool.ruff]` 配置。
- README 增加「开发」小节：`uv sync`、`pytest`、`ruff check` / `ruff format --check`，以及走 `funbuild` 的构建发布命令。

### 变更

- `__version__` 改为从发行元数据读取，版本号唯一来源为 `pyproject.toml` 的 `[project].version`，不再在 `src/funcrack/__init__.py` 里二次硬编码。
- CHANGELOG 改用规范的中文分类（`新增` / `修复` / `变更` / `废弃`）。
- README 小节标题统一为中文、补齐最小可运行示例；移除可直接粘贴执行的远程脚本命令（`curl ... && bash ...`），改为标注第三方来源与执行风险。
- `pyproject.toml` 的 description 与 README 简介不再声称「无代码 / 没有可执行代码」，改为据实说明仓库主体是链接清单、另附用于保留包名的最小 Python 包。
