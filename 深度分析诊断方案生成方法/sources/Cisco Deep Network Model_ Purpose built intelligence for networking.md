> Source: https://blogs.cisco.com/ai/cisco-deep-network-model-overview

Cisco Deep Network Model: Purpose built intelligence for networking - Cisco Blogs



[Skip to content](#content)



[![Cisco Logo](https://blogs.cisco.com/wp-content/themes/ciscowordpress-child/svg/cisco_logo.svg)](https://blogs.cisco.com)

[Cisco Blogs](https://blogs.cisco.com)



[Executive Platform](https://blogs.cisco.com/news)

[AI](https://blogs.cisco.com/ai)

[Networking](https://blogs.cisco.com/networking)

[Data Center](https://blogs.cisco.com/datacenter)

[Security](https://blogs.cisco.com/security)

More 

* [All Industries](/industries)
* [All Countries + Regions](/country-region)
* [Cisco Insider](https://blogs.cisco.com/insidervoices)
* [Cisco on Cisco](https://blogs.cisco.com/cisco-on-cisco)
* [CX](/customerexperience)
* [Developer](https://blogs.cisco.com/developer)
* [High Tech Policy](https://blogs.cisco.com/gov)
* [Industrial IoT](https://blogs.cisco.com/industrial-iot)
* [Innovation](https://blogs.cisco.com/innovation)
* [Learn with Cisco](https://blogs.cisco.com/learning)
* [Our Corporate Purpose](https://blogs.cisco.com/our-corporate-purpose)
* [Partner](https://blogs.cisco.com/partner)
* [SP360: Service Provider](https://blogs.cisco.com/sp)
* [SMB: Small and Medium Business](https://blogs.cisco.com/smb)
* [We Are Cisco](https://blogs.cisco.com/wearecisco)
* [Subscribe to Cisco Blogs](https://app.feedpress.com/e/mailverify?feed_id=CiscoBlogs)

Menu



Search

Search

Voice Search is currently unavailable

Powered by Google Web Speech API

We didn't hear that. Try again.

When autocomplete results are available use up and down arrows to review and enter to select

* [Downloads](https://software.cisco.com/download/navigator.html)
* [Certifications](https://www.cisco.com/site/us/en/learn/training-certifications/index.html)
* [Design Guides](https://www.cisco.com/c/en/us/solutions/design-zone.html)
* [Training](https://learninglocator.cloudapps.cisco.com/#/home)
* [Community](https://community.cisco.com/)
* [Careers](https://www.cisco.com/c/en/us/about/careers.html)



![](https://blogs.cisco.com/wp-content/themes/ciscowordpress-child/svg/search_background.svg)

# Cisco Blogs

[Cisco Blogs](https://blogs.cisco.com/) / [Artificial Intelligence - AI](https://blogs.cisco.com/ai) / Cisco Deep Network Model: Purpose built intelligence for networking

February 5, 2026 [Leave a Comment](https://blogs.cisco.com/ai/cisco-deep-network-model-overview#respond)


---

![Avatar](https://blogs.cisco.com/gcs/ciscoblogs/1/2026/02/IL20260205002801-pukamal-150x150.png)
![Avatar](https://blogs.cisco.com/gcs/ciscoblogs/1/2025/11/IL20251104215547-vmanna-150x150.png)

[##### Artificial Intelligence - AI](https://blogs.cisco.com/ai)

# Cisco Deep Network Model: Purpose built intelligence for networking

6 min read

[Vincent Manna](https://blogs.cisco.com/author/vmanna "Posts by Vincent Manna"), [Puneet Kamal](https://blogs.cisco.com/author/pukamal "Posts by Puneet Kamal")

*This blog was written in collaboration with Yuqing Gao, Jian Tan, Fan Bu, Ali Dabir, Hamid Amini, Doosan Jung, Yury Sokolov, Lei Jin, and Derek Engi.*  
  
LLMs can sound very convincing, but in network operations, sounding right isn’t enough.

Network operations are dominated by structured telemetry, long configuration states, time series at scale, and investigations that sprawl across devices, sites, and domains. The practical constraint is not whether an AI model can answer a networking question in isolation. It’s whether the AI system can reason over real operational data, understand the context of your network and business, preserve the details that change outcomes, and remain reliable across multi-turn interactions—including troubleshooting.

That establishes a clear requirement for technical and business decision makers: if you want AI to support network operations, it must be engineered for networking data and networking workflows, not adapted after the fact.

The Cisco Deep Network Model is fine-tuned and trained for that reality. It is a networking-specialized model designed to reason like an experienced operator. In deployment, it can be paired with Analytics Context Engineering (ACE) and Lightweight Autonomous Program Synthesis and Execution (LAPSE), two model-agnostic innovations that scale context and machine-data handling. Together, they support operator-grade reasoning at enterprise scale, delivering faster, responses grounded in evidence with context preserved across turns so investigations don’t degrade into truncation, looping, or guesswork.   
  
After reading this post, you’ll scroll away knowing **(1)** what the Cisco Deep Network Model is, **(2)** why general-purpose models struggle in network operations, and **(3)** the two breakthroughs that make it practical at scale: ACE and LAPSE.

## **Off the shelf LLMs don’t hold up in networking workflows**

General-purpose models are strong at summarization, conversation, and broad knowledge retrieval. Network operations stress a different set of constraints.

**The data does not fit.** Even routine investigations involve long time-series windows, lots of counters, packet loss and latency across locations, big config sections, and logs from many devices. Off-the-shelf models hit context limits fast, then start dropping information or relying on shortcuts.

**Mixed data gets mangled.**  Networking work is rarely just text. It is telemetry, JSON, syslog, CLI output, config snippets, and ticket context together. Even with massive context windows, many frontier models are optimized for human language, not machine data, so they can lose track of the exact timestamp, interface, policy, or metric change that makes the root cause obvious.

The Cisco Deep Network Model starts with a different assumption: don’t force the model to read everything. Instead, build a system that can handle machine data at scale, preserve investigative context without bloat, and move through troubleshooting like an expert would.

## **So, what is the Cisco Deep Network Model?**

The Cisco Deep Network Model is a purpose-built model for networking, designed to support troubleshooting, configuration, and automation with higher precision than general-purpose models. The intent is not to create a better chatbot. The intent is to create a model that behaves like a seasoned network operator: grounded in evidence, disciplined in troubleshooting, and able to converge on root cause and remediation with clear traceability.

Benchmark results for the Cisco Deep Network model reflect this specialization. On a CCIE-style multiple choice benchmark**, Cisco’s model outperforms general-purpose models by up-to-20 percent.**

![](//blogs.cisco.com/wp-content/plugins/a3-lazy-load/assets/images/lazy_placeholder.gif)

At first glance, some of these differences may appear incremental. In practice, they are not. Once a model surpasses roughly 85 percent, the remaining errors tend to concentrate in rare, complex edge cases rather than common patterns. Improving performance at that level requires addressing the long tail of networking scenarios that general-purpose models often miss.

An analogy is useful here: each additional point beyond that threshold is comparable to an elite athlete shaving fractions of a second off a world record. The effort increases sharply because the work shifts from broad capability improvements to resolving the hardest, least frequent cases. This is where domain-specific training, expert vetting, and operational grounding make a meaningful difference.

## **Trusted training and continuous learning**

The model is built on a foundation of Cisco U courseware and CCIE-level knowledge representing more than 40 years of operational insight. The model has been trained on nearly 100 million tokens, and Cisco experts have contributed thousands of reasoning traces, meticulously annotating and validating each layer of logic so the model learns not just the answer, but the operator-grade path to get there.

Networks also evolve continuously, and the Cisco Deep Network Model is designed to evolve with them. Through reinforcement learning, it adapts using new data and non-public, real-world Technical Assistance Center (TAC) and Customer Experience (CX) insights only available within Cisco, so the model improves as operational patterns, software, and environments change.

## **Optimizing LLM performance for machine data: ACE and LAPSE**

The Cisco Deep Network Model is more than a trained model. It is delivered as a system that combines domain reasoning with context management and machine-data execution—built to overcome the two constraints that break most deployments: **(1)** context scale and **(2)** machine data scale.

### **Analytics Context Engineering (ACE)**

![](//blogs.cisco.com/wp-content/plugins/a3-lazy-load/assets/images/lazy_placeholder.gif)![](https://blogs.cisco.com/gcs/ciscoblogs/1/2026/02/AceFigure-768x353.png)

ACE transforms a dense prompt into compact canonical views and reconstructs it using the fewest possible tokens. The goal is not summarization that discards detail. The goal is to reduce the number of tokens the LLM has to process without losing what matters, so it can maintain context across data-heavy, multi-turn investigations and keep the working prompt within the model’s context window. Practically, this means normalizing mixed inputs such as telemetry summaries, log excerpts, config deltas, and ticket notes into a consistent investigation record that stays usable over time.

This matters because investigations naturally snowball. Every turn adds repeated history, partial artifacts, mixed-format evidence, and competing hypotheses. Over time, even a correct model can become less reliable because the input becomes less usable. ACE is designed to keep the investigation compact, stable, and faithful to the underlying evidence.

Cisco reports that ACE can reduce prompt size by roughly 20 to 90 percent while preserving the information the model needs to stay accurate. Off-the-shelf approaches typically manage only about 0 to 30 percent reduction before critical details start to drop. In practical terms, this is what keeps multi-turn work consistent rather than fragile. 

[*Want the technical details behind Analytics Context Engineering? This blog goes deeper.*](https://blogs.cisco.com/ai/analytics-context-engineering-for-llm)

### **Lightweight Autonomous Program Synthesis and Execution (LAPSE)**

![](//blogs.cisco.com/wp-content/plugins/a3-lazy-load/assets/images/lazy_placeholder.gif)![](https://blogs.cisco.com/gcs/ciscoblogs/1/2026/02/LAPSE-768x277.png)

LAPSE takes a different approach to scale. When the input is large machine data, the system performs on-demand tool creation and execution to transform data from a source schema into a target schema optimized for the task. The model receives task-ready outputs rather than raw telemetry dumps, which keeps the workflow fast and reduces the risk of missing critical signals.

This is a pragmatic design choice. Time series and high-volume telemetry are better handled by tools that aggregate, filter, reshape, and compute. The model should guide what needs to be computed and how to interpret it, not act as the compute engine itself.

LAPSE enables the model to handle practically unlimited machine data, by accelerating machine data processing for interactive operational tasks, turning raw telemetry into structured, task-ready. Reported comparisons show roughly 3–5 seconds of latency (vs. 27–200 seconds for off-the-shelf solutions) for tasks such as machine-data schema transformation. Reported transformation accuracy is near 100% (vs. 0–70%).

The point for decision makers is straightforward. This is the difference between an AI system that can keep up with an operator and one that turns every investigation into a waiting game.

## **How it works in practice**

ACE and LAPSE are complementary by design.

* LAPSE handles the heavy lift of machine data transformation quickly and deterministically.
* ACE keeps the investigation state compact, stable, and usable across multi-turn work.

Together, they enable a workflow that is difficult for generic systems to sustain: **(1)** start with intent, **(2)** pull the minimum relevant evidence, **(3)** maintain a consistent record of what is known, and **(4)** produce outputs that are fast enough and grounded enough to trust in production.

The model also supports a “next best action” troubleshooting loop so investigations progress like expert work: hypothesis, evidence, refinement, and convergence on root cause.

## **Brought to life in Cisco products**

It is brought to life through Cisco AI products that operators use day to day. In Cisco AI Canvas, it helps teams investigate across domains with a coherent evidence record, generate structured outputs from large telemetry, and move from suspicion to validated root cause faster. In [Cisco AI Assistant](https://www.cisco.com/site/us/en/solutions/artificial-intelligence/ai-assistant/) experiences, it turns natural-language intent into operator-grade reasoning and actionable next steps, grounded in the telemetry and context available to the user.

## **What’s actually different**

Many vendors claim AI for networking. The Cisco Deep Network Model differentiates on specific operational properties.

1. Purpose-built training and expert vetting for networking accuracy
2. Engineering for machine data scale through Lightweight Autonomous Program Synthesis and Execution
3. Lossless context optimization for long investigations through Analytics Context Engineering
4. A roadmap to adaptive troubleshooting through the Next Best Action (NBA) loop.

**For technical leaders**, this is about correctness, auditability, and reliability at production scale. **For business leaders**, it is about faster convergence on root cause, fewer dead ends, and a more credible foundation for agentic operations that can execute with discipline instead of guesswork.

## Authors

[![Avatar](https://blogs.cisco.com/gcs/ciscoblogs/1/2025/11/IL20251104215547-vmanna-150x150.png)](https://blogs.cisco.com/author/vmanna)

### [Vincent Manna](https://blogs.cisco.com/author/vmanna)

#### Senior Product Marketing Manager, AI Canvas

#### AI Software & Platform

[![share on facebook](https://blogs.cisco.com/wp-content/themes/ciscowordpress-child/svg/share_li_navy.svg)](http://www.linkedin.com/in/vincentmanna)

[![Avatar](https://blogs.cisco.com/gcs/ciscoblogs/1/2026/02/IL20260205002801-pukamal-150x150.png)](https://blogs.cisco.com/author/pukamal)

### [Puneet Kamal](https://blogs.cisco.com/author/pukamal)

#### Leader, Product Management

#### AI Software & Platform

[![share on facebook](https://blogs.cisco.com/wp-content/themes/ciscowordpress-child/svg/share_li_navy.svg)](https://linkedin.com/in/puneetkamal)

Tags: [AI Canvas](https://blogs.cisco.com/tag/ai-canvas) [AI Security](https://blogs.cisco.com/tag/ai-security-2) [Artificial Intelligence (AI)](https://blogs.cisco.com/tag/artificial-intelligence) [Cisco Deep Network Model](https://blogs.cisco.com/tag/cisco-deep-network-model) 

---

[![share on twitter](https://blogs.cisco.com/wp-content/plugins/cisco-text-to-speech//images/twitter-gray-tts.svg) X/Twitter](https://twitter.com/intent/tweet?url=https://blogs.cisco.com/ai/cisco-deep-network-model-overview&text=Cisco Deep Network Model: Purpose built intelligence for networking&via=Cisco)

[![share on facebook](https://blogs.cisco.com/wp-content/plugins/cisco-text-to-speech//images/facebook-gray-tts.svg)Facebook](http://www.facebook.com/sharer/sharer.php?u=https://blogs.cisco.com/ai/cisco-deep-network-model-overview&title=Cisco Deep Network Model: Purpose built intelligence for networking)

[![share on linkedin](https://blogs.cisco.com/wp-content/plugins/cisco-text-to-speech//images/linkedin-gray-tts.svg) LinkedIn](https://www.linkedin.com/cws/share?url=https://blogs.cisco.com/ai/cisco-deep-network-model-overview)

[![](https://blogs.cisco.com/wp-content/plugins/cisco-text-to-speech//images/email-gray-tts.svg) E-mail](mailto:?subject=Cisco Blog: Cisco Deep Network Model: Purpose built intelligence for networking&body=I saw this post on Cisco Blogs and thought you might like to read it.%0A%0ACisco Deep Network Model: Purpose built intelligence for networking%0A%0Ahttps://blogs.cisco.com/ai/cisco-deep-network-model-overview%0A%0A****Disclaimer****%0A%0ACisco is not responsible for the content of this email, and its contents do not necessarily reflect Cisco’s views or opinions. Cisco has not verified the email address or name of the sender.)

![](https://blogs.cisco.com/wp-content/plugins/cisco-text-to-speech//images/voice.svg)Read aloud
![](https://blogs.cisco.com/wp-content/plugins/cisco-text-to-speech//images/share.svg) Share 

x

< PrevPlayNext >PauseStopSettings

x

Rate

1

Pitch

1

Select a voice:

Voices are browser-dependent.  
Tip: Chrome provides the most options.

Google US English (en-US)
Microsoft David - English (United States) (en-US) -- DEFAULTMicrosoft Mark - English (United States) (en-US)
Microsoft Zira - English (United States) (en-US)

Reset
Save

Quick Links

* [About Cisco](http://www.cisco.com/c/en/us/about.html)
* [Contact Us](http://www.cisco.com/c/en/us/about/contact-cisco.html)
* [Careers](http://www.cisco.com/c/en/us/about/careers.html)
* [Connect with a partner](https://www.cisco.com/site/us/en/partners/connect-with-a-partner/index.html?ccid=cc000864&dtid=odiprc001129)

Resources and Legal

* [Feedback](https://ciscocx.qualtrics.com/jfe/form/SV_bwrmeoKrBHYxOyW?Ref=/c/en/us/index.html)
* [Help](https://www.cisco.com/c/en/us/about/help.html)
* [Terms & Conditions](https://www.cisco.com/c/en/us/about/legal/terms-conditions.html)
* [Privacy](https://www.cisco.com/c/en/us/about/legal/privacy-full.html)
* [Cookies / Do not sell or share my personal data](https://www.cisco.com/c/en/us/about/legal/privacy-full.html#cookies)
* [Accessibility](https://www.cisco.com/c/en/us/about/accessibility.html)
* [Trademarks](https://www.cisco.com/c/en/us/about/legal/trademarks.html)
* [Supply Chain Transparency](https://www.cisco.com/c/dam/en_us/about/supply-chain/cisco-modern-slavery-statement.pdf)
* [Newsroom](https://newsroom.cisco.com/c/r/newsroom/en/us/index.html)
* [Sitemap](https://www.cisco.com/c/en/us/about/sitemap.html)

©2026 Cisco Systems, Inc.