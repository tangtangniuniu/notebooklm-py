> Source: https://dongliang.medium.com/claude-cowork-6c0244380184

Claude Cowork | by Dong Liang | Medium

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fdongliang.medium.com%2Fclaude-cowork-6c0244380184&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fdongliang.medium.com%2Fclaude-cowork-6c0244380184&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:32:32/1*dmbNkD5D-u45r44go_cf0g.png)

# Claude Cowork

[![Dong Liang](https://miro.medium.com/v2/resize:fill:32:32/1*38KuSM9zqiODHBcDN10bSQ.png)](/?source=post_page---byline--6c0244380184---------------------------------------)

[Dong Liang](/?source=post_page---byline--6c0244380184---------------------------------------)

Follow

8 min read

·

Feb 9, 2026

7

1

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D6c0244380184&operation=register&redirect=https%3A%2F%2Fdongliang.medium.com%2Fclaude-cowork-6c0244380184&source=---header_actions--6c0244380184---------------------post_audio_button------------------)

Share

*originally published at* [*dliangthinks.me*](https://www.dliangthinks.me/technology/)

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:700/1*XRwueJlZag2nYPdgMnjeoA.png)

The SaaSpocalypse: From chat-only AI to agentic AI disrupting SaaS

The “chat-only” AI assistant era is ending.

Launched January 12 for Claude Max subscribers ($200/month), the feature expanded to Claude Pro users ($20/month) just four days later — Anthropic’s signal that it intends to dominate agentic AI.

Analysts are calling it the “SaaSpocalypse,” a watershed moment where general-purpose AI agents began to demonstrably dismantle the business models of entrenched software-as-a-service (SaaS) providers.

## Built with its own AI

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:700/1*lLow--5-mCgcw4seNS1keg.png)

Developers have spent the past year using Claude Code, a terminal-based agent, to refactor codebases and debug errors autonomously. Anthropic noticed something unexpected: users were “hacking” Claude Code for non-coding work — sorting vacation photos, renaming thousands of files.

**Claude Cowork** is that behavior, productized.

Four engineers built Cowork in roughly 10 days — using Claude Code itself to generate most of the code. We’ve seen this pattern before with skill.

The cycle: build tool, turn tool into product.

Philosophy:

* If your tool is good, it deserves use by others
* If we love using this tool, we believe you will too (think Microsoft, but inverted)

## How It Works

Cowork transcends the chatbot; it approaches what AI interaction should be.

With chatbots, you ask a question and receive a response.

With Cowork, you assign a task — and it doesn’t “guess” the answer. It executes a loop of planning and action. Here’s what happens under the hood.

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:700/1*0dBHP119uC1WJJvQXfD3FQ.png)

Chatbot Q&A vs Cowork’s planning and action loop

**The Planner:** Claude analyzes your prompt to build a plan, breaking your high-level request (e.g., “Sort these 500 receipts into folders by month”) into discrete sub-tasks.

**The Orchestrator:** For complex tasks, it spins up parallel sub-agents. It can spawn multiple sub-agents for parallel work. Ask it to summarize 50 papers, and it processes them in parallel threads rather than sequentially. Or, one reads PDF metadata; another handles directory creation.

**The Workers:** These sub-agents share the same CC instance but maintain their own context window so as to avoid cross-contamination. You need to grant Cowork **write permissions** and it can create, edit, rename, and delete files in explicitly authorized folders.

**The Tool-user**: Sub-agents can use skills. They also can use MCPs and Claude in Chrome as tools — verifying facts, looking up documentation, downloading missing data — then return to your local files to complete the task.

**The Presenter**: It can generate and displays artifacts (though display issues currently limit full usability).

For people who are familiar with Claude Code, this is hardly news. There is no question Cowork is just a tailored product from Claude Code. However, this pivot significantly expanded the use of agentic framework from coding (a hugely active but nevertheless very small segment) to literally every white collar work.

Much of how Claude Code works is not public knowledge. The popular alternative OpenCode lacks many of the agentic abilities that CC possesses, although it does offer model flexibility.

