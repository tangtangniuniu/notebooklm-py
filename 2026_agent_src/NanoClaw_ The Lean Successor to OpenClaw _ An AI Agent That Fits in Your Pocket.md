> Source: https://till-freitag.com/en/blog/nanoclaw-openclaw-successor-en

NanoClaw: The Lean Successor to OpenClaw –… – Till Freitag















Till Freitag – monday.com Partner & Work Management Experten





[![Till Freitag](/assets/logo-DdxT28Z-.png)](/en)

[Services](/en/services)

[Tools](/en/tools)

[Solutions](/en/solutions)

[Till who?](/en/team)

[References](/en/referenzen)

[Contact](/en/beratung)

en[Book a Call](/en/beratung)

en

![NanoClaw: The Lean Successor to OpenClaw – An AI Agent That Fits in Your Pocket](/assets/openclaw-ki-agent-bWPXj8VW.webp)

[Blog](/en/blog)NanoClaw: The Lean Successor to OpenClaw – An AI Agent That Fits in Your Pocket

[AI](/en/blog?kategorie=AI)[Tools](/en/blog?kategorie=Tools)

# NanoClaw: The Lean Successor to OpenClaw – An AI Agent That Fits in Your Pocket

![Till Freitag](/assets/till-freitag-BjNvOFUr.svg)

[Till Freitag](/en/blog/autor/till-freitag)

21. Februar 20264 min read

![Till Freitag](/assets/till-freitag-BjNvOFUr.svg)

TL;DR: „NanoClaw distills OpenClaw's vision into a one-liner: One process, 5 files, container-isolated, WhatsApp-controllable – and it runs on a Raspberry Pi. The AI agent for minimalists."

— Till Freitag

## From OpenClaw to NanoClaw: Less Is More

We introduced [OpenClaw](/tools/openclaw) as the open-source AI agent that doesn't just talk – it acts. Now there's a spiritual successor that takes the philosophy to its extreme: **NanoClaw**.

Where OpenClaw relies on a modular microservice architecture, NanoClaw takes the radically different path: **One process. Five files. Zero complexity.**

## What Is NanoClaw?

NanoClaw is a personal Claude assistant built on simplicity and security. The core idea: an AI agent so lightweight it runs on a Raspberry Pi – yet still does everything you'd expect from an autonomous agent.

| Metric | Value |
| --- | --- |
| **GitHub Stars** | 6,700+ |
| **Core Files** | 5 |
| **Processes** | 1 |
| **License** | MIT |
| **Version** | v0.4.2 (Production Ready) |

## Feature Overview

### 🔒 Container Isolation

Agents run in Linux containers with filesystem isolation. Only mounted directories are accessible – Bash commands execute safely inside the container, never on your host system.

### 💬 WhatsApp Interface

Yes, you read that right. NanoClaw can be controlled via WhatsApp. Each WhatsApp group gets an isolated context with its own `CLAUDE.md` memory files for personalized interactions.

### 🧠 Per-Group Memory

Isolated contexts per WhatsApp group with dedicated memory files. SQLite-based message storage with per-group queuing and concurrency control.

### ⏰ Scheduled Tasks

Recurring jobs with a built-in task scheduler. Automate daily reports, reminders, and background operations – no external dependencies needed.

### 🤖 Claude Agent SDK

Streaming agent container, powered by the Claude Agent SDK. Direct access to Claude's capabilities with built-in web search and content fetching.

### 🐝 Agent Swarms

Collaborative multi-agent workflows for complex tasks. Coordinate multiple Claude instances to solve demanding problems efficiently.

## NanoClaw vs. Cloud AI: The Comparison

| Feature | Cloud AI (OpenAI/Claude) | NanoClaw (Local) |
| --- | --- | --- |
| **Privacy** | Stored on servers | 100% local |
| **Cost** | From $20+/month | Free after setup |
| **Integrations** | Limited API | 100+ (Zapier-like) |
| **Device Support** | Web only | Mac / RPi / Docker |
| **Customization** | Prompt-based only | Fully open source |
| **Internet required?** | Always online | Fully offline-capable |

## NanoClaw vs. OpenClaw: What's the Difference?

| Aspect | OpenClaw | NanoClaw |
| --- | --- | --- |
| **Architecture** | Microservices | Single Process |
| **Complexity** | Modular stack | 5 Core Files |
| **LLM Support** | Multi-LLM (OpenAI, Claude, Llama) | Claude-focused (Agent SDK) |
| **Edge Support** | Server-optimized | Raspberry Pi, Mac mini |
| **Messaging** | API / Terminal | Native WhatsApp |
| **Setup** | Docker Compose + config | `git clone && claude` |
| **Community** | Growing | 6,700+ GitHub Stars |

