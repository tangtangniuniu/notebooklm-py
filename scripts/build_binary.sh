#!/usr/bin/env bash
# 使用 Nuitka 将 NotebookLM Web UI 编译为单文件可执行文件。
#
# 输出：
#   dist/notebooklm-ui            （Linux / macOS）
#   dist/notebooklm-ui.exe        （Windows）
#
# 用法：
#   ./scripts/build_binary.sh                  # 直接编译（需先建好 venv）
#   ./scripts/build_binary.sh --bootstrap      # 从零开始：建 venv、装依赖、编译
#   ./scripts/build_binary.sh --jobs 8         # 指定并行编译任务数
#
# 依赖：
#   - uv（脚本会在 --bootstrap 模式下自动安装）
#   - Python 3.10+
#   - 编译期：nuitka, ordered-set, zstandard
#   - 运行期：fastapi, uvicorn, jinja2, sse-starlette, python-multipart, httpx, click
#
# 已知限制：
#   - 不打包 Playwright。生成的二进制只包含 Web UI 服务端；首次登录仍需用
#     pip 版 CLI（`notebooklm login`）。
#   - 单文件二进制启动时会先解压到临时目录，比直接 venv 启动慢一些。
#   - macOS / Linux 二进制约 60-90MB；Windows 约 80-120MB。

set -euo pipefail

if [ -t 1 ]; then
    BOLD=$'\033[1m'; DIM=$'\033[2m'; GREEN=$'\033[32m'; YELLOW=$'\033[33m'; RED=$'\033[31m'; RESET=$'\033[0m'
else
    BOLD="" DIM="" GREEN="" YELLOW="" RED="" RESET=""
fi
log()  { echo "${BOLD}==>${RESET} $*"; }
warn() { echo "${YELLOW}${BOLD}⚠${RESET} $*" >&2; }
err()  { echo "${RED}${BOLD}✘${RESET} $*" >&2; }
ok()   { echo "${GREEN}✓${RESET} $*"; }

BOOTSTRAP=0
JOBS=""
while [ $# -gt 0 ]; do
    case "$1" in
        --bootstrap) BOOTSTRAP=1 ;;
        --jobs)      JOBS="$2"; shift ;;
        --jobs=*)    JOBS="${1#*=}" ;;
        -h|--help)
            grep -E '^# ' "$0" | sed 's/^# \{0,1\}//'
            exit 0
            ;;
        *) err "未知参数: $1"; exit 2 ;;
    esac
    shift
done

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$PROJECT_ROOT"

# ---------- 解析平台 / 架构 ----------
case "$(uname -s)" in
    Linux*)   PLATFORM="linux" ;;
    Darwin*)  PLATFORM="macos" ;;
    MINGW*|CYGWIN*|MSYS*) PLATFORM="windows" ;;
    *)        PLATFORM="$(uname -s | tr 'A-Z' 'a-z')" ;;
esac
ARCH="$(uname -m)"
log "目标平台: ${BOLD}${PLATFORM}-${ARCH}${RESET}"

# ---------- 准备 venv ----------
if [ "$BOOTSTRAP" = "1" ]; then
    if ! command -v uv >/dev/null 2>&1; then
        log "安装 uv ..."
        curl -LsSf https://astral.sh/uv/install.sh | sh
        export PATH="$HOME/.local/bin:$PATH"
    fi
    log "创建 / 复用 venv ..."
    [ -d .venv ] || uv venv .venv
    # shellcheck disable=SC1091
    source .venv/bin/activate
    log "安装运行期依赖 + Nuitka ..."
    uv pip install -e ".[ui]"
    uv pip install "nuitka>=2.0" "ordered-set" "zstandard"
elif [ -d .venv ]; then
    # shellcheck disable=SC1091
    source .venv/bin/activate
fi

# ---------- 校验依赖 ----------
PYTHON="${PYTHON:-python}"
if ! "$PYTHON" -c "import nuitka" 2>/dev/null; then
    err "未发现 nuitka。请运行: ${BOLD}$0 --bootstrap${RESET}（或手动 pip install nuitka）"
    exit 1
