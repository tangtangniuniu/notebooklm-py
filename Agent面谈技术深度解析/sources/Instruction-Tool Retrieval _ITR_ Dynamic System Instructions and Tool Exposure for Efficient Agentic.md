> Source: https://arxiv.org/html/2602.17046v1

Instruction-Tool Retrieval (ITR) Dynamic System Instructions and Tool Exposure for Efficient Agentic LLMs





1. [1 Introduction](https://arxiv.org/html/2602.17046v1#S1 "In Instruction-Tool Retrieval (ITR) Dynamic System Instructions and Tool Exposure for Efficient Agentic LLMs")
2. [2 Related Work](https://arxiv.org/html/2602.17046v1#S2 "In Instruction-Tool Retrieval (ITR) Dynamic System Instructions and Tool Exposure for Efficient Agentic LLMs")
   1. [2.1 Retrieval-Augmented Generation](https://arxiv.org/html/2602.17046v1#S2.SS1 "In 2 Related Work ‣ Instruction-Tool Retrieval (ITR) Dynamic System Instructions and Tool Exposure for Efficient Agentic LLMs")
   2. [2.2 Tool Learning and Function Calling](https://arxiv.org/html/2602.17046v1#S2.SS2 "In 2 Related Work ‣ Instruction-Tool Retrieval (ITR) Dynamic System Instructions and Tool Exposure for Efficient Agentic LLMs")
   3. [2.3 Prompt Engineering and Compression](https://arxiv.org/html/2602.17046v1#S2.SS3 "In 2 Related Work ‣ Instruction-Tool Retrieval (ITR) Dynamic System Instructions and Tool Exposure for Efficient Agentic LLMs")
   4. [2.4 Autonomous Agents and Cost Optimization](https://arxiv.org/html/2602.17046v1#S2.SS4 "In 2 Related Work ‣ Instruction-Tool Retrieval (ITR) Dynamic System Instructions and Tool Exposure for Efficient Agentic LLMs")
   5. [2.5 Position of Our Work](https://arxiv.org/html/2602.17046v1#S2.SS5 "In 2 Related Work ‣ Instruction-Tool Retrieval (ITR) Dynamic System Instructions and Tool Exposure for Efficient Agentic LLMs")
3. [3 Method](https://arxiv.org/html/2602.17046v1#S3 "In Instruction-Tool Retrieval (ITR) Dynamic System Instructions and Tool Exposure for Efficient Agentic LLMs")
   1. [3.1 Problem Setup and Notation](https://arxiv.org/html/2602.17046v1#S3.SS1 "In 3 Method ‣ Instruction-Tool Retrieval (ITR) Dynamic System Instructions and Tool Exposure for Efficient Agentic LLMs")
   2. [3.2 Corpora and Indexing](https://arxiv.org/html/2602.17046v1#S3.SS2 "In 3 Method ‣ Instruction-Tool Retrieval (ITR) Dynamic System Instructions and Tool Exposure for Efficient Agentic LLMs")
   3. [3.3 Retrieval and Scoring](https://arxiv.org/html/2602.17046v1#S3.SS3 "In 3 Method ‣ Instruction-Tool Retrieval (ITR) Dynamic System Instructions and Tool Exposure for Efficient Agentic LLMs")
   4. [3.4 Budget-Aware Selection](https://arxiv.org/html/2602.17046v1#S3.SS4 "In 3 Method ‣ Instruction-Tool Retrieval (ITR) Dynamic System Instructions and Tool Exposure for Efficient Agentic LLMs")
   5. [3.5 System Architecture](https://arxiv.org/html/2602.17046v1#S3.SS5 "In 3 Method ‣ Instruction-Tool Retrieval (ITR) Dynamic System Instructions and Tool Exposure for Efficient Agentic LLMs")
   6. [3.6 Assembly and Safety Overlay](https://arxiv.org/html/2602.17046v1#S3.SS6 "In 3 Method ‣ Instruction-Tool Retrieval (ITR) Dynamic System Instructions and Tool Exposure for Efficient Agentic LLMs")
   7. [3.7 Fallbacks and Confidence Gating](https://arxiv.org/html/2602.17046v1#S3.SS7 "In 3 Method ‣ Instruction-Tool Retrieval (ITR) Dynamic System Instructions and Tool Exposure for Efficient Agentic LLMs")
   8. [3.8 Caching](https://arxiv.org/html/2602.17046v1#S3.SS8 "In 3 Method ‣ Instruction-Tool Retrieval (ITR) Dynamic System Instructions and Tool Exposure for Efficient Agentic LLMs")
   9. [3.9 Why ITR Improves Tool Routing](https://arxiv.org/html/2602.17046v1#S3.SS9 "In 3 Method ‣ Instruction-Tool Retrieval (ITR) Dynamic System Instructions and Tool Exposure for Efficient Agentic LLMs")
4. [4 Experiment Protocol](https://arxiv.org/html/2602.17046v1#S4 "In Instruction-Tool Retrieval (ITR) Dynamic System Instructions and Tool Exposure for Efficient Agentic LLMs")
   1. [4.1 Tasks](https://arxiv.org/html/2602.17046v1#S4.SS1 "In 4 Experiment Protocol ‣ Instruction-Tool Retrieval (ITR) Dynamic System Instructions and Tool Exposure for Efficient Agentic LLMs")
   2. [4.2 Baselines](https://arxiv.org/html/2602.17046v1#S4.SS2 "In 4 Experiment Protocol ‣ Instruction-Tool Retrieval (ITR) Dynamic System Instructions and Tool Exposure for Efficient Agentic LLMs")
   3. [4.3 Metrics](https://arxiv.org/html/2602.17046v1#S4.SS3 "In 4 Experiment Protocol ‣ Instruction-Tool Retrieval (ITR) Dynamic System Instructions and Tool Exposure for Efficient Agentic LLMs")
5. [5 Results](https://arxiv.org/html/2602.17046v1#S5 "In Instruction-Tool Retrieval (ITR) Dynamic System Instructions and Tool Exposure for Efficient Agentic LLMs")
   1. [5.1 Multi-Loop Agent Scenarios](https://arxiv.org/html/2602.17046v1#S5.SS1 "In 5 Results ‣ Instruction-Tool Retrieval (ITR) Dynamic System Instructions and Tool Exposure for Efficient Agentic LLMs")
   2. [5.2 Context Window Implications](https://arxiv.org/html/2602.17046v1#S5.SS2 "In 5 Results ‣ Instruction-Tool Retrieval (ITR) Dynamic System Instructions and Tool Exposure for Efficient Agentic LLMs")
   3. [5.3 Internal Consistency Validation](https://arxiv.org/html/2602.17046v1#S5.SS3 "In 5 Results ‣ Instruction-Tool Retrieval (ITR) Dynamic System Instructions and Tool Exposure for Efficient Agentic LLMs")
   4. [5.4 Per-Step Context and Tool Accuracy (All Tasks)](https://arxiv.org/html/2602.17046v1#S5.SS4 "In 5 Results ‣ Instruction-Tool Retrieval (ITR) Dynamic System Instructions and Tool Exposure for Efficient Agentic LLMs")
   5. [5.5 Episode Outcomes (T2, L≈9L\approx 9)](https://arxiv.org/html/2602.17046v1#S5.SS5 "In 5 Results ‣ Instruction-Tool Retrieval (ITR) Dynamic System Instructions and Tool Exposure for Efficient Agentic LLMs")
   6. [5.6 Compounding Across Steps](https://arxiv.org/html/2602.17046v1#S5.SS6 "In 5 Results ‣ Instruction-Tool Retrieval (ITR) Dynamic System Instructions and Tool Exposure for Efficient Agentic LLMs")
   7. [5.7 Miss-Rate and Fallbacks](https://arxiv.org/html/2602.17046v1#S5.SS7 "In 5 Results ‣ Instruction-Tool Retrieval (ITR) Dynamic System Instructions and Tool Exposure for Efficient Agentic LLMs")
   8. [5.8 Ablations](https://arxiv.org/html/2602.17046v1#S5.SS8 "In 5 Results ‣ Instruction-Tool Retrieval (ITR) Dynamic System Instructions and Tool Exposure for Efficient Agentic LLMs")
   9. [5.9 Sensitivity to Catalog Size](https://arxiv.org/html/2602.17046v1#S5.SS9 "In 5 Results ‣ Instruction-Tool Retrieval (ITR) Dynamic System Instructions and Tool Exposure for Efficient Agentic LLMs")
6. [6 Cost Model and Theory Sketch](https://arxiv.org/html/2602.17046v1#S6 "In Instruction-Tool Retrieval (ITR) Dynamic System Instructions and Tool Exposure for Efficient Agentic LLMs")
7. [7 Discussion](https://arxiv.org/html/2602.17046v1#S7 "In Instruction-Tool Retrieval (ITR) Dynamic System Instructions and Tool Exposure for Efficient Agentic LLMs")
8. [8 Limitations and Threats to Validity](https://arxiv.org/html/2602.17046v1#S8 "In Instruction-Tool Retrieval (ITR) Dynamic System Instructions and Tool Exposure for Efficient Agentic LLMs")
9. [9 Conclusion](https://arxiv.org/html/2602.17046v1#S9 "In Instruction-Tool Retrieval (ITR) Dynamic System Instructions and Tool Exposure for Efficient Agentic LLMs")
10. [10 Method](https://arxiv.org/html/2602.17046v1#S10 "In Instruction-Tool Retrieval (ITR) Dynamic System Instructions and Tool Exposure for Efficient Agentic LLMs")
11. [11 Ablation Summary](https://arxiv.org/html/2602.17046v1#S11 "In Instruction-Tool Retrieval (ITR) Dynamic System Instructions and Tool Exposure for Efficient Agentic LLMs")
12. [12 Deployment Notes](https://arxiv.org/html/2602.17046v1#S12 "In Instruction-Tool Retrieval (ITR) Dynamic System Instructions and Tool Exposure for Efficient Agentic LLMs")

# Instruction-Tool Retrieval (ITR) Dynamic System Instructions and Tool Exposure for Efficient Agentic LLMs

Uria Franko
  
uriafranko@gmail.com

###### Abstract

Large Language Model (LLM) agents often run for many steps while re-ingesting long system instructions and large tool catalogs each turn. This increases cost, agent derailment probability, latency, and tool-selection errors.

We propose Instruction-Tool Retrieval (ITR), a RAG variant that retrieves, per step, only the minimal system-prompt fragments and the smallest necessary subset of tools. ITR composes a dynamic runtime system prompt and exposes a narrowed toolset with confidence-gated fallbacks.

Using a controlled benchmark with internally consistent numbers, ITR reduces per-step context tokens by 95%, improves correct tool routing by 32% relative, and cuts end-to-end episode cost by 70% versus a monolithic baseline. These savings enable agents to run 2-20x more loops within context limits. Savings compound with the number of agent steps, making ITR particularly valuable for long-running autonomous agents.

We detail the method, evaluation protocol, ablations, and operational guidance for practical deployment.

## 1 Introduction

Large Language Model (LLM) agents [yao2023react, nakano2021webgpt, zhou2023agents] have emerged as powerful paradigms for solving complex, multi-step tasks through iterative reasoning and tool interaction. These agents frequently operate in loops, maintaining conversation history while interacting with external systems [wang2023survey, xi2024review]. However, modern agents quickly exhaust context windows, with system instructions and tools consuming 90% of available tokens. At each step they typically receive the prior full context, a static multi-page system prompt containing all possible instructions, and a broad catalog of tool/function schemas [qin2023toolllm, patil2023gorilla]. This monolithic design inflates context windows, slows inference, increases operational costs, and paradoxically leads to spurious tool calls due to the overwhelming number of available options [chen2024token, zhou2024economics].

The challenge is particularly acute in production environments where agents may run for dozens or hundreds of steps. Consider a coding assistant that must handle file operations, web searches, code execution, and version control [yang2024sweagent, jimenez2024swebench]. Loading all possible tools and their detailed documentation at every step wastes computational resources and increases the likelihood of the model selecting incorrect tools due to attention dilution [liu2024lost, li2024long]. Furthermore, static system instructions often contain contradictory or irrelevant instructions for specific contexts, leading to behavioral inconsistencies [wang2024solo, meng2024artist].

To address these fundamental inefficiencies, we introduce Instruction-Tool Retrieval (ITR): a novel approach that treats both instructions and tools as retrievable resources. Instead of retrieving domain knowledge as in traditional RAG systems [lewis2020retrieval, gao2023retrieval], ITR retrieves the instructions and tools themselves. Our method indexes system-prompt fragments (role descriptions, style guides, safety policies) and tool specifications, retrieves only what a specific step requires based on the current context, and dynamically assembles a minimal per-step prompt while exposing a narrowed, relevant toolset.

This dynamic composition yields multiple benefits. First, it dramatically reduces token usage-our experiments show up to 95% reduction in per-step context tokens. Second, it improves tool routing accuracy by 32% by reducing the search space and eliminating irrelevant options. Third, it enables faster responses through shorter context processing. Most importantly, because agents operate in loops, these benefits compound multiplicatively across steps, resulting in 70% total cost reduction for complete agent episodes. This approach directly addresses the scalability challenges noted in recent work [meng2024artist, guo2024towards] and builds upon advances in dynamic prompting [wang2024solo, jiang2023llmlingua].

Our system also incorporates safety mechanisms through confidence-gated fallbacks and always-on security overlays, ensuring that critical instructions (like content policies) remain accessible even under aggressive retrieval pruning. This allows ITR to optimize for efficiency without compromising on safety or capability coverage in edge cases [zhang2024dylan, sun2024scalemcp].

Contributions.

1. 1.

   A formulation of retrieval-based prompt and tool selection that treats instructions and tools as first-class retrievable objects rather than static context.
2. 2.

   A budget-aware selector with confidence-gated fallbacks and an always-on safety overlay that balances efficiency with robustness.
3. 3.

   A comprehensive benchmark protocol and metrics for multi-step agent episodes that captures both efficiency and accuracy dimensions.
4. 4.

   Extensive experimental results showing large efficiency and accuracy gains, plus detailed ablations and operational guidance for practical deployment.
5. 5.

   An open-source Python implementation of the ITR framework, available at <https://github.com/uriafranko/ITR>, enabling practitioners to integrate dynamic instruction and tool retrieval into their agent systems.

## 2 Related Work

Our work intersects several active research areas in large language models and autonomous agents. We organize the related work into four key themes that inform our approach.

### 2.1 Retrieval-Augmented Generation

Retrieval-Augmented Generation (RAG) has become a cornerstone technique for grounding language model outputs in external knowledge [lewis2020retrieval]. Early work focused on retrieving relevant passages from large corpora to improve factual accuracy in knowledge-intensive tasks [izacard2021leveraging]. Recent surveys [gao2023retrieval] highlight the evolution toward more sophisticated retrieval strategies, including dense retrieval, hybrid approaches combining sparse and dense methods, and multi-hop reasoning over retrieved content.

However, traditional RAG systems retrieve factual knowledge to answer queries, whereas our approach retrieves instructions and tools to configure agent behavior. This represents a fundamental shift from knowledge augmentation to behavioral configuration through retrieval.

### 2.2 Tool Learning and Function Calling

The integration of external tools with language models has emerged as a critical capability for autonomous agents. Toolformer [schick2023toolformer] demonstrated that language models can learn to use APIs through self-supervised learning. Subsequent work has scaled this approach to thousands of real-world APIs [qin2023toolllm] and developed specialized frameworks for tool routing [patil2023gorilla].

Recent advances include dynamic tool discovery and composition [sun2024scalemcp], multi-step tool planning, and error recovery mechanisms. However, these systems typically expose all available tools to the model at each step, leading to decision paralysis and increased computational overhead. Our work addresses this limitation by dynamically selecting relevant tools based on context.

### 2.3 Prompt Engineering and Compression

The challenge of managing increasingly long prompts has spawned research into prompt compression and optimization. Early work explored prompt compression for controllability [wingate2022prompt], while recent advances include learned compression with gist tokens [mu2023learning] and automated prompt optimization techniques [jiang2023llmlingua].

Dynamic prompting approaches [wang2024solo] have shown promise in adapting prompt content based on task requirements. Token-budget-aware reasoning [chen2024token] and context-aware prompt trimming [jiang2024trim] address the computational costs of long contexts. Our work extends these ideas by treating prompt fragments as retrievable units that can be dynamically composed.

### 2.4 Autonomous Agents and Cost Optimization

Large language model agents have demonstrated remarkable capabilities across diverse domains, from code generation [yang2024sweagent, jimenez2024swebench] to complex reasoning tasks [yao2023react]. Comprehensive surveys [wang2023survey, xi2024review] highlight the rapid progress in agent architectures, planning algorithms, and evaluation methodologies.

However, the operational costs of deploying agents at scale remain prohibitive [guo2024towards, zhou2024economics]. Recent work has explored various cost optimization strategies, including selective computation [chen2024token], model compression, and efficient inference techniques. Multi-agent collaboration frameworks [zhang2024dylan, hong2023metagpt] offer another approach by distributing computational load across specialized agents.

Our work contributes to this cost optimization effort by reducing the per-step computational overhead through selective instruction and tool exposure, with benefits that compound across multi-step agent episodes.

### 2.5 Position of Our Work

ITR represents a novel synthesis of these research directions. Unlike traditional RAG that retrieves external knowledge, we retrieve internal system components-instructions and tools-to dynamically configure agent behavior. This approach addresses the scalability challenges of modern agent architectures while maintaining the flexibility and capability coverage required for complex autonomous tasks.

## 3 Method

### 3.1 Problem Setup and Notation

At step tt in an agent episode, let qtq\_{t} be the model’s current input (task state + user query). Let 𝒜={ai}\mathcal{A}=\{a\_{i}\} be instruction fragments (policies, role guidance, style rules, safety notes, in-context exemplars) with token costs sis\_{i}. Let ℬ={bj}\mathcal{B}=\{b\_{j}\} be tools with schemas and exemplars with token costs tjt\_{j}. Exposing all of 𝒜\mathcal{A} and ℬ\mathcal{B} yields per-step token cost

|  |  |  |  |
| --- | --- | --- | --- |
|  | Tokmono=user/history⏟Ut+∑isi+∑jtj.\operatorname{Tok}\_{\operatorname{mono}}=\underbrace{\text{user/history}}\_{U\_{t}}+\sum\_{i}s\_{i}+\sum\_{j}t\_{j}. |  | (1) |

ITR chooses small subsets 𝒜t∗⊂𝒜\mathcal{A}^{\*}\_{t}\subset\mathcal{A}, ℬt∗⊂ℬ\mathcal{B}^{\*}\_{t}\subset\mathcal{B}, assembling

|  |  |  |  |
| --- | --- | --- | --- |
|  | TokITR=Ut+∑ai∈𝒜t∗si+∑bj∈ℬt∗tj,\operatorname{Tok}\_{\operatorname{ITR}}=U\_{t}+\sum\_{a\_{i}\in\mathcal{A}^{\*}\_{t}}s\_{i}+\sum\_{b\_{j}\in\mathcal{B}^{\*}\_{t}}t\_{j}, |  | (2) |

subject to a step-budget BB. We target high task success and correct tool use given limited TokITR\operatorname{Tok}\_{\operatorname{ITR}}.

### 3.2 Corpora and Indexing

1. 1.

   Instruction corpus 𝒜\mathcal{A}: Chunk system prompt into 200 →\to 600-token units with stable IDs and metadata (domain, policy type, recency).
2. 2.

   Tool corpus ℬ\mathcal{B}: One document per tool containing name, arguments, pre/postconditions, failure modes, and few-shot exemplars (150 →\to 800 tokens).
3. 3.

   Retrievers: Dual encoders for dense similarity, plus BM25. Store vectors and sparse indices. Use a lightweight cross-encoder re-ranker.

### 3.3 Retrieval and Scoring

Given qtq\_{t}, compute dense embeddings E​(qt)E(q\_{t}), E​(ai)E(a\_{i}), E​(bj)E(b\_{j}). Hybrid scores:

|  |  |  |  |
| --- | --- | --- | --- |
|  | S​(ai|qt)=w1⋅cos⁡(E​(qt),E​(ai))+w2⋅BM25​(qt,ai)+w3⋅CE​(qt,ai),S(a\_{i}|q\_{t})=w\_{1}\cdot\cos(E(q\_{t}),E(a\_{i}))+w\_{2}\cdot\text{BM25}(q\_{t},a\_{i})+w\_{3}\cdot\text{CE}(q\_{t},a\_{i}), |  | (3) |

and similarly for bjb\_{j}. Keep top MA,MBM\_{A},M\_{B} and re-rank.

### 3.4 Budget-Aware Selection

We choose KAK\_{A} instruction chunks and KBK\_{B} tools to maximize a proxy for success given a token budget BB. Let Δ​(ai)\Delta(a\_{i}) and Δ​(bj)\Delta(b\_{j}) estimate marginal gain (from historical traces or bandit feedback). Solve a knapsack-like objective:

|  |  |  |  |
| --- | --- | --- | --- |
|  | max𝒜∗,ℬ∗​∑ai∈𝒜∗Δ​(ai)+∑bj∈ℬ∗Δ​(bj)s.t.∑si+∑tj≤B.\max\_{\mathcal{A}^{\*},\mathcal{B}^{\*}}\sum\_{a\_{i}\in\mathcal{A}^{\*}}\Delta(a\_{i})+\sum\_{b\_{j}\in\mathcal{B}^{\*}}\Delta(b\_{j})\quad\text{s.t.}\quad\sum s\_{i}+\sum t\_{j}\leq B. |  | (4) |

In practice, a greedy selection by re-ranker score per token works well.

### 3.5 System Architecture

Figure [1](https://arxiv.org/html/2602.17046v1#S3.F1 "Figure 1 ‣ 3.5 System Architecture ‣ 3 Method ‣ Instruction-Tool Retrieval (ITR) Dynamic System Instructions and Tool Exposure for Efficient Agentic LLMs") illustrates the ITR pipeline:

Query qtq\_{t} +HistoryInstructionRetrievalToolRetrievalRe-rank𝒜∗\mathcal{A}^{\*}Re-rankℬ∗\mathcal{B}^{\*}Budget-AwareSelectionPrompt Assembly +Safety OverlayLLM withExposed ToolsDiscoveryFallback


Figure 1: ITR system architecture showing dual retrieval, budget-aware selection, and confidence-gated fallback mechanisms.

### 3.6 Assembly and Safety Overlay

Assemble a step-local system prompt:

1. 1.

   Safety/Legal overlay (always on, small).
2. 2.

   Selected instructions ordered by policy priority.
3. 3.

   Selected tools with schemas and 1 →\to 2 exemplars each.
4. 4.

   Routing note: ask the model to avoid hidden tools; if insufficient, request “tool discovery”.

### 3.7 Fallbacks and Confidence Gating

1. 1.

   Tool sufficiency check: The model self-rates whether exposed tools suffice. If below τ\tau, run a “discovery” sub-step that expands KBK\_{B} or briefly exposes the catalog summary.
2. 2.

   Recall-first retrieval: Prefer slightly higher recall for tools; precision is handled by the model and cross-encoder.
3. 3.

   Pinned tools: Rare but critical tools can be conditionally “always-eligible” via domain classifiers.

### 3.8 Caching

Cache top-KK instruction/tool sets per task signature to amortize retrieval over loops and repeated episodes.

### 3.9 Why ITR Improves Tool Routing

Let there be NN total tools with one gold-valid tool gg. Suppose the chance of a wrong tool call grows roughly with the number of irrelevant tools. A simple hazard model gives

|  |  |  |  |
| --- | --- | --- | --- |
|  | Pr[correct∣N]≈αα+β​(N−1),\operatorname\*{Pr}[\text{correct}\mid N]\approx\frac{\alpha}{\alpha+\beta(N-1)}, |  | (5) |

with α\alpha capturing clarity of schema/exemplars and β\beta the interference of distractors. ITR reduces candidates to m≪Nm\ll N with recall rr. Then

|  |  |  |  |
| --- | --- | --- | --- |
|  | Pr[correct under ITR]≈r⋅αα+β​(m−1).\operatorname\*{Pr}[\text{correct under ITR}]\approx r\cdot\frac{\alpha}{\alpha+\beta(m-1)}. |  | (6) |

As mm drops, accuracy rises unless recall rr is too low; hence the value of recall-first retrieval with a discovery fallback.

## 4 Experiment Protocol

### 4.1 Tasks

1. 1.

   T1 Structured-API: 40 tasks across CRM, support, analytics, billing; 1 →\to 3 tools per task.
2. 2.

   T2 Reason+Act: 30 multi-hop data analysis tasks, 5 →\to 1 →\to 2 steps per episode.
3. 3.

   T3 DevOps/Docs: 30 tasks requiring selective doc reading and 2 →\to 5 tools.

Each task has validators for end-state success and gold-valid tool sequences.

### 4.2 Baselines

1. 1.

   B0 Monolithic: Full system prompt + all tools exposed.
2. 2.

   B1 Router-Only: Learned tool router; full prompt retained.
3. 3.

   B2 Prompt-RAG: Retrieve instruction fragments; still expose all tools.
4. 4.

   ITR: Retrieve both instructions and tools with fallbacks.

### 4.3 Metrics

1. 1.

   Ctx/step: Prompt tokens per step.
2. 2.

   Tools-correct: % of steps where the tool call matches any gold-valid tool.
3. 3.

   API-success: % of episodes passing validators.
4. 4.

   Cost: Tokenized input + output ×\times model rates.
5. 5.

   Latency: p50 and p95 wall time per episode.
6. 6.

   Miss-rate: Episodes failing because the correct tool was hidden.
7. 7.

   Compounding: Total tokens vs. number of steps LL.

## 5 Results

### 5.1 Multi-Loop Agent Scenarios

Practical agent deployments often involve multiple iterations or loops, where context accumulation becomes a critical bottleneck. We evaluated ITR’s performance across extended agent loops to understand its scalability characteristics. While our controlled experiments use a representative baseline, production systems with extensive tool catalogs and comprehensive system instructions exhibit even more pronounced benefits. In one production deployment with enterprise-grade safety policies and operational guidelines, the baseline system consumed approximately 30,000 tokens per step, which ITR reduced to 1,500 tokens-a 95% reduction consistent with our experimental findings.

Figure [2](https://arxiv.org/html/2602.17046v1#S5.F2 "Figure 2 ‣ 5.1 Multi-Loop Agent Scenarios ‣ 5 Results ‣ Instruction-Tool Retrieval (ITR) Dynamic System Instructions and Tool Exposure for Efficient Agentic LLMs") presents a comprehensive analysis of 10 agent loops, demonstrating:

* •

  Constant savings: 28,500 tokens saved at each step regardless of loop count
* •

  Loop 1: 95.0% savings (30,000 → 1,500 tokens)
* •

  Loop 5: 73.1% savings (39,000 → 10,500 tokens)
* •

  Loop 10: 57.0% savings (50,000 → 21,500 tokens)
* •

  Token distribution: System + Tools remain constant while User + Output + History accumulate

![Refer to caption](results/agent_loops_comprehensive.png)


Figure 2: Comprehensive analysis of token accumulation over 10 agent loops. Top: Cumulative token usage showing constant 28,500 token savings per step. Bottom left: Token distribution breakdown at loops 1, 5, and 10. Bottom center: Available context window over loops. Bottom right: Percentage token savings per loop, decreasing from 95% to 57% as history accumulates.

### 5.2 Context Window Implications

Modern LLMs offer increasingly large context windows: GPT-4.1 supports 1M tokens, Claude Sonnet 4.5 provides 200K tokens (up to 1M via cloud providers), Gemini 2.5 Pro offers 1–2M tokens, and GPT-5 delivers approximately 400K tokens. One might assume these expanded windows obviate the need for ITR. However, the opposite is true larger windows make ITR more valuable, not less.

Consider high-scale production deployments with extreme settings: |𝒜|=300|\mathcal{A}|=300 instruction fragments (∼\sim120K tokens) and |ℬ|=200|\mathcal{B}|=200 tools (∼\sim100K tokens). Even with million-token windows, the monolithic approach faces critical challenges:

1. 1.

   Exponential loop constraints. With 220K tokens of static context, an agent can execute at most ⌊(1​M−220​K)/h⌋\lfloor(1\text{M}-220\text{K})/h\rfloor steps before exhausting the window, where hh is per-step history growth. ITR’s 1.5K static footprint permits 147×\times more agent loops within the same window.
2. 2.

   Cost scales with window usage. API pricing is proportional to tokens processed. A 10-step episode with monolithic context costs (220​K×10)=2.2​M(220\text{K}\times 10)=2.2\text{M} input tokens; ITR reduces this to (1.5​K×10)=15​K(1.5\text{K}\times 10)=15\text{K}—a 147×\times cost reduction that compounds with each additional step.
3. 3.

   Attention degradation. Even within supported windows, model performance degrades on long contexts. Studies show retrieval accuracy drops 10–30% when relevant information is buried in 100K+ token contexts. ITR keeps relevant instructions at prompt boundaries where attention is strongest.
4. 4.

   Latency compounds. Time-to-first-token scales with context length. At 200K+ tokens, latency penalties of 2–5 seconds per step accumulate to minutes over multi-step episodes.

Table [1](https://arxiv.org/html/2602.17046v1#S5.T1 "Table 1 ‣ 5.2 Context Window Implications ‣ 5 Results ‣ Instruction-Tool Retrieval (ITR) Dynamic System Instructions and Tool Exposure for Efficient Agentic LLMs") illustrates how ITR’s advantage grows with instruction/tool corpus size—the margin is not linear but exponential in terms of viable agent loop depth.

Table 1: Maximum viable agent loops within a 1M token context window, assuming 2K tokens per-step history growth. ITR enables exponentially more loops as corpus size increases.

| Corpus Size | Static Tokens | Mono Max Loops | ITR Max Loops |
| --- | --- | --- | --- |
| 50 instr + 30 tools | 40K | 480 | 499 |
| 150 instr + 100 tools | 110K | 445 | 499 |
| 300 instr + 200 tools | 220K | 390 | 499 |
| 500 instr + 400 tools | 400K | 300 | 499 |
| 800 instr + 600 tools | 620K | 190 | 499 |

Key insight: As organizations scale their agent capabilities with more instructions and tools, monolithic approaches hit hard ceilings while ITR maintains near-constant overhead. At enterprise scale (500+ instructions, 400+ tools), ITR is not an optimization—it is the only architecture that permits meaningful agent autonomy.

The comprehensive analysis in Figure [2](https://arxiv.org/html/2602.17046v1#S5.F2 "Figure 2 ‣ 5.1 Multi-Loop Agent Scenarios ‣ 5 Results ‣ Instruction-Tool Retrieval (ITR) Dynamic System Instructions and Tool Exposure for Efficient Agentic LLMs") and extended 20-loop evaluation in Figure [4](https://arxiv.org/html/2602.17046v1#S5.F4 "Figure 4 ‣ 5.6 Compounding Across Steps ‣ 5 Results ‣ Instruction-Tool Retrieval (ITR) Dynamic System Instructions and Tool Exposure for Efficient Agentic LLMs") demonstrate how ITR maintains constant absolute token savings regardless of the number of agent loops. While percentage savings decrease as context accumulates (from 95% to 57% over 10 loops), the constant 28,500 token reduction per step is critical for enabling long-running agent systems to operate within context constraints.

### 5.3 Internal Consistency Validation

1. 1.

   Token reduction validation: 1.5​k/30​k=5%1.5\text{k}/30\text{k}=5\% usage, yielding 95%95\% reduction
2. 2.

   Tool accuracy improvement: (82%−62%)/62%=32.3%(82\%-62\%)/62\%=32.3\% relative improvement ≈32%\approx 32\%
3. 3.

   Cost reduction: $​0.86/$​2.90=29.7%\mathdollar 0.86/\mathdollar 2.90=29.7\% usage, yielding 70.3%70.3\% reduction ≈70%\approx 70\%
4. 4.

   Compounding validation: At L=10L=10: ITR cumulative =105​k=105\text{k} vs B0 cumulative =390​k=390\text{k}, savings =285​k=285\text{k} (3.7×\times reduction)
5. 5.

   Catalog scaling: Tool accuracy decreases with catalog size for B0 (74%→\to45%) while ITR maintains performance (84%→\to76%), consistent with interference model

### 5.4 Per-Step Context and Tool Accuracy (All Tasks)

Table 2: Per-step token usage and tool selection accuracy across all tasks. ITR achieves 95% token reduction and 32% relative improvement in tool selection compared to monolithic baseline.

| Method | Tokens/Step | Tools-Correct (%) |
| --- | --- | --- |
| B0 Monolithic | 30,000 | 62 |
| B1 Router-Only | 30,000 | 70 |
| B2 Prompt-RAG | 11,000 | 66 |
| ITR (KA=4,KB=2K\_{A}=4,K\_{B}=2) | 1,500 | 82 |

Key Finding: ITR cuts tokens/step by 95% versus B0 and improves tool accuracy by 32% relative.

### 5.5 Episode Outcomes (T2, L≈9L\approx 9)

Table 3: End-to-end episode metrics for multi-hop reasoning tasks (T2, L≈9L\approx 9 steps). ITR delivers 70% cost reduction and 35% latency improvement while achieving highest success rate.

| Method | API-Success (%) | Cost/Episode ($) | p50 Latency (s) |
| --- | --- | --- | --- |
| B0 Monolithic | 64 | 2.90 | 68 |
| B1 Router-Only | 70 | 2.55 | 65 |
| B2 Prompt-RAG | 72 | 1.45 | 51 |
| ITR | 79 | 0.86 | 44 |

Performance Drivers: Fewer tokens and fewer misfires reduce retries and rewinds.

### 5.6 Compounding Across Steps

As agent episodes grow longer, ITR’s savings compound dramatically. Let LL be steps/episode, outputs excluded for clarity:

1. 1.

   B0: System (30k) + accumulated history per step ⇒\Rightarrow at L=10L=10: 390k cumulative tokens.
2. 2.

   ITR: System (1.5k) + accumulated history per step ⇒\Rightarrow at L=10L=10: 105k cumulative tokens.

Figures [2](https://arxiv.org/html/2602.17046v1#S5.F2 "Figure 2 ‣ 5.1 Multi-Loop Agent Scenarios ‣ 5 Results ‣ Instruction-Tool Retrieval (ITR) Dynamic System Instructions and Tool Exposure for Efficient Agentic LLMs") and [4](https://arxiv.org/html/2602.17046v1#S5.F4 "Figure 4 ‣ 5.6 Compounding Across Steps ‣ 5 Results ‣ Instruction-Tool Retrieval (ITR) Dynamic System Instructions and Tool Exposure for Efficient Agentic LLMs") demonstrate how this advantage scales across multiple agent loops, showing a constant 28,500 token per-step reduction that enables agents to run 2-5x more loops within context limits.

Compounding Effect: At L=10L=10, cumulative savings reach 285k tokens (3.7×\times reduction). The savings grow linearly with steps (28.5k ×L\times L), making longer episodes increasingly favorable for ITR adoption.

0224466881010121214140100100200200300300400400500500600600700700285k savingsNumber of Agent Steps (LL)Cumulative Context Tokens (k)B0 MonolithicITR


Figure 3: Context token usage scaling with episode length. ITR maintains constant per-step overhead while monolithic approaches scale linearly, resulting in compound savings for longer agent runs.

0224466881010121214141616181820200101020203030404050506060707028.5k constant savings95%57%39%Agent Loop NumberTokens per Step (k)B0 MonolithicITR


Figure 4: Extended 20-loop evaluation showing constant 28,500 token savings per step. While percentage savings decrease from 95% (loop 1) to 39% (loop 20) as history accumulates, the absolute token reduction remains constant, enabling longer agent runs within context limits.

### 5.7 Miss-Rate and Fallbacks

Table 4: Impact of discovery fallback mechanism on miss-rate. The fallback reduces cases where correct tools are hidden from the agent.

| Variant | KBK\_{B} (Tools Exposed) | Discovery Fallback | Miss-Rate (%) |
| --- | --- | --- | --- |
| ITR naive | 1 | No | 6.1 |
| ITR default | 2 | Yes | 2.4 |

### 5.8 Ablations

1. 1.

   Increasing KAK\_{A} from 1→\to4 adds +6 pp API-Success with modest token increase.
2. 2.

   Increasing KBK\_{B} from 1→\to2 adds +7 pp Tools-Correct and halves miss-rate.
3. 3.

   Hybrid (dense+sparse+re-rank) outperforms dense-only by +3 pp Tools-Correct at fixed budget.

### 5.9 Sensitivity to Catalog Size

As the number of available tools grows, ITR’s advantage increases:

Table 5: Tool routing accuracy vs. catalog size. ITR’s advantage increases with larger tool catalogs, demonstrating resilience to scale. Note: Table 1 shows averaged results across mixed catalog sizes.

|  |  |  |  |
| --- | --- | --- | --- |
| # Tools | B0 Tools-Correct (%) | ITR Tools-Correct (%) | Absolute Gain (pp) |
| 8 | 74 | 84 | +10 |
| 40 | 57 | 82 | +25 |
| 120 | 45 | 76 | +31 |

## 6 Cost Model and Theory Sketch

Per-step tokens

|  |  |  |  |
| --- | --- | --- | --- |
|  | Tokmono=Ut+S+Tall,TokITR=Ut+SKA+TKB,\operatorname{Tok}\_{\operatorname{mono}}=U\_{t}+S+T\_{\text{all}},\quad\operatorname{Tok}\_{\operatorname{ITR}}=U\_{t}+S\_{K\_{A}}+T\_{K\_{B}}, |  | (7) |

with S=∑isiS=\sum\_{i}s\_{i}, Tall=∑jtjT\_{\text{all}}=\sum\_{j}t\_{j}, SKA≪SS\_{K\_{A}}\ll S, TKB≪TallT\_{K\_{B}}\ll T\_{\text{all}}. For LL steps:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Episodemono\displaystyle\text{Episode}\_{\operatorname{mono}} | ≈L​(S+Tall)+∑tUt,\displaystyle\approx L(S+T\_{\text{all}})+\sum\_{t}U\_{t}, |  | (8) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | EpisodeITR\displaystyle\text{Episode}\_{\operatorname{ITR}} | ≈L​(SKA+TKB)+∑tUt.\displaystyle\approx L(S\_{K\_{A}}+T\_{K\_{B}})+\sum\_{t}U\_{t}. |  | (9) |

Savings scale linearly in LL, giving compounding benefits for long-running agents.

## 7 Discussion

When ITR helps.

1. 1.

   Long prompts or many tools.
2. 2.

   Multi-step episodes.
3. 3.

   Domains with clear instruction modularity.

Failure modes.
ITR can fail due to instruction omission on edge cases, hidden-tool errors under low recall, or retriever drift over time.

Mitigations include always-on safety overlay, discovery fallback, hard-negative mining, and pinning rare critical tools. These challenges echo broader concerns about LLM agent reliability [mialon2023gaia] and the need for robust evaluation protocols [karpinska2021perils].

Operational guidance.
Start with KA=4K\_{A}=4, KB=2K\_{B}=2, hybrid retrieval, and a small re-ranker. Cache selections. Track “retrieval sufficiency” and “hidden-tool misses” as first-class metrics. Expose safety + logging tools always.

## 8 Limitations and Threats to Validity

Real outcomes depend on corpus quality, tool schema clarity, and model family [openai2023gpt4, anthropic2024claude]. Benchmarks may not capture adversarial or open-world settings [mialon2023gaia]. Safety overlays must remain visible to avoid policy gaps. Retrieval adds another component that can fail; telemetry and circuit breakers are required.

## 9 Conclusion

Instruction-Tool Retrieval reframes RAG to operate on system instructions and tool catalogs rather than external knowledge. By dynamically selecting relevant instructions and tools per agent step, ITR achieves substantial efficiency gains: 95% reduction in context tokens, 32% improvement in tool accuracy, and 70% cost reduction.

The approach is simple to implement on existing stacks and yields clear operational benefits. Critically, savings compound across agent steps, making ITR particularly valuable for long-running autonomous systems.

Building on recent advances in agent frameworks [hong2023metagpt, li2023camel] and cost optimization [guo2024towards], we recommend ITR as a default design pattern for scalable, economical LLM agents. ITR is essential for deploying cost-effective, long-running agent systems in production environments where context window limitations and operational costs are critical constraints.

## 10 Method

Algorithm 1  ITR Step(qtq\_{t}, history)

0: step query qtq\_{t}, conversation history, indices 𝒜\mathcal{A} (instructions), ℬ\mathcal{B} (tools)

1: e←e\leftarrow Embed(qtq\_{t})

2: 𝒜0←\mathcal{A}\_{0}\leftarrow TopMA by (cos + BM25); ℬ0←\mathcal{B}\_{0}\leftarrow TopMB by (cos + BM25)

3: 𝒜1←\mathcal{A}\_{1}\leftarrow ReRank(𝒜0\mathcal{A}\_{0}, qtq\_{t}); ℬ1←\mathcal{B}\_{1}\leftarrow ReRank(ℬ0\mathcal{B}\_{0}, qtq\_{t})

4: (𝒜∗,ℬ∗\mathcal{A}^{\*},\mathcal{B}^{\*}) ←\leftarrow GreedySelectByScorePerToken(𝒜1\mathcal{A}\_{1}, ℬ1\mathcal{B}\_{1}, budget BB)

5: P←P\leftarrow AssemblePrompt(SAFETY\_OVERLAY ∥\| 𝒜∗\mathcal{A}^{\*} ∥\| ToolSchemas(ℬ∗\mathcal{B}^{\*}))

6: yy, conf ←\leftarrow LLM(PP, qtq\_{t}) with tools ℬ∗\mathcal{B}^{\*} enabled

7: if ToolSufficiency(conf, yy) <τ<\tau then

8:  (𝒜∗,ℬ∗\mathcal{A}^{\*},\mathcal{B}^{\*}) ←\leftarrow ExpandOrDiscover(𝒜1\mathcal{A}\_{1}, ℬ1\mathcal{B}\_{1})

9:  P←P\leftarrow AssemblePrompt(…); y←y\leftarrow LLM(PP, qtq\_{t})

10: end if

11: return yy

## 11 Ablation Summary

Table 6: Component ablation study showing impact on performance. Each factor contributes to overall system effectiveness with manageable token overhead.

| Factor | Setting | Δ\Delta API-Success (pp) | Δ\Delta Tokens/Step |
| --- | --- | --- | --- |
| KAK\_{A} (Instructions) | 1 →\to 4 | +6 | +220 |
| KBK\_{B} (Tools) | 1 →\to 2 | +7 | +180 |
| Re-ranker | Off →\to On | +3 | +60 |
| Retrieval Type | Dense-only →\to Hybrid | +3 | +0 |

## 12 Deployment Notes

1. 1.

   Chunk hygiene: Deduplicate, add stable IDs, maintain change logs.
2. 2.

   Schemas: Include explicit preconditions and negative examples.
3. 3.

   Telemetry: Log selected chunks/tools, sufficiency scores, fallbacks, and errors.
4. 4.

   Caching: Key caches by task signature and domain; expire on content updates.
5. 5.

   Governance: Treat instruction retrieval as policy execution. Require review gates.

Generated on Mon Dec 1 06:41:47 2025 by [LaTeXML![Mascot Sammy](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAsAAAAOCAYAAAD5YeaVAAAAAXNSR0IArs4c6QAAAAZiS0dEAP8A/wD/oL2nkwAAAAlwSFlzAAALEwAACxMBAJqcGAAAAAd0SU1FB9wKExQZLWTEaOUAAAAddEVYdENvbW1lbnQAQ3JlYXRlZCB3aXRoIFRoZSBHSU1Q72QlbgAAAdpJREFUKM9tkL+L2nAARz9fPZNCKFapUn8kyI0e4iRHSR1Kb8ng0lJw6FYHFwv2LwhOpcWxTjeUunYqOmqd6hEoRDhtDWdA8ApRYsSUCDHNt5ul13vz4w0vWCgUnnEc975arX6ORqN3VqtVZbfbTQC4uEHANM3jSqXymFI6yWazP2KxWAXAL9zCUa1Wy2tXVxheKA9YNoR8Pt+aTqe4FVVVvz05O6MBhqUIBGk8Hn8HAOVy+T+XLJfLS4ZhTiRJgqIoVBRFIoric47jPnmeB1mW/9rr9ZpSSn3Lsmir1fJZlqWlUonKsvwWwD8ymc/nXwVBeLjf7xEKhdBut9Hr9WgmkyGEkJwsy5eHG5vN5g0AKIoCAEgkEkin0wQAfN9/cXPdheu6P33fBwB4ngcAcByHJpPJl+fn54mD3Gg0NrquXxeLRQAAwzAYj8cwTZPwPH9/sVg8PXweDAauqqr2cDjEer1GJBLBZDJBs9mE4zjwfZ85lAGg2+06hmGgXq+j3+/DsixYlgVN03a9Xu8jgCNCyIegIAgx13Vfd7vdu+FweG8YRkjXdWy329+dTgeSJD3ieZ7RNO0VAXAPwDEAO5VKndi2fWrb9jWl9Esul6PZbDY9Go1OZ7PZ9z/lyuD3OozU2wAAAABJRU5ErkJggg==)](http://dlmf.nist.gov/LaTeXML/)