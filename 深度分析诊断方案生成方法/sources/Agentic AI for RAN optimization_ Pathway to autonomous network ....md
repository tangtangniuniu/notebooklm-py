> Source: https://aws.amazon.com/blogs/industries/agentic-ai-for-ran-optimization-pathway-to-autonomous-network-level-5/

Agentic AI for RAN optimization: Pathway to autonomous network level 5 | AWS for Industries


 [Skip to Main Content](#aws-page-content-main)


* Filter: All



* English
* [Contact us](https://aws.amazon.com/contact-us/?nc2=h_ut_cu)
* [AWS Marketplace](https://aws.amazon.com/marketplace/?nc2=h_utmp)
* Support
* My account

* Search

  Filter: All
* [Sign in to console](https://console.aws.amazon.com/console/home/?nc2=h_si&src=header-signin)
* [Create account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_su&src=header_signup)

AWS Blogs

* [Home](https://aws.amazon.com/blogs/)
* Blogs
* Editions

## [AWS for Industries](https://aws.amazon.com/blogs/industries/)

# Agentic AI for RAN optimization: Pathway to autonomous network level 5

by Christian Finelli, Ali Sharaf, Billion Lo, and Manuel Sierra Marco on 28 JUL 2025 in [Amazon Bedrock](https://aws.amazon.com/blogs/industries/category/artificial-intelligence/amazon-machine-learning/amazon-bedrock/ "View all posts in Amazon Bedrock"), [Industries](https://aws.amazon.com/blogs/industries/category/industries/ "View all posts in Industries"), [Telecommunications](https://aws.amazon.com/blogs/industries/category/industries/telecommunications/ "View all posts in Telecommunications") [Permalink](https://aws.amazon.com/blogs/industries/agentic-ai-for-ran-optimization-pathway-to-autonomous-network-level-5/)  [Comments](https://aws.amazon.com/blogs/industries/agentic-ai-for-ran-optimization-pathway-to-autonomous-network-level-5/#Comments)   [Share](#)

### Introduction

In today’s rapidly evolving telecommunications landscape, the management and optimization of Radio Access Networks (RANs) has become extraordinarily complex. As networks roll out 5G, traditional approaches to network management are proving increasingly inadequate. The sheer volume of data, the intricate interdependencies between network elements, and the demanding requirements for real-time optimization demand an innovative approach.

The challenges of modern network operators are multifaceted. They must maintain optimal network performance, deliver high-quality service, manage resource efficiency, adapt to rapidly changing usage patterns and keep operational costs under control. Even with basic automation traditional tools and methodologies, struggle to meet these demands effectively.

Autonomous networks, as defined by the TM Forum (TMF), represent a progression toward self-managing network systems. The highest maturity stages are level 4 (full autonomy under human oversight) and level 5 (full end-to-end autonomy without human intervention). These levels enable networks to use AI-driven insights to adapt, optimize, and self-repair themselves in real time. Achieving these levels is essential for communication service providers (CSPs) to manage the complexity and scale of modern networks efficiently. Without such automation, operational costs can become unsustainable, making high-level autonomy critical for both economic and competitive network operations.

Ericsson is leading the network management transformation with an extensive rApps (RAN Intelligent Controller non-real-time applications) portfolio. rApps are essential for TMF Level 5 (full autonomy) network automation because they embed AI/ML‑powered, policy‑driven intelligence directly in RAN, allowing closed‑loop, intent‑based control (For example: Maximizing throughput in urban cells) without human intervention. Their modular, extensible design aligns with TMF’s composable architecture, allowing networks to self‑configure, self‑optimize, and self‑heal in real time to meet high‑level business goals autonomously.

As the network management system evolves, rApps orchestration and alignment are needed to use all automation for one purpose. This is where as AI makes the difference. Agentic AI is an advancement of generative AI, which is modular. Each module is represented by an agent that can autonomously make decisions, set goals, take actions, and interact with its agent peers. These systems exhibit a degree of independence, often combining reasoning, planning, and adaptability to operate effectively in dynamic environments. Agentic AI is the final step for Autonomous Networks Level 5.

Agentic AI, powered by AWS’s cutting-edge cloud infrastructure, addresses these challenges by introducing an intelligent ecosystem of specialized AI agents. These agents work in concert to monitor, analyze, and optimize network performance by orchestrating and leveraging specialized rApps. Unlike conventional systems, agentic AI brings a level of intelligence and adaptability that closely mirrors human decision-making processes while operating at machine speed and scale.

The AWS foundational services of agentic AI have several advantages. Through [Amazon Bedrock’s](https://aws.amazon.com/bedrock/) supported pre-trained models, Ericsson achieves acceleration in development and deployment cycles. Amazon Bedrock agents simplify complex network management processes. The solution leverages AWS’s high-performance computing infrastructure to ensure consistent performance and global scalability. Additionally, AWS’s comprehensive security framework, including enterprise-grade encryption and extensive compliance certifications, ensures network optimization within a protected environment.

The transformation brought by agentic AI goes beyond mere technical improvements. It represents a fundamental shift in how networks are managed. It moves reactive troubleshooting to proactive optimization, isolated decision-making to coordinated intelligence, and human-dependent operations to autonomous systems that maintain human oversight while handling complexity at scale.

This technological evolution is crucial for the telecommunications industry today. As networks become increasingly complex and user expectations continue to rise, the ability to maintain and optimize network performance efficiently becomes not only an operational advantage but also a competitive necessity. Agentic AI provides the tools and capabilities necessary to navigate this new landscape successfully.

### Talk to network

The concept of ‘talk to network’ represents a paradigm shift in network management by introducing an intuitive, natural language interface between operators and their network infrastructure. This approach transforms complex technical operations into conversational interactions, enabling operators to manage and optimize their networks through human-like conversations. Agentic AI is the key enabler to allow intent-driven, closed-loop automation without human intervention, a pathway to Automation Level 5. Traditional network management interfaces require operators to navigate through complex technical dashboards and maintain expertise across multiple specialized systems. talk to network eliminates these barriers by providing a natural language interface that understands operator intent and translates it into precise technical actions.

A communications service provider (CSP) can ask, ‘What’s going on in the network?’ and the system will analyze the network conditions, identify significant patterns, and present a coherent narrative in clear terms. Similarly, when asked, ‘What needs fixing?’ the system prioritizes issues based on impact and urgency, providing contextual information for informed decisions.

The system’s capability extends beyond mere status reporting. When operators ask, ‘What are the solution scenarios?’, the system evaluates multiple potential interventions and identifies the optimal solution that balances effectiveness, risk, and resource utilization.

### AI Agent ecosystem for network optimization

The power of agentic AI lies in its sophisticated ecosystem of specialized agents, each designed to handle specific aspects of network optimization while working in concert under the coordination of a generative AI powered supervisor agent. This architecture marks a significant advancement in automated network management, moving beyond simple rule-based systems to intelligent, adaptive operations.

A typical use case is triggered by an event spawned by the Cell Anomaly Detector agent, which processes data from over 60,000 KPIs to identify 20 distinct classes of network issues, while advanced classification algorithms minimize false positives and ensure accurate issue categorization. The Root Cause Explainer agent delves deeper into identified issues, analyzes up to 20 sub-causes per issue class, and enables precise problem identification. The Supervisor agent reasons on the identified problem and plans an optimization strategy leveraging specialized optimization agents to gather further data points and implement an action plan.

[![Figure 1 Agentic AI pathway to autonomous networks level 5](https://d2908q01vomqb2.cloudfront.net/c5b76da3e608d34edb07244cd9b875ee86906328/2025/07/02/Figure-1-Agentic-AI-pathway-to-autonomous-networks-level-5.png)](https://d2908q01vomqb2.cloudfront.net/c5b76da3e608d34edb07244cd9b875ee86906328/2025/07/02/Figure-1-Agentic-AI-pathway-to-autonomous-networks-level-5.png)*Figure 1: Agentic AI pathway to autonomous networks level 5*

### From issue detection to resolution

The journey from identifying network issues to implementing effective solutions follows a three-stage process that combines Ericsson’s advanced diagnostics with intelligent performance optimization. This comprehensive approach ensures thorough problem resolution while maintaining network stability and service quality.

**Stage one: Diagnostics**

The diagnostic phase employs three sequential steps building upon each other’s insights. Detection utilizes deep-embedded clustering and semi-supervised learning algorithms to identify anomalies and potential issues before they impact service quality. The classification step leverages convolutional neural networks and generative issue pattern detection, with active learning capabilities that improve accuracy over time. Root cause analysis combines embedded Network Operations Domain (NOD) knowledge with causal analysis to determine the underlying factors behind identified issues.

**Stage two: General optimization**

Once issues are understood, the general optimization phase addresses basic network parameters and configurations. This stage handles straightforward adjustments for immediate improvements in common network challenges. For complex scenarios, the system transitions to advanced performance optimizers that can handle multi-variable optimization problems.

**Stage three: Specialized performance optimization**

The final stage deploys specialized optimization agents for specific network functions. The RET (Remote Electrical Tilt) and AAS (Advanced Antenna System) Cell Shaper agents handle cell configuration, while the Uplink Interference Optimizer addresses signal quality. The Intelligent Layer Manager oversees network layer optimization, and Voice Connection and Integrity optimizers ensure call quality. This approach ensures expert attention to each performance aspect.

[![Figure 3 From issue detection to resolution, end to end flow](https://d2908q01vomqb2.cloudfront.net/c5b76da3e608d34edb07244cd9b875ee86906328/2025/07/02/Figure-3-From-issue-detection-to-resolution-end-to-end-flow.png)](https://d2908q01vomqb2.cloudfront.net/c5b76da3e608d34edb07244cd9b875ee86906328/2025/07/02/Figure-3-From-issue-detection-to-resolution-end-to-end-flow.png)*Figure 2: From issue detection to resolution, end to end flow*

### Architecture

The agentic AI-based architecture features a hierarchical system in which the supervisor agent, implemented using Amazon Bedrock Agent, orchestrates operations. This supervisor oversees specialized agents: The Cell Anomaly Detector agent, the Anomaly Root Cause Explainer agent, and the Anomaly General Optimizer agent.

Each agent interfaces with Talk2Data and the RAG components, creating a comprehensive analytical framework. Each specialized agent is associated with its own rApp and documentation.

An Output Summarization and Visualization agent, also powered by Amazon Bedrock Agent, generates three distinct types of deliverables: Textual explanations, graphical representations, and detailed reports. This multi-modal output ensures effective communication with all stakeholders, regardless of their technical background.

[![Figure 4 Amart solution with agentic AI architecture 2](https://d2908q01vomqb2.cloudfront.net/c5b76da3e608d34edb07244cd9b875ee86906328/2025/07/02/Figure-4-Amart-solution-with-agentic-AI-architecture-2.png)](https://d2908q01vomqb2.cloudfront.net/c5b76da3e608d34edb07244cd9b875ee86906328/2025/07/02/Figure-4-Amart-solution-with-agentic-AI-architecture-2.png)*Figure 3: Smart solution with agentic AI architecture*

### Agentic AI process

The practical implementation of agentic AI’s capabilities is best illustrated through a typical workflow scenario. When an operator requests a cell performance improvement analysis with supporting visualizations, the system activates a coordinated sequence of agent interactions.

The workflow begins with the supervisor agent orchestrating the process. This central intelligence coordinates specialized agents, ensuring smooth information flow and coherent analysis. The Cell Anomaly Detector agent interfaces with its associated rApp through Talk2Data and RAG capabilities to perform the required analysis to evaluate the current situation.

Following detection, the Anomaly Root Cause Explainer agent utilizes Talk2Data and the RAG systems to determine the underlying causes. The investigation then moves to the Anomaly General Optimizer agent, which develops specific optimization recommendations based on the identified issues and their root causes.

Throughout this process, continuous communication flows between all agents and the supervisor agent, ensuring coordinated analysis and consistent recommendations. The Output Summarization and Visualization agent compiles all findings into a comprehensive response package with explanations, visual representations, and actionable recommendations.

*[![Figure 6 Amart solution with agentic AI demo flow 2](https://d2908q01vomqb2.cloudfront.net/c5b76da3e608d34edb07244cd9b875ee86906328/2025/07/02/Figure-6-Amart-solution-with-agentic-AI-demo-flow-2.png)](https://d2908q01vomqb2.cloudfront.net/c5b76da3e608d34edb07244cd9b875ee86906328/2025/07/02/Figure-6-Amart-solution-with-agentic-AI-demo-flow-2.png)Figure 4: Smart solution with agentic AI demo flow*

### Key benefits of agentic AI

The implementation of agentic AI delivers transformative benefits that will reshape network operations and business outcomes. The most evident impact is an 80 percent reduction in time spent on analysis and decision-making processes, creating operational and financial advantages across the organization.

OPEX efficiency gains materialize through streamlined processes and automated analysis. This efficiency reduces the operational effort needed for routine network management tasks, day-to-day troubleshooting, and optimization activities.

The transformation agility enables organizations to adapt swiftly to changing network conditions and market demands. The system’s rapid analysis capabilities enable CSPs to implement changes quickly, maintaining optimal performance even during unexpected events.

Revenue enhancement follows from improved network performance and customer experience. Better network quality increases customer satisfaction and reduces churn, while optimized resource utilization creates opportunities for new services. The system’s predictive capabilities enable proactive capacity planning for future demands.

Speed and agility: Ericsson achieves rapid development and deployment through Amazon Bedrock’s pre-trained models. This enables rapid prototyping and deployment of AI-powered applications, reducing time-to-market for new features. The platform adapts to changing network conditions, ensuring solutions remain current and effective.

Simplification: Through Amazon Bedrock Agents, Ericsson CNS simplifies network management processes. The system integrates with the existing infrastructure and connects with company systems, APIs, and data sources. This integration leverages foundation models for reasoning and transforms complex network operations into streamlined workflows.

Performance and scalability: The solution utilizes AWS’s high-performance computing infrastructure and automatically scales to meet workload demands. This ensures consistent performance across global regions with minimal latency, from small network segments to massive nationwide deployments.

Security: Ericsson CNS leverages AWS’s comprehensive security framework, including enterprise-grade encryption, access controls, secure endpoints, and compliance certifications. The security architecture meets industry standards and regulatory requirements, ensuring that network optimization occurs within a protected environment.

### Beyond talk-to-network

The evolution beyond talk-to-network capabilities marks a quantum leap in network management intelligence. The supervisor agent acts as a strategic mastermind, deriving meaningful insights from complex data patterns to deliver proactive, context-aware network management.

The intelligence framework processes natural language interactions while interpreting network dynamics. Specialized LLM agents comprehend external context, detect anomalies, explain root causes, and materialize generate optimization strategies. These agents operate predictively, anticipating potential issues and developing solutions before problems.

The system maintains continuous awareness of network health through advanced monitoring and analysis. It evaluates whether current actions achieve their intended outcomes and assesses the reliability of underlying models. When opportunities for improvement arise, such as unexpected usage patterns during events, the system generates contextual recommendations tailored to specific situations.

[![Figure 7 Beyond talk-to-network](https://d2908q01vomqb2.cloudfront.net/c5b76da3e608d34edb07244cd9b875ee86906328/2025/07/02/Figure-7-Beyond-talk-to-network.png)](https://d2908q01vomqb2.cloudfront.net/c5b76da3e608d34edb07244cd9b875ee86906328/2025/07/02/Figure-7-Beyond-talk-to-network.png)*Figure 5: Beyond talk-to-network*

### Conclusions

The journey toward Autonomous Networks Level 5 requires sophisticated tools and intelligent systems capable of managing the complexity of modern network operations. Agentic AI, powered by AWS technology, represents a pivotal advancement in this evolution. Its comprehensive agent ecosystem, robust governance framework, and optimization capabilities deliver measurable benefits while ensuring the security and reliability essential for critical network operations.

The increasing complexity of networks underscores the growing importance of intelligent automation. Agentic AI’s architecture, built on AWS services, establishes a foundation for future advancements, enabling CSPs to attain higher levels of operational excellence and preparedness for emerging challenges and opportunities.

Agentic AI’s transformative impact extends beyond technological enhancement, fundamentally redefining network management and optimization practices. The integration of advanced AI capabilities with intuitive interfaces and comprehensive security measures paves the way for autonomous networks while preserving essential operational control and visibility. This balance between automation and oversight combined with substantial operational improvements establishes agentic AI as an indispensable tool for CSPs in the evolving landscape of network management.

![Christian Finelli](https://d2908q01vomqb2.cloudfront.net/c5b76da3e608d34edb07244cd9b875ee86906328/2022/11/18/finelli.png)

### Christian Finelli

Christian Finelli is a Senior Solutions Architect at AWS, part of the Industries Telco Business Unit, with over 20 years of experience of building and architecting for Enterprises, Network Equipment Providers, and Communication Service Providers to achieve their business objectives. Christian bridges cloud and telco expertise to help transform the Industry. Christian is passionate about history and literature.

![Ali Sharaf](https://d2908q01vomqb2.cloudfront.net/c5b76da3e608d34edb07244cd9b875ee86906328/2025/07/22/Ali-Sharaf.png)

### Ali Sharaf

Ali is a Strategic Product Manager at Ericsson, with over 15 years of experience in the telecom sector. He specializes in building solutions in the domain of data analytics and network optimization strategies with dedicated focus on AI-based innovations for Network automation.

![Billion Lo](https://d2908q01vomqb2.cloudfront.net/c5b76da3e608d34edb07244cd9b875ee86906328/2025/07/22/Billion-Lo.png)

### Billion Lo

Billion has over 14+ years of experience in the Telecom space with diverse expertise in service delivery, R&D, product and strategy management with the field of knowledge from cloud-native, AI & MLOps, Automation, Analytics and Core network (including User Data Management and Policy), and cloud infrastructure while having working experience to support customers globally and previous located in Indonesia, and Taiwan.

![Manuel Sierra Marco](https://d2908q01vomqb2.cloudfront.net/c5b76da3e608d34edb07244cd9b875ee86906328/2025/07/22/Manuel-Sierra-Marco.png)

### Manuel Sierra Marco

Specialized in Cognitive Network Solutions, rApps and AI-based solutions. With 20+ years in the telecom industry, he has held technical and strategic roles across Europe, Southeast Asia, and Latin America.



Loading comments…

### Resources

* [AWS for Industry](https://aws.amazon.com/industries?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=industries-resources)
* [AWS Events](https://aws.amazon.com/events?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=industries-resources)
* [AWS Training & Certification](https://aws.amazon.com/training/?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=industries-resources)
* [AWS Whitepapers](https://aws.amazon.com/whitepapers/?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=industries-resources)
* [AWS Compliance Reports](https://aws.amazon.com/artifact/?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=industries-resources)

---

### Follow

* [Twitter](https://twitter.com/awscloud)
* [Facebook](https://www.facebook.com/amazonwebservices)
* [LinkedIn](https://www.linkedin.com/company/amazon-web-services/)
* [Twitch](https://www.twitch.tv/aws)
* [Email Updates](https://pages.awscloud.com/communication-preferences?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=industries-social)

[Create an AWS account](https://signin.aws.amazon.com/signup?request_type=register)

## Learn

* [What Is AWS?](/what-is-aws/?nc1=f_cc)
* [What Is Cloud Computing?](/what-is-cloud-computing/?nc1=f_cc)
* [What Is Agentic AI?](/what-is/agentic-ai/?nc1=f_cc)
* [Cloud Computing Concepts Hub](/what-is/?nc1=f_cc)
* [AWS Cloud Security](/security/?nc1=f_cc)
* [What's New](/new/?nc1=f_cc)
* [Blogs](/blogs/?nc1=f_cc)
* [Press Releases](https://press.aboutamazon.com/press-releases/aws)

## Resources

* [Getting Started](/getting-started/?nc1=f_cc)
* [Training](/training/?nc1=f_cc)
* [AWS Trust Center](/trust-center/?nc1=f_cc)
* [AWS Solutions Library](/solutions/?nc1=f_cc)
* [Architecture Center](/architecture/?nc1=f_cc)
* [Product and Technical FAQs](/faqs/?nc1=f_dr)
* [Analyst Reports](/resources/analyst-reports/?nc1=f_cc)
* [AWS Partners](/partners/work-with-partners/?nc1=f_dr)

## Developers

* [Builder Center](/developer/?nc1=f_dr)
* [SDKs & Tools](/developer/tools/?nc1=f_dr)
* [.NET on AWS](/developer/language/net/?nc1=f_dr)
* [Python on AWS](/developer/language/python/?nc1=f_dr)
* [Java on AWS](/developer/language/java/?nc1=f_dr)
* [PHP on AWS](/developer/language/php/?nc1=f_cc)
* [JavaScript on AWS](/developer/language/javascript/?nc1=f_dr)

## Help

* [Contact Us](/contact-us/?nc1=f_m)
* [File a Support Ticket](https://console.aws.amazon.com/support/home/?nc1=f_dr)
* [AWS re:Post](https://repost.aws/?nc1=f_dr)
* [Knowledge Center](https://repost.aws/knowledge-center/?nc1=f_dr)
* [AWS Support Overview](/premiumsupport/?nc1=f_dr)
* [Get Expert Help](https://iq.aws.amazon.com/?utm=mkt.foot/?nc1=f_m)
* [AWS Accessibility](/accessibility/?nc1=f_cc)
* [Legal](/legal/?nc1=f_cc)

English

Back to top

Amazon is an Equal Opportunity Employer: Minority / Women / Disability / Veteran / Gender Identity / Sexual Orientation / Age.

[x](https://twitter.com/awscloud) [facebook](https://www.facebook.com/amazonwebservices) [linkedin](https://www.linkedin.com/company/amazon-web-services/) [instagram](https://www.instagram.com/amazonwebservices/) [twitch](https://www.twitch.tv/aws) [youtube](https://www.youtube.com/user/AmazonWebServices/Cloud/) [podcasts](/podcasts/?nc1=f_cc) [email](https://pages.awscloud.com/communication-preferences?trk=homepage)

* [Privacy](/privacy/?nc1=f_pr)
* [Site terms](/terms/?nc1=f_pr)
* [Cookie Preferences](#)

© 2026, Amazon Web Services, Inc. or its affiliates. All rights reserved.