fi
if ! "$PYTHON" -c "import notebooklm.web" 2>/dev/null; then
    err "未发现 notebooklm.web 模块。请先安装 [ui] 依赖（pip install -e \".[ui]\"）"
    exit 1
fi
log "Python: $($PYTHON --version)"
log "Nuitka: $($PYTHON -m nuitka --version | head -1)"

# ---------- 准备输出目录 ----------
DIST_DIR="$PROJECT_ROOT/dist"
BUILD_DIR="$PROJECT_ROOT/build/nuitka-${PLATFORM}-${ARCH}"
mkdir -p "$DIST_DIR" "$BUILD_DIR"

OUTPUT_BIN_NAME="notebooklm-ui"
[ "$PLATFORM" = "windows" ] && OUTPUT_BIN_NAME="notebooklm-ui.exe"

# ---------- 调用 Nuitka ----------
NUITKA_ARGS=(
    --onefile
    --standalone
    --assume-yes-for-downloads
    --output-dir="$BUILD_DIR"
    --output-filename="$OUTPUT_BIN_NAME"
    --remove-output

    # 项目本身 + 静态资源
    --include-package=notebooklm
    --include-package-data=notebooklm
    --include-data-dir="$PROJECT_ROOT/src/notebooklm/web/static=notebooklm/web/static"
    --include-data-dir="$PROJECT_ROOT/src/notebooklm/web/templates=notebooklm/web/templates"

    # FastAPI / uvicorn 栈（很多动态导入，Nuitka 必须显式列出）
    --include-package=fastapi
    --include-package=starlette
    --include-package=uvicorn
    --include-package=uvicorn.lifespan
    --include-package=uvicorn.loops
    --include-package=uvicorn.protocols
    --include-package=uvicorn.logging
    --include-package=jinja2
    --include-package=sse_starlette
    --include-package=multipart
    --include-package=python_multipart
    --include-package=anyio
    --include-package=sniffio
    --include-package=httpx
    --include-package=httpcore
    --include-package=h11
    --include-package=click
    --include-package=pydantic
    --include-package=pydantic_core
    --include-package=annotated_types
    --include-package=typing_extensions

    # 元信息便于排错
    --company-name=notebooklm-py
    --product-name="NotebookLM UI"
    --file-description="Local web UI for NotebookLM"
)

# 平台微调
case "$PLATFORM" in
    macos)
        NUITKA_ARGS+=( --macos-create-app-bundle=no )
        ;;
    windows)
        NUITKA_ARGS+=( --windows-console-mode=force )
        ;;
esac

if [ -n "$JOBS" ]; then
    NUITKA_ARGS+=( --jobs="$JOBS" )
fi

log "开始 Nuitka 编译（首次约 5-15 分钟，取决于 CPU）..."
"$PYTHON" -m nuitka "${NUITKA_ARGS[@]}" "$PROJECT_ROOT/scripts/launcher.py"

# ---------- 移动产物到 dist/ ----------
SRC_BIN="$BUILD_DIR/$OUTPUT_BIN_NAME"
DST_BIN="$DIST_DIR/$OUTPUT_BIN_NAME"
if [ ! -f "$SRC_BIN" ]; then
    err "编译完成但未找到二进制文件: $SRC_BIN"
    exit 1
fi
mv -f "$SRC_BIN" "$DST_BIN"
chmod +x "$DST_BIN"

SIZE="$(du -h "$DST_BIN" | cut -f1)"
ok "二进制已生成: ${BOLD}$DST_BIN${RESET}（$SIZE）"

cat <<EOF

${BOLD}下一步：${RESET}
  1. 首次登录（仅一次，需要 pip 版 CLI）：
       pip install 'notebooklm-py[browser]'
       playwright install chromium
       notebooklm login

  2. 之后任何机器只要复制这个二进制 + ~/.notebooklm/storage_state.json 即可：
       ./$OUTPUT_BIN_NAME

  3. 若要分发：
       - 同时复制 ~/.notebooklm/ 目录可让收件人无需登录直接使用（注意：该目录
         包含 cookies，等同于你的 NotebookLM 会话凭证，请仅在可信场景内分享）。
       - 或仅分发二进制，让对方按上一步自行登录。
EOF
