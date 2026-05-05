#!/usr/bin/env bash
# notebooklm-py 一键安装与启动脚本（Linux / macOS）
#
# 行为：
#   1. 检测/安装 uv（Python 包管理器）
#   2. 在项目根目录创建 .venv（如已存在则复用）
#   3. 以可编辑模式安装本仓库 + [ui,browser] 可选依赖
#   4. 首次运行时执行 `playwright install chromium`
#   5. 若没有认证信息，引导执行 `notebooklm login`
#   6. 启动 `notebooklm ui`
#
# 用法：
#   ./scripts/install_and_run.sh              # 完整流程
#   ./scripts/install_and_run.sh --no-launch  # 只安装、不启动 UI
#   ./scripts/install_and_run.sh --skip-login # 跳过登录引导
#   ./scripts/install_and_run.sh --port 9000  # 指定 UI 端口
#
# 安全：
#   出错即停（set -e），所有依赖都装在 .venv 内，不会污染系统 Python。

set -euo pipefail

# ---------- 颜色 ----------
if [ -t 1 ]; then
    BOLD=$'\033[1m'
    DIM=$'\033[2m'
    GREEN=$'\033[32m'
    YELLOW=$'\033[33m'
    RED=$'\033[31m'
    RESET=$'\033[0m'
else
    BOLD="" DIM="" GREEN="" YELLOW="" RED="" RESET=""
fi
log()  { echo "${BOLD}==>${RESET} $*"; }
warn() { echo "${YELLOW}${BOLD}⚠${RESET} $*" >&2; }
err()  { echo "${RED}${BOLD}✘${RESET} $*" >&2; }
ok()   { echo "${GREEN}✓${RESET} $*"; }

# ---------- 解析参数 ----------
LAUNCH=1
DO_LOGIN=1
PORT=""
while [ $# -gt 0 ]; do
    case "$1" in
        --no-launch)  LAUNCH=0 ;;
        --skip-login) DO_LOGIN=0 ;;
        --port)       PORT="$2"; shift ;;
        --port=*)     PORT="${1#*=}" ;;
        -h|--help)
            grep -E '^# ' "$0" | sed 's/^# \{0,1\}//'
            exit 0
            ;;
        *)
            err "未知参数: $1"
            exit 2
            ;;
    esac
    shift
done

# ---------- 定位项目根 ----------
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$PROJECT_ROOT"
log "项目根目录: ${DIM}${PROJECT_ROOT}${RESET}"

# ---------- 检测 / 安装 uv ----------
if ! command -v uv >/dev/null 2>&1; then
    log "未发现 uv，正在安装到 ~/.local/bin ..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    # 当前 shell 不会自动加载 ~/.local/bin
    export PATH="$HOME/.local/bin:$PATH"
    if ! command -v uv >/dev/null 2>&1; then
        err "uv 安装失败，请参考 https://docs.astral.sh/uv/getting-started/installation/ 手动安装"
        exit 1
    fi
fi
ok "uv: $(uv --version)"

# ---------- 创建 / 复用 venv ----------
if [ ! -d .venv ]; then
    log "创建虚拟环境 .venv ..."
    uv venv .venv
else
    log "复用已存在的 .venv"
fi

# 在当前 shell 中激活，方便后续直接调用 notebooklm
# shellcheck disable=SC1091
source .venv/bin/activate

# ---------- 安装项目 + 可选依赖 ----------
log "安装本仓库 + [ui,browser] 依赖（可编辑模式）..."
uv pip install -e ".[ui,browser]"
ok "Python 依赖安装完成"

# ---------- 自检 ----------
log "自检 ..."
NB_BIN="$(command -v notebooklm || true)"
if [ -z "$NB_BIN" ]; then
    err "找不到 notebooklm 命令。venv 没激活成功？"
    exit 1
