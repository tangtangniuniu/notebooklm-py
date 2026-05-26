> Source: https://www.lunar.dev/post/why-dynamic-tool-discovery-solves-the-context-management-problem

Dynamic Tool Selection for AI Agents | Solving the Context Management Problem

MCP Risk Score Engine is available! [contact us for early (beta) access.](https://meetings-eu1.hubspot.com/eyal-solomon)

[![](https://cdn.prod.website-files.com/64953aa597d13b0acee8291d/6799376f73f39a24fb24f3d8_Dark%20Mode%20-%20Glow%20-%20Rectangular.svg)](/)

Product

Product

[AI Gateway](/product/ai-gateway)[MCP Gateway](/product/mcp)

Solutions

Use cases

[Employees

Govern Employee AI Tools](/use-cases/employees)[Agent Builders

Control your self-built agents](/use-cases/agent-builders)[Security

For Security teams](/security)

Resources

Learning Hub

[Blog](/lunar-blog)[Guides & Ebooks](/guides-resources)[Tutorials](https://www.youtube.com/channel/UCgWge-0djZcm-JWU82FbR7A)[Customer Stories](/case-study)

[AI Gateway](/product/ai-gateway)

Community

[Discord](https://discord.gg/Kgqu4XQprN)[Twitter](https://twitter.com/lunardevapi)[GitHub](https://github.com/TheLunarCompany/lunar)[YouTube](https://www.youtube.com/@LunarDev-api/videos)[Linkedin](https://linkedin.com/company/lunar-api)

Comparison

[Truefoundry](/comparison/truefoundry)[Kong](/comparison/kong)[Runlayer](/comparison/runlayer)[Obot](/comparison/obot)

[Documentation](https://docs.lunar.dev/mcpx)

[Pricing](/pricing)

Company

[About](/about-us)[In the news](/in-the-news)[Open Source](https://github.com/TheLunarCompany/lunar)[Careers](/about-us#careers)

[Github](#)

[Log in](#)[Get Started](/demo)

[![](https://cdn.prod.website-files.com/64953aa597d13b0acee8291d/6516cb5ad8f1623473e9b83b_github-mark.svg)](https://github.com/TheLunarCompany/lunar)

[Sign In](https://app.lunar.dev/)[Book a demo](https://www.lunar.dev/demo)

# Why dynamic tool discovery solves the context management problem

![Why dynamic tool discovery solves the context management problem](https://cdn.prod.website-files.com/649c330ec64b4a2c43b6fa63/69bade6db437996bd680a53b_Generated%20Image%20March%2018%2C%202026%20-%207_16PM%201.png)

# Why dynamic tool discovery solves the context management problem

Lunar's Intent-Based Dynamic Tool Selection solves the agent context management problem by loading only the tools a task needs at runtime. This post explains how it works, why it matters for accuracy and security, and how to get started.

![Eyal Solomon, Co-Founder & CEO](https://cdn.prod.website-files.com/649c330ec64b4a2c43b6fa63/65c0db66ec6e719a385d88f1_eyal.png)

### Eyal Solomon, Co-Founder & CEO

#### March 18, 2026

#### Tool Scoping

# **Why dynamic tool discovery solves the context management problem**

### TL;DR

* Static tool injection breaks at scale: 50+ tools consume 77K tokens before any task runs
* MCPX's Dynamic Selection, the productized form of progressive tool discovery, drops that to ~8.7K by loading only what the agent needs
* Lunar MCPX delivers this as infrastructure: Tool Groups, policy gating, and auto-refresh
* The result is deterministic tool access, a smaller attack surface, and a full audit trail

![](https://cdn.prod.website-files.com/649c330ec64b4a2c43b6fa63/69badaf23ad833b9bcb0edcd_Line%201.png)

Dynamic tool selection, increasingly known as progressive tool discovery, enables agents to work with massive tool libraries that would otherwise exceed context window limits. The assumption that agents could discover tools at runtime has existed from the start of MCP, but recent advancements in 'tool search' capabilities (following the [Advanced Tool Use framework from Anthropic](https://www.anthropic.com/engineering/advanced-tool-use)) make it practical for production use. The underlying design principle, which Anthropic calls progressive disclosure in its Agent Skills framework, is simple: load what the current task needs, defer the rest.

This evolution in how agents interact with the MCP protocol unlocks new capabilities without pushing context windows to extreme limits, making large-scale tool catalogs viable for the first time.

That shift sounds subtle. It is not. It impacts context efficiency, security posture, orchestration strategy, and ultimately, how scalable your agent architecture can become.

In this post, we unpack the concept, the problems it solves across context, security, and orchestration, and how Lunar.dev productizes the same principle as a governed runtime capability with Tool Groups, policy gating, and tool list auto refresh behavior via MCP list change notifications, where supported.

## **What Dynamic Tool Selection Actually Is**

As tool ecosystems grow, the traditional approach of sending the entire tool catalog in every request quickly breaks down. Large schemas increase token usage, slow down responses, and push the model's context window to its limits. To solve this, Anthropic introduced the Tool Search Tool as part of the Advanced Tool Use framework: a mechanism designed to make large-scale tool libraries practical in production environments.

The idea behind Dynamic Tool Selection is simple but powerful: register the full tool catalog with the API, but avoid loading everything into the model's context up front.

Instead, tools can be marked as deferred:

defer\_loading: true

You register the full tool catalog with the API, but mark most tools as deferred, so they are discoverable but not injected into the model's context up front. The model initially sees only a search primitive and any explicitly non-deferred core tools. When the model needs additional capabilities, it calls the search primitive. The API returns a small number of tool\_reference objects, typically three to five. Only those references are expanded into full schemas inside the active context.

The core principle is: Discovery first. Injection second.

This pattern allows agent systems, MCP servers, and gateway-based architectures to scale to hundreds or thousands of tools without exploding context size, making Dynamic Tool Selection a key building block for real-world, production-grade agent infrastructure.

## **Why Static Full Catalog Injection Breaks at Scale**

Static tool injection assumes that showing the model everything improves decision-making. That works at a small scale. It degrades rapidly as catalogs grow.

### **1. Context and Token Overhead**

Tool schemas consume significant context. Anthropic's data shows 50 MCP tools requiring roughly 72K tokens just for definitions, 77K total before any task execution begins. In typical production setups, 50 tools cost 10K–20K tokens of context that cannot be used for reasoning, memory, or output.

MCPX's dynamic tool selection changes the cost structure. The upfront search primitive costs approximately 500 tokens. A typical search returns 3–5 relevant tools at roughly 3K tokens total. In Anthropic's framing, this results in 8.7K tokens of total context consumption, compared with 77K in the static approach. The difference is structural, not incremental.

![](https://cdn.prod.website-files.com/649c330ec64b4a2c43b6fa63/69bad9852cc50cbf11ec4f4d_4e058686.png)

### **2. Accuracy Degradation**

Tool selection accuracy degrades when too many tools are visible simultaneously. Anthropic's evaluation data shows that selection quality drops significantly once models see more than 30–50 tools in conventional setups. Enabling Tool Search improves MCP evaluation accuracy by reducing the visible tool space.

Fewer visible tools reduce interference and ambiguity. In production, we've seen this translate directly to fewer incorrect tool calls and fewer retry loops.

### **3. Observability and Governance Blind Spots**

When every tool is always in scope, it becomes harder to answer a basic question: what was the model actually allowed to use at decision time?

Static injection makes the eligibility boundary implicit. Dynamic selection makes it explicit. The discovery step produces a shortlist that can be logged, audited, and analyzed.

## **Context and Token Management Value**

The headline benefit is simple: restore the context window to doing work rather than describing capabilities.

Tool definitions consume significant portions of context. Tool search exists specifically to address both context efficiency and the selection accuracy cliff. By paying for only the tools actually needed for a given task, you preserve the majority of your window for reasoning, chaining, and execution.

For teams running multi-step agents, retrieval-augmented workflows, or long-lived sessions, this is not optimization theater. It is architectural hygiene

## **Security, Governance, and Observability**

Dynamic selection is not a silver bullet for LLM security. It is, however, a structural control.

Threat models increasingly include tool poisoning and prompt injection embedded in tool metadata. If malicious or compromised tool descriptions are injected into the model’s decision boundary, they can manipulate tool calls or bypass guardrails.

We covered the full MCP attack surface in [MCP Risk Analysis: Attack Vectors and Lunar's AI-Driven Risk Assessment](https://www.lunar.dev/post/mcp-risk-analysis-attack-vectors-owasp-guidance-and-lunars-ai-driven-risk-assessment).

Dynamic selection contributes to several governance outcomes:

* **Reduced attack surface in context**: fewer tool schemas are present at any moment.
* **Contextual least privilege**: only tools discovered for the current task are eligible for use.
* **Observability**: discovery produces an explicit shortlist that can be logged and audited.

In other words, dynamic selection narrows exposure windows and clarifies accountability.

## **Agent Efficiency and Orchestration**

Dynamic tool selection improves efficiency in two complementary ways.

First, it improves tool choice. Research reports significant accuracy gains in MCP evaluations when dynamic selection mechanisms are enabled.

Reducing tool space interference aligns with what we observe in production systems: narrower scope improves decision clarity. However, this assumes the model selects the right tools, which is not always guaranteed in practice. Some models perform significantly better at tool selection than others, and results vary depending on the underlying architecture and tuning.

Tool selection quality is also heavily influenced by prompt design. A well-structured prompt guides the model toward the correct tools, while a vague or overloaded prompt can make selection less reliable, leading to unnecessary searches or incorrect tool usage.  [For a deeper look at how prompts shape tool selection and agent reasoning at runtime.](https://www.lunar.dev/post/mcp-prompts-at-runtime-how-agents-reason-execute-and-stay-accurate)

Second, it improves orchestration discipline. Once you can reliably discover relevant tools, you can begin to externalize repeated multi-step sequences from the model and into deterministic workflows. Instead of relying on probabilistic chaining inside the LLM for strict multi-step processes, you can combine discovery with programmatic tool calling, reducing context pollution from intermediate reasoning and making flows more predictable.

‍

Dynamic tool selection often becomes the first step toward a more governed, hybrid orchestration model. Rather than loading every available tool into context up front, the agent discovers what it needs when it needs it.

![](https://cdn.prod.website-files.com/649c330ec64b4a2c43b6fa63/69bad9852cc50cbf11ec4f50_988dbaba.png)

[[Context Usage Comparison: Traditional vs Tool Search Too by Anthropic]](https://www.anthropic.com/engineering/advanced-tool-use)

‍

## **How Lunar Productizes Dynamic Tool Selection**

At [Lunar.dev](https://lunar.dev), we have released Dynamic Tool Group Selection as a governed, runtime implementation of the same principle: agents should see only the tools they need, when they need them, and tool exposure should be centrally controlled.

Within [MCPX](https://docs.lunar.dev/mcpx/):

* **Tool Groups** allow teams to organize tools across multiple servers into reusable collections aligned to workflows.
* These groups can be applied across multiple agents, keeping access consistent across environments.
* Policy gating enables runtime control based on identity, environment, or workload.
* Tool exposure becomes a dynamic control surface rather than a static registry decision.

We also address the stale-tool-view problem. By aligning with MCP list changed notifications, MCPX can signal clients when tool access changes. In clients and IDEs that support this behavior, the tool list can auto-refresh. Where client support is incomplete, fallback behavior may require a restart or periodic resync, depending on the client.

The result is a cross-client, runtime-governed implementation of dynamic tool selection, not just a prompt engineering pattern.

We believe this pattern is foundational for the next generation of governed, production-grade agent systems. We would genuinely value your thoughts and feedback on the feature, how you are approaching tool scaling in your own systems, and where you see the biggest gaps or opportunities in dynamic selection and governance.

Dynamic Tool Group Selection is available now in MCPX. To get started, see the [documentation](https://docs.lunar.dev/mcpx) or [book a demo](https://calendly.com/eyal-lunar/30-min-chat-with-eyal-solomon?month=2026-03).

## ‍

## Ready to Start your journey?

Govern all agentic traffic in real time with enterprise-grade security and control. Deploy safely on-prem, in your VPC, or hybrid cloud.

[Get Started](https://www.lunar.dev/demo)

[![](https://cdn.prod.website-files.com/649c330ec64b4a2c43b6fa63/69fb5f3861e0ea803170a60b_image%20(37)%20(1).png)](/post/how-to-enable-ai-for-every-department-not-just-engineering)

[May 6, 2026

## How to Enable AI for Every Department, Not Just Engineering](/post/how-to-enable-ai-for-every-department-not-just-engineering)

![Rony Sinai, Solution Engineer](https://cdn.prod.website-files.com/649c330ec64b4a2c43b6fa63/69c40e88f3bbc3048c57cb0f_1569259622340.jpeg)

Rony Sinai, Solution Engineer

[![](https://cdn.prod.website-files.com/649c330ec64b4a2c43b6fa63/69ea199a211a9d0e2585dc4a_Generated%20Image%20April%2023%2C%202026%20-%203_49PM%20(1).jpg)](/post/best-practices-for-mcp-secret-management-at-enterprise-scale)

[April 23, 2026

## Best practices for MCP secret management at enterprise scale](/post/best-practices-for-mcp-secret-management-at-enterprise-scale)

![Eyal Solomon, Co-Founder & CEO](https://cdn.prod.website-files.com/649c330ec64b4a2c43b6fa63/65c0db66ec6e719a385d88f1_eyal.png)

Eyal Solomon, Co-Founder & CEO

[![](https://cdn.prod.website-files.com/649c330ec64b4a2c43b6fa63/69e0d15432452eb734ba89ee_Generated%20Image%20April%2012%2C%202026%20-%205_00PM%20(1)%20(1).jpg)](/post/cli-vs-mcp-youre-asking-the-wrong-question)

[April 16, 2026

## CLI vs MCP: You're Asking the Wrong Question](/post/cli-vs-mcp-youre-asking-the-wrong-question)

![Roy Gabbay, Co-Founder & CTO](https://cdn.prod.website-files.com/649c330ec64b4a2c43b6fa63/65c0dc707505cd1896e86f59_roy%201%20(1).png)

Roy Gabbay, Co-Founder & CTO

[![](https://cdn.prod.website-files.com/64953aa597d13b0acee8291d/65ad43c66d1cea5736731c02_exit.webp)](#)![](https://cdn.prod.website-files.com/64953aa597d13b0acee8291d/651beac84d6195a65d9e958c_logo.svg)

## Get Early Access

Join the beta. Be the first to explore the free new features with lunar.dev's API Egress Proxy,

By signing up, I agree with the [Terms](/terms-of-use) and [Privacy Policy](/privacy-policy)

[![](https://cdn.prod.website-files.com/64953aa597d13b0acee8291d/64ca1458a1974f6da44739cf_Dark%20Mode%20-%20Glow%20-%20Rectangular%402x.svg)](/)

The Enterprise Gateway for AI Governance

[![](https://cdn.prod.website-files.com/64953aa597d13b0acee8291d/66a8ac021b5de127772a47d4_twitter-x-fill.svg)](https://twitter.com/lunardevapi)[![](https://cdn.prod.website-files.com/64953aa597d13b0acee8291d/66a8ac014c40e166b72df985_github-fill.svg)](https://github.com/TheLunarCompany/lunar)[![](https://cdn.prod.website-files.com/64953aa597d13b0acee8291d/66a8ac013a4adb1a039022ce_youtube-fill.svg)](https://www.youtube.com/@LunarDev-api/videos)[![](https://cdn.prod.website-files.com/64953aa597d13b0acee8291d/66a8ac01e5b1522483b148c0_linkedin-box-fill.svg)](https://linkedin.com/company/lunar-api)[![](https://cdn.prod.website-files.com/64953aa597d13b0acee8291d/68c01c2b27be8c1b09944ae7_icons8-discord.svg)](https://discord.com/invite/Kgqu4XQprN)

**Contact us**: [info@lunar.dev](mailto:info@lunar.dev)

### Get Started

[AI Gateway](/product/ai-gateway)[MCP Gateway](/product/mcp)[External API management](/product/production-ready-api-consumption-gateway)[Pricing](/pricing)

### Use Cases

[Employees](/use-cases/employees)[Agent builders](/use-cases/agent-builders)[Security](/security)

### Resources

[Documentation](https://docs.lunar.dev/)[Blog](/blog)[FAQs](/product/mcp#faqs)[Tutorials](https://www.youtube.com/channel/UCgWge-0djZcm-JWU82FbR7A)

### Comparison

[Truefoundry](/comparison/truefoundry)[Kong](/comparison/kong)[Runlayer](/comparison/runlayer)[Obot](/comparison/obot)

### Company

[About](/about-us)[In the news](/in-the-news)[Careers](/about-us#careers)[Open Source](https://github.com/TheLunarCompany/lunar)

224 W 35th St., New York, NY

[Privacy & Terms](/privacy-policy)[Terms and Conditions](/terms-of-use)

Copyright @ 2026 Lunar.dev

[Tool Scoping](/tags/tool-scoping)