It is not only the agent harness layer. It also involves strategic decision on persistent long-term memory layer and on-demand retrieval tools. How does CC keep track of things? According to this [article](https://milvus.io/blog/is-rag-become-outdated-now-long-running-agents-like-claude-cowork-are-emerging.md#Conversation-Retrieval-The-On-Demand-Part),

```
Claude is running background heuristics to decide what’s worth persisting, and it’s not waiting for explicit instructions.  
...  
Claude does _not_ keep a rolling summary like many LLM systems. Instead, it has a toolbox of retrieval functions it can call whenever it thinks it’s missing context. These retrieval calls don’t happen every turn — the model triggers them based on its own internal judgment.
```

In other words, it is much more intelligent than the simple context management we have seen in most chatbot, adding RAG or tool calls when explicitly called but remain largely stateless.

## Safety Concerns

With more power come more responsibility.

Technically, a Cowork workspace is a **Micro-VM**.

When you see “Starting Workspace,” Claude isn’t loading a UI; it’s **provisioning a compute environment.**

* **Booting the OS:** On macOS, Cowork utilizes the **Apple Virtualization Framework (**`VZVirtualMachine`**)**. It downloads and boots a lightweight, custom **Linux root filesystem** in the background.
* **Sandboxing:** It creates a “jail” for itself, mounting only specifically granted folders into this Linux environment. This setup phase — initializing the kernel, mounting volumes, checking network egress — causes that 5–15 second delay.
* **Fresh State:** Every Cowork session starts from a blank slate for security. It doesn’t remember previous sessions’ temporary files, so it rebuilds the environment each time.

Unlike standard containers (like Docker), which share the host’s OS kernel, a Micro-VM (via `VZVirtualMachine`) provides higher isolation. This is why Cowork is currently macOS-exclusive; it relies on Apple's hardware-accelerated virtualization to run safely and quickly.

## Get Dong Liang’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Subscribe

Remember me for faster sign in

Because Cowork runs in a VM, it can’t “escape” to delete System files. However, it **can** delete anything inside folders you grant it access to. Tell it to “Clean up my desktop,” and if its plan is “Delete everything that isn’t a PDF,” it will do exactly that without hesitation.

## Plugins

Cowork is highly volatile at this stage and may evolve in multiple directions.

The recent plugin addition is a strong move. Plugins were first implemented in Claude Code and now available in Cowork, and in even better forms.

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:700/1*xMEqAQWn0SKNes1XzGHSsA.png)

Claude Code plugin system architecture and workflow

A plugin is an extension that enhance Claude Code. It is literally a package that contains custom slash commands, specialized agents, hooks, and MCP servers. Plugins can be shared across projects and teams, providing consistent tooling and workflows.

Once a plugin is installed. You can see the content, such as all the commands and skills included in this plugin. You can read through the skill definition, which is a hugely important way to understand and fine-tune the behavior of these skills.

It even allows you to edit the skill directly, by sending it over to a markdown editor such as VSC or Cursor. This is not ideal but I am sure it will be fixed. I am not sure if you need to reload the skill after you have changed things.

Technically, these tools are packaged and live on a repo. The owner name and repo name retrieve it — an idea familiar to git users.

Additional details are added to make it a marketplace.

A marketplace can host multiple plugins. In each plugin folder, you declare what’s being packaged with a plugin.json file.

## Industry-specific Productization

While Cowork sets up an agentic framework for AI interaction, Anthropic is also making a massive enterprise backend play. Plugins really could help here.

