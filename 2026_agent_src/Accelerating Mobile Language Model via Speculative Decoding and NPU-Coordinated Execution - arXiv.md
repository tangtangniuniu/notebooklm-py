> Source: https://arxiv.org/html/2510.15312v3

Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution





1. [1 Introduction](https://arxiv.org/html/2510.15312v3#S1 "In Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution")
2. [2 Background](https://arxiv.org/html/2510.15312v3#S2 "In Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution")
   1. [2.1 On-device Context-Augmented Generation for Mobile Task](https://arxiv.org/html/2510.15312v3#S2.SS1 "In 2. Background ‣ Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution")
   2. [2.2 Opportunity: Retrieval-based Speculative Decoding](https://arxiv.org/html/2510.15312v3#S2.SS2 "In 2. Background ‣ Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution")
   3. [2.3 Challenges: Aligning Retrieval-based Speculative Decoding with NPU](https://arxiv.org/html/2510.15312v3#S2.SS3 "In 2. Background ‣ Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution")
3. [3 Methodology](https://arxiv.org/html/2510.15312v3#S3 "In Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution")
   1. [3.1 Overview](https://arxiv.org/html/2510.15312v3#S3.SS1 "In 3. Methodology ‣ Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution")
   2. [3.2 Progressive Graph Scheduling](https://arxiv.org/html/2510.15312v3#S3.SS2 "In 3. Methodology ‣ Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution")
   3. [3.3 In-Context Distribution Calibration](https://arxiv.org/html/2510.15312v3#S3.SS3 "In 3. Methodology ‣ Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution")
   4. [3.4 NPU-Optimized Draft Reuse](https://arxiv.org/html/2510.15312v3#S3.SS4 "In 3. Methodology ‣ Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution")
4. [4 Evaluation](https://arxiv.org/html/2510.15312v3#S4 "In Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution")
   1. [4.1 Implementation and Setup](https://arxiv.org/html/2510.15312v3#S4.SS1 "In 4. Evaluation ‣ Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution")
   2. [4.2 Overall Performance](https://arxiv.org/html/2510.15312v3#S4.SS2 "In 4. Evaluation ‣ Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution")
   3. [4.3 Memory Overhead](https://arxiv.org/html/2510.15312v3#S4.SS3 "In 4. Evaluation ‣ Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution")
   4. [4.4 Latency Breakdown](https://arxiv.org/html/2510.15312v3#S4.SS4 "In 4. Evaluation ‣ Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution")
   5. [4.5 Ablation Study](https://arxiv.org/html/2510.15312v3#S4.SS5 "In 4. Evaluation ‣ Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution")
5. [5 Related Work](https://arxiv.org/html/2510.15312v3#S5 "In Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution")
6. [6 Conclusions](https://arxiv.org/html/2510.15312v3#S6 "In Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution")
7. [A NP-hardness Proof of the Graph Scheduling Problem](https://arxiv.org/html/2510.15312v3#A1 "In Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution")

# Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution

Zhiyang Chen
[0009-0006-8607-8539](https://orcid.org/0009-0006-8607-8539 "ORCID identifier")
Peking UniversityBeijingChina
[zhiyangchen@stu.pku.edu.cn](mailto:zhiyangchen@stu.pku.edu.cn)
, 
Daliang Xu

Beijing University of Posts and TelecommunicationsBeijingChina
[xudaliang@bupt.edu.cn](mailto:xudaliang@bupt.edu.cn)
, 
Haiyang Shen
[0009-0000-4599-3198](https://orcid.org/0009-0000-4599-3198 "ORCID identifier")
Peking UniversityBeijingChina
[hyshen@stu.pku.edu.cn](mailto:hyshen@stu.pku.edu.cn)
, 
Mengwei Xu

Beijing University of Posts and TelecommunicationsBeijingChina
[mwx@bupt.edu.cn](mailto:mwx@bupt.edu.cn)
, 
Shangguang Wang

Beijing University of Posts and TelecommunicationsBeijingChina
[sgwang@bupt.edu.cn](mailto:sgwang@bupt.edu.cn)
 and 
Yun Ma
[0000-0001-7866-4075](https://orcid.org/0000-0001-7866-4075 "ORCID identifier")
Peking UniversityBeijingChina
[mayun@pku.edu.cn](mailto:mayun@pku.edu.cn)

###### Abstract.

Enhancing on-device large language models (LLMs) with contextual information from local data enables personalized and task-aware generation, powering use cases such as intelligent assistants and UI agents. While recent developments in neural processors have substantially improved the efficiency of prefill on mobile devices, the token-by-token generation process still suffers from high latency and limited hardware utilization due to its inherently memory-bound characteristics. This work presents sd.npu, a mobile inference framework that integrates speculative decoding with dynamic hardware scheduling to accelerate context-aware text generation on mobile devices. The framework introduces three synergistic components: (1) adaptive execution scheduling, which dynamically balances compute graphs between prefill and decoding phases; (2) context-aligned drafting, which improves speculative efficiency through lightweight online calibration to current tasks; and (3) hardware-efficient draft extension, which reuses and expands intermediate sequences to improve processing parallelism and reduce verification cost. Experiments on multiple smartphones and representative workloads show consistent improvements of up to 3.8× in generation speed and 4.7× in energy efficiency compared with existing mobile inference solutions. Component-level analysis further validates the contribution of each optimization.

## 1. Introduction

Recent advances in large language models (LLMs) (Brown et al., [2020](https://arxiv.org/html/2510.15312v3#bib.bib7); OpenAI et al., [2024](https://arxiv.org/html/2510.15312v3#bib.bib47); Touvron et al., [2023](https://arxiv.org/html/2510.15312v3#bib.bib64); Guo et al., [2024](https://arxiv.org/html/2510.15312v3#bib.bib21)), rising concerns over privacy, and rapid progress in hardware have fueled interest in on-device LLM. In particular, the integration of neural processing units (NPUs) (Qualcomm, [2024](https://arxiv.org/html/2510.15312v3#bib.bib51), [2025b](https://arxiv.org/html/2510.15312v3#bib.bib53)) makes it feasible to run LLMs directly on mobile devices (Google, [2024](https://arxiv.org/html/2510.15312v3#bib.bib18); Huawei, [2024](https://arxiv.org/html/2510.15312v3#bib.bib26); Samsung, [2024](https://arxiv.org/html/2510.15312v3#bib.bib56); Apple, [2024a](https://arxiv.org/html/2510.15312v3#bib.bib3)), enabling applications such as voice assistants and UI automation (Apple, [2024b](https://arxiv.org/html/2510.15312v3#bib.bib4); AI, [2024](https://arxiv.org/html/2510.15312v3#bib.bib2); Wen et al., [2024](https://arxiv.org/html/2510.15312v3#bib.bib70); Lee et al., [2024](https://arxiv.org/html/2510.15312v3#bib.bib31)).
To extend LLMs’ capabilities in handling complex tasks, context-augmented generation (CAG) has emerged as a key technique (Wang and Chau, [2024](https://arxiv.org/html/2510.15312v3#bib.bib68); Ouyang et al., [2025](https://arxiv.org/html/2510.15312v3#bib.bib49)). As shown in Figure [1](https://arxiv.org/html/2510.15312v3#acmlabel1 "Figure 1 ‣ 1. Introduction ‣ Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution"), CAG augments a user’s query with task-relevant contexts before inference to strengthen the knowledge grounding of LLM.
With CAG, LLMs can, for example, summarize documents using user-uploaded files, generate responses by retrieving and integrating information from the chat history, and act as UI agents by reasoning over current UI screenshots captured from the operating system, significantly expanding their functionality.

Despite these benefits, on-device CAG still has high end-to-end latency, primarily from decoding (accounting for 73.5% of total inference, details in Section [2.1](https://arxiv.org/html/2510.15312v3#S2.SS1 "2.1. On-device Context-Augmented Generation for Mobile Task ‣ 2. Background ‣ Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution")). When diving into the reasons, we find that the prefill bottleneck is largely eliminated by NPU-based chunked prefill (Xu et al., [2025b](https://arxiv.org/html/2510.15312v3#bib.bib76); Chen et al., [2025a](https://arxiv.org/html/2510.15312v3#bib.bib12); Xue et al., [2024](https://arxiv.org/html/2510.15312v3#bib.bib78)) (only 2 s for 1–2K tokens context).
In contrast, the decoding stage remains memory-bound, a scenario poorly suited for NPUs. Therefore, most existing work resorts to CPU execution, leading to high latency. Motivated by the NPU’s superior energy efficiency and lower contention, this paper raises the question whether NPUs can be effectively utilized to accelerate the decoding stage.

![Refer to caption](x1.png)


Figure 1. Workflow of context-augmented generation and comparison between sd.npu and related work
††:

To address this issue, we observe that CAG outputs exhibit strong similarity to both the interaction history and the augmented context (Section [2.2](https://arxiv.org/html/2510.15312v3#S2.SS2 "2.2. Opportunity: Retrieval-based Speculative Decoding ‣ 2. Background ‣ Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution")), making them well-suited for retrieval-based speculative decoding (R-SD), a technique originally developed for code generation, and in turn, to NPU acceleration. In many CAG tasks, generated content is semantically close to previously produced tokens and to the augmented context: for example, summarization and automated email reply often reuse spans from user-uploaded documents or earlier emails, while UI agents repeatedly emit fixed commands (e.g., “click set clock button”). These characteristics align naturally with R-SD, which proceeds in two stages: (1) drafting, where a retriever proposes candidate token sequences by selecting similar fragments from the augmented context or a local store (e.g., a code repository); and (2) verifying, where the LLM compares these drafts against its own next-token predictions and corrects discrepancies (see Section [2.2](https://arxiv.org/html/2510.15312v3#S2.SS2 "2.2. Opportunity: Retrieval-based Speculative Decoding ‣ 2. Background ‣ Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution")). By evaluating multiple drafts in parallel, R-SD shifts decoding from a memory-bound to a compute-bound workload, making it a strong fit for NPU acceleration.

In this paper, we present sd.npu, the first system to enable retrieval-based speculative decoding for efficient on-device CAG through end-to-end on-chip NPU offloading. During prefill, sd.npu employs chunked prefill-based NPU inference like existing approaches (Xu et al., [2025b](https://arxiv.org/html/2510.15312v3#bib.bib76); Chen et al., [2025a](https://arxiv.org/html/2510.15312v3#bib.bib12)); during decoding, it dynamically switches to a compute graph optimized for decoding, performing retrieval-driven drafting and parallel verification. Designing sd.npu requires addressing the following three unique challenges of aligning retrieval-based speculative decoding with NPUs, which prior work has not explored:

∙\bullet NPU execution: costly switching overhead for distinct prefill and decoding optimal compute graphs. 
Prefill favors large-shape graphs with long sequence inputs which degrade decoding performance, while decoding benefits from small-shape graphs that underperform for prefill.
Since the NPU only supports inference on static shapes, achieving optimal end-to-end performance thus requires switching between prefill-optimal and decoding-optimal compute graphs, incurring a significant performance overhead.
For instance, our preliminary evaluation on Qwen2.5-1.5B model shows this switching overhead incurs a 94.9% delay of end-to-end latency.

∙\bullet Draft construction: task context and LLM outputs follow different lexical distributions, yielding a low acceptance ratio.
In R-SD, the LLM only accepts tokens that exactly match its own prediction. Our preliminary evaluation shows that drafts constructed from the task context often have high semantic similarity to the target output yet exhibit notable lexical gaps (e.g., normalized Levenshtein distance >0.11>0.11 for Qwen2.5-1.5B). As a result, LLM often accepts only few tokens per draft, falling back to token-by-token decoding and underscoring the need for lexical distribution calibration.

∙\bullet Draft verification: short or absent drafts fail to saturate NPU computation.
Mobile NPUs excel at processing large batches or long sequences due to their weight-stationary design where short inputs obtain fewer benefits (Jouppi et al., [2017](https://arxiv.org/html/2510.15312v3#bib.bib28); Chen et al., [2025a](https://arxiv.org/html/2510.15312v3#bib.bib12)). However, due to strict suffix-matching, existing R-SD methods often generate only a few candidate tokens or none at all. Such short sequences cannot fully exploit the NPU’s weight-stationary design, resulting in low verification throughput. For example, our experiments show that over 75% of the drafts fall below length 8, which is far below the verification-optimal length (64) and leads to 50% lower throughput.

To address these challenges, we propose three techniques:

∙\bullet Progressive Graph Scheduling (Section [3.2](https://arxiv.org/html/2510.15312v3#S3.SS2 "3.2. Progressive Graph Scheduling ‣ 3. Methodology ‣ Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution")). sd.npu deploys two specialized graphs and switches between them asynchronously to minimize overhead. The LLM is partitioned into blocks. During each round of chunked prefill, we switch to a decoding-optimized block graph while prefill computation continues in parallel. The switched decoding graph is invoked multiple times within the prefill stage to ensure result correctness. This design rests on two observations: (i) executing short-input graphs multiple times is equivalent to a single long-input execution, and (ii) graph loading can be overlapped with one-round chunked prefill computation. Consequently, sd.npu can transition to the decoding graph without additional load overhead, yielding a negligible graph-switching cost.

∙\bullet In-Context Distribution Calibration (Section [3.3](https://arxiv.org/html/2510.15312v3#S3.SS3 "3.3. In-Context Distribution Calibration ‣ 3. Methodology ‣ Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution")). Motivated by the observation that, during prefill, the model computes next-token logits for each context token that already align with its output distribution, sd.npu uses these logits to calibrate the task context by constructing a model-distributed token tree via depth-first search. In the subsequent retrieval-based drafting stage, sd.npu retrieves from this calibrated tree to mitigate lexical divergence between the context and the model’s expectations. Compared with costly precomputation or task-specific fine-tuning, this lightweight procedure incurs negligible overhead.

∙\bullet NPU-Optimized Draft Reuse (Section [3.4](https://arxiv.org/html/2510.15312v3#S3.SS4 "3.4. NPU-Optimized Draft Reuse ‣ 3. Methodology ‣ Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution")). sd.npu extends draft construction by selectively reusing plausible tokens from previously rejected drafts based on a confidence-based strategy. This is motivated by the observation that rejected tokens may still capture correct semantics and be accepted in later decoding steps. By reusing such tokens, sd.npu increases effective draft length with useful content, improving NPU utilization and reducing verification costs.

sd.npu is implemented atop mllm (Xu et al., [2025b](https://arxiv.org/html/2510.15312v3#bib.bib76)), an open-source mobile LLM inference framework with NPU offloading support. We conduct extensive experiments on three devices (Redmi K60 Pro, Redmi K70 Pro and OnePlus 13), four datasets (summarization, RAG-based question answering, UI automation and auto-reply (Xia et al., [2024](https://arxiv.org/html/2510.15312v3#bib.bib73); Xing et al., [2024](https://arxiv.org/html/2510.15312v3#bib.bib74); Salemi et al., [2023](https://arxiv.org/html/2510.15312v3#bib.bib55))), and three LLMs (Qwen2.5-1.5B-Instruct, Qwen2.5-0.5B-Instruct, LLaMA3.2-3B-Instruct (Qwen et al., [2025](https://arxiv.org/html/2510.15312v3#bib.bib54); Grattafiori et al., [2024](https://arxiv.org/html/2510.15312v3#bib.bib19))). Results show that sd.npu achieves 1.06–3.81×\times end-to-end speedup over the vanilla framework and 1.09–2.53×\times over frameworks integrated with existing SD algorithms. In terms of energy efficiency, sd.npu reduces consumption by 1.11–4.18×\times and 1.07–4.71×\times, respectively. Overhead analysis, latency breakdown, and ablation studies further validate the effectiveness of our proposed techniques.

Our contributions are summarized as follows:

∙\bullet We present the first study of inefficiencies in context-aware generation for mobile tasks, identifying key optimization opportunities of using retrieval-based speculative decoding.

∙\bullet We design and implement sd.npu, an efficient NPU-optimized on-device context-augmented generation framework with three novel techniques, bridging the gap between retrieval-based speculative decoding and NPU offloading.

∙\bullet We conduct comprehensive evaluations across four datasets, three smartphones, and three LLMs, demonstrating that sd.npu delivers consistent and significant performance gains in diverse mobile scenarios.

## 2. Background

### 2.1. On-device Context-Augmented Generation for Mobile Task

Context-augmented generation.
With the rapid development of LLMs and increasing demands for privacy protection, there is a growing trend of deploying large models on mobile devices (Belcak et al., [2025](https://arxiv.org/html/2510.15312v3#bib.bib6); Navardi et al., [2025](https://arxiv.org/html/2510.15312v3#bib.bib46); Union, [2021](https://arxiv.org/html/2510.15312v3#bib.bib65); Kshetri, [2023](https://arxiv.org/html/2510.15312v3#bib.bib30); Eleftherakis et al., [2024](https://arxiv.org/html/2510.15312v3#bib.bib15)). An emerging paradigm, *context-augmented generation*, leverages both the long-context capability of LLMs and the abundance of private on-device data, showing strong potential for supporting complex tasks such as personal assistant and UI automation (Wang and Chau, [2024](https://arxiv.org/html/2510.15312v3#bib.bib68); Ouyang et al., [2025](https://arxiv.org/html/2510.15312v3#bib.bib49); Park et al., [2025](https://arxiv.org/html/2510.15312v3#bib.bib50)). Typically, context-augmented generation first exploits additional information, either directly provided by the user or retrieved from relevant sources, to enrich the prompt with task-specific contexts. Then, the normal LLM inference procedure is executed, including prefill and decoding stages. The enriched prompt can alleviate the limitations of the model’s built-in knowledge and enable it to handle a wider range of concrete tasks. For instance, in a summarization task, the user may supply a meeting transcript as context, and the LLM directly generates a concise summary from it. In another case, a personalized assistant retrieves a user’s past chat records to draft a reply in the user’s typical style, where the retrieved records provide the key context for generation.

LLMs on NPUs.
As modern mobile SoCs increasingly integrate high-performance NPUs (Table [1](https://arxiv.org/html/2510.15312v3#S2.T1 "Table 1 ‣ 2.1. On-device Context-Augmented Generation for Mobile Task ‣ 2. Background ‣ Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution")), recent mobile LLM frameworks aim to offload LLM inference onto NPUs to improve efficiency. In practice, NPUs are mainly used for the prefill stage, which benefits from their high throughput on long input sequences, while decoding is still executed on CPUs or GPUs (Xu et al., [2025b](https://arxiv.org/html/2510.15312v3#bib.bib76); Chen et al., [2025a](https://arxiv.org/html/2510.15312v3#bib.bib12); Xue et al., [2024](https://arxiv.org/html/2510.15312v3#bib.bib78)).
Our experiments reveal that mobile CAG still suffers from high latency under this design, with decoding dominating end-to-end performance. For example, for Qwen2.5-1.5B (Qwen et al., [2025](https://arxiv.org/html/2510.15312v3#bib.bib54)) running on a OnePlus 13, decoding accounts for 90.2% of latency in question answering (QA) tasks and 87.2% in summarization, even when prefill runs at over 1000 tokens/s (Xu et al., [2025b](https://arxiv.org/html/2510.15312v3#bib.bib76)) (Figure [2](https://arxiv.org/html/2510.15312v3#S2.F2 "Figure 2 ‣ 2.1. On-device Context-Augmented Generation for Mobile Task ‣ 2. Background ‣ Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution")).
Simply offloading decoding to the NPU provides no advantage over CPU execution and often increases overall latency, as decoding is inherently memory-bound, processing one token at a time and leaving the NPU underutilized.

![Refer to caption](x2.png)


Figure 2. Comparison of prefill and decoding latency for several CAG tasks. Task details are provided in Section [4.1](https://arxiv.org/html/2510.15312v3#S4.SS1 "4.1. Implementation and Setup ‣ 4. Evaluation ‣ Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution").




Table 1. Specifications of representative mobile NPUs.

| Vendor | SoC | NPU | Perf. (Tops) |
| --- | --- | --- | --- |
| Qualcomm | 8 Gen 3 | Hexagon NPU | 73 |
| Apple | A18 | Neural Engine | 35 |
| MediaTek | K9300 | APU 790 | 60 |
| Huawei | Kirin-9000 | Ascend NPU | 16 |

Perf. = INT8 Performance in Tops.

These findings are closely tied to the architectural characteristics of mobile NPUs.
First, their *systolic-array with weight-stationary design* excels at long input sequences: weights are preloaded once and reused across tokens, greatly reducing memory traffic. This property aligns naturally with the prefill stage, which requires lots of computation over long prompts.
Second, NPUs rely on *static compute graphs* with precompiled execution plans, where operator arrangements and tensor shapes are fixed in advance for efficiency. Naively reusing prefill-optimized graphs for decoding leads to severe inefficiencies.
As a result, while NPUs eliminate prefill bottlenecks, they bring little benefit to decoding, which thus remains the dominant source of latency and energy consumption in on-device CAG.

### 2.2. Opportunity: Retrieval-based Speculative Decoding

A key observation is that CAG naturally inherits similarity from the request or the augmented context, making it well-suited for *retrieval-based speculative decoding* (Saxena, [2023](https://arxiv.org/html/2510.15312v3#bib.bib57); He et al., [2024](https://arxiv.org/html/2510.15312v3#bib.bib23); Hu et al., [2024](https://arxiv.org/html/2510.15312v3#bib.bib25); Somasundaram et al., [2024](https://arxiv.org/html/2510.15312v3#bib.bib60)), an acceleration technique exploiting similarity between contexts and outputs.
We find that mobile CAG tasks exhibit the same property, offering strong opportunities for acceleration via R-SD.

∙\bullet History similarity in similar tasks:
outputs from similar tasks resemble previous generations because their contexts are similar. For example, a UI automation agent often repeats commands like clicking the same button. Our evaluation on four UI automation task groups (Wen et al., [2024](https://arxiv.org/html/2510.15312v3#bib.bib70)) with Qwen2.5-1.5B (Qwen et al., [2025](https://arxiv.org/html/2510.15312v3#bib.bib54)) confirms this (Figure [3(a)](https://arxiv.org/html/2510.15312v3#S2.F3.sf1 "In Figure 3 ‣ 2.2. Opportunity: Retrieval-based Speculative Decoding ‣ 2. Background ‣ Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution")): predictions within the same task show the highest semantic similarity (0.72), those within the same group moderate similarity (0.61), and across groups low similarity (0.38). Cosine similarity is computed using embeddings from all-MiniLM-L6-v2 (Wang et al., [2020](https://arxiv.org/html/2510.15312v3#bib.bib67)).

∙\bullet Context similarity at semantic level:
Outputs align with the enriched context, which often includes direct clues for response (Wang and Chau, [2024](https://arxiv.org/html/2510.15312v3#bib.bib68); Ouyang et al., [2025](https://arxiv.org/html/2510.15312v3#bib.bib49); Park et al., [2025](https://arxiv.org/html/2510.15312v3#bib.bib50)). For instance, assistants answering QA queries frequently extract information from documents. On a summarization dataset (Xia et al., [2024](https://arxiv.org/html/2510.15312v3#bib.bib73)) with Qwen2.5-1.5B, we compute semantic similarity between context and predictions (via cosine similarity) and lexical overlap (via Levenshtein distance). Figure [3(b)](https://arxiv.org/html/2510.15312v3#S2.F3.sf2 "In Figure 3 ‣ 2.2. Opportunity: Retrieval-based Speculative Decoding ‣ 2. Background ‣ Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution") shows that 90% of samples exhibit high semantic similarity (>0.76>0.76) but low lexical overlap (>0.11>0.11), reflecting a stylistic gap between context and outputs.

![Refer to caption](x3.png)


(a) History

![Refer to caption](x4.png)


(b) Context

Figure 3. Demonstration of similarities in context-augmented generation.

![Refer to caption](x5.png)


Figure 4. Workflow of retrieval-based speculative decoding.

R-SD exploits these similarities through two stages (Figure [4](https://arxiv.org/html/2510.15312v3#S2.F4 "Figure 4 ‣ 2.2. Opportunity: Retrieval-based Speculative Decoding ‣ 2. Background ‣ Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution")):
(1) retrieval-based drafting, where relevant fragments are retrieved from history or context to draft candidate sequences. For example, tokens “need to” may retrieve drafts such as “click on” and “find the”;
(2) verifying, where the LLM validates these candidates in parallel, accepting matches and discarding mismatches to guarantee correctness (Leviathan et al., [2023a](https://arxiv.org/html/2510.15312v3#bib.bib32)). In the example where model expects “find the”, mismatched drafts like “click on” are discarded while the matched draft is accepted, extending the output to “find the Google”.
The similarities in mobile CAG tasks offer promising draft candidates, enabling R-SD to efficiently generate multiple tokens in parallel. R-SD thus substantially raises the computation-to-memory ratio, shifting decoding from memory-bound to compute-bound where NPU excels.

Parallel to retrieval-based methods, model-based speculative decoding (M-SD) (e.g., EAGLE (Li et al., [2024c](https://arxiv.org/html/2510.15312v3#bib.bib38), [b](https://arxiv.org/html/2510.15312v3#bib.bib37)), Medusa (Cai et al., [2024](https://arxiv.org/html/2510.15312v3#bib.bib8))) trains auxiliary draft models to generate candidates, incurring extra training, storage, and inference overheads. R-SD avoids retraining by directly using contextual information of high similarity, achieving draft latencies under 10ms (Hu et al., [2024](https://arxiv.org/html/2510.15312v3#bib.bib25)). Therefore, R-SD is more suitable for resource-constrained devices while M-SD suffers from higher latency, as shown in our evaluations (Section [4.2](https://arxiv.org/html/2510.15312v3#S4.SS2 "4.2. Overall Performance ‣ 4. Evaluation ‣ Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution")).

### 2.3. Challenges: Aligning Retrieval-based Speculative Decoding with NPU

Although R-SD offers a promising approach to accelerate CAG with NPU offloading, integrating it with NPU offloading poses several challenges.

![Refer to caption](x6.png)


Figure 5. Trade-off between prefill and decoding with fixed-size compute graphs, highlighting the importance to deploy specialized graphs for each stage.

∙\bullet NPU execution: static compute graph design hinders performance improvement for both prefill and decoding.
Static compute graph constraints fixed input and output tensor shapes during execution. To support variable-length sequences in LLM inference, existing systems adopt a chunking strategy, i.e., splitting inputs into fixed-size segments (Xu et al., [2025b](https://arxiv.org/html/2510.15312v3#bib.bib76); Chen et al., [2025a](https://arxiv.org/html/2510.15312v3#bib.bib12)). However, a unified chunk size for both prefill and decoding yields suboptimal performance.
Figure [5](https://arxiv.org/html/2510.15312v3#S2.F5 "Figure 5 ‣ 2.3. Challenges: Aligning Retrieval-based Speculative Decoding with NPU ‣ 2. Background ‣ Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution") compares prefill and speculative decoding speed using different compute graphs on a Redmi K70 Pro smartphone, with a fixed acceptance ratio of 4.2 (based on evaluation results, see Section [4.5](https://arxiv.org/html/2510.15312v3#S4.SS5 "4.5. Ablation Study ‣ 4. Evaluation ‣ Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution")). Results show that compute graphs with larger chunk size improve prefill throughput but hurt decoding performance. For instance, despite a fast prefill speed (¡8 ms/token) of Qwen2.5 1.5B using graph with chunk size 32, the decoding speed using the same graph drops to about 160 ms/token. This tradeoff necessitates specialized compute graphs to improve performance for both prefill and decoding. However, on resource-constrained devices, naively maintaining multiple graphs in memory is costly, highlighting the needs of lightweight graph scheduling algorithms.

![Refer to caption](x7.png)


Figure 6. Comparison of verification speed with different draft lengths, and the length distribution of drafts generated by existing R-SD method (Saxena, [2023](https://arxiv.org/html/2510.15312v3#bib.bib57)) (histogram).

∙\bullet Draft construction: divergence between task context and LLM output reduces the efficiency of speculative decoding.
As discussed in Section [2.1](https://arxiv.org/html/2510.15312v3#S2.SS1 "2.1. On-device Context-Augmented Generation for Mobile Task ‣ 2. Background ‣ Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution"), contexts and predictions often exhibit lexical gaps (i.e., normalized Levenshtein distance >0.11>0.11). These gaps result in frequent rejection of retrieved drafts, despite their success in capturing the similar semantics as LLM. This degrades decoding to a token-by-token process where NPUs offer little speedup due to underutilization.
Lexical gaps arise from divergence between the task context and the LLM’s distribution, necessitating alignment of the two distributions.

∙\bullet Draft verification: existing R-SD methods underutilize NPUs’ weight-stationary design due to drafting short sequences.
The design of mobile NPUs, while ideal for compute-intensive operations such as prefill, is less effective when input sequences become short in the decoding stage. Existing R-SD methods perform retrieval by strict suffix matching between context and output (Somasundaram et al., [2024](https://arxiv.org/html/2510.15312v3#bib.bib60); He et al., [2024](https://arxiv.org/html/2510.15312v3#bib.bib23); Hu et al., [2024](https://arxiv.org/html/2510.15312v3#bib.bib25)), which frequently results in short or empty drafts.
Figure [6](https://arxiv.org/html/2510.15312v3#S2.F6 "Figure 6 ‣ 2.3. Challenges: Aligning Retrieval-based Speculative Decoding with NPU ‣ 2. Background ‣ Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution") demonstrates the influence of draft length on verification speed and the length distribution of generated draft on a summarization dataset (Xia et al., [2024](https://arxiv.org/html/2510.15312v3#bib.bib73)) . Results show that over 90% of drafts fall below the NPU-unfriendly length, significantly reducing the verification speed as NPU computing capacity is underutilized. This results in a similar speed to CPU (shown in the horizontal line). For instance, the verification speed of Qwen2.5 1.5B drops from 5.7 ms/token to 51.1 ms/token when the draft length decreases from 32 to 1.

## 3. Methodology

### 3.1. Overview

![Refer to caption](x8.png)


Figure 7. Overview of sd.npu framework.††:

Design goal.
sd.npu accelerates context-augmented generation by NPU-optimized retrieval-based speculative decoding. This entails (1) deploying and scheduling two compute graphs optimized for prefill and decoding, (2) aligning task context with LLM distribution, and (3) enriching drafts with sufficient high-value tokens to fully utilize NPU resources.

Workflow.
Figure [7](https://arxiv.org/html/2510.15312v3#acmlabel2 "Figure 7 ‣ 3.1. Overview ‣ 3. Methodology ‣ Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution") illustrates the system architecture and workflow of sd.npu.

* •

  Offline stage.
  sd.npu partitions the LLM into multiple blocks, each containing several transformer layers. It profiles the load and compute latency of each block through warm-up to determine scheduling strategy.
* •

  Online stage.
  Upon receiving a request, sd.npu fetches task-relevant database and performs prefill using a SOTA chunk-based approach (Xu et al., [2025b](https://arxiv.org/html/2510.15312v3#bib.bib76); Chen et al., [2025a](https://arxiv.org/html/2510.15312v3#bib.bib12)), splitting the input into chunks processed by a long-sequence optimized graph. During prefill, progressive graph scheduling (Section [3.2](https://arxiv.org/html/2510.15312v3#S3.SS2 "3.2. Progressive Graph Scheduling ‣ 3. Methodology ‣ Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution")) incrementally switches the prefill-optimized graph to the decoding-optimized graph with load overlapped by computation. After prefill, output logits are used for in-context distribution calibration (Section [3.3](https://arxiv.org/html/2510.15312v3#S3.SS3 "3.3. In-Context Distribution Calibration ‣ 3. Methodology ‣ Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution")), augmenting the database with calibrated contexts. sd.npu then performs retrieval-based speculative decoding using the decoding-optimized graph and the calibrated database. It iteratively constructs a drafting tree and verifies it via a confidence-based strategy to identify and reuse valuable tokens (Section [3.4](https://arxiv.org/html/2510.15312v3#S3.SS4 "3.4. NPU-Optimized Draft Reuse ‣ 3. Methodology ‣ Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution")). After an end-of-sequence token is predicted, the final response is returned and stored in the database manager as a historical context for future requests.

Key techniques.
sd.npu incorporates three techniques to align retrieval-based speculative decoding with NPU offloading:

* •

  Progressive NPU graph scheduling (Section [3.2](https://arxiv.org/html/2510.15312v3#S3.SS2 "3.2. Progressive Graph Scheduling ‣ 3. Methodology ‣ Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution")) enables asynchronous graph switching by overlapping load and computation across chunked prefill rounds.
* •

  In-context distribution calibration (Section [3.3](https://arxiv.org/html/2510.15312v3#S3.SS3 "3.3. In-Context Distribution Calibration ‣ 3. Methodology ‣ Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution")) aligns task context with model expectations using prefill logits.
* •

  NPU-optimized draft reuse (Section [3.4](https://arxiv.org/html/2510.15312v3#S3.SS4 "3.4. NPU-Optimized Draft Reuse ‣ 3. Methodology ‣ Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution")) maximizes NPU utilization and reduces verification costs by reusing plausible tokens from rejected drafts.

### 3.2. Progressive Graph Scheduling

Challenges of fixed-shape compute graphs.
As discussed in Section [2.3](https://arxiv.org/html/2510.15312v3#S2.SS3 "2.3. Challenges: Aligning Retrieval-based Speculative Decoding with NPU ‣ 2. Background ‣ Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution"), mobile NPUs require fixed-shape compute graphs, forcing the prefill input to be chunked for variable-length requests. This constraint also forces prefill and decoding to share the same graph despite their distinct input patterns: prefill processes long sequences (e.g., chunk size 256), while decoding handles short inputs (e.g., chunk size 32). Using a unified graph thus leads to inefficiency. To address this, we consider two specialized graphs: G1G^{1} optimized for prefill and G2G^{2} optimized for decoding. We denote the computation latency of a forward pass of model P\operatorname{P} on graph GxG^{x} (x∈{1,2}x\in\{1,2\}) as Tcompute​(P;Gx)T\_{\text{compute}}(\operatorname{P};G^{x}).

Enabling two graphs on NPUs raises two problems: (1) *keeping two graphs in the memory for high efficiency incurs a significant memory overhead*. Although G1G^{1} and G2G^{2} share the same weights, the NPU cannot reuse them across graphs for efficiency reasons, resulting in a redundant 2×\times memory footprint; otherwise, (2) *dynamically loading the decoding graph after prefill stage completes saves memory, but incurs a significant performance overhead* (Figure [8(b)](https://arxiv.org/html/2510.15312v3#S3.F8.sf2 "In Figure 8 ‣ 3.2. Progressive Graph Scheduling ‣ 3. Methodology ‣ Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution")\scriptsize1⃝). This *synchronous loading* approach delays decoding by load time Tload​(P;G2)T\_{\text{load}}(\operatorname{P};G^{2}).
To address this, an intuitive idea is *asynchronous loading*, where the model P\operatorname{P} is partitioned into NN blocks {P1,…,PN}\{\operatorname{P}\_{1},\dots,\operatorname{P}\_{N}\} and G2G^{2} is loaded block-by-block after computing finishes (Figure [8(b)](https://arxiv.org/html/2510.15312v3#S3.F8.sf2 "In Figure 8 ‣ 3.2. Progressive Graph Scheduling ‣ 3. Methodology ‣ Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution")\scriptsize2⃝). Yet this is suboptimal because: (i) prefill input is chunked, so G1G^{1} can only switch after the last chunk; and (ii) load time Tload​(Pi;G2)T\_{\text{load}}(\operatorname{P}\_{i};G^{2}) may exceed compute time Tcompute​(Pj;Gx)T\_{\text{compute}}(\operatorname{P}\_{j};G^{x}), leaving no effective overlap.

Switching graph progressively.
sd.npu gradually switches G1G^{1} to G2G^{2} during prefill. The design builds on two insights:

* •

  Graph equivalence by repetition: executing G2G^{2} multiple times on shorter inputs yields the same result as one execution of G1G^{1} on longer inputs, allowing early switching. As sd.npu maximizes draft lengths (Section [3.4](https://arxiv.org/html/2510.15312v3#S3.SS4 "3.4. NPU-Optimized Draft Reuse ‣ 3. Methodology ‣ Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution")), G2G^{2} will not be too short (e.g., chunk/2 or chunk/4 of G1G^{1}), which will not incur much performance degradation.
* •

  Chunk-level scheduling: multiple block computation can be overlapped with a single block loading.

![Refer to caption](x9.png)


(a) Progressive switching overlaps G2G^{2} loading with computation across blocks.

![Refer to caption](x10.png)


(b) sd.npu (\scriptsize3⃝) hides load latency compared to synchronous (\scriptsize1⃝) and naive asynchronous (\scriptsize2⃝) scheduling.

Figure 8. Progressive graph scheduling example with N=6N=6 and two chunks. (a) shows the workflow of chunk 1 computation; (b) compares prefill pipelines under different scheduling schemes.

Figure [8](https://arxiv.org/html/2510.15312v3#S3.F8 "Figure 8 ‣ 3.2. Progressive Graph Scheduling ‣ 3. Methodology ‣ Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution") illustrates progressive scheduling with N=6N=6 and two input chunks. We suppose that sd.npu decides to overlap loading a block by two blocks of computation based on the profiling results. Initially, all blocks are loaded with G1G^{1}. sd.npu computes P1,P2\operatorname{P}\_{1},\operatorname{P}\_{2} with G1G^{1} while loading G2G^{2} for P6\operatorname{P}\_{6}. Then P3,P4\operatorname{P}\_{3},\operatorname{P}\_{4} execute while G2G^{2} loads for P5\operatorname{P}\_{5}. To compute P5,P6\operatorname{P}\_{5},\operatorname{P}\_{6} under G2G^{2}, chunk 1 is split into sub-chunks matching G2G^{2}’s shape, with G2G^{2} executed repeatedly. Prefill of chunk 1 finishes with output logits while half of the model is switched. The same procedure applies to chunk 2. In contrast, synchronous loading waits for all compute to finish, and naive asynchronous loading only overlaps in chunk 2, both incurring higher latency (Figure [8(b)](https://arxiv.org/html/2510.15312v3#S3.F8.sf2 "In Figure 8 ‣ 3.2. Progressive Graph Scheduling ‣ 3. Methodology ‣ Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution")).

Problem Formulation.
Formally, given NN model blocks that sequentially execute prefill for CC chunks, sd.npu aims to determine the time to load each block, i.e., choosing blocks {Pi,…}\{\operatorname{P\_{i},\dots}\} to overlap load overhead of Pj\operatorname{P\_{j}} by their computations at each compute-load round. The objective is to minimize the overall latency, which is equal to the maximum of the prefill completion time and the switch completion time.

Scheduling methodology. This scheduling problem is NP-hard as it is essentially equivalent to the *2-Partition* problem (Korf, [1998](https://arxiv.org/html/2510.15312v3#bib.bib29))
(proofed in Appendix [A](https://arxiv.org/html/2510.15312v3#A1 "Appendix A NP-hardness Proof of the Graph Scheduling Problem ‣ Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution")).
sd.npu addresses this via a greedy algorithm, choosing the least kk consecutive blocks {Pi,…,Pi+k−1}\{\operatorname{P}\_{i},\dots,\operatorname{P}\_{i+k-1}\} that overlap a block load to execute. This strategy enables fully masking the load overhead by computation to minimize switching overhead.
sd.npu finds the smallest kk by estimating T^load​(Pj;G2)\widehat{T}\_{\text{load}}(\operatorname{P}\_{j};G^{2}) and T^compute​(Pi;Gix)\widehat{T}\_{\text{compute}}(\operatorname{P}\_{i};G^{x}\_{i}) based on the profiling results.
To hide load latency, the sum of the next kk blocks’ compute time must be larger than the load overhead of the last block not switched, formulated as:

|  |  |  |  |
| --- | --- | --- | --- |
| (1) |  | T^load​(Pj;G2)≤∑ℓ=0k−1T^compute​(Pi+ℓ;Gi+ℓx).\displaystyle\widehat{T}\_{\text{load}}(\operatorname{P}\_{j};G^{2})\;\leq\;\sum\_{\ell=0}^{k-1}\widehat{T}\_{\text{compute}}(\operatorname{P}\_{i+\ell};G^{x}\_{i+\ell}). |  |

sd.npu greedily chooses the minimal feasible kk that satisfies Equation [1](https://arxiv.org/html/2510.15312v3#S3.E1 "In 3.2. Progressive Graph Scheduling ‣ 3. Methodology ‣ Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution"):

|  |  |  |  |
| --- | --- | --- | --- |
| (2) |  | k⋆=min⁡{k≥1|T^load​(Pj;G2)≤∑ℓ=0k−1T^compute​(Pi+ℓ;Gi+ℓx)}.\displaystyle k^{\star}\;=\;\min\Big\{k\geq 1\;\big|\;\widehat{T}\_{\text{load}}(\operatorname{P}\_{j};G^{2})\leq\sum\_{\ell=0}^{k-1}\widehat{T}\_{\text{compute}}(\operatorname{P}\_{i+\ell};G^{x}\_{i+\ell})\Big\}. |  |

Then sd.npu executes Pi,…,Pi+k⋆−1\operatorname{P}\_{i},\dots,\operatorname{P}\_{i+k^{\star}-1} under current graphs while loading G2G^{2} for Pj\operatorname{P}\_{j}. This process repeats until all blocks are switched.

### 3.3. In-Context Distribution Calibration

Challenges of language divergence.
As discussed in Section [2.1](https://arxiv.org/html/2510.15312v3#S2.SS1 "2.1. On-device Context-Augmented Generation for Mobile Task ‣ 2. Background ‣ Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution"), leveraging similarity on mobile LLMs is hindered by distribution divergence between task context and LLM modeling. Models often interpret the context with different lexical patterns, thus reducing the acceptance ratio of drafts directly generated from the context.
These lexical gaps appear prominently at the token level. For example, in Figure [9](https://arxiv.org/html/2510.15312v3#acmlabel3 "Figure 9 ‣ 3.3. In-Context Distribution Calibration ‣ 3. Methodology ‣ Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution"), a user request states “… Clinton’s security detail has arrived at Des Moines …,” while the LLM, tasked with summarizing, prefers “Clinton arrived at Des Moines.” For classical retrieve-based speculative decoding approaches (Saxena, [2023](https://arxiv.org/html/2510.15312v3#bib.bib57); He et al., [2024](https://arxiv.org/html/2510.15312v3#bib.bib23); Hu et al., [2024](https://arxiv.org/html/2510.15312v3#bib.bib25)), draft “Clinton’s security” is rejected due to lexical mismatch between token ’s and target arrived. This results in only one token is generated (arrived) by one forward pass as the following draft security is discarded, reducing decoding efficiency.
Such mismatch problem arises in various mobile scenarios such as auto-reply or RAG-based QA, where human-written contexts diverge from the model’s distribution.

![Refer to caption](x11.png)


Figure 9. Overview of in-context distribution calibration with a summarization example. ††:

To tackle this issue, one may forcibly accept drafts with lexical gaps based on semantic-level similarity. However, setting a stringent similarity threshold results in a low acceptance ratio with only marginal performance gains, whereas a loose threshold causes non-negligible accuracy loss, e.g., drops from 0.9 to 0.75 if candidates are forcibly accepted ignoring the distribution divergence (Holsman et al., [2025](https://arxiv.org/html/2510.15312v3#bib.bib24); Bachmann et al., [2025](https://arxiv.org/html/2510.15312v3#bib.bib5)).
This necessitates calibration of draft and model distributions.
A straightforward solution is to precompute a calibrated database by running large volumes of user inputs through the LLM, which suffers from poor generalization to unseen queries and requires prohibitive storage and offline processing. Another method is to fine-tune the LLM to adapt to specific task scenarios, which also consumes lots of resources and energy and is hard to cover the wide diversity of mobile tasks.

Leveraging prefill logits.
To avoid heavy offline or fine-tuning costs, our key observation is that after prefill completes, next-token logits for each token in the entire context have already been calculated. These logits reflect how LLM encodes task semantics and can be used to approximate the model distribution. To that end, we can build a calibrated database for drafting with negligible performance overhead. Therefore, we propose in-context distribution calibration, an online, lightweight method that dynamically aligns context with the LLM distribution using prefill logits.

Workflow.
After prefill, sd.npu first collects predicted logits for all positions. Then sd.npu builds a calibrated token tree representing the model distribution by depth-first search, which includes two steps:

* •

  Sample (Figure [9](https://arxiv.org/html/2510.15312v3#acmlabel3 "Figure 9 ‣ 3.3. In-Context Distribution Calibration ‣ 3. Methodology ‣ Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution") \scriptsize1⃝). Given a token in the context (“Clinton” in the example), its next tokens with high-probability are sampled, i.e., has, arrived, and ’s. These <context, prediction> pairs (Clinton-has, Clinton-arrived, Clinton-’s) form calibrated candidates for draft retrieval as they reflect the LLM’s intrinsic distribution.
* •

  Search (Figure [9](https://arxiv.org/html/2510.15312v3#acmlabel3 "Figure 9 ‣ 3.3. In-Context Distribution Calibration ‣ 3. Methodology ‣ Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution") \scriptsize2⃝). sd.npu searches the occurrence of the calibrated token in the context. Once found (“arrived” in the example), it performs Step \scriptsize1⃝ on that token using its prefill logits to estimate the successors of the calibrated tokens, such as at, in, or . in the example.

Finally, sd.npu augments the calibrated tree into the database as a model-aligned retrieval source for drafting. In this example (Figure [9](https://arxiv.org/html/2510.15312v3#acmlabel3 "Figure 9 ‣ 3.3. In-Context Distribution Calibration ‣ 3. Methodology ‣ Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution") \scriptsize3⃝), token “Clinton” produces the draft candidate “Clinton arrived at” based on the calibrated tree, which is accepted in verification.

Overhead analysis.
The main costs come from sampling and storing calibrated results. In our experiments, sampling incurs an amortized latency of about 2 ms per input token, while building and maintaining calibrated tokens peak below 500 MB memory for a 3B model (Section [4.3](https://arxiv.org/html/2510.15312v3#S4.SS3 "4.3. Memory Overhead ‣ 4. Evaluation ‣ Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution")).

### 3.4. NPU-Optimized Draft Reuse

Challenges of short potentially acceptable drafts.
Existing studies on R-SD focus on improving draft quality, proposing techniques such as pruning draft tree by estimating token confidence (Somasundaram et al., [2024](https://arxiv.org/html/2510.15312v3#bib.bib60); Hu et al., [2024](https://arxiv.org/html/2510.15312v3#bib.bib25); Wu et al., [2025a](https://arxiv.org/html/2510.15312v3#bib.bib71)).
However, as discussed in Section [2.3](https://arxiv.org/html/2510.15312v3#S2.SS3 "2.3. Challenges: Aligning Retrieval-based Speculative Decoding with NPU ‣ 2. Background ‣ Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution"), a large proportion of drafts generated by existing methods have short lengths, which is harmful to the NPU efficiency.
Naively lengthening drafts by loosing retrieving conditions cannot obtain performance benefits as irrelevant tokens will be rejected in verification.

Reuse plausible drafts.
As highlighted in Section [2.1](https://arxiv.org/html/2510.15312v3#S2.SS1 "2.1. On-device Context-Augmented Generation for Mobile Task ‣ 2. Background ‣ Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution"), the model output usually shares similar semantics with the task context despite existing lexical gaps. Although these gaps cause rejection due to token-level misalignment, the rejected tokens include correct semantics and may be accepted in the next verification. sd.npu identifies and reuses these plausible tokens to construct NPU-friendly drafts lengthened by task-relevant information.

Table 2. Given draft T,x1​…​xnT,x\_{1}\dots x\_{n} which misaligns with target z1​…​zn+1z\_{1}\dots z\_{n+1} at position ee, the possible patterns of segment ze​…​znz\_{e}\dots z\_{n} and corresponding reusable tokens. In cases missing and synonymous, tokens after xe+ϵx\_{e+\epsilon} are omitted for simplicity.

| Case | Pattern | Reusable | Ratio |
| --- | --- | --- | --- |
| Missing | ze​…​ze+δ​xe​…​xe+ϵz\_{e}\dots z\_{e+\delta}x\_{e}\dots x\_{e+\epsilon} | xe​…​xe+ϵx\_{e}\dots x\_{e+\epsilon} | 15.4% |
| Synonym | ze​…​ze+δ​xe+γ​…​xe+ϵz\_{e}\dots z\_{e+\delta}x\_{e+\gamma}\dots x\_{e+\epsilon} | xe+γ​…​xe+ϵx\_{e+\gamma}\dots x\_{e+\epsilon} | 23.1% |
| Redundant | ze​…​znz\_{e}\dots z\_{n} | ∅\emptyset | 61.5% |

Rejection causes analysis.
We first analyze the rejection reasons to explore how to identify plausible tokens. Let 𝐱=[T,x1,…,xn]\mathbf{x}=[T,x\_{1},\dots,x\_{n}] be the draft sequence where TT is the most recently accepted token, and 𝐲=[y1,…,yn+1]\mathbf{y}=[y\_{1},\dots,y\_{n+1}] be the model’s predictions. Suppose the expected sequence is 𝐳=[z1,…,zn+1]\mathbf{z}=[z\_{1},\dots,z\_{n+1}] and rejection occurs at position ee due to a mismatch: xe≠yex\_{e}\neq y\_{e}. Thus, the accepted sequence is x1,…,xe−1,yex\_{1},\dots,x\_{e-1},y\_{e}.
According to the patterns of the expected sequence ze​…​znz\_{e}\dots z\_{n}, we categorize reuse opportunities into three general cases and report their distribution, which is obtained by manually labeling the rejection causes from a user case of summarization. Table [2](https://arxiv.org/html/2510.15312v3#S3.T2 "Table 2 ‣ 3.4. NPU-Optimized Draft Reuse ‣ 3. Methodology ‣ Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution") summarizes the results, showing that nearly 40% of the cases include reused sequence portions.

* •

  Missing: the expected sequence includes additional tokens ze​…​ze+δ​(δ≥0)z\_{e}\dots z\_{e+\delta}\ (\delta\geq 0) not present in the draft, while the remaining draft tokens xe​…​xe+ϵ​(ϵ≥1)x\_{e}\dots x\_{e+\epsilon}\ (\epsilon\geq 1) match the expectation. Thus, the expected sequence is ze​…​ze+δ​xe​…​xe+ϵz\_{e}\dots z\_{e+\delta}x\_{e}\dots x\_{e+\epsilon}. If the combined sequence ze+δ​xe​…​xe+ϵz\_{e+\delta}x\_{e}\dots x\_{e+\epsilon} does not exist in the database, next retrieval will fail with no drafts generated. This could be recovered by reserving xe​…​xe+ϵx\_{e}\dots x\_{e+\epsilon}.
* •

  Synonym: the draft includes a semantically equivalent but lexically different segment xe​…​xe+γ−1​(γ≥1)x\_{e}\dots x\_{e+\gamma-1}\ (\gamma\geq 1), replaced in the expected response by ze​…​ze+δz\_{e}\dots z\_{e+\delta}. Similar failure occurs if the post-synonym tokens xe+γ​…​xe+ϵx\_{e+\gamma}\dots x\_{e+\epsilon} cannot be retrieved from database using ze+δz\_{e+\delta}. In this case, xe+γ​…​xe+ϵx\_{e+\gamma}\dots x\_{e+\epsilon} should be preserved.
* •

  Redundant: the entire draft xe​…​xnx\_{e}\dots x\_{n} is incorrect and fully diverges from the expected path. This is the only case where discarding the sequence is appropriate.

Reuse methodology.
To leverage reusable tokens in the first two cases, sd.npu aims to: (1) determine the start and end positions γ,ϵ\gamma,\epsilon of the maximum reusable segment; (2) estimate the reuse lifetime δ\delta, i.e., how many iterations the reused segment should be reserved for verification.

Enumerating all possible reuse strategies is of O​(N3)O(N^{3}) complexity, which is not suitable for online scheduling.
Therefore, sd.npu adopts a confidence-based and length-first reuse strategy, assuming that drafts aligned with model predictions are more likely to be accepted in future steps. Therefore, we identify and retain the longest segment of 𝐱\mathbf{x} such that xi=yix\_{i}=y\_{i} for all i∈[e+γ,e+ϵ]i\in[e+\gamma,e+\epsilon], by solving:

|  |  |  |  |
| --- | --- | --- | --- |
| (3) |  | γ,ϵ=argmaxγ,ϵ​(ϵ−γ)s.t. ​yi=xi,∀i∈[e+γ,e+ϵ]\displaystyle\gamma,\epsilon=\underset{\gamma,\epsilon}{\text{argmax}}(\epsilon-\gamma)\quad\text{s.t. }y\_{i}=x\_{i},\ \forall\ i\in[e+\gamma,e+\epsilon] |  |

Each reused segment is reserved for at least one iteration, and is discarded when the cumulative draft length of current decoding step exceeds a predefined threshold.

By maximizing draft length with potentially acceptable tokens, this reuse mechanism directly enhances NPU utilization and reduces verification times. The overhead of sd.npu’s drafting and reusing processes is near ignorable with ¡3 ms per decoding step, as discussed in Section [4.4](https://arxiv.org/html/2510.15312v3#S4.SS4 "4.4. Latency Breakdown ‣ 4. Evaluation ‣ Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution").

## 4. Evaluation

### 4.1. Implementation and Setup

Implementation.
We implement sd.npu  on top of the mllm framework (Xu et al., [2025b](https://arxiv.org/html/2510.15312v3#bib.bib76)) with approximately 6,000 lines of C/C++ code. We reuse the NPU backend of mllm, including neural kernels and memory managers, to perform prefill and draft verification.
sd.npu inherits kernel-level and layer-level optimizations from mllm and further extends the system with speculative decoding capabilities. Our modular design allows easy porting to other mobile LLM inference frameworks that face NPU inefficiencies during decoding.
To enable NPU-optimized speculative decoding, we augment mllm with customized kernels and sampling strategies. In order to accelerate drafting, we implement a suffix automaton to identify potential suffix matches (Mohri et al., [2009](https://arxiv.org/html/2510.15312v3#bib.bib45)). To support NPU graph switching, we integrate the graph saving and loading APIs provided by the Qualcomm QNN SDK (Qualcomm, [2025a](https://arxiv.org/html/2510.15312v3#bib.bib52)).

Hardware.
We evaluate sd.npu on three representative smartphones with Qualcomm SoCs: Redmi K60 Pro (Snapdragon 8 Gen 2, Android 13, 12 GB RAM), Redmi K70 Pro (Snapdragon 8 Gen 3, Android 14, 16 GB RAM), and OnePlus 13 (Snapdragon 8 Gen Elite, Android 14, 24 GB RAM).
All devices are evaluated under real mobile conditions with the CPU frequency governed by the Android OS’s dynamic voltage and frequency scaling controller.

Datasets.
We evaluate four common mobile tasks collected from prior work: document summarization (summary), RAG-based question answering (rag), UI automation (ui) and automatic message reply (tweet) (Xia et al., [2024](https://arxiv.org/html/2510.15312v3#bib.bib73); Xing et al., [2024](https://arxiv.org/html/2510.15312v3#bib.bib74); Salemi et al., [2023](https://arxiv.org/html/2510.15312v3#bib.bib55)).

Models.
We use Qwen2.5-0.5B-Instruct, Qwen2.5-1.5B-Instruct and LLaMA3.2-3B-Instruct (Qwen et al., [2025](https://arxiv.org/html/2510.15312v3#bib.bib54); Grattafiori et al., [2024](https://arxiv.org/html/2510.15312v3#bib.bib19)), exploring the effect of different model size.

Baselines.
We compare sd.npu against six baselines, all implemented atop mllm to eliminate performance gaps from backend design differences
111Other existing mobile LLM inference frameworks with NPU offloading support such as PowerInfer-v2 (Xue et al., [2024](https://arxiv.org/html/2510.15312v3#bib.bib78)) and HeteroLLM (Chen et al., [2025a](https://arxiv.org/html/2510.15312v3#bib.bib12)) are not open-source, making them unsuitable for direct implementation. sd.npu, as a decoding optimization, is orthogonal and integrable with PowerInfer-v2 and HeteroLLM, so we do not compare it directly.
EdgeLLM (Xu et al., [2025a](https://arxiv.org/html/2510.15312v3#bib.bib75)) optimizes model-based SD mainly to alleviate memory constraints. With sufficient memory, its performance reduces to that of EAGLE and does not address the memory-bound issue of decoding, thus making it an uninformative baseline for our settings.
.
All baselines use NPU for prefill, which is a widely-adopted approach for both industry and academic (Xu et al., [2025b](https://arxiv.org/html/2510.15312v3#bib.bib76); Chen et al., [2025a](https://arxiv.org/html/2510.15312v3#bib.bib12); Li et al., [2024a](https://arxiv.org/html/2510.15312v3#bib.bib35); Xue et al., [2024](https://arxiv.org/html/2510.15312v3#bib.bib78)).
We categorize these baselines by whether they use CPU for decoding or apply speculative decoding:

* •

  (1)NPU vanilla: use NPU for both prefill and decoding222mllm (Xu et al., [2025b](https://arxiv.org/html/2510.15312v3#bib.bib76)) and other on-device LLM engines  (Chen et al., [2025a](https://arxiv.org/html/2510.15312v3#bib.bib12); Xue et al., [2024](https://arxiv.org/html/2510.15312v3#bib.bib78)) offload precision-sensitive operations, such as attention, to CPU/GPU to improve response quality. sd.npu follows this pattern even in the NPU vanilla mode.;
* •

  (2)CPU vanilla: use NPU for prefill and CPU for decoding, adopted by recent frameworks such as mllm and HeteroLLM (Xu et al., [2025b](https://arxiv.org/html/2510.15312v3#bib.bib76); Chen et al., [2025a](https://arxiv.org/html/2510.15312v3#bib.bib12));
* •

  (3)NPU-SAM: apply retrieval-based speculative decoding (SAM (Hu et al., [2024](https://arxiv.org/html/2510.15312v3#bib.bib25))) to NPU vanilla. SAM drafts from both historical and local contexts, serving as a standard retrieval-based baseline without mobile-specific optimization;
* •

  (4)NPU-SAM: similar to (3) but decoding on the CPU;
* •

  (5)NPU-EAGLE: apply model-based speculative decoding (EAGLE-2 (Li et al., [2024b](https://arxiv.org/html/2510.15312v3#bib.bib37))) to NPU vanilla. EAGLE-2 is the SOTA model-based SD approach that uses both tokens and hidden states for drafting through a pretrained transformer-like model;
* •

  (6)CPU-EAGLE: similar to (5) but decoding on the CPU.

Since EAGLE-2 requires a separate draft model that is unavailable for selected LLMs, baselines (5) and (6) are simulated by estimating the expected speed via amortizing the forward costs of the target and draft model. We approximate the draft model as a single transformer layer with a head layer of the target LLM, assuming a fixed maximum acceptance ratio of 5.5, as reported in its paper (Li et al., [2024b](https://arxiv.org/html/2510.15312v3#bib.bib37)).

Metrics and Configuration.
We evaluate average per-token latency, energy consumption and peak memory. We exclude accuracy comparison as sd.npu achieves lossless generation (Leviathan et al., [2023a](https://arxiv.org/html/2510.15312v3#bib.bib32)).
Energy is measured via Android’s virtual file system under `/sys/class/power_supply` by profiling every 100ms. The Redmi K70 Pro is excluded from energy results as the device lacks root access. Experiments are repeated three times and we report the average numbers.

### 4.2. Overall Performance

Per-Token Latency. sd.npuis faster and achieves improvements ranging 1.06–3.81×, as shown in Figure [10](https://arxiv.org/html/2510.15312v3#acmlabel4 "Figure 10 ‣ 4.2. Overall Performance ‣ 4. Evaluation ‣ Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution").

![Refer to caption](x12.png)


Figure 10. Per-token latency (ms/token) comparison on different datasets, devices and models. ††:

∙\bullet Compared to baselines without SD (NPU vanilla and CPU vanilla), sd.npu consistently reduces per-token latency by 1.14–3.81× and 1.06–1.78×. These performance gains stem from both the NPU-optimized SD method and the specialized compute graphs.
Larger improvements are observed on small-to-medium models (e.g., Qwen2.5 0.5B and 1.5B) as their inference is memory-bound which is preferred by SD.
Comparing different datasets, we find that tasks with higher context similarity such as summary, exhibit higher speed gains (1.41–3.80×, 1.24–1.61×) since SD is more effective.

∙\bullet Compared to baselines with SD, sd.npu consistently improves by 1.11–2.53× than SAM, 1.09–1.80× than EAGLE. This arises because SAM ignores the ineffectiveness of computing short drafts on NPUs while EAGLE suffers from the latency of running another parametric model.
Improvements of applying SD on CPU vanilla are moderate (0.92–1.13× for SAM, 0.56–1.18× for EAGLE), as LLM inference on mobile CPU is compute-bound due to the limited CPU capacity.

Energy Consumption. sd.npu is more energy-efficient and reduces energy consumption by 1.07–4.71× (Figure [11](https://arxiv.org/html/2510.15312v3#acmlabel5 "Figure 11 ‣ 4.2. Overall Performance ‣ 4. Evaluation ‣ Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution")).

∙\bullet Compared to baselines without SD (NPU vanilla and CPU vanilla), sd.npu significantly reduces energy consumption by 1.35–4.18× and 1.11–2.50×. The improvements stem jointly from the higher generation speed and the avoidance of CPU computation, allowing energy-efficient utilization of NPUs. On larger models (e.g., Llama3.2 3B), the effectiveness becomes less pronounced (1.42–1.85×) as relatively longer inference time results in the device continues working under a high power consumption.

∙\bullet Compared to baselines with SD, sd.npu consumes significantly less energy than SAM (1.07–3.07×) and EAGLE (1.77–4.71×). Energy saving of SAM is limited due to frequent verification incurred by rejected drafts. EAGLE suffers from additional computation required by drafter, amplifying energy overhead. For instance, for Qwen2.5 0.5B, sd.npu reduces energy ranging 1.40–3.50× compared with NPU vanilla, while SAM reduces energy by only 1.17–1.54× and EAGLE even increases energy consumption.

Comparison Across Devices.
We find that NPU computation on Redmi K70 Pro is much slower than on other devices, while Redmi K60 Pro and Oneplus 13 demonstrate relatively similar performance patterns. This results in less profound latency improvements on Redmi K70 Pro (e.g., 1.14–2.91× compared to NPU vanilla and 1.13–1.64× compared to CPU vanilla) as compute becomes the bottleneck. In terms of energy consumption, Oneplus 13 consumes more energy than Redmi K60 Pro, e.g., average 53.85 J and 56.52 J per request for Qwen2.5 1.5B.

![Refer to caption](x13.png)


Figure 11. Energy consumption (J) comparison on different datasets, devices and models. ††:

### 4.3. Memory Overhead

![Refer to caption](x14.png)


Figure 12. Peak memory comparison (GB) on different devices and models. ††:

As shown in Figure [12](https://arxiv.org/html/2510.15312v3#acmlabel6 "Figure 12 ‣ 4.3. Memory Overhead ‣ 4. Evaluation ‣ Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution"), sd.npu maintains a memory footprint close to NPU vanilla with an additional overhead less than 500 MB across all evaluations.
For example, sd.npu requires 3.14 GB for Qwen2.5 1.5B, nearly identical to NPU vanilla (3.05–3.12 GB), while CPU vanilla requires over 6 GB. This gap comes from maintaining separate weights for CPU and NPU in heterogeneous baselines.

The memory overhead of sd.npu primarily arises from distribution calibration and context-relevant database structures, which is manageable for mobile devices with limited memory.
In contrast, EAGLE’s memory usage increases noticeably (0.84–1.22 GB) due to maintaining the drafter model, highlighting that sd.npu delivers superior efficiency without sacrificing memory scalability.

### 4.4. Latency Breakdown

To analyze the runtime characteristics and latency overhead of sd.npu, we decompose the end-to-end inference latency into prefill, decoding and potential overhead. Measurements are conducted on Oneplus 13 under the summary benchmark, with results shown in Figure [13](https://arxiv.org/html/2510.15312v3#acmlabel7 "Figure 13 ‣ 4.4. Latency Breakdown ‣ 4. Evaluation ‣ Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution").

![Refer to caption](x15.png)


Figure 13. Breakdown of inference latency (ms). ††:

The results show that sd.npu significantly accelerates both prefill and decoding compared to NPU vanilla baseline, with little additional overhead. Specifically, decoding of NPU vanilla baseline consumes a substantial portion of total latency (67–74%), highlighting the significance of introducing specialized optimization. sd.npu directly addresses this by integrating retrieval-based speculative decoding, reducing decoding latency by 5.25–8.15×.

The prefill overhead is due to sampling tokens from logits for distribution calibration, which costs about 2 ms for each input token. The decoding overhead is caused by draft retrieval and tree construction. Benefited from the low time complexity of suffix automaton, our drafter costs less than 3 ms for each decoding step. Overall, our lightweight techniques incur negligible overhead compared to the overall inference cost.

### 4.5. Ablation Study

Effectiveness of three techniques.
Experiments are conducted on Redmi K60 Pro using the summary benchmark across four baselines: (1) NPU vanilla (NPU), (2) NPU-SAM (+SD), (3) NPU-Graph (+G), and (4) NPU-SAM-Graph (+G+SD). Baselines (1)(2) are identical with those in Section [4.2](https://arxiv.org/html/2510.15312v3#S4.SS2 "4.2. Overall Performance ‣ 4. Evaluation ‣ Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution"), while (3)(4) integrate progressive graph scheduling into (1) and (2), respectively. Results are reported in Table [3](https://arxiv.org/html/2510.15312v3#S4.T3 "Table 3 ‣ 4.5. Ablation Study ‣ 4. Evaluation ‣ Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution").

Table 3. Ablation experiments on average per-token latency (ms/token).

| Model | NPU | +G | +SD | +G+SD | Ours |
| --- | --- | --- | --- | --- | --- |
| Qwen2.5-1.5B | 57.41 | 47.72 | 35.04 | 25.35 | 15.08 |
| Qwen2.5-0.5B | 24.46 | 23.43 | 18.75 | 18.45 | 7.17 |
| LLaMA3.2-3B | 71.71 | 70.03 | 47.93 | 46.25 | 41.62 |

We observe that progressive graph scheduling provides consistent speed improvements regardless of whether SD is applied. For example, for Qwen2.5-1.5B, graph scheduling reduces latency from 57.41 ms to 47.72 ms. The results also show that in-context distribution calibration and NPU-optimized draft reuse contribute to significant performance gains across three models, reducing latency from 25.35 ms to 15.08 ms for Qwen2.5-1.5B.

Effectiveness in acceptance ratio.
To analyze the effectiveness of techniques relevant to R-SD, we evaluate the acceptance ratio gains applying our techniques to existing methods (PLD (Saxena, [2023](https://arxiv.org/html/2510.15312v3#bib.bib57)), SAM (Hu et al., [2024](https://arxiv.org/html/2510.15312v3#bib.bib25))). PLD drafts from local contexts only while SAM drafts from both local and historical contexts. Experiments are conducted on a cloud server equipped with A100 GPUs. The results in Table [4](https://arxiv.org/html/2510.15312v3#S4.T4 "Table 4 ‣ 4.5. Ablation Study ‣ 4. Evaluation ‣ Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution") show consistent improvements across benchmarks and models. Our techniques improve the acceptance ratio of PLD by 1.05–1.25×, improve SAM by 1.06–1.24×. These improvements directly translate to higher decoding efficiency, as a higher acceptance ratio reduces the number of tokens that must be recomputed.
These results also demonstrate that in-context distribution calibration and draft reuse strategy are orthogonal enhancements with existing R-SD methods, making it effortless to integrate advanced techniques.

Table 4. Ablation on acceptance ratio (average accepted tokens per verification).

| Dataset | Method | Q1.5B | Q7B | L1B |
| --- | --- | --- | --- | --- |
| summary | PLD | 2.53 | 1.55 | 1.42 |
| PLD+Ours | 2.91 (×\times1.15) | 1.84 (×\times1.18) | 1.70 (×\times1.19) |
| SAM | 3.60 | 1.96 | 1.68 |
| SAM+Ours | 4.21 (×\times1.17) | 2.43 (×\times1.24) | 2.07 (×\times1.24) |
| rag | PLD | 3.19 | 1.63 | 1.77 |
| PLD+Ours | 3.73 (×\times1.17) | 1.89 (×\times1.16) | 2.11 (×\times1.19) |
| SAM | 4.42 | 2.29 | 2.25 |
| SAM+Ours | 5.47 (×\times1.24) | 2.80 (×\times1.22) | 2.66 (×\times1.19) |
| ui | PLD | 2.28 | 1.64 | 1.57 |
| PLD+Ours | 2.64 (×\times1.16) | 1.73 (×\times1.05) | 1.82 (×\times1.16) |
| SAM | 3.56 | 2.44 | 1.72 |
| SAM+Ours | 4.01 (×\times1.13) | 2.59 (×\times1.06) | 2.05 (×\times1.20) |
| tweet | PLD | 2.53 | 2.06 | 1.49 |
| PLD+Ours | 3.17 (×\times1.25) | 2.52 (×\times1.22) | 1.72 (×\times1.15) |
| SAM | 3.57 | 2.98 | 1.79 |
| SAM+Ours | 3.82 (×\times1.07) | 3.70 (×\times1.24) | 2.18 (×\times1.22) |

Q1.5B = Qwen2.5 1.5B, Q7B = Qwen2.5 7B, L1B = LLaMA3.2 1B.

## 5. Related Work

Mobile LLM inference optimization.
The constrained resources of mobile devices require reducing computation to enable efficient on-device LLM inference (Xu et al., [2024](https://arxiv.org/html/2510.15312v3#bib.bib77); Subramanian et al., [2025](https://arxiv.org/html/2510.15312v3#bib.bib62); Ma et al., [2024](https://arxiv.org/html/2510.15312v3#bib.bib43); Thawakar et al., [2024](https://arxiv.org/html/2510.15312v3#bib.bib63); Xu et al., [2025a](https://arxiv.org/html/2510.15312v3#bib.bib75)). Several approaches exploit different forms of sparsity. Mixture-of-experts leverages activation sparsity by computing only neurons important to the final output (Yi et al., [2025](https://arxiv.org/html/2510.15312v3#bib.bib79); Chen et al., [2025c](https://arxiv.org/html/2510.15312v3#bib.bib10); Wu et al., [2025b](https://arxiv.org/html/2510.15312v3#bib.bib72); Frantar and Alistarh, [2024](https://arxiv.org/html/2510.15312v3#bib.bib17)). Early-exit reduces layer-level computation by skipping non-critical layers (Venkatesha et al., [2025](https://arxiv.org/html/2510.15312v3#bib.bib66); Fan et al., [2024](https://arxiv.org/html/2510.15312v3#bib.bib16)). Model compression reduces model size by retaining only the most valuable layers (Yu et al., [2024](https://arxiv.org/html/2510.15312v3#bib.bib81); Smith et al., [2025](https://arxiv.org/html/2510.15312v3#bib.bib59)). Token pruning eliminates redundant tokens to shorten the context (Liu et al., [2025b](https://arxiv.org/html/2510.15312v3#bib.bib40); Ma et al., [2023](https://arxiv.org/html/2510.15312v3#bib.bib44)). sd.npu is compatible with these techniques, as it requires no architectural modifications to models or inputs.

Mobile NPU offloading.
Modern mobile SoCs are increasingly equipped with high-performance NPUs (OPPO, [2024](https://arxiv.org/html/2510.15312v3#bib.bib48); Samsung, [2024](https://arxiv.org/html/2510.15312v3#bib.bib56); Huawei, [2024](https://arxiv.org/html/2510.15312v3#bib.bib26)), offering new opportunities for LLM acceleration (Xue et al., [2024](https://arxiv.org/html/2510.15312v3#bib.bib78); Chen et al., [2025a](https://arxiv.org/html/2510.15312v3#bib.bib12); Lu et al., [2025](https://arxiv.org/html/2510.15312v3#bib.bib42); Xu et al., [2025b](https://arxiv.org/html/2510.15312v3#bib.bib76); Yin et al., [2025](https://arxiv.org/html/2510.15312v3#bib.bib80); Wei et al., [2025](https://arxiv.org/html/2510.15312v3#bib.bib69)). PowerInfer-V2 (Xue et al., [2024](https://arxiv.org/html/2510.15312v3#bib.bib78)) integrates parameter swapping with NPU offloading to scale inference to larger LLMs. HeteroLLM (Chen et al., [2025a](https://arxiv.org/html/2510.15312v3#bib.bib12)) introduces tensor partitioning strategies tailored to mobile GPUs and NPUs for efficient parallelization. While these studies primarily focus on accelerating prefill, sd.npu complements them by incorporating speculative decoding to optimize both prefill and decoding.

Retrieval-augmented generation.
Retrieval-augmented generation (RAG) enhances LLM’s knowledge by retrieving relevant documents from an external database, enabling effective context-aware generation (Lewis et al., [2020](https://arxiv.org/html/2510.15312v3#bib.bib34)). Recent work explores advanced database architectures such as knowledge graph (Edge et al., [2024](https://arxiv.org/html/2510.15312v3#bib.bib14); Han et al., [2025](https://arxiv.org/html/2510.15312v3#bib.bib22); Zhang et al., [2025](https://arxiv.org/html/2510.15312v3#bib.bib82)). Other efforts optimize retrieval with adaptive strategies, such as extracting fine-grained information and caching key documents based on user demands (Jeong et al., [2024](https://arxiv.org/html/2510.15312v3#bib.bib27); Seemakhupt et al., [2024](https://arxiv.org/html/2510.15312v3#bib.bib58); Liu et al., [2025a](https://arxiv.org/html/2510.15312v3#bib.bib41)). RAG can be employed to augment the context for CAG.

Speculative decoding uses LLM as a verifier to process multiple draft tokens in parallel, shifting memory-bound decoding to compute-bound (Stern et al., [2018](https://arxiv.org/html/2510.15312v3#bib.bib61); Chen et al., [2023](https://arxiv.org/html/2510.15312v3#bib.bib9); Leviathan et al., [2023b](https://arxiv.org/html/2510.15312v3#bib.bib33)).
The main difference between these studies is how drafts are generated. Model-based methods employ an auxiliary parametric model, typically a smaller LLM (Li et al., [2024c](https://arxiv.org/html/2510.15312v3#bib.bib38), [b](https://arxiv.org/html/2510.15312v3#bib.bib37); Cai et al., [2024](https://arxiv.org/html/2510.15312v3#bib.bib8); Du et al., [2024](https://arxiv.org/html/2510.15312v3#bib.bib13); Li et al., [2025b](https://arxiv.org/html/2510.15312v3#bib.bib39)). Although these approaches improve the acceptance ratio, they introduce significant drafting overhead (Hu et al., [2024](https://arxiv.org/html/2510.15312v3#bib.bib25)). Retrieval-based methods avoid this cost by using lightweight retrievers for drafting, but often suffer from low acceptance ratios (Saxena, [2023](https://arxiv.org/html/2510.15312v3#bib.bib57); Somasundaram et al., [2024](https://arxiv.org/html/2510.15312v3#bib.bib60); Hu et al., [2024](https://arxiv.org/html/2510.15312v3#bib.bib25); Chen et al., [2025b](https://arxiv.org/html/2510.15312v3#bib.bib11); Li et al., [2025a](https://arxiv.org/html/2510.15312v3#bib.bib36); Gritta et al., [2025](https://arxiv.org/html/2510.15312v3#bib.bib20)).
sd.npu advances R-SD through hardware–algorithm co-design, integrating it with mobile NPUs for efficient acceleration.

## 6. Conclusions

In this paper, we propose sd.npu, the first framework designed to align retrieval-based speculative decoding with mobile NPUs to optimize context-augmented generation. sd.npu incorporates novel techniques such as progressive graph scheduling and in-context calibration to address the gaps between speculative decoding and NPUs. Extensive experiments demonstrate sd.npu achieves outstanding and consistent performance gains.

## References

* (1)
* AI (2024)

  HIX AI. 2024.
  *GPT-based email writer*.

  <https://hix.ai/ai-email-writer-emailgenerator/>
* Apple (2024a)

  Apple. 2024a.
  *Apple Intelligence*.

  <https://www.apple.com/apple-intelligence/>
* Apple (2024b)

  Apple. 2024b.
  *Siri*.

  <https://www.apple.com/siri/>
* Bachmann et al. (2025)

  Gregor Bachmann, Sotiris Anagnostidis, Albert Pumarola, Markos Georgopoulos, Artsiom Sanakoyeu, Yuming Du, Edgar Schönfeld, Ali Thabet, and Jonas Kohler. 2025.
  Judge Decoding: Faster Speculative Sampling Requires Going Beyond Model Alignment.
  *arXiv preprint arXiv:2501.19309* (2025).
* Belcak et al. (2025)

  Peter Belcak, Greg Heinrich, Shizhe Diao, Yonggan Fu, Xin Dong, Saurav Muralidharan, Yingyan Celine Lin, and Pavlo Molchanov. 2025.
  Small Language Models are the Future of Agentic AI.
  *arXiv preprint arXiv:2506.02153* (2025).
* Brown et al. (2020)

  Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, et al. 2020.
  Language Models Are Few-Shot Learners.
  *arXiv preprint arXiv:2005.14165* (2020).
* Cai et al. (2024)

  Tianle Cai, Yuhong Li, Zhengyang Geng, Hongwu Peng, Jason D. Lee, Deming Chen, and Tri Dao. 2024.
  MEDUSA: Simple LLM inference acceleration framework with multiple decoding heads. In *Proceedings of the 41st International Conference on Machine Learning*. Article 203, 27 pages.
* Chen et al. (2023)

  Charlie Chen, Sebastian Borgeaud, Geoffrey Irving, Jean-Baptiste Lespiau, Laurent Sifre, and John Jumper. 2023.
  Accelerating Large Language Model Decoding with Speculative Sampling.
  *arXiv preprint arXiv:2302.01318* (2023).
* Chen et al. (2025c)

  Fahao Chen, Jie Wan, Peng Li, Zhou Su, and Dongxiao Yu. 2025c.
  Federated Fine-Tuning of Sparsely-Activated Large Language Models on Resource-Constrained Devices.
  *arXiv preprint arXiv:2508.19078* (2025).
* Chen et al. (2025b)

  Guanzheng Chen, Qilong Feng, Jinjie Ni, Xin Li, and Michael Qizhe Shieh. 2025b.
  Long-Context Inference with Retrieval-Augmented Speculative Decoding.
  *arXiv preprint arXiv:2502.20330* (2025).
* Chen et al. (2025a)

  Le Chen, Dahu Feng, Erhu Feng, Rong Zhao, Yingrui Wang, Yubin Xia, Haibo Chen, and Pinjie Xu. 2025a.
  HeteroLLM: Accelerating Large Language Model Inference on Mobile SoCs platform with Heterogeneous AI Accelerators.
  *arXiv preprint arXiv:2501.14794* (2025).
* Du et al. (2024)

  Cunxiao Du, Jing Jiang, Xu Yuanchen, Jiawei Wu, Sicheng Yu, Yongqi Li, Shenggui Li, Kai Xu, Liqiang Nie, Zhaopeng Tu, and Yang You. 2024.
  GliDe with a CaPE: A Low-Hassle Method to Accelerate Speculative Decoding. In *Proceedings of the 41st International Conference on Machine Learning*, Vol. 235. 11704–11720.
* Edge et al. (2024)

  Darren Edge, Ha Trinh, Newman Cheng, Joshua Bradley, Alex Chao, Apurva Mody, Steven Truitt, Dasha Metropolitansky, Robert Osazuwa Ness, and Jonathan Larson. 2024.
  From local to global: A graph RAG approach to query-focused summarization.
  *arXiv preprint arXiv:2404.16130* (2024).
* Eleftherakis et al. (2024)

  Stavros Eleftherakis, Timothy Otim, Giuseppe Santaromita, Almudena Diaz Zayas, Domenico Giustiniano, and Nicolas Kourtellis. 2024.
  Demystifying privacy in 5G stand alone networks. In *Proceedings of the 30th Annual International Conference on Mobile Computing and Networking*. 1330–1345.
* Fan et al. (2024)

  Siqi Fan, Xin Jiang, Xiang Li, Xuying Meng, Peng Han, Shuo Shang, Aixin Sun, Yequan Wang, and Zhongyuan Wang. 2024.
  Not All Layers of LLMs Are Necessary During Inference.
  *arXiv preprint arXiv:2403.02181* (2024).
* Frantar and Alistarh (2024)

  Elias Frantar and Dan Alistarh. 2024.
  QMoE: Sub-1-Bit Compression of Trillion Parameter Models. In *Proceedings of Machine Learning and Systems*, Vol. 6. 439–451.
* Google (2024)

  Google. 2024.
  *AI Core*.

  <https://developer.android.com/ai/aicore>
* Grattafiori et al. (2024)

  Aaron Grattafiori, Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian, Ahmad Al-Dahle, Aiesha Letman, Akhil Mathur, Alan Schelten, Alex Vaughan, et al. 2024.
  The Llama 3 Herd of Models.
  *arXiv preprint arXiv:2407.21783* (2024).
* Gritta et al. (2025)

  Milan Gritta, Huiyin Xue, and Gerasimos Lampouras. 2025.
  DReSD: Dense Retrieval for Speculative Decoding.
  *arXiv preprint arXiv:2502.15572* (2025).
* Guo et al. (2024)

  Daya Guo, Qihao Zhu, Dejian Yang, Zhenda Xie, Kai Dong, Wentao Zhang, Guanting Chen, Xiao Bi, Yu Wu, YK Li, et al. 2024.
  DeepSeek-Coder: When the Large Language Model Meets Programming–The Rise of Code Intelligence.
  *arXiv preprint arXiv:2401.14196* (2024).
* Han et al. (2025)

  Haoyu Han, Harry Shomer, Yu Wang, Yongjia Lei, Kai Guo, Zhigang Hua, Bo Long, Hui Liu, and Jiliang Tang. 2025.
  RAG vs. GraphRAG: A systematic evaluation and key insights.
  *arXiv preprint arXiv:2502.11371* (2025).
* He et al. (2024)

  Zhenyu He, Zexuan Zhong, Tianle Cai, Jason Lee, and Di He. 2024.
  REST: Retrieval-Based Speculative Decoding. In *Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)*. 1582–1595.
  [doi:10.18653/v1/2024.naacl-long.88](https://doi.org/10.18653/v1/2024.naacl-long.88)
* Holsman et al. (2025)

  Maximilian Holsman, Yukun Huang, and Bhuwan Dhingra. 2025.
  Fuzzy Speculative Decoding for a Tunable Accuracy-Runtime Tradeoff.
  *arXiv preprint arXiv:2502.20704* (2025).
* Hu et al. (2024)

  Yuxuan Hu, Ke Wang, Xiaokang Zhang, Fanjin Zhang, Cuiping Li, Hong Chen, and Jing Zhang. 2024.
  SAM Decoding: Speculative Decoding via Suffix Automaton.
  *arXiv preprint arXiv:2411.10666* (2024).
* Huawei (2024)

  Huawei. 2024.
  *Huawei’s LLM on Mate 70 Series*.

  <https://www.huaweicentral.com/huawei-mate-70-serieslaunched-with-new-camera-design-5700mahbattery-generative-ai-and-more/>
* Jeong et al. (2024)

  Soyeong Jeong, Jinheon Baek, Sukmin Cho, Sung Ju Hwang, and Jong C Park. 2024.
  Adaptive-RAG: Learning to Adapt Retrieval-Augmented Large Language Models through Question Complexity. In *Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)*. 7029–7043.
* Jouppi et al. (2017)

  Norman P Jouppi, Cliff Young, Nishant Patil, David Patterson, Gaurav Agrawal, Raminder Bajwa, Sarah Bates, Suresh Bhatia, Nan Boden, Al Borchers, et al. 2017.
  In-datacenter performance analysis of a tensor processing unit. In *Proceedings of the 44th annual international symposium on computer architecture*. 1–12.
* Korf (1998)

  Richard E. Korf. 1998.
  A complete anytime algorithm for number partitioning.
  *Artificial Intelligence* 106, 2 (1998), 181–203.
  [doi:10.1145/3637528.3671650](https://doi.org/10.1145/3637528.3671650)
* Kshetri (2023)

  Nir Kshetri. 2023.
  Cybercrime and Privacy Threats of Large Language Models.
  *IT Professional* 25 (2023), 9–13.
* Lee et al. (2024)

  Sunjae Lee, Junyoung Choi, Jungjae Lee, Munim Hasan Wasi, Hojun Choi, Steve Ko, Sangeun Oh, and Insik Shin. 2024.
  Mobilegpt: Augmenting llm with human-like app memory for mobile task automation. In *Proceedings of the 30th Annual International Conference on Mobile Computing and Networking*. 1119–1133.
* Leviathan et al. (2023a)

  Yaniv Leviathan, Matan Kalman, and Yossi Matias. 2023a.
  Fast Inference from Transformers via Speculative Decoding. In *Proceedings of the 40th International Conference on Machine Learning*, Vol. 202. 19274–19286.
* Leviathan et al. (2023b)

  Yaniv Leviathan, Matan Kalman, and Yossi Matias. 2023b.
  Fast Inference from Transformers via Speculative Decoding. In *Proceedings of the 40th International Conference on Machine Learning*, Vol. 202. 19274–19286.
* Lewis et al. (2020)

  Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich Küttler, Mike Lewis, Wen-tau Yih, Tim Rocktäschel, et al. 2020.
  Retrieval-augmented generation for knowledge-intensive nlp tasks.
  *Advances in neural information processing systems* 33 (2020), 9459–9474.
* Li et al. (2024a)

  Luchang Li, Sheng Qian, Jie Lu, Lunxi Yuan, Rui Wang, and Qin Xie. 2024a.
  Transformer-lite: High-efficiency deployment of large language models on mobile phone gpus.
  *arXiv preprint arXiv:2403.20041* (2024).
* Li et al. (2025a)

  Yanhong Li, Karen Livescu, and Jiawei Zhou. 2025a.
  Chunk-Distilled Language Modeling. In *The 13th International Conference on Learning Representations*.
* Li et al. (2024b)

  Yuhui Li, Fangyun Wei, Chao Zhang, and Hongyang Zhang. 2024b.
  EAGLE-2: Faster Inference of Language Models with Dynamic Draft Trees. In *Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing*. 7421–7432.
* Li et al. (2024c)

  Yuhui Li, Fangyun Wei, Chao Zhang, and Hongyang Zhang. 2024c.
  EAGLE: speculative sampling requires rethinking feature uncertainty. In *Proceedings of the 41st International Conference on Machine Learning*. Article 1162, 14 pages.
* Li et al. (2025b)

  Yuhui Li, Fangyun Wei, Chao Zhang, and Hongyang Zhang. 2025b.
  EAGLE-3: Scaling up Inference Acceleration of Large Language Models via Training-Time Test.
  *arXiv preprint arXiv:2303.01840* (2025).
* Liu et al. (2025b)

  Kaiyuan Liu, Xiaobo Zhou, and Li Li. 2025b.
  m22LLM: A Multi-Dimensional Optimization Framework for LLM Inference on Mobile Devices.
  *IEEE Transactions on Parallel and Distributed Systems* 36, 10 (2025), 2014–2029.
  [doi:10.1109/TPDS.2025.3587445](https://doi.org/10.1109/TPDS.2025.3587445)
* Liu et al. (2025a)

  Mugeng Liu, Siqi Zhong, Qi Yang, Yudong Han, Xuanzhe Liu, and Yun Ma. 2025a.
  WebANNS: Fast and Efficient Approximate Nearest Neighbor Search in Web Browsers. In *Proceedings of the 48th International ACM SIGIR Conference on Research and Development in Information Retrieval*. 2483–2492.
* Lu et al. (2025)

  Xudong Lu, Yinghao Chen, Cheng Chen, Hui Tan, Boheng Chen, Yina Xie, Rui Hu, Guanxin Tan, Renshou Wu, Yan Hu, Yi Zeng, Lei Wu, Liuyang Bian, Zhaoxiong Wang, Long Liu, Yanzhou Yang, Han Xiao, Aojun Zhou, Yafei Wen, Xiaoxin Chen, Shuai Ren, and Hongsheng Li. 2025.
  BlueLM-V-3B: Algorithm and System Co-Design for Multimodal Large Language Models on Mobile Devices. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition)*. 4145–4155.
* Ma et al. (2024)

  Shuming Ma, Hongyu Wang, Lingxiao Ma, Lei Wang, Wenhui Wang, Shaohan Huang, Li Dong, Ruiping Wang, Jilong Xue, and Furu Wei. 2024.
  The Era of 1-bit LLMs: All Large Language Models are in 1.58 Bits.
  *arXiv preprint arXiv:2402.17764* (2024).
* Ma et al. (2023)

  Xinyin Ma, Gongfan Fang, and Xinchao Wang. 2023.
  LLM-Pruner: On the Structural Pruning of Large Language Models. In *Advances in Neural Information Processing Systems*, A. Oh, T. Naumann, A. Globerson, K. Saenko, M. Hardt, and S. Levine (Eds.), Vol. 36. 21702–21720.
* Mohri et al. (2009)

  Mehryar Mohri, Pedro Moreno, and Eugene Weinstein. 2009.
  General suffix automaton construction algorithm and space bounds.
  *Theoretical Computer Science* 410, 37 (2009), 3553–3562.
* Navardi et al. (2025)

  Mozhgan Navardi, Romina Aalishah, Yuzhe Fu, Yueqian Lin, Hai Li, Yiran Chen, and Tinoosh Mohsenin. 2025.
  GenAI at the Edge: Comprehensive Survey on Empowering Edge Devices.
  *arXiv preprint arXiv:2502.15816* (2025).
  arXiv:2502.15816
* OpenAI et al. (2024)

  OpenAI, Josh Achiam, Steven Adler, Sandhini Agarwal, Lama Ahmad, Ilge Akkaya, Florencia Leoni Aleman, Diogo Almeida, Janko Altenschmidt, Sam Altman, et al. 2024.
  GPT-4 Technical Report.
  *arXiv preprint arXiv:2303.08774* (2024).
* OPPO (2024)

  OPPO. 2024.
  *OPPO Announces Commitment to Making AI Phones Accessible to Everyone*.

  <https://www.oppo.com/en/newsroom/press/oppo-make-ai-phones-accessible/>
* Ouyang et al. (2025)

  Tao Ouyang, Guihang Hong, Kongyange Zhao, Zhi Zhou, Weigang Wu, Zhaobiao Lv, and Xu Chen. 2025.
  AdaRAG: Adaptive Optimization for Retrieval Augmented Generation with Multilevel Retrievers at the Edge. In *IEEE INFOCOM 2025 - IEEE Conference on Computer Communications*. 1–10.
  [doi:10.1109/INFOCOM55648.2025.11044685](https://doi.org/10.1109/INFOCOM55648.2025.11044685)
* Park et al. (2025)

  Taehwan Park, Geonho Lee, and Min-Soo Kim. 2025.
  MobileRAG: A Fast, Memory-Efficient, and Energy-Efficient Method for On-Device RAG.
  *arXiv preprint arXiv:2507.01079* (2025).
* Qualcomm (2024)

  Qualcomm. 2024.
  *Snapdragon 8 Gen 3 Mobile Platform*.

  <https://www.qualcomm.com/products/mobile/snapdragon/smartphones/snapdragon-8-series-mobile-platforms/snapdragon-8-gen-3-mobile-platform>
* Qualcomm (2025a)

  Qualcomm. 2025a.
  *QNN SDK*.

  <https://docs.qualcomm.com/bundle/publicresource/topics/80-63442-50/introduction.html>
* Qualcomm (2025b)

  Qualcomm. 2025b.
  *Snapdragon 8 Elite Platform*.

  <https://www.qualcomm.com/products/mobile/snapdragon/smartphones/snapdragon-8-series-mobile-platforms/snapdragon-8-elite-mobile-platform>
* Qwen et al. (2025)

  Qwen, :, An Yang, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chengyuan Li, Dayiheng Liu, Fei Huang, Haoran Wei, Huan Lin, Jian Yang, et al. 2025.
  Qwen2.5 Technical Report.
  *arXiv preprint arXiv:2412.15115* (2025).
* Salemi et al. (2023)

  Alireza Salemi, Sheshera Mysore, Michael Bendersky, and Hamed Zamani. 2023.
  LaMP: When Large Language Models Meet Personalization.
  *arXiv preprint arXiv:2304.11406* (2023).
* Samsung (2024)

  Samsung. 2024.
  *Samsung’s LLM on Galaxy S24*.

  <https://www.samsung.com/global/galaxy/s24/>
* Saxena (2023)

  Apoorv Saxena. 2023.
  *Prompt Lookup Decoding*.

  <https://github.com/apoorvumang/prompt-lookup-decoding/>
* Seemakhupt et al. (2024)

  Korakit Seemakhupt, Sihang Liu, and Samira Khan. 2024.
  EdgeRAG: Online-indexed rag for edge devices.
  *arXiv preprint arXiv:2412.21023* (2024).
* Smith et al. (2025)

  James Seale Smith, Chi-Heng Lin, Shikhar Tuli, Haris Jeelani, Shangqian Gao, Yilin Shen, Hongxia Jin, and Yen-Chang Hsu. 2025.
  FlexiGPT: Pruning and Extending Large Language Models with Low-Rank Weight Sharing.
  *arXiv preprint arXiv:2501.14713* (2025).
* Somasundaram et al. (2024)

  Shwetha Somasundaram, Anirudh Phukan, and Apoorv Saxena. 2024.
  PLD+: Accelerating LLM inference by leveraging Language Model Artifacts.
  *arXiv preprint arXiv:2412.01447* (2024).
* Stern et al. (2018)

  Mitchell Stern, Noam Shazeer, and Jakob Uszkoreit. 2018.
  Blockwise Parallel Decoding for Deep Autoregressive Models. In *Advances in Neural Information Processing Systems*, Vol. 31.
* Subramanian et al. (2025)

  Shreyas Subramanian, Vikram Elango, and Mecit Gungor. 2025.
  Small Language Models (SLMs) Can Still Pack a Punch: A survey.
  *arXiv preprint arXiv:2501.05465* (2025).
* Thawakar et al. (2024)

  Omkar Thawakar, Ashmal Vayani, Salman Khan, Hisham Cholakal, Rao M. Anwer, Michael Felsberg, Tim Baldwin, Eric P. Xing, and Fahad Shahbaz Khan. 2024.
  MobiLlama: Towards Accurate and Lightweight Fully Transparent GPT.
  *arXiv preprint arXiv:2402.16840* (2024).
* Touvron et al. (2023)

  Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert, Amjad Almahairi, Yasmine Babaei, Nikolay Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti Bhosale, et al. 2023.
  Llama 2: Open Foundation and Fine-Tuned Chat Models.
  *arXiv preprint arXiv:2307.09288* (2023).
* Union (2021)

  European Union. 2021.
  *General data protection regulation*.

  <https://gdpr-info.eu/>
* Venkatesha et al. (2025)

  Yeshwanth Venkatesha, Souvik Kundu, and Priyadarshini Panda. 2025.
  Fast and Cost-effective Speculative Edge-Cloud Decoding with Early Exits.
  *arXiv preprint arXiv:2505.21594* (2025).
* Wang et al. (2020)

  Wenhui Wang, Furu Wei, Li Dong, Hangbo Bao, Nan Yang, and Ming Zhou. 2020.
  MiniLM: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers.
  *arXiv preprint arXiv:2002.10957* (2020).
* Wang and Chau (2024)

  Zijie J. Wang and Duen Horng Chau. 2024.
  MeMemo: On-device Retrieval Augmentation for Private and Personalized Text Generation. In *Proceedings of the 47th International ACM SIGIR Conference on Research and Development in Information Retrieval*. 2765––2770.
  [doi:10.1145/3626772.3657662](https://doi.org/10.1145/3626772.3657662)
* Wei et al. (2025)

  Xinming Wei, Jiahao Zhang, Haoran Li, Jiayu Chen, Rui Qu, Maoliang Li, Xiang Chen, and Guojie Luo. 2025.
  Agent.xpu: Efficient Scheduling of Agentic LLM Workloads on Heterogeneous SoC.
  *arXiv preprint arXiv:2506.24045* (2025).
* Wen et al. (2024)

  Hao Wen, Yuanchun Li, Guohong Liu, Shanhui Zhao, Tao Yu, Toby Jia-Jun Li, Shiqi Jiang, Yunhao Liu, Yaqin Zhang, and Yunxin Liu. 2024.
  Autodroid: Llm-powered task automation in android. In *Proceedings of the 30th Annual International Conference on Mobile Computing and Networking*. 543–557.
* Wu et al. (2025a)

  Tong Wu, Junzhe Shen, Zixia Jia, Yuxuan Wang, and Zilong Zheng. 2025a.
  From hours to minutes: Lossless acceleration of ultra long sequence generation up to 100k tokens.
  *arXiv preprint arXiv:2502.18890* (2025).
* Wu et al. (2025b)

  Tian Wu, Liming Wang, Zijian Wen, Xiaoxi Zhang, Jingpu Duan, Xianwei Zhang, and Jinhang Zuo. 2025b.
  Accelerating Edge Inference for Distributed MoE Models with Latency-Optimized Expert Placement.
  *arXiv preprint arXiv:2508.12851* (2025).
  arXiv:2508.12851
* Xia et al. (2024)

  Heming Xia, Zhe Yang, Qingxiu Dong, Peiyi Wang, Yongqi Li, Tao Ge, Tianyu Liu, Wenjie Li, and Zhifang Sui. 2024.
  Unlocking Efficiency in Large Language Model Inference: A Comprehensive Survey of Speculative Decoding. In *Findings of the Association for Computational Linguistics ACL 2024*. 7655–7671.
  [doi:10.18653/v1/2024.findings-acl.456](https://doi.org/10.18653/v1/2024.findings-acl.456)
* Xing et al. (2024)

  Mingzhe Xing, Rongkai Zhang, Hui Xue, Qi Chen, Fan Yang, and Zhen Xiao. 2024.
  Understanding the Weakness of Large Language Model Agents within a Complex Android Environment. In *Proceedings of the 30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining*. 6061–6072.
  [doi:10.1145/3637528.3671650](https://doi.org/10.1145/3637528.3671650)
* Xu et al. (2025a)

  Daliang Xu, Wangsong Yin, Hao Zhang, Xin Jin, Ying Zhang, Shiyun Wei, Mengwei Xu, and Xuanzhe Liu. 2025a.
  EdgeLLM: Fast On-Device LLM Inference With Speculative Decoding.
  *IEEE Transactions on Mobile Computing* 24, 4 (2025), 3256–3273.
  [doi:10.1109/TMC.2024.3513457](https://doi.org/10.1109/TMC.2024.3513457)
* Xu et al. (2025b)

  Daliang Xu, Hao Zhang, Liming Yang, Ruiqi Liu, Gang Huang, Mengwei Xu, and Xuanzhe Liu. 2025b.
  Fast On-device LLM Inference with NPUs. In *Proceedings of the 30th ACM International Conference on Architectural Support for Programming Languages and Operating Systems*, Vol. 1. 445––462.
  [doi:10.1145/3669940.3707239](https://doi.org/10.1145/3669940.3707239)
* Xu et al. (2024)

  Mengwei Xu, Wangsong Yin, Dongqi Cai, Rongjie Yi, Daliang Xu, Qipeng Wang, Bingyang Wu, Yihao Zhao, Chen Yang, Shihe Wang, Qiyang Zhang, et al. 2024.
  A Survey of Resource-efficient LLM and Multimodal Foundation Models.
  *arXiv preprint arXiv:2401.08092* (2024).
* Xue et al. (2024)

  Zhenliang Xue, Yixin Song, Zeyu Mi, Xinrui Zheng, Yubin Xia, and Haibo Chen. 2024.
  Powerinfer-2: Fast large language model inference on a smartphone.
  *arXiv preprint arXiv:2406.06282* (2024).
* Yi et al. (2025)

  Rongjie Yi, Liwei Guo, Shiyun Wei, Ao Zhou, Shangguang Wang, and Mengwei Xu. 2025.
  EdgeMoE: Empowering Sparse Large Language Models on Mobile Devices.
  *IEEE Transactions on Mobile Computing* 24 (2025), 7059–7073.
  [doi:10.1109/TMC.2025.3546466](https://doi.org/10.1109/TMC.2025.3546466)
* Yin et al. (2025)

  Wangsong Yin, Daliang Xu, Mengwei Xu, Gang Huang, and Xuanzhe Liu. 2025.
  Dynamic Sparse Attention on Mobile SoCs.
  *arXiv preprint arXiv:2508.16703* (2025).
* Yu et al. (2024)

  Zhongzhi Yu, Zheng Wang, Yuhan Li, Ruijie Gao, Xiaoya Zhou, Sreenidhi Reddy Bommu, Yang (Katie) Zhao, and Yingyan (Celine) Lin. 2024.
  EDGE-LLM: Enabling Efficient Large Language Model Adaptation on Edge Devices via Unified Compression and Adaptive Layer Voting. In *Proceedings of the 61st ACM/IEEE Design Automation Conference*. Article 327.
  [doi:10.1145/3649329.3658473](https://doi.org/10.1145/3649329.3658473)
* Zhang et al. (2025)

  Yaoze Zhang, Rong Wu, Pinlong Cai, Xiaoman Wang, Guohang Yan, Song Mao, Ding Wang, and Botian Shi. 2025.
  LeanRAG: Knowledge-Graph-Based Generation with Semantic Aggregation and Hierarchical Retrieval.
  *arXiv preprint arXiv:2508.10391* (2025).

## Appendix A NP-hardness Proof of the Graph Scheduling Problem

We prove that the graph scheduling problem described in Section [3.2](https://arxiv.org/html/2510.15312v3#S3.SS2 "3.2. Progressive Graph Scheduling ‣ 3. Methodology ‣ Accelerating Mobile Language Model via Speculative Decoding and NPU-Coordinated Execution") is NP-hard via a reduction from the 2-Partition problem (Korf, [1998](https://arxiv.org/html/2510.15312v3#bib.bib29)).

Graph scheduling problem.
Given NN model blocks that sequentially execute prefill for CC chunks, each block ii must execute a prefill for every chunk and perform exactly one graph switch from G1G^{1} to G2G^{2}. Using G2G^{2} to prefill is slower than using G1G^{1}. Switches can run in parallel with the computation of other blocks, while switches / computation of different blocks cannot overlap with each other.
We aim to determine the time to switch each block with an objective to minimize the maximum of the prefill completion time and the switch completion time.

2-Partition problem.
Given a set of positive integers a1,…,ama\_{1},\dots,a\_{m} with sum S=2​BS=2B, determine whether there exists a subset I⊆{1,…,m}I\subseteq\{1,\dots,m\} such that ∑j∈Iaj=B\sum\_{j\in I}a\_{j}=B.

Construction of the scheduling instance. Given a Partition instance a1,…,ama\_{1},\dots,a\_{m}, we construct a scheduling instance as follows:

* •

  Let N=m+1N=m+1. Indices 1,…,m1,\dots,m correspond to the mm items of the Partition instance, and the block 0 (or equivalently m+1m+1) serves as a long block.
* •

  Let the number of chunks be C=2C=2.
* •

  For each j=1,…,mj=1,\dots,m (corresponding to aja\_{j}):

  + –

    Load time: sj=ajs\_{j}=a\_{j}.
  + –

    Compute time using G2G^{2}: dj=εd\_{j}=\varepsilon, where ε>0\varepsilon>0 is a very small constant.
  + –

    Compute time using G1G^{1}: pj<djp\_{j}<d\_{j}.
* •

  For the additional block 0:

  + –

    Load time s0=0s\_{0}=0.
  + –

    Compute time using G1G^{1}: p0=Bp\_{0}=B.
  + –

    Compute time using G2G^{2}: d0>p0d\_{0}>p\_{0}.
* •

  We ask whether there exists a schedule such that the overall latency TT is not larger than the prefill completion time.

Key properties.
This instance thus satisfy:

* •

  For each chunk, block 0 follows blocks 1,…,m1,\dots,m and occupies p0=Bp\_{0}=B units of prefill time. Thus, in chunk 1 and chunk 2 we obtain two disjoint windows of length BB each. Any switching placed inside one of these windows does not extend the prefill completion time. Conversely, placing a switch outside these windows delays completion beyond TT.
* •

  Since all switchings must fit within these two windows of total length 2​B2B, the only way to complete them before prefill ends is to divide them into two groups of total duration BB each. This is exactly the Partition problem.

Correctness.

* •

  (⇒\Rightarrow)
  If the Partition instance is solvable, i.e., there exists a subset II such that ∑j∈Iaj=B\sum\_{j\in I}a\_{j}=B, then in the scheduling instance we place all switchings for indices in II inside the window of chunk 1 (block 0), and place the rest in chunk 2’s window. Each window contains exactly BB switching time, all of which finish before the prefill completion time. Hence, this scheduling satisfies that the overall latency is not larger than the prefill completion time.
* •

  (⇐\Leftarrow)
  If the scheduling instance admits a feasible schedule with overall latency ≤T\leq T, then all switchings must be finished before the prefill total time TT. The only available periods where switchings can be hidden without delaying prefill are the two BB-length windows (one in each chunk at block 0). Since switchings are serialized, their total time 2​B2B must be exactly distributed across the two windows. This requires splitting the switchings into two groups summing to BB each, which directly provides a solution to the Partition instance.

  Thus, we have equivalence:

  |  |  |  |
  | --- | --- | --- |
  |  | Partition is solvable⟺Scheduling instance is solvable.\text{Partition is solvable}\;\;\Longleftrightarrow\;\;\text{Scheduling instance is solvable}. |  |

Conclusion. The reduction can be performed in polynomial time. Since Partition is NP-complete, the prefill scheduling problem is NP-hard.

Generated on Thu Oct 23 09:30:39 2025 by [LaTeXML![Mascot Sammy](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAsAAAAOCAYAAAD5YeaVAAAAAXNSR0IArs4c6QAAAAZiS0dEAP8A/wD/oL2nkwAAAAlwSFlzAAALEwAACxMBAJqcGAAAAAd0SU1FB9wKExQZLWTEaOUAAAAddEVYdENvbW1lbnQAQ3JlYXRlZCB3aXRoIFRoZSBHSU1Q72QlbgAAAdpJREFUKM9tkL+L2nAARz9fPZNCKFapUn8kyI0e4iRHSR1Kb8ng0lJw6FYHFwv2LwhOpcWxTjeUunYqOmqd6hEoRDhtDWdA8ApRYsSUCDHNt5ul13vz4w0vWCgUnnEc975arX6ORqN3VqtVZbfbTQC4uEHANM3jSqXymFI6yWazP2KxWAXAL9zCUa1Wy2tXVxheKA9YNoR8Pt+aTqe4FVVVvz05O6MBhqUIBGk8Hn8HAOVy+T+XLJfLS4ZhTiRJgqIoVBRFIoric47jPnmeB1mW/9rr9ZpSSn3Lsmir1fJZlqWlUonKsvwWwD8ymc/nXwVBeLjf7xEKhdBut9Hr9WgmkyGEkJwsy5eHG5vN5g0AKIoCAEgkEkin0wQAfN9/cXPdheu6P33fBwB4ngcAcByHJpPJl+fn54mD3Gg0NrquXxeLRQAAwzAYj8cwTZPwPH9/sVg8PXweDAauqqr2cDjEer1GJBLBZDJBs9mE4zjwfZ85lAGg2+06hmGgXq+j3+/DsixYlgVN03a9Xu8jgCNCyIegIAgx13Vfd7vdu+FweG8YRkjXdWy329+dTgeSJD3ieZ7RNO0VAXAPwDEAO5VKndi2fWrb9jWl9Esul6PZbDY9Go1OZ7PZ9z/lyuD3OozU2wAAAABJRU5ErkJggg==)](http://dlmf.nist.gov/LaTeXML/)