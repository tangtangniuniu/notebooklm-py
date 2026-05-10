> Source: https://developers.redhat.com/articles/2026/01/08/building-effective-ai-agents-mcp

Building effective AI agents with Model Context Protocol (MCP) | Red Hat Developer


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

# Building effective AI agents with Model Context Protocol (MCP)

January 8, 2026

[Cedric Clyburn](/author/cedric-clyburn)


[Peter Double](/author/peter-double)


[Addie Stevens](/author/addie-stevens)

Related topics:
:   [Artificial intelligence](/topics/ai-ml)

Related products:
:   [Red Hat AI](/taxonomy/term/37288)[Red Hat OpenShift AI](/products/red-hat-openshift-ai/overview)

Table of contents:

Large language models can generate impressive language, but [they still struggle to operate effectively within enterprise systems](https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/). To make these models useful, you need more than good prompts. You need a reliable way for models to find the right context, call the right tools, follow enterprise policies, and leave an auditable record of their actions.

The [Model Context Protocol (MCP)](https://www.redhat.com/en/topics/ai/what-is-model-context-protocol-mcp) offers that foundation. MCP standardizes how models discover, select, and call tools (Figure 1). This helps developers move from simple chatbots to reliable, active applications without reinventing every integration from scratch.

![Figure 1](/sites/default/files/figure1_32.png)

Figure 1: Model Context Protocol provides a standard for calling tools, services, and more from an AI application.

## The evolution of interacting with LLMs

Early LLM applications were simple. You asked a question and [the model responded based on the data it was trained on](https://developers.redhat.com/articles/2025/11/04/post-training-methods-language-models) (Figure 2). If you typed "What is Red Hat?", the model searched its internal parameters for an answer drawn from the public internet. These responses reflected the model provider's training set, not your organization's unique knowledge.

![Figure 2](/sites/default/files/figure_2_8.png)

Figure 2: Typical interactions with an LLM answering solely based on its training data.

That limitation quickly became obvious. Enterprise data—from design documents and Jira tickets to meeting transcripts and product wikis—lived outside the model's reach. Without that context, responses were generic and often incomplete. Developers began exploring ways to bring private knowledge into the model's reasoning process and context window (the amount of information it can "see" at once).

### Chatting with your documents: RAG as a first step

The first major breakthrough was [retrieval-augmented generation (RAG)](https://www.redhat.com/en/topics/ai/what-is-retrieval-augmented-generation). RAG connects models to vector or graph databases so they can perform semantic search and retrieve information relevant to a query.

Imagine asking, "How do I create a data science project in Red Hat OpenShift AI?" A RAG pipeline searches internal documentation, retrieves the top results, and passes them into the model's context window. The model then generates a precise, grounded answer.

Figure 3 shows this pipeline in action. By supplementing what the model already knows with external knowledge, [RAG makes answers much more accurate and up-to-date](https://developers.redhat.com/articles/2024/12/04/level-your-generative-ai-llms-and-rag). Still, it requires constant retrieval, even for simple requests that do not need additional context. As models gained reasoning ability, it became clear that they should decide when to fetch data and even when to act.

![Figure 3](/sites/default/files/figure3_27.png)

Figure 3: Enterprise and unique data typically isnt known by LLMs. That's where a RAG Pipeline can fetch data relevant to a user's question for a more grounded, accurate result.

### Beyond RAG: The rise of agentic AI

This shift gave rise to tool calling, where an LLM does not just read information but performs actions through APIs. Instead of just searching a document store, a model can now [access external services to retrieve or modify data](https://developers.redhat.com/blog/2024/12/03/chatbot-i-choose-you-call-function#). For example, when a user asks "What is the weather today?", the model can call the AccuWeather API to fetch the current forecast, interpret the response, and return a clear summary. In the same way, it might open a pull request in GitHub or check the health of a Kubernetes cluster and post a summary of any issues to Slack.

Figure 4 illustrates this evolution. It shows how the model identifies available tools, selects the right one for the task, and performs the action. The LLM becomes context-aware, understanding both the question and the systems it can interact with. This marks the transition from simple text generation to [agentic AI](https://www.redhat.com/en/topics/ai/what-is-agentic-ai), systems that can reason, plan, and act on behalf of the user.

![Figure 4](/sites/default/files/figure_4_7.png)

Figure 4: Agentic AI really just means AI systems that can take action. Models reason what decision need to be taken, then use custom instructions to call an API or service.

However, this new flexibility introduced new challenges. Every organization implemented tool calling differently, writing custom code for each integration. This resulted in duplication, fragmentation, and a lack of shared standards. MCP addresses these issues by defining one consistent way for models to communicate with tools.

## Introducing the Model Context Protocol (MCP)

MCP defines a clear way for models to call external tools. Instead of hard-coding logic for every service, you register an MCP server that exposes an interface the model can understand.

A client, typically an LLM or an application using one, sends a standardized request. The server executes the action against a system like GitHub, Slack, or Kubernetes. (These systems already have public servers available for use). The MCP layer coordinates communication between them. See Figure 5.

![Figure 5](/sites/default/files/figure5_16.png)

Figure 5: Instead of each team building their own unique communication protocol between the LLM and various APIs, Model Context Protocol is a standard for clear, defined integration.

Think of MCP as a common language for model-to-tool interaction, much like TCP standardized network communication. [Anthropic introduced the protocol in late 2024](https://www.anthropic.com/news/model-context-protocol), and the ecosystem has expanded rapidly since then. There are now [tens of thousands of community-built MCP servers](https://github.com/punkpeye/awesome-mcp-servers) that connect to data storage systems, communication platforms, productivity apps, and infrastructure tools. Clients such as Claude Desktop, ChatGPT, and many open source applications can register these servers and call them directly.

## Making MCP enterprise-ready

The promise of MCP is clear, but for large companies to use it, they need more than just compatibility. They need trust, governance, and control.

Enterprises need to verify that the right people and models can call the right tools with the right permissions. They must track [which MCP servers are running, what versions they use, and what actions they perform](https://www.redhat.com/en/blog/introducing-ai-hub-and-genai-studio-new-command-center-enterprise-generative-ai-red-hat-openshift-ai). They need [automated scanning, signing, and certification to confirm that each server is secure and compliant](https://www.redhat.com/en/blog/model-context-protocol-mcp-understanding-security-risks-and-controls). They must also be able to observe and audit tool calls in real time.

These needs shape Red Hat's approach to MCP within Red Hat OpenShift AI. Red Hat is extending the platform to include built-in identity and access management through role-based access control (RBAC) and OAuth, lifecycle and metadata management for every MCP server, and enhanced observability as a core capability. With these controls in place, MCP becomes more useful, safe, and ready for production environments.

## MCP on Red Hat AI

[OpenShift AI 3 adds MCP support directly to the platform](https://www.redhat.com/en/products/ai/openshift-ai/mcp-servers), giving AI engineers a fast way to connect models to tools. A guided creation flow walks users through spinning up an MCP server, containerizing it, and deploying it safely.

Once deployed, the [Playground](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.0/html-single/experimenting_with_models_in_the_gen_ai_playground/index) (Figure 6) allows teams to experiment safely. They can run a server alongside a model, observe its behavior, and fine-tune it before moving to production. Approved MCP servers then appear in the **AI Assets** listing, a centralized catalog where engineers can discover, reuse, and extend trusted integrations.

![Figure 6](/sites/default/files/figure6_14.png)

Figure 6: OpenShift AI's asset playground allows teams to select, stage, and deploy MCP Servers.

Because this capability integrates with [Llama Stack](https://www.redhat.com/en/blog/llama-stack-and-case-open-run-anywhere-contract-agents), models can invoke MCP tools easily during inference. The result is an environment designed for instant experimentation today and certified, governed usage tomorrow.

### Red Hat's end-to-end MCP lifecycle

Red Hat's vision for MCP in OpenShift AI extends beyond experimentation. It includes a complete lifecycle for developing, certifying, and running MCP servers.

Everything begins with the registry, a secure staging area where new servers are scanned, quarantined if needed, and enriched with metadata. After they are validated, servers move into the catalog, a curated set of certified integrations available to all AI engineers within the organization.

Lifecycle management ensures that each server is tracked and versioned. Updates are scanned and signed automatically, while deprecated versions are retired safely. At runtime, the MCP gateway ties it all together. It enforces policy and RBAC rules, applies rate limits and logging, and provides consistent observability for every request.

Together, these components make MCP predictable and governable at scale.

## A quick demo of Model Context Protocol

To see MCP in action, check out the following video demonstration. Through a chat interface ([Goose](https://block.github.io/goose/) in this example), the model connects to both [OpenShift](https://github.com/containers/kubernetes-mcp-server) and Slack MCP servers. It retrieves system information, detects anomalies, and posts updates to Slack.

See how inference and tool calling work together to power real-time agentic applications with various enterprise systems.

## The road ahead for MCP in OpenShift AI

In the near term, OpenShift AI 3.0 and future versions will add more support. MCP will appear in the AI Assets catalog and Playground to simplify experimentation (Figure 7). Red Hat will also onboard partner and ISV MCP servers for early access while previewing the full MCP registry, catalog, and gateway stack. Each release will add richer metadata for certification status, security scans, and maturity levels.

![Figure 7](/sites/default/files/figure7_13.png)

Figure 7: The Playground, where teams can experiment with MCP servers in a sandboxed environment.

Beyond that, Red Hat is building a longer-term vision for MCP-as-a-Service (MCPaaS), a managed layer for hosting, observing, and auditing MCP servers centrally. The AI Hub will unify models, agents, guardrails, and MCP servers as composable AI assets. The OpenShift DevHub plug-in will show developers which servers they can use directly within their workspace, and MCP for AI Coders will provide access in [Red Hat OpenShift Dev Spaces](https://developers.redhat.com/products/openshift-dev-spaces/overview) or local environments.

Red Hat product teams are also developing their own MCP servers for OpenShift, [Red Hat Ansible Automation Platform](https://developers.redhat.com/products/ansible/overview), [Red Hat Enterprise Linux](https://developers.redhat.com/products/rhel/overview), and [Red Hat Lightspeed](https://www.redhat.com/en/lightspeed), enabling new combinations of infrastructure automation and intelligent behavior. As these servers mature, developers will be able to orchestrate complex workflows such as a model coordinating updates across clusters or [triggering an Ansible playbook entirely through MCP](https://www.redhat.com/en/blog/red-hat-lightspeed-2025-observability-actionable-automation).

## Building the future of agentic AI

As you've learned about the brief history of LLM application design, MCP is a major shift in how we connect our AI models to existing systems. It lets developers build models that act with context, enforce policy, and integrate safely into enterprise environments.

By enabling Model Context Protocol into OpenShift AI, Red Hat is giving teams a complete foundation for agentic AI, one where experimentation, governance, and scalability coexist. Developers can test an MCP server in the Playground, publish it to the catalog, and deploy it with confidence.

As the ecosystem grows, expect MCP to become as fundamental to AI development as containers are to cloud infrastructure, a standard layer that makes intelligent automation predictable, secure, and reusable.

*Last updated:
January 13, 2026*

## Related Posts

* ### [Your AI agents, evolved: Modernize Llama Stack agents by migrating to the Responses API](/articles/2025/12/09/your-ai-agents-evolved-modernize-llama-stack-agents-migrating-responses-api)
* ### [Using AI agents with Red Hat Lightspeed](/articles/2025/10/13/using-ai-agents-red-hat-insights)
* ### [Why some agentic AI developers are moving code from Python to Rust](/articles/2025/09/15/why-some-agentic-ai-developers-are-moving-code-python-rust)
* ### [Your agent, your rules: A deep dive into the Responses API with Llama Stack](/articles/2025/08/20/your-agent-your-rules-deep-dive-responses-api-llama-stack)
* ### [How I built an agentic application for Docling with MCP](/articles/2025/08/20/how-i-built-agentic-application-docling-mcp)
* ### [How to build a simple agentic AI server with MCP](/articles/2025/08/12/how-build-simple-agentic-ai-server-mcp)

## Recent Posts

* ### [Federated identity across the hybrid cloud using zero trust workload identity manager](/articles/2026/05/08/federated-identity-across-hybrid-cloud-using-zero-trust-workload-identity)
* ### [Confidential virtual machine storage attack scenarios](/articles/2026/05/07/confidential-virtual-machine-storage-attack-scenarios)
* ### [Introducing virtualization platform autopilot](/articles/2026/05/07/introducing-virtualization-platform-autopilot)
* ### [Integrate zero trust workload identity manager with Red Hat OpenShift GitOps](/articles/2026/05/07/integrate-zero-trust-workload-identity-manager-red-hat-openshift-gitops)
* ### [Best Practice Configuration and Tuning for Linux and Windows VMs](/blog/2026/05/06/best-practice-configuration-and-tuning-linux-and-windows-vms)

## What’s up next?

Read **Applied AI for Enterprise Java Development**, a practical guide for Java developers to integrate generative AI and machine learning using familiar enterprise tools.

[Get the e-book](https://developers.redhat.com/e-books/applied-ai-enterprise-java-development)

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