**In short**: OpenClaw is the powerful all-rounder. NanoClaw is the minimalist that runs on a Pi under your desk.

## Installation in 3 Steps

```
# 1. Clone the repository
git clone https://github.com/gavrielc/nanoclaw.git

# 2. Navigate to the directory
cd nanoclaw

# 3. Start Claude Code and run setup
claude
# In Claude Code: /setup
```

Claude Code automatically handles dependencies, authentication, container setup, and service configuration.

### Prerequisites

* macOS or Linux (Windows via WSL2)
* Node.js 20+
* Claude Code CLI
* Apple Container (macOS) or Docker

### Hardware Requirements

* **Raspberry Pi 4** (4GB+ RAM)
* **Mac mini** with Apple Silicon (M1/M2/M3)
* **Any modern PC** with 16GB+ RAM
* NVIDIA RTX 3060+ GPU recommended, CPU-only works too

## Use Cases

| Use Case | Description |
| --- | --- |
| **Code Assistant** | Local code completion, debugging, and documentation – your code stays private |
| **Content Creation** | Write blog posts, emails, and documents with AI assistance |
| **Data Analysis** | Analyze sensitive business data locally – nothing leaves your infrastructure |
| **Personal Assistant** | Manage calendar, emails, and tasks via voice commands |
| **Research & Learning** | Summarize papers, organize knowledge bases |
| **API Integration** | Build custom applications via NanoClaw's REST API |

## Our Take

NanoClaw strikes a nerve. Not everyone needs an enterprise AI platform. Many people simply need a smart agent running on their own device, reachable via WhatsApp, that doesn't send their data to cloud servers.

The combination of **container isolation**, **WhatsApp interface**, and **Raspberry Pi support** is unique. The fact that it all works with 5 files and a single process is impressive.

**Who is NanoClaw for?**

* Developers who want a local Claude agent
* Privacy-conscious teams that can't use cloud AI
* Makers and tinkerers who want to bring AI to edge devices
* Anyone who found OpenClaw exciting but shied away from the setup effort

**Not ideal for**: Teams that need multi-LLM support or enterprise integrations with monday.com or Make – for that, [OpenClaw](/tools/openclaw) remains the better choice.

> NanoClaw is open source under the MIT license. You only pay for the Anthropic API (Claude calls) – no subscription, no hidden costs. **Heads up:** Anthropic recently [killed third-party tool coverage under Claude subscriptions](/en/blog/openclaw-pricing-shock-en) – check your API costs!

