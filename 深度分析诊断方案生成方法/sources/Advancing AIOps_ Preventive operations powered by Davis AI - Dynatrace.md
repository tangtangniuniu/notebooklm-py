> Source: https://www.dynatrace.com/news/blog/advancing-aiops-preventive-operations-powered-by-davis-ai/

Preventive operations powered by Davis AI































































![Header background](https://dt-cdn.net/images/half-wave-1920-53e1c04e4a.jpg)

# Advancing AIOps: Preventive operations powered by Davis AI

Published 
February 4, 2025
Updated 
September 23, 2025
 8 min read

[![Christian Kiesewetter](https://news.cdn.dm.dynatrace.com/wp-content/uploads/2022/10/christian-kiesewetter-120x120.jpg)](https://www.dynatrace.com/news/blog/author/christian-kiesewetter/)

[Christian Kiesewetter](https://www.dynatrace.com/news/blog/author/christian-kiesewetter/)

[Product news](https://www.dynatrace.com/news/category/product-news/) [AIOps](https://www.dynatrace.com/news/category/aiops/) [Observability](https://www.dynatrace.com/news/category/observability/)

### In this blog post

1. [1.Automatic root cause detection](#automatic-root-cause-detection)
2. [2.Problem journey and reactive remediation](#problem-journey-and-reactive-remediation)
3. [3.Automating the remediation](#automating-the-remediation)
4. [4.Preventive operations](#preventive-operations)
5. [5.Summary](#summary)

The 2024 CrowdStrike incident demonstrated our societal vulnerabilities to IT outages. A faulty software update caused widespread issues, impacting critical services globally, including airlines, banks, hospitals, and public safety systems. Despite recent advancements such as containers, Kubernetes, and platform engineering, it’s evident that managing enterprise software services has become increasingly complex. IT operations must be prepared to quickly address and mitigate disruptions, ensuring business continuity and minimizing damage.

AI, especially [AIOps](/news/blog/what-is-aiops-2/), has emerged as a pivotal solution, promising to avoid downtime. The 2024 State of AI Report highlights this trend, with 89% of technology leaders anticipating that AI will significantly enhance incident response by learning to automate and optimize various tasks, such as performance monitoring and workload scheduling.

![Blue screens of death at LGA airport due to the July 2024 CrowdStrike outage. (Source: Wikimedia Commons.)](https://news.cdn.dm.dynatrace.com/wp-content/uploads/2025/02/CrowdStrike_BSOD_at_LGA.jpg)

Figure 1. Blue screens of death at LGA airport due to the July 2024 CrowdStrike outage. (Source: Wikimedia Commons.)

AIOps can identify and address potential issues before they become major incidents by learning from history and analyzing large amounts of data in real time. This approach improves operational efficiency and resilience, though it’s not without flaws. The complexity of IT environments and the changing nature of threats necessitate human oversight and ongoing adjustment of AIOps systems to handle unforeseen challenges and ensure optimal performance. Additionally, predictions based on historical data are reactive, solely relying on past information to anticipate future events, and can’t prevent all new or emerging issues. This limitation highlights the importance of continuous innovation and adaptation in IT operations and AIOps strategies.

> “The shift from reactive to preventive operations represents the next evolution in AIOps.”  
> Bernd Greifeneder, CTO Dynatrace

When Dynatrace set out with Davis® AI over 10 years ago, pioneering AI-driven operations, we focused initially on problem identification before moving on to problem remediation. The next milestone in enhancing the capabilities of Davis AI—another pioneering step forward in AI-driven operations—is outright problem prevention. In this blog post, we explain how the unique combination of causal, predictive, and generative AI—augmented by the latest Davis AI advancements—is transforming how Dynatrace customers manage and optimize their IT infrastructure.

## Automatic root cause detection

Modern, complex, and distributed environments generate a substantial number of events. This necessitates additional requirements such as minimizing the total number of issues, eliminating false positives, and conducting accurate root cause analysis.

Dynatrace has a longstanding reputation for accurately analyzing root causes and identifying related events. While other methods typically rely on mere correlation and historical data analysis, we’ve further enhanced our capabilities by implementing causational analysis, which leverages contextual information automatically gathered during data ingestion and processing in addition to historical data analysis. This is achieved using [Dynatrace Grail™](/platform/grail/), our causational data lakehouse, which unifies all data in an always-up-to-date topology model. By applying causal AI to incoming data in real time, Davis instantly learns and continuously adapts to new information. This facilitates more precise root cause analysis and anomaly detection, including identifying seasonal anomalies and establishing auto-adaptive thresholds.

![Root cause analysis with the Problems app](https://news.cdn.dm.dynatrace.com/wp-content/uploads/2025/02/Identify-Root-Cause-with-Davis-AI.png)

Figure 2. Root cause analysis with the Problems app

When applying this Davis root cause detection within our own IT environment, Davis effectively **filters out over 99.9% of incoming data noise**, condensing hundreds of thousands of daily system events into no more than four or five incidents that require attention from our IT operations team.

These algorithms are not limited to monitoring IT environments. At our [February 2025 Dynatrace Perform session on exploratory analytics with AI-driven insights](/perform/on-demand/perform-2025/?session=power-exploratory-analytics-with-ai-driven-insights), the Performance Engineering Lead of XXXLutz—one of the world’s largest furniture retailers operating more than 370 stores across Europe—explains how XXXLutz utilizes Davis AI to proactively identify critical order drops, allowing them to respond quickly and effectively to changing market conditions and ensuring that their business remains agile and responsive to the needs of their customers.

## Problem journey and reactive remediation

At the core of Dynatrace problem remediation stands the [Problems app](/news/blog/transform-your-operations-with-davis-ai-root-cause-analysis/)—an optimized view into opinionated insights, details, and context of each detected issue—for Operations, SREs, and developers. It filters billions of log lines, including the topology of each incident and its affected entities, for efficient problem triaging and troubleshooting, resulting in a **56% faster mean time to repair (MTTR)** for critical incidents.

With the latest release, we drive this further by improving the automatic connection of relevant log and trace data for further drill down, presenting the full context of an issue in a single view. This provides comprehensive visibility into even complex architectures, simplifying the process of examining relevant details and addressing code-level issues, **reducing 100 clicks and manual filtering to a single click with no loss of context**.

![Comparative analysis of multiple problems with Davis CoPilot](https://news.cdn.dm.dynatrace.com/wp-content/uploads/2025/02/Comparative-Analysis.png)

Figure 3. Comparative analysis of multiple problems with Davis CoPilot

By utilizing Davis CoPilot™, you can conduct comparative analyses of multiple issues, obtain natural language summaries of individual problems, and receive contextual recommendations along with specific remediation steps.

You can also link troubleshooting guides created in [Notebooks](/hub/detail/notebooks/) to remediated issues, thereby building an intelligent knowledge base. Davis automatically connects additional documents as well as stored [workflows](/hub/detail/automations/). So the next time a similar problem arises, Davis brings up related guides, enabling teams to learn from previous experiences and reducing the risk of knowledge loss.

![Harness your collective knowledge by connecting troubleshooting guides](https://news.cdn.dm.dynatrace.com/wp-content/uploads/2025/02/troubleshooting-guides.png)

Figure 4. Harness your collective knowledge by connecting troubleshooting guides

Please refer to our recent blog posts for more information on [utilizing Problems for AI-driven insights](/news/blog/powerful-exploratory-analytics-for-ai-driven-insights/) and [the latest Davis CoPilot advancements.](/news/blog/davis-copilot-expands-get-answers-and-insights-across-the-dynatrace-platform/)

## Automating the remediation

While obtaining comprehensive insights is beneficial, true transformation occurs through the use of tools that automatically execute remediation steps. To implement these “AI-driven operations,” it’s essential to forecast future requirements, including capacity demands, potential system failures, and security incidents.

Traditional forecasting engines typically depend on historical data, stored in metrics. In contrast, Davis AI generates real-time predictions, facilitating proactive operations. This capability is due to Davis’s ability to process raw data, such as logs, for forecasting, leveraging Grail to execute previously unattainable queries.

Consider the following scenario: You begin by retrieving and analyzing logs to identify relevant values for automation. Once this task is complete, you proceed to your pipelining tool to configure ingestion rules that extract these values into metrics and then wait several weeks for your prediction engine to generate alerts that can serve as triggers for your workflows.

However, when utilizing Dynatrace with its integrated anomaly detection and forecasting capabilities, you gain the advantage of schema-less data analysis and the ability to process any raw data into time series in real time. This significantly reduces the time required to establish AIOps workflows **from several weeks to less than 30 minutes**.

## Preventive operations

The complexity of modern software environments makes it challenging to determine a service’s reliability solely through testing. It’s impractical to emulate scenarios such as generating a million tickets to assess performance capabilities. This necessitates real-time insights and operations rather than reactive problem-solving or raising alerts to notify personnel.

Preventive operations address this need by enabling proactive corrective actions before issues arise, akin to predictive maintenance. AI-supported anomaly detection identifies parameters that deviate from the norm, allowing for automatic configuration adjustment to mitigate potential problems preemptively.

![Dynatrace offers the only unified, AI-powered platform for all data, all teams, and all possibilities.](https://news.cdn.dm.dynatrace.com/wp-content/uploads/2025/02/Davis-Overview-scaled.jpg)

Figure 5. Dynatrace offers the only unified, AI-powered platform for all data, all teams, and all possibilities.

Davis CoPilot combines the “power of three”:

* Davis **causal AI** for identifying anomalies and root cause analysis
* Davis **predictive AI** for precise forecasting and determining when to take action
* **Generative AI** capabilities that perform actions beyond simply sending notifications or restarting services

In this way, Dynatrace extends AIOps beyond traditional IT operations tasks and addresses complex scenarios, including security use cases such as threat observability. Consider the following real-world example:

At Dynatrace, we log all failed login attempts. We can predict potential threats when abnormal patterns are identified and raise a security event by utilizing seasonal baselining. The subsequent workflow involves checking the IP address and generating a threat score. Upon reaching a certain threshold, a new ruleset is automatically added to the web application firewall. This entire process is fully automated, running before a problem even occurs, significantly reducing the response **time from over an hour to a fraction of a second**.

In another instance, automatic log pattern analysis crawling our application logs decreased the number of bugs in the production environment by 15% and **freed up time previously spent on log analysis and triaging (in pre-prod), equivalent to 17 full-time employees**. Consequently, these 17 developers can now dedicate their efforts to adding more value to Dynatrace.

## Summary

The State of AI report states that over 88% of technology leaders anticipate AI will enhance incident responses and **improve their teams’ ability to predict and proactively resolve** **service-affecting issues.**

With Dynatrace, organizations are prepared to evolve their ITOps and SRE departments from troubleshooting to prevention, getting proactive with forecasting, and utilizing generative AI instead of purely focusing on history-focused root cause analysis.

Start your preventive operations journey with smart automation and auto-remediation that prevents larger issues.

### Are you interested in gaining more insights?

* Read about [recent advancements in our Problems app](/news/blog/powerful-exploratory-analytics-for-ai-driven-insights/)
* [Get insights into Davis root cause analysis](/news/blog/transform-your-operations-with-davis-ai-root-cause-analysis/)
* Learn more about [how Davis CoPilot helps you be more productive](/news/blog/davis-copilot-expands-get-answers-and-insights-across-the-dynatrace-platform/)
* Or [dig deeper into how to utilize Davis forecasting capabilities within Dashboards](/news/blog/better-dashboarding-with-dynatrace-davis-ai/)

### Share blog post

### Stay Updated

Enter your email

* All updates
* Blog posts
* Product news

Subscribe now

**Tags:** 
[AI](https://www.dynatrace.com/news/tag/ai/), [AI Observability](https://www.dynatrace.com/news/tag/ai-observability/), [AIOps](https://www.dynatrace.com/news/tag/aiops/), [Davis AI](https://www.dynatrace.com/news/tag/davis-ai/), [Davis CoPilot](https://www.dynatrace.com/news/tag/davis-copilot/), [Dynatrace](https://www.dynatrace.com/news/tag/dynatrace/), [Perform 2025](https://www.dynatrace.com/news/tag/perform-2025/), [problem analysis](https://www.dynatrace.com/news/tag/problem-analysis/), [problems](https://www.dynatrace.com/news/tag/problems/), [root cause](https://www.dynatrace.com/news/tag/root-cause/), [troubleshooting](https://www.dynatrace.com/news/tag/troubleshooting/)

[![Christian Kiesewetter](https://news.cdn.dm.dynatrace.com/wp-content/uploads/2022/10/christian-kiesewetter-150x150.jpg)](/news/blog/author/christian-kiesewetter/)

[Christian Kiesewetter](/news/blog/author/christian-kiesewetter/)

The Author

Christian is a Principal Product Manager, focusing on Go-to-Market topics for the Dynatrace core platform. He connects the dots between business and strategy on the one side and product and development on the other. Previously, he managed international teams and was responsible for delivering SaaS products from their core idea to market-ready solutions. Christian combines technical expertise with a track record in sales, marketing, and business development and is - as an innovator - always curious about developing new things and ideas that add value to the journey of our customers.

Disclaimer: The views expressed on this blog are my own and do not reflect the views of Dynatrace LLC or its affiliates.

You may also like

[![](https://news.cdn.dm.dynatrace.com/wp-content/uploads/2026/04/Blog__OTP_0192__high_res_version-300x169.webp)

## How to build trust in Digital Experience Monitoring

By Miriam Derenbach -

May 8, 2026

Read now](https://www.dynatrace.com/news/blog/how-to-build-trust-in-digital-experience-monitoring/)
[![Dynatrace SaaS Release Notes](https://news.cdn.dm.dynatrace.com/wp-content/uploads/2023/04/SaaS_Release_notes_3-300x169.png)

## What’s new in Dynatrace SaaS version 1.338

By Malcolm Davidson -

May 5, 2026

Read now](https://www.dynatrace.com/news/blog/whats-new-in-dynatrace-saas-version-1-338/)
[![](https://news.cdn.dm.dynatrace.com/wp-content/uploads/2026/04/header_release_radar-2-300x169.png)

## Dynatrace Release Radar 03.26

By Michael Winkler -

April 30, 2026

Read now](https://www.dynatrace.com/news/blog/dynatrace-release-radar-03-26/)

![Section background](https://dt-cdn.net/images/full-wave-cta-1500-c11df5539d.jpg)

Perform 2026

Watch every boundary-breaking session and product announcement on-demand.

[Watch On-demand](/perform/on-demand/perform-2026/)