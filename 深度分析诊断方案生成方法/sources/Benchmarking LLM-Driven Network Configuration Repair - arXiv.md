> Source: https://arxiv.org/html/2604.22513v1

Benchmarking LLM-Driven Network Configuration Repair






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

[Back to Abstract](/abs/2604.22513v1 "Back to abstract page")

[Download PDF](/pdf/2604.22513v1 "Download PDF")

1. [Abstract.](#abstract1 "In Benchmarking LLM-Driven Network Configuration Repair")
2. [1 Introduction](#S1 "In Benchmarking LLM-Driven Network Configuration Repair")
3. [2 Overview](#S2 "In Benchmarking LLM-Driven Network Configuration Repair")
   1. [2.1 Design Goals](#S2.SS1 "In 2. Overview ‣ Benchmarking LLM-Driven Network Configuration Repair")
   2. [2.2 Key Insights](#S2.SS2 "In 2. Overview ‣ Benchmarking LLM-Driven Network Configuration Repair")
   3. [2.3 Cornetto](#S2.SS3 "In 2. Overview ‣ Benchmarking LLM-Driven Network Configuration Repair")
4. [3 Dataset Generation Pipeline](#S3 "In Benchmarking LLM-Driven Network Configuration Repair")
   1. [3.1 Task Definition](#S3.SS1 "In 3. Dataset Generation Pipeline ‣ Benchmarking LLM-Driven Network Configuration Repair")
   2. [3.2 Effective Task Space Representation](#S3.SS2 "In 3. Dataset Generation Pipeline ‣ Benchmarking LLM-Driven Network Configuration Repair")
   3. [3.3 Scenario Generation](#S3.SS3 "In 3. Dataset Generation Pipeline ‣ Benchmarking LLM-Driven Network Configuration Repair")
   4. [3.4 Dataset Statistics](#S3.SS4 "In 3. Dataset Generation Pipeline ‣ Benchmarking LLM-Driven Network Configuration Repair")
5. [4 Evaluation Framework](#S4 "In Benchmarking LLM-Driven Network Configuration Repair")
   1. [4.1 LLM-Benchmark Interface](#S4.SS1 "In 4. Evaluation Framework ‣ Benchmarking LLM-Driven Network Configuration Repair")
   2. [4.2 Differential Data Plane Analysis](#S4.SS2 "In 4. Evaluation Framework ‣ Benchmarking LLM-Driven Network Configuration Repair")
   3. [4.3 Diagnosis Evaluator](#S4.SS3 "In 4. Evaluation Framework ‣ Benchmarking LLM-Driven Network Configuration Repair")
6. [5 Experimental Setup](#S5 "In Benchmarking LLM-Driven Network Configuration Repair")
7. [6 Evaluation](#S6 "In Benchmarking LLM-Driven Network Configuration Repair")
8. [7 Related Work](#S7 "In Benchmarking LLM-Driven Network Configuration Repair")
9. [8 Discussion and Limitations](#S8 "In Benchmarking LLM-Driven Network Configuration Repair")
10. [9 Conclusion](#S9 "In Benchmarking LLM-Driven Network Configuration Repair")
11. [References](#bib "In Benchmarking LLM-Driven Network Configuration Repair")
12. [A Fault Library](#A1 "In Benchmarking LLM-Driven Network Configuration Repair")
13. [B Additional Results](#A2 "In Benchmarking LLM-Driven Network Configuration Repair")

[License: CC BY 4.0](https://info.arxiv.org/help/license/index.html#licenses-available)

arXiv:2604.22513v1 [cs.NI] 24 Apr 2026

# Benchmarking LLM-Driven Network Configuration Repair

Ioannis Protogeros, Rufat Asadli, Benjamin Hoffman, Laurent Vanbever
ETH ZürichZürichSwitzerland
[iprotogeros, rasadli, bhoffman, lvanbever@ethz.ch](2604.22513v1/mailto:iprotogeros,%20rasadli,%20bhoffman,%20lvanbever@ethz.ch)

(2026)

###### Abstract.

There is a rapidly growing interest in using Large Language Models (LLMs) to automate complex network operations, but their reliable adoption requires rigorous assessment of their effectiveness and safety.
Existing benchmarks do not address whether LLMs can successfully resolve errors in large-scale, interdependent network configurations without introducing new disruptions. Developing such a benchmark is challenging: scenarios must be diverse and increasingly complex, yet their evaluation must be straightforward and meaningful.

In this paper, we present Cornetto, the first benchmark to evaluate LLM-driven network configuration repair functionally and at scale. Cornetto features a generation pipeline that synthesizes representative and plausible misconfiguration scenarios, coupled with an evaluation framework that uses formal verification to assess functional correctness of proposed fixes against ground-truth specifications.

Using this pipeline, we synthesize a dataset of 231 problems for fixing configurations across varying network topologies (20–754 nodes) and diverse protocols. We evaluate 9 state-of-the-art LLMs and find that while they show promise, they often introduce regressions and their performance degrades at scale. Our results indicate that reliable LLM-powered network automation requires integrating LLMs into iterative workflows guided by formal verification.

††copyright: none††journalyear: 2026††doi: XXXXXXX.XXXXXXX††conference: Make sure to enter the correct
conference title from your rights confirmation email; ; ††isbn: 978-1-4503-XXXX-X/2018/06

## 1. Introduction

Network correctness, while paramount, remains extremely difficult to achieve and maintain. While network verification and synthesis (Fogel et al., [2015](#bib.bib10 "A general approach to network configuration analysis"); Beckett et al., [2017a](#bib.bib27 "A general approach to network configuration verification"); Khurshid et al., [2013](#bib.bib26 "VeriFlow: verifying Network-Wide invariants in real time"); El-Hassany et al., [2018](#bib.bib5 "NetComplete: Practical Network-Wide Configuration Synthesis with Autocompletion"); Beckett et al., [2016](#bib.bib3 "Don’t mind the gap: bridging network-wide objectives and device-level configurations")) have made significant strides towards eliminating human-induced misconfigurations, they are not a silver bullet. In particular, their adoption is hindered by limited protocol coverage and inaccuracies in modelling complex network behaviour (Birkner et al., [2021](#bib.bib2 "Metha: network verifiers need to be correct too!"); Krentsel et al., [2025](#bib.bib19 "Towards accessible model-free verification")).

More recently, there has been a surge of interest in leveraging Large Language Models (LLMs) as a more flexible approach to automating network operations. Hyperscalers have already begun deploying LLM-based frameworks that assist with such tasks, including ByteDance’s NetAssistant (Wang et al., [2024b](#bib.bib22 "NetAssistant: dialogue based network diagnosis in data center networks")), Alibaba’s BiAn (Wang et al., [2025a](#bib.bib20 "Towards llm-based failure localization in production-scale networks")), and Meta’s Confucius (Wang et al., [2025b](#bib.bib21 "Intent-driven network management with multi-agent llms: the confucius framework")). On the one hand, with their impressive capabilities across domains (Google DeepMind, [2025](#bib.bib28 "Gemini 3 Pro"); OpenAI, [2025](#bib.bib29 "GPT-5 System Card")), LLMs appear promising for facilitating complex workflows that are bottlenecked by human reasoning. On the other hand, as probabilistic models, they remain prone to errors and hallucinations (Bender et al., [2021](#bib.bib37 "On the dangers of stochastic parrots: can language models be too big?"); Ji et al., [2023](#bib.bib36 "Survey of hallucination in natural language generation")), precluding their adoption for managing critical infrastructure.

The tension between the tremendous potential for automating network operations and their associated risks makes principled evaluation indispensable. Doing so requires designing a benchmark that challenges LLM reasoning with complex and diverse configuration tasks, alongside with a proper methodology to assess their capabilities on said tasks.

Constructing such a diverse benchmark with plausible, well-posed problems is nontrivial. Unlike domains such as mathematics or software engineering, where benchmarks can leverage vast publicly available datasets, network configurations are proprietary and sensitive. Consequently, we must synthesize the dataset. Crucially, this synthesis cannot be random; to ensure relevance, test cases must reflect the complexities that operators face in production networks, including large-scale configurations with feature and protocol dependencies. Lastly, the evaluation must verify the functional correctness of solutions, scalably and automatically.

The gap in LLM network configuration benchmarking. LLMs’ progress outpaces our abilities to evaluate them effectively
in fields that require deep domain expertise and complex reasoning.
Despite growing interest in using LLMs for network operations, we still lack benchmarks to evaluate their performance and explore strategies to improve them.

While previous works such as NetConfEval (Wang et al., [2024a](#bib.bib14 "NetConfEval: can llms facilitate network configuration?")) and NetLLMBench (Aykurt et al., [2024](#bib.bib18 "NetLLMBench: a benchmark framework for large language models in network configuration tasks")) have established baselines for evaluating LLMs on network configuration tasks, they are severely constrained in scale and complexity relative to the capabilities of current models. Additionally, their proposed evaluation methods rely on proxy metrics (e.g., textual similarity or ping-test validation) that do not guarantee the functional correctness of a configuration. A more recent benchmark, NIKA (Wang et al., [2025c](#bib.bib17 "A network arena for benchmarking ai agents on network troubleshooting")), evaluates the diagnostic capabilities of LLM Agents in dynamic, emulated network environments. Yet, it does not support the evaluation of proposed fixes for network faults.

Consequently, evaluating the performance of LLMs in repairing realistic, large-scale network configurations correctly and safely remains underexplored.

Cornetto: Correct & safe configuration repair. To address this gap, we introduce Cornetto, a benchmark that evaluates end-to-end configuration repair in representative, large-scale networks.111The idea behind the system was presented in a previously-accepted poster (Protogeros and Vanbever, [2025](#bib.bib49 "Continual benchmarking of llm-based systems on networking operations")). The task of resolving misconfigurations encapsulates critical challenges in network operations: understanding the interplay among interdependent features and protocols, and bridging the semantic gap between low-level configurations and high-level intent (Beckett et al., [2016](#bib.bib3 "Don’t mind the gap: bridging network-wide objectives and device-level configurations")). To capture this complexity, Cornetto employs a generation pipeline that produces syntactically valid configurations subject to logical and semantic constraints, thereby ensuring structural coherence and consistency. We use this pipeline to synthesize 231 challenging misconfiguration scenarios spanning diverse protocols and scales, where the intended network state is unambiguously defined.

To evaluate correctness and safety, Cornetto formally verifies the data plane of the reconfigured network against ground-truth specifications. This ensures that success depends on functional correctness, requiring restoration of intended behaviour. The introduction of new bugs is penalised based on the extent of disruption to previously functional behaviour. Crucially, we also evaluate the diagnostic reasoning (localization and root-cause analysis) that led to the fix.

Key findings. Our evaluation of 9 LLMs reveals that while current models can diagnose and fix faults (restoring up to 60% of network state on average), they cannot reliably act as monolithic solvers—the best-performing model successfully resolved only 25% of scenarios. We find that performance degrades in large-scale settings with noisy data, and models often propose partial or unsafe solutions. These insights indicate that reliable automation requires integrating LLMs into systems that filter noisy data, preserve necessary context, and iteratively verify the safety of repairs before application.

Key contributions. Our summarized contributions are:

* •

  We formulate the problem of automated configuration repair, enabling the quantification of functional disruption caused by misconfigurations and the assessment of fix correctness and safety.
* •

  We develop a scenario generation pipeline that synthesizes logically valid network configurations for any topology and systematically injects faults across diverse protocols.
* •

  Using this pipeline, we curate a dataset of 231 misconfiguration scenarios of varying scale and complexity by optimizing fault diversity within a minimal number of scenarios.
* •

  We design a verification-based evaluation pipeline that utilizes data-plane analysis to automatically infer ground-truth specifications and assess the functional correctness and safety of fixes.
* •

  We evaluate 9 state-of-the-art LLMs on Cornetto and comprehensively analyze their performance, examining the effects of scenario complexity on reconfiguration correctness and safety.

Outlook. We will open source Cornetto to the community as an extensible and modular framework. 222available at <https://github.com/nsg-ethz/cornetto> Cornetto enables the generation of more challenging tasks, and its architecture supports the evaluation of any LLM-based system, including advanced scaffolds such as Retrieval-Augmented Generation (RAG) systems and agentic setups. By providing a standardized testbed, Cornetto contributes to the continual evaluation of LLMs on configuration repair.

## 2. Overview

Cornetto is a benchmark for assessing LLMs’ capabilities in automated network configuration repair. A Cornetto scenario simulates an end-to-end troubleshooting task: Given a misconfigured network state (including topology and configuration files) and a set of high-level intents (e.g., Reachability between A and B), the model must localize and diagnose the misconfiguration, and propose a correct reconfiguration that restores the network’s intended function.

![Refer to caption](2604.22513v1/x1.png)


Figure 1. Cornetto architecture. (I) The Dataset Generation pipeline coordinates the scenarios to ensure a diverse and complex test suite, generates sensible configurations and misconfigurations, and provides a standardized problem definition. (II) The Evaluation Framework enables automated and meaningful evaluation of the created scenarios by validating the reconfigured network’s behaviour against ground-truth specifications.

Cornetto comprises two pipelines. First, the Dataset Generation focuses on creating realistic, diverse, and complex misconfiguration scenarios. Second, the Evaluation Framework provides an automated system that enables meaningful evaluation of proposed solutions against intended network behaviour.

This section outlines Cornetto design goals, the key insights required to address emerging challenges, and the system components that implement these solutions.

### 2.1. Design Goals

Diversity and Complexity. To gain meaningful insights into the performance of LLMs,
the benchmark must cover a wide variety of scenarios.
This includes growing topology scales,
features across diverse protocols, and complex fault scenarios
that reflect real-world issues. At the same time, the benchmark should remain small enough to keep its execution feasible without incurring high costs.

Additionally, the complexity of these scenarios should be sufficient to challenge models’ reasoning capabilities and ensure resilience against benchmark saturation (Hardt, [2025](#bib.bib48 "The emerging science of machine learning benchmarks")). A key challenge lies in identifying the dimensions that affect a scenario’s complexity.

Sensible problems. Scenarios must be sensible so that a model’s performance reliably proxies its real-world applicability. However, actual network-wide configurations and historical bug data are proprietary and hence unavailable. Therefore, the system must generate scenarios synthetically. This includes base configurations that are syntactically and semantically valid, maintain internal coherence, and respect dependencies between protocols.

Well-posed problems. Despite the scenarios’ complexity, the evaluation of their proposed solutions
must be straightforward and provide concrete, interpretable metrics for success, efficiency and safety. This requires the concrete formulation of a misconfiguration scenario, including the definition and quantification of success metrics.

Meaningful evaluation.
Evaluation should take into account the emergent network behaviour,
rather than relying solely on the comparison of the configuration files. This
requires analyzing the network’s data plane behaviour post-fix, and comparing it
against a specification that captures the intended behaviour. Furthermore, all the different facets of troubleshooting should be assessed, including localization and diagnosis abilities.

### 2.2. Key Insights

Efficiently representing a massive task space (Enabling diversity). The space of all possible network configurations and misconfigurations is prohibitively large. To create a representative benchmark that can be run on a minimal compute budget, we identify the key dimensions that affect scenario difficulty (e.g., topology size, fault types) and employ sampling strategies and combinatorial testing techniques (Kuhn et al., [2004](#bib.bib11 "Software fault interactions and implications for software testing")) to efficiently cover them. This enables Cornetto to test LLMs against a diverse suite of scenarios without requiring thousands of redundant test cases.

Producing sensible configurations with grammar-based generation and semantic constraints (Providing sensible problems). For a benchmark to effectively evaluate LLM performance on resolving misconfigurations, it must contain sensible configurations that can exist in reality. This means that configurations must be syntactically and semantically valid and realize a plausible intent. To achieve that, we first define a high-level logical network plan that specifies its functionality. Then, we synthesize configs using a grammar-based approach and enable features iteratively and contextually. This approach ensures that semantic constraints (e.g., that a prefix list is defined before it is referenced) and feature dependencies are respected.

Formulating concrete problems through differential data plane analysis (Providing well-posed problems). We cannot proxy the effect of a misconfiguration by a textual diff; a perturbation of just a few Lines of Code (LoC) may cause significant disruptions in the network, while a larger change can be functionally benign. To rigorously define the problem, Cornetto employs differential data-plane analysis. We compare the forwarding behaviour of the faulty network against the “golden” reference state using Batfish (Fogel et al., [2015](#bib.bib10 "A general approach to network configuration analysis")). The resulting set of behavioural differences (e.g., “A cannot reach B”) yields a concrete, symptom-based problem description.

Evaluating functional correctness and reasoning (Enabling meaningful evaluation). To automate evaluation, we treat the network’s functional requirements as a suite of “unit tests”.
We mine the specific data-plane properties (Reachability, Isolation, Waypointing) satisfied by the golden network (Birkner et al., [2020](#bib.bib1 "Config2Spec: mining network specifications from network configurations")) to create a ground-truth specification. A correct solution will produce a reconfigured network that restores the previously violated predicates (i.e., it is efficacious), without violating any previously satisfied predicates (i.e., it is safe). Crucially, we also evaluate the intermediate steps of a model’s reasoning (localization, root-cause diagnosis) to gain a holistic view into its troubleshooting effectiveness.

### 2.3. Cornetto

Cornetto comprises two primary pipelines, as shown in Fig. [1](#S2.F1 "Figure 1 ‣ 2. Overview ‣ Benchmarking LLM-Driven Network Configuration Repair"). The Dataset Generation (§3) pipeline accepts a topology collection and a fault library to generate a minimal yet diverse suite of misconfiguration scenarios, along with their problem formulations. With the generated scenarios, the Evaluation Framework (§4) assesses repair capabilities by verifying configurations against a ground-truth specification.

Scenario coordination and creation (§[3.2](#S3.SS2 "3.2. Effective Task Space Representation ‣ 3. Dataset Generation Pipeline ‣ Benchmarking LLM-Driven Network Configuration Repair")). To drive fault generation, we implement a diverse fault library, where each fault is a function that slightly perturbs a configuration to break or alter the functionality of a protocol. The scenario coordinator utilizes this library and the topology collection to orchestrate the creation of diverse scenarios, ensuring representation across all topology scales and fault combinations. For each scenario, the system generates a valid configuration that enables the specific protocols and features targeted by the fault. This process yields two network states per scenario: the Golden (healthy) state and the Broken (faulty) states.

Data plane analysis and problem formulation (§[3.3](#S3.SS3 "3.3. Scenario Generation ‣ 3. Dataset Generation Pipeline ‣ Benchmarking LLM-Driven Network Configuration Repair")). The system invokes *Batfish* to simulate the forwarding behaviour for both the Golden and Broken states. It then distills the behaviour of the Golden network into a set of invariants, or predicates, which constitute the ground-truth specification. By verifying the Broken network state against this specification, the system identifies which specifications are violated. These violations are the “symptoms” that indicate the problem in network behaviour.

Benchmark testbed (§[4](#S4 "4. Evaluation Framework ‣ Benchmarking LLM-Driven Network Configuration Repair")). The testbed manages the interaction with the LLM-based system under test. The benchmarked system receives a description of the network problem created by the Dataset Generation pipeline. This description contains the network topology, the faulty configurations, and the violated specifications (symptoms). Cornetto tasks the model under test with a standard troubleshooting workflow: localizing the fault, diagnosing the root cause, and proposing a reconfiguration to restore intended behaviour.

The evaluation pipeline parses the proposed solution, simulates the new data plane, and compares the network state against the desired specification set. This process yields metrics for reconfiguration Efficacy (did the proposed reconfiguration fix the violations?) and Safety (did it introduce any new violations?), along with performance metrics for diagnosis and localization.

Output and results. For each test case, Cornetto generates a structured report primarily containing:

* •

  Fix Rate (Efficacy): The proportion of initially violated specifications that are successfully restored by the configuration
* •

  Regression Rate (Safety): Quantifies unintended side effects by measuring new violations introduced by the reconfiguration.

Additionally, the testbed evaluates diagnostic quality using both objective metrics (precision/recall on faulty devices for localization) and an LLM-as-a-Judge (Zheng et al., [2023](#bib.bib39 "Judging llm-as-a-judge with mt-bench and chatbot arena")) approach to assess provided textual diagnoses against ground-truth misconfigurations.

## 3. Dataset Generation Pipeline

The test suite of our benchmark must cover a wide variety of high-quality scenarios of varying complexity. Yet, it should include a minimal number of test cases so the research community can test their methods without incurring prohibitive LLM inference costs. In this section, we define the network configuration troubleshooting task space and show how to represent it effectively, constructing a benchmark that meets our design goals.

### 3.1. Task Definition

Formally, we define a Cornetto benchmark scenario as a tuple (T,Cgold,Cbroken,Φ)(T,C\_{\text{gold}},C\_{\text{broken}},\Phi), where:

* •

  TT represents the network topology (undirected graph of devices and links between interfaces).
* •

  CgoldC\_{\text{gold}} is the configuration at its “Golden” state.
* •

  CbrokenC\_{\text{broken}} is the faulty configuration that is derived from CgoldC\_{\text{gold}} by applying a fault function ff, so Cbroken=f​(Cgold)C\_{\text{broken}}=f(C\_{\text{gold}}).
* •

  Φ\Phi is the set of data plane specifications (or intent) that the Golden Configuration satisfies. We denote satisfaction as Cgold⊧ΦC\_{\text{gold}}\models\Phi. Since the forwarding plane of CbrokenC\_{\text{broken}} deviates from intended behaviour, it holds that Cbroken⊧̸ΦC\_{\text{broken}}\not\models\Phi.

#### Specifications

We define a specification ϕ∈Φ\phi\in\Phi as a boolean predicate that describes a property in the network’s forwarding behaviour. We consider four types of predicates that encompass the most common requirements about the network’s function (Birkner et al., [2020](#bib.bib1 "Config2Spec: mining network specifications from network configurations")):

* •

  Reachability(r,p): Traffic from router r can reach prefix p.
* •

  Isolation(r,p): Traffic from r cannot reach p.
* •

  Waypointing(r,p,w): Traffic from r destined to p always passes through router w.
* •

  LoadBalancing(r,p,n): Traffic from r destined to p is load-balanced across n paths.

#### Specification violations

The fault ff introduces a disruption in the data plane. We define the set 𝒱\mathcal{V} of violated specifications as the subset of specifications that are satisfied by CgoldC\_{\text{gold}} but violated by CbrokenC\_{\text{broken}}:

|  |  |  |
| --- | --- | --- |
|  | 𝒱={ϕ∈Φ∣Cbroken⊧̸ϕ}\mathcal{V}=\{\phi\in\Phi\mid C\_{\text{broken}}\not\models\phi\} |  |

#### The objective

The system under test’s task is twofold. Given the input tuple ℐ=(T,Cbroken,𝒱)\mathcal{I}=(T,C\_{\text{broken}},\mathcal{V}), it must:

* •

  Localize and Diagnose: Provide (i) a list of the misconfigured routers and (ii) a textual description of the faults in the network that correspond to the misconfiguration Δ​(Cgold,Cbroken)\Delta(C\_{\text{gold}},\allowbreak C\_{\text{broken}}).
* •

  Repair: Act as a repair function ℛ\mathcal{R} that produces a reconfiguration Cfix=ℛ​(ℐ)C\_{\text{fix}}=\mathcal{R}(\mathcal{I}) such that Cfix⊧ΦC\_{\text{fix}}\models\Phi.

### 3.2. Effective Task Space Representation

For a given topology set 𝒯\mathcal{T}, the theoretical space of benchmark scenarios is defined by all the configurations that could take the place of CgoldC\_{\text{gold}} and CbrokenC\_{\text{broken}}. If we consider both configs to be a part of a configuration space 𝒞\mathcal{C} that fits each topology, then the scenario space would be contained in 𝒯×𝒞×𝒞\mathcal{T}\times\mathcal{C}\times\mathcal{C}. This space is prohibitively large and dominated by unreasonable elements, i.e., random configuration pairs that cannot represent either operational networks or realistic misconfiguration scenarios. To construct a useful benchmark, we must restrict the space to a meaningful subset of scenarios and strategically represent it with minimal samples.

Benchmark diversity. Covering the entire task space is neither possible nor relevant to our goals. However, to ensure robust evaluation, the benchmark should challenge the tested systems across different complexity dimensions.

We identify the following controllable characteristics that are expected to critically affect the difficulty and nature of a misconfiguration scenario:

* •

  Topology scale: Varying the size of the network up to hundreds of nodes will
  stress-test the models’ ability to handle large inputs and identify the information that points to the issue.
* •

  Number of applied faults: Applying multiple simultaneous faults will challenge models with having to detect multiple independent root causes, potentially causing masking or compounding symptoms.
* •

  Fault types: Different faults from the library ℱ\mathcal{F} will cause different types of symptoms that will be more or less difficult to link to the root cause.

These three dimensions will be used to select the scenarios that will comprise the benchmark.

The fault library. To ensure the benchmark contains troubleshooting tasks across a wide array of misconfigurations, we curated a collection ℱ\mathcal{F} of 27 fault functions that target specific protocol functionalities. This fault library spans across the following dimensions that we expect to affect scenario complexity:

* •

  Protocols and features affected: The library includes faults that target features of eBGP, iBGP (incl. route reflection), OSPF and IS-IS (single and multi area), redistribution, ACLs, route-maps, and static routes
* •

  Configuration impact: From perturbing a single parameter (e.g., the subnet mask of an interface) to performing “organized” alterations like removing a route reflector functionality from a router.
* •

  Operational impact: Faults that disrupt a protocol’s functionality (e.g., mismatched remote-as numbers preventing BGP session establishment), and faults that only change the intent of the used feature (e.g., stripping an export policy)

Appendix [A](#A1 "Appendix A Fault Library ‣ Benchmarking LLM-Driven Network Configuration Repair") contains the comprehensive list of all faults.

Representative Sampling Strategy. To balance scenario diversity with a manageable test set size, we employ a sampling strategy centred on pairwise coverage (Kuhn et al., [2004](#bib.bib11 "Software fault interactions and implications for software testing")). Our goal is to generate complex scenarios with up to N=8N=8 simultaneous faults, where every possible pair of fault types appears together at least once. This ensures we test model performance on scenarios with varying disruptions and multi-root-cause failures.

#### 1. Fault selection procedure

We construct a compact collection of fault sets 𝒮\mathcal{S} by iteratively sampling from the fault library ℱ\mathcal{F} until 100% pairwise coverage is achieved. For each generation step:

1. (1)

   We randomly select a number k∈{2,…,8}k\in\{2,\dots,8\} of simultaneous faults to apply. This variation ensures the benchmark includes scenarios from few to many root causes.
2. (2)

   Select a subset Fs⊂ℱF\_{s}\subset\mathcal{F} of kk faults |Fs|=k|F\_{s}|=k that greedily maximizes the number of newly covered fault pairs
3. (3)

   Repeat this process until the set of applied scenarios covers 100% of feasible fault pairs.

This optimization yields a compact collection of 5050 distinct fault sets 𝒮={F1,F2,…​F50}\mathcal{S}=\{F\_{1},F\_{2},\dots F\_{50}\} that describe which faults are to be applied in each scenario. To this collection, we add all monosets of single faults (k=1k=1) to include each fault type individually.

#### 2. Topology selection

For the topology collection 𝒯\mathcal{T}, we use real-world topologies from the Topology Zoo (Knight et al., [2011](#bib.bib40 "The internet topology zoo")). To ensure these fault patterns are tested across varying scales, we stratify our topology dataset 𝒯\mathcal{T} into three tiers: Small (¡50 nodes), Medium (50–100 nodes), and Large (¿100 nodes).

For each generated fault set Fi∈𝒮F\_{i}\in\mathcal{S}, we instantiate the benchmark scenario by applying the faults to three distinct topologies, one randomly sampled from each tier. This yields a final dataset of 231 scenarios that cover diverse combinations of fault types across all scale tiers.

### 3.3. Scenario Generation

The scenario selection procedure described before yields for each scenario a descriptor (F,T)(F,T) with (i) the set of faults F⊂ℱF\subset\mathcal{F} and (ii) the topology of the network T∈𝒯T\in\mathcal{T}. We now describe the pipeline that synthesizes the configurations themselves and applies the fault functions to obtain the configurations CgoldC\_{\text{gold}} and CbrokenC\_{\text{broken}}.

To ensure the benchmark scenarios are plausible and useful, the generated configurations must satisfy two constraints:

* •

  The base configuration CgoldC\_{\text{gold}} must be syntactically and semantically valid. Crucially, the features that are enabled in the network must not exist vacuously (e.g. BGP processes without peers or unreferenced route-maps), but they must be structured to realize a functional intent within the network context.
* •

  The “broken” config CbrokenC\_{\text{broken}} must be derived from CgoldC\_{\text{gold}} after a perturbation that is *minimal*, so it can represent a plausible misconfiguration.

Existing synthesizers like NetComplete (El-Hassany et al., [2018](#bib.bib5 "NetComplete: Practical Network-Wide Configuration Synthesis with Autocompletion")) or Propane (Beckett et al., [2016](#bib.bib3 "Don’t mind the gap: bridging network-wide objectives and device-level configurations"), [2017b](#bib.bib4 "Network configuration synthesis with abstract topologies")) are ill-suited for this task because they optimize for a fundamentally different objective: finding *any* valid configuration that satisfies a specific high-level intent, often resulting in simple, uniform implementations. Our benchmark requires configurations that vary in protocols and specific, low-level configuration features. High-level intent is insufficient for this purpose, as a single intent (e.g., reachability) can be satisfied by many combinations of features. Therefore, we adopt a grammar-based generation approach building on Metha (Birkner et al., [2021](#bib.bib2 "Metha: network verifiers need to be correct too!")), allowing for the selection of features that the fault functions in ℱ\mathcal{F} can affect.

#### Configuration feature selection

Each fault function acts upon specific configuration features. But for the fault to be applicable, the appropriate ”attack surface” must exist in the first place. For instance, removing a route reflector requires that the AS is configured with route reflection clusters.

To ensure that generated configurations are operationally viable, we model the dependencies between network protocols. Network features are rarely independent; for example, testing a route-reflection fault requires the AS to support iBGP, which, in turn, relies on an underlying IGP (e.g., OSPF) for loopback reachability. We enforce these constraints during the generation phase: for each selected fault, the generator enables the target features and recursively satisfies all its prerequisite protocol dependencies.

#### Configuration generation

The syntactic and semantic validity of the “Golden” state configurations is critical for the realism and utility of the benchmark. While syntactic validity ensures the configuration can be parsed, semantic validity ensures the configuration is logically consistent. We enforce two types of semantic constraints, as stipulated in Metha:

* •

  Intra-device constraints: Dependencies within a single configuration file. For example, a BGP neighbour statement cannot apply a route-map that has not been defined, and an interface cannot be assigned to an OSPF area if the OSPF process is not active.
* •

  Inter-device constraints: Dependencies across the network. For example, two routers connected via a link must have IP addresses in the same subnet, and eBGP peers must have matching remote-as declarations.

To satisfy these, we construct a high-level logical plan of the network. This process is iterative and context-aware: First, we extend the physical topology with logical groupings to define the control plane hierarchy. We split the topology into ASes and assign OSPF/IS-IS areas to router interfaces according to the chosen IGP in each domain. We also define peering relationships, including iBGP full-meshes and route-reflection clusters. Then, we assign subnets to links and IP addresses to the interfaces on those links. Finally, additional resources are generated based on the selected features and their dependencies, as defined by the logical topology. For instance, BGP advertisements are generated strictly for subnets assigned to the router’s local interfaces.

Once the logical plan is defined, we render it using a template that follows a Context-Free Grammar for vendor-specific configurations (e.g., Cisco IOS). This part ensures the syntactical correctness of the produced configurations, and is decoupled from the process of enforcing semantic constraints (which are not context-free).

#### Fault injection

We apply the fault functions to the produced logical plan, so when it passes through the renderer, it results in the broken configuration CbrokenC\_{\text{broken}}. After these faults, the configurations may either violate semantic constraints (e.g., mismatched remote-as parameters) or remain semantically valid, only deviating from intended behaviour (e.g., changing a route-map action from permit to deny). In both cases, the specifications violated after fault injection are verified through data-plane analysis, ensuring that all faults induce a tangible change in forwarding behaviour.

### 3.4. Dataset Statistics

The resulting Cornetto dataset comprises 231 network misconfiguration scenarios across topologies with 20 to 754 nodes. Table [1](#S3.T1 "Table 1 ‣ 3.4. Dataset Statistics ‣ 3. Dataset Generation Pipeline ‣ Benchmarking LLM-Driven Network Configuration Repair") reports the key features of the scenarios. Notably, the network-wide configurations are large (¿16K lines of code on average), yet contain only a few lines actually affected by the fault. Consequently, solving Cornetto requires navigating massive, distributed configuration files to locate the few relevant lines that point to an issue.

At the same time, the actual change in the configuration is small and buried under the volume of code. The effect of a misconfiguration is not related to its textual difference either; most of the faults affect ¡1% of the total configuration lines, but may greatly affect the functionality of the network as shown in Fig. [2](#S3.F2 "Figure 2 ‣ 3.4. Dataset Statistics ‣ 3. Dataset Generation Pipeline ‣ Benchmarking LLM-Driven Network Configuration Repair"). We expect the varying levels of perturbations and symptoms to affect scenario difficulty.

Table 1. Cornetto spans diverse scales and misconfiguration severities.

|  | Metric | Mean | Max |
| --- | --- | --- | --- |
| Topology | Nodes (#) | 86.4 | 754 |
|  | Configuration lines (LoC) | 16.1K | 200.0K |
|  | Routes | 4.6K | 130.4K |
|  | Data plane predicates | 12.7K | 598.0K |
| Fault impact | Lines edited | 50.5 | 345 |
|  | Routers affected | 5.5 | 20 |
|  | Routes changed | 568.4 | 9.2K |
|  | Predicates changed | 1.5K | 38.4K |
| Impact (%) | LoC% changed | 0.44 | 5.93 |
|  | Routes% changed | 6.34 | 57.3 |
|  | Predicates% changed | 6.82 | 49.8 |

![Refer to caption](2604.22513v1/x2.png)


Figure 2. While configuration perturbations are minimal, disruption in network behaviour varies greatly across scenarios.

## 4. Evaluation Framework

To derive meaningful insights into the diagnostic capabilities of LLMs, the evaluation system must distil concrete, interpretable metrics that quantify the functional success of a solution. In this section, we delineate the Cornetto evaluation pipeline that enables automatic evaluation of proposed reconfigurations against the ground truth of the network’s data-plane behaviour.

### 4.1. LLM-Benchmark Interface

To enable testing and comparing different models and systems around them, we build a standardized interface that decouples evaluation logic from the specific solver. Hence, Cornetto can evaluate any proposed system that can generate a configuration CfixC\_{\text{fix}}. To carry out experiments across different models, we implement an evaluation framework that (i) builds a structured prompt containing the problem description to elicit a solution, and (ii) parses a model-generated patch to build the configuration CfixC\_{\text{fix}}.

#### Context Construction

To provide the necessary info to diagnose and fix the problem in the configuration, the system constructs a prompt containing three main information sources:

* •

  The physical topology TT
* •

  The list of violated specifications 𝒱\mathcal{V}
* •

  The faulty configuration files CbrokenC\_{\text{broken}}

A key challenge for the benchmarked system is handling the volume and sparsity of the available raw data; among thousands of configuration lines, only a very small subset points to the root cause in the network. At the same time, it is possible that network-wide configurations, along with the specifications and topology data, cannot fit within the LLMs’ context windows, and their performance is known to degrade well before that limit (Shi et al., [2023](#bib.bib13 "Large language models can be easily distracted by irrelevant context"); Liu et al., [2023](#bib.bib12 "Lost in the middle: how language models use long contexts")).

Consequently, handling the context constitutes a core experimental dimension (§[5](#S5 "5. Experimental Setup ‣ Benchmarking LLM-Driven Network Configuration Repair")). We define the system under test to include not only the generation model but also the context strategy, that is used to derive, filter, or retrieve relevant information from the available raw data (TT, CbrokenC\_{\text{broken}}, Φ\Phi, 𝒱\mathcal{V}).

For obtaining the solution, we prompt the models to output the following:

1. (1)

   A textual diagnosis, containing all the detected faults in the network configuration CbrokenC\_{\text{broken}}
2. (2)

   A list of all the routers that need to be reconfigured, and the needed reconfigurations to resolve the specification violations

#### Reconfiguration Parser

The raw text output of the model needs to be processed in order to apply the fixes and obtain the proposed reconfiguration CfixC\_{\text{fix}}. We decided against requiring Unix diff patches (Mackenzie et al., [2002](#bib.bib47 "Comparing and merging files with gnu diff and patch")), since they require precise line arithmetic, which language models famously struggle with (Glukhov et al., [2025](#bib.bib7 "Diff-xyz: a benchmark for evaluating diff understanding"); Jimenez et al., [2024](#bib.bib9 "SWE-bench: can language models resolve real-world github issues?")). Instead, following common practice in coding agents (Gauthier, [2023](#bib.bib8 "Aider: ai pair programming in your terminal")) that perform edit operations, we expect the answer to include, for each reconfigured file:

* •

  A search block, containing a snippet that is uniquely present in the configuration file
* •

  A replace block, containing the snippet that will replace the search block

Since unparseable output is still possible (wrong format, non-existent search block), we draw inspiration from the same practices and robustify the pipeline by (i) allowing fuzzy matching of search blocks, if there is a block that differs only in whitespaces or has a small enough Levenshtein distance (Levenshtein, [1966](#bib.bib6 "Binary codes capable of correcting deletions, insertions and reversals")), and (ii) by providing feedback from the parser in case of invalid outputs.

### 4.2. Differential Data Plane Analysis

Evaluating the functional correctness of the proposed reconfiguration CfixC\_{\text{fix}} requires extracting the network’s emergent high-level behaviour from its low-level configuration files and comparing it against a “ground truth” behaviour.

We standardize a network’s high-level function with the following procedure: First, we use Batfish to simulate the data plane of each network, including forwarding decisions for each (src, dst prefix) pair.
Then, we construct a forwarding graph for each prefix, and use the graph algorithms proposed in Config2Spec (Birkner et al., [2020](#bib.bib1 "Config2Spec: mining network specifications from network configurations")) to extract the set of predicates that describe the specifications of the network. Fig. [3](#S4.F3 "Figure 3 ‣ 4.2. Differential Data Plane Analysis ‣ 4. Evaluation Framework ‣ Benchmarking LLM-Driven Network Configuration Repair") shows an example of this flow.

Specification-based reconfiguration evaluation. With the previous process we obtain from CgoldC\_{\text{gold}} the set of specifications Φ\Phi that the reconfigured network must satisfy.
To evaluate a proposed reconfiguration, we also need to compare the behaviour between each network state.
We do this by extracting and comparing the high-level specifications across networks. To improve efficiency, we construct the forwarding graphs only for prefixes whose entries in the forwarding behaviour table differ from the golden state. We calculate the set of violated specifications 𝒱\mathcal{V}, and after performing the predicate extraction pipeline for CfixC\_{\text{fix}}, we calculate the following sets on which we will base our scoring:

* •

  The set of successfully resolved violations

  |  |  |  |
  | --- | --- | --- |
  |  | Φfixed={ϕ∈𝒱∣Cfix⊧ϕ}\Phi\_{\text{fixed}}=\{\phi\in\mathcal{V}\mid C\_{\text{fix}}\models\phi\} |  |
* •

  The set of regressions as originally healthy specifications that are violated by the fix

  |  |  |  |
  | --- | --- | --- |
  |  | Φregressed={ϕ∈(Φ∖𝒱)∣Cfix⊧̸ϕ}\Phi\_{\text{regressed}}=\{\phi\in(\Phi\setminus\mathcal{V})\mid C\_{\text{fix}}\not\models\phi\} |  |
* •

  The set of violations that remained unresolved:

  |  |  |  |
  | --- | --- | --- |
  |  | Φunfixed=𝒱∖Φfixed\Phi\_{\text{unfixed}}=\mathcal{V}\setminus\Phi\_{\text{fixed}} |  |

And we calculate the following scores that describe different performance aspects of the solutions:

* •

  Safety (Regression Rate): The proportion of specifications that were violated because of the proposed misconfiguration:

  |  |  |  |
  | --- | --- | --- |
  |  | Regression=|Φregressed||Φfixed|+|Φunfixed|+|Φregressed|\text{Regression}=\frac{|\Phi\_{\text{regressed}}|}{|\Phi\_{\text{fixed}}|+|\Phi\_{\text{unfixed}}|+|\Phi\_{\text{regressed}}|} |  |
* •

  Efficacy (Fix Score): The proportion of resolved specifications relative to the total violations (initial and regressions):

  |  |  |  |
  | --- | --- | --- |
  |  | Fix Score=|Φfixed||Φfixed|+|Φunfixed|+|Φregressed|\text{Fix Score}=\frac{|\Phi\_{\text{fixed}}|}{|\Phi\_{\text{fixed}}|+|\Phi\_{\text{unfixed}}|+|\Phi\_{\text{regressed}}|} |  |

| Node | Dest. | Action |
| --- | --- | --- |
| R1 | 10.1/24 | Fwd R2 |
| R1 | 10.1/24 | Fwd R3 |
| R2 | 10.1/24 | Fwd R4 |
| R3 | 10.1/24 | Drop |
| R4 | 10.1/24 | Accept |

R1R2R3R4


Reachability(R1,10.1/24) Reachability(R2,10.1/24) Isolation(R3,10.1/24) Reachability(R4,10.1/24) Waypoint(R1,10.1/24,R2)

Figure 3. *For each* unique destination prefix, the pipeline uses the forwarding behaviour table (calculated by Batfish) to construct a forwarding graph, from which it derives the specifications of the network.

### 4.3. Diagnosis Evaluator

While the previous procedure quantifies the restoration of the intended network behaviour, we are also interested in evaluating LLMs’ ability to localize (at the router-level) and diagnose root causes. The following parts of a proposed solution are related to this:

* •

  The list of routers that are detected
* •

  The textual description of the detected faults

We use these artifacts to gain insights into how sound (are only real faults detected?) and how complete (are *all* the faults detected) the proposed diagnoses are. For the task of localizing faulty routers, computing precision and recall is straightforward because they can be compared against the ground truth.

To evaluate diagnostic accuracy, a naïve approach would be to have the models classify each fault into a class from the fault library ℱ\mathcal{F}. However, this would require exposing the model to the list of potential fault types, thereby contaminating the reasoning process and compromising the generalizability of the open-ended diagnosis problem.

Instead, we use the LLM-as-a-Judge method (Zheng et al., [2023](#bib.bib39 "Judging llm-as-a-judge with mt-bench and chatbot arena")), as a viable and scalable alternative to expert human annotation, where we provide 3 different high-capability LLMs (GPT-5.1, Claude 4.5 Opus, Gemini 2.5 Pro) with (i) the proposed textual diagnosis of the benchmarked LLM, and (ii) the ground truth list of misconfigurations in the network; both the types of faults and the textual differences. We request two separate scores that quantify the completeness (i.e., the percentage of faults correctly identified) and the soundness (i.e., the percentage of faults hallucinated) of the diagnosis. To obtain the final scores, we aggregate scores across the judge models to further ensure robustness and mitigate potential biases.

## 5. Experimental Setup

In this section, we review the models examined and describe how inputs are constructed to evaluate LLMs on Cornetto.

Model selection. We evaluate 9 LLMs of varying sizes on Cornetto: 8 state-of-the-art proprietary LLMs (including GPT-5.2, Gemini 3.0, and Claude 4.5 Opus) that consistently dominate benchmark leaderboards (Jimenez et al., [2024](#bib.bib9 "SWE-bench: can language models resolve real-world github issues?"); Balunović et al., [2026](#bib.bib15 "MathArena: evaluating llms on uncontaminated math competitions")) and a single open-source model: GPT-OSS-20B. We include the latter to test the viability of smaller, lower-cost models, though we expect it to be outperformed by the larger proprietary ones.

Input and context construction. A model receives as input a topology TT, a set of violated specifications 𝒱\mathcal{V}, and a network-wide configuration CbrokenC\_{\text{broken}}, which is potentially very large. This data is noisy and voluminous, posing a distinct challenge for the LLM-based troubleshooting workflow (Jiang et al., [2024](#bib.bib41 "CAIP: detecting router misconfigurations with context-aware iterative prompting of llms"); Hamadanian et al., [2023](#bib.bib42 "A holistic view of ai-driven network incident management")). For evaluating LLMs’ robustness in handling this volume and noise, we test the following strategies for including configurations in the context:

* •

  Full context: The model receives the entire network-wide configuration CbrokenC\_{\text{broken}}. Because of the high context window limits of current models, the vast majority (98%) of cases can fit entirely within the prompt. If a model cannot handle the entire input, configuration files are truncated.
* •

  Oracle context: The model receives only the files affected by the misconfiguration. This is an idealized scenario for analysis purposes, since realistically, this information is not known a priori.
* •

  Retrieval mode: For a subset of models, we evaluate a two-stage workflow where the LLM is first prompted to retrieve the necessary configuration files for diagnosis. This should yield a superset of the faulty configurations; therefore, we evaluate the success of this step using the recall metric.

Prompting and parsing. Following standard practices in tackling holistic and multi-stage reasoning tasks (Wei et al., [2023](#bib.bib30 "Chain-of-thought prompting elicits reasoning in large language models"); Zhou et al., [2023](#bib.bib44 "Least-to-most prompting enables complex reasoning in large language models")), we design a prompt that decomposes the reconfiguration repair problem into a structured workflow. We instruct the model to use a Chain-of-Thought (CoT) process that mirrors the formal fault management lifecycle standard ([19](#bib.bib43 "Information processing systems – Open Systems Interconnection – Basic Reference Model – Part 4: Management Framework")).

We implement a parser that expects three distinct solution parts that map to each goal of the process:

* •

  Localization: The list of detected faulty routers.
* •

  Diagnosis: A textual diagnosis of the root causes in the configuration.
* •

  Reconfiguration: A list of configuration changes for the detected faulty routers, using the mandated search-and-replace format (as described in §[4.1](#S4.SS1 "4.1. LLM-Benchmark Interface ‣ 4. Evaluation Framework ‣ Benchmarking LLM-Driven Network Configuration Repair")).

This structured elicitation allows Cornetto to evaluate the accuracy of the intermediate reasoning steps (localization and diagnosis) independently of the final repair quality.
Finally, to ensure that format following is not a confounding factor in our evaluation, we configure the parser to allow one retry attempt per scenario if the model produces a solution that cannot be parsed.

Metrics and reporting. We evaluate performance for each stage leading up to the configuration repair.

#### 1. Diagnostic Reasoning

To assess the models’ ability to isolate faults before fixing them, we report two key metrics:

* •

  Localization F1: The harmonic mean of precision and recall for the set of faulty routers identified by the model against the ground truth.
* •

  Diagnosis Quality: Using the LLM-as-a-Judge method (§[4.3](#S4.SS3 "4.3. Diagnosis Evaluator ‣ 4. Evaluation Framework ‣ Benchmarking LLM-Driven Network Configuration Repair")), we quantify the soundness and completeness of the model’s natural language explanation against the ground truth misconfigurations provided to the LLM-Judges.

#### 2. Functional Correctness

We use differential data plane analysis and report the fix rate and regression rate metrics for each scenario, as defined in §[4.2](#S4.SS2 "4.2. Differential Data Plane Analysis ‣ 4. Evaluation Framework ‣ Benchmarking LLM-Driven Network Configuration Repair"). We also report the percentage of cases correctly resolved, i.e., fixes that satisfy the intended specification without introducing new regressions.

| Model | Fix Score ↑\uparrow | Localization ↑\uparrow | Diagnosis ↑\uparrow | Regression ↓\downarrow | Success Rate ↑\uparrow | Cost ($/task) ↓\downarrow |
| --- | --- | --- | --- | --- | --- | --- |
| GPT-5.2 (High) | 57.8 | 76.5 | 76.8 | 8.6 | 25.5 | 0.16 |
| Gemini 3 Flash | 55.4 | 73.7 | 70.2 | 11.3 | 24.2 | 0.04 |
| Gemini 3 Pro | 47.2 | 70.9 | 66.7 | 13.9 | 18.6 | 0.18 |
| GPT-5.1 (High) | 45.4 | 60.7 | 65.6 | 5.3 | 22.9 | 0.11 |
| Claude 4.5 Opus | 44.2 | 59.8 | 64.1 | 3.5 | 24.3 | 0.42 |
| Claude 4.5 Sonnet | 37.2 | 58.1 | 60.6 | 5.4 | 17.3 | 0.28 |
| GPT-5 mini (High) | 33.9 | 57.5 | 58.3 | 12.8 | 16.9 | 0.02 |
| Grok 4.1 Fast (R.) | 4.5 | 17.1 | 45.2 | 4.9 | 0.03 | 0.01 |
| GPT-OSS-20B | 1.7 | 15.2 | 12.5 | 2.0 | 0.01 | - |

Table 2. While models show promise in restoring network state, they rarely achieve complete resolution and frequently introduce regressions.

## 6. Evaluation

We use Cornetto to evaluate 9 state-of-the-art LLMs across 231 diverse troubleshooting scenarios. Through our analysis, we aim to answer two primary research questions:

* •

  RQ1: To what extent can current LLMs autonomously localize, diagnose, and repair network misconfigurations without introducing regressions? We present the performance of all LLMs across our core metrics for diagnostic accuracy and repair functional correctness, summarizing key insights into their capabilities.
* •

  RQ2: How do task factors such as topological and configuration scale, fault multiplicity, and extent of disruption impact model performance? We quantify the degradation of model reliability across increasing difficulty gradients.

![Refer to caption](2604.22513v1/x3.png)


Figure 4. Frontier LLMs benefit from access to global context.

![Refer to caption](2604.22513v1/x4.png)


Figure 5. Cornetto is not saturated with either impossible or trivial tasks.

Table [2](#S5.T2 "Table 2 ‣ 2. Functional Correctness ‣ 5. Experimental Setup ‣ Benchmarking LLM-Driven Network Configuration Repair") and Figure [4](#S6.F4 "Figure 4 ‣ 6. Evaluation ‣ Benchmarking LLM-Driven Network Configuration Repair") present the comprehensive evaluation of all 9 models on Cornetto. The histogram of Fig. [5](#S6.F5 "Figure 5 ‣ 6. Evaluation ‣ Benchmarking LLM-Driven Network Configuration Repair") illustrates the distribution of fix scores — calculated as the per-task average of the top five models. This quasi-normal distribution confirms a desirable property of the benchmark (Hardt, [2025](#bib.bib48 "The emerging science of machine learning benchmarks")): it captures a spectrum of complexity rather than being saturated with impossible (score 0.0) or trivial (score 1.0) cases.

While LLMs demonstrate potential for diagnostic and repair tasks, our analysis shows that they rarely produce fully correct fixes, with strictly correct resolutions (100% fix rate with zero regressions) occurring in at most 25.5% of cases. This ceiling in performance suggests that current models are best deployed as “Human-in-the-Loop” assistants, consistent with recent research (Hamadanian et al., [2023](#bib.bib42 "A holistic view of ai-driven network incident management")) and industry practices (Wang et al., [2024b](#bib.bib22 "NetAssistant: dialogue based network diagnosis in data center networks"), [2025a](#bib.bib20 "Towards llm-based failure localization in production-scale networks"), [2025b](#bib.bib21 "Intent-driven network management with multi-agent llms: the confucius framework")).

We detail the specific factors affecting LLM performance through the following insights:

Models perform better with access to global context. As shown in Fig. [4](#S6.F4 "Figure 4 ‣ 6. Evaluation ‣ Benchmarking LLM-Driven Network Configuration Repair"), providing the full network-wide configuration almost always outperforms the idealized oracle setting, which only contains the faulty configuration files. This indicates that for top-performing models, the ability to examine configurations contextually outweighs the noise introduced by all the irrelevant configuration data. We quantify this trade-off in the Retrieval mode results (Table [3](#S6.T3 "Table 3 ‣ 6. Evaluation ‣ Benchmarking LLM-Driven Network Configuration Repair")). When tasked with autonomous context selection, GPT-5 mini achieves high recall (82.6%) of faulty routers, thereby effectively filtering noise and improving performance across all metrics. Gemini 3.0 Flash, however, misses critical configuration files (68.1% Recall), and its performance degrades. This suggests that smaller models can benefit from careful context selection. This finding is consistent with work on multi-agent systems powered by smaller language models (Belcak et al., [2025](#bib.bib46 "Small language models are the future of agentic ai"); Wu et al., [2023](#bib.bib34 "AutoGen: enabling next-gen llm applications via multi-agent conversation")).

| Model | Recall | Δ​Fix\Delta\text{Fix} | Δ​Diag.\Delta\text{Diag.} | Δ​Regr.\Delta\text{Regr.} | Δ​$\Delta\mathdollar |
| --- | --- | --- | --- | --- | --- |
| [Uncaptioned image] 3 Flash | 68.1% | -4.7% | -2.0% | +0.5% | +0.03 |
| [Uncaptioned image] 5 Mini | 82.6% | +5.7% | +4.0% | -2.0% | +0.01 |

Table 3. Accurate retrieval of critical configurations can filter out noisy data and improve performance

Most efficacious LLMs are not always the safest. A high fix rate does not guarantee preservation of previously satisfied specifications. While GPT-5.2 leads in fix rate (57.8%), several other models achieve lower regression rates, including its predecessor GPT-5.1. In contrast, Claude 4.5 Opus is more conservative in its repairs, achieving a lower score of 44.2% but the lowest regression rate at 3.6%.

Accurate diagnoses lead to (but do not guarantee) effective fixes. We analyse the correlation between the diagnosis performance and final repair quality in Fig. [6](#S6.F6 "Figure 6 ‣ 6. Evaluation ‣ Benchmarking LLM-Driven Network Configuration Repair"). We observe a moderate positive correlation between diagnosis accuracy/localization and fix score. Crucially, the cluster of high diagnostic scores that yield poor repair metrics (upper-left quadrant in the scatter plot) represents cases in which models identified issues but failed to resolve them. Thus, while correct diagnoses often lead to correct fixes, they do not guarantee them.

![Refer to caption](2604.22513v1/x5.png)


Figure 6. Diagnostic accuracy is necessary but not sufficient for repair.

LLM performance degrades at scale. Topological scale, configuration length, and predicate set size are all factors that directly affect the amount of information included in the prompt. Hence, it is unsurprising that model performance consistently degrades with increasing input size, as shown in Fig. [7](#S6.F7 "Figure 7 ‣ 6. Evaluation ‣ Benchmarking LLM-Driven Network Configuration Repair"). This amplifies the need for selecting relevant information for a model’s limited context window.

LLMs struggle more to detect all faults. We observe a revealing divergence between diagnostic soundness (precision) and completeness (recall) as fault multiplicity increases. As seen in Fig. [8](#S6.F8 "Figure 8 ‣ 6. Evaluation ‣ Benchmarking LLM-Driven Network Configuration Repair"), completeness degrades sharply, while soundness exhibits a slight upward trend. We hypothesize the following: In single-fault scenarios, the misconfiguration “signal” is sparse, which often causes models to miss the issue entirely or even hallucinate faults — hurting both soundness and completeness. Counterintuitively, as the number of faults increases, the abundance of such signals makes it easier for the model to identify any of the real faults. Yet, models often stop at a partial diagnosis and reconfiguration, ignoring other disrupting misconfigurations.

Major network disruptions impact model performance. As shown in Fig. [9](#S6.F9 "Figure 9 ‣ 6. Evaluation ‣ Benchmarking LLM-Driven Network Configuration Repair"), we observe a general negative correlation between network disruption (percentage of broken predicates) and fix score performance. Notably, GPT-5.1 exhibits the sharpest degradation, whereas more capable models such as GPT-5.2 show resilience in repairing networks under more severe disruptions, indicating the ability to link broader specification violations to their root causes.

Takeaways. The results of our analysis show that:

* •

  Global context is critical but noisy: While excessive data volume degraded performance, we found that models benefited from access to global configuration context. A system that effectively handles configuration repair should include a stage in which critical context is filtered in a dependency-aware manner, akin to recent work in (Jiang et al., [2024](#bib.bib41 "CAIP: detecting router misconfigurations with context-aware iterative prompting of llms")).
* •

  Verification is a prerequisite for safety: Regressions frequently accompany fixes, which is prohibitive while configuring networks. We posit that a system that automates configuration requires a closed loop with a verifier that proves the safety of solutions before deployment.
* •

  Iterative repair is needed for completeness: Models struggle to resolve concurrent faults in a single pass, indicating that monolithic prompting fails at scale despite expansive context windows. Troubleshooting must be decomposed into an iterative agentic workflow that diagnoses, proposes, and verifies solutions until the desired result is achieved.

![Refer to caption](2604.22513v1/x6.png)


Figure 7. Repair performance consistently degrades with increasing context length.

![Refer to caption](2604.22513v1/x7.png)


Figure 8. Models struggle to handle concurrent failures; as the number of root causes increases, diagnosis becomes partial and fix rate degrades.

![Refer to caption](2604.22513v1/x8.png)


Figure 9. While some models remain robust, many perform poorly on more disruptive network faults.

## 7. Related Work

Network verification. Two decades of research have established formal methods to mathematically prove network correctness. Data plane verification (Khurshid et al., [2013](#bib.bib26 "VeriFlow: verifying Network-Wide invariants in real time"); Mai et al., [2011](#bib.bib38 "Debugging the data plane with anteater")) checks that the network’s forwarding behaviour satisfies some desired property, and control plane verification (Fogel et al., [2015](#bib.bib10 "A general approach to network configuration analysis"); Beckett et al., [2017a](#bib.bib27 "A general approach to network configuration verification")), verifies that a network configuration will produce a data plane that satisfies some intent (Krentsel et al., [2025](#bib.bib19 "Towards accessible model-free verification")). Specification mining (Birkner et al., [2020](#bib.bib1 "Config2Spec: mining network specifications from network configurations")) builds on these approaches to derive the set of forwarding specifications satisfied by a configuration.

Cornetto uses Batfish (Fogel et al., [2015](#bib.bib10 "A general approach to network configuration analysis")) in conjunction with the specification mining algorithms proposed in Config2Spec (Birkner et al., [2020](#bib.bib1 "Config2Spec: mining network specifications from network configurations")) as an integral component of its problem formulation. Specifically, we mine the ground-truth specifications from the correct reference network and use them to rigorously evaluate the functional correctness of the LLM-generated fixes.

LLM Benchmarks. Benchmarks such as SWE-Bench (Jimenez et al., [2024](#bib.bib9 "SWE-bench: can language models resolve real-world github issues?")) and BaxBench (Vero et al., [2025](#bib.bib45 "BaxBench: can llms generate correct and secure backends?")) indicate that rigorous evaluation of LLMs in software engineering faces fundamental challenges similar to those in network configuration repair. First, ensuring usability requires automatic, functional verification of solutions. Second, realistic tasks require navigating large volumes of noisy data (whether from entire code repositories or network-wide configurations) to identify useful information and arrive at a solution. Cornetto contextualizes these challenges within the realm of network configuration repair, ensuring that it reflects the complexities of real-world network operations.

LLMs for network operations. Interest in LLMs to address the limitations of formal verification is growing, evidenced by recent industry assistants (Wang et al., [2024b](#bib.bib22 "NetAssistant: dialogue based network diagnosis in data center networks"), [2025b](#bib.bib21 "Intent-driven network management with multi-agent llms: the confucius framework"), [2025a](#bib.bib20 "Towards llm-based failure localization in production-scale networks")) and benchmarks (Wang et al., [2024a](#bib.bib14 "NetConfEval: can llms facilitate network configuration?"); Aykurt et al., [2024](#bib.bib18 "NetLLMBench: a benchmark framework for large language models in network configuration tasks"); Wang et al., [2025c](#bib.bib17 "A network arena for benchmarking ai agents on network troubleshooting"); Zhou et al., [2026](#bib.bib50 "NetArena: dynamic benchmarks for ai agents in network automation")). Cornetto complements those efforts by rigorously evaluating end-to-end configuration repair, thereby advancing understanding of AI’s potential and applicability to automated network operations.

## 8. Discussion and Limitations

What about evaluating fancier LLM-based systems? The strategy space for LLM-based configuration repair is immense. Among others, it encompasses different prompting strategies that affect a model’s reasoning process (Brown et al., [2020](#bib.bib31 "Language models are few-shot learners"); Wei et al., [2023](#bib.bib30 "Chain-of-thought prompting elicits reasoning in large language models")), retrieval methods that determine which relevant information is included in the context from large volumes of data (Lewis et al., [2021](#bib.bib32 "Retrieval-augmented generation for knowledge-intensive nlp tasks")), and agentic systems, which constitute a distinct design space of their own (Yao et al., [2023](#bib.bib33 "ReAct: synergizing reasoning and acting in language models"); Wu et al., [2023](#bib.bib34 "AutoGen: enabling next-gen llm applications via multi-agent conversation"); Hong et al., [2024](#bib.bib35 "MetaGPT: meta programming for a multi-agent collaborative framework")).

In this work, we assess the intrinsic capabilities of LLMs to reason about network state and resolve misconfigurations. We argue that establishing this baseline is critical, as it decouples performance attributable to the model’s reasoning power from gains attributed to complex-system scaffolding. Still, we design Cornetto as a modular platform that supports the evaluation of such advanced setups (including RAG and agentic systems).

What about specifications under failures? Network operators often care about invariants holding across multiple environments (e.g., maintaining reachability under any 2 link failures). While control-plane verification (Beckett et al., [2017a](#bib.bib27 "A general approach to network configuration verification")) can prove properties across all possible environments, we focus on specifications for a single environment; we posit that performance in this setting serves as a necessary upper bound on model capability. Since our results demonstrate that LLMs already struggle to reason about network state in a single environment, introducing the complexity of failure models is currently premature. Evaluating reasoning across all possible environments efficiently enough to support many benchmark cases will be considered in the future.

## 9. Conclusion

We presented Cornetto, a comprehensive framework for evaluating LLM-driven configuration repair. Cornetto generates diverse scenarios and rigorously evaluates the end-to-end troubleshooting process by assessing diagnostic accuracy and formally verifying the correctness of repairs. Our evaluation of 9 state-of-the-art LLMs on 231 generated scenarios reveals their potential to diagnose misconfigurations and their struggle to reliably synthesize correct and safe reconfigurations. By providing a platform for thorough assessment of these repair capabilities, Cornetto contributes towards the advancement of reliable, automated network operations.

This work does not raise ethical issues.

## References

* [1]
  K. Aykurt, A. Blenk, and W. Kellerer (2024)
  NetLLMBench: a benchmark framework for large language models in network configuration tasks.
  In 2024 IEEE Conference on Network Function Virtualization and Software Defined Networks (NFV-SDN),
  Vol. ,  pp. 1–6.
  External Links: [Document](https://dx.doi.org/10.1109/NFV-SDN61811.2024.10807499)
  Cited by: [§1](#S1.p6.1 "1. Introduction ‣ Benchmarking LLM-Driven Network Configuration Repair"),
  [§7](#S7.p4.1 "7. Related Work ‣ Benchmarking LLM-Driven Network Configuration Repair").
* [2]
  M. Balunović, J. Dekoninck, I. Petrov, N. Jovanović, and M. Vechev (2026)
  MathArena: evaluating llms on uncontaminated math competitions.
  External Links: 2505.23281,
  [Link](https://arxiv.org/abs/2505.23281)
  Cited by: [§5](#S5.p2.1 "5. Experimental Setup ‣ Benchmarking LLM-Driven Network Configuration Repair").
* [3]
  R. Beckett, A. Gupta, R. Mahajan, and D. Walker (2017)
  A general approach to network configuration verification.
  In Proceedings of the Conference of the ACM Special Interest Group on Data Communication,
  SIGCOMM ’17, New York, NY, USA,  pp. 155–168.
  External Links: ISBN 9781450346535,
  [Link](https://doi.org/10.1145/3098822.3098834),
  [Document](https://dx.doi.org/10.1145/3098822.3098834)
  Cited by: [§1](#S1.p1.1 "1. Introduction ‣ Benchmarking LLM-Driven Network Configuration Repair"),
  [§7](#S7.p1.1 "7. Related Work ‣ Benchmarking LLM-Driven Network Configuration Repair"),
  [§8](#S8.p3.1 "8. Discussion and Limitations ‣ Benchmarking LLM-Driven Network Configuration Repair").
* [4]
  R. Beckett, R. Mahajan, T. Millstein, J. Padhye, and D. Walker (2017)
  Network configuration synthesis with abstract topologies.
  In Proceedings of the 38th ACM SIGPLAN Conference on Programming Language Design and Implementation,
  PLDI 2017, New York, NY, USA,  pp. 437–451.
  External Links: ISBN 9781450349888,
  [Link](https://doi.org/10.1145/3062341.3062367),
  [Document](https://dx.doi.org/10.1145/3062341.3062367)
  Cited by: [§3.3](#S3.SS3.p4.1 "3.3. Scenario Generation ‣ 3. Dataset Generation Pipeline ‣ Benchmarking LLM-Driven Network Configuration Repair").
* [5]
  R. Beckett, R. Mahajan, T. Millstein, J. Padhye, and D. Walker (2016-08)
  Don’t mind the gap: bridging network-wide objectives and device-level configurations.
  In SIGCOMM 2016,
  External Links: [Link](https://www.microsoft.com/en-us/research/publication/dont-mind-gap-bridging-network-wide-objectives-device-level-configurations/)
  Cited by: [§1](#S1.p1.1 "1. Introduction ‣ Benchmarking LLM-Driven Network Configuration Repair"),
  [§1](#S1.p8.1 "1. Introduction ‣ Benchmarking LLM-Driven Network Configuration Repair"),
  [§3.3](#S3.SS3.p4.1 "3.3. Scenario Generation ‣ 3. Dataset Generation Pipeline ‣ Benchmarking LLM-Driven Network Configuration Repair").
* [6]
  P. Belcak, G. Heinrich, S. Diao, Y. Fu, X. Dong, S. Muralidharan, Y. C. Lin, and P. Molchanov (2025)
  Small language models are the future of agentic ai.
  External Links: 2506.02153,
  [Link](https://arxiv.org/abs/2506.02153)
  Cited by: [§6](#S6.p6.1 "6. Evaluation ‣ Benchmarking LLM-Driven Network Configuration Repair").
* [7]
  E. M. Bender, T. Gebru, A. McMillan-Major, and S. Shmitchell (2021)
  On the dangers of stochastic parrots: can language models be too big?.
  In Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency,
  FAccT ’21, New York, NY, USA,  pp. 610–623.
  External Links: ISBN 9781450383097,
  [Link](https://doi.org/10.1145/3442188.3445922),
  [Document](https://dx.doi.org/10.1145/3442188.3445922)
  Cited by: [§1](#S1.p2.1 "1. Introduction ‣ Benchmarking LLM-Driven Network Configuration Repair").
* [8]
  R. Birkner, T. Brodmann, P. Tsankov, L. Vanbever, and M. Vechev (2021-04)
  Metha: network verifiers need to be correct too!.
  In 18th USENIX Symposium on Networked Systems Design and Implementation (NSDI 21),
   pp. 99–113.
  External Links: ISBN 978-1-939133-21-2,
  [Link](https://www.usenix.org/conference/nsdi21/presentation/birkner)
  Cited by: [§1](#S1.p1.1 "1. Introduction ‣ Benchmarking LLM-Driven Network Configuration Repair"),
  [§3.3](#S3.SS3.p4.1 "3.3. Scenario Generation ‣ 3. Dataset Generation Pipeline ‣ Benchmarking LLM-Driven Network Configuration Repair").
* [9]
  R. Birkner, D. Drachsler-Cohen, L. Vanbever, and M. Vechev (2020)
  Config2Spec: mining network specifications from network configurations.
  In 17th USENIX Symposium on Networked Systems Design and Implementation (NSDI 20),
  Cited by: [§2.2](#S2.SS2.p4.1 "2.2. Key Insights ‣ 2. Overview ‣ Benchmarking LLM-Driven Network Configuration Repair"),
  [§3.1](#S3.SS1.SSSx1.p1.1 "Specifications ‣ 3.1. Task Definition ‣ 3. Dataset Generation Pipeline ‣ Benchmarking LLM-Driven Network Configuration Repair"),
  [§4.2](#S4.SS2.p2.1 "4.2. Differential Data Plane Analysis ‣ 4. Evaluation Framework ‣ Benchmarking LLM-Driven Network Configuration Repair"),
  [§7](#S7.p1.1 "7. Related Work ‣ Benchmarking LLM-Driven Network Configuration Repair"),
  [§7](#S7.p2.1 "7. Related Work ‣ Benchmarking LLM-Driven Network Configuration Repair").
* [10]
  T. B. Brown, B. Mann, N. Ryder, M. Subbiah, J. Kaplan, P. Dhariwal, A. Neelakantan, P. Shyam, G. Sastry, A. Askell, S. Agarwal, A. Herbert-Voss, G. Krueger, T. Henighan, R. Child, A. Ramesh, D. M. Ziegler, J. Wu, C. Winter, C. Hesse, M. Chen, E. Sigler, M. Litwin, S. Gray, B. Chess, J. Clark, C. Berner, S. McCandlish, A. Radford, I. Sutskever, and D. Amodei (2020)
  Language models are few-shot learners.
  External Links: 2005.14165,
  [Link](https://arxiv.org/abs/2005.14165)
  Cited by: [§8](#S8.p1.1 "8. Discussion and Limitations ‣ Benchmarking LLM-Driven Network Configuration Repair").
* [11]
  A. El-Hassany, P. Tsankov, L. Vanbever, and M. Vechev (2018)
  NetComplete: Practical Network-Wide Configuration Synthesis with Autocompletion.
  In USENIX NSDI’18,
  Renton, WA, USA.
  Cited by: [§1](#S1.p1.1 "1. Introduction ‣ Benchmarking LLM-Driven Network Configuration Repair"),
  [§3.3](#S3.SS3.p4.1 "3.3. Scenario Generation ‣ 3. Dataset Generation Pipeline ‣ Benchmarking LLM-Driven Network Configuration Repair").
* [12]
  A. Fogel, S. Fung, L. Pedrosa, M. Walraed-Sullivan, R. Govindan, R. Mahajan, and T. Millstein (2015-05)
  A general approach to network configuration analysis.
  In 12th USENIX Symposium on Networked Systems Design and Implementation (NSDI 15),
  Oakland, CA,  pp. 469–483.
  External Links: ISBN 978-1-931971-218,
  [Link](https://www.usenix.org/conference/nsdi15/technical-sessions/presentation/fogel)
  Cited by: [§1](#S1.p1.1 "1. Introduction ‣ Benchmarking LLM-Driven Network Configuration Repair"),
  [§2.2](#S2.SS2.p3.1 "2.2. Key Insights ‣ 2. Overview ‣ Benchmarking LLM-Driven Network Configuration Repair"),
  [§7](#S7.p1.1 "7. Related Work ‣ Benchmarking LLM-Driven Network Configuration Repair"),
  [§7](#S7.p2.1 "7. Related Work ‣ Benchmarking LLM-Driven Network Configuration Repair").
* [13]
  P. Gauthier (2023)
  Aider: ai pair programming in your terminal.
  External Links: [Link](https://github.com/paul-gauthier/aider)
  Cited by: [§4.1](#S4.SS1.SSSx2.p1.1 "Reconfiguration Parser ‣ 4.1. LLM-Benchmark Interface ‣ 4. Evaluation Framework ‣ Benchmarking LLM-Driven Network Configuration Repair").
* [14]
  E. Glukhov, M. Conti, E. Bogomolov, Y. Golubev, and A. Bezzubov (2025)
  Diff-xyz: a benchmark for evaluating diff understanding.
  External Links: 2510.12487,
  [Link](https://arxiv.org/abs/2510.12487)
  Cited by: [§4.1](#S4.SS1.SSSx2.p1.1 "Reconfiguration Parser ‣ 4.1. LLM-Benchmark Interface ‣ 4. Evaluation Framework ‣ Benchmarking LLM-Driven Network Configuration Repair").
* [15]
  Google DeepMind (2025)
  Gemini 3 Pro.
  Note: <https://deepmind.google/models/gemini/pro/>Accessed: 2026-02-01
  Cited by: [§1](#S1.p2.1 "1. Introduction ‣ Benchmarking LLM-Driven Network Configuration Repair").
* [16]
  P. Hamadanian, B. Arzani, S. Fouladi, S. K. R. Kakarla, R. Fonseca, D. Billor, A. Cheema, E. Nkposong, and R. Chandra (2023)
  A holistic view of ai-driven network incident management.
  In Proceedings of the 22nd ACM Workshop on Hot Topics in Networks,
  HotNets ’23, New York, NY, USA,  pp. 180–188.
  External Links: ISBN 9798400704154,
  [Link](https://doi.org/10.1145/3626111.3628176),
  [Document](https://dx.doi.org/10.1145/3626111.3628176)
  Cited by: [§5](#S5.p3.3 "5. Experimental Setup ‣ Benchmarking LLM-Driven Network Configuration Repair"),
  [§6](#S6.p4.1 "6. Evaluation ‣ Benchmarking LLM-Driven Network Configuration Repair").
* [17]
  M. Hardt (2025)
  The emerging science of machine learning benchmarks.
  Note: Online at <https://mlbenchmarks.org>Manuscript
  Cited by: [§2.1](#S2.SS1.p2.1 "2.1. Design Goals ‣ 2. Overview ‣ Benchmarking LLM-Driven Network Configuration Repair"),
  [§6](#S6.p3.1 "6. Evaluation ‣ Benchmarking LLM-Driven Network Configuration Repair").
* [18]
  S. Hong, M. Zhuge, J. Chen, X. Zheng, Y. Cheng, C. Zhang, J. Wang, Z. Wang, S. K. S. Yau, Z. Lin, L. Zhou, C. Ran, L. Xiao, C. Wu, and J. Schmidhuber (2024)
  MetaGPT: meta programming for a multi-agent collaborative framework.
  External Links: 2308.00352,
  [Link](https://arxiv.org/abs/2308.00352)
  Cited by: [§8](#S8.p1.1 "8. Discussion and Limitations ‣ Benchmarking LLM-Driven Network Configuration Repair").
* [19]
  Cited by: [§5](#S5.p5.1 "5. Experimental Setup ‣ Benchmarking LLM-Driven Network Configuration Repair").
* [20]
  Z. Ji, N. Lee, R. Frieske, T. Yu, D. Su, Y. Xu, E. Ishii, Y. J. Bang, A. Madotto, and P. Fung (2023-03)
  Survey of hallucination in natural language generation.
  ACM Computing Surveys 55 (12),  pp. 1–38.
  External Links: ISSN 1557-7341,
  [Link](http://dx.doi.org/10.1145/3571730),
  [Document](https://dx.doi.org/10.1145/3571730)
  Cited by: [§1](#S1.p2.1 "1. Introduction ‣ Benchmarking LLM-Driven Network Configuration Repair").
* [21]
  X. Jiang, A. Gember-Jacobson, and N. Feamster (2024)
  CAIP: detecting router misconfigurations with context-aware iterative prompting of llms.
  External Links: 2411.14283,
  [Link](https://arxiv.org/abs/2411.14283)
  Cited by: [§5](#S5.p3.3 "5. Experimental Setup ‣ Benchmarking LLM-Driven Network Configuration Repair"),
  [1st item](#S6.I2.i1.p1.1 "In 6. Evaluation ‣ Benchmarking LLM-Driven Network Configuration Repair").
* [22]
  C. E. Jimenez, J. Yang, et al. (2024)
  SWE-bench: can language models resolve real-world github issues?.
  In ICLR,
  Cited by: [§4.1](#S4.SS1.SSSx2.p1.1 "Reconfiguration Parser ‣ 4.1. LLM-Benchmark Interface ‣ 4. Evaluation Framework ‣ Benchmarking LLM-Driven Network Configuration Repair"),
  [§5](#S5.p2.1 "5. Experimental Setup ‣ Benchmarking LLM-Driven Network Configuration Repair"),
  [§7](#S7.p3.1 "7. Related Work ‣ Benchmarking LLM-Driven Network Configuration Repair").
* [23]
  A. Khurshid, X. Zou, W. Zhou, M. Caesar, and P. B. Godfrey (2013-04)
  VeriFlow: verifying Network-Wide invariants in real time.
  In 10th USENIX Symposium on Networked Systems Design and Implementation (NSDI 13),
  Lombard, IL,  pp. 15–27.
  External Links: ISBN 978-1-931971-00-3,
  [Link](https://www.usenix.org/conference/nsdi13/technical-sessions/presentation/khurshid)
  Cited by: [§1](#S1.p1.1 "1. Introduction ‣ Benchmarking LLM-Driven Network Configuration Repair"),
  [§7](#S7.p1.1 "7. Related Work ‣ Benchmarking LLM-Driven Network Configuration Repair").
* [24]
  S. Knight, H. X. Nguyen, N. Falkner, R. Bowden, and M. Roughan (2011)
  The internet topology zoo.
  IEEE Journal on Selected Areas in Communications 29 (9),  pp. 1765–1775.
  External Links: [Document](https://dx.doi.org/10.1109/JSAC.2011.111002)
  Cited by: [§3.2](#S3.SS2.SSSx2.p1.2 "2. Topology selection ‣ 3.2. Effective Task Space Representation ‣ 3. Dataset Generation Pipeline ‣ Benchmarking LLM-Driven Network Configuration Repair").
* [25]
  A. Krentsel, O. Ye, A. Tafoya, X. Ma, S. Ratnasamy, and A. Shaikh (2025)
  Towards accessible model-free verification.
  HotNets ’25, New York, NY, USA,  pp. 210–217.
  External Links: ISBN 9798400722806,
  [Link](https://doi.org/10.1145/3772356.3772380),
  [Document](https://dx.doi.org/10.1145/3772356.3772380)
  Cited by: [§1](#S1.p1.1 "1. Introduction ‣ Benchmarking LLM-Driven Network Configuration Repair"),
  [§7](#S7.p1.1 "7. Related Work ‣ Benchmarking LLM-Driven Network Configuration Repair").
* [26]
  D.R. Kuhn, D.R. Wallace, and A.M. Gallo (2004)
  Software fault interactions and implications for software testing.
  IEEE Transactions on Software Engineering 30 (6),  pp. 418–421.
  External Links: [Document](https://dx.doi.org/10.1109/TSE.2004.24)
  Cited by: [§2.2](#S2.SS2.p1.1 "2.2. Key Insights ‣ 2. Overview ‣ Benchmarking LLM-Driven Network Configuration Repair"),
  [§3.2](#S3.SS2.p7.1 "3.2. Effective Task Space Representation ‣ 3. Dataset Generation Pipeline ‣ Benchmarking LLM-Driven Network Configuration Repair").
* [27]
  V. I. Levenshtein (1966-02)
  Binary codes capable of correcting deletions, insertions and reversals.
  Soviet Physics Doklady 10,  pp. 707.
  Cited by: [§4.1](#S4.SS1.SSSx2.p2.1 "Reconfiguration Parser ‣ 4.1. LLM-Benchmark Interface ‣ 4. Evaluation Framework ‣ Benchmarking LLM-Driven Network Configuration Repair").
* [28]
  P. Lewis, E. Perez, A. Piktus, F. Petroni, V. Karpukhin, N. Goyal, H. Küttler, M. Lewis, W. Yih, T. Rocktäschel, S. Riedel, and D. Kiela (2021)
  Retrieval-augmented generation for knowledge-intensive nlp tasks.
  External Links: 2005.11401,
  [Link](https://arxiv.org/abs/2005.11401)
  Cited by: [§8](#S8.p1.1 "8. Discussion and Limitations ‣ Benchmarking LLM-Driven Network Configuration Repair").
* [29]
  N. F. Liu, K. Lin, J. Hewitt, A. Paranjape, M. Bevilacqua, F. Petroni, and P. Liang (2023)
  Lost in the middle: how language models use long contexts.
  External Links: 2307.03172,
  [Link](https://arxiv.org/abs/2307.03172)
  Cited by: [§4.1](#S4.SS1.SSSx1.p3.1 "Context Construction ‣ 4.1. LLM-Benchmark Interface ‣ 4. Evaluation Framework ‣ Benchmarking LLM-Driven Network Configuration Repair").
* [30]
  D. Mackenzie, P. Eggert, and J. Meyering (2002)
  Comparing and merging files with gnu diff and patch.
   Free Software Foundation.
  External Links: [Link](https://www.gnu.org/software/diffutils/manual/)
  Cited by: [§4.1](#S4.SS1.SSSx2.p1.1 "Reconfiguration Parser ‣ 4.1. LLM-Benchmark Interface ‣ 4. Evaluation Framework ‣ Benchmarking LLM-Driven Network Configuration Repair").
* [31]
  H. Mai, A. Khurshid, R. Agarwal, M. Caesar, P. B. Godfrey, and S. T. King (2011-08)
  Debugging the data plane with anteater.
  SIGCOMM Comput. Commun. Rev. 41 (4),  pp. 290–301.
  External Links: ISSN 0146-4833,
  [Link](https://doi.org/10.1145/2043164.2018470),
  [Document](https://dx.doi.org/10.1145/2043164.2018470)
  Cited by: [§7](#S7.p1.1 "7. Related Work ‣ Benchmarking LLM-Driven Network Configuration Repair").
* [32]
  OpenAI (2025)
  GPT-5 System Card.
  Technical report
   OpenAI.
  Note: Accessed: 2026-02-01
  External Links: [Link](https://cdn.openai.com/gpt-5-system-card.pdf)
  Cited by: [§1](#S1.p2.1 "1. Introduction ‣ Benchmarking LLM-Driven Network Configuration Repair").
* [33]
  I. Protogeros and L. Vanbever (2025)
  Continual benchmarking of llm-based systems on networking operations.
  In Proceedings of the ACM SIGCOMM 2025 Posters and Demos,
  ACM SIGCOMM Posters and Demos ’25, New York, NY, USA,  pp. 70–72.
  External Links: ISBN 9798400720260,
  [Link](https://doi.org/10.1145/3744969.3748425),
  [Document](https://dx.doi.org/10.1145/3744969.3748425)
  Cited by: [footnote 1](#footnote1 "In 1. Introduction ‣ Benchmarking LLM-Driven Network Configuration Repair").
* [34]
  F. Shi, X. Chen, K. Misra, N. Scales, D. Dohan, E. Chi, N. Schärli, and D. Zhou (2023)
  Large language models can be easily distracted by irrelevant context.
  External Links: 2302.00093,
  [Link](https://arxiv.org/abs/2302.00093)
  Cited by: [§4.1](#S4.SS1.SSSx1.p3.1 "Context Construction ‣ 4.1. LLM-Benchmark Interface ‣ 4. Evaluation Framework ‣ Benchmarking LLM-Driven Network Configuration Repair").
* [35]
  M. Vero, N. Mündler, V. Chibotaru, V. Raychev, M. Baader, N. Jovanović, J. He, and M. Vechev (2025)
  BaxBench: can llms generate correct and secure backends?.
  External Links: 2502.11844,
  [Link](https://arxiv.org/abs/2502.11844)
  Cited by: [§7](#S7.p3.1 "7. Related Work ‣ Benchmarking LLM-Driven Network Configuration Repair").
* [36]
  C. Wang, M. Scazzariello, A. Farshin, S. Ferlin, D. Kostić, and M. Chiesa (2024-06)
  NetConfEval: can llms facilitate network configuration?.
  Proc. ACM Netw. 2 (CoNEXT2).
  External Links: [Link](https://doi.org/10.1145/3656296),
  [Document](https://dx.doi.org/10.1145/3656296)
  Cited by: [§1](#S1.p6.1 "1. Introduction ‣ Benchmarking LLM-Driven Network Configuration Repair"),
  [§7](#S7.p4.1 "7. Related Work ‣ Benchmarking LLM-Driven Network Configuration Repair").
* [37]
  C. Wang, X. Zhang, R. Lu, X. Lin, X. Zeng, X. Zhang, Z. An, G. Wu, J. Gao, C. Tian, G. Chen, G. Liu, Y. Liao, T. Lin, D. Cai, and E. Zhai (2025)
  Towards llm-based failure localization in production-scale networks.
  In Proceedings of the ACM SIGCOMM 2025 Conference,
  SIGCOMM ’25, New York, NY, USA,  pp. 496–511.
  External Links: ISBN 9798400715242,
  [Link](https://doi.org/10.1145/3718958.3750505),
  [Document](https://dx.doi.org/10.1145/3718958.3750505)
  Cited by: [§1](#S1.p2.1 "1. Introduction ‣ Benchmarking LLM-Driven Network Configuration Repair"),
  [§6](#S6.p4.1 "6. Evaluation ‣ Benchmarking LLM-Driven Network Configuration Repair"),
  [§7](#S7.p4.1 "7. Related Work ‣ Benchmarking LLM-Driven Network Configuration Repair").
* [38]
  H. Wang, A. Abhashkumar, C. Lin, T. Zhang, X. Gu, N. Ma, C. Wu, S. Liu, W. Zhou, Y. Dong, W. Jiang, and Y. Wang (2024-04)
  NetAssistant: dialogue based network diagnosis in data center networks.
  In 21st USENIX Symposium on Networked Systems Design and Implementation (NSDI 24),
  Santa Clara, CA,  pp. 2011–2024.
  External Links: ISBN 978-1-939133-39-7,
  [Link](https://www.usenix.org/conference/nsdi24/presentation/wang-haopei)
  Cited by: [§1](#S1.p2.1 "1. Introduction ‣ Benchmarking LLM-Driven Network Configuration Repair"),
  [§6](#S6.p4.1 "6. Evaluation ‣ Benchmarking LLM-Driven Network Configuration Repair"),
  [§7](#S7.p4.1 "7. Related Work ‣ Benchmarking LLM-Driven Network Configuration Repair").
* [39]
  Z. Wang, S. Lin, G. Yan, S. Ghorbani, M. Yu, J. Zhou, N. Hu, L. Baruah, S. Peters, S. Kamath, J. Yang, and Y. Zhang (2025)
  Intent-driven network management with multi-agent llms: the confucius framework.
  In Proceedings of the ACM SIGCOMM 2025 Conference,
  SIGCOMM ’25, New York, NY, USA,  pp. 347–362.
  External Links: ISBN 9798400715242,
  [Link](https://doi.org/10.1145/3718958.3750537),
  [Document](https://dx.doi.org/10.1145/3718958.3750537)
  Cited by: [§1](#S1.p2.1 "1. Introduction ‣ Benchmarking LLM-Driven Network Configuration Repair"),
  [§6](#S6.p4.1 "6. Evaluation ‣ Benchmarking LLM-Driven Network Configuration Repair"),
  [§7](#S7.p4.1 "7. Related Work ‣ Benchmarking LLM-Driven Network Configuration Repair").
* [40]
  Z. Wang, A. Cornacchia, A. Sacco, F. Galante, M. Canini, and D. Jiang (2025)
  A network arena for benchmarking ai agents on network troubleshooting.
  External Links: 2512.16381,
  [Link](https://arxiv.org/abs/2512.16381)
  Cited by: [§1](#S1.p6.1 "1. Introduction ‣ Benchmarking LLM-Driven Network Configuration Repair"),
  [§7](#S7.p4.1 "7. Related Work ‣ Benchmarking LLM-Driven Network Configuration Repair").
* [41]
  J. Wei, X. Wang, D. Schuurmans, M. Bosma, B. Ichter, F. Xia, E. Chi, Q. Le, and D. Zhou (2023)
  Chain-of-thought prompting elicits reasoning in large language models.
  External Links: 2201.11903,
  [Link](https://arxiv.org/abs/2201.11903)
  Cited by: [§5](#S5.p5.1 "5. Experimental Setup ‣ Benchmarking LLM-Driven Network Configuration Repair"),
  [§8](#S8.p1.1 "8. Discussion and Limitations ‣ Benchmarking LLM-Driven Network Configuration Repair").
* [42]
  Q. Wu, G. Bansal, J. Zhang, Y. Wu, B. Li, E. Zhu, L. Jiang, X. Zhang, S. Zhang, J. Liu, A. H. Awadallah, R. W. White, D. Burger, and C. Wang (2023)
  AutoGen: enabling next-gen llm applications via multi-agent conversation.
  External Links: 2308.08155,
  [Link](https://arxiv.org/abs/2308.08155)
  Cited by: [§6](#S6.p6.1 "6. Evaluation ‣ Benchmarking LLM-Driven Network Configuration Repair"),
  [§8](#S8.p1.1 "8. Discussion and Limitations ‣ Benchmarking LLM-Driven Network Configuration Repair").
* [43]
  S. Yao, J. Zhao, D. Yu, N. Du, I. Shafran, K. Narasimhan, and Y. Cao (2023)
  ReAct: synergizing reasoning and acting in language models.
  External Links: 2210.03629,
  [Link](https://arxiv.org/abs/2210.03629)
  Cited by: [§8](#S8.p1.1 "8. Discussion and Limitations ‣ Benchmarking LLM-Driven Network Configuration Repair").
* [44]
  L. Zheng, W. Chiang, Y. Sheng, S. Zhuang, Z. Wu, Y. Zhuang, Z. Lin, Z. Li, D. Li, E. P. Xing, H. Zhang, J. E. Gonzalez, and I. Stoica (2023)
  Judging llm-as-a-judge with mt-bench and chatbot arena.
  External Links: 2306.05685,
  [Link](https://arxiv.org/abs/2306.05685)
  Cited by: [§2.3](#S2.SS3.p7.1 "2.3. Cornetto ‣ 2. Overview ‣ Benchmarking LLM-Driven Network Configuration Repair"),
  [§4.3](#S4.SS3.p5.1 "4.3. Diagnosis Evaluator ‣ 4. Evaluation Framework ‣ Benchmarking LLM-Driven Network Configuration Repair").
* [45]
  D. Zhou, N. Schärli, L. Hou, J. Wei, N. Scales, X. Wang, D. Schuurmans, C. Cui, O. Bousquet, Q. Le, and E. Chi (2023)
  Least-to-most prompting enables complex reasoning in large language models.
  External Links: 2205.10625,
  [Link](https://arxiv.org/abs/2205.10625)
  Cited by: [§5](#S5.p5.1 "5. Experimental Setup ‣ Benchmarking LLM-Driven Network Configuration Repair").
* [46]
  Y. Zhou, J. Ruan, E. S. Wang, S. Fouladi, F. Y. Yan, K. Hsieh, and Z. Liu (2026)
  NetArena: dynamic benchmarks for ai agents in network automation.
  External Links: 2506.03231,
  [Link](https://arxiv.org/abs/2506.03231)
  Cited by: [§7](#S7.p4.1 "7. Related Work ‣ Benchmarking LLM-Driven Network Configuration Repair").

## Appendix A Fault Library

Table 4. Comprehensive Fault Catalog listing the protocols affected, the nature of the misconfiguration (Summary), and the resulting impact on the network (Expected Effect).

|  |  |  |
| --- | --- | --- |
| Protocol / Type | Summary | Expected Effect |
| BGP | eBGP neighbor configured with incorrect remote AS | eBGP session reset due to ASN mismatch, cutting off inter-AS route exchange |
|  | Administratively shut down a BGP neighbor | BGP Peering is administratively disabled, withdrawing all prefixes learnt via the neighbor |
|  | Node configured with incorrect local ASN | Misaligned local ASN breaks iBGP/eBGP sessions and splits the AS control plane |
|  | Force invalid next-hop on eBGP advertisements | Outbound policy rewrites next-hop to an unreachable address, causing downstream traffic blackholes |
|  | Remove next-hop-self from RR →\rightarrow client iBGP session | iBGP routes advertised to clients retain original eBGP next-hop, which may be unreachable from clients causing traffic blackholes |
|  | Withdraw a BGP network statement from the process | Prefix is no longer originated, withdrawing reachability from downstream peers |
|  | Remove outbound route-map from eBGP neighbor | Export policy no longer enforced, allowing infrastructure routes (loopbacks, P2P) and unintended prefixes to leak to external peers |
|  | Swap inbound and outbound route-maps on a neighbor | Inbound filters begin applying outbound and vice versa, breaking intended import/export policy |
|  | Leak router loopback by stripping export/import policies | ASBR originates its loopback /32 into eBGP and the peer accepts it because inbound filtering was removed |
|  | Break RR sessions to orphan clients | iBGP sessions removed between RR and up to 5 (exclusive) clients, orphaning them from iBGP reachability |
|  | Duplicate cluster-id across route reflectors and isolate clients on one RR | Conflicting cluster-ids cause route reflectors to drop one another’s updates, stranding clients that now depend on the misconfigured RR (cf. RFC 4456, Sec. 8) |
| OSPF | OSPF interface cost set to extreme value | Artificially high OSPF cost diverts traffic away from the link based on alternate SPF paths |
|  | Disable OSPF adjacency on a link | Removing the link from OSPF prevents adjacency formation and withdraws LSAs learned across it |
|  | Node missing OSPF area membership | Router withdraws from all OSPF areas, tearing down adjacencies and LSAs |
|  | Assign duplicate OSPF router-ID to multiple routers | OSPF adjacencies fail or LSAs rejected due to router-ID collision, fragmenting OSPF domain and blackholing traffic |
| IS-IS | Disable IS-IS on an intra-AS link | Removing the link from IS-IS prevents adjacency formation and withdraws LSPs learned across it |
|  | Demote a Level-1-2 IS-IS router to Level-1 | Reduces inter-area reachability by removing a backbone-capable router, risking L2 partitioning |
|  | Assign router to wrong IS-IS area | Router in wrong area cannot form L1 adjacencies with its physical neighbors; causes partition of L1 domain and reachability loss |
| Addressing | Duplicate loopback IPv4 addresses | Two routers share the same loopback, risking routing loops and control-plane instability |
|  | Link interfaces disagree on prefix length | One side of a point-to-point link uses a mismatched subnet mask, preventing adjacency formation |
|  | Link interfaces reside in different subnets | Interfaces on a point-to-point link move to disjoint IPv4 subnets, breaking adjacency formation |
| Device | Remove supporting static route for advertised prefix | Advertised network disappears once the backing static route is withdrawn, causing a control-plane withdraw |
| Policy | Remove permit entry from prefix-list | Prefix-list no longer matches intended prefixes, causing route filtering to block previously allowed routes |
|  | Convert BGP route-map permit clause into deny | Previously exported prefixes are now filtered, withdrawing routes from neighbors |
|  | Lower BGP local-preference on inbound policy | Reduced local-preference makes an alternate egress the best path for affected prefixes |
| Redistribution | Drop BGP →\rightarrow OSPF redistribution on an ASBR | Internal OSPF loses external reachability because Type-5 LSAs are never originated |
| Security | Insert implicit deny at top of interface ACL | Ingress traffic on the protected interface is dropped before policy permits, breaking connectivity |
|  | Insert implicit deny at top of outbound interface ACL | Egress traffic on the protected interface is dropped before policy permits, breaking connectivity |

## Appendix B Additional Results

![Refer to caption](2604.22513v1/x9.png)


(a) Diagnosis

![Refer to caption](2604.22513v1/x10.png)


(b) Localization

![Refer to caption](2604.22513v1/x11.png)


(c) Regression Rate

Figure 10. Overview of the model leaderboard using other core performance metrics: diagnosis (left) and localization (center) scores, followed by regression rate (right).



![Refer to caption](2604.22513v1/x12.png)


(a) Diagnosis

![Refer to caption](2604.22513v1/x13.png)


(b) Regression Rate

Figure 11. Diagnosis performance (left) consistently degrades with increasing input prompt tokens. The same trend is noticeable for regression rates (right) too; this potentially stems from the fact that with smaller context models might hallucinate more and break correct predicates.



![Refer to caption](2604.22513v1/x14.png)


(a) Fix Score

![Refer to caption](2604.22513v1/x15.png)


(b) Regression Rate

Figure 12. Cost-Pareto frontier with respect to average fix score (left) and regression rate (right).

Experimental support, please
[view the build logs](./2604.22513v1/__stdout.txt)
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