[→ View NanoClaw on GitHub](https://github.com/)

---

*More on AI agents: [What is OpenClaw?](/blog/was-ist-openclaw) · [Our Tool Philosophy](/tools)*

Inhalt

* [From OpenClaw to NanoClaw: Less Is More](#from-openclaw-to-nanoclaw-less-is-more)
* [What Is NanoClaw?](#what-is-nanoclaw)
* [Feature Overview](#feature-overview)
* [🔒 Container Isolation](#container-isolation)
* [💬 WhatsApp Interface](#whatsapp-interface)
* [🧠 Per-Group Memory](#per-group-memory)
* [⏰ Scheduled Tasks](#scheduled-tasks)
* [🤖 Claude Agent SDK](#claude-agent-sdk)
* [🐝 Agent Swarms](#agent-swarms)
* [NanoClaw vs. Cloud AI: The Comparison](#nanoclaw-vs-cloud-ai-the-comparison)
* [NanoClaw vs. OpenClaw: What's the Difference?](#nanoclaw-vs-openclaw-what-s-the-difference)
* [Installation in 3 Steps](#installation-in-3-steps)
* [Prerequisites](#prerequisites)
* [Hardware Requirements](#hardware-requirements)
* [Use Cases](#use-cases)
* [Our Take](#our-take)

Inhalt

* [From OpenClaw to NanoClaw: Less Is More](#from-openclaw-to-nanoclaw-less-is-more)
* [What Is NanoClaw?](#what-is-nanoclaw)
* [Feature Overview](#feature-overview)
* [🔒 Container Isolation](#container-isolation)
* [💬 WhatsApp Interface](#whatsapp-interface)
* [🧠 Per-Group Memory](#per-group-memory)
* [⏰ Scheduled Tasks](#scheduled-tasks)
* [🤖 Claude Agent SDK](#claude-agent-sdk)
* [🐝 Agent Swarms](#agent-swarms)
* [NanoClaw vs. Cloud AI: The Comparison](#nanoclaw-vs-cloud-ai-the-comparison)
* [NanoClaw vs. OpenClaw: What's the Difference?](#nanoclaw-vs-openclaw-what-s-the-difference)
* [Installation in 3 Steps](#installation-in-3-steps)
* [Prerequisites](#prerequisites)
* [Hardware Requirements](#hardware-requirements)
* [Use Cases](#use-cases)
* [Our Take](#our-take)

Teilen[LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=http%3A%2F%2Flocalhost%3A4173%2Fblog%2Fnanoclaw-openclaw-successor-en)[WhatsApp](https://wa.me/?text=NanoClaw%3A%20The%20Lean%20Successor%20to%20OpenClaw%20%E2%80%93%20An%20AI%20Agent%20That%20Fits%20in%20Your%20Pocket%20http%3A%2F%2Flocalhost%3A4173%2Fblog%2Fnanoclaw-openclaw-successor-en)[E-Mail](mailto:?subject=NanoClaw%3A%20The%20Lean%20Successor%20to%20OpenClaw%20%E2%80%93%20An%20AI%20Agent%20That%20Fits%20in%20Your%20Pocket&body=http%3A%2F%2Flocalhost%3A4173%2Fblog%2Fnanoclaw-openclaw-successor-en)Link kopieren

## Related Articles

[![The Best OpenClaw Alternatives 2026 – from NanoClaw to NullClaw](/assets/openclaw-alternativen-2026-0NrmZwrh.webp)Deep Dive

February 21, 202610 min

### The Best OpenClaw Alternatives 2026 – from NanoClaw to NullClaw

OpenClaw has 160,000+ GitHub stars – but not everyone needs 430,000 lines of code. We compare the best alternatives in 2…

Read more](/en/blog/openclaw-alternatives-en)[![OpenClaw AI agent interface with autonomous task management and LLM integration](/assets/openclaw-ki-agent-B2sS_05_.webp)

February 20, 20265 min

### What Is OpenClaw? The Open-Source AI Agent Overview

OpenClaw is an open-source AI agent that handles tasks autonomously – from emails to calendars. Self-hosted, GDPR-compli…

Read more](/en/blog/what-is-openclaw-en)[![OpenClaw Pricing Shock: How to Avoid the $500 Bill](/assets/openclaw-pricing-shock-BzgpELdq.webp)

April 5, 20262 min

### OpenClaw Pricing Shock: How to Avoid the $500 Bill

Anthropic just killed third-party tool coverage under Claude subscriptions. If you're running OpenClaw without prep, you…

Read more](/en/blog/openclaw-pricing-shock-en)[April 28, 20266 min

### Paperclip: If OpenClaw Is the Employee, Paperclip Is the Company

Paperclip is open-source infrastructure to run an entire AI-only company – org chart, budgets, approvals, audit trail. W…

Read more](/en/blog/paperclip-control-plane-for-ai-companies-en)[![monday.com board connected to OpenClaw AI agent as central memory and control system](/assets/monday-openclaw-integration-BL4wGHuu.webp)

March 12, 20266 min

### monday.com + OpenClaw: How monday.com Becomes the Brain of Your AI Agent

monday.com is more than a project management tool – it can serve as the long-term memory and execution log for an AI age…

Read more](/en/blog/monday-openclaw-integration-en)[![OpenClaw Self-Hosting Guide: GDPR-Compliant in 30 Minutes](/assets/openclaw-ki-agent-B2sS_05_.webp)

February 28, 20264 min

### OpenClaw Self-Hosting Guide: GDPR-Compliant in 30 Minutes

Self-host OpenClaw with Docker, persistent storage, and local LLMs via Ollama – fully GDPR-compliant because no data eve…

Read more](/en/blog/openclaw-self-hosting-gdpr-en)[![Gemma 4 AI model running on a compact mini PC – frontier intelligence goes local](/assets/gemma-4-local-ai-B-BC1ND0.webp)

April 6, 20264 min

### Gemma 4: Frontier Intelligence Goes Laptop-Sized – The Hype Is Real

Google's Gemma 4 delivers GPT-4 level intelligence in 14 GB. 85 tokens per second on consumer hardware, 256K context, na…

Read more](/en/blog/gemma-4-local-ai-en)[![Three architectures compared – structured grid, open mesh, and neural network as symbols for Copilot, OpenClaw, and Claude](/assets/copilot-vs-openclaw-vs-claude-urfZ5RvY.webp)Deep Dive

April 4, 20268 min

### Copilot vs. OpenClaw vs. Claude: Enterprise AI Agents Compared 2026

Three philosophies, one goal: AI agents in the enterprise. Microsoft Copilot (platform), OpenClaw (open source), Claude …

Read more](/en/blog/copilot-vs-openclaw-vs-claude-en)[![Smartphone sending a task to a desktop computer where an AI agent works autonomously](/assets/claude-dispatch-feature-BIV_8WFi.webp)

March 22, 20264 min

### Claude Dispatch: Your AI Agent Works While You're Away

Anthropic launched Dispatch – turning Claude from a chatbot into a digital coworker. Send a task from your phone, Claude…

Read more](/en/blog/claude-dispatch-ai-agent-feature-en)

Ready for the next step?

## Let's build your frictionless future together.

1

Intro CallGetting to know & Goals

2

Workflow AuditAnalysis & Concept

3

Go LiveHands-on Implementation

[Schedule a call](/en/beratung)

Technology Partners

[![Lovable](/assets/lovable-icon-jZJZP_r2.png)](/en/tools/lovable)[![monday.com](data:image/svg+xml,%3c?xml%20version='1.0'%20encoding='UTF-8'?%3e%3c!--%20Uploaded%20to:%20SVG%20Repo,%20www.svgrepo.com,%20Generator:%20SVG%20Repo%20Mixer%20Tools%20--%3e%3csvg%20width='800px'%20height='800px'%20viewBox='0%20-50%20256%20256'%20version='1.1'%20xmlns='http://www.w3.org/2000/svg'%20xmlns:xlink='http://www.w3.org/1999/xlink'%20preserveAspectRatio='xMidYMid'%3e%3cg%3e%3cpath%20d='M31.8458633,153.488694%20C20.3244423,153.513586%209.68073708,147.337265%203.98575204,137.321731%20C-1.62714067,127.367831%20-1.29055839,115.129325%204.86093879,105.498969%20L62.2342919,15.4033556%20C68.2125882,5.54538256%2079.032489,-0.333585033%2090.5563073,0.0146553508%20C102.071737,0.290611552%20112.546041,6.74705604%20117.96667,16.9106216%20C123.315033,27.0238906%20122.646488,39.1914174%20116.240607,48.6847625%20L58.9037201,138.780375%20C52.9943022,147.988884%2042.7873202,153.537154%2031.8458633,153.488694%20L31.8458633,153.488694%20Z'%20fill='%23F62B54'%3e%3c/path%3e%3cpath%20d='M130.25575,153.488484%20C118.683837,153.488484%20108.035731,147.301291%20102.444261,137.358197%20C96.8438154,127.431292%2097.1804475,115.223704%20103.319447,105.620522%20L160.583402,15.7315506%20C166.47539,5.73210989%20177.327374,-0.284878136%20188.929728,0.0146553508%20C200.598885,0.269918151%20211.174058,6.7973526%20216.522421,17.0078646%20C221.834319,27.2183766%20221.056375,39.4588356%20214.456008,48.9278699%20L157.204209,138.816842%20C151.313487,147.985468%20141.153618,153.5168%20130.25575,153.488484%20Z'%20fill='%23FFCC00'%3e%3c/path%3e%3cellipse%20fill='%2300CA72'%20cx='226.465527'%20cy='125.324379'%20rx='29.5375538'%20ry='28.9176274'%3e%3c/ellipse%3e%3c/g%3e%3c/svg%3e)](/en/tools/monday-com)[![Airtable](data:image/svg+xml,%3c?xml%20version='1.0'%20encoding='utf-8'?%3e%3c!--%20Uploaded%20to:%20SVG%20Repo,%20www.svgrepo.com,%20Generator:%20SVG%20Repo%20Mixer%20Tools%20--%3e%3csvg%20fill='%23000000'%20width='800px'%20height='800px'%20viewBox='0%200%2032%2032'%20version='1.1'%20xmlns='http://www.w3.org/2000/svg'%3e%3ctitle%3eairtable%3c/title%3e%3cpath%20d='M1.849%2011.12c-0.008-0-0.018-0.001-0.029-0.001-0.223%200-0.425%200.091-0.571%200.238l-0%200c-0.141%200.126-0.234%200.304-0.245%200.504l-0%200.002v10.441c0.024%200.42%200.371%200.751%200.794%200.751%200.124%200%200.241-0.028%200.345-0.079l-0.005%200.002%208.219-3.94%203.71-1.794c0.246-0.125%200.411-0.376%200.411-0.666%200-0.319-0.2-0.591-0.482-0.697l-0.005-0.002-11.884-4.706c-0.076-0.033-0.165-0.053-0.258-0.055l-0.001-0zM30.246%2011.071c-0.1%200.001-0.195%200.021-0.282%200.058l0.005-0.002-12.511%204.845c-0.28%200.117-0.474%200.388-0.475%200.705v11.117c0.004%200.411%200.338%200.743%200.75%200.743%200.099%200%200.194-0.019%200.281-0.055l-0.005%200.002%2012.513-4.861c0.28-0.106%200.475-0.372%200.475-0.683%200-0.002%200-0.004-0-0.006v0-11.117c-0.003-0.412-0.337-0.745-0.75-0.745%200%200%200%200-0%200v0zM15.99%203.461c-0.577%200-1.127%200.118-1.627%200.331l0.027-0.010-11.163%204.616c-0.274%200.116-0.463%200.383-0.463%200.694%200%200.317%200.196%200.588%200.473%200.699l0.005%200.002%2011.224%204.446c0.454%200.189%200.981%200.299%201.533%200.299s1.080-0.11%201.56-0.309l-0.027%200.010%2011.224-4.446c0.28-0.115%200.473-0.385%200.473-0.7%200-0.31-0.187-0.576-0.453-0.692l-0.005-0.002-11.193-4.616c-0.468-0.203-1.012-0.321-1.584-0.321-0.002%200-0.004%200-0.006%200h0z'%3e%3c/path%3e%3c/svg%3e)](/en/tools/airtable)[![Claude](data:image/svg+xml,%3c?xml%20version='1.0'%20encoding='UTF-8'?%3e%3c!--%20Generated%20by%20Pixelmator%20Pro%203.6.17%20--%3e%3csvg%20width='1200'%20height='1200'%20viewBox='0%200%201200%201200'%20xmlns='http://www.w3.org/2000/svg'%3e%3cg%20id='g314'%3e%3cpath%20id='path147'%20fill='%23d97757'%20stroke='none'%20d='M%20233.959793%20800.214905%20L%20468.644287%20668.536987%20L%20472.590637%20657.100647%20L%20468.644287%20650.738403%20L%20457.208069%20650.738403%20L%20417.986633%20648.322144%20L%20283.892639%20644.69812%20L%20167.597321%20639.865845%20L%2054.926208%20633.825623%20L%2026.577238%20627.785339%20L%203.3e-05%20592.751709%20L%202.73832%20575.27533%20L%2026.577238%20559.248352%20L%2060.724873%20562.228149%20L%20136.187973%20567.382629%20L%20249.422867%20575.194763%20L%20331.570496%20580.026978%20L%20453.261841%20592.671082%20L%20472.590637%20592.671082%20L%20475.328857%20584.859009%20L%20468.724915%20580.026978%20L%20463.570557%20575.194763%20L%20346.389313%20495.785217%20L%20219.543671%20411.865906%20L%20153.100723%20363.543762%20L%20117.181267%20339.060425%20L%2099.060455%20316.107361%20L%2091.248367%20266.01355%20L%20123.865784%20230.093994%20L%20167.677887%20233.073853%20L%20178.872513%20236.053772%20L%20223.248367%20270.201477%20L%20318.040283%20343.570496%20L%20441.825592%20434.738342%20L%20459.946411%20449.798706%20L%20467.194672%20444.64447%20L%20468.080597%20441.020203%20L%20459.946411%20427.409485%20L%20392.617493%20305.718323%20L%20320.778564%20181.932983%20L%20288.80542%20130.630859%20L%20280.348999%2099.865845%20C%20277.369171%2087.221436%20275.194641%2076.590698%20275.194641%2063.624268%20L%20312.322174%2013.20813%20L%20332.8591%206.604126%20L%20382.389313%2013.20813%20L%20403.248352%2031.328979%20L%20434.013519%20101.71814%20L%20483.865753%20212.537048%20L%20561.181274%20363.221497%20L%20583.812134%20407.919434%20L%20595.892639%20449.315491%20L%20600.40271%20461.959839%20L%20608.214783%20461.959839%20L%20608.214783%20454.711609%20L%20614.577271%20369.825623%20L%20626.335632%20265.61084%20L%20637.771851%20131.516846%20L%20641.718201%2093.745117%20L%20660.402832%2048.483276%20L%20697.530334%2024.000122%20L%20726.52356%2037.852417%20L%20750.362549%2072%20L%20747.060486%2094.067139%20L%20732.886047%20186.201416%20L%20705.100708%20330.52356%20L%20686.979919%20427.167847%20L%20697.530334%20427.167847%20L%20709.61084%20415.087341%20L%20758.496704%20350.174561%20L%20840.644348%20247.490051%20L%20876.885925%20206.738342%20L%20919.167847%20161.71814%20L%20946.308838%20140.29541%20L%20997.61084%20140.29541%20L%201035.38269%20196.429626%20L%201018.469849%20254.416199%20L%20965.637634%20321.422852%20L%20921.825562%20378.201538%20L%20859.006714%20462.765259%20L%20819.785278%20530.41626%20L%20823.409424%20535.812073%20L%20832.75177%20534.92627%20L%20974.657776%20504.724915%20L%201051.328979%20490.872559%20L%201142.818848%20475.167786%20L%201184.214844%20494.496582%20L%201188.724854%20514.147644%20L%201172.456421%20554.335693%20L%201074.604126%20578.496765%20L%20959.838989%20601.449829%20L%20788.939636%20641.879272%20L%20786.845764%20643.409485%20L%20789.261841%20646.389343%20L%20866.255127%20653.637634%20L%20899.194702%20655.409424%20L%20979.812134%20655.409424%20L%201129.932861%20666.604187%20L%201169.154419%20692.537109%20L%201192.671265%20724.268677%20L%201188.724854%20748.429688%20L%201128.322144%20779.194641%20L%201046.818848%20759.865845%20L%20856.590759%20714.604126%20L%20791.355774%20698.335754%20L%20782.335693%20698.335754%20L%20782.335693%20703.731567%20L%20836.69812%20756.885986%20L%20936.322205%20846.845581%20L%201061.073975%20962.81897%20L%201067.436279%20991.490112%20L%201051.409424%201014.120911%20L%201034.496704%201011.704712%20L%20924.885986%20929.234924%20L%20882.604126%20892.107544%20L%20786.845764%20811.48999%20L%20780.483276%20811.48999%20L%20780.483276%20819.946289%20L%20802.550415%20852.241699%20L%20919.087341%201027.409424%20L%20925.127625%201081.127686%20L%20916.671204%201098.604126%20L%20886.469849%201109.154419%20L%20853.288696%201103.114136%20L%20785.073914%201007.355835%20L%20714.684631%20899.516785%20L%20657.906067%20802.872498%20L%20650.979858%20806.81897%20L%20617.476624%201167.704834%20L%20601.771851%201186.147705%20L%20565.530212%201200%20L%20535.328857%201177.046997%20L%20519.302124%201139.919556%20L%20535.328857%201066.550537%20L%20554.657776%20970.792053%20L%20570.362488%20894.68457%20L%20584.536926%20800.134277%20L%20592.993347%20768.724976%20L%20592.429626%20766.630859%20L%20585.503479%20767.516968%20L%20514.22821%20865.369263%20L%20405.825531%201011.865906%20L%20320.053711%201103.677979%20L%20299.516815%201111.812256%20L%20263.919525%201093.369263%20L%20267.221497%201060.429688%20L%20287.114136%201031.114136%20L%20405.825531%20880.107361%20L%20477.422913%20786.52356%20L%20523.651062%20732.483276%20L%20523.328918%20724.671265%20L%20520.590698%20724.671265%20L%20205.288605%20929.395935%20L%20149.154434%20936.644409%20L%20124.993355%20914.01355%20L%20127.973183%20876.885986%20L%20139.409409%20864.80542%20L%20234.201385%20799.570435%20L%20233.879227%20799.8927%20Z'/%3e%3c/g%3e%3c/svg%3e)](/en/tools/claude)[![Make](/assets/make-icon-DGDX6Qql.png)](/en/tools/make-com)[![n8n](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAAFKUlEQVRoge2XfWhVZRzHP79ztjt15pbb7syXylYSUYKLIqxomc62u2lFg9AQ+sekNO+dWy9kcitBQXR3vhQYgSAKRfTCducbqIURKo1UkJxvEGrzng3b2q56d+/59cfO3e6u2xXDNqH7+euc5/k+z/l+z3nO7zwH0qRJkyZNmjRp/r/ISBtIhfr9Ruhw91SMqBYG684NprkjA2hVlWl1T65FeA/IdVrPqkFNYUPg+0StMQL+bkpb9+TNCGvoMw8gRWLLt1a5b0Gi9o4LYFV6i1VY0nsmm2IxnYrqDOBnQFSoP1/iHxXXZwy3QfX7DetI5yIMrUC5/4Z+m0Ln8LeC4IblAgpgzfVWaYZcAPLvGv3XTGA/DHMArfK72o52BBFm99pKyZm4eYD8PYFWy+PrAsbZJuPj7cMawAp3fALMBmwRdqith0WkJ1GjylMIbyjMCpXXTnA3rWsFaKvwVaCMAzBj5sm4ftAqdNnje8BQnYVhCCrNBcH1vw5l6spL3txIjBJs4x4VWgq7xv0oB/3RZJ2W+DOssR0XUdwoH7mb6lYPNV9Pj5wHckEvgWxXGC+wCMgCDriDdbMGDaAl/gwru6MOeIvEF1zZG8mKLJj83Zb2gUGrXwetF/ofKfC7GLqwoCHQnKhtLfc9ZgjHAUw7OiVv16YLQ90Uq8JboiqNQHZSV4tpR19IHDugCrVld64BljrtbcA5J2apK+JqUL+/Tx8q85YJus0x341wCogCD6stu9vLlk1OnNs0ZI5z+Gcq8wAFjYGDYmZOQ1gLug/YLVBj95jFyWP7nkBraY3byIxdADKBzQXdOT456I+GKryvovIVYCDymktdewEiGtmD6BOgh1yMmpcbXHulvWzFIzHTPuAsk3qXZH3cE702ys405ojqFmAsaMAdDPhSBbgV+gJYnup5iv4AXO+wozkP7dp0Pd4X8nj3Qt8dHIjaz7mb6n/q05b7ViJ8OsT1zrjIejI3uPbKbfLfv4Rsw44f2w9ezYsNlA2sFImokdQnQ2tRwtd6opF/4XNI+gIY4joCxIDRoezOVeo8nbYy7yygFEBUligUKRQBJ5y2VZcqF48BaJ9fPQXVt50pv1Qoihk8KogPuIYw3XDFVt7OAAOqkFXu+7z/M04LKh2IFgMmyvGCcM7j8RLpvBtfO3NcBj0NMoPeytGpMCNxBxnyVH8Iulrhj8Jg3X3JRixP9fOqOh9highnjZixLW/X+pPJumQGVKGucI5PkR3O6bTelxQTlaOSkVmWWN/djYFvEN4BwkAhyDOO+YuoXXnD9temyblj94bKayfEm9XvN0Ke6i8V3Y+wHHhFldqYYR+zyqvfvFmAQT9kVqW3WG1jDqqiJs3uhrp9iZ/1Adp5707UWORFgUmqcipqdjdObNgaTtZpld9lhTtagbsF8RUENwQALnu8NYKsc1SHBE4olIIUATFb7acnNNUfvqUA/xUhT/VG0GUKEUE/E+WIiqwDJiGyxd24YSnApcrFYzJi2b8gTFdhZ2Fj3cKh5hzW7XTU6Hpf4YiAC8SrIjuBSQAKX8R1Exu2hlV0O4CoTk8157AGmNiwNewek/OsiKwADiKEcJamOEHi9J/L36nmHPFfylC5bw9CKdAiysL87Jzj1tXOl1HdBoxKtfGDEfihSUZM/UBtmQlMU+GoFe5I7D5tanRjqvEj/ktZ0BBoVmQucCyhWYGgmJklebs2daYaP+JLKI6ChDy+qYbBFFHO5DfWXRxpT2nSpEmTJk2aNHc6/wCXiQVfjqIbLQAAAABJRU5ErkJggg==)](/en/partner)[![knots.io](/assets/knots-dRxHGj3F.webp)](/en/partner)[![Aircall](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAIAAAACACAMAAAD04JH5AAAAKlBMVEVHcEwAvYIAv4MAvYIAvYIAvoIAvYIAvYL////a9eyu6dWB3L1R0KYnxpNrGzOeAAAAB3RSTlMAdiDmokDG4kiU6gAABD9JREFUeJzNW9HaoyoMLAL+ivr+r7ug2NYWYSZW2PnOze7pmmlmEqwmjweKzsNaq5Qxpu97rfXfE/4P/q/8/1BKWRs+CV8WCRyi+rD9W8Q8PJudytXgPrYJ3xYNfaCx8vAsxOFDcFHoYzY8CdGXV9eDv0goNg3W/Cx65GCYNHTqx+FXCrASPvm/Dx8ACmHNPeH/QB3uyP4LvSqm/87wAXkG3X3pf8JkjFAjfo5BnfgZBpXinzK43X8vJJ1YMX6SQXdr/X+i/+pItQy448sG9zbABD5EsDedP+fojymo6sANhxTY2gJ46HcfVnbgBtOqBHfolwsaOCDg5YLqJbChv2zBJUL4z582lCiwzNPknpimWcJCybvw5MbhgNHN/FViPxZ0wWlIYKIvE48k3gLzmCIw0DmIJqAtsKTjDyPtAyWzgEvHF4iwmqBjLXAiQEgBK8J6JNIeTDpwg2MJWIEHzxPAp2B1IevBTALoFGjFE8glgE+BgMBpCWwgC0HxNyPZBPgUcFczdBXO+fhsO/SNgCRQUIC1oW8E3O1YMQFkCvxtWUcxLiaATUH3sMzH8zW4gatEyxEAEkBWoqXawAIRcMypzBFAFBg4GyqKAJQAzoaKaYRgAigbGoZA9hx8B2FDigCoAKWBIX6WAV1wB65BTxCAFWA0YAiAFgzAD+X+AZ9FhAKEBhonAFswALYhTuDs59CJBmg71g+UKmHBANiGMAFKAUIDlADahnfA7RglQCowjKgGdxGANQAJsArgdXAfAVADkABZAwGgBhgBrgvFFGAaYASoc2AHVohYKxYoAGoAngUCBcAzGSMgUmAYEBNo6IaE7kIbkELE7ohECmAaQAT4LhQJAHXQI7flQgUgDZDfBdhP0hSAQoQICBWANDDAj9NJTqCsAfLrWGwBxASq/IREbgHkWQXwiEZahAFlEwAELigAnIi2/JjuEoGiCcoPKq9YoGwCXX5UK+8CAaXbovCottCJhEfxjoIJwkujAoFLFiiawJRfWFyyQPE4AN6YXIs/DACBfBncTyD/2m45vfIY4Nb/PE4/li2D9bVd/sVlugjGdWLgee1lnSYQvNFeX1zmG0GyCFxqXGGZk37NlsH66jbfCBIZGKeTtC6pO4dsBrYJhnwZUN8pka/sxRUwwPB1zWxOv1TIfjoOMBRen8/u4PH8zf7h5PAVkm+EcYSjdBoEjzu3l1qhuU8x9OhcebJmHyoEXpp4Er7SPI/iAR8+42t0RqaL9lGqFrN0Aa95utajXO2H2ZqP8zUfaGw/0tl8qJWfZrqMz9nq2inQn9PlzUe7K/tQJ9ZtWo/3t19wqGgDk4z/Hyy5NF/zab/oVMOJxY27xstujxuWLd+ArV22XngMSbhn5ZNZfG289BqFaLn2u6XhB4vPWrz4vKUhrn5LY19c/Y4k4vI7sYLuv/WPlt+PRJ57+Ln1f0uu//8DMROcdiK/IjUAAAAASUVORK5CYII=)](/en/partner)

Not only cat pictures here:

[![LinkedIn](/assets/linkedin-yV12_Qa1.png)](https://linkedin.com/company/till-freitag)[![Instagram](/assets/instagram-DmYWk5ch.png)](https://www.instagram.com/till_freitag_consulting/)[![Luma](data:image/svg+xml,%3csvg%20width='500'%20height='500'%20viewBox='0%200%20500%20500'%20fill='none'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='M400%20250C317.177%20250%20250%20182.822%20250%20100C250%20182.822%20182.823%20250%20100%20250C182.823%20250%20250%20317.178%20250%20400C250%20317.178%20317.177%20250%20400%20250Z'%20fill='currentColor'/%3e%3c/svg%3e)](https://luma.com/till-freitag)

### Solutions

* [All Solutions](/en/solutions)
* [monday.com](/en/services#monday)
* [CRM](/en/services#crm)
* [Use Cases](/en/use-cases)
* [No-Code Solutions](/en/services/nocode-automation)
* [Migration](/en/services/monday-migration)
* [MVP to Production](/en/mvp-to-production)

### AI

* [AI Services](/en/ai)
* [AI & Automation](/en/services/ai-agents)
* [AI First Consultancy](/en/ai-first)
* [AI Tool Selection](/en/ai-toolauswahl)
* [Vibe Coding](/en/vibe-coding)
* [Agentic Engineering](/en/agentic-engineering)
* [Work 2.0](/en/arbeiten-2-0)

### Industries

* [Construction & Real Estate](/en/solutions/construction)
* [Retail & eCommerce](/en/solutions/retail)
* [Industry & Manufacturing](/en/solutions/manufacturing)
* [Technology & Software](/en/solutions/technology)
* [Media & Publishing](/en/solutions/media)
* [Renewable Energy](/en/solutions/renewable-energy)
* [Agencies & Creatives](/en/agenturen)

### Locations

* [Hamburg](/en/beratung)
* [Berlin](/en/beratung)
* [Munich](/en/beratung)
* [Frankfurt](/en/beratung)
* [Cologne](/en/beratung)
* [Stuttgart](/en/beratung)
* [Remote (DACH)](/en/beratung)

### Resources

* [Blog](/en/blog)
* [FAQ](/en/faq)
* [Tools](/en/tools)
* [Toolbox](/en/werkzeugkiste)
* [Events](/en/events)
* [Community](/en/monday-community)
* [References](/en/referenzen)

### Company

* [About Till](/en/team)
* [Partners](/en/partner)
* [monday Agency](/en/monday-agency)
* [Training & Workshop](/en/monday-schulung-workshop)
* [Own Your Monday](/en/own-your-monday)
* [Careers](/en/karriere)
* [Remote Work](/en/remote-work)

Stop fighting your tools. Start using them.Sounds good? Book a [free consultation](/en/beratung).[hi@till-freitag.com](mailto:hi@till-freitag.com)or[+49 40 696 386 96](tel:+494069638696)✌️

© 2023–2026 [Till Freitag](/en/companies-we-like). All rights reserved.

Stuff you gotta have:

[Imprint](/en/impressum)[Privacy](/en/datenschutz)[Terms](/en/agb)[Brand](/en/brand)

![](https://www.facebook.com/tr?id=2016225179316358&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=2016225179316358&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=2016225179316358&ev=PageView&noscript=1)