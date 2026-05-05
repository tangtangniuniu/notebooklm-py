> Source: https://www.descope.com/learn/post/mcp

What Is the Model Context Protocol (MCP) and How It Works

[Skip to main contentArrow Right](#main-content)

Get your complimentary copy of the Gartner Report: IAM Adapts to Secure and Enable AI Agents. [Let's go >](https://hello.descope.com/gartner-reprint)

[Log InUser Circle](https://app.descope.com)

[![Descope.com Logo](https://images.ctfassets.net/xqb1f63q68s1/1yC6rbxovvGLHcNiiXkhgf/9010920c6ac89c6017c00097d4c43233/Frame__1_.svg)](/)

* Product
* Use Cases
* Developers
* [Customers](/customers)
* Resources
* Company
* Pricing

[Sign upArrow Right](/sign-up)[Book a demoArrow Right](/demo)

[![Descope.com Logo](https://images.ctfassets.net/xqb1f63q68s1/1yC6rbxovvGLHcNiiXkhgf/9010920c6ac89c6017c00097d4c43233/Frame__1_.svg)](/)

```
# Contents

## Summary
Explains the Model Context Protocol (MCP), how it standardizes LLM integration with external systems, and its client-server architecture.

## Key concepts
- Model Context Protocol (MCP) – Standardized protocol for LLMs to connect with external tools and data
- The NxM problem – Challenge of integrating N LLMs with M external systems without custom code for each combination

## Main points
- MCP replaces custom integrations with a universal standard across all LLMs and external systems
- Rapid ecosystem adoption: Many different MCP clients and growing number of official/community servers already available
- Security relies on OAuth 2.1, least privilege, human-in-the-loop permissions, and PKCE
- Upcoming: official registry, sampling capabilities, improved authorization specs

# Context

## Audience
Developers evaluating or building MCP integrations.

## Taxonomy
Learning center guide. Part of Descope's MCP series; foundational for security and deployment posts.

## Prerequisites / Related reading

**Related reading:**
- [Top 6 MCP Vulnerabilities](https://www.descope.com/blog/post/mcp-vulnerabilities) – Explores threats and mitigations
- [Diving Into the MCP Authorization Specification](https://www.descope.com/blog/post/mcp-auth-spec) – OAuth implementation discussion

# Authority

## Descope's authority
Descope secures production MCP deployments and advises enterprises on safe MCP integration.

## Why this matters
MCP standardization is foundational infrastructure for production AI applications. Understanding its architecture is essential for developers building connected AI systems.
```

[IdentipediaArrow Left](/learn)

# What Is the Model Context Protocol (MCP) and How It Works

January 15, 2026Copy link

Share on:

Share on LinkedIn

Share on X

[Share on Blusky](https://bsky.app/intent/compose?text=)

![Model Context Protocol logo on a dark blue background with subtle geometric corner elements.](/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fxqb1f63q68s1%2FBqnOT8KVznDb8nNCWIz2D%2F33e516bb9885414284f895e73d6e4efe%2FMCP_learning_center_thumbnail.png&w=3840&q=75)

![](/_next/static/media/blog-post-hero.04309608.svg)

![](/_next/static/media/blog-post-hero.04309608.svg)

Table of Contents

LLM isolation & the NxM problem

Open table of contents

Table of Contents

* [LLM isolation & the NxM problem](#llm-isolation-&-the-nxm-problem)
* [MCP architecture and core components](#mcp-architecture-and-core-components)
* [How MCP works](#how-mcp-works)
* [MCP client & server ecosystem](#mcp-client-&-server-ecosystem)
* [Security considerations for MCP servers](#security-considerations-for-mcp-servers)
* [Conclusion](#conclusion)

Identity and auth news.

  

Straight to your inbox.

Subscribe

Summarize with AI

Don't have the time to read the entire post? Our human writers will be sad, but we understand. Summarize the post with your preferred LLM here instead.

Summarize with AI

Large language models (LLMs) like Claude, ChatGPT, Gemini, and Llama have completely changed how we interact with information and technology. They can write eloquently, perform deep research, and solve increasingly complex problems. But while typical models excel at responding to natural language, they’ve been constrained by their isolation from real-world data and systems.

The **Model Context Protocol (MCP)** addresses this challenge by providing a standardized way for LLMs to connect with external data sources and tools—essentially a “universal remote” for AI. Released by Anthropic as an open-source protocol, MCP builds on existing function calling by eliminating the need for custom integration between LLMs and other apps. This means developers can build more capable, context-aware applications without reinventing the wheel for each combination of AI model and external system.

![Comparison diagram showing LLM integration before and after MCP. On the left, an LLM connects directly to Google Drive, Slack, and GitHub through separate unique APIs. On the right, the LLM connects through a single unified API to the Model Context Protocol, which then connects to each service through their unique APIs, thereby reducing integration complexity.](/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fxqb1f63q68s1%2F2x3R1j8peZzdnweb5m1RK3%2Fa8628561358334a605e7f291560fc7cc%2FMCP_learning_center_image_1-min__1_.png&w=1920&q=75)

Fig: Diagram illustrating integration complexity before and after MCP

This guide explains the Model Context Protocol’s architecture and capabilities, how it solves the inherent challenges of AI integration, and how you can begin using it to build better AI apps that go beyond isolated chat interfaces.

## LLM isolation & the NxM problem

It’s no secret that LLMs are remarkably capable, but they typically operate in isolation from real-world systems and current data. This creates two distinct but related challenges: one for end users, and one for developers and businesses.

For everyday users, the isolation means a constant “copy and paste tango” to get relevant responses about recent data. This requires manually collecting information from various sources, feeding it into the LLM’s chat interface, and then extracting or applying the AI’s output elsewhere.

While several models offer [AI-powered web search](https://www.descope.com/customers/you-com), and Anthropic’s Claude 3.7 and 4 models [boast a Computer Use feature](https://docs.anthropic.com/en/docs/agents-and-tools/computer-use), they still lack direct integration with knowledge stores and tools. Even as major platforms like [OpenAI’s ChatGPT](https://help.openai.com/en/articles/10847137-chatgpt-synced-connectors) and [Google’s Gemini](https://support.google.com/gemini/answer/13695044) add built-in app integrations, these remain platform-specific solutions rather than universal standards.

For devs and enterprises, the challenge is much more complex: the “NxM problem,” where *N* represents LLMs and *M* stands for tools. On the *N* side, there are many AI systems, and on the *M* side, there are countless systems. Each LLM provider has their own protocols to connect with external tools, making the potential integration points essentially endless.

By breaking the NxM problem down, we can see it causes:

* **Redundant development efforts:** Dev teams will repeatedly solve the same integration issues for each new AI model or data source. For example, connecting ChatGPT with your knowledge stores requires starting from scratch with custom code. But with every additional AI system or tool, your devs have to do *everything* from the beginning each time—*N* multiplied by *M*.
* **Excessive maintenance:** Tools, models, and APIs will inevitably evolve, and business will want to stay on the cutting edge. The lack of standardization means an integration can potentially stop working because a tool or model is updated, or an old one is deprecated.
* **Fragmented implementation:** Different integrations may handle similar functions in totally unexpected ways, creating unpredictable or undesirable results. This fragmentation can lead to end user confusion or frustration as different developers and companies implement inconsistent integrations.

However, it’s important to understand that MCP doesn’t solve the NxM problem by simply replacing the integration methods that came before. It connects AI apps to context while building on top of function calling—the primary method for calling APIs from LLMs—to make development simpler and more consistent.

### Relationship between function calling & Model Context Protocol

Function calling, which allows LLMs to invoke predetermined functions based on user requests, is a well-established feature of modern AI models. Sometimes referred to as “tool use,” function calling is not mutually exclusive with MCP; the new protocol simply standardizes how this API feature works, adding context for the LLM. This is achieved by streaming tool definitions (including their capabilities, data stores, and possible prompts) to LLMs from the MCP server.

Without MCP, when you use a function call directly with an LLM API, you need to:

* Define model-specific function schemas, which are JSON descriptions of the function, acceptable parameters, and what it returns.
* Implement handlers (the actual code that executes when a function is called) for those functions.
* Create different implementations for each model you support.

MCP standardizes this process by:

* Defining a consistent way to specify tools (functions) across any AI system.
* Providing a protocol for discovering available tools and executing them.
* Creating a universal, plug-and-play format where any AI app can use any tool without custom integration code.

You might be familiar with AI apps that use function calling, like Custom GPTs using [GPT Actions](https://platform.openai.com/docs/actions/introduction). A Custom GPT can determine which API call resolves the user's prompt, create the necessary JSON, then make the API call with it. While this allows some purpose-built tooling, it’s bound to OpenAI’s ecosystem. MCP brings similar capabilities to any AI application that implements the protocol, regardless of the underlying model vendor.

**Also read:** [**MCP vs Function Calling**](https://www.descope.com/blog/post/mcp-vs-function-calling)

## MCP architecture and core components

The Model Context Protocol uses a client-server architecture [partially inspired by the Language Server Protocol (LSP)](https://spec.modelcontextprotocol.io/specification/2024-11-05/), which helps different programming languages connect with a wide range of dev tools. Similarly, the aim of MCP is to provide a universal way for AI applications to interact with external systems by standardizing context.

![MCP Architecture diagram showing a host application with an MCP client (such as Claude, an IDE, or other tools) connecting via MCP Protocol to three MCP servers. Each server connects to a different data source: Server A and B connect to local data sources, while Server C connects to a remote service via web APIs over the internet.](/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fxqb1f63q68s1%2F6R2RtSw84mTFLKfYBPpqNQ%2Ff1ef779c252dde2997f6cc1ab92fa794%2FMCP_general_architecture-min.png&w=1920&q=75)

Fig: MCP general architecture

### Core components

MCP architecture consists of four primary elements:

![MCP core components](/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fxqb1f63q68s1%2FtED7RTeh1GJfWR3x7DuZJ%2F7e79ee0829dcbb039ab6dc635f2dbf32%2FMCP_core_components-min.png&w=1920&q=75)

Fig: MCP core components

* **Host application:** Applications housing LLMs (or LLMs themselves) that interact with users and initiate connections. This includes Claude Desktop, AI-enhanced IDEs like Cursor, and standard web-based LLM chat interfaces.
* **MCP client:** Integrated within the host application to handle connections with MCP servers, translating between the host’s requirements and the Model Context Protocol. Clients are built into host applications, like the MCP client inside Claude Desktop.
* **MCP server:** Adds context and capabilities, exposing specific functions to AI apps through MCP. Each standalone server typically focuses on a specific integration point, like GitHub for repository access or a PostgreSQL for database operations.
* **Transport layer:** The communication mechanism between clients and servers. MCP supports two primary transport methods:

  + **STDIO (Standard Input/Output):** Mainly local integrations where the server runs in the same environment as the client.
  + **HTTP+SSE (Server-Sent Events):** Remote connections, with HTTP for client requests and SS for server responses and streaming.

All communication in MCP uses [JSON-RPC 2.0](https://www.jsonrpc.org/specification) as the underlying message standard, providing a standardized structure for requests, responses, and notifications.

## How MCP works

When a user interacts with a host application (an AI app) that supports MCP, several processes occur behind the scenes to enable quick and seamless communication between the AI and external systems. Let’s take a closer look at what happens when a user asks Claude Desktop to perform a task that invokes tools outside the chat window.

### Protocol handshake

1. **Initial connection:** When an MCP client (like Claude Desktop) starts up, it connects to the configured MCP servers on your device.
2. **Capability discovery:** The client asks each server "What capabilities do you offer?" Each server responds with its available tools, resources, and prompts.
3. **Registration:** The client registers these capabilities, making them available for the AI to use during your conversation.

![Sequence diagram showing how MCP handles a user request. The user asks Claude "What's the weather in San Francisco?" Claude recognizes the need for external data and requests to use MCP capability. The MCP client displays a permission request, the user grants permission, and the client sends the request to the MCP server. The server queries the external system, returns formatted results, and Claude responds with the contextual answer.](/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fxqb1f63q68s1%2F5uCDzIdxqiMSlIXx2Z9w73%2F21bd511971ecc7115f2edee0bdc8a17c%2FMCP_Claude_Mermaid_Chart.png&w=3840&q=75)

Fig: A mermaid chart created by Claude, demonstrating how Claude uses external tools with MCP.

### From user request to external data

Let's say you ask Claude, "What's the weather like in San Francisco today?" Here's what happens:

1. **Need recognition:** Claude analyzes your question and recognizes it needs external, real-time information that wasn't in its training data.
2. **Tool or resource selection:** Claude identifies that it needs to use an MCP capability to fulfill your request.
3. **Permission request:** The client displays a permission prompt asking if you want to allow access to the external tool or resource.
4. **Information exchange:** Once approved, the client sends a request to the appropriate MCP server using the standardized protocol format.
5. **External processing:** The MCP server processes the request, performing whatever action is needed—querying a weather service, reading a file, or accessing a database.
6. **Result return**: The server returns the requested information to the client in a standardized format.
7. **Context integration:** Claude receives this information and incorporates it into its understanding of the conversation.
8. **Response generation:** Claude generates a response that includes the external information, providing you with an answer based on current data.

Ideally, this entire process happens in seconds, creating an unobtrusive experience where Claude appears to "know" information it couldn't possibly have from its training data alone.

### Additional protocol capabilities

Since its initial release, MCP has added several significant functions that enhance its capabilities:

**Sampling** allows servers to request LLM completions from clients. For example, an MCP server helping with code review could recognize the need for additional context and ask the client’s LLM to generate a summary of recent changes. This enables an essentially “agentic” workflow while still retaining client control over model access, selection, and permissions—all without needing server API keys.

**Elicitation** enables servers to request additional information from users during their operations. For instance, if the GitHub MCP server needs to know which branch to commit to because it wasn’t described in the prompt, it can ask the user for that information mid-operation using structured JSON schemas to validate the response. This enables more interactive workflows while maintaining security through human oversight.

**Roots** are a standardized way for clients to expose filesystem boundaries to servers. For example, when using an MCP server for file operations, the client can specify that the server only has access to `/user/documents/project/` rather than the entire filesystem, preventing accidental (or malicious) access to sensitive data stores.

## MCP client & server ecosystem

Since its introduction in late 2024, MCP has experienced explosive growth. Some MCP marketplaces claim nearly 16,000 unique servers at the time of writing, but the real number (including those that aren’t made public) could be considerably higher.

### Examples of MCP clients

The MCP client ecosystem now includes:

* [Claude Desktop](https://support.anthropic.com/en/articles/10949351-getting-started-with-local-mcp-servers-on-claude-desktop): The original, first-party desktop application with comprehensive MCP client support
* [Claude Code](https://docs.anthropic.com/en/docs/claude-code/mcp): Command-line interface for agentic coding, complete with MCP capabilities
* [Cursor](https://docs.cursor.com/en/tools/mcp): The premier AI-enhanced IDE with one-lick MCP server installation
* [Windsurf:](https://docs.windsurf.com/windsurf/cascade/mcp) Previously known as Codeium, an IDE with MCP support through the Cascade client
* [Continue](https://docs.continue.dev/customize/deep-dives/mcp): Open-source AI coding companion for JetBrains and VS Code
* [Visual Studio Code](https://code.visualstudio.com/blogs/2025/06/12/full-mcp-spec-support): Microsoft’s IDE, which added MCP support in June 2025
* [JetBrains IDEs](https://www.jetbrains.com/help/ai-assistant/mcp.html): Full coding suite that added AI Assistant MCP integration in August 2025
* [Xcode](https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp/extend-copilot-chat-with-mcp?tool=xcode): Apple’s IDE, which received MCP support through GitHub Copilot in August 2025
* [Eclipse](https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp/extend-copilot-chat-with-mcp?tool=eclipse): Open-source IDE with MCP support through GitHub Copilot as of August 2025
* [Zed](https://zed.dev/blog/mcp): Performance-focused code editor with MCP prompts as slash commands
* [Sourcegraph Cody](https://sourcegraph.com/blog/cody-supports-anthropic-model-context-protocol): AI coding assistant implementing MCP through OpenCtx
* [LangChain](https://github.com/langchain-ai/langchain-mcp-adapters): Framework with MCP adapters for agent development
* [Firebase Genkit](https://github.com/firebase/genkit/tree/main/js/plugins/mcp): Google’s AI development framework with MCP support
* [Superinterface](https://superinterface.ai/blog/mcp): Platform for adding in-app AI assistants with MCP functionality

Notably, IDEs like Cursor and Windsurf have turned MCP server setup into a one-click affair. This dramatically lowers the barrier for developer adoption, especially among those already using AI-enabled tools. However, consumer-facing applications like Claude Desktop still require manual configuration with JSON files, highlighting an increasingly apparent gap between developer tooling and consumer use cases.

### Examples of MCP servers

The MCP ecosystem comprises a diverse range of servers including reference servers (created by the protocol maintainers as implementation examples), official integrations (maintained by companies for their platforms), and community servers (developed by independent contributors).

#### Reference servers

Reference servers demonstrate core MCP functionality and serve as examples for developers building their own implementations. These servers, maintained by MCP project contributors, include fundamental integrations like:

* [**Git**](https://github.com/modelcontextprotocol/servers/tree/main/src/git)**:** This server offers tools to read, search, and manipulate Git repositories via LLMs. While relatively simple in its capabilities, the Git MCP reference server provides an excellent model for building your own implementation.
* [**Filesystem**](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem)**:** Node.js server that leverages MCP for filesystem operations: reading/writing, creating/deleting directories, and searching. The server offers dynamic directory access via Roots, a recent MCP feature that outlines the boundaries of server operation within the filesystem.
* [**Fetch**](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch): This MCP server provides web content fetching capabilities. This server converts HTML to markdown for easier consumption by LLMs. This allows them to retrieve and process online content with greater speed and accuracy.

#### Official MCP integrations

These servers are officially supported by the companies who own the tools. Integrations like these are production-ready connectors available for immediate use.

* [**Stripe**](https://github.com/stripe/agent-toolkit)**:** This integration can handle use cases like generating invoices, creating customers, or managing refunds through natural language requests. Here, the main draw is the potential for delegating payment concerns to customer-facing chatbots.
* [**Supabase**](https://github.com/supabase-community/supabase-mcp): This official MCP server allows users to interact with Supabase through an LLM: creating tables, querying data, deploying edge functions, and even managing branches. As an added security measure, Supabase MCP employs a SQL result wrapper to discourage LLMs from obeying malicious commands hidden in the data.
* [**Apify**](https://github.com/apify/actors-mcp-server)**:** Through the use of over 4,000 Apify Actors, enables a wide range of functions including a RAG (Retrieval Augmented Generation) web browser, data scraping across multiple platforms, and content crawling.

#### Community MCP servers

The community-driven ecosystem exemplifies how standardization can accelerate adoption and creativity. The following servers are maintained by enthusiasts rather than businesses, which means they trend toward a more diverse range of needs.

* [**Discord**](https://github.com/v-3/discordmcp)**:** The gaming-focused messaging app Discord shares many similarities with Slack, and the MCP server integration is no different. This allows users to send and read messages, with automatic server and channel discovery for easier navigation.
* [**Docker**](https://github.com/ckreiling/mcp-server-docker)**:** Enables natural language interaction with Docker to manage containers, volumes, and images. Intended for server admins and tinkerers, this abstracts Docker both local and remote engine management into a friendlier interface.
* [**HubSpot**](https://github.com/buryhuang/mcp-hubspot)**:** This integration with ubiquitous CRM HubSpot allows users to list and create contacts, get recent engagements, and manage companies. While simple, this server provides a simple way to retrieve information for use with other tools.

## Security considerations for MCP servers

The rapid adoption of MCP has opened numerous, critical security challenges. [Research by Knostic in July 2025](https://www.knostic.ai/blog/mapping-mcp-servers-study) involved scanning nearly 2,000 MCP servers exposed to the internet, with all verified servers lacking any form of authentication. This essentially means anyone could access internal tool listings and potentially exfiltrate sensitive data. Similarly, [Backslash Security’s June 2025 findings](https://www.backslash.security/blog/hundreds-of-mcp-servers-vulnerable-to-abuse) identified similar vulnerabilities in another 2,000 servers, noting patterns of over-permissioning and complete exposure on local networks.

The June 2025 update to the MCP authorization specification addresses some concerns by classifying MCP servers as OAuth Resource Servers, while requiring clients to implement Resource Indicators (RFC 8707). This intends to prevent malicious servers from obtaining access tokens, but implementation remains inconsistent. The MCP auth spec can’t really solve these issues if implementers don’t actually add security.

One cautionary tale of over-permissioning emerged in July 2025, when Replit’s AI agent [deleted a production database containing over 1,200 records](https://fortune.com/2025/07/23/ai-coding-tool-replit-wiped-database-called-it-a-catastrophic-failure/). This was in spite of explicit instructions (a “code and action freeze”) meant to prevent any changes to production systems. The lesson in this appears to be that proper permissioning, had it been handled via OAuth scopes externally, might have saved their code.

For comprehensive guidance on MCP authentication and authorization, see Descope’s [MCP auth spec guide](https://www.descope.com/blog/post/mcp-auth-spec), and for enterprise deployment considerations, refer to our [enterprise MCP challenges article](https://www.descope.com/blog/post/enterprise-mcp).

Ultimately, human-in-the-loop design remains crucial to keeping LLMs in their appropriate roles, avoiding painful misfires. Clients must request explicit permission before accessing tools or resources, but this protection depends on specific permission prompts—and users understanding the impact of their choices.

## Conclusion

The Model Context Protocol represents a significant leap in connecting LLMs to external systems, standardizing a fragmented ecosystem and potentially resolving the NxM problem. By universalizing how AI applications talk to tools and data sources, MCP reduces development overhead and enables a more interoperable ecosystem where innovation benefits the entire community—rather than remaining siloed.

As MCP continues to progress as a standard, several new developments have appeared on the horizon:

* **Secure elicitation:** The current elicitation mechanism is only for gathering non-sensitive information from users through structured, in-band requests. This proposed new `url` mode for the elicitation capability would secure out-of-band interactions that bypass the MCP client, addressing scenarios such as gathering credentials and handling payments without exposing sensitive data to the MCP client.
* [**Progressive scoping**](https://www.descope.com/blog/post/progressive-scoping)**:** Scoping recklessly can lead to a variety of risks, including malicious incidents. Progressive scoping instead looks at the intent of a tool (what it wants to do) and whether it has permission to do so.This proposed change would introduce an MCP-specific field for a `scopes_default` extension for Protected Resource Metadata (PRM), while defining a scope error handling strategy.
* **Client ID metadata documents:** This proposed change addresses a common MCP scenario in which servers and clients have no pre-existing relationship, mainly due to its reliance on two registration policies: pre-registration, and Dynamic Client Registration (DCR). Both pose significant drawbacks in execution. Client ID metadata documents could reside at specific HTTPS URLs, and OAuth clients could use these URLs as client identifiers. This would enable servers to trust previously unknown clients while retaining total control over authorization policy.

While these upcoming additions will further cement MCP’s role in making AI development faster and easier, the protocol has already made a huge impact on the LLM ecosystem. Providing a common format for integrations amounts to more than speeding up the processes we already have. It has created a space where both major enterprises and individual contributors can build equally viable, increasingly valuable options to make everyone’s lives better.

For more developer updates from the world of authentication, access control, and AI, subscribe to our blog or [follow us on LinkedIn](https://www.linkedin.com/company/descope/). If you’re building MCP servers and looking for identity infrastructure that accelerates their time to production while enhancing security, check out our [MCP Auth SDKs](https://www.descope.com/blog/post/mcp-auth-sdk).

Identity and auth news.

  

Straight to your inbox.

Subscribe

## Liked what you saw?

Check out these posts next

[![What is Open Authorization (OAuth 2.0)?](/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fxqb1f63q68s1%2Fb05EHbTofRMBEGoZYnckn%2Fdd6feda3556abe00dd9e01510db126a5%2FOAuth_learning_center___others.png&w=3840&q=75)

Auth protocols & standards | Apr 14, 2026

### What Is OAuth & How Does It Work

Read more](/learn/post/oauth)[![FGA LC SEO image](/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fxqb1f63q68s1%2FhvRqdLadPwDVW8M4pU5ve%2F4c72bd949881b1d0f173c7b9bb38dae1%2FFGA_learning_center___others.png&w=3840&q=75)

Authentication basics | Nov 22, 2024

### Fine-Grained Authorization Explained & When to Use It

Read more](/learn/post/fine-grained-authorization)[![Token-based auth thumbnail](/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fxqb1f63q68s1%2F6NKXH7N76bVccop2J5eK7B%2F1e989eb4f9f2a09bcd141ce7f0d80c7c%2FToken_auth_learning_center___others.png&w=3840&q=75)

Authentication basics | Mar 17, 2024

### What Is Token-Based Authentication & How It Works

Read more](/learn/post/token-based-authentication)

[![What is Open Authorization (OAuth 2.0)?](/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fxqb1f63q68s1%2Fb05EHbTofRMBEGoZYnckn%2Fdd6feda3556abe00dd9e01510db126a5%2FOAuth_learning_center___others.png&w=3840&q=75)

Auth protocols & standards | Apr 14, 2026

### What Is OAuth & How Does It Work

Read more](/learn/post/oauth)[![FGA LC SEO image](/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fxqb1f63q68s1%2FhvRqdLadPwDVW8M4pU5ve%2F4c72bd949881b1d0f173c7b9bb38dae1%2FFGA_learning_center___others.png&w=3840&q=75)

Authentication basics | Nov 22, 2024

### Fine-Grained Authorization Explained & When to Use It

Read more](/learn/post/fine-grained-authorization)[![Token-based auth thumbnail](/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fxqb1f63q68s1%2F6NKXH7N76bVccop2J5eK7B%2F1e989eb4f9f2a09bcd141ce7f0d80c7c%2FToken_auth_learning_center___others.png&w=3840&q=75)

Authentication basics | Mar 17, 2024

### What Is Token-Based Authentication & How It Works

Read more](/learn/post/token-based-authentication)

[Descope - Go to homepage](/)

[Chat with Sales](https://start-chat.com/slack/descope/V5mA8i)

Anonymously - no Slack account required

![G2 Users Love Us](https://images.ctfassets.net/xqb1f63q68s1/1TPXtSvPWcaJp65NJVlbIz/e71c60b6108453617aed120e5ad8323f/G2_Users_Love_Us.svg)[Leave a Descope review](https://www.g2.com/products/descope/reviews)

Product

* [Platform Overview](/product)
* [Descope Flows](/flows)
* [Integrations](/integrations)
* [Changelog](https://docs.descope.com/changelog)
* [Descope vs Auth0](/descope-vs-auth0)
* [Descope vs Ping Identity](/descope-vs-ping)
* [Descope vs Okta CIS](/descope-vs-okta-cis)
* [Descope vs Amazon Cognito](/descope-vs-amazon-cognito)
* [Descope vs Stytch](/descope-vs-stytch)
* [Descope vs WorkOS](/descope-vs-workos)
* [Descope vs Frontegg](/descope-vs-frontegg)

App Use Cases

* [Passwordless](/use-cases/passwordless-authentication)
* [Identity Federation](/use-cases/identity-federation)
* [ATO Prevention](/use-cases/fraud-prevention)
* [Identity Orchestration](/use-cases/identity-orchestration)

Authentication Methods

* [Social Logins](/use-cases/oauth-social-logins)
* [Passkeys](/use-cases/passkeys)
* [MFA](/use-cases/mfa)
* [Biometrics / WebAuthn](/use-cases/biometrics)
* [Magic Links](/use-cases/magic-links)
* [SSO](/use-cases/sso)
* [OpenID Connect](/use-cases/oidc)
* [nOTP](/use-cases/notp)
* [One-Time Passwords](/use-cases/otp)
* [Authenticator Apps](/use-cases/totp-authenticator-apps)
* [Passwords](/use-cases/passwords)

Developers

* [Docs](https://docs.descope.com)
* [Tutorials](https://docs.descope.com/tutorials/)
* [Community](/community)
* [Open Source](/open-source)

Resources

* [Learning Center](/learn)
* [Blog](/blog)

Company

* [Our Story](/about)
* [Careers](https://job-boards.greenhouse.io/descope)
* [Partners](/partners)
* [Newsroom](/newsroom)
* [Security & Compliance](/security-compliance)
* [Contact Us](/contact)

Legal

* [Privacy Policy](/privacy)
* [Terms of Use](/terms)

Copyright © Descope Inc. All rights reserved.

[All systems operational](https://descopestatus.com)

[Github Icon Grey

![Github Icon Grey](https://images.ctfassets.net/xqb1f63q68s1/38EDaH0h3n6icUh9pVaWmK/ede2197e889712b167ff1f74620150a2/github-logo-grey.svg)](https://github.com/descope)[Linkedin Icon Grey

![Linkedin Icon Grey](https://images.ctfassets.net/xqb1f63q68s1/138nJ4hfyhdCYoOi4kPHKK/bbe644497f90fc02e5d047b7f18ab8f7/linkedin-icon-grey.svg)](https://www.linkedin.com/company/descope/)[X Grey Icon

![X Grey Icon](https://images.ctfassets.net/xqb1f63q68s1/6BBx4b59iu6VuN7KA90LpB/ebe40a377773978d9f3bb0c7ffb8dc3d/x-grey-icon.svg)](https://twitter.com/descopeinc)[Instagram Grey Logo

![Instagram Grey Logo](https://images.ctfassets.net/xqb1f63q68s1/2bbYuYDwqcoJgfzSfEgSlm/47682f9480c62d1fa9b7db26339db4b7/instagram-logo.svg)](https://www.instagram.com/descope.inc/)[Slack Icon

![Slack Icon](https://images.ctfassets.net/xqb1f63q68s1/4GLQKaTyCiD40QliZtucTD/9fcf12aef8fcd6ffcea361eadd055046/slack-logo.svg)](http://authtown.slack.com/)[YouTube Icon

![YouTube Icon](https://images.ctfassets.net/xqb1f63q68s1/3jstGU2pgP1hRDBsV3cx3/65d2a729b15e1101fcfaf893099f8ebf/youtube-logo.svg)](https://www.youtube.com/@descope)[Bluesky Social

![Bluesky Social](https://images.ctfassets.net/xqb1f63q68s1/4LWZXtvgGTc3wlCdrrlxGG/a35299779e03a896ca53e55eb8601239/Bluesky_Logo.svg)](https://bsky.app/profile/descope.com)

[Descope - Go to homepage](/)

[Chat with Sales](https://start-chat.com/slack/descope/V5mA8i)

Anonymously - no Slack account required

* Product
* App Use Cases
* Authentication Methods
* Developers
* Resources
* Company
* Legal

---

![G2 Users Love Us](https://images.ctfassets.net/xqb1f63q68s1/1TPXtSvPWcaJp65NJVlbIz/e71c60b6108453617aed120e5ad8323f/G2_Users_Love_Us.svg)[Leave a Descope review](https://www.g2.com/products/descope/reviews)

---

[Github Icon Grey

![Github Icon Grey](https://images.ctfassets.net/xqb1f63q68s1/38EDaH0h3n6icUh9pVaWmK/ede2197e889712b167ff1f74620150a2/github-logo-grey.svg)](https://github.com/descope)[Linkedin Icon Grey

![Linkedin Icon Grey](https://images.ctfassets.net/xqb1f63q68s1/138nJ4hfyhdCYoOi4kPHKK/bbe644497f90fc02e5d047b7f18ab8f7/linkedin-icon-grey.svg)](https://www.linkedin.com/company/descope/)[X Grey Icon

![X Grey Icon](https://images.ctfassets.net/xqb1f63q68s1/6BBx4b59iu6VuN7KA90LpB/ebe40a377773978d9f3bb0c7ffb8dc3d/x-grey-icon.svg)](https://twitter.com/descopeinc)[Instagram Grey Logo

![Instagram Grey Logo](https://images.ctfassets.net/xqb1f63q68s1/2bbYuYDwqcoJgfzSfEgSlm/47682f9480c62d1fa9b7db26339db4b7/instagram-logo.svg)](https://www.instagram.com/descope.inc/)[Slack Icon

![Slack Icon](https://images.ctfassets.net/xqb1f63q68s1/4GLQKaTyCiD40QliZtucTD/9fcf12aef8fcd6ffcea361eadd055046/slack-logo.svg)](http://authtown.slack.com/)[YouTube Icon

![YouTube Icon](https://images.ctfassets.net/xqb1f63q68s1/3jstGU2pgP1hRDBsV3cx3/65d2a729b15e1101fcfaf893099f8ebf/youtube-logo.svg)](https://www.youtube.com/@descope)[Bluesky Social

![Bluesky Social](https://images.ctfassets.net/xqb1f63q68s1/4LWZXtvgGTc3wlCdrrlxGG/a35299779e03a896ca53e55eb8601239/Bluesky_Logo.svg)](https://bsky.app/profile/descope.com)

---

[All systems operational](https://descopestatus.com)

Copyright © Descope Inc. All rights reserved.