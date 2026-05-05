# Web UI（中文）

> 英文版：[web-ui.md](web-ui.md)

`[ui]` 可选依赖会安装一个本地 Web 应用，以三栏布局（来源 / 对话 / 工坊）镜像 NotebookLM 官方界面，并补足官方界面缺失的两项关键能力：

- **问答自动归档**：每一次对话都会按笔记本独立保存到本地，可一键导出为 Markdown。
- **批量下载**：勾选任意来源、任意工坊产物（音频、视频、幻灯片、信息图、报告、思维导图、数据表、测验、闪卡）、笔记，浏览器中实时显示每一项的下载进度。
- **来源去重**：以 `(标题, 类型, URL)` 为键查找重复来源，一次确认即可清理（与 `notebook_batch.py dedup` 行为一致）。

## 安装

```bash
# 推荐：使用 uv 管理虚拟环境（最快，且自动处理 PEP 668）
curl -LsSf https://astral.sh/uv/install.sh | sh   # 仅首次需要
uv venv .venv
source .venv/bin/activate
uv pip install -e ".[ui,browser]"
playwright install chromium
```

`[ui]` 包含 `fastapi`、`uvicorn`、`sse-starlette`、`jinja2`、`python-multipart`；`[browser]` 引入 Playwright，仅 `notebooklm login` 需要。前端静态资源（CSS、JS）已随 wheel 一起打包，**无需 Node 工具链**，离线环境也能正常渲染。

> 项目根目录提供了一键脚本：
>
> ```bash
> ./scripts/install_and_run.sh        # Linux / macOS
> ./scripts/install_and_run.ps1       # Windows PowerShell
> ```
>
> 脚本会自动检测/安装 uv、创建 venv、安装依赖、首次启动 Playwright 登录，然后打开 UI。

## 启动

```bash
notebooklm login    # 仅首次需要
notebooklm ui
```

输出：

```
Serving NotebookLM UI at http://127.0.0.1:8765
```

浏览器会自动打开。常用参数：

| 参数 | 说明 |
| --- | --- |
| `--port 9000` | 指定端口（默认在 `8765-8775` 中探测可用端口） |
| `--host 127.0.0.1` | 仅允许回环地址（默认值，非回环地址会被拒绝） |
| `--no-browser` | 不自动打开浏览器（适合 SSH/无图形界面环境） |

服务器仅绑定到 `127.0.0.1`，HTTP 中间件会拒绝任何非回环来源的连接。

## 三栏布局

| 面板 | 功能 |
| --- | --- |
| **来源**（左） | 列表/搜索/多选；新增（URL / 文本 / YouTube / 文件）；重命名；删除；去重。 |
| **对话**（中） | 提问；每一条问答都自动保存到 `~/.notebooklm/conversations/<notebook_id>.jsonl`；侧抽屉浏览历史对话；当前对话一键导出 Markdown。 |
| **工坊**（右） | 已生成的工坊产物按类型分组展示；可触发新建生成或下载已有产物。 |

宽度小于 1024px 时面板会自动堆叠并显示顶部 Tab 栏；平板能用，但暂未优化手机端。

## 批量下载

点击页眉的 **下载…** 按钮，弹出对话框：

- **目标目录**：相对或绝对路径，缺失会自动创建。
- **类别勾选**：sources、audio、video、slide-deck、infographic、report、mind-map、data-table、quiz、flashcards、notes，可任意组合。
- **强制重新下载**：默认会跳过已存在的文件（与 `notebook_batch.py` 一致），勾选后强制覆盖。

点 **开始下载** 后立刻创建一个异步任务并打开任务抽屉。每个条目状态：`queued → running → done / skipped / error`。**单条失败不会中止整批**。点击 **Cancel** 取消队列中尚未开始的条目，运行中的条目自然完成。

来源类别下载策略（与 `notebook_batch.py` 对齐）：

- **PDF / DOCX / CSV** 且有 URL：直接下载文件。
- **网页**：若安装了 `wkhtmltopdf` 则转为 PDF，否则写入 `.todo` 占位说明。
- **Markdown / 粘贴文本**：导出 NotebookLM 索引的全文为 `.md`。
- **Drive / YouTube / 不支持的类型**：写入 `.todo` 占位说明。

笔记会写入 `<已清洗标题>.md`。

## 问答历史

每条问答都按以下结构追加写入 `~/.notebooklm/conversations/<notebook_id>.jsonl`：

```json
{
  "ts": "2026-05-02T12:34:56+00:00",
  "conversation_id": "uuid",
  "turn_id": "uuid",
  "question": "X 是什么？",
  "answer": "X 是 …",
  "citations": [{"source_id": "…", "cited_text": "…"}]
}
```

- **打开历史对话**：对话面板右上角的 **Conversations…**。
- **导出当前对话**：点击 **⇩ Markdown** 按钮，浏览器会下载一个带 YAML 元数据头、按问答分段的 `.md` 文件。
- **导出整个笔记本的所有对话**：

  ```
  GET /api/chat/conversations/export-all?notebook_id=<id>
  ```

文件名格式：`<已清洗的笔记本标题>-<YYYY-MM-DD>.md`，**保留中文字符**。

## 认证

UI 直接复用 `notebooklm login` 写入的认证信息。如果 cookie 缺失或过期：

- 页面顶部会出现红色横幅。
- 点击 **Refresh auth**，UI 会重新读取 `storage_state.json` 并刷新 token。
- 仍然失败时，到终端再跑一次 `notebooklm login`，回到 UI 点 **Refresh auth**。

UI **不会**内嵌 OAuth 流程——这是项目一贯的策略，由 Playwright 驱动的 `notebooklm login` 负责所有登录交互。

## 故障排查

**浏览器没自动打开**（headless / WSL）：URL 始终会打印到终端，手动复制即可；`--no-browser` 可以禁用自动打开。

**端口被占用**：默认在 `8765-8775` 之间探测，必要时用 `--port` 显式指定。

**横幅消不掉**：再次运行 `notebooklm login`，UI 会在每次刷新时重新读取认证状态。

**`wkhtmltopdf not found`**：网页类型的来源会回退为写 `.todo` 占位文件。安装 `apt install wkhtmltopdf` 或 `brew install wkhtmltopdf` 后，勾选 **强制重新下载** 重跑批次即可。

**升级前端依赖**：版本信息记录在 `src/notebooklm/web/static/VERSIONS.txt`；替换静态资源时记得同步更新。

## 已知限制

- **单用户、单主机**：服务端拒绝非回环连接。
- **批量任务存于内存**：服务器重启会取消进行中的任务。配合 "跳过已存在" 语义，重试仅需点击一次。
- **聊天暂未流式输出**：当前底层客户端一次性返回完整答案，UI 中的 "正在输入" 提示仅是装饰，待客户端支持流式 API 后启用。
