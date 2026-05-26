> Source: https://developers.redhat.com/articles/2026/05/25/mcp-servers-vs-skills-choosing-right-context-your-ai

MCP servers vs. skills: Choosing the right context for your AI | Red Hat Developer


[Skip to main content](#main-content)

[![Redhat Developers  Logo](/themes/custom/rhdp_fe/images/branding/2023_RHDLogo_reverse.svg)](/)

* AI

  ### Get started with AI

  + [Red Hat AI](/products/red-hat-ai)

    Accelerate the development and deployment of enterprise AI solutions.
  + [AI learning hub](https://docs.redhat.com/en/learn/ai)

    Explore learning materials and tools, organized by task.
  + [AI interactive demos](https://www.redhat.com/en/interactive-experiences#ai-platform)

    Click through scenarios with Red Hat AI, including training LLMs and more.

  + [AI/ML learning paths](/learn/openshift-ai)

    Expand your OpenShift AI knowledge using these learning resources.
  + [AI quickstarts](https://docs.redhat.com/en/learn/ai-quickstarts)

    Focused AI use cases designed for fast deployment on Red Hat AI platforms.
  + [No-cost AI training](https://docs.redhat.com/en/ai-foundations)

    Foundational Red Hat AI training.

  ### Featured resources

  + [OpenShift AI learning](/learn/openshift-ai)
  + [Open source AI for developers](/e-books/open-source-ai-developers)
  + [AI product application development](https://www.redhat.com/en/technologies/all-products#artificial-intelligence)
  + [Open source-powered AI/ML for hybrid cloud](/topics/ai-ml)
  + [AI and Node.js cheat sheet](https://developers.redhat.com/cheat-sheets/ai-nodejs)

  ### Red Hat AI Factory with NVIDIA

  + Red Hat AI Factory with NVIDIA is a co-engineered, enterprise-grade AI solution for building, deploying, and managing AI at scale across hybrid cloud environments.
  + [Explore the solution](https://www.redhat.com/en/products/ai/factory-with-nvidia)
* Learn

  ### Self-guided

  + [Documentation](https://docs.redhat.com/en)

    Find answers, get step-by-step guidance, and learn how to use Red Hat products.
  + [Learning paths](/learn)

    Explore curated walkthroughs for common development tasks.
  + [Guided learning](http://docs.redhat.com/en/learn/guided-learning)

    Receive custom learning paths powered by our AI assistant.
  + [See all learning](/learn)

  ### Hands-on

  + [Developer Sandbox](/developer-sandbox)

    Spin up Red Hat's products and technologies without setup or configuration.
  + [Interactive labs](https://www.redhat.com/en/interactive-labs)

    Learn by doing in these hands-on, browser-based experiences.
  + [Interactive demos](https://www.redhat.com/en/interactive-experiences)

    Click through product features in these guided tours.

  ### Browse by topic

  + [AI/ML](https://developers.redhat.com/topics/ai-ml)
  + [Automation](https://developers.redhat.com/topics/automation)
  + [Java](/topics/java)
  + [Kubernetes](https://developers.redhat.com/topics/kubernetes)
  + [Linux](/topics/linux)
  + [See all topics](/topics)

  ### Training & certifications

  + [Courses and exams](https://www.redhat.com/en/services/training/all-courses-exams)
  + [Certifications](https://www.redhat.com/en/services/certifications)
  + [Skills assessments](https://www.redhat.com/en/services/skills-assessment)
  + [Red Hat Academy](https://www.redhat.com/en/services/training/red-hat-academy)
  + [Learning subscription](https://www.redhat.com/en/services/training/learning-subscription)
  + [Explore training](https://www.redhat.com/en/services/training-and-certification)
* Build

  ### Get started

  + [Red Hat build of Podman Desktop](/products/red-hat-build-podman-desktop)

    A downloadable, local development hub to experiment with our products and builds.
  + [Developer Sandbox](/developer-sandbox)

    Spin up Red Hat's products and technologies without setup or configuration.

  ### Download products

  + Access product downloads to start building and testing right away.
  + [Red Hat Enterprise Linux](/products/rhel/download)
  + [Red Hat AI](https://developers.redhat.com/products/red-hat-ai)
  + [Red Hat OpenShift](https://developers.redhat.com/products/openshift/download)
  + [Red Hat Ansible Automation Platform](/products/ansible/download)
  + [See all products](/products)

  ### Featured

  + [Red Hat build of OpenJDK](/products/openjdk)
  + [Red Hat JBoss Enterprise Application Platform](/products/eap)
  + [Red Hat OpenShift Dev Spaces](/products/openshift-dev-spaces)
  + [Red Hat Developer Toolset](/products/red-hat-developer-toolset/download)

  ### References

  + [E-books](/e-books)
  + [Documentation](https://docs.redhat.com/en)
  + [Cheat sheets](/cheat-sheets)
  + [Architecture center](https://www.redhat.com/architect/portfolio/)
* Community

  ### Get involved

  + [Events](/events)
  + [Live AI events](https://www.redhat.com/en/events/ai)
  + [Red Hat Summit](https://www.redhat.com/en/summit)
  + [Red Hat Accelerators](https://access.redhat.com/accelerators)
  + [Community discussions](https://access.redhat.com/discussions/)

  ### Follow along

  + [Articles & blogs](/blog)
  + [Developer newsletter](/newsletter)
  + [Videos](https://www.youtube.com/@RedHatDevelopers)
  + [Github](https://github.com/redhat-developer)

  ### Get help

  + [Customer service](https://www.redhat.com/en/contact/customer-service)
  + [Customer support](https://access.redhat.com/support)
  + [Regional contacts](https://access.redhat.com/support/contact)
  + [Find a partner](https://catalog.redhat.com/en/search?searchType=Partners)

  ### Join the Red Hat Developer program

  + Download Red Hat products and project builds, access support documentation, learning content, and more.
  + [Explore the benefits](/about)


Search


Search



 



All Red Hat

# MCP servers vs. skills: Choosing the right context for your AI

May 25, 2026

[Cedric Clyburn](/author/cedric-clyburn)

Related topics:
:   [Artificial intelligence](/topics/ai-ml)

Related products:
:   [Red Hat OpenShift AI](/products/red-hat-openshift-ai/overview)

Table of contents:

[Large language models](https://www.redhat.com/en/topics/ai/what-are-large-language-models) (LLMs) are efficient general-purpose tools, but they work *much* better when you give them the right context. Whether you're using a coding assistant (yes, [you can run your own private coding assistant](https://developers.redhat.com/articles/2026/04/22/opencode-model-neutral-ai-coding-assistant-openshift-dev-spaces)), building an agentic application, or trying to get more accurate answers from your favorite model, there are two main ways to extend what an LLM can do: Model Context Protocol (MCP**)** servers and skills.

Both expand the context window of your model, but they solve fundamentally different problems. This article explains what each option does, how they work technically, and how to choose between them—or use both.

## Why LLMs need context

An LLM is a prediction engine trained on massive datasets, and it can identify [the history of Red Hat](https://en.wikipedia.org/wiki/Red_Hat), determine which SQL command inspects a database schema, or write a [Dockerfile](https://www.redhat.com/en/topics/containers/what-is-docker). Most models are great at answering these types of general questions. However, getting the right answer for your specific use case requires providing the right context.  
  
Let's say, for example, you're asking a model for help working with your team's database. In addition to your question, the model will need relevant context. This might include the configuration your team uses for development or production environments, the formatting of queries to send, or a tool executed to check which tables are available. Providing this information used to be entirely manual: copy-pasting documentation, writing long and detailed prompts, and hoping the model understands your question and puts it all together correctly. The workflow shift from manual parsing to an automated context pipeline is illustrated in Figure 1.

[![A user query and context data feed into an LLM, alongside books, reports, and internet data, to yield a response.](/sites/default/files/styles/article_floated/public/figure-1_11.png?itok=PBthJzRx)](/sites/default/files/figure-1_11.png)


Figure 1: Context engineering supplies configuration, formatting rules, and tool output alongside a user's question to produce accurate responses.

This is where [context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) comes in. It goes beyond prompt engineering, which only provides instructions, personas, and basic guidelines. Context engineering is about curating the right data, tools, and instructions, so that the model has everything it needs to give you a correct, useful answer. So the question is, how do we provide that context?

## Connecting external data with the Model Context Protocol

Let's say the context your agent needs lives in an external service: a customer relationship management (CRM) solution, a database, or a cloud provider's API. Previously, with AI agents, you had to manually convert the service's API documentation into a custom tool with an authentication token, instruct the LLM to update the customer's contact info, and hope for the best.

[Model Context Protocol (MCP)](https://www.redhat.com/en/topics/ai/what-is-model-context-protocol-mcp) standardizes how your AI agent talks to external data sources. Instead of custom integrations for every tool, MCP provides a universal interface that:

* Abstracts service APIs into a [simple, LLM-ready format](https://modelcontextprotocol.io/docs/learn/server-concepts).
* Manages [authentication](https://modelcontextprotocol.io/docs/tutorials/security/authorization) by issuing your AI model a scoped access token with specific permissions (for example, read or write).
* Instructs the LLM to provide specific JSON to interact with the MCP server (for example, using `GET` to fetch a record or `POST` to submit an update).
* Defines the structured JSON inputs the LLM must produce to call tools on the MCP server.

This systemic separation of concerns between the agent, protocol, and external APIs is visualized in Figure 2.

[![Agent connects to LLM, and routes through MCP via JSON to a CRM using POST. Direct LLM-to-CRM access is crossed out.](/sites/default/files/styles/article_floated/public/figure-2_9.png?itok=8jCOQq5D)](/sites/default/files/figure-2_9.png)


Figure 2: MCP acts as a bridge between the agent and external services so the LLM can safely exchange JSON data without directly interacting with the API.​​​​​​​​​​​​​​​​

Behind the scenes, when you add an MCP server to your IDE or AI application, the agent client discovers available tools and appends descriptions to the model's context, signaling that it can view active Kubernetes resources. When the user makes a request, the model sees those tool descriptions alongside the conversation and decides which tools to call and with what arguments (Figure 3).

[![Four lifelines map out an MCP sequence across a user query, agent, CRM MCP server, and LLM during tool registration and client interaction phases.](/sites/default/files/styles/article_floated/public/figure-3_9.png?itok=QpkwQwwt)](/sites/default/files/figure-3_9.png)


Figure 3: This sequence diagram shows a full MCP interaction lifecycle where the agent registers available tools from the CRM MCP server, routes queries through the LLM, and returns a grounded answer.

[MCP was introduced by Anthropic in November 2024](https://www.anthropic.com/news/model-context-protocol) as an open standard and has since been widely adopted, with support from major AI tools and providers. In December 2025, Anthropic donated the protocol to the Linux Foundation through the [Agentic AI Foundation](https://aaif.io), which includes Red Hat as a member.

### Structure of an MCP server interaction

Here's a simplified example of what an MCP interaction looks like. Let's say your AI agent has a CRM MCP server configured to look up customer information, and the user requeststhe contact information for customer\_123. The LLM then generates the following JSON:

```
{
  "tool": "crm_get_contact",
  "parameters": {
    "customer_id": "cust_12345"
  }
}
```

This abstracts the LLM from the MCP server, which handles the actual API call, authentication, and response formatting. The LLM gets back structured data it can reason about. For a deeper look at how agentic AI uses MCP servers, check out the [MCP servers for Red Hat OpenShift AI](https://www.redhat.com/en/products/ai/openshift-ai/mcp-servers) and a guide on [Building effective AI agents with Model Context Protocol](https://developers.redhat.com/articles/2026/01/08/building-effective-ai-agents-mcp).

## Adding domain expertise with skills

While MCP solved the problem of “how do we give external data to an LLM,” there's another challenge: how do we give the LLM domain expertise it might not already have?

Sure, with MCP, you can pull those customer records from a CRM, but your sales team wants the output formatted exactly the same way every time: customer name, contact info, and their favorite cookie flavor (Figure 4). Without explicit instructions, the model will format things differently each time.

[![A customer data table showing structured name, contact, and cookie columns, with a note stating, "We need it like this, every time."](/sites/default/files/styles/article_floated/public/figure-4_9.png?itok=WQ43cOur)](/sites/default/files/figure-4_9.png)


Figure 4: Skills provide a consistent output format so the model returns data uniformly every time.

[Skills](https://agentskills.io/) are reusable, structured instructions that teach your LLM how to do something. Think about the tasks you might use an LLM for repeatedly:

* Cleaning up Excel documents in a specific format
* Debugging code (for example, always running `maven verify` before suggesting fixes)
* Running compliance checks against a standard template
* Formatting reports according to your team's style guide

Each of these can be packaged into a skill, which contains the following three parts:

* **Title:** How you and the model identify the capability
* **Description:** When the skill should be added to the model's context
* **The prompt:** Instructions, examples, templates, and scripts

The key feature of skills is [auto-loading](https://agentskills.io/skill-creation/best-practices). The underlying agent loads the relevant skill into its context window only when needed. A code debugger skill only activates when you ask about code errors. A document formatting skill only loads when you're working with documents. This keeps the context window efficient while providing specialized expertise on demand. With [the rising cost of LLMs](https://hyperdev.matsuoka.com/p/opus-46-vs-47-the-real-cost-of-incremental), this capability helps manage resource spending efficiently.

Skills have become a widely adopted pattern across AI tools. The [skill.md](https://agentskills.io/specification) format, popularized through coding assistants like Claude Code, has become a de facto standard across multiple platforms. You can find [community-maintained skill libraries](https://github.com/anthropics/skills) with thousands of entries covering everything from front-end design to Kubernetes deployment and data analysis.

### Anatomy of a skill definition

Here's a basic `skill.md` definition, pulled from [Claude Code's documentation](https://code.claude.com/docs/en/skills):

```
---
name: explain-code
description: Explains code with visual diagrams and analogies. Use when explaining how code works, teaching about a codebase, or when the user asks "how does this work?"
---
When explaining code, always include:
1. **Start with an analogy**: Compare the code to something from everyday life
2. **Draw a diagram**: Use ASCII art to show the flow, structure, or relationships
3. **Walk through the code**: Explain step-by-step what happens
4. **Highlight a gotcha**: What's a common mistake or misconception?
Keep explanations conversational. For complex concepts, use multiple analogies.
```

Once added to your AI coding assistant or AI agent, if a user asks, “How are we handling database queries in our development environment?” the skill auto-loads. The model then follows these standardized conventions automatically. In addition to the markdown file, you can include optional folders like `references`*,* `assets`, or`scripts` to provide context. The standard directory layout of a packaged skill is shown in Figure 5.

[![A directory tree showing a root folder named skill-name containing a Skill.MD file and subfolders for references, assets, and scripts.](/sites/default/files/styles/article_floated/public/figure-5_7.png?itok=cPDd8R5V)](/sites/default/files/figure-5_7.png)


Figure 5: Skills are composed of a folder containing a skill.md definition alongside optional folders for references, assets, and scripts.

## When to use MCP servers

Use MCP when your AI application needs access to real-time, external data in a controlled, tightly permissioned way. MCP is an integration layer between agents and tools. It lets you query what virtual machiness are currently running, determine the cluster state in your cloud provider, or request contact information for a customer.

MCP is the right choice when the value comes from the data itself, not from how the model processes it. The model needs to *read from* or *write to* an external system, and MCP provides a security-focused, standardized pipeline to do that.

## When to use skills

Setting up and configuring an MCP server can be overkill if you only need to add a reusable, custom capability to your AI. That's where skills shine.

Skills are lightweight and tell your model *how* to do something: for example, how to fetch investment data and analyze it using scripts or examples included in the skill. Use skills when you're repeating the same prompts across conversations, or need consistent output formatting across your team, or want to give domain-specific best practices to your model.

## Combining MCP and skills for comprehensive workflows

MCP and skills aren't competing approaches; they're complementary, and the most effective AI agents use both. Let's think about a scenario where you're building an AI agent for your DevOps team:

* **MCP** connects the agent to your Kubernetes cluster, your monitoring stack, and your incident management system. The agent can query pod status, pull metrics, and create incident tickets.
* A **skill** teaches the agent your team's incident response runbook: how to triage alerts, what thresholds matter, how to format a post-incident report, and which Slack channels to notify.

Without MCP, the agent cannot access your systems. Without the skill, the agent has access, but doesn't know your processes. Together, your agent can monitor active statuses and respond according to your team's processes.

## Next steps for your automation architecture

Both MCP and skills are open source capabilities widely adopted across AI environments. [Most providers offer an official MCP server](https://www.redhat.com/en/blog/it-automation-agentic-ai-introducing-mcp-server-red-hat-ansible-automation-platform), specific skills, or both. You can import these directly to your AI coding assistant or agent. Review the underlying code and execute these elements in sandboxed environments to verify behaviors safely.

## Related Posts

* ### [Building effective AI agents with Model Context Protocol (MCP)](/articles/2026/01/08/building-effective-ai-agents-mcp)
* ### [Leverage AI for root-cause analysis with MCP servers in VS Code and Cursor](/articles/2026/02/11/leverage-ai-root-cause-analysis-mcp-servers-vs-code-and-cursor)
* ### [How to set up an MCP server for Red Hat Lightspeed](/articles/2025/12/01/how-set-red-hat-lightspeed-model-context-protocol)
* ### [3 MCP servers you should be using (safely)](/articles/2025/11/04/3-mcp-servers-you-should-be-using)
* ### [How I built an agentic application for Docling with MCP](/articles/2025/08/20/how-i-built-agentic-application-docling-mcp)
* ### [How to build a simple agentic AI server with MCP](/articles/2025/08/12/how-build-simple-agentic-ai-server-mcp)

## Recent Posts

* ### [Testing infrastructure red teaming with abliterated models](/articles/2026/05/26/testing-infrastructure-red-teaming-abliterated-models)
* ### [Build an enterprise RAG system with OGX](/articles/2026/05/26/build-enterprise-rag-system-ogx)
* ### [Solutions for SELinux MCS challenges with GitLab runners](/articles/2026/05/26/solutions-selinux-mcs-challenges-gitlab-runners)
* ### [MCP servers vs. skills: Choosing the right context for your AI](/articles/2026/05/25/mcp-servers-vs-skills-choosing-right-context-your-ai)
* ### [How to route external and local LLMs with Models-as-a-Service](/articles/2026/05/25/route-external-and-local-llms-models-as-a-service)

## What’s up next?

![Open source AI for developers share image](/sites/default/files/styles/card_hero/public/Share%20graphics_Open%20source%20AI%20for%20developers%20copy.png?itok=WQLsed8y)

### [Open source AI for developers](/e-books/open-source-ai-developers "Open source AI for developers")

Red Hat

[![Red Hat Developers logo](/themes/custom/rhdp_fe/images/branding/2023_RHDLogo_reverse.svg)](/)

[LinkedIn](https://www.linkedin.com/showcase/red-hat-developer)

[YouTube](https://www.youtube.com/channel/UC7noUdfWp-ukXUlAsJnSm-Q)

[Twitter](https://twitter.com/rhdevelopers)

[Facebook](https://www.facebook.com/redhat)

### Platforms

* [Red Hat AI](/products/red-hat-ai)
* [Red Hat Enterprise Linux](https://developers.redhat.com/products/rhel/overview)
* [Red Hat OpenShift](https://developers.redhat.com/products/openshift/overview)
* [Red Hat Ansible Automation Platform](https://developers.redhat.com/products/ansible/overview)
* [See all products](/products)

### Build

* [Developer Sandbox](https://developers.redhat.com/developer-sandbox)
* [Developer tools](/topics/developer-tools)
* [Interactive tutorials](https://developers.redhat.com/learn#assembly-id-70181)
* [API catalog](https://developers.redhat.com/api-catalog/)

### Quicklinks

* [Learning resources](/learn)
* [E-books](/e-books)
* [Cheat sheets](/cheat-sheets)
* [Blog](/blog)
* [Events](/events)
* [Newsletter](/newsletter)

### Communicate

* [About us](https://developers.redhat.com/about)
* [Contact sales](https://developers.redhat.com/contact-sales)
* [Find a partner](https://catalog.redhat.com/partners/)
* [Report a website issue](/report_a_website_issue)
* [Site status dashboard](https://status.redhat.com/)
* [Report a security problem](https://access.redhat.com/security/team/contact/)

### RED HAT DEVELOPER

Build here. Go anywhere.

We serve the builders. The problem solvers who create careers with code.

Join us if you’re a developer, software engineer, web designer, front-end designer, UX designer, computer scientist, architect, tester, product manager, project manager or team lead.

[Sign me up](/register "Create a Red Hat Developer account")



### Red Hat legal and privacy links

* [About Red Hat](https://redhat.com/en/about/company)
* [Jobs](https://redhat.com/en/jobs)
* [Events](https://redhat.com/en/events)
* [Locations](https://redhat.com/en/about/office-locations)
* [Contact Red Hat](https://redhat.com/en/contact)
* [Red Hat Blog](https://redhat.com/en/blog)
* [Inclusion at Red Hat](https://www.redhat.com/en/about/our-culture/diversity-equity-inclusion)
* [Cool Stuff Store](https://coolstuff.redhat.com/)
* [Red Hat Summit](https://www.redhat.com/en/summit)

© 2026 Red Hat

### Red Hat legal and privacy links

* [Privacy statement](https://redhat.com/en/about/privacy-policy)
* [Terms of use](https://redhat.com/en/about/terms-use)
* [All policies and guidelines](https://redhat.com/en/about/all-policies-guidelines)
* [Digital accessibility](https://redhat.com/en/about/digital-accessibility)

Ask AI (Beta)


### Chat Support

Please log in with your Red Hat account to access chat support.

Log In with Red Hat SSO