On January 11, the company launched [**Claude for Healthcare** and **Claude for Life Sciences**](https://www.anthropic.com/news/healthcare-life-sciences).

Under the hood, the package includes specialized connectors and skills: two features that Anthropic pioneered to great success.

This method is highly scalable.

For the immediate future, these connectors and skills can be packaged into plugins, which then can be conveniently loaded into specially branded versions of Cowork.

In fact, some of the these industry-oriented plugin already appears, such as [legal](https://claude.com/plugins/legal), and [finance](https://claude.com/plugins/finance).

The plugin ecosystem is rapidly expanding, including not only languages (java, kotlin, Go, C#), specific platforms or services (slack, notion, stripe, supabase) but also domains such as customer service, sales, marketing.

## From Subagent to Agent Teams

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:700/1*BrFC5qk6SC13AQsjUQqNBQ.png)

Hierarchical Subagents vs Collaborative Agent Teams

Cowork primarily uses what Anthropic calls **Subagents** — a hierarchical, hub-and-spoke model.

* **Implementation:** Give Cowork a task, and the “Lead” agent (the one you address) creates a plan, then spawns temporary sub-processes. These subagents are ephemeral, existing only for specific sub-tasks (e.g., “summarize these 10 files”).
* **Communication:** Subagents are strictly subordinate. They report only to the Lead, perform their task, return results to the Lead’s context, then terminate.
* **Context:** Subagents maintain their own context windows to avoid cluttering the Lead’s, but once finished, the Lead must summarize or ingest their output to proceed.

The “Agent Teams” feature (introduced Feb 5, currently experimental in Claude Code) shifts from hierarchical to **Collaborative Network** model.

* **Implementation:** Instead of temporary workers, Agent Teams creates multiple full-fledged Claude Code instances. One serves as **Team Lead**, but the others are **Teammates** with equal agency.
* **The Mailbox System:** This is the core technical differentiator. Agent Teams use a local messaging protocol (often stored in `~/.claude/teams/`) that functions as a mailbox. Agents can `message` or `broadcast` to one another. They don't merely report to the boss; they debate each other, share findings, request help from peers.
* **Shared Task List:** They use a centralized, file-locked task list enabling **self-coordination**. When a teammate finishes a task, they consult the shared list, “claim” the next pending item, mark it “in-progress.” This prevents race conditions or overwrites common in simpler agentic setups.
* **Independence:** Unlike subagents, teammates are independent. You can switch to a teammate’s view (using `Shift+Up/Down` or `tmux` panes) and address them directly, overriding the lead's instructions for that specific agent.

> Technical manual for Agent teams: <https://code.claude.com/docs/en/agent-teams>
>
> Building a C compiler with a team of parallel Claudes: <https://www.anthropic.com/engineering/building-c-compiler>

Now, given the track record of how products evolve at Anthropic, I have reasons to believe that this agent team feature will eventually arrive in Cowork. But maybe more urgent priorities are how to make this feature more usable in Claude Code. I have done some tests with it and noted the extra scaffolding (installing iTerm2 or setting up tmux) is not user friendly.

## The Path Forward

Cowork is labeled “Research Preview” for a reason. It still has a big to-do list to meet mass adoption.

* **Platform:** Currently **macOS only**. Windows and Linux support is planned but undated.
* **No “Memory”:** Claude doesn’t retain context between Cowork sessions. Every task starts from scratch.
* **No “Projects” Integration:** You can’t currently use Cowork within Claude Projects (Anthropic’s shared workspace/knowledge base tool).
* **Limited External Connectors:** While Claude has Google Drive integration in standard chat (via private projects), early users report external connectors in Cowork are “not that reliable yet,” limiting effectiveness for tasks requiring stable third-party integrations.
* **Session Persistence:** The Claude Desktop app must remain **open** for tasks to run. Close your laptop lid or quit the app, and the agent dies.

[Claude](https://medium.com/tag/claude?source=post_page-----6c0244380184---------------------------------------)

[AI](https://medium.com/tag/ai?source=post_page-----6c0244380184---------------------------------------)

[AI Agent](https://medium.com/tag/ai-agent?source=post_page-----6c0244380184---------------------------------------)

7

7

1

[![Dong Liang](https://miro.medium.com/v2/resize:fill:48:48/1*38KuSM9zqiODHBcDN10bSQ.png)](/?source=post_page---post_author_info--6c0244380184---------------------------------------)

[![Dong Liang](https://miro.medium.com/v2/resize:fill:64:64/1*38KuSM9zqiODHBcDN10bSQ.png)](/?source=post_page---post_author_info--6c0244380184---------------------------------------)

Follow

[## Written by Dong Liang](/?source=post_page---post_author_info--6c0244380184---------------------------------------)

[124 followers](/followers?source=post_page---post_author_info--6c0244380184---------------------------------------)

·[12 following](/following?source=post_page---post_author_info--6c0244380184---------------------------------------)

Reading, Writing, Parenting

Follow

[Help](https://help.medium.com/hc/en-us?source=post_page-----6c0244380184---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----6c0244380184---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----6c0244380184---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----6c0244380184---------------------------------------)

[Press](mailto:pressinquiries@medium.com)

[Blog](https://blog.medium.com/?source=post_page-----6c0244380184---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----6c0244380184---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----6c0244380184---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----6c0244380184---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----6c0244380184---------------------------------------)