> Source: https://thenextweb.com/news/google-cloud-next-ai-agents-agentic-era

Google Cloud Next 2026: AI agents, A2A protocol, Workspace Studio, and the full-stack bet against OpenAI and Anthropic





[Skip to content](#main)

Toggle Navigation

* [News](/)
* Events
  + [TNW Conference
    June 19 & 20, 2025](/conference)
  + [All events](/events)
* [Spaces](/spaces)
* [Programs](/programs)

---

* [Newsletters](/newsletters)
* [Partner with us](/partnerships)

* [Jobs](https://thenextweb.homerun.co/)
* [Contact](/cdn-cgi/l/email-protection#2e4d4140484b5c4b404d4b6e5a464b404b565a594b4c004d4143)

News
[news
news
news](/)

* [Latest](/latest)
* [Deep tech](/deep-tech)
* [Sustainability](/sustainability)
* [Ecosystems](/ecosystems)
* [Data and security](/data-security)
* [Fintech and ecommerce](/fintech-ecommerce)
* [Future of work](/future-of-work)
* [Conference media hub](https://thenextweb.com/topic/tnw-conference)
* More
  + [Startups and technology](/startups-technology)
  + [Investors and funding](/investors-funding)
  + [Government and policy](/government-policy)
  + [Corporates and innovation](/corporates-innovation)
  + [Podcast](https://fast.wistia.com/embed/channel/hckmzyzq7e)

* [Corporates and innovation](/corporates-innovation)

# Google just launched its agentic enterprise play, and it runs from chip to inbox

  

April 22, 2026 - 2:26 pm

![Google just launched its agentic enterprise play, and it runs from chip to inbox](https://media.thenextweb.com/2026/04/google-cloud-next-ai-agents-agentic-era.avif)

*Summary: Google rebranded and consolidated its AI platform at Cloud Next 2026, renaming Vertex AI to the Gemini Enterprise Agent Platform and absorbing Agentspace into a unified Gemini Enterprise product. The announcements include Workspace Studio (no-code agent builder), 200+ models in the Model Garden including Anthropic Claude, partner agents from Box, Workday, Salesforce, and ServiceNow, ADK v1.0 stable releases across four languages, Project Mariner (web-browsing agent), managed MCP servers with Apigee as an API-to-agent bridge, and A2A protocol v1.0 in production at 150 organisations. Kurian framed the strategy as owning the full stack from chip to inbox while competitors “hand you the pieces, not the platform.”*

Google used the opening keynote of Cloud Next 2026 on Tuesday to unveil what amounts to a full rebranding and consolidation of its AI platform around agents. Vertex AI is now the Gemini Enterprise Agent Platform. Google Agentspace, the employee-facing AI assistant, has been absorbed into a unified product called Gemini Enterprise. The announcements span a no-code agent builder for Google Workspace, a redesigned developer platform with more than 200 models including third-party options such as Anthropic’s Claude, a web-browsing agent called Project Mariner, managed MCP servers across Google Cloud services, and the production-grade Agent2Agent protocol for cross-platform agent communication. Thomas Kurian, Google Cloud’s chief executive, titled the keynote “The Agentic Cloud” and drew a deliberate contrast with competitors: other vendors, he said, are “handing you the pieces, not the platform,” leaving teams to integrate components themselves.

The timing is deliberate. OpenAI’s Operator is scoring 87% on complex browser task benchmarks and the company has recruited Cognizant and CGI to push its Codex coding agent into enterprise software shops, with enterprise revenue now accounting for 40% of OpenAI’s total. Anthropic has launched a marketplace for Claude-powered enterprise tools and its Model Context Protocol has reached 10,000 servers and 97 million monthly SDK downloads. Google is fighting from third position in cloud market share, behind AWS and Microsoft Azure, but exited the fourth quarter of 2025 with the fastest growth rate of the three at 50% year on year, and is betting that vertical integration, owning the model, the runtime, the silicon, and the distribution channel through Workspace, gives it an advantage neither competitor can replicate.

## The agent stack

![](https://media.thenextweb.com/hardfork-2018/uploads/visuals/tnw-newsletter.png)

![](https://media.thenextweb.com/hardfork-2018/uploads/visuals/tnw-newsletter.png)

The 💜 of EU tech

The latest rumblings from the EU tech scene, a story from our wise ol' founder Boris, and some questionable AI art. It's free, every week, in your inbox. Sign up now!

Google Workspace Studio is the most consumer-facing announcement. It is a no-code platform that lets business users build and deploy AI agents across Gmail, Docs, Sheets, Drive, Meet, and Chat by describing automations in plain language. A user can type “every Friday, ping me to update my tracker” and Gemini creates the automation. Workspace Studio connects to third-party applications including Asana, Jira, Mailchimp, and Salesforce, and can call external APIs via webhooks or run custom logic through Apps Script. It is rolling out to Google Workspace business, enterprise, and education customers.

The developer-facing platform, now called the Gemini Enterprise Agent Platform, received deeper upgrades. Agent Designer, a visual flow canvas for building agent workflows, is in preview. Agent Engine Sessions and Memory Bank, which give agents persistent context across interactions, are generally available. A new Agent Garden provides prebuilt agent solutions for customer service, data analysis, and creative tasks. A free tier via Express mode lowers the entry barrier. The Model Garden now hosts more than 200 models spanning Google’s own Gemini and Gemma families, third-party models including Anthropic Claude, and open models such as Llama. Google also announced six new agents for data engineering and coding in BigQuery, including a data engineering agent that automates pipeline creation from natural language prompts and a code interpreter that translates queries into executable Python with visualisations. Partner agents from Box, Workday, Salesforce, ServiceNow, Dun and Bradstreet, and S&P Global are integrated into the platform, giving enterprise customers prebuilt capabilities for document intelligence, HR self-service, IT operations, and financial data.

Project Mariner, Google DeepMind’s web-browsing agent powered by Gemini 2.0, scores 83.5% on the WebVoyager benchmark and handles ten concurrent tasks on cloud-based virtual machines. It automates shopping, information retrieval, and form-filling, and is available to Google AI Ultra subscribers in the United States. The roadmap includes a visual builder called Mariner Studio in the second quarter, cross-device synchronisation in the third quarter, and an agent marketplace in the fourth quarter.

## The protocol play

The most strategically significant announcement may be the least visible to end users. Google’s [Agent2Agent (A2A) protocol](https://thenextweb.com/news/stop-talking-to-ai-let-them-talk-to-each-other-the-a2a-protocol), originally launched with more than 50 technology partners, has reached 150 organisations in production, not pilot, routing real tasks between agents built on different platforms. The protocol is now governed by the Linux Foundation’s Agentic AI Foundation and has reached version 1.2, with signed agent cards using cryptographic signatures for domain verification. Microsoft, AWS, Salesforce, SAP, and ServiceNow are running A2A in production environments.

A2A is designed to complement rather than compete with Anthropic’s [Model Context Protocol (MCP)](https://thenextweb.com/news/rise-of-model-context-protocol-in-the-agentic-era). MCP handles how an agent connects to tools and data sources. A2A handles how agents communicate with each other across organisational and platform boundaries. Google adopted MCP across its own services in December 2025, launching fully managed remote MCP servers for Google Maps, BigQuery, Compute Engine, and Kubernetes Engine, with Cloud Run, Cloud Storage, AlloyDB, Cloud SQL, Spanner, Looker, and Pub/Sub on the roadmap. Apigee, Google’s API management platform, now functions as an MCP bridge, translating any standard API into a discoverable agent tool with existing security and governance controls. Google is simultaneously positioning A2A as the standard for the layer above: the orchestration of multiple agents from multiple vendors working together on a single task.

The practical implication is that a Salesforce agent built on Agentforce can hand off a task to a Google agent running on Vertex AI, which can query a ServiceNow agent for IT asset data, all through A2A without any of the three systems needing to understand each other’s internal architecture. Native A2A support is now built into Google’s Agent Development Kit, LangGraph, CrewAI, LlamaIndex Agents, Semantic Kernel, and AutoGen. Google’s open-source Agent Development Kit reached stable v1.0 releases across Python, Go, and Java, with TypeScript support also available. It is a code-first framework optimised for Gemini but model-agnostic and deployable to any container or Kubernetes environment. The security layer includes Model Armor for defence against indirect prompt injection, zero-trust architecture applied to decentralised agent systems, and access management through Google Cloud IAM with audit logging.

## The competitive landscape

[OpenAI’s own enterprise agent push](https://thenextweb.com/news/openai-codex-enterprise-partners-cognizant-cgi) through Codex and systems integrator partnerships has reached three million weekly users. [Anthropic’s enterprise marketplace](https://thenextweb.com/news/anthropic-marketplace-claude-enterprise-software) for Claude-powered tools is building an ecosystem through partners including Snowflake. Microsoft’s Copilot is embedded in virtually every Fortune 500 company. AWS has Bedrock with its own agents framework maturing rapidly. The enterprise AI agent market is not a two-horse race. It is a five-way contest in which each competitor has a structural advantage the others lack.

OpenAI has the strongest consumer brand and the most advanced reasoning models. Anthropic has the most trusted safety positioning and the fastest-growing enterprise revenue. Microsoft has the deepest enterprise distribution through Office and Azure. AWS has the largest cloud infrastructure base and the strongest developer gravity. Google’s argument is that it is the only company that owns all four layers of the stack: the custom silicon (Ironwood TPUs), the frontier models (Gemini), the cloud platform (now unified as the Gemini Enterprise Agent Platform), and the enterprise distribution channel (Workspace with more than three billion users across Google’s productivity tools). Kurian framed the strategy explicitly: “If you want to adopt a technology successfully, you need to pick a few important projects and do them well, rather than spraying on a lot of little projects.” No other competitor controls the full vertical from chip to application.

Google’s own AI Agent Trends report, published ahead of the conference, found that 89% of business teams are already using AI agents and the average organisation runs 12. The most common enterprise use cases are customer service at 49%, marketing at 46%, security operations at 46%, and IT support at 45%. Early customer deployments suggest the productivity claims are not purely theoretical: Danfoss, the Danish industrial manufacturer, automated 80% of transactional decisions in email-based order processing using Google’s agents, reducing response times from 42 hours to near real-time. Suzano, a Brazilian pulp and paper company, built an agent with Gemini Pro that translates natural language into SQL queries, cutting query time by 95% for 50,000 employees.

## The model foundation

The agents run on Google’s Gemini model family, with the Gemini 2.5 generation being retired in October in favour of the 3.x line. Gemini 3 Pro and Gemini 3 Flash, released in late 2025 and iterated through early 2026, provide the reasoning backbone. Gemini 3 Flash delivers a 15% improvement in overall accuracy over Gemini 2.5 Flash and is optimised for high-frequency agentic workflows and real-time processing. Gemini 3.1 Pro, the most advanced reasoning variant, is available in preview. A new experimental model, GLM 5, targets complex systems engineering and long-horizon agentic tasks through the Model Garden. Gemini 3.2 is expected to be formally announced during the conference, with an expanded context window beyond one million tokens and optimised parameter counts for reduced inference latency. Demis Hassabis, DeepMind’s chief executive, stated in January that his team is “focusing on Gemini 4 this year.” Google also recently launched [Gemma 4 open models](https://thenextweb.com/news/google-gemma-4-open-models-apache-2-launch) under Apache 2.0 licensing, built from the same research as Gemini 3 and providing an open-weight alternative for enterprise customers who need to run models on their own infrastructure.

The infrastructure beneath the models is equally central to the pitch. Ironwood, Google’s seventh-generation TPU announced the same day, delivers 4.6 petaFLOPS per chip and scales to 9,216-chip superpods producing 42.5 exaFLOPS. Anthropic has committed to up to one million Ironwood units. The custom silicon means Google can offer inference at costs that customers buying Nvidia GPUs at retail cannot match, which in a market where inference is the dominant and growing expense, translates directly into pricing power for the agent services that run on top.

Google Cloud holds roughly 11% of the cloud infrastructure market. AWS holds 31%. Azure holds 25%. The gap is significant and Cloud Next will not close it. But the agentic era, if it materialises at the scale Google is projecting, reshuffles the competitive dynamics in ways that favour a company with a vertically integrated stack over companies that assemble their AI capabilities from multiple vendors. Google is betting that the enterprise customer who adopts AI agents at scale will choose the platform where the model, the runtime, the silicon, the governance, and the productivity suite are all built by the same company and optimised to work together. It is a large bet. Cloud Next 2026 is where Google is asking enterprises to take it.

[![Alina Maria Stan](https://media.thenextweb.com/2025/12/Alina-Maria-Stan.avif)](/author/alina)

## Story by [Alina Maria Stan](/author/alina)

Alina Maria Stan builds connections that people actually feel. As co-founder and COO of Tekpon, she turns product intuition into real moment
(show all)

Alina Maria Stan builds connections that people actually feel. As co-founder and COO of Tekpon, she turns product intuition into real moments of discovery, shaping how teams find and adopt SaaS every day. Since 2020, she has led Tekpon’s brand voice, media strategy, and growth plays with a clear focus on human outcomes behind every metric.
Before Tekpon, Alina followed curiosity across industries and countries. She was CEO of King Casino Bonus and led affiliate and brand strategy at Extremoo Media and Fable Media in Denmark, where she learned how to build partnerships that last. Early on, she sharpened her CRM and pricing instincts at K.H. ApS, always asking why customers choose what they choose.
Her approach is rooted in more than a decade of international experience and two master’s degrees, one in Sustainable Consumption from the Technical University of Munich and one in Consumer Affairs Management from Aarhus University.

## Get the TNW newsletter

Get the most important tech news in your inbox each week.

Published April 22, 2026 - 2:26 pm UTC

[Back to top](#)

[![Alina Maria Stan](https://media.thenextweb.com/2025/12/Alina-Maria-Stan.avif)
Story by
Alina Maria Stan](/author/alina)


## Popular articles

1. 1

   ### [Meta missed mobile. It is building the operating system for humanoids](/news/meta-acquires-assured-robot-intelligence-humanoid)
2. 2

   ### [Nebius paid $643 million for 20 people because inference is where the money is](/news/nebius-eigen-ai-inference-optimization)
3. 3

   ### [OpenAI called the growth report clickbait. The market disagreed by tens of billions of dollars.](/news/openai-growth-fears-firing-all-cylinders)
4. 4

   ### [Amazon tried selling office software and failed. Now it is betting that office software itself is obsolete.](/news/amazon-tried-selling-office-software-and-failed-now-it-is-betting-that-office-software-itself-is-obsolete)
5. 5

   ### [OpenAI’s models are now available everywhere. The question is whether everywhere is enough.](/news/amazon-aws-openai-models-microsoft-exclusivity-ends)

## Related Articles

[![Hospital websites are still leaking patient data to advertisers, four years after the warnings](https://media.thenextweb.com/2026/05/Data-leaking.avif)](/news/hospital-website-trackers-patient-data-leakage)


data security

### [Hospital websites are still leaking patient data to advertisers, four years after the warnings](/news/hospital-website-trackers-patient-data-leakage)

[![Brussels reissues its Huawei warning, six years on, and prepares to make it stick](https://media.thenextweb.com/2026/05/European-Commision.avif)](/news/eu-huawei-zte-connectivity-infrastructure-recommendation)


eu

### [Brussels reissues its Huawei warning, six years on, and prepares to make it stick](/news/eu-huawei-zte-connectivity-infrastructure-recommendation)

[![Discover TNW All Access](https://media.thenextweb.com/hardfork-2018/uploads/visuals/Conference-Nebula.png)](https://thenextweb.com/conference)


### Discover TNW All Access

Watch videos of our inspiring Talks for free
[Sign up now](https://thenextweb.com/auth/tnw/login-required)

[![OpenAI closes The Deployment Company, a $10bn enterprise AI bet on private equity](https://media.thenextweb.com/2026/04/OpenAI.avif)](/news/openai-deployco-finalized-10-billion-joint-venture)


openai

### [OpenAI closes The Deployment Company, a $10bn enterprise AI bet on private equity](/news/openai-deployco-finalized-10-billion-joint-venture)

[![Europe’s finance chiefs want Mythos access to defend their banks. Washington has so far said no.](https://media.thenextweb.com/2024/09/Untitled-design-40.avif)](/news/eurogroup-mythos-access-cyber-defense-europe)


eu

### [Europe’s finance chiefs want Mythos access to defend their banks. Washington has so far said no.](/news/eurogroup-mythos-access-cyber-defense-europe)

The heart of tech

  

## More TNW

* [Media](/latest)
* [Events](/events)
* [Spaces](/spaces)
* [Newsletters](/newsletters)

## About TNW

* [Partner with us](/partnerships)
* [Terms & Conditions](/terms-and-conditions)
* [Cookie Statement](/cookie-statement)
* [Privacy Statement](/privacy-statement )

A Tekpon Company

Copyright © 2006—2026, Cogneve, INC. Made with <3 in Amsterdam.