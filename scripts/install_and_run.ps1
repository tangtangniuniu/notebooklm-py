# notebooklm-py 一键安装与启动脚本（Windows PowerShell）
#
# 用法（在 PowerShell 中）：
#   .\scripts\install_and_run.ps1               # 完整流程
#   .\scripts\install_and_run.ps1 -NoLaunch     # 只安装、不启动 UI
#   .\scripts\install_and_run.ps1 -SkipLogin    # 跳过登录引导
#   .\scripts\install_and_run.ps1 -Port 9000    # 指定 UI 端口

[CmdletBinding()]
param(
    [switch] $NoLaunch,
    [switch] $SkipLogin,
    [int]    $Port = 0
)

$ErrorActionPreference = "Stop"

function Write-Step($msg) { Write-Host "==> $msg" -ForegroundColor Cyan }
function Write-Ok($msg)   { Write-Host "✓ $msg"  -ForegroundColor Green }
function Write-Warn($msg) { Write-Host "⚠ $msg"  -ForegroundColor Yellow }

# 定位项目根
$ScriptDir   = Split-Path -Parent $MyInvocation.MyCommand.Path
$ProjectRoot = Split-Path -Parent $ScriptDir
Set-Location $ProjectRoot
Write-Step "项目根目录: $ProjectRoot"

# 检测/安装 uv
if (-not (Get-Command uv -ErrorAction SilentlyContinue)) {
    Write-Step "未发现 uv，正在安装 ..."
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    $env:Path = "$HOME\.local\bin;$env:Path"
    if (-not (Get-Command uv -ErrorAction SilentlyContinue)) {
        throw "uv 安装失败，请手动安装：https://docs.astral.sh/uv/getting-started/installation/"
    }
}
Write-Ok "uv: $(uv --version)"

# 创建/复用 venv
if (-not (Test-Path ".venv")) {
    Write-Step "创建虚拟环境 .venv ..."
    uv venv .venv
} else {
    Write-Step "复用已存在的 .venv"
}

# 激活 venv
$Activate = Join-Path ".venv\Scripts" "Activate.ps1"
. $Activate

# 安装依赖
Write-Step "安装本仓库 + [ui,browser] 依赖（可编辑模式）..."
uv pip install -e ".[ui,browser]"
Write-Ok "Python 依赖安装完成"

# Playwright Chromium
$PwDir = $env:PLAYWRIGHT_BROWSERS_PATH
if (-not $PwDir) { $PwDir = Join-Path $env:LOCALAPPDATA "ms-playwright" }
$ChromiumDirs = @()
if (Test-Path $PwDir) {
    $ChromiumDirs = Get-ChildItem -Path $PwDir -Directory -ErrorAction SilentlyContinue |
                    Where-Object { $_.Name -like "chromium*" }
}
if ($ChromiumDirs.Count -gt 0) {
    Write-Ok "Playwright Chromium 已安装"
} else {
    Write-Step "下载 Playwright Chromium（一次性，约 150MB）..."
    playwright install chromium
}

# 认证检查
$NbHome = $env:NOTEBOOKLM_HOME
if (-not $NbHome) { $NbHome = Join-Path $HOME ".notebooklm" }
$Storage = Join-Path $NbHome "storage_state.json"

function Test-AuthValid {
    param([string]$Path)
    if (-not (Test-Path $Path)) { return $false }
    if ((Get-Item $Path).Length -eq 0) { return $false }
    try {
        $data = Get-Content $Path -Raw | ConvertFrom-Json
        return ($data.cookies -is [array]) -and ($data.cookies.Count -gt 0)
    } catch {
        return $false
    }
}

function Invoke-Login {
    Write-Step "运行 notebooklm login（浏览器会自动打开 Google 登录页）..."
    notebooklm login
    if ($LASTEXITCODE -ne 0) {
        Write-Host "✘ notebooklm login 失败。可能是浏览器被关闭、网络不通，或 Google 登录中断。" -ForegroundColor Red
        Write-Host "  排查：重跑本脚本，或手动 notebooklm login。" -ForegroundColor Red
        exit 1
    }
    if (-not (Test-AuthValid -Path $Storage)) {
        Write-Host "✘ 登录命令完成但未生成有效的 $Storage。请确认浏览器里完成了 Google 登录。" -ForegroundColor Red
        exit 1
    }
    Write-Ok "登录成功，认证已写入 $Storage"
}

if (Test-AuthValid -Path $Storage) {
    Write-Ok "认证信息已就绪: $Storage"
} elseif ($SkipLogin) {
    Write-Warn "未发现有效认证信息但传入了 -SkipLogin，UI 启动后会显示红色横幅。"
} else {
    if (Test-Path $Storage) {
        Write-Warn "$Storage 存在但无效（空文件/损坏/无 cookie），重新登录..."
    } else {
        Write-Warn "未发现认证信息（$Storage），开始登录..."
    }
    Invoke-Login
}

# 启动 UI
if ($NoLaunch) {
    Write-Step "已跳过启动。后续手动运行: . .\.venv\Scripts\Activate.ps1; notebooklm ui"
    exit 0
}

Write-Step "启动 NotebookLM UI ..."
if ($Port -gt 0) {
    notebooklm ui --port $Port
} else {
    notebooklm ui
}
