> Source: https://arxiv.org/html/2601.11653v1

AI Agents Need Memory Control Over More Context






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

[Back to Abstract](/abs/2601.11653v1 "Back to abstract page")

[Download PDF](/pdf/2601.11653v1 "Download PDF")

1. [Abstract](#abstract1 "In AI Agents Need Memory Control Over More Context")
2. [1 Introduction](#S1 "In AI Agents Need Memory Control Over More Context")
3. [2 Background and Related Work](#S2 "In AI Agents Need Memory Control Over More Context")
   1. [2.1 AI agents: definitions and execution patterns](#S2.SS1 "In 2 Background and Related Work ‣ AI Agents Need Memory Control Over More Context")
   2. [2.2 Memory and state as a limiting factor in multi-turn agents](#S2.SS2 "In 2 Background and Related Work ‣ AI Agents Need Memory Control Over More Context")
   3. [2.3 Cognitive compression as a principle for memory control](#S2.SS3 "In 2 Background and Related Work ‣ AI Agents Need Memory Control Over More Context")
4. [3 Agent Cognitive Compressor (ACC)](#S3 "In AI Agents Need Memory Control Over More Context")
   1. [3.1 Agent Cognitive Compressor: Definition and Role](#S3.SS1 "In 3 Agent Cognitive Compressor (ACC) ‣ AI Agents Need Memory Control Over More Context")
      1. [Formalization.](#S3.SS1.SSS0.Px1 "In 3.1 Agent Cognitive Compressor: Definition and Role ‣ 3 Agent Cognitive Compressor (ACC) ‣ AI Agents Need Memory Control Over More Context")
      2. [ACC flow (per turn).](#S3.SS1.SSS0.Px2 "In 3.1 Agent Cognitive Compressor: Definition and Role ‣ 3 Agent Cognitive Compressor (ACC) ‣ AI Agents Need Memory Control Over More Context")
   2. [3.2 Compressed Cognitive State (CCS)](#S3.SS2 "In 3 Agent Cognitive Compressor (ACC) ‣ AI Agents Need Memory Control Over More Context")
   3. [3.3 ACC Multiturn Control Loop](#S3.SS3 "In 3 Agent Cognitive Compressor (ACC) ‣ AI Agents Need Memory Control Over More Context")
5. [4 ACC in Agent Architecture Patterns](#S4 "In AI Agents Need Memory Control Over More Context")
   1. [4.1 Pattern 1: Multi-turn ReAct Agent](#S4.SS1 "In 4 ACC in Agent Architecture Patterns ‣ AI Agents Need Memory Control Over More Context")
      1. [Example: healthcare operations incident triage (multi-turn).](#S4.SS1.SSS0.Px1 "In 4.1 Pattern 1: Multi-turn ReAct Agent ‣ 4 ACC in Agent Architecture Patterns ‣ AI Agents Need Memory Control Over More Context")
   2. [4.2 Pattern 2: Multi-turn Planning Agent](#S4.SS2 "In 4 ACC in Agent Architecture Patterns ‣ AI Agents Need Memory Control Over More Context")
      1. [Example: web-grounded remediation planning.](#S4.SS2.SSS0.Px1 "In 4.2 Pattern 2: Multi-turn Planning Agent ‣ 4 ACC in Agent Architecture Patterns ‣ AI Agents Need Memory Control Over More Context")
6. [5 Agent Judge Driven Multi-Turn Evaluation](#S5 "In AI Agents Need Memory Control Over More Context")
   1. [5.1 Evaluation setup and judge agent](#S5.SS1 "In 5 Agent Judge Driven Multi-Turn Evaluation ‣ AI Agents Need Memory Control Over More Context")
   2. [5.2 Response-driven outcome evaluation](#S5.SS2 "In 5 Agent Judge Driven Multi-Turn Evaluation ‣ AI Agents Need Memory Control Over More Context")
   3. [5.3 Memory-driven evaluation: hallucination and drift](#S5.SS3 "In 5 Agent Judge Driven Multi-Turn Evaluation ‣ AI Agents Need Memory Control Over More Context")
      1. [Hallucination audit.](#S5.SS3.SSS0.Px1 "In 5.3 Memory-driven evaluation: hallucination and drift ‣ 5 Agent Judge Driven Multi-Turn Evaluation ‣ AI Agents Need Memory Control Over More Context")
      2. [Drift audit.](#S5.SS3.SSS0.Px2 "In 5.3 Memory-driven evaluation: hallucination and drift ‣ 5 Agent Judge Driven Multi-Turn Evaluation ‣ AI Agents Need Memory Control Over More Context")
      3. [Memory footprint.](#S5.SS3.SSS0.Px3 "In 5.3 Memory-driven evaluation: hallucination and drift ‣ 5 Agent Judge Driven Multi-Turn Evaluation ‣ AI Agents Need Memory Control Over More Context")
   4. [5.4 Evaluation data and scenarios](#S5.SS4 "In 5 Agent Judge Driven Multi-Turn Evaluation ‣ AI Agents Need Memory Control Over More Context")
   5. [5.5 Evaluation results and analysis](#S5.SS5 "In 5 Agent Judge Driven Multi-Turn Evaluation ‣ AI Agents Need Memory Control Over More Context")
      1. [5.5.1 Memory footprint across domains](#S5.SS5.SSS1 "In 5.5 Evaluation results and analysis ‣ 5 Agent Judge Driven Multi-Turn Evaluation ‣ AI Agents Need Memory Control Over More Context")
      2. [5.5.2 Response-driven outcome metrics](#S5.SS5.SSS2 "In 5.5 Evaluation results and analysis ‣ 5 Agent Judge Driven Multi-Turn Evaluation ‣ AI Agents Need Memory Control Over More Context")
      3. [5.5.3 Hallucination rate over turns (claim audit)](#S5.SS5.SSS3 "In 5.5 Evaluation results and analysis ‣ 5 Agent Judge Driven Multi-Turn Evaluation ‣ AI Agents Need Memory Control Over More Context")
      4. [5.5.4 Drift rate and constraint retention](#S5.SS5.SSS4 "In 5.5 Evaluation results and analysis ‣ 5 Agent Judge Driven Multi-Turn Evaluation ‣ AI Agents Need Memory Control Over More Context")
      5. [5.5.5 Why ACC outperforms](#S5.SS5.SSS5 "In 5.5 Evaluation results and analysis ‣ 5 Agent Judge Driven Multi-Turn Evaluation ‣ AI Agents Need Memory Control Over More Context")
7. [6 Conclusion](#S6 "In AI Agents Need Memory Control Over More Context")
8. [References](#bib "In AI Agents Need Memory Control Over More Context")

[License: CC BY-NC-SA 4.0](https://info.arxiv.org/help/license/index.html#licenses-available)

arXiv:2601.11653v1 [q-bio.NC] 15 Jan 2026

# AI Agents Need Memory Control Over More Context

Fouad Bousetouane
  
The University of Chicago, USA
  
[bousetouane@uchicago.edu](2601.11653v1/mailto:bousetouane@uchicago.edu)

###### Abstract

AI agents are increasingly used in long, multi-turn workflows in both research and enterprise settings. As interactions grow, agent behavior often degrades due to loss of constraint focus, error accumulation, and memory-induced drift. This problem is especially visible in real-world deployments where context evolves, distractions are introduced, and decisions must remain consistent over time.

A common practice is to equip agents with persistent memory through transcript replay or retrieval-based mechanisms. While convenient, these approaches introduce unbounded context growth and are vulnerable to noisy recall and memory poisoning, leading to unstable behavior and increased drift.

In this work, we introduce the *Agent Cognitive Compressor (ACC)*, a bio-inspired memory controller that replaces transcript replay with a bounded internal state updated online at each turn. ACC separates artifact recall from state commitment, enabling stable conditioning while preventing unverified content from becoming persistent memory.

We evaluate ACC using an agent-judge-driven live evaluation framework that measures both task outcomes and memory-driven anomalies across extended interactions. Across scenarios spanning IT operations, cybersecurity response, and healthcare workflows, ACC consistently maintains bounded memory and exhibits more stable multi-turn behavior, with significantly lower hallucination and drift than transcript replay and retrieval-based agents. These results show that cognitive compression provides a practical and effective foundation for reliable memory control in long-horizon AI agents.

###### Contents

1. [1 Introduction](#S1 "In AI Agents Need Memory Control Over More Context")
2. [2 Background and Related Work](#S2 "In AI Agents Need Memory Control Over More Context")
   1. [2.1 AI agents: definitions and execution patterns](#S2.SS1 "In 2 Background and Related Work ‣ AI Agents Need Memory Control Over More Context")
   2. [2.2 Memory and state as a limiting factor in multi-turn agents](#S2.SS2 "In 2 Background and Related Work ‣ AI Agents Need Memory Control Over More Context")
   3. [2.3 Cognitive compression as a principle for memory control](#S2.SS3 "In 2 Background and Related Work ‣ AI Agents Need Memory Control Over More Context")
3. [3 Agent Cognitive Compressor (ACC)](#S3 "In AI Agents Need Memory Control Over More Context")
   1. [3.1 Agent Cognitive Compressor: Definition and Role](#S3.SS1 "In 3 Agent Cognitive Compressor (ACC) ‣ AI Agents Need Memory Control Over More Context")
   2. [3.2 Compressed Cognitive State (CCS)](#S3.SS2 "In 3 Agent Cognitive Compressor (ACC) ‣ AI Agents Need Memory Control Over More Context")
   3. [3.3 ACC Multiturn Control Loop](#S3.SS3 "In 3 Agent Cognitive Compressor (ACC) ‣ AI Agents Need Memory Control Over More Context")
4. [4 ACC in Agent Architecture Patterns](#S4 "In AI Agents Need Memory Control Over More Context")
   1. [4.1 Pattern 1: Multi-turn ReAct Agent](#S4.SS1 "In 4 ACC in Agent Architecture Patterns ‣ AI Agents Need Memory Control Over More Context")
   2. [4.2 Pattern 2: Multi-turn Planning Agent](#S4.SS2 "In 4 ACC in Agent Architecture Patterns ‣ AI Agents Need Memory Control Over More Context")
5. [5 Agent Judge Driven Multi-Turn Evaluation](#S5 "In AI Agents Need Memory Control Over More Context")
   1. [5.1 Evaluation setup and judge agent](#S5.SS1 "In 5 Agent Judge Driven Multi-Turn Evaluation ‣ AI Agents Need Memory Control Over More Context")
   2. [5.2 Response-driven outcome evaluation](#S5.SS2 "In 5 Agent Judge Driven Multi-Turn Evaluation ‣ AI Agents Need Memory Control Over More Context")
   3. [5.3 Memory-driven evaluation: hallucination and drift](#S5.SS3 "In 5 Agent Judge Driven Multi-Turn Evaluation ‣ AI Agents Need Memory Control Over More Context")
   4. [5.4 Evaluation data and scenarios](#S5.SS4 "In 5 Agent Judge Driven Multi-Turn Evaluation ‣ AI Agents Need Memory Control Over More Context")
   5. [5.5 Evaluation results and analysis](#S5.SS5 "In 5 Agent Judge Driven Multi-Turn Evaluation ‣ AI Agents Need Memory Control Over More Context")
      1. [5.5.1 Memory footprint across domains](#S5.SS5.SSS1 "In 5.5 Evaluation results and analysis ‣ 5 Agent Judge Driven Multi-Turn Evaluation ‣ AI Agents Need Memory Control Over More Context")
      2. [5.5.2 Response-driven outcome metrics](#S5.SS5.SSS2 "In 5.5 Evaluation results and analysis ‣ 5 Agent Judge Driven Multi-Turn Evaluation ‣ AI Agents Need Memory Control Over More Context")
      3. [5.5.3 Hallucination rate over turns (claim audit)](#S5.SS5.SSS3 "In 5.5 Evaluation results and analysis ‣ 5 Agent Judge Driven Multi-Turn Evaluation ‣ AI Agents Need Memory Control Over More Context")
      4. [5.5.4 Drift rate and constraint retention](#S5.SS5.SSS4 "In 5.5 Evaluation results and analysis ‣ 5 Agent Judge Driven Multi-Turn Evaluation ‣ AI Agents Need Memory Control Over More Context")
      5. [5.5.5 Why ACC outperforms](#S5.SS5.SSS5 "In 5.5 Evaluation results and analysis ‣ 5 Agent Judge Driven Multi-Turn Evaluation ‣ AI Agents Need Memory Control Over More Context")
6. [6 Conclusion](#S6 "In AI Agents Need Memory Control Over More Context")
7. [References](#bib "In AI Agents Need Memory Control Over More Context")

## 1 Introduction

Agentic AI is moving beyond conversational assistance toward operational decision support. In enterprise settings, AI agents are increasingly expected to execute multi-step workflows, coordinate external tools, and sustain context across extended multi-turn interactions in domains such as IT operations, cybersecurity response, healthcare operations, and e-commerce. These settings differ from short-form question answering because success depends on continuity under changing requirements, reliable preservation of constraints, and consistent tracking of entities and intermediate decisions. A widely adopted execution pattern is to interleave reasoning and acting during runtime [[38](#bib.bib1 "ReAct: synergizing reasoning and acting in language models")].

Despite rapid progress in agent architectures, memory handling remains a central barrier to reliability in multi-turn workflows. The dominant implementation pattern continues to rely on transcript replay, where prior interactions are appended to the prompt. As interactions extend, this strategy inflates cost and latency, reduces selectivity by forcing attention over increasingly mixed history, and makes early mistakes harder to recover from. In practice, this presents as drift from established constraints, inconsistent adherence to required formats, and the carryover of unsupported assumptions.

Retrieval-based memory partially addresses prompt growth by storing prior interactions in an external store and retrieving top-ranked artifacts per turn [[19](#bib.bib2 "Retrieval-augmented generation for knowledge-intensive NLP tasks"), [18](#bib.bib3 "Dense passage retrieval for open-domain question answering")]. Memory orchestration systems extend this idea by managing what stays in the prompt versus what is stored externally [[29](#bib.bib4 "MemGPT: towards LLMs as operating systems")]. Reflection-based approaches store distilled lessons or self-critique to influence later turns [[34](#bib.bib5 "Reflexion: language agents with verbal reinforcement learning")]. These methods are useful, but they leave an important gap for operational settings. Retrieved or summarized text is not equivalent to a controlled internal state. Retrieval optimizes for relevance signals such as semantic similarity, not for preserving the currently active constraints, and selection errors can compound across turns. What agents often need to preserve is a small set of invariants such as goals, policy constraints, service-level constraints, entity identifiers, and confirmed decisions, while continuously integrating new evidence and ignoring distractions.

We frame this as a memory control problem. Sustained multi-turn performance requires an explicit internal state that is updated online at each turn, rather than an uncontrolled accumulation of text. Biological cognition provides a useful analogy. Human working memory is capacity-limited and relies on compression, selection, and executive control [[2](#bib.bib6 "Working memory"), [11](#bib.bib7 "The magical number 4 in short-term memory: a reconsideration of mental storage capacity")]. Rather than replaying experience verbatim, humans maintain compact task representations that separate recent episodic updates from stable semantic structure [[35](#bib.bib8 "Episodic and semantic memory")]. This motivates an engineering principle for agentic systems: carry forward a bounded working state that preserves task-critical invariants while filtering noise.

Based on this principle, we introduce the *Agent Cognitive Compressor (ACC)*, a cognitively inspired memory controller that replaces transcript replay with a bounded Compressed Cognitive State (CCS). At each turn, ACC updates CCS using the current interaction, the previous CCS, and a small set of retrieved artifacts. The design explicitly separates artifact recall from state commitment. Retrieval proposes candidate information, while compression commits only what is required for control. CCS then conditions downstream reasoning and action, enabling stable behavior across extended multi-turn interactions with bounded memory growth.

We evaluate the ACC agent against two alternative agents, a transcript replay baseline and a retrieval-based agent, on multi-turn scenarios designed to reflect operational conditions, including evolving constraints, injected distractions, and entity-dependent decisions. Our evaluation uses an agent-judge-driven live framework that issues the same query to all three agents at each turn and produces turn-level scores for task outcome metrics, with bias controls such as blinding and randomized presentation order [[41](#bib.bib10 "Judging LLM-as-a-judge with MT-bench and chatbot arena"), [12](#bib.bib11 "Length-controlled alpacaeval: a simple way to debias automatic evaluators")]. To quantify memory-driven anomalies, we use a memory-aware judge that audits hallucination and drift against a judge-maintained canonical state, and we report direct measurements of memory footprint across turns. Results show that the ACC agent improves multi-turn consistency and constraint retention while substantially reducing persistent context size. The remainder of the paper is organized as follows. Section [2](#S2 "2 Background and Related Work ‣ AI Agents Need Memory Control Over More Context") reviews background and related work on agent architectures and memory. Section [3](#S3 "3 Agent Cognitive Compressor (ACC) ‣ AI Agents Need Memory Control Over More Context") introduces the Agent Cognitive Compressor (ACC) and the Compressed Cognitive State (CCS), and Section [4](#S4 "4 ACC in Agent Architecture Patterns ‣ AI Agents Need Memory Control Over More Context") shows how ACC integrates into common agent architecture patterns. Section [5](#S5 "5 Agent Judge Driven Multi-Turn Evaluation ‣ AI Agents Need Memory Control Over More Context") presents the agent-judge-driven multi-turn evaluation framework and reports the empirical results. Section [6](#S6 "6 Conclusion ‣ AI Agents Need Memory Control Over More Context") concludes with implications and directions for future work.

## 2 Background and Related Work

Modern AI agents extend large language models with an orchestration layer that manages control flow, tool invocation, and state across multi-step execution. This section reviews common agent patterns and the memory mechanisms used in practice, then motivates cognitive compression as a principle for stabilizing multi-turn agent behavior.

### 2.1 AI agents: definitions and execution patterns

AI agents are commonly defined as goal-directed systems that generate sequences of actions while maintaining internal state that influences future decisions [[6](#bib.bib99 "Agentic systems: a guide to transforming industries with vertical ai agents"), [30](#bib.bib75 "Generative agents: interactive simulacra of human behavior"), [8](#bib.bib101 "AI agents for everyone: a practical guide to building and understanding ai agents without complexity")]. Many deployed designs follow a loop that interleaves reasoning and acting, where the model produces intermediate reasoning and then invokes tools or actions, updating state from outcomes [[7](#bib.bib100 "Physical ai agents: integrating cognitive intelligence with real-world action")]. Subsequent work extends this pattern with planning modules, tool selection and tool learning, and structured execution graphs that make routing and retries explicit [[24](#bib.bib76 "Plan-and-solve prompting"), [33](#bib.bib77 "Toolformer: language models can teach themselves to use tools"), [37](#bib.bib78 "AgentGraph: structured agent execution with graph control")]. These ideas are reflected in widely used agent frameworks that provide programmable control layers for multi-step workflows.

System-level patterns also recur across implementations. Single-agent designs emphasize sequential reasoning and tool use [[38](#bib.bib1 "ReAct: synergizing reasoning and acting in language models")]. Multi-agent designs decompose tasks across roles and coordinate through message passing [[20](#bib.bib79 "CAMEL: communicative agents for mind exploration"), [36](#bib.bib14 "AutoGen: enabling next-gen llm applications via multi-agent conversation")]. Human-in-the-loop designs incorporate feedback or preference signals to guide behavior [[5](#bib.bib80 "Training a helpful and harmless assistant with rlhf")] [[6](#bib.bib99 "Agentic systems: a guide to transforming industries with vertical ai agents")]. Domain-scoped agents restrict tools and objectives to improve reliability in operational workflows [[9](#bib.bib81 "Vertical ai agents for enterprise decision support")]. Across these variants, a shared practical challenge remains: the agent must preserve task state across turns, even as requirements evolve and distractions appear.

### 2.2 Memory and state as a limiting factor in multi-turn agents

Most deployed agents represent state implicitly through text. Transcript replay preserves information by appending past turns, but prompt length grows with turn count, which increases cost and latency and reduces selectivity [[31](#bib.bib82 "Train short, test long: attention with linear biases"), [21](#bib.bib73 "Lost in the middle: how language models use long contexts")]. Empirical studies on long context behavior also report that models can under-attend to relevant early tokens and over-attend to recent or noisy information, which contributes to drift as interactions extend [[21](#bib.bib73 "Lost in the middle: how language models use long contexts")]. These effects are especially visible in tasks where constraints and output formats must remain stable across turns.

Retrieval-based memory reduces prompt growth by storing past interactions or documents externally and retrieving relevant artifacts per turn [[19](#bib.bib2 "Retrieval-augmented generation for knowledge-intensive NLP tasks"), [18](#bib.bib3 "Dense passage retrieval for open-domain question answering")]. While effective for knowledge access, retrieval optimizes for relevance signals that may not align with control relevance. Retrieved text can be locally similar yet inconsistent with the active constraints, and retrieval can surface outdated or injected artifacts, which destabilizes multi-turn control [[1](#bib.bib26 "Self-rag: learning to retrieve, generate, and critique through self-reflection")]. Memory orchestration systems introduce policies for moving information between short-term and long-term storage [[29](#bib.bib4 "MemGPT: towards LLMs as operating systems")], and reflection-based methods store distilled lessons or critiques [[34](#bib.bib5 "Reflexion: language agents with verbal reinforcement learning")]. These approaches improve efficiency and learning, but they still treat text artifacts as the primary carrier of state, without enforcing a structured update rule for what should persist as committed state versus what should remain episodic.

This motivates a central question for agent design. Are multi-turn failures primarily a capacity problem, or do they stem from inadequate control over what becomes persistent memory?

### 2.3 Cognitive compression as a principle for memory control

Cognitive science suggests that sustained multi-step reasoning is enabled by compact internal representations rather than verbatim replay. Human working memory is capacity-limited and relies on selection and executive control to maintain task-relevant state [[2](#bib.bib6 "Working memory"), [11](#bib.bib7 "The magical number 4 in short-term memory: a reconsideration of mental storage capacity")]. The episodic buffer hypothesis emphasizes temporary binding into structured representations that support reasoning under constraint [[3](#bib.bib53 "The episodic buffer: a new component of working memory?")]. Complementary Learning Systems theory distinguishes fast episodic acquisition from slower semantic consolidation, which reduces interference while preserving adaptability [[25](#bib.bib55 "Why there are complementary learning systems in the hippocampus and neocortex: insights from the successes and failures of connectionist models of learning and memory")]. Predictive coding frameworks similarly model cognition as maintaining compact internal hypotheses that are updated by prediction error [[32](#bib.bib9 "Predictive coding in the visual cortex: a functional interpretation of some extra-classical receptive-field effects"), [13](#bib.bib85 "The free-energy principle")]. Recent accounts further formalize forgetting and distortion as forms of semantic compression under resource constraints, where memory is optimized to preserve decision-relevant structure rather than a faithful record of history [[27](#bib.bib57 "Optimal forgetting: semantic compression of episodic memories")].

These perspectives converge on a shared engineering principle. Reliable multi-turn behavior benefits from continuously distilling experience into a bounded, decision-relevant internal state rather than accumulating raw history. In the next section, we translate this principle into a memory control mechanism through the *Agent Cognitive Compressor (ACC)*, which treats agent memory as an explicit compression and commitment process designed to preserve invariants while resisting drift.

## 3 Agent Cognitive Compressor (ACC)

The previous section established that long horizon agent failures such as drift, constraint erosion, and hallucination compounding are driven primarily by uncontrolled memory growth rather than limitations in model expressivity. Transcript replay expands context approximately linearly with interaction length, increasing non essential tokens that compete for attention and amplifying early errors through continual re exposure. Retrieval based memory reduces prompt growth, but it optimizes for semantic similarity rather than decision relevance, allowing recalled artifacts to perturb goals, constraints, and intermediate assumptions in unstable ways.

Crucially, both paradigms treat memory as accumulated text and provide no principled write path for internal state. They do not specify what should persist, what should be revised, and what should be discarded. As horizons increase, this absence of memory governance leads to drift, loss of task invariants, and hallucinations induced by irrelevant, stale, or inconsistently recalled context.

We argue, grounded in the prior work reviewed in Section [2](#S2 "2 Background and Related Work ‣ AI Agents Need Memory Control Over More Context"), that long horizon reliability requires explicit memory control: a compact, structured set of decision critical variables, including goals, constraints, entities, and relations, updated selectively as new evidence arrives. This requirement is bio inspired. Humans sustain coherence by maintaining a bounded working state that is continuously regulated by salience, constraints, and expected utility.

The motivating question is: *Can we equip agents with a bio inspired cognitive memory, a bounded working state that keeps them focused while reducing context growth, drift, and hallucination compounding?*

We address this question by introducing the *Agent Cognitive Compressor (ACC)*, a dedicated memory controller that governs how an agent’s internal cognitive state evolves across interaction turns.

### 3.1 Agent Cognitive Compressor: Definition and Role

![Refer to caption](2601.11653v1/acc2.png)


Figure 1: Agent architecture incorporating the Agent Cognitive Compressor (ACC).
ACC operates as a cognitive memory controller that constructs and commits a bounded Compressed Cognitive State (CCS) via a schema constrained Cognitive Compressor Model (CCM).
CCS is the sole persistent internal state maintained across turns and conditions downstream reasoning, tool use, and action,
while ACC remains decoupled from policy execution and environment interaction.

The *Agent Cognitive Compressor (ACC)* is a memory control mechanism embedded within an agent’s execution loop. ACC is not an autonomous agent and it does not implement a reasoning or acting policy. It does not perform planning, tool selection, or action selection. Its responsibility is strictly regulatory. ACC governs how the agent’s internal cognitive state is constructed, updated, and committed across interaction turns.

As illustrated in Figure [1](#S3.F1 "Figure 1 ‣ 3.1 Agent Cognitive Compressor: Definition and Role ‣ 3 Agent Cognitive Compressor (ACC) ‣ AI Agents Need Memory Control Over More Context"), ACC sits between transient interaction signals, externally stored evidence, and the agent’s reasoning engine. Rather than accumulating raw dialogue history or injecting retrieved text directly into the reasoning prompt, ACC enforces bounded persistence by writing a compact internal state that captures only what must remain stable for coherent long horizon control. The central design commitment is that ACC writes exactly one persistent state variable and updates it through controlled replacement rather than unbounded accumulation.

ACC replaces transcript replay and retrieval only context injection with an explicit internal state called the *Compressed Cognitive State (CCS)*. CCS is the sole persistent internal representation carried across turns. The reasoning engine conditions on the committed state from the previous turn together with the current user input, not on the full transcript, tool traces, or raw recalled documents. This design preserves a stable signal to noise ratio as the interaction horizon grows, while keeping long horizon commitments explicit.

A defining property of ACC is that state persistence is schema governed. CCS is not a free form summary. It is a structured cognitive state constrained by an explicit schema 𝒮CCS\mathcal{S}\_{\mathrm{CCS}} that specifies required fields, semantic interpretation, and allowable structure. The schema acts as a contract between compression and reasoning. It makes the write path predictable, bounded, and verifiable, and it enables deterministic parsing and validation without an additional model call.

At each turn, ACC aggregates the current turn interaction signal, the previously committed cognitive state, and a bounded set of recalled artifacts from external memory. An *artifact* is any externally persisted evidence that may matter for future control, including prior user constraints, prior agent commitments, tool outputs, retrieved documents, logs, or structured facts extracted earlier. Artifacts are stored outside CCS, typically in an indexed store such as a vector database augmented with metadata and provenance. Retrieval is used to propose candidate evidence, not to update internal state.

ACC then invokes a language model referred to as the *Cognitive Compressor Model (CCM)* to synthesize the next committed cognitive state under the CCS schema constraint. The CCM can be implemented in two ways. A general purpose LLM can be used with a schema conditioned prompt that constrains outputs to comply with 𝒮CCS\mathcal{S}\_{\mathrm{CCS}}. However, for deployment we recommend a fine tuned compressor specialized model, preferably a small language model, to reduce latency and cost overhead while improving schema adherence and reducing output variance. In all cases, the CCM performs abstraction, normalization, and selective incorporation of decision critical information into CCS, and it is not responsible for generating the agent’s final response.

##### Formalization.

Let xtx\_{t} denote the turn level interaction signal at turn tt, let CCSt−1\mathrm{CCS}\_{t-1} denote the previously committed cognitive state, let ℳ\mathcal{M} denote an external artifact store, and let 𝒮CCS\mathcal{S}\_{\mathrm{CCS}} denote the CCS schema. ACC recalls a bounded set of candidate artifacts

|  |  |  |  |
| --- | --- | --- | --- |
|  | At=ℛACC​(xt,CCSt−1;ℳ),A\_{t}=\mathcal{R}\_{\mathrm{ACC}}\!\left(x\_{t},\mathrm{CCS}\_{t-1};\mathcal{M}\right), |  | (1) |

filters recalled artifacts using a decision qualification gate

|  |  |  |  |
| --- | --- | --- | --- |
|  | At+={a∈At|𝒬​(a,CCSt−1,xt)=1},A\_{t}^{+}=\left\{\,a\in A\_{t}\;\middle|\;\mathcal{Q}\!\left(a,\mathrm{CCS}\_{t-1},x\_{t}\right)=1\,\right\}, |  | (2) |

and computes the next committed cognitive state under the schema constraint

|  |  |  |  |
| --- | --- | --- | --- |
|  | CCSt=𝒞θ​(xt,CCSt−1,At+;𝒮CCS),\mathrm{CCS}\_{t}=\mathcal{C}\_{\theta}\!\left(x\_{t},\mathrm{CCS}\_{t-1},A\_{t}^{+};\mathcal{S}\_{\mathrm{CCS}}\right), |  | (3) |

where 𝒞θ\mathcal{C}\_{\theta} denotes the schema constrained compression operator implemented by the CCM.

##### ACC flow (per turn).

Given the formulation above, the ACC update proceeds as follows.

* •

  Observe the current interaction signal xtx\_{t} and read the previously committed state CCSt−1\mathrm{CCS}\_{t-1}.
* •

  Recall a bounded candidate set AtA\_{t} from the external store ℳ\mathcal{M} conditioned on (xt,CCSt−1)(x\_{t},\mathrm{CCS}\_{t-1}).
* •

  Qualify recalled items using 𝒬\mathcal{Q} to produce At+A\_{t}^{+}, retaining only decision relevant evidence.
* •

  Commit the next state by running the CCM with schema constraint 𝒮CCS\mathcal{S}\_{\mathrm{CCS}} to produce CCSt\mathrm{CCS}\_{t}.
* •

  Replace the prior state with the committed state, so CCSt\mathrm{CCS}\_{t} fully replaces CCSt−1\mathrm{CCS}\_{t-1}.

The updated state CCSt\mathrm{CCS}\_{t} fully replaces CCSt−1\mathrm{CCS}\_{t-1} and becomes the sole persistent memory used by the agent in subsequent turns. Internal memory does not grow through accumulation. It evolves through controlled state transitions. This replacement semantics distinguishes ACC from replay based and retrieval based memory designs, and it makes the write path explicit and auditable.

Finally, ACC enforces a strict separation between artifact recall and state commitment. Retrieved artifacts are treated as external evidence and cannot directly modify the cognitive state unless explicitly incorporated by the CCM under the CCS schema constraint. This separation limits uncontrolled state mutation, reduces sensitivity to retrieval noise, and improves long horizon stability. Figure [2](#S3.F2 "Figure 2 ‣ ACC flow (per turn). ‣ 3.1 Agent Cognitive Compressor: Definition and Role ‣ 3 Agent Cognitive Compressor (ACC) ‣ AI Agents Need Memory Control Over More Context") provides a detailed view of the ACC state commitment mechanism used to produce CCSt\mathrm{CCS}\_{t}.

![Refer to caption](2601.11653v1/acc_diagram_aligned_white.png)


Figure 2: ACC state commitment mechanism for producing the next Compressed Cognitive State CCSt\mathrm{CCS}\_{t} under the schema constraint 𝒮CCS\mathcal{S}\_{\mathrm{CCS}}, using the current interaction xtx\_{t}, the previously committed state CCSt−1\mathrm{CCS}\_{t-1}, and the qualified recalled set At+A\_{t}^{+}.

The following subsection defines the Compressed Cognitive State (CCS) itself and details its schema, cognitive motivation, and role as the minimal internal representation required to sustain coherent reasoning over extended interactions.

### 3.2 Compressed Cognitive State (CCS)

The *Compressed Cognitive State (CCS)* is the bounded internal representation maintained by ACC across interaction turns. CCS is neither a transcript summary nor a memory cache. Instead, it is a control oriented cognitive state designed to preserve decision critical information while explicitly discarding irrelevant, redundant, or low utility detail.

CCS is bio inspired. Its design is motivated by how humans maintain task relevant mental state during extended problem solving, not by replaying experience verbatim, but by retaining a compact internal representation of what changed, what matters, what constraints apply, and what goal is being pursued. Cognitive science and neuroscience literature consistently show that human working cognition relies on abstraction, salience, and relational structure rather than raw episodic recall. CCS mirrors this principle by encoding only the minimal set of variables required to sustain coherent reasoning over time [[4](#bib.bib86 "Working memory: theories, models, and controversies"), [26](#bib.bib87 "The magical number seven, plus or minus two: some limits on our capacity for processing information"), [28](#bib.bib88 "Memory and attention: an introduction to human information processing"), [10](#bib.bib89 "The magical number 4 in short-term memory: a reconsideration of mental storage capacity"), [17](#bib.bib90 "Thinking, fast and slow")]. In ACC, this cognitive principle is operationalized as typed, bounded fields that make the agent’s commitments explicit rather than latent in a growing transcript.

Accordingly, CCS is defined as a schema with explicit, typed components that correspond to functional elements of human cognition. This schema is not merely descriptive documentation. It is actively enforced during execution. At each turn, ACC prompts the Cognitive Compressor Model (CCM) to emit a CCS instance conforming to the schema 𝒮CCS\mathcal{S}\_{\mathrm{CCS}}, after which the output is deterministically parsed and validated. This validation step does not require an additional model call. Enforcing schema compliance reduces output variance, prevents missing or malformed state, and makes CCS instances auditable, comparable, stable, and instrumentable across turns.

Each component of the CCS schema serves a distinct functional role analogous to a cognitive function in human reasoning. Together, they form a minimal decomposition of the variables required to maintain coherent long horizon control:

* •

  Episodic trace captures what changed in the current turn, analogous to short term event updating in human working memory.
* •

  Semantic gist encodes the dominant intent or topic, reflecting how humans abstract meaning beyond surface form.
* •

  Focal entities (typed) represent canonicalized objects or actors, supporting stable reference resolution over long horizons.
* •

  Relational map encodes causal and temporal dependencies, mirroring human causal and temporal reasoning.
* •

  Goal orientation represents the persistent objective guiding the interaction, analogous to goal maintenance in executive control.
* •

  Constraints encode task, policy, or safety rules that remain invariant, similar to rule based inhibition in human cognition.
* •

  Predictive cue captures the expected next cognitive operation, resembling anticipatory planning in problem solving.
* •

  Uncertainty signal explicitly represents unresolved or low confidence state, discouraging overconfident inference.
* •

  Retrieved artifacts retain references to external evidence, analogous to consulting notes or tools without internalizing raw content.

Figure [3](#S3.F3 "Figure 3 ‣ 3.2 Compressed Cognitive State (CCS) ‣ 3 Agent Cognitive Compressor (ACC) ‣ AI Agents Need Memory Control Over More Context") illustrates a CCS instance for an IT operations scenario, serialized using a lightweight TOON style token oriented representation. TOON here denotes a compact token oriented serialization designed to minimize entropy while preserving legibility. Compared to transcript replay, this representation is intentionally decision oriented. The encoding exposes CCS as a structured cognitive state composed of typed entities, persistent goals, explicit constraints, and stable relational predicates, while external evidence is retained as referenced artifacts with provenance rather than injected text. This design makes the agent’s internal state interpretable, bounded, and directly usable for downstream reasoning and control.

Figure 3: Example Compressed Cognitive State (CCS) for an IT operations task, serialized using a TOON style token oriented representation.

user\_query:
  
We see intermittent 502 errors in Nginx after enabling HTTP/2. I cannot restart during business hours. Give a safe mitigation and the next checks.
ccs\_t:
episodic\_trace:
  
observed(502\_spikes after(enable(http2)))
logged(nginx\_error upstream\_closed\_early)
constraint(no\_restart during(business\_hours))
semantic\_gist:
  
mitigate(502) & diagnose(upstream\_instability)
focal\_entities:
  
host(vm\_ubuntu22\_04) 
service(nginx) 
service(node\_upstream) 
feature(http2) 
signal(error\_502)
relational\_map:
  
timing(502\_spikes after(http2\_enable))
possible(upstream\_timeout 502)
possible(upstream\_connection\_close 502)
goal\_orientation:
  
reduce(502\_rate within(10min)) & preserve(service\_availability)
constraints:
  
no\_restart(nginx) 
reload\_allowed(nginx) 
safe\_change(minimal) 
avoid(speculation)
predictive\_cue:
  
check(upstream\_latency)  check(node\_memory\_growth)  validate(nginx\_timeouts)
uncertainty\_signal:
  
level(medium)  gaps(root\_cause not\_confirmed)
retrieved\_artifacts:
  
nginx\_error\_snippet(upstream\_prematurely\_closed)
recent\_change(enable\_http2) 
constraint\_note(no\_restart)

Crucially, CCS is not static. It is continuously constructed, evaluated, and selectively updated at each interaction turn. The following section describes how CCS participates in the ACC multiturn control loop, governing recall, filtering, prediction, and state commitment over time.

### 3.3 ACC Multiturn Control Loop

ACC implements schema governed memory control as a per turn state transition system over a single persistent variable, CCSt\mathrm{CCS}\_{t}. At turn tt, the agent policy conditions on the current user input together with the previously committed state. The completed turn is then treated as the interaction signal xtx\_{t} for ACC, which performs recall, qualification, and schema constrained commitment to produce the next state. Algorithm [1](#alg1 "Algorithm 1 ‣ 3.3 ACC Multiturn Control Loop ‣ 3 Agent Cognitive Compressor (ACC) ‣ AI Agents Need Memory Control Over More Context") summarizes the multi-turn ACC update process. At each turn, ACC (i) recalls a bounded set of candidate artifacts from ℳ\mathcal{M}, (ii) applies a qualification gate to retain only decision-relevant evidence, and (iii) commits the next bounded state CCSt\mathrm{CCS}\_{t} under the schema constraint 𝒮CCS\mathcal{S}\_{\mathrm{CCS}}.

Algorithm 1  ACC multiturn cognitive state commitment and evidence persistence

1:Initial committed state CCS0\mathrm{CCS}\_{0}, external artifact store ℳ\mathcal{M}, CCS schema 𝒮CCS\mathcal{S}\_{\mathrm{CCS}}, horizon TT

2:CCS←CCS0\mathrm{CCS}\leftarrow\mathrm{CCS}\_{0}

3:for t=1t=1 to TT do

4:  Input: observe turn interaction signal xtx\_{t}

5:    *// xtx\_{t} is the turn level interaction record provided to ACC*

6:  At←ℛACC​(xt,CCS;ℳ)A\_{t}\leftarrow\mathcal{R}\_{\mathrm{ACC}}(x\_{t},\mathrm{CCS};\mathcal{M})

7:    *// recall a bounded candidate artifact set from ℳ\mathcal{M}*

8:  At+←{a∈At∣𝒬​(a,CCS,xt)=1}A\_{t}^{+}\leftarrow\{\,a\in A\_{t}\mid\mathcal{Q}(a,\mathrm{CCS},x\_{t})=1\,\}

9:    *// filter recalled artifacts by decision qualification*

10:  CCSt←𝒞θ​(xt,CCS,At+;𝒮CCS)\mathrm{CCS}\_{t}\leftarrow\mathcal{C}\_{\theta}\big(x\_{t},\mathrm{CCS},A\_{t}^{+};\mathcal{S}\_{\mathrm{CCS}}\big)

11:    *// commit the next state via the schema constrained CCM*

12:  Commit: CCS←CCSt\mathrm{CCS}\leftarrow\mathrm{CCS}\_{t}

13:    *// CCSt\mathrm{CCS}\_{t} fully replaces the previously committed state*

14:  Agent execution: decisiont←Agent​(CCSt,role,tools)\mathrm{decision}\_{t}\leftarrow\mathrm{Agent}(\mathrm{CCS}\_{t},\mathrm{role},\mathrm{tools})

15:    *// decisiont\mathrm{decision}\_{t} includes the turn output and any tool actions*

16:  Evidence persistence: ℳ←ℳ∪Store​(xt,decisiont)\mathcal{M}\leftarrow\mathcal{M}\cup\mathrm{Store}(x\_{t},\mathrm{decision}\_{t})

17:    *// store the new interaction as future evidence for recall*

18:end for

This loop makes the control semantics explicit. The only persistent internal memory is the committed state, updated once per turn through a schema constrained commitment operation. Recall produces candidate evidence, qualification restricts which evidence may be considered, and commitment determines what is incorporated into CCSt\mathrm{CCS}\_{t}. The result is a bounded, inspectable, and repeatable update mechanism that supports stable long horizon behavior by construction.

* •

  Bounded persistence. The internal state remains constant in size across turns because only CCSt\mathrm{CCS}\_{t} persists.
* •

  Explicit commitment. State changes occur only via 𝒞θ​(⋅)\mathcal{C}\_{\theta}(\cdot) under 𝒮CCS\mathcal{S}\_{\mathrm{CCS}}, which makes updates auditable and comparable across turns.
* •

  Robust recall interface. Retrieval proposes AtA\_{t} but only qualified evidence At+A\_{t}^{+} is eligible to influence commitment.
* •

  Stable conditioning. The policy π\pi receives a fixed format state rather than a growing transcript, reducing sensitivity to horizon length.
* •

  Drift and hallucination suppression. Commitments are refreshed through structured state transition, while irrelevant or stale context is filtered before it can affect the next state.

## 4 ACC in Agent Architecture Patterns

ACC integrates into common agent control loops by acting as a memory control mechanism that commits a bounded CCSt\mathrm{CCS}\_{t} at each turn. We describe two patterns that cover a large portion of enterprise agent deployments: a ReAct multi-turn tool agent and a planning agent with an explicit plan, execute, reflect cycle. Figure [4](#S4.F4 "Figure 4 ‣ 4 ACC in Agent Architecture Patterns ‣ AI Agents Need Memory Control Over More Context") summarizes both flows.

![Refer to caption](2601.11653v1/ReACT_ACC.png)


(a) ReAct multi-turn loop with ACC committing CCSt\mathrm{CCS}\_{t} prior to REASON, and a multi-turn return from ACT to ACC.

![Refer to caption](2601.11653v1/acc_planning.jpeg)


(b) Planning agent loop: ACC →\rightarrow REASON (plan) →\rightarrow ACT →\rightarrow ACC →\rightarrow REFLECT (stop or repeat).

Figure 4: ACC integration patterns in agent architectures: ReAct multi-turn tool execution (left) and plan execute reflect control (right).

### 4.1 Pattern 1: Multi-turn ReAct Agent

In ReAct-style agents, execution alternates between reasoning and tool actions. ACC is invoked once per turn to commit CCSt\mathrm{CCS}\_{t}, which then conditions the next reasoning step (Fig. [4(a)](#S4.F4.sf1 "In Figure 4 ‣ 4 ACC in Agent Architecture Patterns ‣ AI Agents Need Memory Control Over More Context")). This makes long-run consistency depend on a bounded state rather than on replaying a growing transcript or injecting retrieved text into the prompt.

In this pattern, the turn flow is explicit.

1. 1.

   ACC commits CCSt\mathrm{CCS}\_{t} from the current interaction signal xtx\_{t}, the prior state CCSt−1\mathrm{CCS}\_{t-1}, and qualified evidence.
2. 2.

   The reasoning step uses (xt,CCSt)(x\_{t},\mathrm{CCS}\_{t}) to decide the next diagnostic or action.
3. 3.

   The agent performs ACT, producing tool outputs and intermediate observations.
4. 4.

   The next turn returns to ACC, which updates the state by replacing CCSt\mathrm{CCS}\_{t} with CCSt+1\mathrm{CCS}\_{t+1}.

##### Example: healthcare operations incident triage (multi-turn).

Consider an agent supporting an analytics team during an intermittent ingestion failure in a clinical data pipeline. The conversation spans many turns as the user provides new evidence and requests safe mitigations under operational constraints. Tool outputs are verbose and repetitive.

ACC preserves a compact set of invariants while evidence grows externally.

* •

  Constraints that must hold. For example, no disruptive restarts during clinic hours and only read-only diagnostics until the maintenance window.
* •

  Verified entities and scope. For example, pipeline name, environment, affected job IDs, and time window.
* •

  Progress and commitments. For example, checks already executed, active hypothesis, and the next best diagnostic.

Without ACC, transcript replay amplifies noise and early guesses, and retrieval-only memory can surface stale runbooks that perturb control. With ACC, the agent stays anchored to committed constraints and verified state, which reduces repetition and drift across turns.

### 4.2 Pattern 2: Multi-turn Planning Agent

Planning agents make the plan explicit and include a reflection step that decides whether to stop, revise, or continue. ACC strengthens this loop by maintaining bounded plan commitments and validated facts across iterations (Fig. [4(b)](#S4.F4.sf2 "In Figure 4 ‣ 4 ACC in Agent Architecture Patterns ‣ AI Agents Need Memory Control Over More Context")). The planning flow is typically:

1. 1.

   ACC commits CCSt\mathrm{CCS}\_{t} capturing the current goal, constraints, and validated state.
2. 2.

   The reasoning step proposes or updates a plan conditioned on CCSt\mathrm{CCS}\_{t}.
3. 3.

   The agent executes one or more steps, often using web search or enterprise search tools.
4. 4.

   ACC updates the state to CCSt+1\mathrm{CCS}\_{t+1} by committing only validated outcomes and stable commitments.
5. 5.

   Reflection uses CCSt+1\mathrm{CCS}\_{t+1} to decide whether to stop or repeat with targeted revisions.

##### Example: web-grounded remediation planning.

Consider a planning agent drafting a remediation plan for a newly disclosed software vulnerability using web search. Search results are noisy: some pages are outdated, speculative, or biased.

ACC prevents unverified content from becoming persistent state by committing only:

* •

  Validated facts with provenance. For example, affected versions and official mitigation steps from authoritative sources.
* •

  Hard constraints. For example, maintenance window, approval gates, and communication policy.
* •

  Plan commitments and progress. For example, selected option, open questions, and the next evidence needed.

This reduces drift under conflicting sources and makes reflection more reliable because it operates over a stable, bounded record of what is confirmed, what is constrained, and what remains uncertain.

Across both patterns, ACC enables the same core property: external content and tool outputs can scale with task complexity, while the internal state that drives decisions remains bounded, structured, and resistant to drift.

## 5 Agent Judge Driven Multi-Turn Evaluation

Evaluating AI agents is difficult because many tasks are open ended, success depends on multi-turn continuity, and errors compound as interactions extend. Recent work shows that LLM-based judging can approximate human preference for open ended answers and enables scalable comparisons without gold labels [[40](#bib.bib24 "Judging llm-as-a-judge with mt-bench and chatbot arena"), [23](#bib.bib25 "G-eval: nlg evaluation using gpt-4 with better human alignment")]. Agent benchmarks further highlight that failures in multi-step settings are often driven by instruction-following breakdowns and multi-turn consistency issues rather than single-turn fluency [[22](#bib.bib21 "AgentBench: evaluating llms as agents")]. At the same time, surveys emphasize that agent evaluation remains fragmented, with no single standard that jointly measures task outcomes and memory reliability in multi-turn settings [[15](#bib.bib93 "Evaluating llm-based agents for multi-turn conversations: a survey"), [39](#bib.bib96 "Survey on evaluation of LLM-based agents")].

This gap is central to ACC. ACC targets stability by controlling what persists in memory, so evaluation must quantify not only response quality, but also memory-driven failures such as hallucination carryover and drift from established constraints. We introduce an evaluation framework for multi-turn agents that couples response-driven outcome scoring with memory-driven auditing of hallucination and drift, under a single judge-controlled live testing process.

### 5.1 Evaluation setup and judge agent

We compare three different agents under identical multi-turn scenarios: a baseline agent that replays transcript history, a retrieval agent that retrieves context from its own isolated store, and the proposed ACC agent that carries a bounded Compressed Cognitive State. We evaluate across multiple domains to avoid conclusions that are specific to one task family. Our scenarios cover IT operations, cybersecurity response, healthcare operations, and finance workflows.

The evaluation is driven by an agent judge, not a static grader prompt. For each turn, the judge issues a live query, then all three agents answer. In our implementation we execute agents in a fixed live order, baseline then retrieval then ACC agent, and then call the judge to score the three answers for that turn. The judge maintains a canonical memory updated from user queries and prior canonical memory only, and uses that canonical memory as the reference for both scoring and memory auditing.

### 5.2 Response-driven outcome evaluation

At turn tt, the judge query is xtx\_{t} and agent aa returns answer ytay\_{t}^{a}. The judge assigns outcome scores on a 0 to 10 scale for a small set of task oriented metrics that remain stable across domains.

1. 1.

   Relevance, alignment to the request and constraints
2. 2.

   Answer quality, usefulness and correctness for the task
3. 3.

   Instruction following, compliance with explicit format and limits
4. 4.

   Coherence, clarity and internal consistency

We denote the score for metric mm as st,ma∈[0,10]s\_{t,m}^{a}\in[0,10]. For each metric we report the mean score across turns

|  |  |  |
| --- | --- | --- |
|  | s¯ma=1T​∑t=1Tst,ma,\bar{s}\_{m}^{a}=\frac{1}{T}\sum\_{t=1}^{T}s\_{t,m}^{a}, |  |

and we report variability across turns to capture stability under extended multi-turn conditions. To reduce judge bias, we blind agent identities during scoring, randomize presentation order, and bound visible context length. We follow established recommendations to control position and verbosity effects and to log the full judge configuration for reproducibility [[40](#bib.bib24 "Judging llm-as-a-judge with mt-bench and chatbot arena"), [14](#bib.bib97 "A survey on LLM-as-a-judge"), [16](#bib.bib98 "Validating LLM-as-a-judge systems in the absence of gold labels")].

### 5.3 Memory-driven evaluation: hallucination and drift

Outcome scores alone can miss memory failures that emerge over time. We therefore add two memory-driven evaluations grounded in the judge canonical memory.

##### Hallucination audit.

For each answer ytay\_{t}^{a}, the judge extracts a set of atomic claims and labels each claim as supported or unsupported using evidence restricted to the current user query and the judge-maintained canonical memory. Let StaS\_{t}^{a} and UtaU\_{t}^{a} denote the number of supported and unsupported claims at turn tt, respectively. We compute a turn-level hallucination rate as

|  |  |  |
| --- | --- | --- |
|  | Hta=Utamax⁡(1,Sta+Uta).H\_{t}^{a}=\frac{U\_{t}^{a}}{\max(1,S\_{t}^{a}+U\_{t}^{a})}. |  |

Lower values of HtaH\_{t}^{a} indicate better grounding. We report the average hallucination rate across turns as

|  |  |  |
| --- | --- | --- |
|  | Hua=1T​∑t=1THta,H\_{u}^{a}=\frac{1}{T}\sum\_{t=1}^{T}H\_{t}^{a}, |  |

and plot HtaH\_{t}^{a} over time to identify hallucination bursts, which commonly occur following misleading or adversarial turns.

##### Drift audit.

Drift is measured as deviation from previously established constraints and required outputs. At each turn, the judge reads the current query and the prior canonical memory, extracts the active requirements and constraints, and checks whether ytay\_{t}^{a} violates them or omits required elements. Let VtaV\_{t}^{a} denote the number of constraint violations and OtaO\_{t}^{a} the number of omitted required elements at turn tt, and let 𝒦t\mathcal{K}\_{t} denote the set of active constraints at that turn. We compute a normalized drift rate as

|  |  |  |
| --- | --- | --- |
|  | Dta=Vta+Otamax⁡(1,|𝒦t|).D\_{t}^{a}=\frac{V\_{t}^{a}+O\_{t}^{a}}{\max(1,|\mathcal{K}\_{t}|)}. |  |

Lower values of DtaD\_{t}^{a} indicate stronger multi-turn consistency. Drift is undefined at the first turn due to the absence of a prior state, so we exclude t=1t=1 and report the average drift rate as

|  |  |  |
| --- | --- | --- |
|  | Dra=1T−1​∑t=2TDta.D\_{r}^{a}=\frac{1}{T-1}\sum\_{t=2}^{T}D\_{t}^{a}. |  |

##### Memory footprint.

Because ACC is a memory control mechanism, we also log memory growth. We report the per turn token size of baseline transcript memory, retrieval context, and ACC state. Let MtaM\_{t}^{a} denote the measured memory size at turn tt for agent aa. We plot MtaM\_{t}^{a} across turns and report summary statistics such as M¯a\bar{M}^{a} and MTaM\_{T}^{a}. This links memory consumption to hallucination and drift behavior in multi-turn scenarios.

### 5.4 Evaluation data and scenarios

The evaluation data consists of judge-generated questions grounded in curated scenarios. We launched 600 live evaluations for a total of 30,000 turns across all data. Each live evaluation runs for 50 turns to evaluate extended multi-turn behavior, including token consumption, goal sustaining, constraint retention, and robustness under noisy and adversarial updates. We evaluate across three domains: IT operations, cybersecurity response, and healthcare workflows

Scenario design mixes standard task progression with stress turns that probe common multi-turn failure modes. Table [1](#S5.T1 "Table 1 ‣ 5.4 Evaluation data and scenarios ‣ 5 Agent Judge Driven Multi-Turn Evaluation ‣ AI Agents Need Memory Control Over More Context") summarizes the stress topics embedded throughout the 50-turn live testing. The table serves as a dataset taxonomy that clarifies which reliability risks are covered and how the same testing surface is applied consistently across domains.

| Topic in the data | Purpose in evaluation |
| --- | --- |
| Constraints and environment setup | Establish baseline requirements and operational limits early |
| Evidence updates and recalibration | Force hypothesis updates without rewriting prior facts |
| Strict instruction following | Enforce templates, length limits, and structured outputs |
| Conflicting requirements and drift traps | Test resistance to goal deviation and constraint violations |
| Bias pressure from stakeholders | Test factual tone and avoidance of motivated conclusions |
| Poisoned runbook snippets | Test safe critique and refusal of unsafe shortcuts |
| Prompt injection attempts | Test refusal to override prior constraints or policies |
| Uncertainty handling | Test separation of confirmed facts versus hypotheses |
| Operational risk tradeoffs | Test conservative decision making under pressure |
| Executive and incident communication | Test concise, accurate summaries without invented details |

Table 1: Dataset taxonomy of stress topics embedded in the judge-generated evaluation data. Each topic is instantiated with domain-specific content across IT operations, cybersecurity, healthcare, and finance.

### 5.5 Evaluation results and analysis

We report results at two complementary levels. First, we aggregate response-driven outcome metrics across domains to quantify overall task performance under multi-turn stress (Fig. [6](#S5.F6 "Figure 6 ‣ 5.5.4 Drift rate and constraint retention ‣ 5.5 Evaluation results and analysis ‣ 5 Agent Judge Driven Multi-Turn Evaluation ‣ AI Agents Need Memory Control Over More Context")). Second, we report memory reliability and memory footprint behavior over 50-turn episodes, including turn-level hallucination and drift audits (Fig. [7](#S5.F7 "Figure 7 ‣ 5.5.4 Drift rate and constraint retention ‣ 5.5 Evaluation results and analysis ‣ 5 Agent Judge Driven Multi-Turn Evaluation ‣ AI Agents Need Memory Control Over More Context")) and token growth across domains (Fig. [5](#S5.F5 "Figure 5 ‣ 5.5.4 Drift rate and constraint retention ‣ 5.5 Evaluation results and analysis ‣ 5 Agent Judge Driven Multi-Turn Evaluation ‣ AI Agents Need Memory Control Over More Context")). Together, these views capture both *what* the agent produces (task outcome) and *how reliably* it sustains state over long horizons (hallucination, drift, and memory growth).

#### 5.5.1 Memory footprint across domains

Figure [5](#S5.F5 "Figure 5 ‣ 5.5.4 Drift rate and constraint retention ‣ 5.5 Evaluation results and analysis ‣ 5 Agent Judge Driven Multi-Turn Evaluation ‣ AI Agents Need Memory Control Over More Context") shows a clear separation between memory mechanisms across domains. The baseline agent exhibits near-linear growth in context size over turns, increasing the amount of history that competes for attention. In contrast, both the retrieval agent and the ACC agent remain bounded across turns. For retrieval, we explicitly restrict recall to the top 5 artifacts per turn to limit drift escalation observed with larger retrieval sets. The ACC agent remains bounded by design because it carries a compact Compressed Cognitive State rather than replaying a growing transcript.

#### 5.5.2 Response-driven outcome metrics

Figure [6](#S5.F6 "Figure 6 ‣ 5.5.4 Drift rate and constraint retention ‣ 5.5 Evaluation results and analysis ‣ 5 Agent Judge Driven Multi-Turn Evaluation ‣ AI Agents Need Memory Control Over More Context") summarizes outcome quality metrics produced by the three-way judge. Across domains, the ACC agent achieves the strongest relevance and coherence, while remaining competitive on answer quality and instruction following. This pattern is consistent with ACC providing a stable, decision-oriented conditioning signal as horizon length increases.

#### 5.5.3 Hallucination rate over turns (claim audit)

Figure [7](#S5.F7 "Figure 7 ‣ 5.5.4 Drift rate and constraint retention ‣ 5.5 Evaluation results and analysis ‣ 5 Agent Judge Driven Multi-Turn Evaluation ‣ AI Agents Need Memory Control Over More Context") (left column) reports the turn-level hallucination rate HtaH\_{t}^{a} computed by the judge claim audit grounded in canonical memory. Across the shown domains, hallucination increases with turn count for the baseline and retrieval agents, with recurrent spikes after stress turns. The ACC agent remains near zero across most turns with only small transient spikes, indicating that unsupported claims are less likely to enter and persist in the committed cognitive state used for conditioning.

#### 5.5.4 Drift rate and constraint retention

Figure [7](#S5.F7 "Figure 7 ‣ 5.5.4 Drift rate and constraint retention ‣ 5.5 Evaluation results and analysis ‣ 5 Agent Judge Driven Multi-Turn Evaluation ‣ AI Agents Need Memory Control Over More Context") (right column) reports the turn-level drift rate DtaD\_{t}^{a}, which measures violations or omissions relative to active constraints in the judge canonical memory. Drift stays low early for all agents, then rises for baseline under conflicting requirements and strict formatting phases, and remains non-trivial for retrieval due to selection error (stale or competing artifacts). The ACC agent stays near zero with rare small spikes, demonstrating stronger constraint retention and more stable goal sustaining over the full 50-turn horizon

![Refer to caption](2601.11653v1/mem_tokens_all_domains.png)


(a) Per-turn memory tokens across domains.

![Refer to caption](2601.11653v1/avg_mem_tokens_by_domain_agent.png)


(b) Average memory consumption by domain and agent.

Figure 5: Memory footprint across domains over 50-turn live testing. Baseline grows with turn count, while Retrieval (top-3 artifacts) and ACC remain bounded.

![Refer to caption](2601.11653v1/averagemetricsacrosdomains2.png)


Figure 6: Outcome quality metrics (three-way judge, mean ±\pm std across turns) aggregated across domains for Relevance, Answer Quality, Instruction Following, and Coherence.



![Refer to caption](2601.11653v1/it_ops_hallucination_rate.png)


(a) IT operations: hallucination rate HtaH\_{t}^{a}.

![Refer to caption](2601.11653v1/it_ops_drift_rate.png)


(b) IT operations: drift rate DtaD\_{t}^{a}.

![Refer to caption](2601.11653v1/healthcare_hallucination_rate.png)


(c) Healthcare: hallucination rate HtaH\_{t}^{a}.

![Refer to caption](2601.11653v1/healthcare_drift_rate.png)


(d) Healthcare: drift rate DtaD\_{t}^{a}.

![Refer to caption](2601.11653v1/cybersecurity_hallucination_rate.png)


(e) Cybersecurity: hallucination rate HtaH\_{t}^{a}.

![Refer to caption](2601.11653v1/cybersecurity_drift_rate.png)


(f) Cybersecurity: drift rate DtaD\_{t}^{a}.

Figure 7: Turn-level memory reliability audits across domains over 50 turns. Left: hallucination rate HtaH\_{t}^{a} from the judge claim audit grounded in canonical memory. Right: drift rate DtaD\_{t}^{a} measuring constraint violations and missing requirements.

#### 5.5.5 Why ACC outperforms

Across the reported metrics, the results support a consistent explanation grounded in memory control. Transcript replay increases context length, so validated facts and constraints lose salience over time, enabling drift and hallucination carryover through repeated re-exposure. Retrieval bounds the amount of injected context but introduces selection error: when retrieval returns weakly related, stale, or injected artifacts, the agent conditions on the wrong information and errors propagate over turns. ACC addresses both mechanisms directly by (i) bounding the persistent conditioning signal by construction and (ii) separating artifact recall from state commitment, so recalled content only influences the next state through schema-governed compression. The combined effect is the observed cross-domain pattern: bounded memory growth together with higher outcome quality and substantially lower hallucination and drift rates.

## 6 Conclusion

This paper showed that multi-turn agent failures are often driven less by missing knowledge than by weak memory control. Transcript replay causes context to grow with turn count, reduces attention selectivity, and allows early errors to persist and reappear, which increases hallucination carryover and drift from established constraints. Retrieval-based memory bounds prompt length, but adds selection error: stale, conflicting, or injected artifacts can perturb the current task state and destabilize long-horizon behavior, which in our setting required restricting retrieval to three artifacts per turn to limit drift escalation.

We introduced the Agent Cognitive Compressor (ACC), a memory control mechanism that replaces accumulation with a bounded, schema-governed internal state. ACC separates artifact recall from state commitment and updates a single persistent variable, the Compressed Cognitive State (CCS), via controlled replacement rather than growth. This makes the write path explicit and auditable while keeping memory footprint bounded.

We also proposed an agent-judge-driven live evaluation framework that scores response quality and audits memory-driven anomalies at the turn level. Using a judge-maintained canonical memory, the framework computes grounded hallucination and drift rates alongside response-driven outcome metrics and direct measurements of memory footprint. Across domains including IT operations, cybersecurity response, healthcare operations, and finance workflows, ACC consistently maintained bounded memory and exhibited more stable multi-turn behavior with lower hallucination and drift than transcript replay and retrieval-based agents. The representative IT operations results highlight the core effect: ACC preserves constraint salience as horizons extend, while baseline and retrieval agents degrade under growing context or retrieval noise.

These findings support memory governance as a first-class requirement for reliable multi-turn agents. Future work will strengthen validation with targeted human audits, explore learned or task-adaptive CCS schemas, and study specialized compressor models and multi-agent extensions where state synchronization and shared constraints become central.

## References

* [1]
  A. Asai, Z. Wu, Y. Wang, A. Sil, and H. Hajishirzi (2023)
  Self-rag: learning to retrieve, generate, and critique through self-reflection.
  arXiv preprint arXiv:2310.11511.
  External Links: [Document](https://dx.doi.org/10.48550/arXiv.2310.11511)
  Cited by: [§2.2](#S2.SS2.p2.1 "2.2 Memory and state as a limiting factor in multi-turn agents ‣ 2 Background and Related Work ‣ AI Agents Need Memory Control Over More Context").
* [2]
  A. D. Baddeley and G. Hitch (1974)
  Working memory.
  In Psychology of Learning and Motivation, G. H. Bower (Ed.),
  Vol. 8,  pp. 47–89.
  External Links: [Document](https://dx.doi.org/10.1016/S0079-7421%2808%2960452-1)
  Cited by: [§1](#S1.p4.1 "1 Introduction ‣ AI Agents Need Memory Control Over More Context"),
  [§2.3](#S2.SS3.p1.1 "2.3 Cognitive compression as a principle for memory control ‣ 2 Background and Related Work ‣ AI Agents Need Memory Control Over More Context").
* [3]
  A. D. Baddeley (2000)
  The episodic buffer: a new component of working memory?.
  Trends in Cognitive Sciences 4 (11),  pp. 417–423.
  External Links: [Document](https://dx.doi.org/10.1016/S1364-6613%2800%2901538-2)
  Cited by: [§2.3](#S2.SS3.p1.1 "2.3 Cognitive compression as a principle for memory control ‣ 2 Background and Related Work ‣ AI Agents Need Memory Control Over More Context").
* [4]
  A. Baddeley (2012)
  Working memory: theories, models, and controversies.
  Annual Review of Psychology 63,  pp. 1–29.
  Cited by: [§3.2](#S3.SS2.p2.1 "3.2 Compressed Cognitive State (CCS) ‣ 3 Agent Cognitive Compressor (ACC) ‣ AI Agents Need Memory Control Over More Context").
* [5]
  Y. Bai et al. (2022)
  Training a helpful and harmless assistant with rlhf.
  arXiv preprint arXiv:2204.05862.
  Cited by: [§2.1](#S2.SS1.p2.1 "2.1 AI agents: definitions and execution patterns ‣ 2 Background and Related Work ‣ AI Agents Need Memory Control Over More Context").
* [6]
  F. Bousetouane (2025)
  Agentic systems: a guide to transforming industries with vertical ai agents.
  arXiv preprint arXiv:2501.00881.
  Cited by: [§2.1](#S2.SS1.p1.1 "2.1 AI agents: definitions and execution patterns ‣ 2 Background and Related Work ‣ AI Agents Need Memory Control Over More Context"),
  [§2.1](#S2.SS1.p2.1 "2.1 AI agents: definitions and execution patterns ‣ 2 Background and Related Work ‣ AI Agents Need Memory Control Over More Context").
* [7]
  F. Bousetouane (2025)
  Physical ai agents: integrating cognitive intelligence with real-world action.
  arXiv preprint arXiv:2501.08944.
  Cited by: [§2.1](#S2.SS1.p1.1 "2.1 AI agents: definitions and execution patterns ‣ 2 Background and Related Work ‣ AI Agents Need Memory Control Over More Context").
* [8]
  F. Bousetouane (2026)
  AI agents for everyone: a practical guide to building and understanding ai agents without complexity.
   Independently published.
  Note: Self-published via Amazon Kindle Direct Publishing (KDP)
  Cited by: [§2.1](#S2.SS1.p1.1 "2.1 AI agents: definitions and execution patterns ‣ 2 Background and Related Work ‣ AI Agents Need Memory Control Over More Context").
* [9]
  Z. Chen et al. (2024)
  Vertical ai agents for enterprise decision support.
  arXiv preprint arXiv:2401.10247.
  Cited by: [§2.1](#S2.SS1.p2.1 "2.1 AI agents: definitions and execution patterns ‣ 2 Background and Related Work ‣ AI Agents Need Memory Control Over More Context").
* [10]
  N. Cowan (2001)
  The magical number 4 in short-term memory: a reconsideration of mental storage capacity.
  Behavioral and Brain Sciences 24 (1),  pp. 87–114.
  Cited by: [§3.2](#S3.SS2.p2.1 "3.2 Compressed Cognitive State (CCS) ‣ 3 Agent Cognitive Compressor (ACC) ‣ AI Agents Need Memory Control Over More Context").
* [11]
  N. Cowan (2001)
  The magical number 4 in short-term memory: a reconsideration of mental storage capacity.
  Behavioral and Brain Sciences 24 (1),  pp. 87–185.
  External Links: [Document](https://dx.doi.org/10.1017/S0140525X01003922)
  Cited by: [§1](#S1.p4.1 "1 Introduction ‣ AI Agents Need Memory Control Over More Context"),
  [§2.3](#S2.SS3.p1.1 "2.3 Cognitive compression as a principle for memory control ‣ 2 Background and Related Work ‣ AI Agents Need Memory Control Over More Context").
* [12]
  Y. Dubois, B. Galambosi, P. Liang, and T. B. Hashimoto (2024)
  Length-controlled alpacaeval: a simple way to debias automatic evaluators.
  arXiv preprint arXiv:2404.04475.
  External Links: [Link](https://arxiv.org/abs/2404.04475)
  Cited by: [§1](#S1.p6.1 "1 Introduction ‣ AI Agents Need Memory Control Over More Context").
* [13]
  K. Friston (2010)
  The free-energy principle.
  Nature Reviews Neuroscience.
  Cited by: [§2.3](#S2.SS3.p1.1 "2.3 Cognitive compression as a principle for memory control ‣ 2 Background and Related Work ‣ AI Agents Need Memory Control Over More Context").
* [14]
  J. Gu, X. Jiang, Z. Shi, H. Tan, X. Zhai, C. Xu, W. Li, Y. Shen, S. Ma, H. Liu, Y. Wang, W. Gao, L. Ni, and J. Guo (2024)
  A survey on LLM-as-a-judge.
  arXiv preprint arXiv:2411.15594.
  Cited by: [§5.2](#S5.SS2.p2.3 "5.2 Response-driven outcome evaluation ‣ 5 Agent Judge Driven Multi-Turn Evaluation ‣ AI Agents Need Memory Control Over More Context").
* [15]
  S. Guan et al. (2025)
  Evaluating llm-based agents for multi-turn conversations: a survey.
  arXiv preprint arXiv:2503.22458.
  Cited by: [§5](#S5.p1.1 "5 Agent Judge Driven Multi-Turn Evaluation ‣ AI Agents Need Memory Control Over More Context").
* [16]
  L. Guerdan, S. Barocas, K. Holstein, H. Wallach, Z. S. Wu, and A. Chouldechova (2025)
  Validating LLM-as-a-judge systems in the absence of gold labels.
  arXiv preprint arXiv:2503.05965.
  Cited by: [§5.2](#S5.SS2.p2.3 "5.2 Response-driven outcome evaluation ‣ 5 Agent Judge Driven Multi-Turn Evaluation ‣ AI Agents Need Memory Control Over More Context").
* [17]
  D. Kahneman (2011)
  Thinking, fast and slow.
   Farrar, Straus and Giroux, New York.
  Cited by: [§3.2](#S3.SS2.p2.1 "3.2 Compressed Cognitive State (CCS) ‣ 3 Agent Cognitive Compressor (ACC) ‣ AI Agents Need Memory Control Over More Context").
* [18]
  V. Karpukhin, B. Oguz, S. Min, P. Lewis, L. Wu, S. Edunov, D. Chen, and W. Yih (2020)
  Dense passage retrieval for open-domain question answering.
  In Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP),
   pp. 6769–6781.
  External Links: [Link](https://aclanthology.org/2020.emnlp-main.550/),
  [Document](https://dx.doi.org/10.18653/v1/2020.emnlp-main.550)
  Cited by: [§1](#S1.p3.1 "1 Introduction ‣ AI Agents Need Memory Control Over More Context"),
  [§2.2](#S2.SS2.p2.1 "2.2 Memory and state as a limiting factor in multi-turn agents ‣ 2 Background and Related Work ‣ AI Agents Need Memory Control Over More Context").
* [19]
  P. Lewis, E. Perez, A. Piktus, F. Petroni, V. Karpukhin, N. Goyal, H. Küttler, M. Lewis, W. Yih, T. Rocktäschel, S. Riedel, and D. Kiela (2020)
  Retrieval-augmented generation for knowledge-intensive NLP tasks.
  arXiv preprint arXiv:2005.11401.
  External Links: [Link](https://arxiv.org/abs/2005.11401)
  Cited by: [§1](#S1.p3.1 "1 Introduction ‣ AI Agents Need Memory Control Over More Context"),
  [§2.2](#S2.SS2.p2.1 "2.2 Memory and state as a limiting factor in multi-turn agents ‣ 2 Background and Related Work ‣ AI Agents Need Memory Control Over More Context").
* [20]
  G. Li et al. (2023)
  CAMEL: communicative agents for mind exploration.
  arXiv preprint arXiv:2303.17760.
  Cited by: [§2.1](#S2.SS1.p2.1 "2.1 AI agents: definitions and execution patterns ‣ 2 Background and Related Work ‣ AI Agents Need Memory Control Over More Context").
* [21]
  N. Liu et al. (2024)
  Lost in the middle: how language models use long contexts.
  Transactions of the ACL.
  Cited by: [§2.2](#S2.SS2.p1.1 "2.2 Memory and state as a limiting factor in multi-turn agents ‣ 2 Background and Related Work ‣ AI Agents Need Memory Control Over More Context").
* [22]
  X. Liu, H. Yu, H. Zhang, Y. Xu, X. Lei, H. Lai, Y. Gu, H. Ding, K. Men, K. Yang, S. Zhang, X. Deng, A. Zeng, Z. Du, C. Zhang, S. Shen, T. Zhang, Y. Su, H. Sun, M. Huang, Y. Dong, and J. Tang (2023)
  AgentBench: evaluating llms as agents.
  arXiv preprint arXiv:2308.03688.
  External Links: [Document](https://dx.doi.org/10.48550/arXiv.2308.03688)
  Cited by: [§5](#S5.p1.1 "5 Agent Judge Driven Multi-Turn Evaluation ‣ AI Agents Need Memory Control Over More Context").
* [23]
  Y. Liu, D. Iter, Y. Xu, S. Wang, R. Xu, and C. Zhu (2023)
  G-eval: nlg evaluation using gpt-4 with better human alignment.
  arXiv preprint arXiv:2303.16634.
  External Links: [Document](https://dx.doi.org/10.48550/arXiv.2303.16634)
  Cited by: [§5](#S5.p1.1 "5 Agent Judge Driven Multi-Turn Evaluation ‣ AI Agents Need Memory Control Over More Context").
* [24]
  Z. Liu et al. (2023)
  Plan-and-solve prompting.
  arXiv preprint arXiv:2305.04091.
  Cited by: [§2.1](#S2.SS1.p1.1 "2.1 AI agents: definitions and execution patterns ‣ 2 Background and Related Work ‣ AI Agents Need Memory Control Over More Context").
* [25]
  J. L. McClelland, B. L. McNaughton, and R. C. O’Reilly (1995)
  Why there are complementary learning systems in the hippocampus and neocortex: insights from the successes and failures of connectionist models of learning and memory.
  Psychological Review 102 (3),  pp. 419–457.
  External Links: [Document](https://dx.doi.org/10.1037/0033-295X.102.3.419)
  Cited by: [§2.3](#S2.SS3.p1.1 "2.3 Cognitive compression as a principle for memory control ‣ 2 Background and Related Work ‣ AI Agents Need Memory Control Over More Context").
* [26]
  G. A. Miller (1956)
  The magical number seven, plus or minus two: some limits on our capacity for processing information.
  Psychological Review 63 (2),  pp. 81–97.
  Cited by: [§3.2](#S3.SS2.p2.1 "3.2 Compressed Cognitive State (CCS) ‣ 3 Agent Cognitive Compressor (ACC) ‣ AI Agents Need Memory Control Over More Context").
* [27]
  D. G. Nagy, B. Török, and G. Orbán (2020)
  Optimal forgetting: semantic compression of episodic memories.
  PLOS Computational Biology 16 (10),  pp. e1008367.
  External Links: [Document](https://dx.doi.org/10.1371/journal.pcbi.1008367)
  Cited by: [§2.3](#S2.SS3.p1.1 "2.3 Cognitive compression as a principle for memory control ‣ 2 Background and Related Work ‣ AI Agents Need Memory Control Over More Context").
* [28]
  D. A. Norman (1976)
  Memory and attention: an introduction to human information processing.
   John Wiley & Sons, New York.
  Cited by: [§3.2](#S3.SS2.p2.1 "3.2 Compressed Cognitive State (CCS) ‣ 3 Agent Cognitive Compressor (ACC) ‣ AI Agents Need Memory Control Over More Context").
* [29]
  C. Packer, V. Fang, S. G. Patil, K. Lin, S. Wooders, and J. E. Gonzalez (2023)
  MemGPT: towards LLMs as operating systems.
  arXiv preprint arXiv:2310.08560.
  External Links: [Link](https://arxiv.org/abs/2310.08560)
  Cited by: [§1](#S1.p3.1 "1 Introduction ‣ AI Agents Need Memory Control Over More Context"),
  [§2.2](#S2.SS2.p2.1 "2.2 Memory and state as a limiting factor in multi-turn agents ‣ 2 Background and Related Work ‣ AI Agents Need Memory Control Over More Context").
* [30]
  J. S. Park et al. (2023)
  Generative agents: interactive simulacra of human behavior.
  arXiv preprint arXiv:2304.03442.
  Cited by: [§2.1](#S2.SS1.p1.1 "2.1 AI agents: definitions and execution patterns ‣ 2 Background and Related Work ‣ AI Agents Need Memory Control Over More Context").
* [31]
  O. Press and N. Smith (2023)
  Train short, test long: attention with linear biases.
  ICLR.
  Cited by: [§2.2](#S2.SS2.p1.1 "2.2 Memory and state as a limiting factor in multi-turn agents ‣ 2 Background and Related Work ‣ AI Agents Need Memory Control Over More Context").
* [32]
  R. P. N. Rao and D. H. Ballard (1999)
  Predictive coding in the visual cortex: a functional interpretation of some extra-classical receptive-field effects.
  Nature Neuroscience 2 (1),  pp. 79–87.
  External Links: [Document](https://dx.doi.org/10.1038/4580)
  Cited by: [§2.3](#S2.SS3.p1.1 "2.3 Cognitive compression as a principle for memory control ‣ 2 Background and Related Work ‣ AI Agents Need Memory Control Over More Context").
* [33]
  T. Schick et al. (2024)
  Toolformer: language models can teach themselves to use tools.
  NeurIPS.
  Cited by: [§2.1](#S2.SS1.p1.1 "2.1 AI agents: definitions and execution patterns ‣ 2 Background and Related Work ‣ AI Agents Need Memory Control Over More Context").
* [34]
  N. Shinn, F. Cassano, E. Berman, A. Gopinath, K. Narasimhan, and S. Yao (2023)
  Reflexion: language agents with verbal reinforcement learning.
  arXiv preprint arXiv:2303.11366.
  External Links: [Link](https://arxiv.org/abs/2303.11366)
  Cited by: [§1](#S1.p3.1 "1 Introduction ‣ AI Agents Need Memory Control Over More Context"),
  [§2.2](#S2.SS2.p2.1 "2.2 Memory and state as a limiting factor in multi-turn agents ‣ 2 Background and Related Work ‣ AI Agents Need Memory Control Over More Context").
* [35]
  E. Tulving (1972)
  Episodic and semantic memory.
  In Organization of Memory, E. Tulving and W. Donaldson (Eds.),
   pp. 381–403.
  Cited by: [§1](#S1.p4.1 "1 Introduction ‣ AI Agents Need Memory Control Over More Context").
* [36]
  Q. Wu et al. (2023)
  AutoGen: enabling next-gen llm applications via multi-agent conversation.
  arXiv preprint arXiv:2308.08155.
  External Links: [Document](https://dx.doi.org/10.48550/arXiv.2308.08155)
  Cited by: [§2.1](#S2.SS1.p2.1 "2.1 AI agents: definitions and execution patterns ‣ 2 Background and Related Work ‣ AI Agents Need Memory Control Over More Context").
* [37]
  Y. Wu et al. (2024)
  AgentGraph: structured agent execution with graph control.
  arXiv preprint arXiv:2402.01680.
  Cited by: [§2.1](#S2.SS1.p1.1 "2.1 AI agents: definitions and execution patterns ‣ 2 Background and Related Work ‣ AI Agents Need Memory Control Over More Context").
* [38]
  S. Yao, J. Zhao, D. Yu, N. Du, I. Shafran, K. Narasimhan, and Y. Cao (2022)
  ReAct: synergizing reasoning and acting in language models.
  arXiv preprint arXiv:2210.03629.
  External Links: [Link](https://arxiv.org/abs/2210.03629)
  Cited by: [§1](#S1.p1.1 "1 Introduction ‣ AI Agents Need Memory Control Over More Context"),
  [§2.1](#S2.SS1.p2.1 "2.1 AI agents: definitions and execution patterns ‣ 2 Background and Related Work ‣ AI Agents Need Memory Control Over More Context").
* [39]
  A. Yehudai et al. (2025)
  Survey on evaluation of LLM-based agents.
  arXiv preprint arXiv:2503.16416.
  Cited by: [§5](#S5.p1.1 "5 Agent Judge Driven Multi-Turn Evaluation ‣ AI Agents Need Memory Control Over More Context").
* [40]
  L. Zheng, W. Chiang, Y. Sheng, S. Zhuang, Z. Wu, Y. Zhuang, Z. Lin, Z. Li, D. Li, E. P. Xing, H. Zhang, J. E. Gonzalez, and I. Stoica (2023)
  Judging llm-as-a-judge with mt-bench and chatbot arena.
  arXiv preprint arXiv:2306.05685.
  External Links: [Document](https://dx.doi.org/10.48550/arXiv.2306.05685)
  Cited by: [§5.2](#S5.SS2.p2.3 "5.2 Response-driven outcome evaluation ‣ 5 Agent Judge Driven Multi-Turn Evaluation ‣ AI Agents Need Memory Control Over More Context"),
  [§5](#S5.p1.1 "5 Agent Judge Driven Multi-Turn Evaluation ‣ AI Agents Need Memory Control Over More Context").
* [41]
  L. Zheng, W. Chiang, Y. Sheng, S. Zhuang, Z. Wu, Y. Zhuang, Z. Lin, Z. Li, et al. (2023)
  Judging LLM-as-a-judge with MT-bench and chatbot arena.
  arXiv preprint arXiv:2306.05685.
  External Links: [Link](https://arxiv.org/abs/2306.05685)
  Cited by: [§1](#S1.p6.1 "1 Introduction ‣ AI Agents Need Memory Control Over More Context").

Experimental support, please
[view the build logs](./2601.11653v1/__stdout.txt)
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