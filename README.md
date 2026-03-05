# notebooklm-py
<p align="left">
  <img src="https://raw.githubusercontent.com/teng-lin/notebooklm-py/main/notebooklm-py.png" alt="notebooklm-py logo" width="128">
</p>

**Comprehensive Python API for Google NotebookLM.** Full programmatic access to NotebookLM's features—including capabilities the web UI doesn't expose—from Python or the command line.

[![PyPI version](https://img.shields.io/pypi/v/notebooklm-py.svg)](https://pypi.org/project/notebooklm-py/)
[![Python Version](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13%20%7C%203.14-blue)](https://pypi.org/project/notebooklm-py/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://github.com/teng-lin/notebooklm-py/actions/workflows/test.yml/badge.svg)](https://github.com/teng-lin/notebooklm-py/actions/workflows/test.yml)

**Source & Development**: <https://github.com/teng-lin/notebooklm-py>

> **⚠️ Unofficial Library - Use at Your Own Risk**
>
> This library uses **undocumented Google APIs** that can change without notice.
>
> - **Not affiliated with Google** - This is a community project
> - **APIs may break** - Google can change internal endpoints anytime
> - **Rate limits apply** - Heavy usage may be throttled
>
> Best for prototypes, research, and personal projects. See [Troubleshooting](docs/troubleshooting.md) for debugging tips.

## What You Can Build

🤖 **AI Agent Tools** - Integrate NotebookLM into Claude Code or other LLM agents. Ships with [Claude Code skills](#agent-skills-claude-code) for natural language automation (`notebooklm skill install`), or build your own integrations with the async Python API.

📚 **Research Automation** - Bulk-import sources (URLs, PDFs, YouTube, Google Drive), run web/Drive research queries with auto-import, and extract insights programmatically. Build repeatable research pipelines.

🎙️ **Content Generation** - Generate Audio Overviews (podcasts), videos, slide decks, quizzes, flashcards, infographics, data tables, mind maps, and study guides. Full control over formats, styles, and output.

📥 **Downloads & Export** - Download all generated artifacts locally (MP3, MP4, PDF, PNG, CSV, JSON, Markdown). Export to Google Docs/Sheets. **Features the web UI doesn't offer**: batch downloads, quiz/flashcard export in multiple formats, mind map JSON extraction.

## Three Ways to Use

| Method | Best For |
|--------|----------|
| **Python API** | Application integration, async workflows, custom pipelines |
| **CLI** | Shell scripts, quick tasks, CI/CD automation |
| **Agent Skills** | Claude Code, LLM agents, natural language automation |

## Features

### Complete NotebookLM Coverage

| Category | Capabilities |
|----------|--------------|
| **Notebooks** | Create, list, rename, delete |
| **Sources** | URLs, YouTube, files (PDF, text, Markdown, Word, audio, video, images), Google Drive, pasted text; refresh, get guide/fulltext |
| **Chat** | Questions, conversation history, custom personas |
| **Research** | Web and Drive research agents (fast/deep modes) with auto-import |
| **Sharing** | Public/private links, user permissions (viewer/editor), view level control |

### Content Generation (All NotebookLM Studio Types)

| Type | Options | Download Format |
|------|---------|-----------------|
| **Audio Overview** | 4 formats (deep-dive, brief, critique, debate), 3 lengths, 50+ languages | MP3/MP4 |
| **Video Overview** | 2 formats, 9 visual styles (classic, whiteboard, kawaii, anime, etc.) | MP4 |
| **Slide Deck** | Detailed or presenter format, adjustable length; individual slide revision | PDF, PPTX |
| **Infographic** | 3 orientations, 3 detail levels | PNG |
| **Quiz** | Configurable quantity and difficulty | JSON, Markdown, HTML |
| **Flashcards** | Configurable quantity and difficulty | JSON, Markdown, HTML |
| **Report** | Briefing doc, study guide, blog post, or custom prompt | Markdown |
| **Data Table** | Custom structure via natural language | CSV |
| **Mind Map** | Interactive hierarchical visualization | JSON |

### Beyond the Web UI

These features are available via API/CLI but not exposed in NotebookLM's web interface:

- **Batch downloads** - Download all artifacts of a type at once
- **Quiz/Flashcard export** - Get structured JSON, Markdown, or HTML (web UI only shows interactive view)
- **Mind map data extraction** - Export hierarchical JSON for visualization tools
- **Data table CSV export** - Download structured tables as spreadsheets
- **Slide deck as PPTX** - Download editable PowerPoint files (web UI only offers PDF)
- **Slide revision** - Modify individual slides with natural-language prompts
- **Report template customization** - Append extra instructions to built-in format templates
- **Save chat to notes** - Save Q&A answers or conversation history as notebook notes
- **Source fulltext access** - Retrieve the indexed text content of any source
- **Programmatic sharing** - Manage permissions without the UI

## Installation

```bash
# Basic installation
pip install notebooklm-py

# With browser login support (required for first-time setup)
pip install "notebooklm-py[browser]"
playwright install chromium
```

### Development Installation

For contributors or testing unreleased features:

```bash
pip install git+https://github.com/teng-lin/notebooklm-py@main
```

⚠️ The main branch may contain unstable changes. Use PyPI releases for production.

## Quick Start

<p align="center">
  <a href="https://asciinema.org/a/767284" target="_blank"><img src="https://asciinema.org/a/767284.svg" width="600" /></a>
  <br>
  <em>16-minute session compressed to 30 seconds</em>
</p>

### CLI

```bash
# 1. Authenticate (opens browser)
notebooklm login

# 2. Create a notebook and add sources
notebooklm create "My Research"
notebooklm use <notebook_id>
notebooklm source add "https://en.wikipedia.org/wiki/Artificial_intelligence"
notebooklm source add "./paper.pdf"

# 3. Chat with your sources
notebooklm ask "What are the key themes?"

# 4. Generate content
notebooklm generate audio "make it engaging" --wait
notebooklm generate video --style whiteboard --wait
notebooklm generate quiz --difficulty hard
notebooklm generate flashcards --quantity more
notebooklm generate slide-deck
notebooklm generate infographic --orientation portrait
notebooklm generate mind-map
notebooklm generate data-table "compare key concepts"

# 5. Download artifacts
notebooklm download audio ./podcast.mp3
notebooklm download video ./overview.mp4
notebooklm download quiz --format markdown ./quiz.md
notebooklm download flashcards --format json ./cards.json
notebooklm download slide-deck ./slides.pdf
notebooklm download mind-map ./mindmap.json
notebooklm download data-table ./data.csv
```

### Python API

```python
import asyncio
from notebooklm import NotebookLMClient

async def main():
    async with await NotebookLMClient.from_storage() as client:
        # Create notebook and add sources
        nb = await client.notebooks.create("Research")
        await client.sources.add_url(nb.id, "https://example.com", wait=True)

        # Chat with your sources
        result = await client.chat.ask(nb.id, "Summarize this")
        print(result.answer)

        # Generate content (podcast, video, quiz, etc.)
        status = await client.artifacts.generate_audio(nb.id, instructions="make it fun")
        await client.artifacts.wait_for_completion(nb.id, status.task_id)
        await client.artifacts.download_audio(nb.id, "podcast.mp3")

        # Generate quiz and download as JSON
        status = await client.artifacts.generate_quiz(nb.id)
        await client.artifacts.wait_for_completion(nb.id, status.task_id)
        await client.artifacts.download_quiz(nb.id, "quiz.json", output_format="json")

        # Generate mind map and export
        result = await client.artifacts.generate_mind_map(nb.id)
        await client.artifacts.download_mind_map(nb.id, "mindmap.json")

asyncio.run(main())
```

### Agent Skills (Claude Code)

```bash
# Install via CLI or ask Claude Code to do it
notebooklm skill install

# Then use natural language:
# "Create a podcast about quantum computing"
# "Download the quiz as markdown"
# "/notebooklm generate video"
```

## Documentation

- **[CLI Reference](docs/cli-reference.md)** - Complete command documentation
- **[Python API](docs/python-api.md)** - Full API reference
- **[Configuration](docs/configuration.md)** - Storage and settings
- **[Troubleshooting](docs/troubleshooting.md)** - Common issues and solutions
- **[API Stability](docs/stability.md)** - Versioning policy and stability guarantees

### For Contributors

- **[Development Guide](docs/development.md)** - Architecture, testing, and releasing
- **[RPC Development](docs/rpc-development.md)** - Protocol capture and debugging
- **[RPC Reference](docs/rpc-reference.md)** - Payload structures
- **[Changelog](CHANGELOG.md)** - Version history and release notes
- **[Security](SECURITY.md)** - Security policy and credential handling

## Platform Support

| Platform | Status | Notes |
|----------|--------|-------|
| **macOS** | ✅ Tested | Primary development platform |
| **Linux** | ✅ Tested | Fully supported |
| **Windows** | ✅ Tested | Tested in CI |

## License

MIT License. See [LICENSE](LICENSE) for details.

## TODO


## 增加需求
### 1. 增加一个python脚本，调用README.md中关于CLI的说明，利用notebooklm命令完成如下功能，假设已经登陆，不用处理登陆了：
首先列出笔记本notebooklm list，用户选择当前笔记本notebooklm use命令
`notebooklm list --json` 返回json，参考notebook-list.json，注意，所有json的中文内容已经转码不便阅读，需要转回来，ensure_ascii=False
`notebooklm use fbe2dd1b-02d1-4846-b4ed-c654f93de1cd`

1. source去重，通过source list，遍历id，使用get获取详情， 如果source Tilte，Type， URL相同（URL可能没有），则只保留最后一个，删除使用Id，例如`notebooklm source delete 5cb188dc-9969-4e8a-9269-3be21f35c78d`，每个删除需要用户确认
  list命令使用如下：
    ```notebooklm source list --json``` 结果参考：source-list.json
  get命令使用如下：`notebooklm source get 8cdd6ee1-e357-465b-9b58-245c21fd8bde --json`
  get命令返回文本：      
        Source: 8cdd6ee1-e357-465b-9b58-245c21fd8bde
        Title: 传媒行业2026 年度策略报告： Agent 定义入口，AIGC 重塑供给——AI 时代的流量分发重构与内容产
        Type: 📄 PDF
        URL: https://pdf.dfcfw.com/pdf/H3_AP202601091816878674_1.pdf?1767974238000.pdf
        Created: 2026-03-02 23:38

2. source列表
输出：Title，URL列表

3. source下载
遍历source，下载到"{Notebook Title}/"目录中
对不同类型，使用不同的方式下载
   3.1 文档类型type为"SourceType.PDF"，"SourceType.DOCX"，"SourceType.PPTX"等，且包含URL，直接下载URL对应目标文件
   3.2 "type": "SourceType.WEB_PAGE",
      "url": "https://t.cj.sina.com.cn/articles/view/2405591841/8f626b2100102yjmw",
       这种使用curl下载整个页面和资源到目录中
   3.3  "type": "SourceType.MARKDOWN"，且url为null，则用fulltext命令获取内容写入文件
   3.4 其他类型，没有url，不下载，生成一个空文件加todo

4. 一键下载所有的source，artifact

### 转换web为pdf
sudo apt-get update
sudo apt-get install wkhtmltopdf
wkhtmltopdf https://www.gm7.org/archives/38502 output.pdf


### 修改notebook_batch.py，查看调用README.md中关于CLI的说明，此脚本利用notebooklm命令完成一些功能
1. source web的html形式下载改为使用wkhtmltopdf下载，软件已存在，如果没有，安装命令
sudo apt-get update
sudo apt-get install 
wkhtmltopdf命令示例如下：wkhtmltopdf https://www.gm7.org/archives/38502 output.pdf
2. source list输出成markdown 表格方式
3. 如果下载时目录中文件已经存在，则不再下载

### 支持note下载
/opsx/propose @notebook_batch.py增加支持note下载为markdown文件， 全部下载增加支持note下载，对source， artifacts，note下载到不同子目录中，note下载参考notebooklm note get d60a1c1a-66fe-4f22-b6fb-28af201217a3
