# 编译为单文件可执行（中文）

把 NotebookLM Web UI 打包成**一个可分发的二进制文件**，下载后无需安装 Python 即可运行。

> ⚠️ **重要限制**：单文件版本**不内置 Playwright**，因此 `notebooklm login` 不在二进制内。首次登录仍需在任意一台有 Python 的机器上执行 `pip install "notebooklm-py[browser]"; notebooklm login`，然后把 `~/.notebooklm/storage_state.json` 拷过来。原因见文末「为什么不打包 Playwright」。

## 一、 一键编译

```bash
# 从零开始（自动安装 uv、装依赖、编译）
./scripts/build_binary.sh --bootstrap

# 或者：已有 .venv 时直接编译
./scripts/build_binary.sh
```

成功后产物在：

```
dist/
└── notebooklm-ui          # Linux / macOS（约 70MB）
└── notebooklm-ui.exe      # Windows（约 100MB）
```

参数：

| 参数 | 含义 |
| --- | --- |
| `--bootstrap` | 自动 `uv venv` + 安装 `[ui]` + 安装 `[build]`（首次推荐） |
| `--jobs N` | 指定 Nuitka 并行编译任务数（默认按 CPU 自动） |

> 首次编译耗时约 5–15 分钟（取决于 CPU），后续增量构建会快很多。

## 二、 如何使用编译产物

### 第 1 步：在任意 Python 机器上完成登录（仅一次）

```bash
pip install "notebooklm-py[browser]"
playwright install chromium
notebooklm login                  # 浏览器打开 Google 登录页
```

登录信息保存在 `~/.notebooklm/storage_state.json`。

### 第 2 步：在目标机器上启动二进制

将 `dist/notebooklm-ui` **和** `~/.notebooklm/` 目录一起复制到目标机器，然后：

```bash
./notebooklm-ui                   # 默认绑定 127.0.0.1:8765 并打开浏览器
./notebooklm-ui --port 9000       # 指定端口
./notebooklm-ui --no-browser      # 不自动打开浏览器（适合 SSH/headless）
```

### 第 3 步：分发

- **完全免登录使用**：把二进制 + `~/.notebooklm/storage_state.json` 一起分发。**注意**：该文件等同于 NotebookLM 的会话凭证，仅在可信场景共享。
- **每人单独登录**：仅分发二进制；用户按上一步在自己机器上完成登录。

## 三、 手动编译（不使用脚本）

```bash
# 准备环境
uv venv .venv && source .venv/bin/activate
uv pip install -e ".[ui,build]"

# 触发 Nuitka
python -m nuitka \
    --onefile \
    --standalone \
    --output-dir=build/ \
    --output-filename=notebooklm-ui \
    --include-package=notebooklm \
    --include-package-data=notebooklm \
    --include-data-dir=src/notebooklm/web/static=notebooklm/web/static \
    --include-data-dir=src/notebooklm/web/templates=notebooklm/web/templates \
    --include-package=fastapi \
    --include-package=starlette \
    --include-package=uvicorn \
    --include-package=jinja2 \
    --include-package=sse_starlette \
    --include-package=python_multipart \
    --include-package=anyio \
    --include-package=httpx \
    --include-package=click \
    --include-package=pydantic \
    --include-package=pydantic_core \
    --remove-output \
    scripts/launcher.py
```

## 四、 故障排查

### 「ImportError: No module named X」运行时报错

某个 FastAPI/Starlette 子模块通过动态导入加载，Nuitka 静态分析时漏掉了。在 `scripts/build_binary.sh` 的 `NUITKA_ARGS` 中加一行 `--include-package=X`，重新编译。常见漏掉的：`uvicorn.protocols.http.h11_impl`、`uvicorn.lifespan.on`。

### 二进制启动慢（3-5 秒）

正常现象。Nuitka onefile 启动时会把所有依赖解压到临时目录（`/tmp/onefile_*` 或 `%TEMP%\\onefile_*`），首次解压稍慢，后续会复用缓存。**冷启动**可以通过 `--standalone` 改为 `--onefile=False` 避免，但产物会变成一个目录。

### Linux 编译产物在另一台 Linux 上无法运行

通常是 glibc 版本不兼容。建议在最低目标系统（如 Ubuntu 20.04）的 Docker 容器中编译，得到的二进制在更新的发行版上向前兼容。

### macOS 二进制被 Gatekeeper 拒绝

未签名的二进制需要用户右键 → 打开，或：
```bash
xattr -d com.apple.quarantine ./notebooklm-ui
```

正式分发请用 Apple Developer ID 签名 + 公证。

### Windows 反病毒误报

Nuitka onefile 的「自解压」行为在某些杀软的启发式检测下会被误标。
解决：
- 提交样本到杀软厂商；
- 用 EV 代码签名证书签名（最有效，但需要购买）；
- 用 `--standalone`（非 onefile）模式分发整个目录。

## 五、 为什么不打包 Playwright

Playwright 不是纯 Python 包：

- 它通过 Node 子进程驱动浏览器，二进制内嵌 Node 解释器太重。
- 浏览器（Chromium/Firefox/WebKit）由 `playwright install` 在首次运行时下载，而非随包发布。
- 即便用 `--include-package=playwright` 强行包入，运行时仍需要 Node 与浏览器在文件系统上的真实路径，与 Nuitka onefile 的临时解压目录不兼容。

**因此本项目的策略**：
- 单文件二进制 = **UI 服务端**；
- 首次登录 = 由完整 Python 环境的 `pip install "notebooklm-py[browser]"` 提供；
- 登录后认证信息存放在用户主目录，二进制读取该文件即可访问 NotebookLM。

如果将来 Playwright 推出官方静态二进制构建工具，会再考虑全量打包。

## 六、 文件清单

```
scripts/
├── install_and_run.sh      # 一键安装并启动（Linux/macOS, 推荐日常使用）
├── install_and_run.ps1     # 一键安装并启动（Windows PowerShell）
├── launcher.py             # Nuitka 编译入口
└── build_binary.sh         # Nuitka 编译脚本

docs/
├── web-ui.md               # UI 使用说明（英文）
├── web-ui.zh-CN.md         # UI 使用说明（中文）
└── build-binary.zh-CN.md   # 本文档
```
