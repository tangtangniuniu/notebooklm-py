> Source: https://arxiv.org/html/2604.18233v1

Aether: Network Validation Using Agentic AI and Digital Twin






##### Report GitHub Issue

×

Title:


Content selection saved. Describe the issue below:

Description:

Submit without GitHub
Submit in GitHub


[![arXiv logo](/static/browse/0.3.4/images/arxiv-logo-one-color-white.svg)
Back to arXiv](/)


[Why HTML?](https://info.arxiv.org/about/accessible_HTML.html)
[Report Issue](# "Report an issue")

[Back to Abstract](/abs/2604.18233v1 "Back to abstract page")

[Download PDF](/pdf/2604.18233v1 "Download PDF")

1. [Abstract](#abstract1 "In Aether: Network Validation Using Agentic AI and Digital Twin")
2. [I Introduction](#S1 "In Aether: Network Validation Using Agentic AI and Digital Twin")
3. [II Related work](#S2 "In Aether: Network Validation Using Agentic AI and Digital Twin")
   1. [II-A NetDevOps Automation](#S2.SS1 "In II Related work ‣ Aether: Network Validation Using Agentic AI and Digital Twin")
   2. [II-B Formal network verification](#S2.SS2 "In II Related work ‣ Aether: Network Validation Using Agentic AI and Digital Twin")
   3. [II-C Network Digital Twins](#S2.SS3 "In II Related work ‣ Aether: Network Validation Using Agentic AI and Digital Twin")
   4. [II-D Agentic Verification](#S2.SS4 "In II Related work ‣ Aether: Network Validation Using Agentic AI and Digital Twin")
4. [III Problem Statement](#S3 "In Aether: Network Validation Using Agentic AI and Digital Twin")
   1. [III-A Motivation and Design Principles](#S3.SS1 "In III Problem Statement ‣ Aether: Network Validation Using Agentic AI and Digital Twin")
   2. [III-B Network Change Validation process](#S3.SS2 "In III Problem Statement ‣ Aether: Network Validation Using Agentic AI and Digital Twin")
5. [IV Aether](#S4 "In Aether: Network Validation Using Agentic AI and Digital Twin")
   1. [IV-A Aether Agents](#S4.SS1 "In IV Aether ‣ Aether: Network Validation Using Agentic AI and Digital Twin")
   2. [IV-B Aether NDT](#S4.SS2 "In IV Aether ‣ Aether: Network Validation Using Agentic AI and Digital Twin")
      1. [IV-B1 Network Digital Map](#S4.SS2.SSS1 "In IV-B Aether NDT ‣ IV Aether ‣ Aether: Network Validation Using Agentic AI and Digital Twin")
      2. [IV-B2 Aether NDT Tools](#S4.SS2.SSS2 "In IV-B Aether NDT ‣ IV Aether ‣ Aether: Network Validation Using Agentic AI and Digital Twin")
6. [V Aether Implementation](#S5 "In Aether: Network Validation Using Agentic AI and Digital Twin")
7. [VI Evaluation methodology](#S6 "In Aether: Network Validation Using Agentic AI and Digital Twin")
   1. [VI-A Network Change scenarios](#S6.SS1 "In VI Evaluation methodology ‣ Aether: Network Validation Using Agentic AI and Digital Twin")
   2. [VI-B Evaluation Datasets](#S6.SS2 "In VI Evaluation methodology ‣ Aether: Network Validation Using Agentic AI and Digital Twin")
   3. [VI-C Evaluation Metrics](#S6.SS3 "In VI Evaluation methodology ‣ Aether: Network Validation Using Agentic AI and Digital Twin")
8. [VII Evaluation](#S7 "In Aether: Network Validation Using Agentic AI and Digital Twin")
   1. [VII-A Single Agent Assessment](#S7.SS1 "In VII Evaluation ‣ Aether: Network Validation Using Agentic AI and Digital Twin")
   2. [VII-B End-to-end performance](#S7.SS2 "In VII Evaluation ‣ Aether: Network Validation Using Agentic AI and Digital Twin")
9. [VIII Real-World Network use cases](#S8 "In Aether: Network Validation Using Agentic AI and Digital Twin")
10. [IX Discussion](#S9 "In Aether: Network Validation Using Agentic AI and Digital Twin")
11. [X Conclusions](#S10 "In Aether: Network Validation Using Agentic AI and Digital Twin")
12. [References](#bib "In Aether: Network Validation Using Agentic AI and Digital Twin")

[License: arXiv.org perpetual non-exclusive license](https://info.arxiv.org/help/license/index.html#licenses-available)

arXiv:2604.18233v1 [cs.MA] 20 Apr 2026

# Aether: Network Validation Using Agentic AI and Digital Twin

Jordan Auge, Sam Betts, Giovanna Carofiglio, Giulio Grassi, Martin Gysi, John Kenneth d’Souza
J. Auge, S. Betts, G. Carofiglio, and G. Grassi are with Cisco Systems, Paris, France and London, UK.M. Gysi and J. K. d’Souza are with Swisscom, Zurich, Switzerland.

###### Abstract

Network change validation remains a critical yet predominantly manual, time-consuming, and error-prone process in modern network operations. While formal network verification has made substantial progress in proving correctness properties, it is typically applied in offline, pre-deployment settings and faces challenges in accommodating continuous changes and validating live production behavior. Current operational approaches typically involve scattered testing tools, resulting in partial coverage and errors that surface only after deployment.

In this paper, we present Aether, a novel approach that integrates Generative Agentic AI with a multi-functional Network Digital Twin to automate and streamline network change validation workflows.
It features an agentic architecture with five specialized Network Operations AI agents that collaboratively handle the change validation lifecycle from intent analysis to network verification and testing.

Aether agents use a unified Network Digital Twin integrating modeling, simulation, and emulation to maintain a consistent, up-to-date network view for verification and testing. By orchestrating agent collaboration atop this digital twin, Aether enables automated, rapid network change validation while reducing manual effort, minimizing errors, and improving operational agility and cost-effectiveness.
We evaluate Aether over synthetic network change scenarios covering main classes of network changes and on past incidents from a major ISP operational network, demonstrating promising results in error detection (100%), diagnostic coverage (92-96%), and speed (6-7 minutes) over traditional methods.

## I Introduction

As networks grow in scale, complexity, and criticality, the ability to validate changes
introduced by configuration updates and architectural modifications efficiently and reliably has become paramount for network operators in enterprise and service provider environments alike.
Despite substantial research and technological advancements in the field, network change validation remains a largely manual, fragmented, and error-prone process, making it a contributor to network failures and the
nearly 400​B400B of annual cost related to unplanned downtime [[25](#bib.bib42 "The hidden costs of downtime:the $400b problem facing the global 2000")].
Operational workflows typically rely on a patchwork of verification tools, simulation platforms, and ad-hoc testing solutions, each with limited scope and interoperability. This fragmented landscape not only increases the operational burden on skilled professionals but also leads to gaps in testing coverage, with errors frequently surfacing only after changes have been deployed into production networks.
The industry’s growing adoption of automation and Dev-Ops-inspired methodologies (commonly referred to as NetDevOps) has alleviated some operational pain points by promoting repeatable workflows and incremental automation. However, the problem of providing comprehensive, end-to-end validation remains.
In parallel, the emergence of generative AI and agentic AI systems introduces new opportunities for automating and enhancing network operations. When combined with advances in network digital twin technology to provide dynamic, high-fidelity virtual replicas of production networks, there is significant potential to transform the way network change validation is performed.

In this paper, we introduce Aether, a novel solution at the intersection of generative agentic AI, NetDevOps practices and network digital twins that combines the strengths of Agentic AI and multi-functional Network Digital Twins to deliver a unified, NetDevOps-automated and scalable network change validation solution integrated in existing processes.
Aether design is extensible both in terms of AI agents and of validation capabilities: an initial implementation has focused on verification and simulation functions and has been evaluated through practical case studies, including network change scenarios reproducing past incidents within a major ISP operational network.
Aether benefits are quantified against the baseline by means of human and generative AI domain expertise by defining metrics that quantify issue detection accuracy, correctness, robustness and cost for analysis and testing.
Our analysis shows that Aether delivers promising results in automation, test coverage ( 92-96%), error detection (100%), and operational efficiency compared to existing practices, hence encouraging future development and extension of the approach.
This work does not raise any ethical issues.
The paper is organized as follows. Sec. [II](#S2 "II Related work ‣ Aether: Network Validation Using Agentic AI and Digital Twin") surveys network verification and early AI applications. Sec. [III](#S3 "III Problem Statement ‣ Aether: Network Validation Using Agentic AI and Digital Twin") presents the problem and baseline workflow. Sec. [IV](#S4 "IV Aether ‣ Aether: Network Validation Using Agentic AI and Digital Twin") details Aether’s architecture (agents and NDT), with implementation in Sec. [V](#S5 "V Aether Implementation ‣ Aether: Network Validation Using Agentic AI and Digital Twin"). Secs. [VI](#S6 "VI Evaluation methodology ‣ Aether: Network Validation Using Agentic AI and Digital Twin")-[VII](#S7 "VII Evaluation ‣ Aether: Network Validation Using Agentic AI and Digital Twin") present methodology and results, including real-world ISP case studies (Sec. [VIII](#S8 "VIII Real-World Network use cases ‣ Aether: Network Validation Using Agentic AI and Digital Twin")). Finally, Secs. [IX](#S9 "IX Discussion ‣ Aether: Network Validation Using Agentic AI and Digital Twin")-[X](#S10 "X Conclusions ‣ Aether: Network Validation Using Agentic AI and Digital Twin") summarize lessons learned and future work.

## II Related work

Network change validation has evolved through automation, preventative verification, and digital twins. This section surveys relevant research and tools, reviews early generative AI work, and motivates our approach.

### II-A NetDevOps Automation

Intent-driven NetDevOps automation is transforming network operations. Best practices now emphasize scripted automation, CI/CD pipelines, and Network Sources of Truth (NSOT) for managing configuration changes at scale. Tools like Ansible [[31](#bib.bib53 "Ansible: simple, agentless it automation")], Puppet [[29](#bib.bib54 "Puppet: infrastructure automation for security and compliance")], and configuration management databases enable configuration velocity and consistency. However, important challenges remain in both adoption and capabilities.

Lack of semantic verification - These systems validate configuration syntax and structural consistency, but fail to verify semantic effects on network state (operational consistency, i.e. whether the change breaks a critical policy).

Limited testing capabilities - Most automation solutions perform only generic tests that do not validate specific change intents. Meaningful validation often requires additional empirical testing through manually developed test plans, later integrated into test suites. This manual, error-prone, and reactive process scales poorly.

Insufficient root cause analysis - When tests fail, they signal problems without providing root cause analysis or guaranteeing that remediations address all side effects, perpetuating reactive troubleshooting.
To overcome such limitations, the research community has pioneered a more proactive and formal approach, often referred to as declarative network validation.
Here, we focus on previous work relevant to network change validation without attempting an exhaustive survey.

### II-B Formal network verification

Header Space Analysis (HSA) [[16](#bib.bib29 "Header space analysis: static checking for networks")] pioneered rigorous configuration analysis, aiming to mathematically prove network behavior properties rather than rely on empirical testing. Research from cloud operators including Microsoft Azure and Alibaba [[5](#bib.bib30 "Checking cloud contracts in microsoft azure"), [2](#bib.bib31 "A general approach to network configuration verification"), [3](#bib.bib32 "Putting network verification to good use"), [15](#bib.bib63 "Real time network policy checking using header space analysis"), [45](#bib.bib44 "Accuracy, scalability, coverage: a practical configuration verifier on a global wan"), [40](#bib.bib47 "LFVeri: network configuration verification for virtual private cloud networks"), [46](#bib.bib45 "Meissa: scalable network testing for programmable data planes"), [36](#bib.bib46 "Aquila: a practically usable verification system for production-scale programmable data planes"), [43](#bib.bib48 "Relational network verification")] has been instrumental in translating fundamental research into solutions for real-world operational challenges in formal network verification (FNV). Early FNV efforts adopted abstract models independent of vendor-specific configurations. Declarative languages like Datalog [[18](#bib.bib28 "Efficient network configuration verification using optimized datalog")] evolved to represent complex device packet-processing pipelines with sufficient fidelity for modeling vendor configurations.

NetCov [[15](#bib.bib63 "Real time network policy checking using header space analysis")] introduced systematic metrics for quantifying test coverage in network verification, though technical coverage does not necessarily correlate with operational or business-critical concerns. Recent work by Krentsel et al. [[17](#bib.bib14 "Towards accessible model-free verification")] on accessible model-free verification explores approaches to make formal verification more practical for operators.

Relational Verification [[43](#bib.bib48 "Relational network verification")] extended this work to cover change verification, comparing pre-change and post-change network snapshots to ensure modifications introduce only expected, localized effects—the approach we adopt in this paper. Relational NetKAT [[42](#bib.bib83 "Network change validation with relational netkat")] recently introduced a compositional language to formally specify the mapping between pre- and post-change states, allowing operators to verify that end-to-end packet behavior evolves according to an intended transformation. Work to operationalise it remains open, and generative AI is a promising direction to bridge this formal modeling into CI/CD leveraging user intent.
Despite significant growth in open-source verification tools over the past decade, they remain largely underutilized in production environments, with notable exceptions like Batfish [[6](#bib.bib50 "Lessons from the evolution of the batfish configuration analysis tool")].

### II-C Network Digital Twins

Network verification landscape spans multiple paradigms, each one with distinct characteristics and limitations, as summarized in Table [I](#S2.T1 "Table I ‣ II-C Network Digital Twins ‣ II Related work ‣ Aether: Network Validation Using Agentic AI and Digital Twin").

Model-based verification tools represent one approach, with Batfish as a prominent HSA implementation. Batfish’s strengths include what-if scenario analysis, formal model-based verification, and configuration ingestion across diverse vendor platforms. While Batfish excels at Layer 3 verifications—forwarding reachability, ACL (Access Control List) analysis, and model-based data-plane computation, it remains fundamentally limited to these domains.

Simulation-based platforms bridge model-based and emulation approaches, offering dynamic analysis with statistical abstraction. Simulators like [[32](#bib.bib4 "The ns-3 network simulator")], [[39](#bib.bib13 "An overview of the omnet++ simulation environment")] provide varying fidelity levels, enabling realistic traffic patterns and protocol interactions while maintaining computational efficiency. Their main application is
performance analysis which requires scalable simulation of realistic traffic. Recently, tools like RouteNet [[33](#bib.bib61 "RouteNet: leveraging graph neural networks for network modeling and optimization in sdn")] address scalability challenges by training ML models (Graph Neural Networks) for rapid performance prediction based on topology and traffic patterns. However, these specialized tools require complementary solutions like Batfish to compute the topology and forwarding plane states needed for what-if analysis.

Emulation platforms like [[10](#bib.bib12 "GNS3 network emulator")] or [[35](#bib.bib5 "Containerlab")] pursue maximum fidelity through container-based virtualization, VMs, or native router images, exemplifying the core verification tradeoff: fidelity and scalability are inversely related, with hardware optimizations necessarily abstracted. While emulation captures vendor-specific behaviors and edge cases beyond model-based tools’ reach, it requires substantially more compute resources and execution time. Physical network replicas offer ultimate fidelity for detecting otherwise-impossible errors, but their resource demands severely restrict verification scope and frequency.

Aether’s design follows a modular compositional approach to network verification as recently proposed by the research community [[41](#bib.bib77 "Network change validation with relational netkat")].
Complex verification tasks are decomposed into smaller ones that can be independently analyzed and later combined to achieve end-to-end assurance. As an example, verifying an SRv6 overlay involves both examining the underlay’s forwarding behavior—using tools such as Batfish—and evaluating the overlay’s segment routing logic with dedicated SRv6-aware analyzers. Likewise, performance verification across multi-layer networks often requires integrating structural analysis from model-based tools with traffic-aware performance predictions provided by simulation tools like RouteNet.

| Type | Fidelity | Scale | Limitations |
| --- | --- | --- | --- |
| Model | Low-Med | High | L3 only, no traffic |
| Simulation | Medium | Medium | Needs topology |
| Emulation | High | Low | Resource intensive |
| Physical | Highest | Lowest | Limited scope |

Table I: Network Verification Paradigms

Network Digital Twin Platforms: To bridge the gap between different verification approaches, digital twin efforts (cfr. [[30](#bib.bib11 "A comprehensive survey of network digital twin architecture, capabilities, challenges, and requirements for edge-cloud continuum")] and references therein) have emerged to provide a more realistic, real-time mirror of the production network, serving as a sandbox for safe experimentation and test execution. The concept has gained significant traction lately within the Internet Engineering Task Force (IETF), where standardization efforts are underway to define architectural frameworks for Network Digital Twins (in IETF’s Network Management Operations working group [[12](#bib.bib38 "IETF nmog internet draft - simap: concept, requirements, and use cases")])

Initiatives such as TwinEU [[38](#bib.bib39 "Developing a concept of pan-european digital twin of the electricity system")] or TMForum Network Digital Twin group [[37](#bib.bib9 "Digital twin for decision intelligence (dt4di): from strategy to implementation")] also explore standardized frameworks for defining digital maps and for interconnecting specialized digital twins across different network domains.

### II-D Agentic Verification

Applications of generative AI in networking have evolved from basic configuration generation [[27](#bib.bib33 "Kubeplaybook: a repository of ansible playbooks for kubernetes auto-remediation with llms"), [34](#bib.bib37 "Ansible lightspeed: a code generation service for it automation")] to interactive assistants. Recent works like “Ask Batfish” [[26](#bib.bib35 "What do llms need to synthesize correct router configurations?")] demonstrate LLMs as efficient natural language interfaces for formal verification, effectively translating user queries into tool-specific commands. However, these systems function primarily as single-turn, reactive QA interfaces—requiring operators to know precisely what to verify—or serve as static linters within CI/CD pipelines, lacking awareness of the specific change intent.
Aether advances this state of the art by moving from reactive translation to proactive multi-agent orchestration. Unlike static CI/CD suites that run pre-defined checks, Aether’s agents analyze natural language intent to dynamically generate and execute tailored verification plans, orchestrating heterogeneous tools to cover properties addressable only through tool composition (e.g., combining reachability with performance impact). This shift from ”chatting with tools” to ”autonomous validation workflows” enables handling the multi-step reasoning required for production change management.

## III Problem Statement

Drawing from related work analysis, we identify key limitations in current verification approaches and present Aether’s design principles (§[III-A](#S3.SS1 "III-A Motivation and Design Principles ‣ III Problem Statement ‣ Aether: Network Validation Using Agentic AI and Digital Twin")). We then establish the baseline network change validation process (§[III-B](#S3.SS2 "III-B Network Change Validation process ‣ III Problem Statement ‣ Aether: Network Validation Using Agentic AI and Digital Twin")) that contextualizes Aether’s operational setting.

### III-A Motivation and Design Principles

Key Limitations. As discussed in Sec. [II](#S2 "II Related work ‣ Aether: Network Validation Using Agentic AI and Digital Twin"), current verification approaches face three challenges: (i) Fragmentation—verification tools present heterogeneous data models and incompatible interfaces across paradigms (model-based, simulation, emulation), forcing operators to manually coordinate multiple tools for comprehensive validation; (ii) Cognitive barriers—operators face both the conceptual gap between natural language intent and abstract specifications (e.g., flow-set requirements [[4](#bib.bib72 "Network verification 2.0")]) and the operational complexity of using formal verification tools like Batfish, which require deep expertise to correctly specify queries and interpret results; and (iii) Agent operational requirements—network configurations exceed LLM context windows, complex protocol interactions surpass reasoning capabilities, and agents require structured data access, specialized verification tools (for correctness and trust), scalable interfaces, common data models to present information uniformly to both humans and machines, and bidirectional natural language support to integrate into human workflows.

Aether Approach. Aether addresses these limitations through a neuro-symbolic architecture combining LLM-based agents with a unified Network Digital Twin (NDT) infrastructure. This separation enables flexible intent interpretation paired with correct, compositional verification:

(P1) Intent-aware compositional orchestration: LLM agents (§[IV-A](#S4.SS1 "IV-A Aether Agents ‣ IV Aether ‣ Aether: Network Validation Using Agentic AI and Digital Twin")) translate natural language change intent into verification workflows by compositionally orchestrating specialized tools—enabling differential verification tailored to change intent (e.g., verifying specific route absence rather than exhaustive reachability) that would be infeasible with static CI/CD test suites.

(P2) Unified infrastructure addressing agent operational requirements: The NDT (§[IV-B](#S4.SS2 "IV-B Aether NDT ‣ IV Aether ‣ Aether: Network Validation Using Agentic AI and Digital Twin")) addresses agent scalability and reasoning limits through: (a) a temporal knowledge graph providing structured access to network data with query interfaces that fit LLM context windows; (b) specialized verification tools exposed via standardized APIs for correctness verification; (c) common data models (OpenConfig-based) presenting network state uniformly to agents and humans; and (d) natural language query support for graph traversal, enabling agents to gather targeted information without overwhelming their reasoning capabilities.

(P3) Workflow integration: Support integration into existing NetDevOps practices through CI/CD hooks (GitHub Actions, network controller synchronization) and natural language interfaces aligned with established change management workflows (§[III-B](#S3.SS2 "III-B Network Change Validation process ‣ III Problem Statement ‣ Aether: Network Validation Using Agentic AI and Digital Twin")).

Evaluation (§[VII](#S7 "VII Evaluation ‣ Aether: Network Validation Using Agentic AI and Digital Twin")) focuses on P1-P2, demonstrating intent-aware agent orchestration and compositional tool use. Analysis (§[IX](#S9 "IX Discussion ‣ Aether: Network Validation Using Agentic AI and Digital Twin")) examines agent-tool synergy and identifies that specialized knowledge injection is critical for handling protocol complexity. P3’s CI/CD integration is illustrated through production use cases but not systematically evaluated.

### III-B Network Change Validation process

![Refer to caption](2604.18233v1/x1.png)


Figure 1: Network Change Validation process.

Network change validation processes vary across domains and organizations but share common steps that we model as a baseline (Fig.[1](#S3.F1 "Figure 1 ‣ III-B Network Change Validation process ‣ III Problem Statement ‣ Aether: Network Validation Using Agentic AI and Digital Twin")).
The process begins with documenting change intent in an IT Service Management (ITSM) tool, followed by impact assessment to evaluate potential effects on the network environment.
A test plan is then defined to validate all critical areas affected by the change. These artifacts—change intent, impact analysis, and test plan—undergo peer review by the Change Advisory Board (CAB) for initial approval.
Upon approval, the change candidate is developed and tested against the defined plan. Test results are analyzed and the candidate is iteratively refined as needed. Finally, a second CAB review examines the results and documentation before approving production deployment. This multi-stage process ensures thorough validation, risk mitigation, and service reliability.

## IV Aether

Aether combines (i) a unified Network Digital Twin (NDT) with (ii) a suite of specialized AI agents driving the network change validation process by interacting with the user and with the NDT. The NDT acts as the core representation and tool for network validation: it is composed of

* •

  a Network Digital Map (NDM), i.e. a network representation in the form of a temporal graph allowing agents to access network status and knowledge in real-time and of
* •

  a set of network verification and testing tools operating on NDM time snapshots (production and candidate network states).

Aether generative AI Agents orchestrate validation workflows and automate decision-making throughout the change validation life-cycle.

![Refer to caption](2604.18233v1/x2.png)


Figure 2: Aether workflow.

Aether workflow is described in Fig.[2](#S4.F2 "Figure 2 ‣ IV Aether ‣ Aether: Network Validation Using Agentic AI and Digital Twin"): network telemetry data from production network is periodically ingested into the NDM to maintain an accurate up-to-date representation of the current network state and configuration. When a change request is initiated, Aether agents collaborate to analyze the change intent, assess its potential impact and generate tailored test plans, based on the intent and the current state of the network. Once the change has been implemented (by a human or Aether-external automation), agents execute tests against the candidate change within the NDT environment. If test results indicate issues, the user may iterate on the change implementation and re-initiate the validation process. Once tests pass successfully, the change and validation results are presented for final approval; Aether is designed as a Human-in-the-Loop (HITL) system, ensuring that critical deployment decisions and risk acceptance remain under human operator authority.

The following subsections detail Aether’s agent architecture (§[IV-A](#S4.SS1 "IV-A Aether Agents ‣ IV Aether ‣ Aether: Network Validation Using Agentic AI and Digital Twin")) and Network Digital Twin (§[IV-B](#S4.SS2 "IV-B Aether NDT ‣ IV Aether ‣ Aether: Network Validation Using Agentic AI and Digital Twin")).

![Refer to caption](2604.18233v1/x3.png)


Figure 3: Agents logical architecture.

### IV-A Aether Agents

Aether employs a multi-agent architecture to automate network change validation, represented as external entities in Figure [3](#S4.F3 "Figure 3 ‣ IV Aether ‣ Aether: Network Validation Using Agentic AI and Digital Twin"). Agent roles map to the baseline change management workflow, covering: impact assessment, test planning, test execution and reporting. They are orchestrated by a conversational Assistant Agent that serves as the primary user interface.
Such agents interact with Aether Network Digital Map (NDM) via an NDM Query agent allowing natural language queries to NDM Knowledge Graph data.

The multi-agent architecture provides the modularity and extensibility required by our design requirements. By decomposing validation into specialized agents, each focused on a distinct task, the system enables independent development, replacement, or augmentation of capabilities without disrupting the workflow. Task-specific agents maintain focused, domain-relevant context, enhancing reasoning accuracy and efficiency.

All agents support tool calling through the ReAct design pattern [[44](#bib.bib36 "ReAct: synergizing reasoning and acting in language models")], allowing planning, iteration and self-correction based on tool answers. The Assistant (or orchestrating workflow) is responsible for dispatching to specialized agents, and provide them with all required input artifacts such as: (1) context (change intent, ticket id, pull-request id), and (2) relevant artifacts (impact assessment, test plan) which are all persisted in the ITSM; and (3) per-change relevant chat history (shared working memory, backed by a database).
Agents are specialized through their system prompt defining their roles and objectives, available tools, formatting guidelines for the LLM, and more importantly their set of skills and access to memories (see Table [II](#S4.T2 "Table II ‣ IV-A Aether Agents ‣ IV Aether ‣ Aether: Network Validation Using Agentic AI and Digital Twin")).

Table II: Aether Agents Architecture and Specifications

| Assistant | Pattern: ReAct, LLM: GPT-4o |
| --- | --- |
| Objective | Natural Language (NL) interface with users, services and agents; Orchestration. |
| Tools | ITSM; Config. change repository; All agents |
| Skills | Dispatch tasks; Output summary; External artifact retrieval |
| Memories | Chat history, Ticket & Change information |
| Data | In:User Query; Out:Action,Reply; Ctx:Ticket ID |
| NDM Query | Pattern: ReAct, LLM: GPT-4o |
| Objective | Provide network state, NL into Graph Queries. |
| Tools | NDM (Schema & AQL Query) |
| Skills | Network Schema Navigation (OpenConfig), Protocol Logic, Graph Query Generation/Optim., Data Access Resilience |
| Memories | NDM/NDT Production snapshot |
| Data | In: NL Question; Out: Query response (raw/NL); Ctx: Snapshot ID |
| Impact A. | Pattern: ReAct, LLM: GPT-4o |
| Objective | Analyze change impact (affected devices/ layers, downtime, performance). |
| Tools | NDM (Schema & AQL Query); NDT Impact Assessment helper |
| Skills | Change Intent Analysis, NDT layered structure, Network Schema Navigation |
| Memories | NDM/NDT production snapshot |
| Data | In: Change Description Out: Assessment Report; Ctx: Snapshot ID |
| Test Plan | Pattern: ReAct; LLM: GPT-4o |
| Objective | Generate test plans |
| Tools | NDM (Schema & AQL Query) |
| Skills | Change Intent Analysis, Protocol Logic, Automated Relevance Filtering, Operational Verif. |
| Memories | Change Intent/Impact assessment(ITSM); NDM Production snapshot |
| Data | In: Change Description; Out: Test Plan; Ctx: Production Snapshot ID |
| Test Exec. | Pattern: ReAct, LLM: GPT-4o |
| Objective | Execute test plans, Retrieve Change candidate, Act as Validation Gateway. |
| Tools | NDM (Schema & AQL Query); NDT Tools |
| Skills | Operational Verif.; Protocol Logic; NDT Tool use |
| Memories | Change Intent (ITSM); Test plan (ITSM); Change implementation; |
| Data | In: Change Description, Test Plan, Change Implementation Reference; Out: Test Results & Report; Ctx: What-if Snapshot ID |

### IV-B Aether NDT

Aether Network Digital Twin
serves as the backbone of the Aether architecture, facilitating seamless interaction between Aether generative AI agents and the underlying network data and tools.
Aether NDT maintains an up-to-date graph-based Network Digital Map (NDM). It
provides the necessary context and information for the verification tools, ensuring that they operate on accurate and up-to-date representations of the network state. Aether NDT fetches data from the NDM as needed and transforms it based on the requirements of the tools. It also provides computing capabilities to the NDM to enrich the internal network representation.

| Capability | Category | Tool | Description |
| --- | --- | --- | --- |
| MTU consistency | KG-based | NDM | Check all network links have same MTU |
| Reachability | Model-based | Batfish | Check that a source can reach a destination IP address |
| Differential Reachability | Model-based | Batfish | Check if two snapshots have same reachability properties |
| Loop detection | Model-based | Batfish | Check for loops in the network topology |
| Traceroute | Model-based | Batfish | Simulate a traceroute from a source to a destination |
| ACL filters | Model-based | Batfish | Search ACL filters and outcomes |
| ACL filters | Model-based | Batfish | Compare two snapshots for ACL filters and outcomes |
| SLA verification | Simulation-based | NS-3 + custom code | Check if SLA is respected given a traffic demand |
| SLA verification | GNN-based | Routenet [[33](#bib.bib61 "RouteNet: leveraging graph neural networks for network modeling and optimization in sdn")] | Check if SLA is respected given a traffic demand |
| Configuration validation | Pattern-based | Diffy [[14](#bib.bib81 "Diffy: data-driven bug finding for configurations")] | Check if configuration files exhibit anomalies |

Table III: NDT Verification Capabilities and Tools

#### IV-B1 Network Digital Map

The Network Digital Map (NDM) serves as a unified data model and network source of truth (NSOT) for Aether agents that aggregates and normalizes information from diverse network sources into a standardized schema, providing a comprehensive view of network state and configuration as a Knowledge Graph.
The data schema is based on OpenConfig [[11](#bib.bib26 "OpenConfig data model")], a widely adopted vendor-neutral standard for network configuration and management. We chose OpenConfig over alternatives like IETF YANG modules due to its stronger vendor adoption and focus on operational usability.
Aether NDM extends the OpenConfig schema to accommodate Aether NDT requirements, ensuring accurate capture of all relevant network attributes.
At the core of Aether NDM is a Knowledge Graph (KG) modeling relationships between network entities and attributes. The KG is structured into multiple layers, each corresponding to a specific network aspect. The base layer represents physical devices and basic attributes, while higher layers capture complex configurations such as routing policies, L3/L1 interfaces, ACLs (respectively, the OpenConfig modules network-instance, interfaces and ACL are used), CLI configuration, and performance metrics. Each layer is self-contained and independent, enabling flexible integration and extension as requirements emerge. New OpenConfig modules can be added seamlessly.
Fig. [4](#S4.F4 "Figure 4 ‣ IV-B1 Network Digital Map ‣ IV-B Aether NDT ‣ IV Aether ‣ Aether: Network Validation Using Agentic AI and Digital Twin") shows how NDM layers connect to form a KG. The base layer contains device nodes linked to other layers via OWN relations. At each layer, nodes describe specific device status and configuration aspects. Nodes across layers are linked via CONNECT edges, representing relationships between properties owned by different devices (e.g., network instances connected because routes exist between devices).

![Refer to caption](2604.18233v1/x4.png)


Figure 4: NDM Knowledge Graph structure.

Data Ingestion in Aether NDM
The ingestion in Aether NDM is architected as a modular pipeline with three main components: (1) a set of *source adapters* that ingest input data from a specific source, process it, clean it, and normalize it to generate Aether-OpenConfig (Aether-OC) objects; (2) a *KG builder* that, given a set of Aether-OC objects, constructs the Knowledge Graph by creating nodes and edges—this step may leverage NDT computing capabilities to enrich the graph with computed relationships or attributes; and (3) a *graph database adapter* to store the KG (eg. ArangoDB [[1](#bib.bib80 "ArangoDB: the native multi-model database")]). Aether NDM supports extraction of network data from a variety of sources, including direct device access via Netconf [[9](#bib.bib51 "RFC 6241: network configuration protocol (netconf)")], controller APIs (e.g., Cisco Network Services Orchestrator [[7](#bib.bib85 "Cisco network services orchestrator (nso) documentation")]), and simulation or analysis tools (e.g., Batfish). It supports ingestion from production networks as well as from change candidates: for the latter, it exploits the NDT computing capabilities to generate the required KG layers starting from the new device configurations i.e. it uses Batfish to normalise vendor-specific configurations and compute routing/forwarding information.

The types of data ingested encompass OpenConfig (OC)-like
structured configuration and state, raw device configuration, CLI command outputs, and flow performance metrics.

Building Aether NDM Knowledge Graph
Constructing a full KG for every network snapshot may be resource-intensive and often unnecessary. To optimize, Aether allows on-demand ingestion: only essential layers are built initially, and original input data is stored separately. Additional layers are generated as needed for specific verifications or queries and merged to the existing KG. The *database-adapter* merges new layers into the existing KG with per-layer granularity, avoiding duplication.

NDM schema API for agents
The NDM Query Agent requires precise and unambiguous information about the structure and semantics of the Knowledge Graph (KG). Public OpenConfig documentation, while useful, is often too broad, may include unused modules, and does not reflect Aether-specific extensions.
To enable the agent to construct correct and efficient queries, the NDT
provides a dedicated
schema API that exposes the structure of the KG, as well as the schema of each type of nodes and edges, with examples, descriptions, and example-queries tailored to the KG-database.

#### IV-B2 Aether NDT Tools

Aether Network Digital Twin provides a unified platform integrating multiple network verification and testing tools for comprehensive automated validation. It serves as the backbone of the Aether architecture, facilitating seamless interaction between generative AI agents and underlying network data and tools.
Aether NDT currently supports model-based verification (Batfish [[6](#bib.bib50 "Lessons from the evolution of the batfish configuration analysis tool")]) and simulation-based tools (Routenet [[33](#bib.bib61 "RouteNet: leveraging graph neural networks for network modeling and optimization in sdn")]), with emulation support planned. Each tool integrates through a standardized interface, allowing agents to invoke capabilities without understanding underlying complexities. The extensible design enables adding new tools while maintaining a consistent agent interface. Table [III](#S4.T3 "Table III ‣ IV-B Aether NDT ‣ IV Aether ‣ Aether: Network Validation Using Agentic AI and Digital Twin") summarizes the main verification capabilities.
The NDT maintains close integration with the Network Digital Map (NDM), which provides necessary context ensuring tools operate on accurate, up-to-date network state. The NDT fetches and transforms NDM data based on tool requirements and provides computing capabilities to enrich the network representation. For traffic SLA verification, two options are available—simulation-based (Perf-simulator) and GNN-based [[33](#bib.bib61 "RouteNet: leveraging graph neural networks for network modeling and optimization in sdn")]—allowing selection based on scenario requirements (accuracy vs. scalability).

Tool Exposure and Execution.
Tools are exposed to agents via a Model Context Protocol (MCP) server, which provides input schemas and tool descriptions templated into the LLM context with tool-specific tokens. Tool descriptions are based on underlying tool documentation (e.g., Batfish) and modified for agent comprehension and NDT abstractions.
The test executor agent leverages NDT verification capabilities to implement test plans. It selects appropriate verifications based on requirements, uses the NDM Query Agent to gather necessary information (e.g., device IP addresses), executes verifications via the NDT, and retrieves results for analysis.
For Batfish-based verifications, the NDT translates agent input into Batfish-specific parameters and normalizes results. MTU consistency verification directly queries the NDM-KG for link MTU values. SLA verification involves multiple steps: simulating per-flow traffic matrices based on demand models (stored in NDM-KG), running the selected tool (NS-3 or Routenet) to evaluate flow performance (loss, delay), and comparing results against SLA requirements (also in NDM-KG).

Git-like Workflow.
The NDT uses snapshots as consistent network views at specific points in time, identified by UUIDs analogous to git commits. Production evolves along a ”main” branch, with snapshots created for Pull Requests to validate changes before merging.
The layered KG structure enables efficient conflict resolution through per-layer evaluation using computed digests (hashes) per device and layer. Only affected layers require re-validation when conflicts occur, minimizing overhead. Layer dependencies (e.g., ACL changes affecting routing) ensure dependent layers are re-evaluated when parent layers change.
Figure [5](#S4.F5 "Figure 5 ‣ IV-B2 Aether NDT Tools ‣ IV-B Aether NDT ‣ IV Aether ‣ Aether: Network Validation Using Agentic AI and Digital Twin") illustrates this: Snapshot 1 applies change Δ\Delta1 to layers A and B, passes verification, and merges. Snapshot 2 applies Δ\Delta2 to independent layer C and merges successfully. Snapshot 3 applies Δ\Delta3 to layer B, fails verification, is corrected to Δ\Delta3’ and passes, but requires rebase when production advances to Snapshot 4 with conflicting layer B changes.
The NDT exposes git-like APIs for fetching snapshots, forking, updating with change candidates, running verifications (including comparisons), and handling conflicts/rebases, enabling automated end-to-end change validation mirroring familiar git workflows.

![Refer to caption](2604.18233v1/x5.png)


Figure 5: NDT workflow to manage snapshots changes.

## V Aether Implementation

Agents – Aether leverages state-of-the-art agentic protocols defined by emerging bodies [[20](#bib.bib7 "Agentic ai foundation (aaif): advancing agentic ai together."), [21](#bib.bib6 "AGNTCY project: building infrastructure for the internet of agents.")] to ensure interoperability and standard compliance. Agents are implemented in Python using the A2A SDK [[19](#bib.bib73 "Agent-to-agent (a2a) protocol specification v1.0")] and LlamaIndex [[22](#bib.bib75 "LlamaIndex: a data framework for llm applications")], utilizing the ReAct reasoning loop for tool orchestration. All agents use gpt-4o (Azure OpenAI); initial experiments with smaller models revealed limitations in tool utilization and schema adherence.

Communication relies on the A2A protocol over the SLIM (Secure Low-latency Interactive Messaging) [[13](#bib.bib40 "IETF draft-mpsb-agntcy-slim-00, secure low-latency interactive messaging")] layer. The Assistant Agent orchestrates specialized agents while supporting direct peer-to-peer interactions (e.g., Test Planner querying NDM Query agent). NDT tools are exposed through an MCP (Model Context Protocol) server [[24](#bib.bib76 "Model context protocol (mcp) specification")], decoupling tool lifecycle from agent logic.

NDT – Aether NDT is implemented in Go (REST APIs for agents, gRPC for NDM integration). The NDM uses Python-based source adapters and KG builder with ArangoDB for graph storage and operations, exposing gRPC APIs for ingestion and updates. Verification capabilities are exposed to agents via MCP server with tool descriptions and schemas.

NDT Tools – We extended Batfish for IPv6 support, SRv6 locator origination, multiple ISIS processes per VRF (IOS-XR), intra-ISIS redistribution, and prefix summarization.

For simulation-based performance analysis, we integrated two tools: a custom flow-level simulator built on NS-3, and RouteNet for ML-based performance prediction—both extracting topology and traffic demands from the NDM. Our simulation workflow reconstructs topologies and traffic from NDT layers, executes multiple runs, and aggregates metrics—establishing a reusable pattern that extends to emulation workflows with containerized network instances.

Diffy [[14](#bib.bib81 "Diffy: data-driven bug finding for configurations")] was adapted for differential anomaly detection across snapshots, applied to NDM-generated JSON configurations with anomaly-to-configuration mapping.

Deployment and scalability – All components deploy via HELM/Docker in Kubernetes for lifecycle management and scaling. NDT introduces a thin dispatching layer with low overhead relative to verification resource consumption – crucial for decoupling large configurations from agent context and uniformizing API queries.

NDM scaling relies on ArangoDB for both ingestion and querying. For ingestion, leveraging existing network orchestrators (e.g., NSO [[7](#bib.bib85 "Cisco network services orchestrator (nso) documentation")] in our production use cases) enables efficient data collection and pre-normalization at scale, avoiding the need to poll individual devices directly.

## VI Evaluation methodology

| Scenario | Problem | Layer | Context | Verification |
| --- | --- | --- | --- | --- |
| S1. Router Maintenance | Backup path error | L3 Routing | Maintenance | Model + Differential |
| S2. Firewall Update | Policy violation | L3/L4 Security | Evolution | Model + Differential |
| S3. ACL Refactoring | Equivalence failure | L3/L4 Security | Refactoring | Model + Invariant |
| S4. MTU Consistency | Device mismatch | L1 Physical | Maintenance | Cross-device |
| S5. VLAN Migration | Multi-device coordination | L2/L3 | Migration | Multi-device |
| S6. ISP Link Migration | SLA violation | Cross-layer | Migration | Compositional |
| S7. IS-IS Redistribution | Control plane loop | L3 Control | Evolution | Model + Convergence |
| S8. Route Summarization | Forwarding blackhole | L3 Control | Migration | Differential |

Table IV: Network Change Validation Scenarios

We evaluate Aether agentic network change validation system through two complementary approaches: (1) a benchmark suite of network change scenarios designed to cover common operational tasks and failure modes; (2) operational case studies based on real-world ISP production incidents.

To the best of our knowledge, this paper is the first to attempt a systematic assessment of agentic AI contributions to network change validation and lack of publicly available datasets makes a comparison with NetCov[[15](#bib.bib63 "Real time network policy checking using header space analysis")]/RELA[[43](#bib.bib48 "Relational network verification")] not possible.

To allow future comparison, we define an evaluation methodology which we will publicly release along with scenarios, datasets and ground truth built by human experts.

### VI-A Network Change scenarios

Our benchmark dataset includes 88 network change scenarios (Table [IV](#S6.T4 "Table IV ‣ VI Evaluation methodology ‣ Aether: Network Validation Using Agentic AI and Digital Twin")) spanning a range of operational tasks (router maintenance, policy updates, topology migrations) and complex failure modes (protocol logic errors, cross-layer interactions, latent path defects). The scenarios are selected based on two key criteria: *operational relevance*—focusing on common and critical failure types observed in production networks; and *diagnostic diversity*—ensuring coverage across different validation techniques and network layers.
  
Operational Relevance.Three types of failures are covered:

(1) Policy misconfigurations (S1, S2, S3): ACL and firewall errors are the largest category of connectivity failures in large-scale cloud providers and remain pervasive in enterprise networks due to frequent policy evolution [[4](#bib.bib72 "Network verification 2.0")]. We include scenarios testing unintended side-effects of rule additions (S1), collateral damage from policy updates (S2), and semantic equivalence violations during refactoring (S3).

(2) IGP logic errors (S7, S8): While BGP misconfigurations are well-studied causes of Internet outages [[23](#bib.bib55 "Understanding bgp misconfiguration")], errors within Interior Gateway Protocols represent a critical yet under-examined failure domain. We address this gap with scenarios for control-plane loops from IS-IS redistribution (S7) and forwarding blackholes from route summarization (S8)—subtle protocol-specific bugs that evade generic reachability tests.

(3) Latent path defects (S1): Production networks commonly contain dormant failures in backup paths that remain undetected until failover events [[28](#bib.bib56 "Why do internet services fail, and what can be done about it?")]. Our router maintenance scenario targets proactive validation of rarely-exercised paths before production activation.

### VI-B Evaluation Datasets

We evaluate Aether agents first individually, then end to end in terms of agentic workflow. To this aim and in the absence of public datasets, Aether evaluation datasets are curated by a network expert with generative AI assistance: for each network scenario expert-generated input and ground truth output are defined. The test matrix consists of: (i) one input per scenario, (ii) three LLM-generated natural language input variations to test robustness to natural language phrasing, (iii) one correct and one problematic change candidates, and (iv) 1010 independent runs on all combinations to assess consistency.

For the NDM query agent specifically, the evaluation dataset includes 5050 questions LLM-generated from knowledge graph data related to the considered network scenarios covering all KG layers (Interfaces, IP settings, Routing/forwarding, ACL, device configuration). Each question is tested along with three prompt variations across 1010 independent runs.

### VI-C Evaluation Metrics

Aether’s agentic performance is quantified by the evaluation metrics in Table [V](#S6.T5 "Table V ‣ VI-C Evaluation Metrics ‣ VI Evaluation methodology ‣ Aether: Network Validation Using Agentic AI and Digital Twin"):
(1) Change candidate classification precision or simply Precision, measuring the ability of the system to correctly validate a change, where T​PTP (True Positives) are faulty changes that the system blocks (at least one test fails) and F​PFP (False Positives) are valid changes that are blocked (at least one test fails).
Higher precision indicates better diagnostic capability in identifying real issues while avoiding false alarms;
Similarly, we define (2) Main Error classification precision, the metric that measures the ability of the system to detect the main problem in a bad change candidate: a change is considered correctly diagnosed only if the test that can catch the main problem fails for a faulty change (T​PTP) and succeeds for a valid change (T​NTN);
(3) Error Detection, measuring the ability of the system to detect broken changes, where T​NTN (True Negatives) are valid changes that go through (all tests pass); (4) Time to Answer, the average time taken by Aether to produce a response.
For the real-world scenarios, we further explore the intermediate test plan quality by defining RG​TR\_{GT} as the set of ground-truth validation requirements and Tg​e​nT\_{gen} as the set of agent-generated tests. We measure:
(5) Coverage as the proportion of requirements satisfied by at least one test (denoted Rc​o​vR\_{cov});
(6) Efficiency as the ratio of useful tests, defining Tr​e​l​e​v​a​n​tT\_{relevant} for tests mapping to valid requirements (thus filtering out hallucinations); and
(7) Redundancy quantifying how many generated tests target the same intent.

Finally, for the single-agent evaluation we define:
(8) Correctness, assessed using GEval within the Deepeval framework [[8](#bib.bib78 "DeepEval: the llm evaluation framework")], which allows defining specific scoring criteria for the LLM judge: agents’ output is compared against the ground truth and instructions are provided to the judge to focus on the facts and score based on the criteria reported in Figure [6](#S7.F6 "Figure 6 ‣ VII-A Single Agent Assessment ‣ VII Evaluation ‣ Aether: Network Validation Using Agentic AI and Digital Twin"); (9) Robustness, quantifying the agent’s sensitivity to input variations, calculated based on σ\sigma, the standard deviation of correctness scores across test variations and μ\mu, the mean correctness score (i.e. a robustness score of 1.0 indicates perfect consistency); and (10) Consistency, measuring stability across repeated runs under identical conditions, also derived from correctness variance.

| Metric | Formula | Description |
| --- | --- | --- |
| Precision | T​PT​P+F​P\frac{TP}{TP+FP} | Change candidate classification |
| Error Detection | T​PT​P+F​N\frac{TP}{TP+FN} | Faulty candidates detection |
| Time to Answer | Average (sec) | Execution time |
| Coverage | |Rc​o​v|/|RG​T||R\_{cov}|\penalty 10000\ /\penalty 10000\ |R\_{GT}| | Expert requirements met |
| Efficiency | |Tr​e​l​e​v​a​n​t|/|Tg​e​n||T\_{relevant}|/|T\_{gen}| | Ratio of useful tests |
| Redundancy | 1−|Rc​o​v|/|Tr​e​l​e​v​a​n​t|1-|R\_{cov}|/|T\_{relevant}| | Duplication/overlap |
| Correctness | LLM score ∈[0,1]\in[0,1] | Alignment with ground truth |
| Robustness | 1−σμ1-\frac{\sigma}{\mu} (variations) | Stability across prompts |
| Consistency | 1−σμ1-\frac{\sigma}{\mu} (runs) | Stability across runs |

Table V: Evaluation Metrics

## VII Evaluation

We report now on the evaluation of Aether:
individual agents (Sec. [VII-A](#S7.SS1 "VII-A Single Agent Assessment ‣ VII Evaluation ‣ Aether: Network Validation Using Agentic AI and Digital Twin")), then end-to-end system (Sec. [VII-B](#S7.SS2 "VII-B End-to-end performance ‣ VII Evaluation ‣ Aether: Network Validation Using Agentic AI and Digital Twin")).

### VII-A Single Agent Assessment

Figure [6](#S7.F6 "Figure 6 ‣ VII-A Single Agent Assessment ‣ VII Evaluation ‣ Aether: Network Validation Using Agentic AI and Digital Twin") reports the correctness score averaged over each test across all scenarios, with thresholds defined in the LLM-as-a-Judge (LaaJ) prompt.
The average correctness score is always higher than the correctness threshold 0.70.7, indicating Aether agents provide correct answers with only minor inaccuracies or missing non-critical information.
The NDM Query agent shows the highest average correctness with complete answers in most cases. However, a small subset of challenging queries causes the majority of failures, particularly those requiring deep OpenConfig structure knowledge and networking concepts (import/export routing policies, BGP reflection, static routes, ACL specifics). The data schema offers multiple expression paths for the same concept, and the agent often picks the option lacking KG data without exploring alternatives. Improvements can be obtained by enhancing query exploration, memory-based learning, or populating alternative paths at ingestion time. Other error sources include wrong attribute selection and logic errors.
The Test Executor agent’s main failure mode is misuse of NDT tool parameters, suggesting API simplification could help. Despite occasional mistakes, the agent performs correctly in most scenarios.
The Impact Assessment agent occasionally misses information due to task generality, though it provides good device and risk overviews. User interaction and ticket updates can clarify missing information.
The Test Planner agent shows satisfactory correctness, with core plans matching ground truth while occasionally missing tests for less common issues or including unnecessary tests.
The evaluation focuses on NetOps agents and does not consider in isolation the Assistant Agent, given that its primary function is to interface with the user and coordinate other agents. Its performance is assessed in the end-to-end scenarios.

Table [VI](#S7.T6 "Table VI ‣ VII-A Single Agent Assessment ‣ VII Evaluation ‣ Aether: Network Validation Using Agentic AI and Digital Twin") summarizes average Consistency, Robustness, and Time to Answer across scenarios. Overall values are high, indicating stable answers across runs and prompt variations. The Test Executor shows lowest consistency due to: (1) ground truth listing only one valid solution when multiple exist, and (2) NDT parameter misuse causing drastic score decreases when tests unexpectedly fail.
Average response times are acceptable at under two minutes for most agents. The Test Execution Agent takes longer due to actual test execution in the NDT.

| Agent | Consistency | Robustness | Time to Answer |
| --- | --- | --- | --- |
| NDM Query | 83.3 | 82.2 | 12.6 |
| Test Executor | 73.8 | 92.2 | 89.0 |
| Impact | 78.0 | 93.7 | 46.7 |
| Test Plan | 83.7 | 95.1 | 46.8 |

Table VI: Single agent evaluation.

![Refer to caption](2604.18233v1/x6.png)


Figure 6: Single agent correctness.

### VII-B End-to-end performance

In this section we evaluate the ability of Aether to properly validate a change candidate (Precision) and more specifically to block broken changes (Error Detection).
Table [VII](#S7.T7 "Table VII ‣ VII-B End-to-end performance ‣ VII Evaluation ‣ Aether: Network Validation Using Agentic AI and Digital Twin") reports the per-scenario Error Detection and Precision as well as the average results across all scenarios. Overall, Aether is able to block 94%94\% of the broken changes (Error Detection = 0.94) and to provide 0.64 precision in validating the outcome of the change candidate.
When focusing on the detection of the main problem instead, the precision increases from 0.64 to 0.89 (Main Error Precision): the test plan is quite broad in covering different aspects of the change, leading to some false positives, especially when the tests require data not fully supported or available in the NDM. These are normally not related to the main problem introduced in the broken changes, hence the higher Main Error Precision.
Overall, the results show that Aether can accurately detect the most relevant and critical problems, enabling streamlined network change validation. The user remains in the loop and may validate Aether’s actions by analyzing the detailed final report and updating the ITSM ticket to improve test plan and verifications.
Guardrails, agent monitoring as well as improving the robustness of the NDM Query Agent and extending the NDM data coverage are the next steps towards making Aether more autonomous and production-grade.

| Scenario | Error | Precision | Time to |
| --- | --- | --- | --- |
| n. | Detection | All - Main Error | Answer |
| Scenario 1 | 0.6 | 0.67 - 0.78 | 245 |
| Scenario 2 | 0.9 | 0.56 - 0.7 | 163 |
| Scenario 3 | 1.0 | 0.62 - 1 | 269 |
| Scenario 4 | 1.0 | 0.62 - 0.83 | 158 |
| Scenario 5 | 1.0 | 0.56 - 0.8 | 239 |
| Scenario 6 | 1.0 | 0.69 - 1.0 | 187 |
| Scenario 7 | 1.0 | 0.56 - 1.0 | 251 |
| Scenario 8 | 1.0 | 0.83 - 1.0 | 273 |
| Overall | 0.94 | 0.64 - 0.89 | 223 |

Table VII: End-to-end evaluation.

## VIII Real-World Network use cases

This section validates Aether’s practical utility on real-world networks from a major ISP. We deployed Aether on a laboratory replica of the ISP’s production environment—scaled in device count but preserving all architectural patterns, protocol interactions, and policy complexity. The test network includes 2525 routers across CORE, Aggregation, and Metro layers, with 277277 IPv4/IPv6 addresses, 263263 VRFs across 613613 instances, and 7676 ACL lists containing 274274 rules—totaling over 30,00030,000 lines of production-equivalent configuration.

We evaluate Aether on two real past incidents caused by faulty change candidates. Unlike synthetic benchmarks, these involve production-type topologies, real vendor configurations (Cisco IOS-XR), and subtle protocol interactions. Ground truth is established by network experts with incident post-mortem input.

Scenario 1: IS-IS Redistribution Loop. Bidirectional route redistribution between two IS-IS domains used metric- type internal, causing redistributed routes to be re-imported into their originating domain, creating routing loops. The configuration bypassed loop prevention by treating redistributed routes as native IS-IS routes. Ground truth includes end-to-end IPv6 connectivity verification, validation of standard metric configurations to
prevent loops, and confirmation of active IS-IS redistribution.

Scenario 2: SRv6 Prefix Summarization Blackhole. IPv6 prefix summarization was migrated between aggregation routers at L1/L2 boundaries. The same summary prefix was configured on a new router with different backing prefixes. Core routers load-balanced via ECMP, but 5050% of flows were blackholed at the new aggregation router, which lacked backing routes.
Ground truth includes verification of summarized route advertisements, negative assertions for suppressed specific routes, and regression testing for unrelated traffic flows.
Evaluation metrics are reported in Table [VIII](#S9.T8 "Table VIII ‣ IX Discussion ‣ Aether: Network Validation Using Agentic AI and Digital Twin").

Error Detection Accuracy – Both scenarios achieve high detection (100100%): bad candidates are consistently rejected. Precision ranges from 57% (Scenario 1) to 90% (Scenario 2). The lower precision reflects conservative agent behavior, flagging ambiguous behaviors as risks.

Despite variable precision, 100% coverage of expert requirements combined with granular multi-test verification ensures robustness: even if one check fails, others covering the same requirement detect the bug. Tool-based verifications significantly outperformed query-based approaches; the majority of precision issues stemmed from the NDM Query Agent either misforging complex AQL queries or misinterpreting results. The SRv6 blackhole case was particularly challenging due to overlapping prefixes and partial summarization.

Test Plan Coverage – Aether achieves 100% cumulative coverage, proving its capability to generate all required tests. In individual executions, consistency remains high with an average coverage of 91.7% for IS-IS and 95.6% for SRv6 scenarios. The primary omissions are specific test types: the end-to-end connectivity check is missed in 25% of IS-IS runs, and the negative routing assertion (verifying routes are not advertised) is missed in 11% of SRv6 runs. 96-98% of these tests were relevant to specific requirements, showing the ability of the agent also to avoid wasting resources on useless tests, or more likely to fail in case of hallucinations. Finally, redundancy ranging from 1.7% to 24.6%, proved to be mostly due to the generation of multiple granular verification of the same property from different perspective (eg. verify summary prefix present, and verify specific prefixes not present), allowing more robustness but at the same time being more challenging for precision.

Time to Answer. The average execution time per run was short (approx. 6 minutes), significantly faster than manual lab testing, and validating the workflow’s suitability for CI/CD pipelines. In our experiments, 55% of the total runtime was dedicated to tool execution—an incompressible cost of network verification. Agentic reasoning accounted for the remaining 45%: the Test Planner (2%) and Test Executor (12%) remain lightweight, while the most complex tasks are handled by the Impact Assessment agent (18%) and the NDM Query agent, which dominates the compute budget (68%). Despite having room for improvement (eg. query generation; parallel test execution), this confirms that the agentic component remains scalable – it grows with test plan size instead – making the approach a viable replacement for slow manual procedures.

## IX Discussion

Our evaluation demonstrates that agentic AI with NDT effectively streamlines network change validation. Aether detects up to 94% of issues, including intent deviations missed by traditional automation, and achieves 100% detection of critical protocol-interaction issues in real-world ISP validations.
The key takeaways are summarized below:

Intent-Aware Verification. Standard CI/CD pipelines face an efficiency dilemma: full-matrix checks are prohibitive, while sparse tests miss intent-specific failures. In Scenario 2 (SRv6 migration), generic ECMP tests would pass 50% of the time despite blackholes. Aether’s intent-aware approach generated precise validations—verifying exact summary prefixes and absence of specific routes—demonstrating differential verification impossible without understanding the change’s purpose. Agents effectively leveraged model-based tools like Batfish, extending their expressiveness through reasoning and composition.

Synergy of Tools and Reasoning. Effective verification relies on complementary strengths of NDM and NDT tools. The Knowledge Graph provides granular configuration data inaccessible to broad verification tools, yet direct verification proved fragile due to OpenConfig schema complexity. Conversely, NDT tools are essential for verifying complex states like loops or reachability. Future improvements require enhancing agent graph interaction through specialized skills and schema enforcement.

Knowledge as an Artifact. Specialized knowledge injection is critical. Protocol interactions, use-case patterns, and optimization guidelines must be explicit ”skills” or memory. Building such a knowledge base is a high-value artifact, essential for modern network complexity that general-purpose models cannot derive from zero-shot reasoning.

Operational Value. The ISP use case evaluation confirms Aether’s role as a safety layer. With 100% bug detection and high expert coverage, it catches critical failures bypassing standard controls. The 73% global precision indicates acceptable overhead and provides a robust safety net. Future work will focus on multi-agent collaboration and memory-based learning to improve efficiency.

Evaluation Rigor. Ground truth creation remains challenging, requiring iterative expert validation. Aether demonstrates that agents can autonomously execute routine validations, freeing operators for strategic oversight, though quantitative measures for diagnostic accuracy and expanded benchmarks remain needed.

|  |  |  |
| --- | --- | --- |
| Metric | IS-IS Loop | SRv6 Blackhole |
| Error Detection | 100% | 100% |
| Precision | 57% | 90% |
| Main Error Precision | 100% | 100% |
| Coverage | 91.7% | 95.6% |
| Efficiency | 98.3% | 95.7% |
| Redundancy | 1.7% | 24.6% |
| Time to Answer | 414s | 395s |

Table VIII: Real-world use cases evaluation

## X Conclusions

In this paper we present Aether, an agentic system combining five NetOps-specialized generative AI agents with a multi-functional Network Digital Twin for network change validation. We evaluate Aether on 88 network change scenarios and 22 operational use cases in a major ISP’s network, demonstrating promising results in error detection, coverage, consistency, and robustness compared to traditional CI/CD pipelines.
Aether’s effectiveness stems from its neuro-symbolic design: LLM-based agents generate and orchestrate verification workflows while reasoning over ambiguous inputs, paired with structured network representation and specialized verification tools from the NDT. This separation enables flexible intent interpretation with correct and consistent validation execution.

This work makes three primary contributions: (1) a neuro-symbolic architecture bridging natural language intent with formal verification through LLMs, Knowledge Graphs, and verification tools; (2) a comprehensive evaluation methodology assessing individual agent and system performance (Correctness, Consistency, Robustness, Error Detection, Precision), complemented by a thorough assessment of test plan quality in production environments (Coverage, Efficiency, Redundancy); and (3) empirical evidence from 8 synthetic and 2 production scenarios that intent-aware validation detects logic errors missed by regular CI/CD pipelines, and fully leverages a wide range of tooling including model-based verifiers, achieving 94%94\% Error Detection and 64%64\% Precision in synthetic benchmarks, and 100%100\% detection with 73%73\% Precision in production environments.
Aether demonstrates practical value for autonomous network operations, serving as an intelligent assistant for routine validation while operators focus on strategic decisions. Future work will focus on: (1) protocol-specific knowledge injection via skills and memory-based learning; (2) multi-agent collaboration with autonomous agent workflows; (3) feedback loops from production failures; and (4) operational tooling for false positive management.

## References

* [1]
  ArangoDB GmbH (2025)
  ArangoDB: the native multi-model database.
  Note: https://www.arangodb.comOpen-source native multi-model database supporting graph, document, and key–value data models
  Cited by: [§IV-B1](#S4.SS2.SSS1.p2.1 "IV-B1 Network Digital Map ‣ IV-B Aether NDT ‣ IV Aether ‣ Aether: Network Validation Using Agentic AI and Digital Twin").
* [2]
  R. Beckett, A. Gupta, R. Mahajan, and D. Walker (2017-08)
  A general approach to network configuration verification.
  In Proc. of SIGCOMM ’17, Los Angeles, CA, USA, August 21-25, 2017,
  Proc. of SIGCOMM ’17, Los Angeles, CA, USA, August 21-25, 2017 edition,  pp. 14.
  Cited by: [§II-B](#S2.SS2.p1.1 "II-B Formal network verification ‣ II Related work ‣ Aether: Network Validation Using Agentic AI and Digital Twin").
* [3]
  R. Beckett and R. Mahajan
  Putting network verification to good use.
  In Proc. of ACM HotNets ’19, Princeton, NJ, USA, November 13-15, 2019,
  Cited by: [§II-B](#S2.SS2.p1.1 "II-B Formal network verification ‣ II Related work ‣ Aether: Network Validation Using Agentic AI and Digital Twin").
* [4]
  R. Beckett and R. Mahajan (2020-12)
  Network verification 2.0.
  Note: https://netverify.fun/network-verification-2-0/
  Cited by: [§III-A](#S3.SS1.p1.1 "III-A Motivation and Design Principles ‣ III Problem Statement ‣ Aether: Network Validation Using Agentic AI and Digital Twin"),
  [§VI-A](#S6.SS1.p2.1 "VI-A Network Change scenarios ‣ VI Evaluation methodology ‣ Aether: Network Validation Using Agentic AI and Digital Twin").
* [5]
  N. Bjørner and K. Jayaraman (2015)
  Checking cloud contracts in microsoft azure.
  In Distributed Computing and Internet Technology, R. Natarajan, G. Barua, and M. R. Patra (Eds.),
  Cham,  pp. 21–32.
  External Links: ISBN 978-3-319-14977-6
  Cited by: [§II-B](#S2.SS2.p1.1 "II-B Formal network verification ‣ II Related work ‣ Aether: Network Validation Using Agentic AI and Digital Twin").
* [6]
  M. Brown, A. Fogel, D. Halperin, V. Heorhiadi, R. Mahajan, and T. Millstein (2023)
  Lessons from the evolution of the batfish configuration analysis tool.
  In Proceedings of the ACM SIGCOMM 2023 Conference,
  ACM SIGCOMM ’23, New York, NY, USA,  pp. 122–135.
  External Links: ISBN 9798400702365
  Cited by: [§II-B](#S2.SS2.p3.1 "II-B Formal network verification ‣ II Related work ‣ Aether: Network Validation Using Agentic AI and Digital Twin"),
  [§IV-B2](#S4.SS2.SSS2.p1.1 "IV-B2 Aether NDT Tools ‣ IV-B Aether NDT ‣ IV Aether ‣ Aether: Network Validation Using Agentic AI and Digital Twin").
* [7]
  Cisco Systems, Inc. (2024)
  Cisco network services orchestrator (nso) documentation.
   Cisco Systems, Inc..
  Note: Version 6.x
  External Links: [Link](https://developer.cisco.com/docs/nso/)
  Cited by: [§IV-B1](#S4.SS2.SSS1.p2.1 "IV-B1 Network Digital Map ‣ IV-B Aether NDT ‣ IV Aether ‣ Aether: Network Validation Using Agentic AI and Digital Twin"),
  [§V](#S5.p8.1 "V Aether Implementation ‣ Aether: Network Validation Using Agentic AI and Digital Twin").
* [8]
  DeepEval: the llm evaluation framework
  Note: Version 3.8.1. Open-source evaluation framework for LLMs.
  External Links: [Link](https://github.com/confident-ai/deepeval)
  Cited by: [§VI-C](#S6.SS3.p2.2 "VI-C Evaluation Metrics ‣ VI Evaluation methodology ‣ Aether: Network Validation Using Agentic AI and Digital Twin").
* [9]
  R. Enns, M. Bjorklund, J. Schoenwaelder, and A. Bierman (2011)
  RFC 6241: network configuration protocol (netconf).
   RFC Editor.
  Cited by: [§IV-B1](#S4.SS2.SSS1.p2.1 "IV-B1 Network Digital Map ‣ IV-B Aether NDT ‣ IV Aether ‣ Aether: Network Validation Using Agentic AI and Digital Twin").
* [10]
  GNS3 Development Team (2025)
  GNS3 network emulator.
  Note: https://www.gns3.comGraphical network simulator supporting real and virtual devices
  Cited by: [§II-C](#S2.SS3.p4.1 "II-C Network Digital Twins ‣ II Related work ‣ Aether: Network Validation Using Agentic AI and Digital Twin").
* [11]
  O. W. Group
  OpenConfig data model.
  Note: https://www.openconfig.net/Accessed: 2025-10-06
  Cited by: [§IV-B1](#S4.SS2.SSS1.p1.1 "IV-B1 Network Digital Map ‣ IV-B Aether NDT ‣ IV Aether ‣ Aether: Network Validation Using Agentic AI and Digital Twin").
* [12]
  O. Havel, B. Claise, O.G.D. Dios, and T. Graf (2025-10)
  IETF nmog internet draft - simap: concept, requirements, and use cases.
  Note: https://datatracker.ietf.org/doc/draft-ietf-nmop-simap-concept/
  Cited by: [§II-C](#S2.SS3.p6.1 "II-C Network Digital Twins ‣ II Related work ‣ Aether: Network Validation Using Agentic AI and Digital Twin").
* [13]
  IETF AGNTCY Working Group (2024)
  IETF draft-mpsb-agntcy-slim-00, secure low-latency interactive messaging.
  Note: https://datatracker.ietf.org/doc/draft-mpsb-agntcy-slim/
  Cited by: [§V](#S5.p2.1 "V Aether Implementation ‣ Aether: Network Validation Using Agentic AI and Digital Twin").
* [14]
  S. K. R. Kakarla, F. Y. Yan, and R. Beckett (2024)
  Diffy: data-driven bug finding for configurations.
  Proceedings of the ACM on Programming Languages 8 (PLDI),  pp. 199–222.
  Cited by: [Table III](#S4.T3.1.11.10.3.1 "In IV-B Aether NDT ‣ IV Aether ‣ Aether: Network Validation Using Agentic AI and Digital Twin"),
  [§V](#S5.p6.1 "V Aether Implementation ‣ Aether: Network Validation Using Agentic AI and Digital Twin").
* [15]
  P. Kazemian, M. Chang, H. Zeng, G. Varghese, and N. McKeown (2013)
  Real time network policy checking using header space analysis.
  In Proceedings of the 10th USENIX Symposium on Networked Systems Design and Implementation (NSDI),
  Lombard, IL, USA.
  Cited by: [§II-B](#S2.SS2.p1.1 "II-B Formal network verification ‣ II Related work ‣ Aether: Network Validation Using Agentic AI and Digital Twin"),
  [§II-B](#S2.SS2.p2.1 "II-B Formal network verification ‣ II Related work ‣ Aether: Network Validation Using Agentic AI and Digital Twin"),
  [§VI](#S6.p2.1 "VI Evaluation methodology ‣ Aether: Network Validation Using Agentic AI and Digital Twin").
* [16]
  P. Kazemian, G. Varghese, and N. McKeown (2012-04)
  Header space analysis: static checking for networks.
  In 9th USENIX Symposium on Networked Systems Design and Implementation (NSDI 12),
  San Jose, CA,  pp. 113–126.
  External Links: ISBN 978-931971-92-8,
  [Link](https://www.usenix.org/conference/nsdi12/technical-sessions/presentation/kazemian)
  Cited by: [§II-B](#S2.SS2.p1.1 "II-B Formal network verification ‣ II Related work ‣ Aether: Network Validation Using Agentic AI and Digital Twin").
* [17]
  A. Krentsel, O. Ye, A. Tafoya, X. Ma, S. Ratnasamy, and A. Shaikh (2025-11)
  Towards accessible model-free verification.
  In Proceedings of the 24th ACM Workshop on Hot Topics in Networks (HotNets ’25),
  College Park, MD, USA.
  External Links: [Document](https://dx.doi.org/10.1145/3772356.3772380),
  [Link](https://conferences.sigcomm.org/hotnets/2025/papers/hotnets25-final13.pdf)
  Cited by: [§II-B](#S2.SS2.p2.1 "II-B Formal network verification ‣ II Related work ‣ Aether: Network Validation Using Agentic AI and Digital Twin").
* [18]
  Y. Li, Z. Wang, and X. e. al. Yin (2018-04)
  Efficient network configuration verification using optimized datalog.
   pp. 1–2.
  External Links: [Document](https://dx.doi.org/10.1109/INFCOMW.2018.8406876)
  Cited by: [§II-B](#S2.SS2.p1.1 "II-B Formal network verification ‣ II Related work ‣ Aether: Network Validation Using Agentic AI and Digital Twin").
* [19]
  Linux Foundation (2025)
  Agent-to-agent (a2a) protocol specification v1.0.
  Note: Accessed: 2026-02-02
  External Links: [Link](https://a2a-protocol.org/latest/specification/)
  Cited by: [§V](#S5.p1.1 "V Aether Implementation ‣ Aether: Network Validation Using Agentic AI and Digital Twin").
* [20]
  Linux Foundation (2025-12)
  Agentic ai foundation (aaif): advancing agentic ai together..
  Note: https://aaif.io/AAIF establishes neutral, open governance for agentic AI standards including MCP, goose, and AGENTS.md
  Cited by: [§V](#S5.p1.1 "V Aether Implementation ‣ Aether: Network Validation Using Agentic AI and Digital Twin").
* [21]
  Linux Foundation (2025-07)
  AGNTCY project: building infrastructure for the internet of agents..
  Note: https://agntcy.org/
  Cited by: [§V](#S5.p1.1 "V Aether Implementation ‣ Aether: Network Validation Using Agentic AI and Digital Twin").
* [22]
  J. Liu and L. Contributors (2023)
  LlamaIndex: a data framework for llm applications.
  Note: https://github.com/run-llama/llama\_index
  Cited by: [§V](#S5.p1.1 "V Aether Implementation ‣ Aether: Network Validation Using Agentic AI and Digital Twin").
* [23]
  R. Mahajan, D. Wetherall, and T. Anderson (2002)
  Understanding bgp misconfiguration.
  In Proceedings of the 2002 Conference on Applications, Technologies, Architectures, and Protocols for Computer Communications (SIGCOMM ’02),
  New York, NY, USA,  pp. 3–16.
  External Links: [Document](https://dx.doi.org/10.1145/633025.633027)
  Cited by: [§VI-A](#S6.SS1.p3.1 "VI-A Network Change scenarios ‣ VI Evaluation methodology ‣ Aether: Network Validation Using Agentic AI and Digital Twin").
* [24]
  Model Context Protocol Community (2025)
  Model context protocol (mcp) specification.
  Note: Accessed: 2026-02-02
  External Links: [Link](https://modelcontextprotocol.io/specification/)
  Cited by: [§V](#S5.p2.1 "V Aether Implementation ‣ Aether: Network Validation Using Agentic AI and Digital Twin").
* [25]
  A. Mohanty, T. Robinson, and A. O’Farrell (2024-07)
  The hidden costs of downtime:the $400b problem facing the global 2000.
  Note: https://www.oxfordeconomics.com/resource/the-hidden-costs-of-downtime-the-400b-problem-facing-the-global-2000/
  Cited by: [§I](#S1.p1.1 "I Introduction ‣ Aether: Network Validation Using Agentic AI and Digital Twin").
* [26]
  R. Mondal, A. Tang, R. Beckett, T. Millstein, and G. Varghese (2023)
  What do llms need to synthesize correct router configurations?.
  In Proc. of ACM HotNets, Cambridge, MA, USA, November 28-29, 2023,
   pp. 189–195.
  Cited by: [§II-D](#S2.SS4.p1.1 "II-D Agentic Verification ‣ II Related work ‣ Aether: Network Validation Using Agentic AI and Digital Twin").
* [27]
  Z. Namrud, K. Sarda, and M. e. al. Litoiu (2024)
  Kubeplaybook: a repository of ansible playbooks for kubernetes auto-remediation with llms.
  In Companion of the 15th ACM/SPEC International Conference on Performance Engineering,
   pp. 57–61.
  Cited by: [§II-D](#S2.SS4.p1.1 "II-D Agentic Verification ‣ II Related work ‣ Aether: Network Validation Using Agentic AI and Digital Twin").
* [28]
  D. Oppenheimer, A. Ganapathi, and D. A. Patterson (2003)
  Why do internet services fail, and what can be done about it?.
  In Proceedings of the 4th USENIX Symposium on Internet Technologies and Systems (USITS ’03),
   pp. 1–16.
  Cited by: [§VI-A](#S6.SS1.p4.1 "VI-A Network Change scenarios ‣ VI Evaluation methodology ‣ Aether: Network Validation Using Agentic AI and Digital Twin").
* [29]
  Puppet, Inc. (2024)
  Puppet: infrastructure automation for security and compliance.
  Note: https://puppet.com/Configuration management and automation platform
  Cited by: [§II-A](#S2.SS1.p1.1 "II-A NetDevOps Automation ‣ II Related work ‣ Aether: Network Validation Using Agentic AI and Digital Twin").
* [30]
  S. M. Raza, R. Minerva, N. Crespi, M. Alvi, M. Herath, and H. Dutta (2025)
  A comprehensive survey of network digital twin architecture, capabilities, challenges, and requirements for edge-cloud continuum.
  Computer Communications.
  External Links: [Link](https://hal.science/hal-04986834)
  Cited by: [§II-C](#S2.SS3.p6.1 "II-C Network Digital Twins ‣ II Related work ‣ Aether: Network Validation Using Agentic AI and Digital Twin").
* [31]
  Red Hat, Inc. (2024)
  Ansible: simple, agentless it automation.
  Note: https://www.ansible.com/Open-source automation tool for configuration management and application deployment
  Cited by: [§II-A](#S2.SS1.p1.1 "II-A NetDevOps Automation ‣ II Related work ‣ Aether: Network Validation Using Agentic AI and Digital Twin").
* [32]
  G. F. Riley and T. R. Henderson (2010)
  The ns-3 network simulator.
  In Modeling and Tools for Network Simulation,
  Berlin, Heidelberg,  pp. 15–34.
  External Links: [Document](https://dx.doi.org/10.1007/978-3-642-12331-3%5F2)
  Cited by: [§II-C](#S2.SS3.p3.1 "II-C Network Digital Twins ‣ II Related work ‣ Aether: Network Validation Using Agentic AI and Digital Twin").
* [33]
  K. Rusek, J. Suárez-Varela, A. Mestres, P. Barlet-Ros, and A. Cabellos-Aparicio (2020)
  RouteNet: leveraging graph neural networks for network modeling and optimization in sdn.
  In IEEE Journal on Selected Areas in Communications,
  Vol. 38,  pp. 2260–2270.
  External Links: [Document](https://dx.doi.org/10.1109/JSAC.2020.3000405)
  Cited by: [§II-C](#S2.SS3.p3.1 "II-C Network Digital Twins ‣ II Related work ‣ Aether: Network Validation Using Agentic AI and Digital Twin"),
  [§IV-B2](#S4.SS2.SSS2.p1.1 "IV-B2 Aether NDT Tools ‣ IV-B Aether NDT ‣ IV Aether ‣ Aether: Network Validation Using Agentic AI and Digital Twin"),
  [Table III](#S4.T3.1.10.9.3.1 "In IV-B Aether NDT ‣ IV Aether ‣ Aether: Network Validation Using Agentic AI and Digital Twin").
* [34]
  P. Sahoo, S. Pujar, G. Nalawade, R. Genhardt, L. Mandel, and L. Buratti (2024)
  Ansible lightspeed: a code generation service for it automation.
  In Proc. of IEEE/ACM International Conference on Automated Software Engineering,
   pp. 2148–2158.
  Cited by: [§II-D](#S2.SS4.p1.1 "II-D Agentic Verification ‣ II Related work ‣ Aether: Network Validation Using Agentic AI and Digital Twin").
* [35]
  Containerlab
  External Links: [Link](https://github.com/srl-labs/containerlab)
  Cited by: [§II-C](#S2.SS3.p4.1 "II-C Network Digital Twins ‣ II Related work ‣ Aether: Network Validation Using Agentic AI and Digital Twin").
* [36]
  B. Tian, J. Gao, and M. e. al. Liu (2021)
  Aquila: a practically usable verification system for production-scale programmable data planes.
  In Proc. of ACM SIGCOMM 2021,
  SIGCOMM ’21, New York, NY, USA,  pp. 17–32.
  External Links: ISBN 9781450383837
  Cited by: [§II-B](#S2.SS2.p1.1 "II-B Formal network verification ‣ II Related work ‣ Aether: Network Validation Using Agentic AI and Digital Twin").
* [37]
  TM Forum (2025)
  Digital twin for decision intelligence (dt4di): from strategy to implementation.
  Technical report
  Technical Report IG1307, TM Forum.
  External Links: [Link](https://www.tmforum.org/resources/introductory-guide-whitepaper/dt4di-from-strategy-to-implementation-v3-0-0-ig1307/)
  Cited by: [§II-C](#S2.SS3.p7.1 "II-C Network Digital Twins ‣ II Related work ‣ Aether: Network Validation Using Agentic AI and Digital Twin").
* [38]
  Twin EU Consortium (2024-01)
  Developing a concept of pan-european digital twin of the electricity system.
  Note: https://twineu.net/
  Cited by: [§II-C](#S2.SS3.p7.1 "II-C Network Digital Twins ‣ II Related work ‣ Aether: Network Validation Using Agentic AI and Digital Twin").
* [39]
  A. Varga and R. Hornig (2008)
  An overview of the omnet++ simulation environment.
  Proceedings of the 1st International Conference on Simulation Tools and Techniques (Simutools),  pp. 1–10.
  External Links: [Document](https://dx.doi.org/10.4108/ICST.SIMUTOOLS2008.3027)
  Cited by: [§II-C](#S2.SS3.p3.1 "II-C Network Digital Twins ‣ II Related work ‣ Aether: Network Validation Using Agentic AI and Digital Twin").
* [40]
  K. Wang, C. Zhao, J. Chu, Y. Shi, J. Lu, B. Lyu, S. Zhu, P. Cheng, and J. Chen (2024-10)
  LFVeri: network configuration verification for virtual private cloud networks.
  IEEE/ACM Trans. Netw. 32 (6),  pp. 5475–5490.
  External Links: ISSN 1063-6692,
  [Link](https://doi.org/10.1109/TNET.2024.3469386),
  [Document](https://dx.doi.org/10.1109/TNET.2024.3469386)
  Cited by: [§II-B](#S2.SS2.p1.1 "II-B Formal network verification ‣ II Related work ‣ Aether: Network Validation Using Agentic AI and Digital Twin").
* [41]
  H. Xu, Z. Kincaid, R. Mahajan, and D. Walker (2026-01)
  Network change validation with relational netkat.
  Proc. ACM Program. Lang. 10 (POPL).
  Cited by: [§II-C](#S2.SS3.p5.1 "II-C Network Digital Twins ‣ II Related work ‣ Aether: Network Validation Using Agentic AI and Digital Twin").
* [42]
  H. Xu, Z. Kincaid, R. Mahajan, and D. Walker (2026)
  Network change validation with relational netkat.
  Proceedings of the ACM on Programming Languages 10 (POPL),  pp. 384–412.
  Cited by: [§II-B](#S2.SS2.p3.1 "II-B Formal network verification ‣ II Related work ‣ Aether: Network Validation Using Agentic AI and Digital Twin").
* [43]
  X. Xu, Y. Yuan, Z. Kincaid, A. Krishnamurthy, R. Mahajan, D. Walker, and E. Zhai (2024)
  Relational network verification.
  In Proceedings of the ACM SIGCOMM 2024 Conference,
  ACM SIGCOMM ’24, New York, NY, USA,  pp. 213–227.
  External Links: ISBN 9798400706141,
  [Link](https://doi.org/10.1145/3651890.3672238),
  [Document](https://dx.doi.org/10.1145/3651890.3672238)
  Cited by: [§II-B](#S2.SS2.p1.1 "II-B Formal network verification ‣ II Related work ‣ Aether: Network Validation Using Agentic AI and Digital Twin"),
  [§II-B](#S2.SS2.p3.1 "II-B Formal network verification ‣ II Related work ‣ Aether: Network Validation Using Agentic AI and Digital Twin"),
  [§VI](#S6.p2.1 "VI Evaluation methodology ‣ Aether: Network Validation Using Agentic AI and Digital Twin").
* [44]
  S. Yao, J. Zhao, D. Yu, N. Du, I. Shafran, K. Narasimhan, and Y. Cao (2023)
  ReAct: synergizing reasoning and acting in language models.
  External Links: 2210.03629,
  [Link](https://arxiv.org/abs/2210.03629)
  Cited by: [§IV-A](#S4.SS1.p3.1 "IV-A Aether Agents ‣ IV Aether ‣ Aether: Network Validation Using Agentic AI and Digital Twin").
* [45]
  F. Ye, D. Yu, E. Zhai, and H. H. e. al. Liu (2020)
  Accuracy, scalability, coverage: a practical configuration verifier on a global wan.
  In Proc. of ACM SIGCOMM 2020,
  SIGCOMM ’20, New York, NY, USA,  pp. 599–614.
  External Links: ISBN 9781450379557,
  [Document](https://dx.doi.org/10.1145/3387514.3406217)
  Cited by: [§II-B](#S2.SS2.p1.1 "II-B Formal network verification ‣ II Related work ‣ Aether: Network Validation Using Agentic AI and Digital Twin").
* [46]
  N. Zheng, M. Liu, and E. e. al. Zhai (2022)
  Meissa: scalable network testing for programmable data planes.
  In Proc. of ACM SIGCOMM 2022,
  SIGCOMM ’22, New York, NY, USA,  pp. 350–364.
  External Links: ISBN 9781450394208
  Cited by: [§II-B](#S2.SS2.p1.1 "II-B Formal network verification ‣ II Related work ‣ Aether: Network Validation Using Agentic AI and Digital Twin").

Experimental support, please
[view the build logs](./2604.18233v1/__stdout.txt)
for errors. Generated by
[L
A
T
E
xml
![[LOGO]](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAsAAAAOCAYAAAD5YeaVAAAAAXNSR0IArs4c6QAAAAZiS0dEAP8A/wD/oL2nkwAAAAlwSFlzAAALEwAACxMBAJqcGAAAAAd0SU1FB9wKExQZLWTEaOUAAAAddEVYdENvbW1lbnQAQ3JlYXRlZCB3aXRoIFRoZSBHSU1Q72QlbgAAAdpJREFUKM9tkL+L2nAARz9fPZNCKFapUn8kyI0e4iRHSR1Kb8ng0lJw6FYHFwv2LwhOpcWxTjeUunYqOmqd6hEoRDhtDWdA8ApRYsSUCDHNt5ul13vz4w0vWCgUnnEc975arX6ORqN3VqtVZbfbTQC4uEHANM3jSqXymFI6yWazP2KxWAXAL9zCUa1Wy2tXVxheKA9YNoR8Pt+aTqe4FVVVvz05O6MBhqUIBGk8Hn8HAOVy+T+XLJfLS4ZhTiRJgqIoVBRFIoric47jPnmeB1mW/9rr9ZpSSn3Lsmir1fJZlqWlUonKsvwWwD8ymc/nXwVBeLjf7xEKhdBut9Hr9WgmkyGEkJwsy5eHG5vN5g0AKIoCAEgkEkin0wQAfN9/cXPdheu6P33fBwB4ngcAcByHJpPJl+fn54mD3Gg0NrquXxeLRQAAwzAYj8cwTZPwPH9/sVg8PXweDAauqqr2cDjEer1GJBLBZDJBs9mE4zjwfZ85lAGg2+06hmGgXq+j3+/DsixYlgVN03a9Xu8jgCNCyIegIAgx13Vfd7vdu+FweG8YRkjXdWy329+dTgeSJD3ieZ7RNO0VAXAPwDEAO5VKndi2fWrb9jWl9Esul6PZbDY9Go1OZ7PZ9z/lyuD3OozU2wAAAABJRU5ErkJggg==)](https://math.nist.gov/~BMiller/LaTeXML/).

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile
support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the
methods listed below:

* Click the "Report Issue" (

  ) button, located in the page header.

**Tip:** You can select the relevant text first, to include it in your report.

Our team has already identified [the following issues](https://github.com/arXiv/html_feedback/issues). We appreciate your time reviewing and reporting rendering errors we
may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability
should not be a barrier to accessing research. Thank you for your continued support in championing open access for
all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a [list of packages that need conversion](https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML), and welcome [developer contributions](https://github.com/brucemiller/LaTeXML/issues).

BETA