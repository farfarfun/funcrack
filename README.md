# funcrack

个人收藏的软件激活与下载资源链接清单：JetBrains 系列激活工具、Mac 软件下载站等。仓库主体是下面这份链接清单，另外附带一个最小 Python 包（`src/funcrack/`，只暴露 `__version__`）用于保留 `funcrack` 这个包名。

## 安装

链接清单直接看本文件即可，**不需要安装任何东西**。

包内除 `__version__` 外不提供任何 API。确实需要在环境里引用时，可以从源码安装：

```bash
pip install git+https://github.com/farfarfun/funcrack.git
```

## 最小示例

```python
import funcrack

print(funcrack.__version__)
```

## JetBrains 系列

> ⚠️ 下面都是**第三方站点**，不受本组织维护，也没有做过安全审计。这类站点常见的一键脚本（形如 `curl ... | bash`）会从外部地址下载并**以当前用户权限直接执行任意代码**，可能改写 IDE 配置、写入系统目录甚至植入后门。本仓库因此**不提供**可直接粘贴执行的命令。如确需使用，请自行承担风险，并至少做到：先把脚本下载到本地、完整通读内容、核对站点给出的校验值，再在隔离环境里执行。

- [ckey](https://ckey.run/) — 站点上有自己的使用说明，按上面的注意事项自行评估
- [热心大佬](https://3.jetbra.in/)

## Mac 软件

- [未来软件园](https://mac.macxz.com/) — 第三方下载站，安装包来源不明，下载后请自行扫描校验

## 开发

开发依赖（`pytest`、`ruff`）定义在 `pyproject.toml` 的 `[dependency-groups].dev` 中，由 `uv` 管理：

```bash
uv sync
```

测试与静态检查：

```bash
uv run pytest -q
uv run ruff check .
uv run ruff format --check .
```

构建与发布走 `funbuild`，不要手写发布脚本：

```bash
funbuild install   # 本地构建并安装，验证当前代码可安装（不发布、不打标签）
funbuild build     # 完整发布流程：递增版本、构建、安装校验、发布 PyPI、推送并打标签
```

---

## 关于 farfarfun

[farfarfun](https://github.com/farfarfun) 是一个专注于实用工具库的开源组织，
涵盖云存储、数据处理、AI、多媒体与开发工具链等方向。

- 🏠 组织主页：<https://github.com/farfarfun>
- 📦 PyPI：<https://pypi.org/user/niuliangtao/>
- 📧 联系：farfarfun@qq.com

本项目基于 [MIT](LICENSE) 协议开源。