fi
EXPECTED_BIN="$PROJECT_ROOT/.venv/bin/notebooklm"
if [ "$NB_BIN" != "$EXPECTED_BIN" ]; then
    warn "notebooklm 解析到的位置不是当前 venv："
    warn "  实际:   $NB_BIN"
    warn "  期望:   $EXPECTED_BIN"
    warn "可能是 ~/.local/bin/ 或其他位置的旧拷贝在拦截。建议："
    warn "  hash -r && deactivate 2>/dev/null && source .venv/bin/activate"
    warn "或者删掉那个旧拷贝再跑本脚本。"
fi
if ! python -c "import playwright" 2>/dev/null; then
    err "playwright Python 包未装入当前 venv。请检查 uv pip install 的输出有无报错。"
    exit 1
fi
ok "notebooklm: $NB_BIN"
ok "playwright Python 包: 已装入 venv"

# ---------- Playwright Chromium ----------
PLAYWRIGHT_DIR="${PLAYWRIGHT_BROWSERS_PATH:-$HOME/.cache/ms-playwright}"
if [ -d "$PLAYWRIGHT_DIR" ] && find "$PLAYWRIGHT_DIR" -maxdepth 2 -name 'chromium*' -type d -print -quit | grep -q .; then
    ok "Playwright Chromium 已安装"
else
    log "下载 Playwright Chromium（一次性，约 150MB）..."
    playwright install chromium
fi

# ---------- 检查认证状态 ----------
NB_HOME="${NOTEBOOKLM_HOME:-$HOME/.notebooklm}"
STORAGE="$NB_HOME/storage_state.json"

# 判断 storage_state.json 是否真的可用：文件存在 + 非空 + 是合法 JSON + 含至少一个 cookie。
# 仅检查文件存在不可靠 —— 可能是空文件或上次登录中断留下的残骸。
auth_is_valid() {
    [ -f "$STORAGE" ] || return 1
    [ -s "$STORAGE" ] || return 1
    python - "$STORAGE" <<'PY' 2>/dev/null
import json, sys
try:
    data = json.load(open(sys.argv[1], encoding="utf-8"))
except Exception:
    sys.exit(1)
cookies = data.get("cookies") if isinstance(data, dict) else None
sys.exit(0 if isinstance(cookies, list) and len(cookies) > 0 else 1)
PY
}

run_login() {
    log "运行 notebooklm login（浏览器会自动打开 Google 登录页）..."
    if ! notebooklm login; then
        err "notebooklm login 失败。可能是浏览器被关闭、网络不通，或 Google 登录中断。"
        err "排查："
        err "  1. 重跑本脚本：./scripts/install_and_run.sh"
        err "  2. 或手动运行：notebooklm login"
        err "  3. 若没有图形界面，到有 GUI 的机器上登录后把 ${STORAGE} 复制过来。"
        exit 1
    fi
    if ! auth_is_valid; then
        err "登录命令完成但未生成有效的 ${STORAGE}。"
        err "请检查浏览器里是否真正完成了 Google 登录。"
        exit 1
    fi
    ok "登录成功，认证已写入 ${STORAGE}"
}

if auth_is_valid; then
    ok "认证信息已就绪：$STORAGE"
elif [ "$DO_LOGIN" = "0" ]; then
    warn "未发现有效认证信息但传入了 --skip-login，UI 启动后会显示红色横幅。"
else
    if [ -e "$STORAGE" ]; then
        warn "${STORAGE} 存在但无效（空文件/损坏/无 cookie），重新登录..."
    else
        warn "未发现认证信息（${STORAGE}），开始登录..."
    fi
    run_login
fi

# ---------- 启动 UI ----------
if [ "$LAUNCH" = "0" ]; then
    log "已跳过启动。后续手动运行: ${BOLD}source .venv/bin/activate && notebooklm ui${RESET}"
    exit 0
fi

log "启动 NotebookLM UI ..."
if [ -n "$PORT" ]; then
    exec notebooklm ui --port "$PORT"
else
    exec notebooklm ui
fi
