> Source: https://arxiv.org/html/2504.18776v2

ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning





1. [1 Introduction](https://arxiv.org/html/2504.18776v2#S1 "In ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning")
2. [2 Background & Motivation](https://arxiv.org/html/2504.18776v2#S2 "In ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning")
   1. [2.1 Failure in Microservice Systems](https://arxiv.org/html/2504.18776v2#S2.SS1 "In 2. Background & Motivation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning")
   2. [2.2 Failure Localization](https://arxiv.org/html/2504.18776v2#S2.SS2 "In 2. Background & Motivation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning")
   3. [2.3 Distributed Tracing](https://arxiv.org/html/2504.18776v2#S2.SS3 "In 2. Background & Motivation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning")
   4. [2.4 Reinforcement Fine-Tuning](https://arxiv.org/html/2504.18776v2#S2.SS4 "In 2. Background & Motivation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning")
   5. [2.5 Key Capabilities for LLM-based Failure Localization](https://arxiv.org/html/2504.18776v2#S2.SS5 "In 2. Background & Motivation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning")
      1. [(1) Tool Invocation Capability.](https://arxiv.org/html/2504.18776v2#S2.SS5.SSS0.Px1 "In 2.5. Key Capabilities for LLM-based Failure Localization ‣ 2. Background & Motivation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning")
      2. [(2) Tool Reasoning Chain Capability.](https://arxiv.org/html/2504.18776v2#S2.SS5.SSS0.Px2 "In 2.5. Key Capabilities for LLM-based Failure Localization ‣ 2. Background & Motivation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning")
3. [3 Empirical Study](https://arxiv.org/html/2504.18776v2#S3 "In ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning")
   1. [3.1 Capability of SOTA Lightweight LLMs](https://arxiv.org/html/2504.18776v2#S3.SS1 "In 3. Empirical Study ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning")
   2. [3.2 Direct Application of GRPO Algorithm](https://arxiv.org/html/2504.18776v2#S3.SS2 "In 3. Empirical Study ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning")
      1. [Training Setup.](https://arxiv.org/html/2504.18776v2#S3.SS2.SSS0.Px1 "In 3.2. Direct Application of GRPO Algorithm ‣ 3. Empirical Study ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning")
      2. [Training Dynamics.](https://arxiv.org/html/2504.18776v2#S3.SS2.SSS0.Px2 "In 3.2. Direct Application of GRPO Algorithm ‣ 3. Empirical Study ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning")
      3. [Reward Signal Limitation.](https://arxiv.org/html/2504.18776v2#S3.SS2.SSS0.Px3 "In 3.2. Direct Application of GRPO Algorithm ‣ 3. Empirical Study ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning")
      4. [Qualitative Observations.](https://arxiv.org/html/2504.18776v2#S3.SS2.SSS0.Px4 "In 3.2. Direct Application of GRPO Algorithm ‣ 3. Empirical Study ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning")
4. [4 ThinkFL](https://arxiv.org/html/2504.18776v2#S4 "In ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning")
   1. [4.1 Recursion-of-Thought Actor](https://arxiv.org/html/2504.18776v2#S4.SS1 "In 4. ThinkFL ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning")
      1. [4.1.1 Data Tools](https://arxiv.org/html/2504.18776v2#S4.SS1.SSS1 "In 4.1. Recursion-of-Thought Actor ‣ 4. ThinkFL ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning")
      2. [4.1.2 Recursion-of-Thought](https://arxiv.org/html/2504.18776v2#S4.SS1.SSS2 "In 4.1. Recursion-of-Thought Actor ‣ 4. ThinkFL ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning")
         1. [Tool Invocation Strategy.](https://arxiv.org/html/2504.18776v2#S4.SS1.SSS2.Px1 "In 4.1.2. Recursion-of-Thought ‣ 4.1. Recursion-of-Thought Actor ‣ 4. ThinkFL ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning")
         2. [Interpretability of the Reasoning Path.](https://arxiv.org/html/2504.18776v2#S4.SS1.SSS2.Px2 "In 4.1.2. Recursion-of-Thought ‣ 4.1. Recursion-of-Thought Actor ‣ 4. ThinkFL ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning")
   2. [4.2 Multi-Factor Failure Localization Grader](https://arxiv.org/html/2504.18776v2#S4.SS2 "In 4. ThinkFL ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning")
      1. [4.2.1 Recall Grader](https://arxiv.org/html/2504.18776v2#S4.SS2.SSS1 "In 4.2. Multi-Factor Failure Localization Grader ‣ 4. ThinkFL ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning")
      2. [4.2.2 Route Grader](https://arxiv.org/html/2504.18776v2#S4.SS2.SSS2 "In 4.2. Multi-Factor Failure Localization Grader ‣ 4. ThinkFL ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning")
      3. [4.2.3 Hallucination Penalty](https://arxiv.org/html/2504.18776v2#S4.SS2.SSS3 "In 4.2. Multi-Factor Failure Localization Grader ‣ 4. ThinkFL ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning")
   3. [4.3 Progressive Multi-Stage GRPO Fine-Tuning](https://arxiv.org/html/2504.18776v2#S4.SS3 "In 4. ThinkFL ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning")
      1. [4.3.1 Format-Aware Policy Priming](https://arxiv.org/html/2504.18776v2#S4.SS3.SSS1 "In 4.3. Progressive Multi-Stage GRPO Fine-Tuning ‣ 4. ThinkFL ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning")
      2. [4.3.2 Guided Exploration Augmentation](https://arxiv.org/html/2504.18776v2#S4.SS3.SSS2 "In 4.3. Progressive Multi-Stage GRPO Fine-Tuning ‣ 4. ThinkFL ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning")
      3. [4.3.3 Rank-Oriented Refinement](https://arxiv.org/html/2504.18776v2#S4.SS3.SSS3 "In 4.3. Progressive Multi-Stage GRPO Fine-Tuning ‣ 4. ThinkFL ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning")
5. [5 Evaluation](https://arxiv.org/html/2504.18776v2#S5 "In ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning")
   1. [5.1 Experimental Setup](https://arxiv.org/html/2504.18776v2#S5.SS1 "In 5. Evaluation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning")
      1. [5.1.1 Dataset](https://arxiv.org/html/2504.18776v2#S5.SS1.SSS1 "In 5.1. Experimental Setup ‣ 5. Evaluation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning")
      2. [5.1.2 Baseline Models and Approaches](https://arxiv.org/html/2504.18776v2#S5.SS1.SSS2 "In 5.1. Experimental Setup ‣ 5. Evaluation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning")
      3. [5.1.3 Evaluation Metrics](https://arxiv.org/html/2504.18776v2#S5.SS1.SSS3 "In 5.1. Experimental Setup ‣ 5. Evaluation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning")
      4. [5.1.4 Implementation and Settings](https://arxiv.org/html/2504.18776v2#S5.SS1.SSS4 "In 5.1. Experimental Setup ‣ 5. Evaluation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning")
      5. [5.1.5 Evaluation Procedure](https://arxiv.org/html/2504.18776v2#S5.SS1.SSS5 "In 5.1. Experimental Setup ‣ 5. Evaluation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning")
   2. [5.2 Overall Accuracy](https://arxiv.org/html/2504.18776v2#S5.SS2 "In 5. Evaluation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning")
   3. [5.3 Inference Time](https://arxiv.org/html/2504.18776v2#S5.SS3 "In 5. Evaluation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning")
   4. [5.4 Ablation Study](https://arxiv.org/html/2504.18776v2#S5.SS4 "In 5. Evaluation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning")
   5. [5.5 Training Process Analysis](https://arxiv.org/html/2504.18776v2#S5.SS5 "In 5. Evaluation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning")
   6. [5.6 LLM Backbone Comparison](https://arxiv.org/html/2504.18776v2#S5.SS6 "In 5. Evaluation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning")
   7. [5.7 Case Study](https://arxiv.org/html/2504.18776v2#S5.SS7 "In 5. Evaluation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning")
   8. [5.8 Hyperparameter Analysis](https://arxiv.org/html/2504.18776v2#S5.SS8 "In 5. Evaluation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning")
   9. [5.9 Generalizability Evaluation](https://arxiv.org/html/2504.18776v2#S5.SS9 "In 5. Evaluation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning")
6. [6 Discussion](https://arxiv.org/html/2504.18776v2#S6 "In ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning")
   1. [6.1 Distinction Between Research Evaluation and Practical Usage](https://arxiv.org/html/2504.18776v2#S6.SS1 "In 6. Discussion ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning")
   2. [6.2 Dependence on Microservice Characteristics and Potential Extension](https://arxiv.org/html/2504.18776v2#S6.SS2 "In 6. Discussion ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning")
   3. [6.3 Handling Context Window Limitations in Recursive Analysis](https://arxiv.org/html/2504.18776v2#S6.SS3 "In 6. Discussion ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning")
   4. [6.4 Practical Implications for SREs](https://arxiv.org/html/2504.18776v2#S6.SS4 "In 6. Discussion ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning")
   5. [6.5 Limitations and Threats to Validity](https://arxiv.org/html/2504.18776v2#S6.SS5 "In 6. Discussion ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning")
7. [7 Related Work](https://arxiv.org/html/2504.18776v2#S7 "In ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning")
   1. [7.1 Root Cause Localization](https://arxiv.org/html/2504.18776v2#S7.SS1 "In 7. Related Work ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning")
   2. [7.2 LLM-based Failure Management](https://arxiv.org/html/2504.18776v2#S7.SS2 "In 7. Related Work ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning")
8. [8 Conclusion](https://arxiv.org/html/2504.18776v2#S8 "In ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning")
9. [9 Data Availability](https://arxiv.org/html/2504.18776v2#S9 "In ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning")
10. [A Sample Output from ThinkFL](https://arxiv.org/html/2504.18776v2#A1 "In ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning")
11. [B Systematic Review Process](https://arxiv.org/html/2504.18776v2#A2 "In ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning")
    1. [B.1 Search strategy](https://arxiv.org/html/2504.18776v2#A2.SS1 "In Appendix B Systematic Review Process ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning")
    2. [B.2 Exclusion criteria](https://arxiv.org/html/2504.18776v2#A2.SS2 "In Appendix B Systematic Review Process ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning")
    3. [B.3 Overview of selected publications](https://arxiv.org/html/2504.18776v2#A2.SS3 "In Appendix B Systematic Review Process ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning")

# ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning

Lingzhe Zhang†
Peking UniversityBeijingChina
[zhang.lingzhe@stu.pku.edu.cn](mailto:zhang.lingzhe@stu.pku.edu.cn)
, 
Yunpeng Zhai†
Alibaba GroupChina
[zhaiyunpeng.zyp@alibaba-inc.com](mailto:zhaiyunpeng.zyp@alibaba-inc.com)
, 
Tong Jia∗
Peking University; National Key Laboratory of Data Space Technology and SystemBeijingChina
[jia.tong@pku.edu.cn](mailto:jia.tong@pku.edu.cn)
, 
Chiming Duan
Peking UniversityBeijingChina
[duanchiming@stu.pku.edu.cn](mailto:duanchiming@stu.pku.edu.cn)
, 
Siyu Yu
Peking UniversityBeijingChina
[gaiusyu6@gmail.com](mailto:gaiusyu6@gmail.com)
, 
Jinyang Gao
Alibaba GroupChina
[jinyang.gjy@alibaba-inc.com](mailto:jinyang.gjy@alibaba-inc.com)
, 
Bolin Ding
Alibaba GroupUnited States
[bolin.ding@alibaba-inc.com](mailto:bolin.ding@alibaba-inc.com)
, 
Zhonghai Wu
Peking UniversityBeijingChina
[wuzh@pku.edu.cn](mailto:wuzh@pku.edu.cn)
 and 
Ying Li∗
Peking UniversityBeijingChina
[li.ying@pku.edu.cn](mailto:li.ying@pku.edu.cn)

###### Abstract.

As modern microservice systems grow increasingly popular and complex—often consisting of hundreds or even thousands of interdependent components—they are becoming more susceptible to frequent and subtle failures. Ensuring system reliability therefore hinges on accurate and efficient failure localization. Traditional failure localization approaches based on small models lack the flexibility to adapt to diverse failure scenarios, while recent LLM-based methods suffer from two major limitations: they often rely on rigid invocation workflows that constrain the model’s ability to dynamically explore effective localization paths, and they require resource-intensive inference, making them cost-prohibitive for real-world deployment. To address these challenges, we explore the use of reinforcement fine-tuning to equip lightweight LLMs with reasoning and self-refinement capabilities, significantly improving the cost-effectiveness and adaptability of LLM-based failure localization. We begin with an empirical study to identify three key capabilities essential for accurate localization. Building on these insights, we propose a progressive multi-stage GRPO fine-tuning framework, which integrates a multi-factor failure localization grader and a recursion-of-thought actor module. The resulting model, ThinkFL, not only outperforms existing state-of-the-art LLMs and baseline methods in localization accuracy but also reduces end-to-end localization latency from minutes to seconds, demonstrating strong potential for real-world applications.

Failure Localization, Trace, Large Language Model, Reinforcement Fine-Tuning

†Equal contribution

∗Corresponding author

††journal: TOSEM††journalyear: 2026††journalvolume: 1††journalnumber: 1††publicationmonth: 1††doi: 10.1145/3789262††ccs: Software and its engineering Maintaining software

## 1. Introduction

Modern microservice architectures have grown increasingly intricate due to evolving runtime conditions and complex inter-service interactions (Zhang et al., [2025a](https://arxiv.org/html/2504.18776v2#bib.bib17 "A survey of aiops in the era of large language models")). These systems typically comprise hundreds or even thousands of tightly coupled subsystems, where a fault in any single component can cascade into system-wide performance degradations (Waseem et al., [2021](https://arxiv.org/html/2504.18776v2#bib.bib1 "Design, monitoring, and testing of microservices systems: the practitioners’ perspective")). Consequently, timely and accurate identification of the underlying cause of such failures is essential to maintaining overall system reliability (Xu et al., [2025](https://arxiv.org/html/2504.18776v2#bib.bib121 "OpenRCA: can large language models locate the root cause of software failures?"); Wang et al., [2024a](https://arxiv.org/html/2504.18776v2#bib.bib120 "MRCA: metric-level root cause analysis for microservices via multi-modal data")).

Nevertheless, pinpointing the exact root cause remains a formidable challenge due to the complex interdependencies among subsystems (Sun et al., [2025](https://arxiv.org/html/2504.18776v2#bib.bib45 "Interpretable failure localization for microservice systems based on graph autoencoder")). Each request typically triggers an elaborate chain of invocations that spans multiple components—ranging from services and service instances to physical hosts—and encompasses various interactions, such as Application Programming Interface (API) calls, database queries, and other inter-component communications. The inherent dynamism and heterogeneity of these interactions render the task of isolating the true root cause both complex and non-trivial.

To enable root cause localization, extensive research has been conducted in this area. Many studies have leveraged machine learning and deep learning models to address this challenge. Microscope (Lin et al., [2018](https://arxiv.org/html/2504.18776v2#bib.bib3 "Microscope: pinpoint performance issues with causal graphs in micro-service environments")) constructs causality graphs and employs a depth-first search strategy to detect front-end anomalies. CIRCA (Li et al., [2022b](https://arxiv.org/html/2504.18776v2#bib.bib2 "Causal inference-based root cause analysis for online service systems with intervention recognition")) builds a causal Bayesian network using regression-based hypothesis testing and descendant adjustment to infer faulty components. RUN (Lin et al., [2024](https://arxiv.org/html/2504.18776v2#bib.bib8 "Root cause analysis in microservice using neural granger causal discovery")) integrates time series forecasting with neural Granger causal discovery and a personalized PageRank algorithm to efficiently recommend the top-k root causes. MicroRank (Yu et al., [2021](https://arxiv.org/html/2504.18776v2#bib.bib6 "Microrank: end-to-end latency issue localization with extended spectrum analysis in microservice environments")) constructs a trace coverage tree to capture dependencies between requests and service instances, applying the PageRank algorithm to rank potential root causes. TraceRank (Yu et al., [2023b](https://arxiv.org/html/2504.18776v2#bib.bib5 "TraceRank: abnormal service localization with dis-aggregated end-to-end tracing data in cloud native systems")) combines spectrum analysis with a PageRank-based random walk to pinpoint abnormal services. CRISP (Zhang et al., [2022](https://arxiv.org/html/2504.18776v2#bib.bib7 "{crisp}: Critical path analysis of {large-scale} microservice architectures")) performs critical path analysis to drill down into latency issues, while TraceConstract (Zhang et al., [2024a](https://arxiv.org/html/2504.18776v2#bib.bib4 "Trace-based multi-dimensional root cause localization of performance issues in microservice systems")) employs sequence representations, contrast sequential pattern mining, and spectrum analysis to efficiently localize multi-dimensional root causes.

However, these approaches rely on predefined service causal graphs, fixed statistical models of fault-symptom relationships, or learned associations from training data, fundamentally operating as static, one-time analyses. Furthermore, deep learning-based methods often struggle to provide interpretable reasoning paths, which are crucial for Site Reliability Engineers (SREs) to validate diagnoses and implement effective resolutions (Beyer et al., [2018](https://arxiv.org/html/2504.18776v2#bib.bib126 "The site reliability workbook: practical ways to implement sre"); Yao et al., [2024](https://arxiv.org/html/2504.18776v2#bib.bib127 "Chain-of-event: interpretable root cause analysis for microservices through automatically learning weighted event causal graph"); Yu et al., [2023a](https://arxiv.org/html/2504.18776v2#bib.bib128 "Nezha: interpretable fine-grained root causes analysis for microservices on multi-modal observability data"); Zhang et al., [2025b](https://arxiv.org/html/2504.18776v2#bib.bib133 "Adaptive root cause localization for microservice systems with multi-agent recursion-of-thought")). Fortunately, large language models (LLMs) offer promising solutions to these challenges, leading to the emergence of LLM-based approaches. For instance, mABC (Zhang et al., [2024e](https://arxiv.org/html/2504.18776v2#bib.bib24 "MABC: multi-agent blockchain-inspired collaboration for root cause analysis in micro-services architecture")) introduces a multi-agent, blockchain-inspired collaboration framework, where multiple LLM-based agents follow a structured workflow and coordinate via blockchain-inspired voting mechanisms. RCAgent (Wang et al., [2024b](https://arxiv.org/html/2504.18776v2#bib.bib44 "Rcagent: cloud root cause analysis by autonomous agents with tool-augmented large language models")) utilizes a tool-augmented LLM framework that incorporates log and code data to perform root cause analysis tasks, such as predicting root causes, identifying solutions, gathering evidence, and determining responsibilities.

Although these LLM-based methods have significantly advanced failure localization, several challenges remain in practical deployment:

* •

  Rigid Invocation Workflows. Current LLM-based approaches typically rely on fixed invocation workflows—for instance, multi-agent frameworks use a set of pre-defined agents that are called in a predetermined sequence (Zhang et al., [2024e](https://arxiv.org/html/2504.18776v2#bib.bib24 "MABC: multi-agent blockchain-inspired collaboration for root cause analysis in micro-services architecture"); Wang et al., [2024b](https://arxiv.org/html/2504.18776v2#bib.bib44 "Rcagent: cloud root cause analysis by autonomous agents with tool-augmented large language models"); Pei et al., [2025](https://arxiv.org/html/2504.18776v2#bib.bib100 "Flow-of-action: sop enhanced llm-based multi-agent system for root cause analysis"); Li et al., [2025b](https://arxiv.org/html/2504.18776v2#bib.bib101 "COCA: generative root cause analysis for distributed systems with code knowledge"); Wang et al., [2025](https://arxiv.org/html/2504.18776v2#bib.bib102 "TAMO: fine-grained root cause analysis via tool-assisted llm agent with multi-modality observation data in cloud-native systems"); Ren, [2025](https://arxiv.org/html/2504.18776v2#bib.bib104 "The multi-agent fault localization system based on monte carlo tree search approach")). For example, mABC (Zhang et al., [2024e](https://arxiv.org/html/2504.18776v2#bib.bib24 "MABC: multi-agent blockchain-inspired collaboration for root cause analysis in micro-services architecture")) adopts a staged multi-agent pipeline in which alerts flow through predefined roles in order—Alert Receiver (A1) →\rightarrow Process Scheduler (A2) →\rightarrow Data Detective (A3) / Dependency Explorer (A4) / Probability Oracle (A5) / Fault Mapper (A6) →\rightarrow Solution Engineer (A7)—with each agent bound to a specific diagnostic subtask. Similarly, Flow-of-Action (Pei et al., [2025](https://arxiv.org/html/2504.18776v2#bib.bib100 "Flow-of-action: sop enhanced llm-based multi-agent system for root cause analysis")) constrains the agent’s behavior using Standard Operating Procedures (SOPs): the model must follow an SOP-guided sequence of actions. This inflexibility limits the LLM’s ability to dynamically explore and determine the correct failure localization path under varying conditions.
* •

  Resource-Intensive Inference. The models employed in these approaches are generally ultra-large (with parameter counts ≥\geq 70 billion or more) or are closed-source, which restricts their practicality in terms of inference speed and computational cost. For instance, mABC (Zhang et al., [2024e](https://arxiv.org/html/2504.18776v2#bib.bib24 "MABC: multi-agent blockchain-inspired collaboration for root cause analysis in micro-services architecture")), Flow-of-Action (Pei et al., [2025](https://arxiv.org/html/2504.18776v2#bib.bib100 "Flow-of-action: sop enhanced llm-based multi-agent system for root cause analysis")), and TAMO (Wang et al., [2025](https://arxiv.org/html/2504.18776v2#bib.bib102 "TAMO: fine-grained root cause analysis via tool-assisted llm agent with multi-modality observation data in cloud-native systems")) report their strongest performance only when powered by closed-source frontier models such as GPT-4-Turbo. Likewise, COCA (Li et al., [2025b](https://arxiv.org/html/2504.18776v2#bib.bib101 "COCA: generative root cause analysis for distributed systems with code knowledge")) relies on GPT-3.5, GPT-4o, Llama-3.1-405B, Gemini-1.5-Pro, and Claude-3.5-Sonnet to achieve competitive results. More recently, KnowledgeMind (Ren, [2025](https://arxiv.org/html/2504.18776v2#bib.bib104 "The multi-agent fault localization system based on monte carlo tree search approach")) demonstrates the need for ultra-large open-source models (e.g., LLaMA-3.3-70B, Qwen-QwQ) or GPT-4-Turbo to realize its full potential. While such settings yield strong benchmarks, they highlight a critical challenge: in real-world failure localization scenarios, even a mature small-scale microservice system (with fewer than 10 nodes) may encounter issues every few minutes, making rapid and cost-effective problem resolution essential to minimize impact and loss.

Recognizing these limitations, we require a model that is both computationally efficient and capable of flexible, autonomous invocation. To address the first requirement, we leverage lightweight LLMs, which reduce deployment and inference costs while providing general-purpose semantic understanding that can be further specialized (Dubey et al., [2024](https://arxiv.org/html/2504.18776v2#bib.bib118 "The llama 3 herd of models"); Yang et al., [2025a](https://arxiv.org/html/2504.18776v2#bib.bib119 "Qwen3 technical report")). To achieve flexible and autonomous invocation, the model must be able to self-explore multi-step diagnostic paths and optimize action selection. Reinforcement fine-tuning provides a principled mechanism for this: it enables the model to learn policies that select the effective sequence of actions based on feedback (Rafailov et al., [2023](https://arxiv.org/html/2504.18776v2#bib.bib75 "Direct preference optimization: your language model is secretly a reward model"); Schulman et al., [2017](https://arxiv.org/html/2504.18776v2#bib.bib76 "Proximal policy optimization algorithms"); Shao et al., [2024](https://arxiv.org/html/2504.18776v2#bib.bib77 "Deepseekmath: pushing the limits of mathematical reasoning in open language models")). Therefore, employing reinforcement fine-tuning to adapt lightweight LLMs (with parameter counts <\textless 10 billion) naturally addresses both constraints, allowing the model to iteratively explore effective failure localization pathways while avoiding the limitations of rigid invocation workflows and resource-intensive inference.

Based on this idea, we first conduct an empirical study to explore how to equip lightweight LLMs with failure localization capabilities. Our study identifies three core capabilities essential for effective failure localization: (i) a high dependence on standardized tool invocation, (ii) the need for exploratory behavior under standardized tool usage, and (iii) an integrated reward mechanism that accounts for both the reasoning process and the final output.

Based on our empirical study findings, we introduce ThinkFL, a self-refining failure localization model for microservice systems developed via reinforcement fine-tuning. ThinkFL leverages a Recursion-of-Thought Actor that integrates multiple data tools—combining trace analysis and metrics evaluation—to iteratively generate a ranked list of potential root causes along with a fully interpretable inference path. This actor output is then validated by expert SREs and further refined using a Multi-Factor Failure Localization Grader, which merges the model’s predictions with ground-truth feedback to compute a comprehensive score.

The entire fine-tuning process is driven by our Progressive Multi-Stage Group Relative Policy Optimization (GRPO) Fine-Tuning approach, which comprises three distinct stages: a format-aware policy priming stage to ensure the model reliably invokes tools in a standardized manner, a guided exploration augmentation stage to enhance the model’s capacity for extensive exploratory search, and a rank-oriented refinement stage to improve the final ranking and accuracy of the identified root cause.

Our experiments demonstrate that ThinkFL not only significantly outperforms existing large-scale LLMs in failure localization but also surpasses state-of-the-art root cause localization methods. In addition, ThinkFL achieves over 10× faster inference speed compared to these large models. By applying the ThinkFL training methodology to fine-tune various lightweight LLMs, we further validate the effectiveness and generalizability of our reinforcement learning approach. In summary, the key contributions of this work are as follows:

* •

  We conduct a comprehensive study to explore how lightweight LLMs can be endowed with failure localization capabilities. Our study identifies three core capabilities essential for effective LLM-based failure localization.
* •

  Drawing inspiration from these insights, we propose ThinkFL, a self-refining failure localization model for microservice systems, achieved through reinforcement fine-tuning. ThinkFL introduces a novel progressive multi-stage GRPO fine-tuning approach, addressing the challenges identified in our empirical study while minimizing inference cost and iteratively exploring effective failure localization pathway.
* •

  We evaluate ThinkFL on six diverse datasets, demonstrating its superior performance. Experimental results reveal that ThinkFL achieves both higher accuracy and faster inference speed compared to large-scale baseline models and state-of-the-art failure localization methods.

## 2. Background & Motivation

This section outlines the essential background underpinning our approach, including what is a failure in microservice systems, a formal description of the failure localization (FL) problem, the role of distributed tracing as a core data modality in system observability, and the emerging use of reinforcement fine-tuning (RFT) to enhance the reasoning and adaptability of LLMs.

### 2.1. Failure in Microservice Systems

In large-scale microservice systems, failures typically manifest as abnormal behaviors observable at the request or application layer. For example, a user request may experience significantly increased latency, return an unexpected error code, or fail to complete altogether. At the system level, such failures are reflected in observability signals, including anomalous spikes in service metrics (e.g., error rates, CPU usage, or memory consumption), suspicious log patterns (e.g., repeated timeout errors), or incomplete traces where downstream calls do not return. These symptoms provide indirect evidence of the underlying faulty component but rarely reveal the exact root cause directly.

Specifically, in this work, a *failure* is defined as an abnormal episode detectable from request-level observations within a short time window (typically one minute). An episode is triggered when any of the following request-observable signals cross predefined thresholds:

* •

  Correctness/availability: a surge in HTTP 5​x​x5xx error rate, request timeout rate, or sudden unavailability of a service;
* •

  Performance: tail-latency (e.g., p​95/p​99p95/p99) exceeding the SLO budget, or throughput dropping sharply under steady load.

We note that resource saturation metrics (e.g., CPU, memory, GC pauses, I/O wait, or connection pool exhaustion) are excluded as primary failure categories because they are not directly observable from request-level signals. Instead, their impact typically manifests as correctness or performance degradations, which are captured by the above observables.

These conditions are reflected in observability signals—metrics, logs, and distributed traces—and grouped into a single failure *episode* by temporal proximity and correlation.

We focus on application-layer *correctness* and *performance* failures in microservice systems, explicitly excluding security incidents, user-intent/query-quality issues, front-end-only rendering glitches, and source-level bug localization. Our target is *component-level* localization, identifying faulty entities such as services, pods, or hosts.

### 2.2. Failure Localization

Failure localization is a central problem in system failure diagnosis, aiming to identify the specific component—such as a microservice, process, or host—responsible for abnormal behavior. It is often considered the second stage of failure diagnosis, following coarse-grained failure category classification (e.g., identifying a CPU overload versus a network delay). Accurate localization is essential for reducing system recovery time and minimizing service disruption.

In this work, we define the *root cause* as the system component directly responsible for the observed failure, with granularity at multiple levels: service, pod, and node. At the service level, the root cause corresponds to the microservice exhibiting the abnormal behavior, such as CheckoutService. At the pod level, the root cause can be a specific instance of a service (e.g., checkoutservice-0) that is malfunctioning. At the node level, the root cause is the physical or virtual machine (e.g., node-0) hosting the affected components.

For each failure episode, the root cause occurs at exactly one of these levels. Precise identification at the correct level allows operators to apply targeted remediation strategies. For example, if a request experiences abnormal latency due to checkoutservice-0 being overloaded, the pod checkoutservice-0 is the root cause. The service CheckoutService and underlying node node-0 may exhibit symptoms, but the actual root cause is at the pod level.

|  |  |  |  |
| --- | --- | --- | --- |
| (1) |  | C∗=arg⁡maxC∈𝒞⁡s​(C,R)C^{\*}=\arg\max\_{C\in\mathcal{C}}s(C,R) |  |

Formally, let R={r1,r2,…,rn}R=\{r\_{1},r\_{2},\dots,r\_{n}\} denote the set of abnormal requests observed within a diagnostic window, and let 𝒞\mathcal{C} represent the set of candidate components potentially responsible for these anomalies. The objective of failure localization is to identify the component C∗C^{\*} as defined in Equation [1](https://arxiv.org/html/2504.18776v2#S2.E1 "Equation 1 ‣ 2.2. Failure Localization ‣ 2. Background & Motivation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"), where s​(C,R)s(C,R) is a scoring function that quantifies the likelihood of CC being the root cause based on the observed request-level anomalies in RR.

### 2.3. Distributed Tracing

Distributed tracing provides end-to-end visibility into request execution across components of a distributed system. It is widely adopted in industry-standard observability stacks (e.g., OpenTelemetry, Jaeger, Zipkin) and has become a foundational data source for latency analysis, root cause diagnosis, and performance optimization.

Each trace records the lifecycle of a single request, capturing all the services and operations involved. A trace is composed of multiple spans, each representing a specific operation such as a database query or RPC invocation. Spans contain structured fields including start/end timestamps, service and operation names, status codes, and a parent\_span identifier, from which parent–child relationships and execution dependencies can be inferred at the trace level.

![Refer to caption](x1.png)


Figure 1. Example of a distributed trace with multiple spans

As shown in Figure [1](https://arxiv.org/html/2504.18776v2#S2.F1 "Figure 1 ‣ 2.3. Distributed Tracing ‣ 2. Background & Motivation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"), a complete trace reconstructs the execution graph of a request. This graph encodes both the control flow and performance dynamics, making it a rich source of context for understanding how and where delays or failures propagate. Entry spans—typically the first span initiated by a frontend or gateway service—are used to determine the health status of the entire request. In our work, we treat a trace as anomalous if (i) the latency of its entry span exceeds 100× the average latency under normal conditions, indicating a performance failure, or (ii) the entry span reports a non-OK status (e.g., non-200/0 codes), indicating a correctness failure. For such anomalous requests—whether caused by performance degradation or correctness violations—localizing the root cause among the many involved services remains a non-trivial but critical task.

### 2.4. Reinforcement Fine-Tuning

Reinforcement Fine-Tuning (RFT) is a paradigm that leverages reinforcement learning (RL) to adapt large language models to complex decision-making tasks in a reward-driven manner (Christiano et al., [2017](https://arxiv.org/html/2504.18776v2#bib.bib129 "Deep reinforcement learning from human preferences"); Ziegler et al., [2019](https://arxiv.org/html/2504.18776v2#bib.bib130 "Fine-tuning language models from human preferences")). This approach enables the fine-tuning of models using reinforcement learning techniques to enhance their performance on specialized tasks with minimal training data.

Unlike supervised fine-tuning (SFT), which requires high-quality labeled data and learns via direct instruction, RFT allows models to explore action spaces and learn from reward signals, enabling adaptation in settings where ground truth annotations are scarce or ambiguous. This makes RFT particularly suitable for tasks such as code generation, multi-step reasoning, and tool-use planning.

A number of core algorithms underpin modern RFT strategies. Direct Preference Optimization (DPO) (Rafailov et al., [2023](https://arxiv.org/html/2504.18776v2#bib.bib75 "Direct preference optimization: your language model is secretly a reward model")) simplifies the traditional reward model plus Proximal Policy Optimization (PPO) pipeline by directly optimizing preference-based objectives. PPO (Schulman et al., [2017](https://arxiv.org/html/2504.18776v2#bib.bib76 "Proximal policy optimization algorithms")) remains widely used due to its stability in continuous action spaces. Group Relative Policy Optimization (GRPO) (Shao et al., [2024](https://arxiv.org/html/2504.18776v2#bib.bib77 "Deepseekmath: pushing the limits of mathematical reasoning in open language models")) extends PPO by introducing group-based policy updates, allowing for more robust modeling of action diversity.

Next, we briefly introduce the principles of GRPO, which we later extend in our work. GRPO operates over groups of completions, capturing the relative preference structure within each group.

Formally, let 𝒢={(a1,…,ak)}\mathcal{G}=\{(a\_{1},\dots,a\_{k})\} represent a group of kk sampled completions under the same prompt xx, and let πθ\pi\_{\theta} denote the policy parameterized by θ\theta. GRPO seeks to maximize the group-based expected log-likelihood weighted by soft preferences, as shown in Equation [2](https://arxiv.org/html/2504.18776v2#S2.E2 "Equation 2 ‣ 2.4. Reinforcement Fine-Tuning ‣ 2. Background & Motivation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").

|  |  |  |  |
| --- | --- | --- | --- |
| (2) |  | ℒGRPO=𝔼𝒢∼πθ​[∑i=1kwi​log⁡πθ​(ai|x)]\mathcal{L}\_{\text{GRPO}}=\mathbb{E}\_{\mathcal{G}\sim\pi\_{\theta}}\left[\sum\_{i=1}^{k}w\_{i}\log\pi\_{\theta}(a\_{i}|x)\right] |  |

Among them, the weights wiw\_{i} encode the relative preference (or ranking) among completions within the group. These weights are typically computed using a softmax function over reward scores R​(ai)R(a\_{i}), as shown in Equation [3](https://arxiv.org/html/2504.18776v2#S2.E3 "Equation 3 ‣ 2.4. Reinforcement Fine-Tuning ‣ 2. Background & Motivation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"), where β\beta is a temperature parameter that controls the sharpness of preference.

|  |  |  |  |
| --- | --- | --- | --- |
| (3) |  | wi=exp⁡(β​R​(ai))∑j=1kexp⁡(β​R​(aj))w\_{i}=\frac{\exp(\beta R(a\_{i}))}{\sum\_{j=1}^{k}\exp(\beta R(a\_{j}))} |  |

In contrast to PPO’s per-sample KL divergence constraint, GRPO applies a group-wise trust region constraint to regulate policy updates, as described in Equation [4](https://arxiv.org/html/2504.18776v2#S2.E4 "Equation 4 ‣ 2.4. Reinforcement Fine-Tuning ‣ 2. Background & Motivation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").

|  |  |  |  |
| --- | --- | --- | --- |
| (4) |  | KL​(πθgroup∥πoldgroup)≤δ\text{KL}(\pi\_{\theta}^{\text{group}}\parallel\pi\_{\text{old}}^{\text{group}})\leq\delta |  |

This formulation enables more stable and expressive updates by leveraging the relative quality of multiple completions simultaneously, rather than relying on isolated samples. As a result, GRPO is particularly well-suited for tasks involving structured reasoning, where maintaining diversity and avoiding premature convergence to suboptimal outputs is critical.

Recent work has already extended these foundational algorithms to address domain-specific challenges. Token-level DPO (TDPO) (Zeng et al., [2024](https://arxiv.org/html/2504.18776v2#bib.bib81 "Token-level direct preference optimization")) introduces token-wise feedback granularity to better align model generation with human intent. Offset-DPO (ODPO) (Amini et al., [2024](https://arxiv.org/html/2504.18776v2#bib.bib82 "Direct preference optimization with an offset")) improves training efficiency by assigning non-uniform weights to preference pairs. Completion Pruning PPO (CPPO) (Lin et al., [2025](https://arxiv.org/html/2504.18776v2#bib.bib78 "Cppo: accelerating the training of group relative policy optimization-based reasoning models")) accelerates reasoning tasks by selectively pruning low-quality completions during optimization. Hybrid GRPO (Sane, [2025](https://arxiv.org/html/2504.18776v2#bib.bib79 "Hybrid group relative policy optimization: a multi-sample approach to enhancing policy optimization")) fuses empirical sampling with value-function stability. Adaptive GRPO (AGPO) (Li et al., [2025a](https://arxiv.org/html/2504.18776v2#bib.bib80 "Adaptive group policy optimization: towards stable training and token-efficient reasoning")) mitigates variance and overthinking issues by modifying advantage estimation and applying length-sensitive reward shaping.

Despite these advances, RFT has not been widely explored in LLM-based observability tasks such as failure localization, where reasoning across complex traces and dynamic dependencies is essential. This motivates our investigation into leveraging RFT to enhance the reasoning ability of lightweight LLMs in practical system diagnosis settings.

### 2.5. Key Capabilities for LLM-based Failure Localization

Large-scale distributed systems generate massive volumes of heterogeneous telemetry data—metrics, traces, and logs—especially during failure episodes. As illustrated in Figure [2](https://arxiv.org/html/2504.18776v2#S2.F2 "Figure 2 ‣ 2.5. Key Capabilities for LLM-based Failure Localization ‣ 2. Background & Motivation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"), even a single minute of system activity may produce over 18,000 telemetry lines and more than 3.8 million characters. Such scale far exceeds the context limits of modern LLMs, making direct ingestion of raw observations infeasible.

![Refer to caption](x2.png)

(a) Lines Count

![Refer to caption](x3.png)

(b) Characters Count

Figure 2. Data Source Quantity Within 1-Minute Window

To understand how existing LLM-based failure localization systems cope with this challenge. We gathered relevant papers by searching for work related to LLMs and system-level failure diagnosis, and by following references from closely related studies—including recent surveys on LLM-based automated program repair (Yang et al., [2025b](https://arxiv.org/html/2504.18776v2#bib.bib125 "A survey of llm-based automated program repair: taxonomies, design paradigms, and applications")). We closely examined representative methods, as illustrated in Table [1](https://arxiv.org/html/2504.18776v2#S2.T1 "Table 1 ‣ 2.5. Key Capabilities for LLM-based Failure Localization ‣ 2. Background & Motivation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"). These systems span microservice failure diagnosis, production incident analysis, and multi-modality RCA pipelines. While differing in design, they share a common pattern: each augments the LLM with domain-specific tools that preprocess, filter, or reconstruct relevant context prior to reasoning. For example, mABC (Zhang et al., [2024e](https://arxiv.org/html/2504.18776v2#bib.bib24 "MABC: multi-agent blockchain-inspired collaboration for root cause analysis in micro-services architecture")) integrates a dependency query engine and metric explorer to surface suspicious services; RCAgent (Wang et al., [2024b](https://arxiv.org/html/2504.18776v2#bib.bib44 "Rcagent: cloud root cause analysis by autonomous agents with tool-augmented large language models")) invokes log and trace analysis tools to construct structured evidence; Flow-of-Action (Pei et al., [2025](https://arxiv.org/html/2504.18776v2#bib.bib100 "Flow-of-action: sop enhanced llm-based multi-agent system for root cause analysis")) coordinates multiple tools under an SOP-style workflow; COCA (Li et al., [2025b](https://arxiv.org/html/2504.18776v2#bib.bib101 "COCA: generative root cause analysis for distributed systems with code knowledge")) extracts code snippets and execution paths; TAMO (Wang et al., [2025](https://arxiv.org/html/2504.18776v2#bib.bib102 "TAMO: fine-grained root cause analysis via tool-assisted llm agent with multi-modality observation data in cloud-native systems")) aligns multi-modal observations; and KnowledgeMind (Ren, [2025](https://arxiv.org/html/2504.18776v2#bib.bib104 "The multi-agent fault localization system based on monte carlo tree search approach")) pairs metric/log/trace tools with Monte Carlo Tree Search for guided exploration.

Table 1. Summary of representative LLM-based failure localization methods and selected key tools. The table does not include all tools used in each paper, but highlights those that are particularly important.

|  |  |
| --- | --- |
| Paper | Main Tools Used |
| mABC (Zhang et al., [2024e](https://arxiv.org/html/2504.18776v2#bib.bib24 "MABC: multi-agent blockchain-inspired collaboration for root cause analysis in micro-services architecture")) | Dependency Query Tool: Identifies service dependencies to narrow the search space.  Metric Tool: Retrieves key metrics for suspicious services. |
| RCAgent (Wang et al., [2024b](https://arxiv.org/html/2504.18776v2#bib.bib44 "Rcagent: cloud root cause analysis by autonomous agents with tool-augmented large language models")) | Log Analysis Tool: Segments long logs and performs RAG-based extraction of evidence for reliable reasoning. |
| Flow-of-Action (Pei et al., [2025](https://arxiv.org/html/2504.18776v2#bib.bib100 "Flow-of-action: sop enhanced llm-based multi-agent system for root cause analysis")) | Multimodal Data Collection Tool: Gathers and textualizes metrics, traces, and logs to highlight abnormal signals.  SOP Flow Tools: Structures tool invocation through SOP-guided diagnostic workflows. |
| COCA (Li et al., [2025b](https://arxiv.org/html/2504.18776v2#bib.bib101 "COCA: generative root cause analysis for distributed systems with code knowledge")) | Code Snippet Extractor: Locates relevant code regions by log messages.  Execution Path Reconstructor: Rebuilds execution paths leading to the failure to supply actionable context. |
| TAMO (Wang et al., [2025](https://arxiv.org/html/2504.18776v2#bib.bib102 "TAMO: fine-grained root cause analysis via tool-assisted llm agent with multi-modality observation data in cloud-native systems")) | Multi-modality Alignment Tool: Aligns diverse telemetry into a unified, time-consistent representation.  Failure Localization Tool: Models causal propagation patterns to pinpoint the fault source.  Fault Type Classifier: Detects failure patterns using a causal graph. |
| KnowledgeMind (Ren, [2025](https://arxiv.org/html/2504.18776v2#bib.bib104 "The multi-agent fault localization system based on monte carlo tree search approach")) | Metric Tool: Detects anomalies in time-series metrics.  Log Tool: Filters and extracts salient log details.  Trace Tool: Examines service-call latencies and communications. |

These observations reveal that the core challenge is not merely having tools, but enabling the LLM to use them effectively. Across the representative works, two capabilities consistently emerge as fundamental to successful diagnosis:

##### (1) Tool Invocation Capability.

The LLM must determine *which* tool to call and *how* to parameterize it in order to distill high-relevance context from massive telemetry streams. Existing systems rely on a variety of such tools—including dependency analyzers, log summarizers, metric explorers, trace analyzers, and multi-modality preprocessors (Table [1](https://arxiv.org/html/2504.18776v2#S2.T1 "Table 1 ‣ 2.5. Key Capabilities for LLM-based Failure Localization ‣ 2. Background & Motivation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning")). The LLM therefore plays an active role in orchestrating data reduction by selecting and chaining appropriate tools.

##### (2) Tool Reasoning Chain Capability.

Failure localization rarely succeeds in a single step; evidence must be gathered iteratively. Modern systems thus couple LLM reasoning with multi-hop tool interactions. Examples include ReAct-style iterative querying (mABC (Zhang et al., [2024e](https://arxiv.org/html/2504.18776v2#bib.bib24 "MABC: multi-agent blockchain-inspired collaboration for root cause analysis in micro-services architecture")) , Flow-of-Action (Pei et al., [2025](https://arxiv.org/html/2504.18776v2#bib.bib100 "Flow-of-action: sop enhanced llm-based multi-agent system for root cause analysis"))), self-consistency aggregation (RCAgent (Wang et al., [2024b](https://arxiv.org/html/2504.18776v2#bib.bib44 "Rcagent: cloud root cause analysis by autonomous agents with tool-augmented large language models"))), evidence reconstruction pipelines (COCA (Li et al., [2025b](https://arxiv.org/html/2504.18776v2#bib.bib101 "COCA: generative root cause analysis for distributed systems with code knowledge"))), cross-tool coordination (TAMO (Wang et al., [2025](https://arxiv.org/html/2504.18776v2#bib.bib102 "TAMO: fine-grained root cause analysis via tool-assisted llm agent with multi-modality observation data in cloud-native systems"))), and search-based planning (KnowledgeMind (Ren, [2025](https://arxiv.org/html/2504.18776v2#bib.bib104 "The multi-agent fault localization system based on monte carlo tree search approach"))). In all cases, the LLM must refine hypotheses, resolve contradictions, and issue new tool calls based on previously retrieved information.

Summary. The fundamental difficulty in LLM-based failure localization is not only the sheer volume of telemetry data, but the need for the LLM to orchestrate tools in a multi-step reasoning process. Existing representative methods all embody two essential capabilities: (i) invoking the right tools to distill relevant context, and (ii) forming multi-hop reasoning chains that progressively narrow down the root cause.

## 3. Empirical Study

In this section, we empirically examine whether lightweight LLMs possess the capabilities required for failure localization (as discussed in Section [2.5](https://arxiv.org/html/2504.18776v2#S2.SS5 "2.5. Key Capabilities for LLM-based Failure Localization ‣ 2. Background & Motivation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning")), and whether these capabilities can be enhanced through GRPO-based training. Our investigation is guided by the following research questions:

* •

  RQ1: Do state-of-the-art lightweight LLMs naturally possess the required capabilities?
* •

  RQ2: Can existing GRPO algorithms enhance these capabilities and improve failure localization performance?

### 3.1. Capability of SOTA Lightweight LLMs

Lightweight LLMs are appealing for failure localization because they are inexpensive and can be deployed efficiently in both edge and cloud environments. However, prior work has consistently shown that such models exhibit fundamental limitations in reasoning and planning (Wu et al., [2025](https://arxiv.org/html/2504.18776v2#bib.bib112 "Inference scaling laws: an empirical analysis of compute-optimal inference for llm problem-solving"); Zhou et al., [2025](https://arxiv.org/html/2504.18776v2#bib.bib113 "LightPlanner: unleashing the reasoning capabilities of lightweight large language models in task planning"); Feng et al., [2025](https://arxiv.org/html/2504.18776v2#bib.bib114 "Efficient reasoning models: a survey")). While most lightweight models—including very small ones such as LLaMA-3.2-3B—can readily acquire tool-invocation syntax through simple function-call fine-tuning (Yuan et al., [2025](https://arxiv.org/html/2504.18776v2#bib.bib115 "EASYTOOL: enhancing llm-based agents with concise tool instruction"); Shen, [2024](https://arxiv.org/html/2504.18776v2#bib.bib116 "Llm with tools: a survey"); YifeiLu et al., [2025](https://arxiv.org/html/2504.18776v2#bib.bib117 "CodeTool: enhancing programmatic tool invocation of llms via process supervision")), syntactic correctness alone does not guarantee effective failure localization. In practice, success depends on whether the model can integrate heterogeneous tool outputs into a coherent, multi-step reasoning process.

To quantify the impact of reasoning capability, we compare lightweight LLMs against a stronger model with demonstrably superior reasoning skills. We reproduced two representative failure-localization methods, mABC and RCAgent, both implemented using LLaMA-3.2-3B as the backbone, and evaluated them on the AIOPS 2022 dataset (subdataset 2022-03-20-cloudbed3). These two methods were chosen because they represent the dominant paradigms in LLM-based system diagnosis: mABC relies on structured, recursive multi-agent pipelines, whereas RCAgent operates through autonomous action–observation loops. To provide an upper bound on achievable performance with stronger reasoning, we additionally ran the same pipelines using Qwen-2.5-Plus.

Table 2. Failure Localization Results (LLaMA3.2-3B vs. Qwen-2.5-Plus)

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Method | | R​e​c​a​l​l​@​1Recall@1 | R​e​c​a​l​l​@​2Recall@2 | R​e​c​a​l​l​@​3Recall@3 | R​e​c​a​l​l​@​5Recall@5 | R​e​c​a​l​l​@​10Recall@10 | M​R​RMRR |
| LLaMA-3.2-3B | RCAgent | 11.01 | 15.94 | 17.97 | 18.84 | 19.42 | 14.43 |
| mABC | 2.65 | 22.26 | 31.17 | 34.54 | 37.79 | 16.83 |
| Qwen-2.5-Plus | RCAgent | 22.10 | 25.80 | 28.40 | 30.25 | 31.10 | 23.95 |
| mABC | 34.19 | 39.87 | 42.13 | 44.51 | 46.78 | 38.46 |

As shown in Table [2](https://arxiv.org/html/2504.18776v2#S3.T2 "Table 2 ‣ 3.1. Capability of SOTA Lightweight LLMs ‣ 3. Empirical Study ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"), the results highlight several key findings. First, although lightweight models can reliably produce syntactically correct tool calls, they struggle to aggregate and interpret evidence from multiple heterogeneous tools. This limitation is most evident in the performance of mABC with LLaMA-3.2-3B, which attains only 2.65% Recall@1 despite successfully executing many tool calls. Second, substituting the lightweight backbone with a model possessing stronger reasoning abilities yields substantial performance gains while keeping the tool pipelines unchanged. For example, the Recall@1 of mABC increases from 2.65% to 34.19% (+31.54 %) when LLaMA-3.2-3B is replaced with Qwen-2.5-Plus; RCAgent shows a similar improvement from 11.01% to 22.10% (+11.09 %). These results provide direct quantitative evidence that reasoning capability plays a central role in determining the effectiveness of failure localization. Third, methods with more complex or recursive tool workflows benefit disproportionately from stronger reasoning. mABC exhibits the largest performance jump, reflecting its heavy reliance on multi-hop reasoning patterns that lightweight models fail to execute reliably.

Together, these findings demonstrate that the primary bottleneck in lightweight LLM-based failure localization is not tool usage itself, but the ability to integrate tool outputs into a coherent reasoning chain. Improving lightweight models’ reasoning abilities remains essential for advancing practical LLM-driven system diagnosis.

To understand the shortcomings of lightweight models, we conducted a systematic qualitative error analysis on the AIOps 2022 dataset. Specifically, from the full set of 835 failure episodes (including both successful and unsuccessful predictions), we randomly sampled 50 cases in which both lightweight LLMs (LLaMA-3.2-3B) equipped with mABC and RCAgent failed to correctly identify the root cause in their top-1 predictions. For each episode, we examined the full sequence of tool invocations, intermediate outputs, and final predictions. The analysis was performed independently by two researchers with experience in failure localization and LLM-based reasoning, followed by a consensus discussion to resolve discrepancies.

* •

  Type-1: Lack of termination awareness.
  Models frequently fail to recognize when sufficient evidence for localization has been collected. This can result in tool call sequences that are either prematurely truncated—missing critical evidence—or excessively prolonged, introducing noise and confusion into the reasoning context. For example, in diagnosing a failure with span ID b711142c1d8f7fd9, mABC identified an anomaly in the downstream span ID 6a214f194590145c and prematurely concluded the reasoning process, treating the corresponding RecommendationService as the root cause and proceeding with further analysis. In reality, the true root cause was located three layers deeper, in the ProductCatalogService.
* •

  Type-2: Parameter extraction failure.
  When the output of previous tools becomes lengthy or semantically complex, lightweight models struggle to correctly extract the necessary fields for the next tool call. For instance, the service name or metric type inferred from a diagnostic trace may be incorrectly formatted, omitted, or mismatched. For example, RCAgent is built upon log analysis and includes adaptations for handling lengthy log data. However, the processed log blocks can still contain hundreds of lines, making it difficult for lightweight models to extract potential root causes for the next reasoning step. As a result, critical information is often missed.
* •

  Type-3: Missed root cause despite available evidence.
  Even in relatively simple cases where the first two issues do not occur—that is, the relevant data for the true root cause is successfully retrieved during the tool invocation process—lightweight models sometimes still fail to correctly identify it. For example, during mABC’s reasoning for a failure with span ID b562d708ca6f300f, all potential root cause services were retrieved, including Frontend, CheckoutService, and EmailService, yet the model incorrectly ranked the true root cause outside the top-1 prediction.

A closer comparison between the two methods further reveals why their failure patterns differ. For the 50 mispredicted cases, mABC exhibits 3 Type-1 failures, 5 Type-2 failures, and 42 Type-3 failures. This distribution aligns with its design characteristics: mABC relies primarily on a voting-based mechanism with a relatively strict and stable reasoning path and a more tolerant parameter-extraction rule (i.e., minor extraction failures do not affect the final decision). As a result, it is less likely to suffer from Type-1 or Type-2 issues, but heavily impacted by Type-3 failures.

By contrast, RCAgent shows 19 Type-1 failures, 7 Type-2 failures, and 24 Type-3 failures. Because RCAgent must autonomously plan its reasoning trajectory and decide when to terminate, and because long multi-turn interactions may accumulate excessive context, it is more vulnerable to Type-1 and Type-2 errors. While its retry mechanism mitigates parameter-extraction issues to some degree, its flexible reasoning flow makes it more likely to deviate when encountering ambiguous or noisy environment feedback.

Notably, both methods exhibit a substantial number of Type-3 failures, which is expected: locating the correct root cause in long, noisy, and highly redundant contexts remains fundamentally challenging for lightweight models.

These observations suggest that the core bottleneck is not tool-use syntax but insufficient semantic understanding and reasoning planning. Lightweight LLMs, due to their limited capacity, are especially susceptible to cascading failures in multi-step reasoning. Unlike larger models that can generalize stable reasoning templates across tasks and remain coherent even under imperfect tool outputs, smaller models often collapse once intermediate steps diverge from their expected distribution.

Summary. Although lightweight LLMs can acquire tool invocation abilities through simple tuning, their effectiveness in failure localization remains limited. The key missing link is their inability to construct coherent, goal-driven reasoning chains under noisy and multi-modal data conditions.

### 3.2. Direct Application of GRPO Algorithm

To further enhance lightweight LLMs with the ability to perform deep and strategic failure localization through tool usage, we experimented with applying the Group Relative Policy Optimization (GRPO) algorithm—originally proposed in the DeepSeekMath work (Shao et al., [2024](https://arxiv.org/html/2504.18776v2#bib.bib77 "Deepseekmath: pushing the limits of mathematical reasoning in open language models")) and subsequently used in the training of DeepSeek-R1 (Guo et al., [2025](https://arxiv.org/html/2504.18776v2#bib.bib50 "Deepseek-r1: incentivizing reasoning capability in llms via reinforcement learning"))—to train LLaMA3.2-3B and LLaMA3-8B models. The key motivation is to leverage reward-based fine-tuning to refine the tool invocation strategy in complex reasoning chains. Given that the core metric for failure localization is Mean Reciprocal Rank (MRR), we set the reward function directly to MRR and implemented GRPO using the OpenRLHF framework (Hu et al., [2024](https://arxiv.org/html/2504.18776v2#bib.bib52 "Openrlhf: an easy-to-use, scalable and high-performance rlhf framework")). We selected LLaMA-3.2-3B and LLaMA-3.1-8B as the GRPO training backbones for three pragmatic reasons. First, they are representative lightweight open-source models, covering the small (≈\approx3B) and medium (≈\approx8B) parameter regimes most relevant for real-world, cost-sensitive deployment. Second, the LLaMA family benefits from a large user community and a mature tooling ecosystem for fine-tuning and RL workflows, which simplifies implementation and reproducibility of GRPO experiments. Third, and importantly, LLaMA’s pretraining and tokenization are strongly English-centric, which better matches the language characteristics of our observability signals (service names, logs, and trace annotations). In our preliminary internal comparisons, LLaMA backbones produced more stable baseline tool-invocation behavior than some other lightweight families, so applying GRPO to these models allowed us to more clearly isolate and measure the gains due to reinforcement fine-tuning. Taken together, these considerations made LLaMA-3.2-3B and LLaMA-3.1-8B a practical and informative choice for evaluating GRPO in the lightweight regime.

##### Training Setup.

Following the standard GRPO pipeline, we adopted a two-phase training regime:

* •

  Phase 1: Supervised Fine-Tuning (SFT). We used a small-scale synthetic dataset composed of multi-turn diagnostic dialogues generated by Claude-3.5-Sonnet. This step imparts initial tool invocation capabilities and coarse-grained decision heuristics.
* •

  Phase 2: GRPO-Based RL Fine-Tuning. The models were then further optimized with GRPO, using MRR as the reward signal. GRPO refines the model by evaluating the relative performance of the group of candidate policies, encouraging outputs that improve their group-relative rank. Instead of relying on traditional reinforcement learning techniques like value or critic networks, GRPO directly optimizes the policy by comparing the relative performance of multiple candidates, thus enabling more robust exploration and policy improvement.

##### Training Dynamics.

As illustrated in Figure [3](https://arxiv.org/html/2504.18776v2#S3.F3 "Figure 3 ‣ Training Dynamics. ‣ 3.2. Direct Application of GRPO Algorithm ‣ 3. Empirical Study ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"), the training curves show limited or even negative improvement in reward and response diversity:

* •

  For LLaMA3-8B, we observed a steady decline in both the average reward and the response length. This implies that the model learned to avoid complex tool chains and instead favored shorter, low-risk responses—a clear symptom of reward hacking.
* •

  The LLaMA3.2-3B model maintained a nearly constant reward ( 0.38) throughout training, failing to discover improved strategies or leverage exploration to escape local optima.

![Refer to caption](x4.png)

(a) Reward

![Refer to caption](x5.png)

(b) Response Length

Figure 3. Training Effects of Direct GRPO Application

##### Reward Signal Limitation.

A core issue lies in the nature of the MRR reward signal itself. MRR is inherently non-smooth and discontinuous:

* •

  A correct answer ranked first yields a score of 1, but this drops to 0.5 if ranked second, and to 0.33 for third, etc.
* •

  This sharp drop-off produces a highly imbalanced reward landscape, where most sampled outputs yield near-zero rewards, making it difficult for policy updates to gain signal and direction.

##### Qualitative Observations.

Inspection of generated outputs post-training revealed several patterns:

* •

  Models tend to collapse to single-step predictions, avoiding exploration of longer reasoning paths.
* •

  When multi-step outputs were generated, their structure was often shallow or repetitive, failing to refine hypotheses based on intermediate tool feedback.
* •

  Tool parameters were often valid syntactically but lacked task-relevance, reflecting a disconnection between search strategy and task-specific semantics.

Summary. The direct application of the GRPO algorithm fails to effectively steer lightweight LLMs toward more optimal failure localization strategies. The coarse and imbalanced MRR-based reward signal hinders effective exploration, while the models’ low capacity limits their ability to recover from early-stage reward sparsity.

In summary, our empirical study reveals that in order to equip lightweight LLMs with failure localization capabilities, the following challenges must be addressed:

* •

  High Dependence on Standardized Tool Invocation. In failure localization, directly feeding all raw data into the LLM rarely yields the correct root cause. Instead, LLM-based methods depend heavily on data querying tools. Since the localization process often requires multiple tool invocations—each based on the results of previous queries—any deviation in the standardized format of these invocations can mislead the model’s judgment. This is in stark contrast to the knowledge QA or mathematical reasoning tasks where GRPO is typically applied.
* •

  Demand for Exploration under Standardized Tool Usage. Although standard supervised fine-tuning (SFT) combined with tool learning can teach LLMs to use tools correctly, such constraints on output format can greatly limit the model’s exploratory capabilities. In contrast, failure localization requires the LLM to explore diverse ways of invoking tools—while still maintaining standardization—to discover the correct pathway under different scenarios.
* •

  Integrated Reward Mechanism for Reasoning Process and Final Output. Once the tool-based inference of the root cause is complete, the final evaluation cannot rely solely on semantic correctness, as in typical knowledge QA tasks. Instead, it necessitates a multi-dimensional scoring approach that combines a rating of the final root cause, the quality of the reasoning path, and penalties for hallucinations.

## 4. ThinkFL

The observations in empirical study underscore the need for a dedicated failure localization paradigm that moves beyond static tool-usage templates. It must support flexible, multi-turn tool reasoning, provide feedback-grounded rewards, and enable lightweight models to improve iteratively over time.

Therefore, in this section, we introduce ThinkFL, a self-refining failure localization model for microservice systems using reinforcement fine-tuning. ThinkFL is designed to bridge the gap between static tool-use policies and dynamic, feedback-driven optimization by combining structured tool invocation with progressive, reward-sensitive adaptation. Figure [4](https://arxiv.org/html/2504.18776v2#S4.F4 "Figure 4 ‣ 4. ThinkFL ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning") illustrates the overall workflow of ThinkFL.

![Refer to caption](x6.png)


Figure 4. Pipeline of ThinkFL

As microservice systems operate continuously, they generate large volumes of trace and metrics data. An external anomaly detection module—which is not part of ThinkFL itself—first processes this data to determine whether a request exhibits abnormal behavior. In our implementation, this step follows the heuristic described earlier in Section [2.3](https://arxiv.org/html/2504.18776v2#S2.SS3 "2.3. Distributed Tracing ‣ 2. Background & Motivation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"), though in practice it may be replaced with any more advanced anomaly detection technique.

Once an anomalous trace is identified, the workflow transitions to failure localization, where ThinkFL begins its reasoning from the entry span of the trace, which anchors the diagnostic episode. For example, an entry span may look like: timestamp=1647747340693, service=frontend-2, traceID=d1b3f238, spanID=ae265c5b, duration=13385835, protocol=http, status=0, operation=hipstershop.Frontend/Recv. Each field provides essential context: the timestamp of the span, the service instance processing the request, the trace ID and span ID identifying the request and its sub-operation, the duration (µs), the protocol used, the status code, and the operation name. From this input, ThinkFL invokes a Recursion-of-Thought (RoT) Actor, which interacts with multiple data tools, including trace analysis and metric evaluation tools. The RoT Actor ultimately produces an actor result, consisting of a ranked list of potential root causes, corresponding explanations, and a complete inference path that is easily interpretable by humans.

The generated actor result is then submitted to expert SREs for validation. If the inferred result is correct, the SRE proceeds with remediation. If it is incorrect, the SRE uses the provided inference path and the list of ranked candidate services as additional context when identifying the true root cause. A Multi-Factor Failure Localization (FL) Grader is then applied, incorporating both the generated actor result and the verified ground-truth root cause to evaluate ThinkFL’s performance. Finally, ThinkFL undergoes further refinement through a Progressive Multi-Stage GRPO Fine-Tuning approach, enhancing its ability to localize failures more accurately over time.

### 4.1. Recursion-of-Thought Actor

Within the overall workflow, the core reasoning engine is the Recursion-of-Thought Actor, as illustrated in Figure [5](https://arxiv.org/html/2504.18776v2#S4.F5 "Figure 5 ‣ 4.1. Recursion-of-Thought Actor ‣ 4. ThinkFL ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"). This actor is built upon a pre-trained large language model—ThinkFL—which continues to evolve through online refinement and task-specific feedback. Its primary role is to perform recursive, multi-step reasoning by selectively invoking a diverse set of data tools and integrating their results into the evolving inference state.

Unlike static prompting pipelines, the Recursion-of-Thought Actor operates in a dynamic, context-aware loop: at each step, it evaluates the current evidence, decides which data tool to apply next, and updates its internal reasoning chain accordingly. Through this iterative process, the actor progressively gathers and synthesizes relevant information, ultimately converging on a ranked set of likely root causes. This design enables flexible adaptation to a wide range of failure patterns and system configurations.

![Refer to caption](x7.png)


Figure 5. Workflow of Recursion-of-Thought Actor

To support this reasoning loop, a collection of data tools serves as the interface between the actor and the underlying system telemetry. These tools abstract the complexity of large-scale observability data and provide structured, filtered insights that facilitate efficient and focused analysis.

#### 4.1.1. Data Tools

Data tools are modular components that provide structured access to specific types of system data. Given a query input, each tool retrieves and preprocesses the relevant information, making it readily consumable by the reasoning agent. In our current implementation, we focus on two primary tools: the Trace Tool and the Metrics Tool. However, the framework is extensible, allowing additional tools—such as logs, configuration diffs, or service topology graphs—to be integrated as needed.

Trace Tool. Distributed trace data captures the end-to-end flow of requests across microservices, making it a foundational resource for root cause localization. In such traces, a span represents a single unit of work, typically corresponding to the execution of a service operation or a method within a microservice. Each span records key information such as its start and end timestamps, the service handling the request, the operation name, and status codes. Spans are organized hierarchically, where a parent span can trigger multiple child spans—these span-level dependencies encode the causal relationships between service calls, effectively forming a tree or directed acyclic graph (DAG) of the request flow across microservices.

To illustrate, consider a request processed by a frontend service that generates span ID b711142c. This request triggers the CheckoutService, which generates a direct child span with ID c4829a7f, and the CheckoutService further invokes the PaymentService, producing another child span d9357b2a. Here, b711142c is the parent span, c4829a7f is its direct child, and d9357b2a is a child of the CheckoutService span. Understanding these span-level dependencies is critical: the true root cause of a failure may reside in a downstream service, and reasoning over the span hierarchy allows the localization agent to trace how errors propagate through the microservice system.

However, the sheer volume of trace data—especially in systems with high request throughput—makes it infeasible to process all spans. To address this, we introduce a Trace Tool that performs targeted retrieval of relevant spans based on span-level dependencies:

|  |  |  |  |
| --- | --- | --- | --- |
| (5) |  | T​(s)={⟨t,s′,s​v​c,o​p,d,σ⟩|s′∈𝒞​(s)}T(s)=\left\{\langle t,s^{\prime},svc,op,d,\sigma\rangle\;\middle|\;s^{\prime}\in\mathcal{C}(s)\right\} |  |

Formally, for a given span identifier ss, the Trace Tool returns the set of its direct child spans 𝒞​(s)\mathcal{C}(s), along with associated metadata such as timestamp tt, child span identifier s′s^{\prime}, service name s​v​csvc, operation name o​pop, duration dd, and status code σ\sigma. This selective retrieval allows the reasoning agent to incrementally explore the trace graph, capturing causal relationships between microservices while staying within the context limits of the LLM.

Metrics Tool. Metrics reflect the performance and health status of various system components, such as services, pods, or nodes. However, in large-scale environments, the volume of metrics can be overwhelming, and most remain stable even during system faults. To reduce noise and focus on actionable signals, we design a Metrics Tool that selectively surfaces only those metrics exhibiting statistically significant deviations.

|  |  |  |  |
| --- | --- | --- | --- |
| (6) |  | |m​(t)−μm|>n×σm|m(t)-\mu\_{m}|>n\times\sigma\_{m} |  |

Specifically, given a timestamp t0t\_{0} and a target component CC, let ℳ​(C)\mathcal{M}(C) be the set of associated metrics. For each metric m∈ℳ​(C)m\in\mathcal{M}(C), we calculate its historical mean μm\mu\_{m} and standard deviation σm\sigma\_{m}. The Metrics Tool applies an nn-sigma test over the window [t0−δ,t0+δ][t\_{0}-\delta,t\_{0}+\delta] to detect abnormal fluctuations:

|  |  |  |  |
| --- | --- | --- | --- |
| (7) |  | Q(t0,δ,C)={m(t)|m∈ℳ​(C),t∈[t0−δ,t0+δ],|m​(t)−μm|>n×σm}Q(t\_{0},\delta,C)=\left\{m(t)\;\middle|\;\begin{array}[]{c}m\in\mathcal{M}(C),\\ t\in[t\_{0}-\delta,t\_{0}+\delta],\\ |m(t)-\mu\_{m}|>n\times\sigma\_{m}\end{array}\right\} |  |

Crucially, the Metrics Tool is not a standalone anomaly detector. It is invoked in the context of a suspected failure episode, where the Trace Tool has already identified candidate components along the span hierarchy. The Metrics Tool then queries only those components and only within the failure’s time window, surfacing deviations that are most relevant to the ongoing episode. In this way, the tool links failures to metrics by conditioning the retrieval on (i) the failure trigger time and (ii) the components under investigation.

This design ensures that the reasoning process is not overwhelmed by irrelevant data, while still leveraging quantitative signals that reinforce or contradict hypotheses generated during trace exploration. Together, the Trace and Metrics Tools provide complementary perspectives—traces identify *where* failures propagate, while metrics explain *why* they occur. Combined, they form the foundation of the Recursion-of-Thought Actor’s reasoning capability, enabling it to navigate vast diagnostic spaces in a scalable and interpretable manner.

#### 4.1.2. Recursion-of-Thought

While traditional Chain-of-Thought (CoT) approaches have shown effectiveness in structured reasoning tasks, they encounter substantial challenges when applied to failure localization in complex distributed systems (Ren, [2025](https://arxiv.org/html/2504.18776v2#bib.bib104 "The multi-agent fault localization system based on monte carlo tree search approach")). In these environments, the diagnostic space is large, noisy, and hierarchically structured—rendering linear reasoning brittle and prone to premature convergence on misleading signals. In contrast, experienced site reliability engineers (SREs) rarely follow a rigid path. Instead, they iteratively formulate and revise hypotheses, consult various data sources, and backtrack as needed.

Inspired by this human-like diagnostic behavior, we propose the Recursion-of-Thought (RoT) framework—a dynamic and self-correcting reasoning paradigm tailored for root cause inference. Unlike CoT, which constructs a static sequence of reasoning steps, RoT performs recursive reasoning driven by evolving context. As illustrated in Algorithm [1](https://arxiv.org/html/2504.18776v2#alg1 "Algorithm 1 ‣ 4.1.2. Recursion-of-Thought ‣ 4.1. Recursion-of-Thought Actor ‣ 4. ThinkFL ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"), where the LLM iteratively selects one of the tools—Trace, Metrics, or Print—based on the evolving reasoning path. Each selected tool contributes new evidence to the inference path RR, which is then used to guide the next step. The algorithm proceeds recursively with a bounded depth, and if no conclusive root cause is printed within the limit, it triggers a fallback mechanism to generate the final output based on the accumulated reasoning history.

Algorithm 1  Recursion-of-Thought Algorithm

1:Entry trace TT for a high-duration request.

2:Formatted potential root cause(s) RfR\_{f}.

3:Initialize inference path R←{T}R\leftarrow\{T\}

4:Initialize allowed actions 𝒜←{Trace,Metrics,Print}\mathcal{A}\leftarrow\{\text{Trace},\text{Metrics},\text{Print}\}

5:printed←False\textit{printed}\leftarrow\text{False}

6:Set maximum recursion depth d←Dmaxd\leftarrow D\_{\max}

7:while d>0d>0 do

8:  Generate reasoning instruction I←f​(R,𝒜)I\leftarrow f(R,\mathcal{A})

9:  a​c​t​i​o​n,p​a​r​a​m​s←Decide​(I)action,params\leftarrow\text{Decide}(I)

10:  if a​c​t​i​o​n=Traceaction=\text{Trace} then

11:   D←TraceTool​(p​a​r​a​m​s)D\leftarrow\text{TraceTool}(params)

12:   R←R∪{D}R\leftarrow R\cup\{D\}

13:  else if a​c​t​i​o​n=Metricsaction=\text{Metrics} then

14:   M←MetricsTool​(p​a​r​a​m​s)M\leftarrow\text{MetricsTool}(params)

15:   R←R∪{M}R\leftarrow R\cup\{M\}

16:  else if a​c​t​i​o​n=Printaction=\text{Print} then

17:   Rf←PrintRootCauses​(R)R\_{f}\leftarrow\text{PrintRootCauses}(R)

18:   printed←True\textit{printed}\leftarrow\text{True}

19:   return RfR\_{f}

20:  end if

21:  d←d−1d\leftarrow d-1

22:end while

23:if printed=False\textit{printed}=\text{False} then

24:  Rf←PrintRootCauses​(f​(R,{Print}))R\_{f}\leftarrow\text{PrintRootCauses}(f(R,\{\text{Print}\}))

25:  return RfR\_{f}

26:end if

##### Tool Invocation Strategy.

Rather than relying on predefined heuristics or action scoring, the Recursion-of-Thought Actor adopts a fully LLM-driven strategy for tool selection. As illustrated in Figure [6](https://arxiv.org/html/2504.18776v2#S4.F6 "Figure 6 ‣ Tool Invocation Strategy. ‣ 4.1.2. Recursion-of-Thought ‣ 4.1. Recursion-of-Thought Actor ‣ 4. ThinkFL ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"), we provide a feasible prompt that demonstrates this process (the actual prompt used in practice includes additional parameters required by the data tools as well as intermediate reasoning steps, making it more complex). At each reasoning step, the actor leverages the contextual knowledge embedded in the language model to decide which tool to invoke—or whether to proceed directly with inference.

Please continue to identify the root cause service.
You may explore deeper by using the search\_traces tool or combine with
search\_fluctuating\_metrics.
If you have determined the root cause, call the print\_results function.
Available tools:
print\_results: report candidate root causes (node/service/pod) with reasoning.
search\_traces: retrieve child spans of a given span\_id.
search\_fluctuating\_metrics: retrieve anomalous metrics around a given service\_name and timestamp.


Figure 6. Illustrative prompt for tool invocation.

This strategy capitalizes on the LLM’s ability to interpret partial observations, maintain reasoning continuity, and adapt its behavior based on newly acquired evidence. Given the current inference path and relevant context, the model formulates its next move through natural language reasoning, without relying on external prioritization logic.

Such a flexible and data-driven decision mechanism ensures generalizability across diverse scenarios, and enables seamless integration of new tools or reasoning patterns without modifying the core workflow.

##### Interpretability of the Reasoning Path.

Beyond enhancing inference performance, the RoT framework offers high interpretability by maintaining an explicit and structured reasoning path RR. Each recursive step—including the generated instruction, the invoked tool, and its output—is appended to this path, forming a transparent trace of the decision-making process.

This interpretability supports expert validation, facilitates post-mortem diagnosis, and enables knowledge distillation for future learning cycles. As a result, the framework not only provides accurate inferences but also fosters trust and reproducibility in system-level debugging workflows.

### 4.2. Multi-Factor Failure Localization Grader

![Refer to caption](x8.png)


Figure 7. Structure of Multi-Factor Failure Localization (FL) Grader

During the online execution of the entire workflow through the recursion-of-thought algorithm, the core component is the multi-factor failure localization grader, as illustrated in Figure [7](https://arxiv.org/html/2504.18776v2#S4.F7 "Figure 7 ‣ 4.2. Multi-Factor Failure Localization Grader ‣ 4. ThinkFL ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"). This grader evaluates the model’s performance from multiple dimensions: (1) Result Correctness via the Recall Grader, (2) Reasoning Path Validity via the Route Grader, and (3) Answer Reliability through a Hallucination Penalty, which discourages the generation of unsupported or fabricated content. The overall score is computed as a weighted combination of these components, formulated in Equation [8](https://arxiv.org/html/2504.18776v2#S4.E8 "Equation 8 ‣ 4.2. Multi-Factor Failure Localization Grader ‣ 4. ThinkFL ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"), where RR denotes the recall score, PP represents the route matching score, and HH is the hallucination penalty. The weights α\alpha, β\beta, and γ\gamma control the relative influence of each component.

|  |  |  |  |
| --- | --- | --- | --- |
| (8) |  | S=α⋅R+β⋅P−γ⋅HS=\alpha\cdot R+\beta\cdot P-\gamma\cdot H |  |

#### 4.2.1. Recall Grader

The recall grader is the most critical component for directly evaluating the model’s final output. While the final failure localization performance is measured using metrics like MRR, this type of reward is often too sparse to effectively guide the training of RoT models. As illustrated in our empirical study, discrete rewards such as MRR provide limited feedback signals during training.

|  |  |  |  |
| --- | --- | --- | --- |
| (9) |  | R={1−rrm​a​x,r≤rmax1rm​a​x,r>rmaxR=\begin{cases}1-\frac{r}{r\_{max}},&r\leq r\_{\text{max}}\\ \frac{1}{r\_{max}},&r\textgreater r\_{\text{max}}\end{cases} |  |

To address this, we adopt a linear rank-based scoring scheme, as formulated in Equation [9](https://arxiv.org/html/2504.18776v2#S4.E9 "Equation 9 ‣ 4.2.1. Recall Grader ‣ 4.2. Multi-Factor Failure Localization Grader ‣ 4. ThinkFL ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"), where rr is the rank of the correct root cause in the model’s predicted list. We define a maximum effective rank rm​a​xr\_{max}, beyond which all predictions receive a fixed low score. For ranks within the valid range [0,rm​a​x][0,r\_{max}], each higher position in the ranking receives a proportionally lower score, with rank 0 corresponding to a full score of 1.

#### 4.2.2. Route Grader

The Route Grader is designed to evaluate the correctness and appropriateness of the reasoning path generated during failure localization. It serves two main purposes. First, it measures the position of the correct root cause within the reasoning path: a later appearance (closer to the end) suggests a well-refined inference. However, we introduce a tolerance threshold to account for slightly extended reasoning paths, which may include normal service components that help confirm the diagnostic conclusion. Second, if the correct root cause is not present in the path, the grader instead assigns a score based on the path length, under the assumption that a longer reasoning process may still yield useful evidence.

|  |  |  |  |
| --- | --- | --- | --- |
| (10) |  | P={min⁡{rL−μ, 1},if ​r∈Rmin⁡{LDmax, 1},if ​r∉RP=\begin{cases}\min\left\{\frac{r}{L-\mu},\ 1\right\},&\text{if }r\in R\\ \min\left\{\frac{L}{D\_{\text{max}}},\ 1\right\},&\text{if }r\notin R\end{cases} |  |

To capture these two perspectives, the route score PP is defined as a combination of the position score PposP\_{\text{pos}} and the length score PlenP\_{\text{len}}. The position score reflects how close the correct root cause appears to the end of the reasoning path. If it occurs within the final μ\mu steps of a reasoning path of length LL, a full score of 1 is awarded; otherwise, the score decays linearly. The length score rewards longer reasoning paths, up to a maximum threshold DmaxD\_{\text{max}}, encouraging more comprehensive analysis when the root cause is not identified. In summary, the route grader can be calculated as Equation [10](https://arxiv.org/html/2504.18776v2#S4.E10 "Equation 10 ‣ 4.2.2. Route Grader ‣ 4.2. Multi-Factor Failure Localization Grader ‣ 4. ThinkFL ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").

#### 4.2.3. Hallucination Penalty

During training, we observed that lightweight LLMs occasionally generate hallucinated information when exposed to unfamiliar data. Specifically, two major types of hallucinations frequently occur in the final root cause outputs: (1) predicting root causes that do not appear in the generated reasoning path, and (2) redundantly outputting the same root cause multiple times.

|  |  |  |  |
| --- | --- | --- | --- |
| (11) |  | H=λ1⋅NinvNtotal+λ2⋅NdupNtotalH=\lambda\_{1}\cdot\frac{N\_{\text{inv}}}{N\_{\text{total}}}+\lambda\_{2}\cdot\frac{N\_{\text{dup}}}{N\_{\text{total}}} |  |

To penalize these behaviors and encourage the model to produce faithful and diverse outputs, we introduce a hallucination penalty, as defined in Equation [11](https://arxiv.org/html/2504.18776v2#S4.E11 "Equation 11 ‣ 4.2.3. Hallucination Penalty ‣ 4.2. Multi-Factor Failure Localization Grader ‣ 4. ThinkFL ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"). Here, NinvN\_{\text{inv}} denotes the number of predicted root causes not found in the reasoning path, NdupN\_{\text{dup}} is the number of duplicated root causes, NtotalN\_{\text{total}} is the total number of predicted root causes, and λ1\lambda\_{1} and λ2\lambda\_{2} are weighting coefficients used to balance the penalty for each type of hallucination.

### 4.3. Progressive Multi-Stage GRPO Fine-Tuning

![Refer to caption](x9.png)


Figure 8. Workflow of Progressive Multi-Stage GRPO Fine-Tuning

Although the proposed multi-factor failure localization grader offers effective guidance for improving root cause identification via Recursion-of-Thought (RoT), the lightweight LLM backbone still exhibits two prominent limitations: (1) suboptimal external tool invocation behavior, and (2) insufficient diversity in reasoning trajectories. To mitigate these issues, we introduce a progressive multi-stage GRPO fine-tuning algorithm, designed to incrementally enhance the model’s capabilities.

As depicted in Figure [8](https://arxiv.org/html/2504.18776v2#S4.F8 "Figure 8 ‣ 4.3. Progressive Multi-Stage GRPO Fine-Tuning ‣ 4. ThinkFL ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"), the proposed framework consists of three carefully orchestrated stages:

1. (1)

   Format-Aware Policy Priming, which equips the model with accurate and structured tool usage abilities;
2. (2)

   Guided Exploration Augmentation, which encourages diverse and informative reasoning behaviors;
3. (3)

   Rank-Oriented Refinement, which aligns the model’s outputs with high-quality, grader-validated reasoning trajectories.

#### 4.3.1. Format-Aware Policy Priming

This stage aims to establish a robust foundation for tool-augmented reasoning. It operates in two phases: Supervised Fine-Tuning (SFT) and Reinforced Fine-Tuning (RFT).

SFT Phase. We begin by sampling a small, diverse subset of questions from the raw dataset. Broadly speaking, the raw dataset consists of accumulated, high-quality historical failure localization cases, including the questions, reasoning process, and answers. In this work, the raw dataset specifically refers to the AIOPS 2022 dataset, from which we select only 100 questions for the SFT phase. Using an oracle model (e.g., Claude or DeepSeek-R1), we generate multi-turn conversations (MTCs) that follow the Recursion-of-Thought (RoT) protocol. These MTCs include both intermediate reasoning steps and the final root cause predictions, serving as high-quality supervision to teach the lightweight LLM (ThinkFL) how to invoke tools correctly and structure its reasoning.

Importantly, we keep the SFT scale deliberately small to preserve the model’s exploratory capacity and avoid premature overfitting to rigid patterns.

RFT Phase. Building on the SFT initialization, the model enters a reinforced learning stage in which it explores diverse reasoning paths under higher sampling temperature. For each generated trajectory, we apply a hybrid reward function comprising:

* •

  A recall grader, which measures correctness of the final prediction;
* •

  A format grader, which evaluates structural adherence to the expected schema.

The format grader plays a critical role in ensuring output consistency and tool usability. It verifies schema compliance across multiple levels, such as correct inclusion of name and arguments fields, valid JSON-like argument structures, and well-formed root cause elements containing essential attributes like node, service, and pod. Malformed outputs are down-weighted to enforce format discipline.

Algorithm 2  Diversity Grader Evaluation

1:Question qq, Reasoning path pp, Path cache 𝒫q\mathcal{P}\_{q}

2:p′←p^{\prime}\leftarrow Deduplicate(pp)

3:if p′p^{\prime} not in 𝒫q\mathcal{P}\_{q} then

4:  𝒫q←𝒫q∪{p′}\mathcal{P}\_{q}\leftarrow\mathcal{P}\_{q}\cup\{p^{\prime}\}

5:  if SolvesProblem(qq, p′p^{\prime}) then

6:   return Score =A=A ⊳\triangleright New + Correct

7:  else

8:   return Score =B=B ⊳\triangleright New but Incorrect

9:  end if

10:else

11:  return Score =C=C ⊳\triangleright Repetitive

12:end if

#### 4.3.2. Guided Exploration Augmentation

While the priming stage focuses on correctness and format, this stage emphasizes reasoning diversity, which aims to enhance the model’s ability to explore diverse failure localization paths while maintaining correct tool invocation. To achieve this, we introduce data augmentation through controlled duplication of input questions. By presenting the same question multiple times during training, we encourage the model to generate varied reasoning paths and corresponding root causes across different training steps. Each generated output is evaluated using a combined grading mechanism consisting of a diversity grader and a recall grader, with a slightly higher weight assigned to the recall grader to discourage the model from exploiting the reward signal by generating overly noisy or irrelevant reasoning paths.

The diversity grader operates as described in Algorithm [2](https://arxiv.org/html/2504.18776v2#alg2 "Algorithm 2 ‣ 4.3.1. Format-Aware Policy Priming ‣ 4.3. Progressive Multi-Stage GRPO Fine-Tuning ‣ 4. ThinkFL ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"). For each question, we maintain a dynamic cache of previously generated reasoning paths. After a new reasoning path is produced, redundant tool invocations—those with identical tools and parameters—are filtered out. The path is then compared against the cache: if the path is entirely novel, a high reward AA is given; if the path solves the question with only slight variation, a moderate reward BB is assigned; if the path is already present in the cache, a lower reward CC is used, where A≫B>CA\gg B>C.

#### 4.3.3. Rank-Oriented Refinement

After the previous two stages, the model has developed a strong capability in failure localization. The goal of this final stage—Rank-Oriented Refinement—is to further consolidate the model’s reasoning and output quality. For each question, the model generates multiple rollouts, and these outputs are subsequently evaluated using the multi-factor failure localization grader.

As aforementioned, this grader comprehensively assesses each rollout based on multiple dimensions, such as accuracy of root cause identification, reasoning trace completeness, and format correctness. By ranking the outputs according to these scores and reinforcing the higher-quality responses, the model is guided to converge towards more precise and reliable failure localization strategies.

## 5. Evaluation

To evaluate the effectiveness and robustness of ThinkFL, we design a series of experiments guided by the following research questions:

* •

  EV-RQ1: How does ThinkFL perform in failure localization accuracy compared to baseline LLMs and state-of-the-art failure localization approaches?
* •

  EV-RQ2: What is the inference efficiency of ThinkFL in terms of runtime, and how does it compare with baseline LLMs?
* •

  EV-RQ3: How does each stage in the ThinkFL training pipeline contribute to the final localization accuracy?
* •

  EV-RQ4: What are the key behavioral and policy changes observed during the GRPO training process, and how do they reflect the model’s evolving decision strategies?
* •

  EV-RQ5: How effective is the proposed ThinkFL training method when applied to different LLM backbones (e.g., Qwen2.5, Llama3), and what is the trade-off between model size and performance?
* •

  EV-RQ6: In what ways does self-refinement in ThinkFL enable more accurate and nuanced failure localization, as illustrated through detailed case studies?
* •

  EV-RQ7: How sensitive is ThinkFL’s performance to key hyperparameters?
* •

  EV-RQ8: How well does ThinkFL generalize to other microservice systems?

### 5.1. Experimental Setup

#### 5.1.1. Dataset

Our experiments use the AIOPS 2022 dataset from a mature microservices-based e-commerce system, spanning six subsets across two days and three cloudbeds; for clarity, we denote them as 𝐀\mathbf{A}, 𝐁\mathbf{B}, 𝚪\mathbf{\Gamma}, 𝚫\mathbf{\Delta}, 𝐄\mathbf{E}, 𝐙\mathbf{Z}. The monitored system has 7 microservices deployed over 44 pods and 6 nodes, with traces ranging from hundreds to thousands of spans.

We define failures at the end-to-end request level. A trace is anomalous if its entry span latency exceeds 100× the normal average or reports an abnormal status (e.g., 5xx). Each failure is annotated with the ground-truth root cause at exactly one level: service (e.g., CheckoutService), pod (e.g., checkoutservice-0), or node (e.g., node-0).

Each case provides (i) the entry span with basic attributes, (ii) the full distributed trace (span DAG), (iii) time-aligned node/service/pod metrics around the failure, and (iv) the labeled root cause. This format supports traversal of span-level dependencies and validation using metrics, facilitating methods like ThinkFL for component-level localization.

#### 5.1.2. Baseline Models and Approaches

We compared ThinkFL against five state-of-the-art (SOTA) LLMs and eight representative root cause localization methods. The LLMs—Claude-3.5-Sonnet, Qwen-2.5-Plus, Llama3.1-70B, DeepSeek-R1-Qwen-32B, and Qwen-2.5-Max—were guided to reason under the Recursion-of-Thought (RoT) paradigm to generate final root causes.

The eight SOTA localization approaches can be categorized into two groups: ML/DL-based, and LLM-based methods.

ML/DL-based: CRISP (Zhang et al., [2022](https://arxiv.org/html/2504.18776v2#bib.bib7 "{crisp}: Critical path analysis of {large-scale} microservice architectures")) represents traces as critical paths and applies a lightweight heuristic to identify root cause instances. TraceContrast (Zhang et al., [2024a](https://arxiv.org/html/2504.18776v2#bib.bib4 "Trace-based multi-dimensional root cause localization of performance issues in microservice systems")) utilizes sequence representations, contrastive sequential pattern mining, and spectrum analysis to localize multi-dimensional root causes. TraceRank (Yu et al., [2023b](https://arxiv.org/html/2504.18776v2#bib.bib5 "TraceRank: abnormal service localization with dis-aggregated end-to-end tracing data in cloud native systems")) combines spectrum analysis with a PageRank-based random walk algorithm to pinpoint anomalous services. MicroRank (Yu et al., [2021](https://arxiv.org/html/2504.18776v2#bib.bib6 "Microrank: end-to-end latency issue localization with extended spectrum analysis in microservice environments")) constructs a trace coverage tree to capture dependencies between requests and service instances, leveraging the PageRank algorithm to score potential root causes. RUN (Lin et al., [2024](https://arxiv.org/html/2504.18776v2#bib.bib8 "Root cause analysis in microservice using neural granger causal discovery")) employs time series forecasting for neural Granger causal discovery and integrates a personalized PageRank algorithm to efficiently recommend the top-k root causes. Microscope (Lin et al., [2018](https://arxiv.org/html/2504.18776v2#bib.bib3 "Microscope: pinpoint performance issues with causal graphs in micro-service environments")) builds causality graphs and utilizes a depth-first search strategy to detect front-end anomalies.

LLM-based: mABC (Zhang et al., [2024e](https://arxiv.org/html/2504.18776v2#bib.bib24 "MABC: multi-agent blockchain-inspired collaboration for root cause analysis in micro-services architecture")) proposes a multi-agent, blockchain-inspired collaboration framework where multiple LLM-based agents follow a structured workflow and collaborate through blockchain-inspired voting mechanisms. RCAgent (Wang et al., [2024b](https://arxiv.org/html/2504.18776v2#bib.bib44 "Rcagent: cloud root cause analysis by autonomous agents with tool-augmented large language models")) is an LLM-based reasoning and acting framework where a controller agent executes a thought–action–observation loop and dynamically invokes expert agents as tools for domain-specific tasks, with a flexible exit mechanism to report findings.

#### 5.1.3. Evaluation Metrics

We use the top-k recall (Recall@k) and mean reciprocal rank (MRR) to evaluate the accuracy of root cause localization following existing works (Zhang et al., [2024a](https://arxiv.org/html/2504.18776v2#bib.bib4 "Trace-based multi-dimensional root cause localization of performance issues in microservice systems")).

* •

  Recall@kk: Measures the proportion of fault instances for which the ground-truth root cause appears in the top-kk positions of the predicted list. Formally, as illustrated by Equation [12](https://arxiv.org/html/2504.18776v2#S5.E12 "Equation 12 ‣ 1st item ‣ 5.1.3. Evaluation Metrics ‣ 5.1. Experimental Setup ‣ 5. Evaluation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"), given a set of fault instances AA, let H​i​t​@​kiHit@k\_{i} denote whether the root cause for the ii-th instance appears within the top-kk predictions (H​i​t​@​ki=1Hit@k\_{i}=1 if yes, 0 otherwise). In this paper, we evaluate Recall@1, Recall@2, Recall@3, Recall@5, and Recall@10.

  |  |  |  |  |
  | --- | --- | --- | --- |
  | (12) |  | R​e​c​a​l​l​@​k=1|A|​∑i=1|A|H​i​t​@​kiRecall@k=\frac{1}{|A|}\sum\_{i=1}^{|A|}Hit@k\_{i} |  |
* •

  MRR: is the multiplicative inverse of the rank of the root cause in the result list. If the root cause is not included in the result list, the rank can be regarded as positive infinity. Given a set of fault instances AA, R​a​n​kiRank\_{i} is the ii rank of the root cause in the returned list of the iith fault instance, MRR is calculated by Equation [13](https://arxiv.org/html/2504.18776v2#S5.E13 "Equation 13 ‣ 5.1.3. Evaluation Metrics ‣ 5.1. Experimental Setup ‣ 5. Evaluation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").

|  |  |  |  |
| --- | --- | --- | --- |
| (13) |  | M​R​R=1|A|​∑i=1|A|1R​a​n​kiMRR=\frac{1}{|A|}\sum\_{i=1}^{|A|}\frac{1}{Rank\_{i}} |  |

#### 5.1.4. Implementation and Settings

We implement our algorithm using OpenRLHF v0.6.1.post1 (Hu et al., [2024](https://arxiv.org/html/2504.18776v2#bib.bib52 "Openrlhf: an easy-to-use, scalable and high-performance rlhf framework")). Unless otherwise specified, we set the maximum effective rank to rmax=10r\_{\text{max}}=10, the maximum dialogue depth to Dmax=10D\_{\text{max}}=10, and the weighting parameters to α=1\alpha=1, β=0.2\beta=0.2, and γ=0.2\gamma=0.2. Throughout all experiments, we adopt Llama-3.2-3B as the backbone LLM for fine-tuning. For comparison, all state-of-the-art LLM-based failure localization baselines are executed on Qwen-2.5-Plus.

All experiments are conducted on a CentOS 8 Linux server equipped with 24 Intel(R) Xeon(R) CPUs (2.90GHz), 400GB of RAM, and two NVIDIA A800 GPUs, each with 80GB of memory.

#### 5.1.5. Evaluation Procedure

For each research question (EV-RQ1–EV-RQ8), we follow a systematic procedure to ensure fair and reproducible evaluation:

* •

  Data selection: For RQs evaluating accuracy and efficiency (EV-RQ1 and EV-RQ2), all six subsets of the AIOPS 2022 dataset are used. For generalization studies (EV-RQ8), the TrainTicket dataset is additionally evaluated. Each subset is treated independently to capture different workload patterns and system behaviors.
* •

  Method execution: Each baseline and ThinkFL model is executed on the corresponding dataset subset. LLM-based methods are prompted using the Recursion-of-Thought or tool-invocation paradigms as described in Section 3. For trace- and metrics-based methods, the original or reproduced implementations are applied directly to the subset.
* •

  Metric computation: Recall@k and MRR are computed for each subset-method combination. For multi-step methods (e.g., ThinkFL), final predictions are aggregated per failure case to compute metrics. This ensures that evaluation reflects both accuracy and practical usability.
* •

  Result aggregation: Metrics are averaged across all subsets for overall comparison, while subset-level results are reported to analyze sensitivity to workload, system configuration, and dataset characteristics. Ablation studies and hyperparameter sensitivity analyses are similarly performed per subset before aggregation.

### 5.2. Overall Accuracy

Table 3. Evaluation Results Compared with SOTA LLMs

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Model | | 𝐀\mathbf{A} | 𝐁\mathbf{B} | 𝚪\mathbf{\Gamma} | 𝚫\mathbf{\Delta} | 𝐄\mathbf{E} | 𝐙\mathbf{Z} |
| Claude-3.5-Sonnet | R​e​c​a​l​l​@​1Recall@1 | 28.47 | 41.26 | 36.29 | 38.06 | 30.40 | 39.87 |
| R​e​c​a​l​l​@​2Recall@2 | 59.66 | 57.40 | 69.10 | 49.74 | 54.19 | 62.41 |
| R​e​c​a​l​l​@​3Recall@3 | 62.37 | 70.85 | 89.22 | 64.86 | 64.76 | 72.66 |
| R​e​c​a​l​l​@​5Recall@5 | 64.41 | 72.20 | 91.73 | 71.74 | 69.82 | 76.58 |
| R​e​c​a​l​l​@​10Recall@10 | 68.14 | 73.54 | 92.57 | 79.35 | 78.19 | 80.63 |
| M​R​RMRR | 46.13 | 54.42 | 60.07 | 51.86 | 48.51 | 56.17 |
| Qwen-2.5-Plus | R​e​c​a​l​l​@​1Recall@1 | 21.11 | 26.82 | 26.63 | 15.79 | 11.89 | 26.93 |
| R​e​c​a​l​l​@​2Recall@2 | 30.79 | 26.82 | 49.15 | 20.29 | 34.58 | 32.08 |
| R​e​c​a​l​l​@​3Recall@3 | 32.18 | 27.27 | 50.24 | 24.58 | 37.00 | 33.63 |
| R​e​c​a​l​l​@​5Recall@5 | 32.87 | 28.18 | 53.51 | 29.39 | 40.75 | 35.56 |
| R​e​c​a​l​l​@​10Recall@10 | 33.91 | 29.55 | 58.35 | 35.67 | 45.15 | 39.05 |
| MRR | 26.89 | 27.37 | 39.98 | 21.73 | 25.75 | 31.08 |
| Llama3.1-70B | R​e​c​a​l​l​@​1Recall@1 | 16.67 | 26.46 | 23.74 | 25.44 | 6.17 | 24.69 |
| R​e​c​a​l​l​@​2Recall@2 | 30.42 | 26.91 | 45.08 | 28.99 | 27.88 | 29.77 |
| R​e​c​a​l​l​@​3Recall@3 | 32.92 | 28.25 | 48.44 | 32.85 | 28.95 | 33.45 |
| R​e​c​a​l​l​@​5Recall@5 | 35.83 | 29.60 | 53.12 | 35.35 | 34.05 | 36.78 |
| R​e​c​a​l​l​@​10Recall@10 | 38.33 | 31.84 | 59.23 | 39.10 | 41.82 | 43.43 |
| M​R​RMRR | 25.69 | 27.88 | 37.74 | 29.79 | 19.92 | 30.44 |
| DeepSeek-R1-Qwen-32B | R​e​c​a​l​l​@​1Recall@1 | 14.34 | 14.81 | 27.30 | 18.81 | 12.66 | 15.77 |
| R​e​c​a​l​l​@​2Recall@2 | 27.91 | 14.81 | 50.42 | 21.67 | 38.23 | 22.43 |
| R​e​c​a​l​l​@​3Recall@3 | 27.91 | 15.34 | 51.53 | 23.10 | 39.75 | 23.73 |
| R​e​c​a​l​l​@​5Recall@5 | 29.46 | 15.87 | 53.76 | 24.05 | 41.77 | 27.21 |
| R​e​c​a​l​l​@​10Recall@10 | 33.72 | 17.99 | 60.31 | 28.81 | 46.82 | 32.71 |
| M​R​RMRR | 22.19 | 15.56 | 40.98 | 21.76 | 27.33 | 21.36 |
| Qwen-2.5-Max | R​e​c​a​l​l​@​1Recall@1 | 3.20 | 16.51 | 7.80 | 5.75 | 2.08 | 10.36 |
| R​e​c​a​l​l​@​2Recall@2 | 13.52 | 18.87 | 36.76 | 7.51 | 30.09 | 16.87 |
| R​e​c​a​l​l​@​3Recall@3 | 14.23 | 19.81 | 37.75 | 8.40 | 32.18 | 18.46 |
| R​e​c​a​l​l​@​5Recall@5 | 15.30 | 20.75 | 39.23 | 10.50 | 33.79 | 20.05 |
| R​e​c​a​l​l​@​10Recall@10 | 18.86 | 22.17 | 41.21 | 11.27 | 35.18 | 21.65 |
| M​R​RMRR | 9.78 | 18.42 | 23.54 | 7.56 | 17.37 | 14.93 |
| ThinkFL-3B (ours) | R​e​c​a​l​l​@​1Recall@1 | 37.63 | 60.54 | 49.34 | 60.90 | 33.04 | 51.52 |
| R​e​c​a​l​l​@​2Recall@2 | 65.42 | 71.30 | 81.20 | 75.29 | 55.95 | 74.05 |
| R​e​c​a​l​l​@​3Recall@3 | 72.54 | 73.54 | 86.71 | 80.60 | 69.38 | 77.47 |
| R​e​c​a​l​l​@​5Recall@5 | 73.56 | 75.34 | 90.54 | 83.73 | 76.43 | 81.14 |
| R​e​c​a​l​l​@​10Recall@10 | 74.92 | 75.78 | 91.86 | 86.86 | 80.62 | 84.05 |
| M​R​RMRR | 54.44 | 67.13 | 68.26 | 71.05 | 51.48 | 65.22 |

We first compare ThinkFL against state-of-the-art LLMs. As shown in Table [3](https://arxiv.org/html/2504.18776v2#S5.T3 "Table 3 ‣ 5.2. Overall Accuracy ‣ 5. Evaluation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"), ThinkFL significantly outperforms all baseline models on the failure localization task across all evaluation metrics and datasets. In terms of R​e​c​a​l​l​@​1Recall@1, ThinkFL achieves an average improvement of 13.05% over Claude-3.5-Sonnet, the strongest among the compared baselines, highlighting its superior ability to identify the correct root cause at the top-ranked position. On dataset 𝐁\mathbf{B}, ThinkFL attains 60.54% in R​e​c​a​l​l​@​1Recall@1, a substantial lead over Claude-3.5-Sonnet’s 41.26%, suggesting its stronger discriminative capability in more complex cases. Similarly, for dataset 𝚫\mathbf{\Delta}, ThinkFL improves R​e​c​a​l​l​@​1Recall@1 by over 22.84% compared to Claude-3.5-Sonnet, demonstrating robustness even under challenging diagnostic scenarios.

As the number of retrieved candidates increases, ThinkFL consistently maintains its lead. At R​e​c​a​l​l​@​3Recall@3 and R​e​c​a​l​l​@​5Recall@5, ThinkFL records average gains of 5.88% and 5.70% over Claude-3.5-Sonnet, respectively. These results indicate that even when multiple hypotheses are allowed, ThinkFL provides more relevant candidate causes, reinforcing its utility in real-world scenarios where analysts often consider a short list of likely causes. Moreover, ThinkFL exhibits outstanding performance in Mean Reciprocal Rank (MRR), with an average improvement of 10.08% over Claude-3.5-Sonnet. The MRR advantage indicates that ThinkFL not only ranks the correct answer more frequently at the top, but also returns it earlier in the list more consistently than any other model.

In addition to outperforming Claude-3.5-Sonnet, ThinkFL demonstrates significant superiority over other strong baselines such as Qwen-2.5-Plus and Llama3.1-70B. On dataset 𝚪\mathbf{\Gamma}, for instance, ThinkFL reaches 86.71% in R​e​c​a​l​l​@​3Recall@3, compared to 50.24% and 48.44% for Qwen-2.5-Plus and Llama3.1-70B, respectively—illustrating its notable edge in identifying root causes in high-noise settings. On dataset 𝐄\mathbf{E}, which requires more intricate and multi-hop reasoning to accurately identify the root cause, ThinkFL achieves an MRR of 51.48%, outperforming Qwen-2.5-Plus and Llama3.1-70B by 25.73% and 31.56%, respectively. These substantial margins underscore ThinkFL’s superior capacity for deep reasoning and causal inference, particularly in scenarios where surface-level correlations are insufficient and a nuanced understanding of system behavior is essential for correct localization.

We further compare ThinkFL against existing SOTA root cause localization methods, including ML/DL-based, and LLM-based approaches. As reported in Table [4](https://arxiv.org/html/2504.18776v2#S5.T4 "Table 4 ‣ 5.2. Overall Accuracy ‣ 5. Evaluation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"), ThinkFL yields the highest MRR on all datasets except 𝐁\mathbf{B}, where it is slightly outperformed by TraceRank. However, even in that case, ThinkFL remains highly competitive, with only a 9.63% difference while achieving superior generalization across the remaining five datasets.

Table 4. Evaluation Results Compared with SOTA Methods

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Method | | 𝐀\mathbf{A} | 𝐁\mathbf{B} | 𝚪\mathbf{\Gamma} | 𝚫\mathbf{\Delta} | 𝐄\mathbf{E} | 𝐙\mathbf{Z} |
| ML/DL-based | CRISP | 8.27 | 20.13 | 18.13 | 17.34 | 31.08 | 17.14 |
| TraceConstract | 13.07 | 65.74 | 58.55 | 2.48 | 33.77 | 8.15 |
| TraceRank | 6.26 | 76.76 | 34.41 | 61.54 | 35.79 | 38.36 |
| MicroRank | 11.38 | 18.12 | 38.10 | 2.98 | 30.81 | 9.15 |
| RUN | 11.72 | 3.12 | 25.65 | 5.62 | 7.58 | 8.95 |
|  | MicroScope | 23.76 | 4.55 | 37.46 | 13.24 | 21.38 | 21.33 |
| LLM-based | RCAgent | 17.59 | 20.20 | 23.95 | 14.64 | 12.65 | 16.35 |
| mABC | 35.47 | 33.77 | 38.46 | 31.33 | 21.92 | 21.37 |
| ThinkFL | | 54.44 | 67.13 | 68.26 | 71.05 | 49.59 | 65.22 |

Compared to TraceRank, the strongest trace-based baseline, ThinkFL delivers an average improvement of 20.43% in MRR, with particularly notable advantages on 𝐀\mathbf{A} (48.18 %) and 𝚪\mathbf{\Gamma} (33.85 %), demonstrating ThinkFL’s ability to generalize across both noisy and structured traces. When compared to MicroScope, the best-performing metrics-based method, ThinkFL exhibits an even more dramatic improvement of 42.33%, underscoring the limitations of relying solely on metrics in isolation. Likewise, ThinkFL exceeds the best-performing LLM-based method, mABC, by 32.23%, showcasing the advantage of our design in integrating logs and metrics under a unified inference framework. It is also worth emphasizing that all LLM-based baselines are implemented on Qwen-2.5-Plus, a model with significantly more parameters than ThinkFL.

### 5.3. Inference Time

To further highlight the efficiency of ThinkFL, we conduct a comprehensive comparison of its inference time against SOTA LLMs. As presented in Table [5](https://arxiv.org/html/2504.18776v2#S5.T5 "Table 5 ‣ 5.3. Inference Time ‣ 5. Evaluation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"), ThinkFL demonstrates remarkable speed, completing each failure localization task in an average of only 3.40 seconds across six representative datasets. This is approximately 673.11% faster than the second-best model, Qwen-2.5-Plus, and outpaces heavier models such as Llama3.1-70B and DeepSeek-R1-Qwen by several orders of magnitude.

Table 5. Inference Speed Compared with SOTA Models (seconds/query)

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Model | 𝐀\mathbf{A} | 𝐁\mathbf{B} | 𝚪\mathbf{\Gamma} | 𝚫\mathbf{\Delta} | 𝐄\mathbf{E} | 𝐙\mathbf{Z} |
| Claude-3.5-Sonnet | 90.38 | 51.30 | 89.45 | 44.00 | 29.83 | 29.40 |
| Qwen-2.5-Plus | 30.87 | 23.98 | 26.05 | 19.55 | 27.57 | 29.85 |
| Llama3.1-70B | 95.42 | 579.36 | 235.81 | 283.25 | 939.28 | 103.35 |
| DeepSeek-R1-Qwen-32B | 194.81 | 154.14 | 149.31 | 143.47 | 234.43 | 333.42 |
| Qwen-2.5-Max | 64.61 | 39.64 | 36.71 | 42.18 | 36.79 | 38.43 |
| ThinkFL-3B | 3.51 | 3.30 | 3.30 | 3.54 | 3.38 | 3.39 |

This drastic reduction in inference time is not merely a numerical advantage—it translates directly into practical benefits in real-world system operations. In latency-sensitive environments where SREs must react swiftly to service disruptions, ThinkFL enables near-instantaneous root cause localization, thereby significantly shortening the mean time to recovery (MTTR). In contrast to models like Llama3.1-70B—which may require several minutes per failure case—ThinkFL reduces the latency to the order of seconds, making it far more practical for real-time troubleshooting scenarios.

Moreover, ThinkFL’s speed advantage comes without sacrificing accuracy or robustness, proving that lightweight and targeted reasoning can outperform brute-force processing by large-scale models. Unlike general-purpose LLMs such as Llama3.1-70B, which suffer from massive parameter overhead and rely on overly generalized reasoning paths, ThinkFL’s domain-specialized design and efficient recursion-of-thought architecture enable it to operate effectively in low-latency regimes. This makes it particularly well-suited for production-scale environments where both time and resources are at a premium.

### 5.4. Ablation Study

To evaluate the effectiveness of our progressive multi-stage GRPO fine-tuning algorithm, we track the failure localization performance of ThinkFL after each stage on two representative backbone models: Llama3.2-3B and Qwen2.5-3B.

Table 6. Ablation Study of Progressive GRPO (ThinkFL-Llama3.2-3B)

|  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Dataset | Stage 1 | | | | Stage 2 | | | | Stage 3 | | | |
| R1 | R3 | R5 | MRR | R1 | R3 | R5 | MRR | R1 | R3 | R5 | MRR |
| 𝐀\mathbf{A} | 25.08 | 31.53 | 32.88 | 28.64 | 22.37 | 50.85 | 54.24 | 37.09 | 37.63 | 72.54 | 73.56 | 54.44 |
| 𝐁\mathbf{B} | 46.19 | 70.85 | 71.75 | 57.50 | 69.51 | 70.85 | 73.09 | 59.32 | 60.54 | 73.54 | 75.34 | 67.13 |
| 𝚪\mathbf{\Gamma} | 30.42 | 82.16 | 86.35 | 54.92 | 61.08 | 63.83 | 64.67 | 62.54 | 49.34 | 86.71 | 90.54 | 68.26 |
| 𝚫\mathbf{\Delta} | 46.19 | 76.64 | 81.86 | 62.01 | 50.26 | 79.04 | 85.19 | 64.24 | 60.90 | 80.60 | 83.73 | 71.05 |
| 𝐄\mathbf{E} | 32.16 | 35.46 | 35.68 | 33.86 | 28.63 | 60.35 | 69.38 | 45.34 | 33.04 | 69.38 | 76.43 | 51.48 |
| 𝐙\mathbf{Z} | 36.71 | 71.77 | 77.97 | 54.15 | 40.89 | 74.43 | 79.37 | 58.01 | 51.52 | 77.47 | 81.14 | 65.22 |

As shown in Table [6](https://arxiv.org/html/2504.18776v2#S5.T6 "Table 6 ‣ 5.4. Ablation Study ‣ 5. Evaluation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"), ThinkFL based on Llama3.2-3B already exhibits strong localization performance after Stage 1, with an average MRR of 48.51% across six datasets. After Stage 2, the average MRR increases to 54.42%, and further improves to 62.93% after Stage 3, marking a relative improvement of 14.42% from Stage 1 to Stage 3. Notably, Dataset 𝐀\mathbf{A} shows the most dramatic gain, with MRR rising from 28.64% to 54.44%—an increase of 25.80%. These results suggest that GRPO effectively injects task-specific reasoning abilities in a staged manner.

To further verify the generalizability of GRPO, we apply the same fine-tuning stages to Qwen2.5-3B, and report the results in Table [7](https://arxiv.org/html/2504.18776v2#S5.T7 "Table 7 ‣ 5.4. Ablation Study ‣ 5. Evaluation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").

Table 7. Ablation Study of Progressive GRPO (ThinkFL-Qwen2.5-3B)

|  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Dataset | Stage 1 | | | | Stage 2 | | | | Stage 3 | | | |
| R1 | R3 | R5 | MRR | R1 | R3 | R5 | MRR | R1 | R3 | R5 | MRR |
| 𝐀\mathbf{A} | 12.88 | 21.02 | 22.03 | 16.88 | 16.61 | 38.64 | 40.68 | 28.34 | 20.00 | 48.14 | 49.15 | 34.23 |
| 𝐁\mathbf{B} | 45.29 | 56.05 | 57.40 | 50.64 | 37.67 | 63.68 | 69.06 | 51.84 | 55.16 | 63.68 | 67.71 | 60.05 |
| 𝚪\mathbf{\Gamma} | 28.26 | 45.87 | 49.34 | 37.03 | 27.19 | 59.04 | 64.55 | 43.91 | 50.90 | 73.53 | 75.69 | 62.41 |
| 𝚫\mathbf{\Delta} | 38.06 | 55.16 | 61.63 | 47.59 | 35.45 | 59.54 | 72.26 | 50.85 | 55.16 | 67.88 | 74.97 | 63.04 |
| 𝐄\mathbf{E} | 15.64 | 36.78 | 40.75 | 26.23 | 20.70 | 46.04 | 54.85 | 35.68 | 26.65 | 49.56 | 54.85 | 39.04 |
| 𝐙\mathbf{Z} | 34.18 | 53.16 | 56.20 | 43.72 | 30.63 | 59.62 | 67.09 | 46.95 | 50.76 | 64.81 | 69.24 | 58.71 |

Here, ThinkFL-Qwen2.5-3B starts with an average MRR of 37.02% in Stage 1, which rises to 42.93% in Stage 2, and reaches 52.91% in Stage 3—resulting in an overall 15.89% relative improvement. The most impressive leap appears in Dataset 𝚪\mathbf{\Gamma}, where MRR increases from 37.03% to 62.41%.

These consistent gains across both model architectures demonstrate that our GRPO fine-tuning strategy is both effective and generalizable. Each stage gradually introduces more complex reasoning skills—from basic grounding in Stage 1, to multi-hop reasoning in Stage 2, and finally to full recursive optimization in Stage 3—resulting in a model that not only localizes failures more accurately but does so in a more structured and explainable manner.

### 5.5. Training Process Analysis

Among the three stages in the progressive multi-stage GRPO fine-tuning algorithm, Stage 2 (Guided Exploration Augmentation) plays the most crucial role in enhancing the exploratory ability of lightweight LLMs. To better understand its internal dynamics, we conduct an in-depth analysis of key metrics throughout the training process.

![Refer to caption](x10.png)

(a) Reward

![Refer to caption](x11.png)

(b) Response Length

Figure 9. Training Effects on Stage2 (Guided Exploration Augmentation)

As shown in Figure [9](https://arxiv.org/html/2504.18776v2#S5.F9 "Figure 9 ‣ 5.5. Training Process Analysis ‣ 5. Evaluation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"), both recall reward and diversity reward exhibit distinct trends. In Figure [9(a)](https://arxiv.org/html/2504.18776v2#S5.F9.sf1 "Figure 9(a) ‣ Figure 9 ‣ 5.5. Training Process Analysis ‣ 5. Evaluation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"), the recall reward rapidly rises from 0.35 to 0.55 in the early steps, followed by a sharp drop back to the initial level. This suggests that the model initially tends to overfit conservative patterns. However, within the next 100 steps, the recall reward quickly rebounds and stabilizes at around 0.75, indicating that the model gradually learns to balance exploration and accurate identification.

In contrast, the diversity reward increases more steadily and with a slight delay. It climbs from 0.3 to approximately 0.5 in the first 300 steps, followed by a sudden surge to around 0.7 within the next 100 steps. This ”slow-then-surge” pattern indicates that the model requires more time to effectively diversify its output, and that high diversity tends to emerge later in the training. Interestingly, this surge in diversity is not always beneficial—excessive diversity can dilute effective reasoning paths, which justifies the need for the final stage to constrain the output via ranking mechanisms.

We also track the length of the responses generated by ThinkFL at each step (response length), along with the combined length including tool call results (total length), as shown in Figure [9(b)](https://arxiv.org/html/2504.18776v2#S5.F9.sf2 "Figure 9(b) ‣ Figure 9 ‣ 5.5. Training Process Analysis ‣ 5. Evaluation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"). Both metrics grow steadily in the first 300 steps—reaching approximately 500 and 3000 characters, respectively—before experiencing rapid increases. This trend coincides with the diversity spike, confirming that increased diversity correlates with longer, more exploratory outputs.

Overall, our analysis reveals that Stage 2 is essential for equipping the model with diverse exploratory abilities, while also highlighting the importance of proper constraint mechanisms in Stage 3 to harness and refine this exploration toward effective failure localization.

### 5.6. LLM Backbone Comparison

To further validate the generality and robustness of ThinkFL, we apply the same fine-tuning procedure across various LLM backbones, including Qwen2.5-0.5B, Qwen2.5-3B, Llama3-8B, and Llama3.2-3B. The final MRR results on six evaluation tasks are summarized in Table [8](https://arxiv.org/html/2504.18776v2#S5.T8 "Table 8 ‣ 5.6. LLM Backbone Comparison ‣ 5. Evaluation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").

Table 8. Effectiveness of ThinkFL on Various LLMs

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Model | 𝐀\mathbf{A} | 𝐁\mathbf{B} | 𝚪\mathbf{\Gamma} | 𝚫\mathbf{\Delta} | 𝐄\mathbf{E} | 𝐙\mathbf{Z} |
| ThinkFL-Qwen2.5-0.5B | 32.52 | 50.56 | 32.68 | 55.52 | 34.34 | 38.38 |
| ThinkFL-Qwen2.5-3B | 34.23 | 60.05 | 62.41 | 63.04 | 39.04 | 58.71 |
| ThinkFL-Llama3-8B | 45.44 | 60.14 | 66.25 | 71.07 | 50.15 | 63.51 |
| ThinkFL-Llama3.2-3B | 54.44 | 67.13 | 68.26 | 71.05 | 51.48 | 65.22 |

From the results, we observe that while scaling up model size often brings performance gains, model size alone is not the sole determinant of effectiveness. For instance, despite being smaller, ThinkFL-Llama3.2-3B surpasses the larger Llama3-8B, highlighting that architectural refinements and instruction-tuning quality can outweigh sheer parameter count.

Nevertheless, a general scaling trend is evident when comparing Qwen2.5-0.5B to Qwen2.5-3B. The average MRR increases by 12.24% (from approximately 40.67% to 52.91%), with the most noticeable improvements in tasks Γ\Gamma and Δ\Delta, where MRR rises from 32.68% to 62.41% and from 55.52% to 63.04%, respectively. These results indicate that models around the 3B scale strike a strong balance between accuracy and parameter efficiency for failure localization.

Models from the Llama family further demonstrate robust performance. ThinkFL-Llama3-8B achieves an average MRR of approximately 59.43% across all tasks and stands out in tasks Γ\Gamma and 𝐙\mathbf{Z}, with scores of 66.25% and 63.51%—outperforming Qwen2.5-3B by 3.84% and 4.8%, respectively. This suggests that Llama-based models possess stronger reasoning and multi-step planning capabilities.

Finally, ThinkFL-Llama3.2-3B achieves the highest overall performance with an average MRR of approximately 62.93%, outperforming its larger counterpart Llama3-8B by 3.50%. Notably, it delivers significant gains on task 𝐀\mathbf{A} (54.44% vs. 45.44%) and task 𝐄\mathbf{E} (51.48% vs. 50.15%). This exception underscores that model architecture refinements and instruction-tuning quality, as exemplified by Llama3.2, can play a decisive role. Such findings make Llama3.2-3B particularly attractive for real-world deployments, where computational efficiency is as critical as accuracy.

### 5.7. Case Study

To better understand why ThinkFL achieves improved failure localization performance after self-refinement, we present a case study comparing its reasoning paths before and after the full progressive training pipeline.

As illustrated in Figure [10](https://arxiv.org/html/2504.18776v2#S5.F10 "Figure 10 ‣ 5.7. Case Study ‣ 5. Evaluation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"), we examine two reasoning trajectories generated by ThinkFL for the same failure event with the root trace ID 9ef42cab5049f52e. The left side depicts the output of ThinkFL trained only with Stage 1 (format-aware policy priming), while the right shows the behavior after completing the full self-refinement process (Stage 2 and Stage 3).

![Refer to caption](x12.png)


Figure 10. Case Study: Reasoning Path Comparison before and after Self-Refinement

In the Stage 1 setting, ThinkFL detects an initial abnormal sub-call b54bde8fabf0f139 and proceeds to follow its downstream chain. It then identifies another abnormal call 487ca8682f64d792, but eventually reaches a normal sub-call 9f340db2a4bc0be5. Based on this limited exploration, it concludes that the root cause likely lies in Service-A, to which 487ca8682f64d792 belongs.

In contrast, the self-refined ThinkFL exhibits significantly broader exploration behavior. Instead of strictly following a single path, it also investigates two sibling sub-calls: 72e2534801a08aca and 8b89497416d1cb92, both of which belong to Service-B. Since these traces form abnormal chains within the same service, ThinkFL aggregates information from both Service-A and Service-B, including relevant metrics, to form a more holistic judgment. It ultimately attributes the failure to Service-B — the ground-truth root cause.

This comparison clearly demonstrates ThinkFL’s enhanced capability to localize failures more accurately after undergoing self-refinement. The model’s ability to escape early-stage greedy search and explore alternative hypotheses not only improves the reasoning depth but also leads to better coverage of plausible failure paths. It is worth noting that this ability to perform diversified and metric-grounded exploration is also one of the key reasons why ThinkFL outperforms even significantly larger models such as Claude-3.5-Sonnet in our evaluations.

Although ThinkFL has made significant progress after Progressive Multi-Stage GRPO Fine-Tuning, there still exist cases where it fails to accurately localize failures. As shown in Figure [11](https://arxiv.org/html/2504.18776v2#S5.F11 "Figure 11 ‣ 5.7. Case Study ‣ 5. Evaluation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"), this example involves a relatively simple trace, where all anomalies can be traced back to the CurrencyService. Ideally, the model only needs to query the metrics of CurrencyService to confirm the root cause. However, upon inspection, all three related pods—currencyservice-0, currencyservice-1, and currencyservice-2—exhibited abnormal fluctuations. In this situation, ThinkFL found it difficult to interpret the metrics and distinguish which pod was the true source of the failure. Across multiple reasoning attempts, the model produced different predictions, with most of them being incorrect.

![Refer to caption](x13.png)


Figure 11. Case Study of a Failed Failure Localization

This example indicates that ThinkFL’s current limitation lies not in its ability to follow structured reasoning, but in its insufficient understanding of performance metrics when multiple components exhibit correlated anomalies. Enhancing the model’s capability to interpret metric and differentiate between correlated and causal anomalies will be an important avenue for future improvement.

### 5.8. Hyperparameter Analysis

Among all hyperparameters, the most critical one is the maximum dialogue depth DmaxD\_{\text{max}}, which controls the depth of the model’s exploration process. To understand its impact, we conduct experiments on the 𝚫\mathbf{\Delta} dataset — a medium-difficulty benchmark — by varying DmaxD\_{\text{max}} and evaluating its effect on failure localization performance.

![Refer to caption](x14.png)

(a) ThinkFL-Llama3.2-3B

![Refer to caption](x15.png)

(b) ThinkFL-Qwen2.5-3B

Figure 12. Hyperparameter Experiment of Dm​a​xD\_{max}

As shown in Figure [12](https://arxiv.org/html/2504.18776v2#S5.F12 "Figure 12 ‣ 5.8. Hyperparameter Analysis ‣ 5. Evaluation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"), increasing DmaxD\_{\text{max}} generally leads to improved failure localization performance, but the improvement eventually plateaus.

For ThinkFL-Llama3.2-3B (Figure [12(a)](https://arxiv.org/html/2504.18776v2#S5.F12.sf1 "Figure 12(a) ‣ Figure 12 ‣ 5.8. Hyperparameter Analysis ‣ 5. Evaluation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning")), we observe a substantial performance gain when increasing DmaxD\_{\text{max}} from 1 to 4, achieving a 62.09% improvement in MRR. Beyond Dmax=4D\_{\text{max}}=4, the gain continues but at a slower rate, with an additional 5.71% improvement from Dmax=4D\_{\text{max}}=4 to 1010. This suggests that deeper dialogue depths can still contribute marginal improvements, especially for more capable backbones like Llama3.2-3B, which benefit from extended reasoning chains.

In contrast, ThinkFL-Qwen2.5-3B (Figure [12(b)](https://arxiv.org/html/2504.18776v2#S5.F12.sf2 "Figure 12(b) ‣ Figure 12 ‣ 5.8. Hyperparameter Analysis ‣ 5. Evaluation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning")) reaches its peak performance much earlier. The MRR increases by 31.81% from Dmax=1D\_{\text{max}}=1 to 22, but further increases in dialogue depth offer little to no improvement. This indicates that Qwen2.5-3B may struggle to fully utilize deeper multi-hop reasoning, possibly due to its architectural or training limitations.

These results suggest that while increasing DmaxD\_{\text{max}} is generally beneficial, the optimal value depends heavily on the backbone’s reasoning capacity. For lighter or less structured models, shallower dialogues may suffice, whereas more powerful models can leverage longer reasoning paths to refine their localization hypotheses more effectively.

### 5.9. Generalizability Evaluation

To evaluate ThinkFL’s generalizability to other microservice systems, we applied it to the Train-Ticket system111https://github.com/FudanSELab/train-ticket, which we manually set up with 41 microservices and injected 10 types of faults to simulate failures. Notably, ThinkFL was used directly without any retraining on this system.

Table 9. Failure Localization Results in Train-Ticket

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Method | R​e​c​a​l​l​@​1Recall@1 | R​e​c​a​l​l​@​2Recall@2 | R​e​c​a​l​l​@​3Recall@3 | R​e​c​a​l​l​@​5Recall@5 | R​e​c​a​l​l​@​10Recall@10 | M​R​RMRR |
| RCAgent | 41.33 | 51.75 | 58.13 | 64.97 | 73.17 | 59.18 |
| mABC | 44.89 | 54.97 | 59.88 | 68.12 | 75.32 | 61.33 |
| ThinkFL (ours) | 61.23 | 71.30 | 73.26 | 81.25 | 87.67 | 76.32 |

As shown in Table [9](https://arxiv.org/html/2504.18776v2#S5.T9 "Table 9 ‣ 5.9. Generalizability Evaluation ‣ 5. Evaluation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"), ThinkFL substantially outperforms the baselines. For instance, its R​e​c​a​l​l​@​1Recall@1 of 61.23% is 16.34 points higher than mABC (44.89%) and 19.90 points higher than RCAgent (41.33%). Similarly, the mean reciprocal rank (MRR) of ThinkFL reaches 76.32, which represents an improvement of 15.0–17.1 points over the baselines. Across other metrics (R​e​c​a​l​l​@​2Recall@2, R​e​c​a​l​l​@​3Recall@3, R​e​c​a​l​l​@​5Recall@5, R​e​c​a​l​l​@​10Recall@10), ThinkFL consistently shows gains of 10–15 percentage points, highlighting its ability to accurately identify root causes in an unseen microservice system.

These results indicate that the model trained via Progressive Multi-Stage GRPO Fine-Tuning generalizes effectively to an environment with different services, architectures, and fault patterns. Importantly, ThinkFL achieves this performance without any system-specific retraining, demonstrating its robustness and practical applicability in diverse operational settings.

## 6. Discussion

### 6.1. Distinction Between Research Evaluation and Practical Usage

Our evaluation isolates the technical capabilities of ThinkFL, whereas real-world failure diagnosis is fundamentally a human-in-the-loop process. In practice, SREs interpret model outputs, validate evidence, and decide on remediation actions. While our experiments do not measure these human interactions, they assess the core technical abilities required for practical deployment: correct tool invocation, structured reasoning generation, and accurate root-cause identification at multiple granularities.

The goal of this work is the research contribution—advancing the reasoning ability of lightweight LLMs through Progressive Multi-Stage GRPO Fine-Tuning, including the Recursion-of-Thought framework and format-aware policy priming. Accordingly, our evaluation focuses on controlled technical metrics rather than end-to-end incident-management workflows.

In operational use, ThinkFL is intended as an assistive system: it produces interpretable reasoning traces and ranked candidate root causes that SREs can verify and act upon. The structured outputs provide transparent evidence that supports faster confirmation and remediation. To partially verify this practical utility, we conducted a small-scale, informal study by presenting selected interpretable reasoning paths and predictions to professional developers and SREs. They reported that these interpretable traces improved their understanding of the diagnostic process and helped them reach resolutions more quickly. This preliminary check suggests practical promise, although a systematic evaluation with a larger SRE cohort and real incident-management scenarios remains future work due to resource constraints.

### 6.2. Dependence on Microservice Characteristics and Potential Extension

ThinkFL is designed around microservice observability, where spans, traces, and metrics provide rich structured signals for reasoning. These signals enable ThinkFL to trace request propagation, correlate anomalies with service- or pod-level behavior, and generate interpretable Recursion-of-Thought (RoT) reasoning chains. Thus, its current performance naturally benefits from characteristics inherent to microservice architectures.

Our evaluation on the Train-Ticket benchmark (41 services, 10 injected failures) further reflects this dependency. ThinkFL performs well on this dataset partly because its failures are simpler and more localized than those in AIOPS 2022. This demonstrates both its generalizability across microservice systems and its sensitivity to system scale and fault complexity.

Nevertheless, ThinkFL is not fundamentally limited to microservices. Its design consists of three modular layers—(i) a trace abstraction layer, (ii) a metrics integration layer, and (iii) a reasoning/localization layer—only the first two of which are domain-specific. By redefining the trace abstraction and mapping metrics to domain-specific signals, ThinkFL’s reasoning layer can operate unchanged.

In summary, ThinkFL’s success stems from microservice-aligned observability, but its modular structure enables extension to other distributed systems as long as comparable structured traces and metrics can be provided.

### 6.3. Handling Context Window Limitations in Recursive Analysis

A natural concern regarding ThinkFL lies in whether recursive tool invocations and long traces might cause the accumulated context to exceed the LLM’s window size. We acknowledge that such situations could theoretically occur; however, our framework was explicitly designed with this constraint in mind. Instead of passing the entire raw trace into the model at once, ThinkFL performs iterative querying: at each step, only the necessary fragment of the trace is retrieved and fed into the model. This design keeps the effective context size small and manageable.

In practice, the traces in the AIOPS 2022 dataset contain at most five levels of depth. Consequently, during our experiments, we did not encounter cases where the accumulated trace length exceeded the model’s context window. Nevertheless, to further safeguard against excessive recursive queries, we impose a maximum reasoning depth of 20 tool-invocation rounds. If this limit is reached, ThinkFL terminates the exploration process and produces a final root cause judgment based on the available information. This mechanism ensures that ThinkFL remains both context-efficient and robust, even under scenarios with potentially large or repetitive traces.

### 6.4. Practical Implications for SREs

We acknowledge the concern regarding the effort and resources required to deploy ThinkFL. In practice, training and inference only require lightweight resources—e.g., several consumer-grade GPUs such as NVIDIA RTX 4090 are sufficient for the 3B-parameter backbone—making the computational cost manageable compared to large-scale LLMs.

Before training ThinkFL, we manually verified that advanced models (e.g., Claude-3.5) can generate correct tool-invocation sequences and reasoning chains for some failure localization cases. While these models occasionally produce incomplete reasoning or incorrect conclusions, we selected only correctly solved cases during the supervised fine-tuning (SFT) phase. As a result, ThinkFL can learn accurate reasoning patterns from advanced models, reducing the need for extensive manual annotations by SREs.

From the SRE perspective, ThinkFL does not introduce heavy additional workload. Recording new cases for incremental improvement requires only lightweight annotations (e.g., timestamp + root cause), which aligns with routine incident reporting. Moreover, since ThinkFL produces interpretable reasoning paths, its outputs remain useful even when imperfect, helping to reduce investigation overhead and accelerate failure triage. Overall, the combination of manageable GPU cost, minimal annotation requirements, and training data largely sourced from verified advanced model outputs makes the solution practically satisfactory for operators.

### 6.5. Limitations and Threats to Validity

Despite the promising results demonstrated by ThinkFL, several limitations and potential threats to validity should be acknowledged:

Implementation of Baselines. While we directly used publicly available source code for CRISP, MicroRank, and mABC, other baseline methods were re-implemented based on the descriptions provided in their respective papers. To ensure faithful reproduction, we carefully followed the algorithmic details, hyperparameter settings, and experimental protocols whenever available. For methods lacking released code or complete configuration details, we acknowledge that our implementations may deviate slightly from the originals. To mitigate this risk, multiple members of our research team independently reviewed and cross-checked the re-implemented code to ensure correctness and consistency.

Reliance on OpenRLHF. Our method is implemented based on the OpenRLHF framework, which provides a general foundation for reinforcement learning with LLMs. While we made necessary adaptations for our setting, there is a possibility that some default configurations in the framework—if not fully aligned with our objectives—could affect the final training performance. To mitigate this, we invited multiple domain experts to review our implementation in detail and ensure correctness and consistency.

Simplified Failure Definition. ThinkFL focuses exclusively on failure localization and does not include an anomaly detection component. Therefore, our definition of a failure is simplified: any request whose latency exceeds 100 times the normal threshold is considered anomalous. While this heuristic helps reduce false positives and ensures consistency in our evaluation, it may miss subtler forms of failure or introduce labeling noise.

## 7. Related Work

### 7.1. Root Cause Localization

Root cause localization is a fundamental component of failure management, aiming to identify the services, components, or operations responsible for system anomalies. Existing approaches can be broadly categorized into two types: ML/DL-based methods and LLM-based methods.

ML/DL-based Methods.
Traditional machine learning and deep learning approaches form the foundation of prior research on failure localization. These methods typically learn correlations, dependencies, or causal relationships from system telemetry—such as KPIs, logs, and traces—to identify abnormal components.

A large body of work focuses on analyzing system-level KPIs. Approaches such as LOUD (Mariani et al., [2018](https://arxiv.org/html/2504.18776v2#bib.bib56 "Localizing faults in cloud systems")), AID (Yang et al., [2021](https://arxiv.org/html/2504.18776v2#bib.bib57 "AID: efficient prediction of aggregated intensity of dependency in large-scale cloud systems")), and CloudScout (Yin et al., [2016](https://arxiv.org/html/2504.18776v2#bib.bib58 "Cloudscout: a non-intrusive approach to service dependency discovery")) construct correlation graphs or compute similarity measures over KPIs (e.g., CPU, memory, disk I/O) to infer faulty services. More advanced techniques integrate causality analysis or forecasting, including CIRCA (Li et al., [2022b](https://arxiv.org/html/2504.18776v2#bib.bib2 "Causal inference-based root cause analysis for online service systems with intervention recognition")), RUN (Lin et al., [2024](https://arxiv.org/html/2504.18776v2#bib.bib8 "Root cause analysis in microservice using neural granger causal discovery")), and KPIRoot (Gu et al., [2024](https://arxiv.org/html/2504.18776v2#bib.bib59 "KPIRoot: efficient monitoring metric-based root cause localization in large-scale cloud systems")), which leverage Bayesian networks, neural Granger causality, or symbolic KPI encoding for improved root cause ranking. Other methods target high-dimensional KPI attributes, such as CMMD (Yan et al., [2022](https://arxiv.org/html/2504.18776v2#bib.bib60 "Cmmd: cross-metric multi-dimensional root cause analysis")), HALO (Zhang et al., [2021](https://arxiv.org/html/2504.18776v2#bib.bib61 "Halo: hierarchy-aware fault localization for cloud systems")), iDice (Lin et al., [2016](https://arxiv.org/html/2504.18776v2#bib.bib62 "IDice: problem identification for emerging issues")), and MID (Gu et al., [2020](https://arxiv.org/html/2504.18776v2#bib.bib63 "Efficient incident identification from multi-dimensional issue reports via meta-heuristic search")), which use graph attention, conditional entropy, statistical scoring, or meta-heuristic search to identify fault-indicating metric combinations.

In parallel, another line of work analyzes distributed traces to capture end-to-end service interactions. Early efforts (Li et al., [2022a](https://arxiv.org/html/2504.18776v2#bib.bib26 "Enjoy your observability: an industrial survey of microservice tracing and analysis"); Luo et al., [2021](https://arxiv.org/html/2504.18776v2#bib.bib53 "Characterizing microservice dependency and performance: alibaba trace analysis")) demonstrated the diagnostic value of trace structures. Subsequent learning-based techniques—such as MEPFL (Zhou et al., [2019](https://arxiv.org/html/2504.18776v2#bib.bib27 "Latent error prediction and fault localization for microservice applications by learning from system trace logs")), Seer (Gan et al., [2019](https://arxiv.org/html/2504.18776v2#bib.bib28 "Seer: leveraging big data to navigate the complexity of performance debugging in cloud microservices")), TraceAnomaly (Liu et al., [2020](https://arxiv.org/html/2504.18776v2#bib.bib29 "Unsupervised detection of microservice trace anomalies through service-level deep bayesian networks")), and Sage (Gan et al., [2021](https://arxiv.org/html/2504.18776v2#bib.bib30 "Sage: practical and scalable ml-driven performance debugging in microservices"))—apply supervised or unsupervised models, including CNNs, LSTMs, and GNNs, to detect anomalies and infer faulty components from trace patterns.

To improve interpretability and reduce reliance on large training datasets, spectrum-based methods have also been widely explored. MicroRank (Yu et al., [2021](https://arxiv.org/html/2504.18776v2#bib.bib6 "Microrank: end-to-end latency issue localization with extended spectrum analysis in microservice environments")), TraceRank (Yu et al., [2023b](https://arxiv.org/html/2504.18776v2#bib.bib5 "TraceRank: abnormal service localization with dis-aggregated end-to-end tracing data in cloud native systems")), and the method of Li et al. (Li et al., [2021](https://arxiv.org/html/2504.18776v2#bib.bib13 "Practical root cause localization for microservice systems via trace analysis")) compute suspiciousness scores based on trace evidence, while TraceConstract (Zhang et al., [2024a](https://arxiv.org/html/2504.18776v2#bib.bib4 "Trace-based multi-dimensional root cause localization of performance issues in microservice systems")) integrates sequence modeling with contrast pattern mining to localize complex multi-dimensional root causes.

Several human-in-the-loop approaches further incorporate SRE feedback to guide or refine the localization process. HRLHF (Wang et al., [2023](https://arxiv.org/html/2504.18776v2#bib.bib122 "Root cause analysis for microservice systems via hierarchical reinforcement learning from human feedback")), HiLogX (Jia et al., [2024](https://arxiv.org/html/2504.18776v2#bib.bib123 "Hilogx: noise-aware log-based anomaly detection with human feedback")), and HiLog (Jia et al., [2022](https://arxiv.org/html/2504.18776v2#bib.bib124 "Augmenting log-based anomaly detection models to reduce false anomalies with human feedback")) leverage expert annotations or interaction signals to improve dependency inference or log-based anomaly detection.

Despite their diversity, these ML/DL-based techniques share common limitations: they rely on predefined causal graphs, fixed statistical assumptions, or models trained on historical data. As a result, they often require substantial feature engineering, retraining, or manual updates when system behaviors evolve, and may struggle to generalize to previously unseen failure patterns.

LLM-based Methods.
Recent work applies large language models to failure localization, leveraging their ability to conduct flexible and interpretable reasoning over heterogeneous operational data. Existing approaches can be broadly grouped into two categories: tool-augmented single-agent systems and LLM-based multi-agent frameworks.

The first category consists of tool-augmented single-agent systems, where an LLM is equipped with domain-specific tools that preprocess, filter, or reconstruct diagnostic context before reasoning. Representative examples include RCAgent (Wang et al., [2024b](https://arxiv.org/html/2504.18776v2#bib.bib44 "Rcagent: cloud root cause analysis by autonomous agents with tool-augmented large language models")), which integrates log and code analysis tools to support tasks such as predicting root causes and gathering evidence; COCA (Li et al., [2025b](https://arxiv.org/html/2504.18776v2#bib.bib101 "COCA: generative root cause analysis for distributed systems with code knowledge")), which enhances issue-report analysis by extracting relevant code snippets and reconstructing execution paths; and TAMO (Wang et al., [2025](https://arxiv.org/html/2504.18776v2#bib.bib102 "TAMO: fine-grained root cause analysis via tool-assisted llm agent with multi-modality observation data in cloud-native systems")), which unifies multi-modal operational signals into time-aligned representations and incorporates specialized tools for component-level localization.

The second category comprises LLM-based multi-agent frameworks, where multiple agents collaborate through structured workflows. Flow-of-Action (Pei et al., [2025](https://arxiv.org/html/2504.18776v2#bib.bib100 "Flow-of-action: sop enhanced llm-based multi-agent system for root cause analysis")) introduces an SOP-enhanced architecture in which procedural knowledge constrains LLM decisions at key junctures, ensuring a more reliable diagnostic trajectory. mABC (Zhang et al., [2024e](https://arxiv.org/html/2504.18776v2#bib.bib24 "MABC: multi-agent blockchain-inspired collaboration for root cause analysis in micro-services architecture")) coordinates agents via workflow rules and voting-based consensus, while KnowledgeMind (Ren, [2025](https://arxiv.org/html/2504.18776v2#bib.bib104 "The multi-agent fault localization system based on monte carlo tree search approach")) employs Monte Carlo Tree Search and a knowledge-base reward mechanism to support standardized, service-by-service reasoning.

Although these approaches improve interpretability and incorporate valuable domain knowledge, they lack the self-iterative reasoning capability of ThinkFL and often struggle to precisely localize the true root-cause components when diagnostic context must be dynamically constructed rather than statically preprocessed.

### 7.2. LLM-based Failure Management

Large language models, with their strong semantic comprehension and reasoning capabilities, have shown great potential in advancing various aspects of failure management (Zhang et al., [2025a](https://arxiv.org/html/2504.18776v2#bib.bib17 "A survey of aiops in the era of large language models")). Recent studies have leveraged LLMs to improve anomaly detection, failure diagnosis, and automated remediation. These efforts can be broadly classified into three categories: foundation models, fine-tuning-based approaches, and prompt-based methods.

Foundation Models.
Several studies aim to build foundation models specifically designed for time-series or log data. Lag-Llama (Rasul et al., [2023](https://arxiv.org/html/2504.18776v2#bib.bib31 "Lag-llama: towards foundation models for time series forecasting")) pretrains a decoder-only transformer for univariate forecasting by modeling lag-based covariates. Timer (Liu et al., [2024f](https://arxiv.org/html/2504.18776v2#bib.bib33 "Timer: generative pre-trained transformers are large time series models")) develops a GPT-style model that unifies forecasting, imputation, and anomaly detection for long-term sequences. TimesFM (Das et al., [2024](https://arxiv.org/html/2504.18776v2#bib.bib32 "A decoder-only foundation model for time-series forecasting")) proposes a patched-decoder attention architecture to handle diverse forecasting lengths and granularities. For command-line automation, ShellGPT (Shi et al., [2023](https://arxiv.org/html/2504.18776v2#bib.bib34 "Shellgpt: generative pre-trained transformer model for shell language understanding")) incorporates shell scripting semantics into the GPT framework. TimeGPT (Liao et al., [2024](https://arxiv.org/html/2504.18776v2#bib.bib64 "TimeGPT in load forecasting: a large time series model perspective")) and SimMTM (Dong et al., [2024](https://arxiv.org/html/2504.18776v2#bib.bib65 "Simmtm: a simple pre-training framework for masked time-series modeling")) adopt encoder-decoder structures for reconstructing time-series patterns from massive datasets. In the log domain, PreLog (Le and Zhang, [2024](https://arxiv.org/html/2504.18776v2#bib.bib66 "PreLog: a pre-trained model for log analytics")) uses hierarchical objectives to enable pretraining for both log parsing and anomaly detection. KAD-Disformer (Yu et al., [2024](https://arxiv.org/html/2504.18776v2#bib.bib67 "Pre-trained kpi anomaly detection model through disentangled transformer")) further disentangles temporal and spatial dynamics to enhance detection performance in multivariate metrics data.

Fine-Tuning-Based Approaches.
Fine-tuning general-purpose LLMs on domain-specific tasks is another common strategy. UniTime (Liu et al., [2024c](https://arxiv.org/html/2504.18776v2#bib.bib38 "Unitime: a language-empowered unified model for cross-domain time series forecasting")) fine-tunes GPT-2 for unified time-series forecasting across domains. AnomalyLLM (Liu et al., [2024b](https://arxiv.org/html/2504.18776v2#bib.bib37 "Anomalyllm: few-shot anomaly edge detection for dynamic graphs using large language models")) applies contrastive fine-tuning on LLaMA2-7B for graph-based anomaly detection. PromptCast (Xue and Salim, [2023](https://arxiv.org/html/2504.18776v2#bib.bib68 "Promptcast: a new prompt-based learning paradigm for time series forecasting")) adapts T5 and BART via task-oriented fine-tuning to support text-visible time-series forecasting. RAG4ITOps (Zhang et al., [2024c](https://arxiv.org/html/2504.18776v2#bib.bib69 "RAG4ITOps: a supervised fine-tunable and comprehensive rag framework for it operations and maintenance")) applies retrieval-augmented fine-tuning on Qwen-14B for interactive failure diagnosis. OWL (Guo et al., [2023](https://arxiv.org/html/2504.18776v2#bib.bib35 "Owl: a large language model for it operations")) fine-tunes LLaMA2-13B using adapter modules for assisted troubleshooting and log anomaly detection. Similarly, LLM4TS (Chang et al., [2023](https://arxiv.org/html/2504.18776v2#bib.bib70 "Llm4ts: two-stage fine-tuning for time-series forecasting with pre-trained llms")) freezes most GPT-2 parameters while tuning a small subset for forecasting tasks. LogLM (Liu et al., [2024d](https://arxiv.org/html/2504.18776v2#bib.bib36 "Loglm: from task-based to instruction-based automated log analysis")) introduces instruction-based fine-tuning on LLaMA2-7B to support multi-task log analytics, including parsing and detection.

Prompt-Based Methods.
Prompt-based methods avoid the cost of full fine-tuning by leveraging LLMs through instruction design. RCACopilot (Chen et al., [2024](https://arxiv.org/html/2504.18776v2#bib.bib39 "Automatic root cause analysis via large language models for cloud incidents")) and Xpert (Jiang et al., [2024](https://arxiv.org/html/2504.18776v2#bib.bib54 "Xpert: empowering incident management with query recommendations via large language models")) use in-context learning (ICL) to structure multi-step diagnostic reasoning. LasRCA (Han et al., [2024](https://arxiv.org/html/2504.18776v2#bib.bib71 "The potential of one-shot failure root cause analysis: collaboration of the large language model and small classifier")) employs one-shot prompting with auxiliary classifiers to improve anomaly detection on metrics. LSTPrompt (Liu et al., [2024a](https://arxiv.org/html/2504.18776v2#bib.bib72 "LSTPrompt: large language models as zero-shot time series forecasters by long-short-term prompting")) decomposes prediction into short- and long-term subtasks using chain-of-thought (CoT) prompting. LogGPT (Liu et al., [2024e](https://arxiv.org/html/2504.18776v2#bib.bib73 "Interpretable online log analysis using large language models with prompt strategies")) enhances log anomaly detection via step-wise CoT generation. LM-PACE (Zhang et al., [2024b](https://arxiv.org/html/2504.18776v2#bib.bib40 "LM-pace: confidence estimation by large language models for effective root causing of cloud incidents")) further strengthens diagnostic interpretability by prompting GPT-4 to analyze incident reports. Retrieval-augmented methods such as RAGLog (Pan et al., [2024](https://arxiv.org/html/2504.18776v2#bib.bib74 "Raglog: log anomaly detection using retrieval augmented generation")), LogRAG (Zhang et al., [2024d](https://arxiv.org/html/2504.18776v2#bib.bib43 "LogRAG: semi-supervised log-based anomaly detection with retrieval-augmented generation")) enhance log-based anomaly detection by retrieving and incorporating historical case logs into the prompt context. ThinkRemed (Zhang et al., [2025c](https://arxiv.org/html/2504.18776v2#bib.bib134 "MicroRemed: benchmarking llms in microservices remediation")) employs a multi-agent framework to address microservice remediation.

## 8. Conclusion

In this paper, we address the limitations of existing LLM-based failure localization methods, such as rigid invocation workflows and resource-intensive inference. To overcome these challenges, we explore the use of reinforcement fine-tuning to endow lightweight LLMs with reasoning and self-refinement capabilities, thereby enhancing the cost-effectiveness and adaptability of LLM-based failure localization in real-world applications.

To this end, we first conduct an empirical study and identify three core capabilities essential for effective failure localization. Based on these insights, we propose a progressive multi-stage GRPO fine-tuning framework, which incorporates a multi-factor failure localization grader and a resursion-of-thought actor. The resulting model, ThinkFL, not only surpasses all existing state-of-the-art LLMs and methods in localization accuracy, but also significantly reduces localization latency from minutes to seconds.

In future work, we plan to investigate whether such reasoning-capable models can be extended beyond accurate failure localization to achieve automated recovery in runtime microservice systems.

## 9. Data Availability

The training code, which is based on OpenRLHF (Hu et al., [2024](https://arxiv.org/html/2504.18776v2#bib.bib52 "Openrlhf: an easy-to-use, scalable and high-performance rlhf framework")), is publicly available at <https://github.com/LLM4AIOps/OpenRLHF-ThinkFL>. In addition, we implemented an alternative training version based on AgentEvolver (Zhai et al., [2025](https://arxiv.org/html/2504.18776v2#bib.bib132 "AgentEvolver: towards efficient self-evolving agent system")), which is available at <https://github.com/modelscope/AgentEvolver>. The fine-tuned model weights are publicly released on ModelScope222ModelScope links: <https://modelscope.cn/models/ZhangLingzhe/ThinkFL-Qwen2.5-0.5B>, <https://modelscope.cn/models/ZhangLingzhe/ThinkFL-Qwen2.5-3B>, <https://modelscope.cn/models/ZhangLingzhe/ThinkFL-Llama3.2-3B>, <https://modelscope.cn/models/ZhangLingzhe/ThinkFL-Llama3-8B>. and Hugging Face333Hugging Face links: <https://huggingface.co/Zhang-Lingzhe/ThinkFL-Qwen2.5-0.5B>, <https://huggingface.co/Zhang-Lingzhe/ThinkFL-Qwen2.5-3B>, <https://huggingface.co/Zhang-Lingzhe/ThinkFL-Llama3.2-3B>, <https://huggingface.co/Zhang-Lingzhe/ThinkFL-Llama3-8B>..

###### Acknowledgements.

This work is supported by Key-Area Research and Development Program of Guangdong Province, China (NO.2020B010164003).

## References

* A. Amini, T. Vieira, and R. Cotterell (2024)
  Direct preference optimization with an offset.
  arXiv preprint arXiv:2402.10571.
  Cited by: [§2.4](https://arxiv.org/html/2504.18776v2#S2.SS4.p12.1 "2.4. Reinforcement Fine-Tuning ‣ 2. Background & Motivation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* B. Beyer, N. R. Murphy, D. K. Rensin, K. Kawahara, and S. Thorne (2018)
  The site reliability workbook: practical ways to implement sre.
   ” O’Reilly Media, Inc.”.
  Cited by: [§1](https://arxiv.org/html/2504.18776v2#S1.p4.1 "1. Introduction ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* C. Chang, W. Peng, and T. Chen (2023)
  Llm4ts: two-stage fine-tuning for time-series forecasting with pre-trained llms.
  arXiv preprint arXiv:2308.08469.
  Cited by: [§7.2](https://arxiv.org/html/2504.18776v2#S7.SS2.p3.1 "7.2. LLM-based Failure Management ‣ 7. Related Work ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* Y. Chen, H. Xie, M. Ma, Y. Kang, X. Gao, L. Shi, Y. Cao, X. Gao, H. Fan, M. Wen, et al. (2024)
  Automatic root cause analysis via large language models for cloud incidents.
  In Proceedings of the Nineteenth European Conference on Computer Systems,
   pp. 674–688.
  Cited by: [§7.2](https://arxiv.org/html/2504.18776v2#S7.SS2.p4.1 "7.2. LLM-based Failure Management ‣ 7. Related Work ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* P. F. Christiano, J. Leike, T. Brown, M. Martic, S. Legg, and D. Amodei (2017)
  Deep reinforcement learning from human preferences.
  Advances in neural information processing systems 30.
  Cited by: [§2.4](https://arxiv.org/html/2504.18776v2#S2.SS4.p1.1 "2.4. Reinforcement Fine-Tuning ‣ 2. Background & Motivation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* A. Das, W. Kong, R. Sen, and Y. Zhou (2024)
  A decoder-only foundation model for time-series forecasting.
  In Forty-first International Conference on Machine Learning,
  Cited by: [§7.2](https://arxiv.org/html/2504.18776v2#S7.SS2.p2.1 "7.2. LLM-based Failure Management ‣ 7. Related Work ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* J. Dong, H. Wu, H. Zhang, L. Zhang, J. Wang, and M. Long (2024)
  Simmtm: a simple pre-training framework for masked time-series modeling.
  Advances in Neural Information Processing Systems 36.
  Cited by: [§7.2](https://arxiv.org/html/2504.18776v2#S7.SS2.p2.1 "7.2. LLM-based Failure Management ‣ 7. Related Work ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* A. Dubey, A. Jauhri, A. Pandey, A. Kadian, A. Al-Dahle, A. Letman, A. Mathur, A. Schelten, A. Yang, A. Fan, et al. (2024)
  The llama 3 herd of models.
  arXiv e-prints,  pp. arXiv–2407.
  Cited by: [§1](https://arxiv.org/html/2504.18776v2#S1.p7.1 "1. Introduction ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* S. Feng, G. Fang, X. Ma, and X. Wang (2025)
  Efficient reasoning models: a survey.
  arXiv preprint arXiv:2504.10903.
  Cited by: [§3.1](https://arxiv.org/html/2504.18776v2#S3.SS1.p1.1 "3.1. Capability of SOTA Lightweight LLMs ‣ 3. Empirical Study ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* Y. Gan, M. Liang, S. Dev, D. Lo, and C. Delimitrou (2021)
  Sage: practical and scalable ml-driven performance debugging in microservices.
  In Proceedings of the 26th ACM International Conference on Architectural Support for Programming Languages and Operating Systems,
   pp. 135–151.
  Cited by: [§7.1](https://arxiv.org/html/2504.18776v2#S7.SS1.p4.1 "7.1. Root Cause Localization ‣ 7. Related Work ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* Y. Gan, Y. Zhang, K. Hu, D. Cheng, Y. He, M. Pancholi, and C. Delimitrou (2019)
  Seer: leveraging big data to navigate the complexity of performance debugging in cloud microservices.
  In Proceedings of the twenty-fourth international conference on architectural support for programming languages and operating systems,
   pp. 19–33.
  Cited by: [§7.1](https://arxiv.org/html/2504.18776v2#S7.SS1.p4.1 "7.1. Root Cause Localization ‣ 7. Related Work ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* J. Gu, C. Luo, S. Qin, B. Qiao, Q. Lin, H. Zhang, Z. Li, Y. Dang, S. Cai, W. Wu, et al. (2020)
  Efficient incident identification from multi-dimensional issue reports via meta-heuristic search.
  In Proceedings of the 28th ACM Joint Meeting on European Software Engineering Conference and Symposium on the Foundations of Software Engineering,
   pp. 292–303.
  Cited by: [§7.1](https://arxiv.org/html/2504.18776v2#S7.SS1.p3.1 "7.1. Root Cause Localization ‣ 7. Related Work ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* W. Gu, X. Sun, J. Liu, Y. Huo, Z. Chen, J. Zhang, J. Gu, Y. Yang, and M. R. Lyu (2024)
  KPIRoot: efficient monitoring metric-based root cause localization in large-scale cloud systems.
  In 2024 IEEE 35th International Symposium on Software Reliability Engineering (ISSRE),
   pp. 403–414.
  Cited by: [§7.1](https://arxiv.org/html/2504.18776v2#S7.SS1.p3.1 "7.1. Root Cause Localization ‣ 7. Related Work ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* D. Guo, D. Yang, H. Zhang, J. Song, R. Zhang, R. Xu, Q. Zhu, S. Ma, P. Wang, X. Bi, et al. (2025)
  Deepseek-r1: incentivizing reasoning capability in llms via reinforcement learning.
  arXiv preprint arXiv:2501.12948.
  Cited by: [§3.2](https://arxiv.org/html/2504.18776v2#S3.SS2.p1.2 "3.2. Direct Application of GRPO Algorithm ‣ 3. Empirical Study ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* H. Guo, J. Yang, J. Liu, L. Yang, L. Chai, J. Bai, J. Peng, X. Hu, C. Chen, D. Zhang, et al. (2023)
  Owl: a large language model for it operations.
  arXiv preprint arXiv:2309.09298.
  Cited by: [§7.2](https://arxiv.org/html/2504.18776v2#S7.SS2.p3.1 "7.2. LLM-based Failure Management ‣ 7. Related Work ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* Y. Han, Q. Du, Y. Huang, J. Wu, F. Tian, and C. He (2024)
  The potential of one-shot failure root cause analysis: collaboration of the large language model and small classifier.
  In Proceedings of the 39th IEEE/ACM International Conference on Automated Software Engineering,
   pp. 931–943.
  Cited by: [§7.2](https://arxiv.org/html/2504.18776v2#S7.SS2.p4.1 "7.2. LLM-based Failure Management ‣ 7. Related Work ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* J. Hu, X. Wu, Z. Zhu, W. Wang, D. Zhang, Y. Cao, et al. (2024)
  Openrlhf: an easy-to-use, scalable and high-performance rlhf framework.
  arXiv preprint arXiv:2405.11143.
  Cited by: [§3.2](https://arxiv.org/html/2504.18776v2#S3.SS2.p1.2 "3.2. Direct Application of GRPO Algorithm ‣ 3. Empirical Study ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"),
  [§5.1.4](https://arxiv.org/html/2504.18776v2#S5.SS1.SSS4.p1.5 "5.1.4. Implementation and Settings ‣ 5.1. Experimental Setup ‣ 5. Evaluation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"),
  [§9](https://arxiv.org/html/2504.18776v2#S9.p1.1 "9. Data Availability ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* T. Jia, Y. Li, Y. Yang, G. Huang, and Z. Wu (2022)
  Augmenting log-based anomaly detection models to reduce false anomalies with human feedback.
  In Proceedings of the 28th ACM SIGKDD Conference on Knowledge Discovery and Data Mining,
   pp. 3081–3089.
  Cited by: [§7.1](https://arxiv.org/html/2504.18776v2#S7.SS1.p6.1 "7.1. Root Cause Localization ‣ 7. Related Work ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* T. Jia, Y. Li, Y. Yang, and G. Huang (2024)
  Hilogx: noise-aware log-based anomaly detection with human feedback.
  The VLDB Journal 33 (3),  pp. 883–900.
  Cited by: [§7.1](https://arxiv.org/html/2504.18776v2#S7.SS1.p6.1 "7.1. Root Cause Localization ‣ 7. Related Work ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* Y. Jiang, C. Zhang, S. He, Z. Yang, M. Ma, S. Qin, Y. Kang, Y. Dang, S. Rajmohan, Q. Lin, et al. (2024)
  Xpert: empowering incident management with query recommendations via large language models.
  In Proceedings of the IEEE/ACM 46th International Conference on Software Engineering,
   pp. 1–13.
  Cited by: [§7.2](https://arxiv.org/html/2504.18776v2#S7.SS2.p4.1 "7.2. LLM-based Failure Management ‣ 7. Related Work ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* V. Le and H. Zhang (2024)
  PreLog: a pre-trained model for log analytics.
  Proceedings of the ACM on Management of Data 2 (3),  pp. 1–28.
  Cited by: [§7.2](https://arxiv.org/html/2504.18776v2#S7.SS2.p2.1 "7.2. LLM-based Failure Management ‣ 7. Related Work ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* B. Li, X. Peng, Q. Xiang, H. Wang, T. Xie, J. Sun, and X. Liu (2022a)
  Enjoy your observability: an industrial survey of microservice tracing and analysis.
  Empirical Software Engineering 27,  pp. 1–28.
  Cited by: [§7.1](https://arxiv.org/html/2504.18776v2#S7.SS1.p4.1 "7.1. Root Cause Localization ‣ 7. Related Work ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* C. Li, N. Liu, and K. Yang (2025a)
  Adaptive group policy optimization: towards stable training and token-efficient reasoning.
  arXiv preprint arXiv:2503.15952.
  Cited by: [§2.4](https://arxiv.org/html/2504.18776v2#S2.SS4.p12.1 "2.4. Reinforcement Fine-Tuning ‣ 2. Background & Motivation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* M. Li, Z. Li, K. Yin, X. Nie, W. Zhang, K. Sui, and D. Pei (2022b)
  Causal inference-based root cause analysis for online service systems with intervention recognition.
  In Proceedings of the 28th ACM SIGKDD Conference on Knowledge Discovery and Data Mining,
   pp. 3230–3240.
  Cited by: [§1](https://arxiv.org/html/2504.18776v2#S1.p3.1 "1. Introduction ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"),
  [§7.1](https://arxiv.org/html/2504.18776v2#S7.SS1.p3.1 "7.1. Root Cause Localization ‣ 7. Related Work ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* Y. Li, Y. Wu, J. Liu, Z. Jiang, Z. Chen, G. Yu, and M. R. Lyu (2025b)
  COCA: generative root cause analysis for distributed systems with code knowledge.
  In 2025 IEEE/ACM 47th International Conference on Software Engineering (ICSE),
   pp. 1346–1358.
  Cited by: [§B.3](https://arxiv.org/html/2504.18776v2#A2.SS3.p2.1 "B.3. Overview of selected publications ‣ Appendix B Systematic Review Process ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"),
  [1st item](https://arxiv.org/html/2504.18776v2#S1.I1.i1.p1.3 "In 1. Introduction ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"),
  [2nd item](https://arxiv.org/html/2504.18776v2#S1.I1.i2.p1.1 "In 1. Introduction ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"),
  [§2.5](https://arxiv.org/html/2504.18776v2#S2.SS5.SSS0.Px2.p1.1 "(2) Tool Reasoning Chain Capability. ‣ 2.5. Key Capabilities for LLM-based Failure Localization ‣ 2. Background & Motivation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"),
  [§2.5](https://arxiv.org/html/2504.18776v2#S2.SS5.p2.1 "2.5. Key Capabilities for LLM-based Failure Localization ‣ 2. Background & Motivation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"),
  [Table 1](https://arxiv.org/html/2504.18776v2#S2.T1.1.5.1 "In 2.5. Key Capabilities for LLM-based Failure Localization ‣ 2. Background & Motivation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"),
  [§7.1](https://arxiv.org/html/2504.18776v2#S7.SS1.p9.1 "7.1. Root Cause Localization ‣ 7. Related Work ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* Z. Li, J. Chen, R. Jiao, N. Zhao, Z. Wang, S. Zhang, Y. Wu, L. Jiang, L. Yan, Z. Wang, et al. (2021)
  Practical root cause localization for microservice systems via trace analysis.
  In 2021 IEEE/ACM 29th International Symposium on Quality of Service (IWQOS),
   pp. 1–10.
  Cited by: [§7.1](https://arxiv.org/html/2504.18776v2#S7.SS1.p5.1 "7.1. Root Cause Localization ‣ 7. Related Work ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* W. Liao, F. Porte-Agel, J. Fang, C. Rehtanz, S. Wang, D. Yang, and Z. Yang (2024)
  TimeGPT in load forecasting: a large time series model perspective.
  arXiv preprint arXiv:2404.04885.
  Cited by: [§7.2](https://arxiv.org/html/2504.18776v2#S7.SS2.p2.1 "7.2. LLM-based Failure Management ‣ 7. Related Work ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* C. Lin, C. Chang, W. Wang, K. Wang, and W. Peng (2024)
  Root cause analysis in microservice using neural granger causal discovery.
  In Proceedings of the AAAI Conference on Artificial Intelligence,
  Vol. 38,  pp. 206–213.
  Cited by: [§1](https://arxiv.org/html/2504.18776v2#S1.p3.1 "1. Introduction ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"),
  [§5.1.2](https://arxiv.org/html/2504.18776v2#S5.SS1.SSS2.p3.1 "5.1.2. Baseline Models and Approaches ‣ 5.1. Experimental Setup ‣ 5. Evaluation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"),
  [§7.1](https://arxiv.org/html/2504.18776v2#S7.SS1.p3.1 "7.1. Root Cause Localization ‣ 7. Related Work ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* J. Lin, P. Chen, and Z. Zheng (2018)
  Microscope: pinpoint performance issues with causal graphs in micro-service environments.
  In Service-Oriented Computing: 16th International Conference, ICSOC 2018, Hangzhou, China, November 12-15, 2018, Proceedings 16,
   pp. 3–20.
  Cited by: [§1](https://arxiv.org/html/2504.18776v2#S1.p3.1 "1. Introduction ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"),
  [§5.1.2](https://arxiv.org/html/2504.18776v2#S5.SS1.SSS2.p3.1 "5.1.2. Baseline Models and Approaches ‣ 5.1. Experimental Setup ‣ 5. Evaluation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* Q. Lin, J. Lou, H. Zhang, and D. Zhang (2016)
  IDice: problem identification for emerging issues.
  In Proceedings of the 38th International Conference on Software Engineering,
   pp. 214–224.
  Cited by: [§7.1](https://arxiv.org/html/2504.18776v2#S7.SS1.p3.1 "7.1. Root Cause Localization ‣ 7. Related Work ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* Z. Lin, M. Lin, Y. Xie, and R. Ji (2025)
  Cppo: accelerating the training of group relative policy optimization-based reasoning models.
  arXiv preprint arXiv:2503.22342.
  Cited by: [§2.4](https://arxiv.org/html/2504.18776v2#S2.SS4.p12.1 "2.4. Reinforcement Fine-Tuning ‣ 2. Background & Motivation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* H. Liu, Z. Zhao, J. Wang, H. Kamarthi, and B. A. Prakash (2024a)
  LSTPrompt: large language models as zero-shot time series forecasters by long-short-term prompting.
  arXiv preprint arXiv:2402.16132.
  Cited by: [§7.2](https://arxiv.org/html/2504.18776v2#S7.SS2.p4.1 "7.2. LLM-based Failure Management ‣ 7. Related Work ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* P. Liu, H. Xu, Q. Ouyang, R. Jiao, Z. Chen, S. Zhang, J. Yang, L. Mo, J. Zeng, W. Xue, et al. (2020)
  Unsupervised detection of microservice trace anomalies through service-level deep bayesian networks.
  In 2020 IEEE 31st International Symposium on Software Reliability Engineering (ISSRE),
   pp. 48–58.
  Cited by: [§7.1](https://arxiv.org/html/2504.18776v2#S7.SS1.p4.1 "7.1. Root Cause Localization ‣ 7. Related Work ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* S. Liu, D. Yao, L. Fang, Z. Li, W. Li, K. Feng, X. Ji, and J. Bi (2024b)
  Anomalyllm: few-shot anomaly edge detection for dynamic graphs using large language models.
  arXiv preprint arXiv:2405.07626.
  Cited by: [§7.2](https://arxiv.org/html/2504.18776v2#S7.SS2.p3.1 "7.2. LLM-based Failure Management ‣ 7. Related Work ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* X. Liu, J. Hu, Y. Li, S. Diao, Y. Liang, B. Hooi, and R. Zimmermann (2024c)
  Unitime: a language-empowered unified model for cross-domain time series forecasting.
  In Proceedings of the ACM Web Conference 2024,
   pp. 4095–4106.
  Cited by: [§7.2](https://arxiv.org/html/2504.18776v2#S7.SS2.p3.1 "7.2. LLM-based Failure Management ‣ 7. Related Work ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* Y. Liu, Y. Ji, S. Tao, M. He, W. Meng, S. Zhang, Y. Sun, Y. Xie, B. Chen, and H. Yang (2024d)
  Loglm: from task-based to instruction-based automated log analysis.
  arXiv preprint arXiv:2410.09352.
  Cited by: [§7.2](https://arxiv.org/html/2504.18776v2#S7.SS2.p3.1 "7.2. LLM-based Failure Management ‣ 7. Related Work ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* Y. Liu, S. Tao, W. Meng, J. Wang, W. Ma, Y. Chen, Y. Zhao, H. Yang, and Y. Jiang (2024e)
  Interpretable online log analysis using large language models with prompt strategies.
  In Proceedings of the 32nd IEEE/ACM International Conference on Program Comprehension,
   pp. 35–46.
  Cited by: [§7.2](https://arxiv.org/html/2504.18776v2#S7.SS2.p4.1 "7.2. LLM-based Failure Management ‣ 7. Related Work ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* Y. Liu, H. Zhang, C. Li, X. Huang, J. Wang, and M. Long (2024f)
  Timer: generative pre-trained transformers are large time series models.
  In Proceedings of the 41st International Conference on Machine Learning,
   pp. 32369–32399.
  Cited by: [§7.2](https://arxiv.org/html/2504.18776v2#S7.SS2.p2.1 "7.2. LLM-based Failure Management ‣ 7. Related Work ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* S. Luo, H. Xu, C. Lu, K. Ye, G. Xu, L. Zhang, Y. Ding, J. He, and C. Xu (2021)
  Characterizing microservice dependency and performance: alibaba trace analysis.
  In Proceedings of the ACM symposium on cloud computing,
   pp. 412–426.
  Cited by: [§7.1](https://arxiv.org/html/2504.18776v2#S7.SS1.p4.1 "7.1. Root Cause Localization ‣ 7. Related Work ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* L. Mariani, C. Monni, M. Pezzé, O. Riganelli, and R. Xin (2018)
  Localizing faults in cloud systems.
  In 2018 IEEE 11th International Conference on Software Testing, Verification and Validation (ICST),
   pp. 262–273.
  Cited by: [§7.1](https://arxiv.org/html/2504.18776v2#S7.SS1.p3.1 "7.1. Root Cause Localization ‣ 7. Related Work ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* J. Pan, W. S. Liang, and Y. Yidi (2024)
  Raglog: log anomaly detection using retrieval augmented generation.
  In 2024 IEEE World Forum on Public Safety Technology (WFPST),
   pp. 169–174.
  Cited by: [§7.2](https://arxiv.org/html/2504.18776v2#S7.SS2.p4.1 "7.2. LLM-based Failure Management ‣ 7. Related Work ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* C. Pei, Z. Wang, F. Liu, Z. Li, Y. Liu, X. He, R. Kang, T. Zhang, J. Chen, J. Li, et al. (2025)
  Flow-of-action: sop enhanced llm-based multi-agent system for root cause analysis.
  In Companion Proceedings of the ACM on Web Conference 2025,
   pp. 422–431.
  Cited by: [§B.3](https://arxiv.org/html/2504.18776v2#A2.SS3.p2.1 "B.3. Overview of selected publications ‣ Appendix B Systematic Review Process ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"),
  [1st item](https://arxiv.org/html/2504.18776v2#S1.I1.i1.p1.3 "In 1. Introduction ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"),
  [2nd item](https://arxiv.org/html/2504.18776v2#S1.I1.i2.p1.1 "In 1. Introduction ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"),
  [§2.5](https://arxiv.org/html/2504.18776v2#S2.SS5.SSS0.Px2.p1.1 "(2) Tool Reasoning Chain Capability. ‣ 2.5. Key Capabilities for LLM-based Failure Localization ‣ 2. Background & Motivation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"),
  [§2.5](https://arxiv.org/html/2504.18776v2#S2.SS5.p2.1 "2.5. Key Capabilities for LLM-based Failure Localization ‣ 2. Background & Motivation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"),
  [Table 1](https://arxiv.org/html/2504.18776v2#S2.T1.1.4.1 "In 2.5. Key Capabilities for LLM-based Failure Localization ‣ 2. Background & Motivation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"),
  [§7.1](https://arxiv.org/html/2504.18776v2#S7.SS1.p10.1 "7.1. Root Cause Localization ‣ 7. Related Work ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* R. Rafailov, A. Sharma, E. Mitchell, C. D. Manning, S. Ermon, and C. Finn (2023)
  Direct preference optimization: your language model is secretly a reward model.
  Advances in Neural Information Processing Systems 36,  pp. 53728–53741.
  Cited by: [§1](https://arxiv.org/html/2504.18776v2#S1.p7.1 "1. Introduction ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"),
  [§2.4](https://arxiv.org/html/2504.18776v2#S2.SS4.p3.1 "2.4. Reinforcement Fine-Tuning ‣ 2. Background & Motivation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* K. Rasul, A. Ashok, A. R. Williams, A. Khorasani, G. Adamopoulos, R. Bhagwatkar, M. Biloš, H. Ghonia, N. Hassen, A. Schneider, et al. (2023)
  Lag-llama: towards foundation models for time series forecasting.
  In R0-FoMo: Robustness of Few-shot and Zero-shot Learning in Large Foundation Models,
  Cited by: [§7.2](https://arxiv.org/html/2504.18776v2#S7.SS2.p2.1 "7.2. LLM-based Failure Management ‣ 7. Related Work ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* R. Ren (2025)
  The multi-agent fault localization system based on monte carlo tree search approach.
  arXiv preprint arXiv:2507.22800.
  Cited by: [§B.3](https://arxiv.org/html/2504.18776v2#A2.SS3.p2.1 "B.3. Overview of selected publications ‣ Appendix B Systematic Review Process ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"),
  [1st item](https://arxiv.org/html/2504.18776v2#S1.I1.i1.p1.3 "In 1. Introduction ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"),
  [2nd item](https://arxiv.org/html/2504.18776v2#S1.I1.i2.p1.1 "In 1. Introduction ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"),
  [§2.5](https://arxiv.org/html/2504.18776v2#S2.SS5.SSS0.Px2.p1.1 "(2) Tool Reasoning Chain Capability. ‣ 2.5. Key Capabilities for LLM-based Failure Localization ‣ 2. Background & Motivation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"),
  [§2.5](https://arxiv.org/html/2504.18776v2#S2.SS5.p2.1 "2.5. Key Capabilities for LLM-based Failure Localization ‣ 2. Background & Motivation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"),
  [Table 1](https://arxiv.org/html/2504.18776v2#S2.T1.1.7.1 "In 2.5. Key Capabilities for LLM-based Failure Localization ‣ 2. Background & Motivation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"),
  [§4.1.2](https://arxiv.org/html/2504.18776v2#S4.SS1.SSS2.p1.1 "4.1.2. Recursion-of-Thought ‣ 4.1. Recursion-of-Thought Actor ‣ 4. ThinkFL ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"),
  [§7.1](https://arxiv.org/html/2504.18776v2#S7.SS1.p10.1 "7.1. Root Cause Localization ‣ 7. Related Work ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* S. Sane (2025)
  Hybrid group relative policy optimization: a multi-sample approach to enhancing policy optimization.
  arXiv preprint arXiv:2502.01652.
  Cited by: [§2.4](https://arxiv.org/html/2504.18776v2#S2.SS4.p12.1 "2.4. Reinforcement Fine-Tuning ‣ 2. Background & Motivation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* J. Schulman, F. Wolski, P. Dhariwal, A. Radford, and O. Klimov (2017)
  Proximal policy optimization algorithms.
  arXiv preprint arXiv:1707.06347.
  Cited by: [§1](https://arxiv.org/html/2504.18776v2#S1.p7.1 "1. Introduction ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"),
  [§2.4](https://arxiv.org/html/2504.18776v2#S2.SS4.p3.1 "2.4. Reinforcement Fine-Tuning ‣ 2. Background & Motivation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* Z. Shao, P. Wang, Q. Zhu, R. Xu, J. Song, X. Bi, H. Zhang, M. Zhang, Y. Li, Y. Wu, et al. (2024)
  Deepseekmath: pushing the limits of mathematical reasoning in open language models.
  arXiv preprint arXiv:2402.03300.
  Cited by: [§1](https://arxiv.org/html/2504.18776v2#S1.p7.1 "1. Introduction ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"),
  [§2.4](https://arxiv.org/html/2504.18776v2#S2.SS4.p3.1 "2.4. Reinforcement Fine-Tuning ‣ 2. Background & Motivation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"),
  [§3.2](https://arxiv.org/html/2504.18776v2#S3.SS2.p1.2 "3.2. Direct Application of GRPO Algorithm ‣ 3. Empirical Study ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* Z. Shen (2024)
  Llm with tools: a survey.
  arXiv preprint arXiv:2409.18807.
  Cited by: [§3.1](https://arxiv.org/html/2504.18776v2#S3.SS1.p1.1 "3.1. Capability of SOTA Lightweight LLMs ‣ 3. Empirical Study ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* J. Shi, S. Jiang, B. Xu, J. Liang, Y. Xiao, and W. Wang (2023)
  Shellgpt: generative pre-trained transformer model for shell language understanding.
  In 2023 IEEE 34th International Symposium on Software Reliability Engineering (ISSRE),
   pp. 671–682.
  Cited by: [§7.2](https://arxiv.org/html/2504.18776v2#S7.SS2.p2.1 "7.2. LLM-based Failure Management ‣ 7. Related Work ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* Y. Sun, Z. Lin, B. Shi, S. Zhang, S. Ma, P. Jin, Z. Zhong, L. Pan, Y. Guo, and D. Pei (2025)
  Interpretable failure localization for microservice systems based on graph autoencoder.
  ACM Transactions on Software Engineering and Methodology 34 (2),  pp. 1–28.
  Cited by: [§1](https://arxiv.org/html/2504.18776v2#S1.p2.1 "1. Introduction ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* Y. Tian, Y. Liu, Z. Chong, Z. Huang, and H. Jacobsen (2025)
  GALA: can graph-augmented large language model agentic workflows elevate root cause analysis?.
  arXiv preprint arXiv:2508.12472.
  Cited by: [§B.3](https://arxiv.org/html/2504.18776v2#A2.SS3.p2.1 "B.3. Overview of selected publications ‣ Appendix B Systematic Review Process ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* L. Wang, C. Zhang, R. Ding, Y. Xu, Q. Chen, W. Zou, Q. Chen, M. Zhang, X. Gao, H. Fan, et al. (2023)
  Root cause analysis for microservice systems via hierarchical reinforcement learning from human feedback.
  In Proceedings of the 29th ACM SIGKDD Conference on Knowledge Discovery and Data Mining,
   pp. 5116–5125.
  Cited by: [§7.1](https://arxiv.org/html/2504.18776v2#S7.SS1.p6.1 "7.1. Root Cause Localization ‣ 7. Related Work ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* Q. Wang, X. Zhang, M. Li, Y. Yuan, M. Xiao, F. Zhuang, and D. Yu (2025)
  TAMO: fine-grained root cause analysis via tool-assisted llm agent with multi-modality observation data in cloud-native systems.
  arXiv preprint arXiv:2504.20462.
  Cited by: [§B.3](https://arxiv.org/html/2504.18776v2#A2.SS3.p2.1 "B.3. Overview of selected publications ‣ Appendix B Systematic Review Process ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"),
  [1st item](https://arxiv.org/html/2504.18776v2#S1.I1.i1.p1.3 "In 1. Introduction ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"),
  [2nd item](https://arxiv.org/html/2504.18776v2#S1.I1.i2.p1.1 "In 1. Introduction ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"),
  [§2.5](https://arxiv.org/html/2504.18776v2#S2.SS5.SSS0.Px2.p1.1 "(2) Tool Reasoning Chain Capability. ‣ 2.5. Key Capabilities for LLM-based Failure Localization ‣ 2. Background & Motivation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"),
  [§2.5](https://arxiv.org/html/2504.18776v2#S2.SS5.p2.1 "2.5. Key Capabilities for LLM-based Failure Localization ‣ 2. Background & Motivation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"),
  [Table 1](https://arxiv.org/html/2504.18776v2#S2.T1.1.6.1 "In 2.5. Key Capabilities for LLM-based Failure Localization ‣ 2. Background & Motivation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"),
  [§7.1](https://arxiv.org/html/2504.18776v2#S7.SS1.p9.1 "7.1. Root Cause Localization ‣ 7. Related Work ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* Y. Wang, Z. Zhu, Q. Fu, Y. Ma, and P. He (2024a)
  MRCA: metric-level root cause analysis for microservices via multi-modal data.
  In Proceedings of the 39th IEEE/ACM International Conference on Automated Software Engineering,
   pp. 1057–1068.
  Cited by: [§1](https://arxiv.org/html/2504.18776v2#S1.p1.1 "1. Introduction ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* Z. Wang, Z. Liu, Y. Zhang, A. Zhong, J. Wang, F. Yin, L. Fan, L. Wu, and Q. Wen (2024b)
  Rcagent: cloud root cause analysis by autonomous agents with tool-augmented large language models.
  In Proceedings of the 33rd ACM International Conference on Information and Knowledge Management,
   pp. 4966–4974.
  Cited by: [§B.3](https://arxiv.org/html/2504.18776v2#A2.SS3.p2.1 "B.3. Overview of selected publications ‣ Appendix B Systematic Review Process ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"),
  [1st item](https://arxiv.org/html/2504.18776v2#S1.I1.i1.p1.3 "In 1. Introduction ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"),
  [§1](https://arxiv.org/html/2504.18776v2#S1.p4.1 "1. Introduction ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"),
  [§2.5](https://arxiv.org/html/2504.18776v2#S2.SS5.SSS0.Px2.p1.1 "(2) Tool Reasoning Chain Capability. ‣ 2.5. Key Capabilities for LLM-based Failure Localization ‣ 2. Background & Motivation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"),
  [§2.5](https://arxiv.org/html/2504.18776v2#S2.SS5.p2.1 "2.5. Key Capabilities for LLM-based Failure Localization ‣ 2. Background & Motivation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"),
  [Table 1](https://arxiv.org/html/2504.18776v2#S2.T1.1.3.1 "In 2.5. Key Capabilities for LLM-based Failure Localization ‣ 2. Background & Motivation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"),
  [§5.1.2](https://arxiv.org/html/2504.18776v2#S5.SS1.SSS2.p4.1 "5.1.2. Baseline Models and Approaches ‣ 5.1. Experimental Setup ‣ 5. Evaluation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"),
  [§7.1](https://arxiv.org/html/2504.18776v2#S7.SS1.p9.1 "7.1. Root Cause Localization ‣ 7. Related Work ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* M. Waseem, P. Liang, M. Shahin, A. Di Salle, and G. Márquez (2021)
  Design, monitoring, and testing of microservices systems: the practitioners’ perspective.
  Journal of Systems and Software 182,  pp. 111061.
  Cited by: [§1](https://arxiv.org/html/2504.18776v2#S1.p1.1 "1. Introduction ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* Y. Wu, Z. Sun, S. Li, S. Welleck, and Y. Yang (2025)
  Inference scaling laws: an empirical analysis of compute-optimal inference for llm problem-solving.
  In The Thirteenth International Conference on Learning Representations,
  Cited by: [§3.1](https://arxiv.org/html/2504.18776v2#S3.SS1.p1.1 "3.1. Capability of SOTA Lightweight LLMs ‣ 3. Empirical Study ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* Y. Xiang, C. P. Chen, L. Zeng, W. Yin, X. Liu, H. Li, and W. Xu (2025)
  Simplifying root cause analysis in kubernetes with stategraph and llm.
  arXiv preprint arXiv:2506.02490.
  Cited by: [§B.3](https://arxiv.org/html/2504.18776v2#A2.SS3.p2.1 "B.3. Overview of selected publications ‣ Appendix B Systematic Review Process ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* J. Xu, Q. Zhang, Z. Zhong, S. He, C. Zhang, Q. Lin, D. Pei, P. He, D. Zhang, and Q. Zhang (2025)
  OpenRCA: can large language models locate the root cause of software failures?.
  In The Thirteenth International Conference on Learning Representations,
  Cited by: [§1](https://arxiv.org/html/2504.18776v2#S1.p1.1 "1. Introduction ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* H. Xue and F. D. Salim (2023)
  Promptcast: a new prompt-based learning paradigm for time series forecasting.
  IEEE Transactions on Knowledge and Data Engineering.
  Cited by: [§7.2](https://arxiv.org/html/2504.18776v2#S7.SS2.p3.1 "7.2. LLM-based Failure Management ‣ 7. Related Work ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* S. Yan, C. Shan, W. Yang, B. Xu, D. Li, L. Qiu, J. Tong, and Q. Zhang (2022)
  Cmmd: cross-metric multi-dimensional root cause analysis.
  In Proceedings of the 28th ACM SIGKDD Conference on Knowledge Discovery and Data Mining,
   pp. 4310–4320.
  Cited by: [§7.1](https://arxiv.org/html/2504.18776v2#S7.SS1.p3.1 "7.1. Root Cause Localization ‣ 7. Related Work ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* A. Yang, A. Li, B. Yang, B. Zhang, B. Hui, B. Zheng, B. Yu, C. Gao, C. Huang, C. Lv, et al. (2025a)
  Qwen3 technical report.
  arXiv preprint arXiv:2505.09388.
  Cited by: [§1](https://arxiv.org/html/2504.18776v2#S1.p7.1 "1. Introduction ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* B. Yang, Z. Cai, F. Liu, B. Le, L. Zhang, T. F. Bissyandé, Y. Liu, and H. Tian (2025b)
  A survey of llm-based automated program repair: taxonomies, design paradigms, and applications.
  arXiv preprint arXiv:2506.23749.
  Cited by: [§2.5](https://arxiv.org/html/2504.18776v2#S2.SS5.p2.1 "2.5. Key Capabilities for LLM-based Failure Localization ‣ 2. Background & Motivation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* T. Yang, J. Shen, Y. Su, X. Ling, Y. Yang, and M. R. Lyu (2021)
  AID: efficient prediction of aggregated intensity of dependency in large-scale cloud systems.
  In 2021 36th IEEE/ACM International Conference on Automated Software Engineering (ASE),
   pp. 653–665.
  Cited by: [§7.1](https://arxiv.org/html/2504.18776v2#S7.SS1.p3.1 "7.1. Root Cause Localization ‣ 7. Related Work ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* Z. Yao, C. Pei, W. Chen, H. Wang, L. Su, H. Jiang, Z. Xie, X. Nie, and D. Pei (2024)
  Chain-of-event: interpretable root cause analysis for microservices through automatically learning weighted event causal graph.
  In Companion Proceedings of the 32nd ACM International Conference on the Foundations of Software Engineering,
   pp. 50–61.
  Cited by: [§1](https://arxiv.org/html/2504.18776v2#S1.p4.1 "1. Introduction ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* Y. YifeiLu, F. Ye, J. Li, Q. Gao, C. Liu, H. Luo, N. Du, X. Li, and F. Ren (2025)
  CodeTool: enhancing programmatic tool invocation of llms via process supervision.
  In Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers),
   pp. 18287–18304.
  Cited by: [§3.1](https://arxiv.org/html/2504.18776v2#S3.SS1.p1.1 "3.1. Capability of SOTA Lightweight LLMs ‣ 3. Empirical Study ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* J. Yin, X. Zhao, Y. Tang, C. Zhi, Z. Chen, and Z. Wu (2016)
  Cloudscout: a non-intrusive approach to service dependency discovery.
  IEEE Transactions on Parallel and Distributed Systems 28 (5),  pp. 1271–1284.
  Cited by: [§7.1](https://arxiv.org/html/2504.18776v2#S7.SS1.p3.1 "7.1. Root Cause Localization ‣ 7. Related Work ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* G. Yu, P. Chen, H. Chen, Z. Guan, Z. Huang, L. Jing, T. Weng, X. Sun, and X. Li (2021)
  Microrank: end-to-end latency issue localization with extended spectrum analysis in microservice environments.
  In Proceedings of the Web Conference 2021,
   pp. 3087–3098.
  Cited by: [§1](https://arxiv.org/html/2504.18776v2#S1.p3.1 "1. Introduction ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"),
  [§5.1.2](https://arxiv.org/html/2504.18776v2#S5.SS1.SSS2.p3.1 "5.1.2. Baseline Models and Approaches ‣ 5.1. Experimental Setup ‣ 5. Evaluation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"),
  [§7.1](https://arxiv.org/html/2504.18776v2#S7.SS1.p5.1 "7.1. Root Cause Localization ‣ 7. Related Work ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* G. Yu, P. Chen, Y. Li, H. Chen, X. Li, and Z. Zheng (2023a)
  Nezha: interpretable fine-grained root causes analysis for microservices on multi-modal observability data.
  In Proceedings of the 31st ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering,
   pp. 553–565.
  Cited by: [§1](https://arxiv.org/html/2504.18776v2#S1.p4.1 "1. Introduction ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* G. Yu, Z. Huang, and P. Chen (2023b)
  TraceRank: abnormal service localization with dis-aggregated end-to-end tracing data in cloud native systems.
  Journal of Software: Evolution and Process 35 (10),  pp. e2413.
  Cited by: [§1](https://arxiv.org/html/2504.18776v2#S1.p3.1 "1. Introduction ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"),
  [§5.1.2](https://arxiv.org/html/2504.18776v2#S5.SS1.SSS2.p3.1 "5.1.2. Baseline Models and Approaches ‣ 5.1. Experimental Setup ‣ 5. Evaluation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"),
  [§7.1](https://arxiv.org/html/2504.18776v2#S7.SS1.p5.1 "7.1. Root Cause Localization ‣ 7. Related Work ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* Z. Yu, C. Pei, X. Wang, M. Ma, C. Bansal, S. Rajmohan, Q. Lin, D. Zhang, X. Wen, J. Li, et al. (2024)
  Pre-trained kpi anomaly detection model through disentangled transformer.
  In Proceedings of the 30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining,
   pp. 6190–6201.
  Cited by: [§7.2](https://arxiv.org/html/2504.18776v2#S7.SS2.p2.1 "7.2. LLM-based Failure Management ‣ 7. Related Work ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* S. Yuan, K. Song, J. Chen, X. Tan, Y. Shen, K. Ren, D. Li, and D. Yang (2025)
  EASYTOOL: enhancing llm-based agents with concise tool instruction.
  In Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers),
   pp. 951–972.
  Cited by: [§3.1](https://arxiv.org/html/2504.18776v2#S3.SS1.p1.1 "3.1. Capability of SOTA Lightweight LLMs ‣ 3. Empirical Study ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* Y. Zeng, G. Liu, W. Ma, N. Yang, H. Zhang, and J. Wang (2024)
  Token-level direct preference optimization.
  arXiv preprint arXiv:2404.11999.
  Cited by: [§2.4](https://arxiv.org/html/2504.18776v2#S2.SS4.p12.1 "2.4. Reinforcement Fine-Tuning ‣ 2. Background & Motivation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* Y. Zhai, S. Tao, C. Chen, A. Zou, Z. Chen, Q. Fu, S. Mai, L. Yu, J. Deng, Z. Cao, et al. (2025)
  AgentEvolver: towards efficient self-evolving agent system.
  arXiv preprint arXiv:2511.10395.
  Cited by: [§9](https://arxiv.org/html/2504.18776v2#S9.p1.1 "9. Data Availability ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* C. Zhang, Z. Dong, X. Peng, B. Zhang, and M. Chen (2024a)
  Trace-based multi-dimensional root cause localization of performance issues in microservice systems.
  In Proceedings of the IEEE/ACM 46th International Conference on Software Engineering,
   pp. 1–12.
  Cited by: [§1](https://arxiv.org/html/2504.18776v2#S1.p3.1 "1. Introduction ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"),
  [§5.1.2](https://arxiv.org/html/2504.18776v2#S5.SS1.SSS2.p3.1 "5.1.2. Baseline Models and Approaches ‣ 5.1. Experimental Setup ‣ 5. Evaluation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"),
  [§5.1.3](https://arxiv.org/html/2504.18776v2#S5.SS1.SSS3.p1.1 "5.1.3. Evaluation Metrics ‣ 5.1. Experimental Setup ‣ 5. Evaluation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"),
  [§7.1](https://arxiv.org/html/2504.18776v2#S7.SS1.p5.1 "7.1. Root Cause Localization ‣ 7. Related Work ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* D. Zhang, X. Zhang, C. Bansal, P. Las-Casas, R. Fonseca, and S. Rajmohan (2024b)
  LM-pace: confidence estimation by large language models for effective root causing of cloud incidents.
  In Companion Proceedings of the 32nd ACM International Conference on the Foundations of Software Engineering,
   pp. 388–398.
  Cited by: [§7.2](https://arxiv.org/html/2504.18776v2#S7.SS2.p4.1 "7.2. LLM-based Failure Management ‣ 7. Related Work ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* L. Zhang, T. Jia, M. Jia, Y. Wu, A. Liu, Y. Yang, Z. Wu, X. Hu, P. Yu, and Y. Li (2025a)
  A survey of aiops in the era of large language models.
  ACM Computing Surveys.
  Cited by: [§1](https://arxiv.org/html/2504.18776v2#S1.p1.1 "1. Introduction ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"),
  [§7.2](https://arxiv.org/html/2504.18776v2#S7.SS2.p1.1 "7.2. LLM-based Failure Management ‣ 7. Related Work ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* L. Zhang, T. Jia, K. Wang, W. Hong, C. Duan, M. He, and Y. Li (2025b)
  Adaptive root cause localization for microservice systems with multi-agent recursion-of-thought.
  arXiv preprint arXiv:2508.20370.
  Cited by: [§1](https://arxiv.org/html/2504.18776v2#S1.p4.1 "1. Introduction ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* L. Zhang, Y. Zhai, T. Jia, C. Duan, M. He, L. Pan, Z. Liu, B. Ding, and Y. Li (2025c)
  MicroRemed: benchmarking llms in microservices remediation.
  arXiv preprint arXiv:2511.01166.
  Cited by: [§7.2](https://arxiv.org/html/2504.18776v2#S7.SS2.p4.1 "7.2. LLM-based Failure Management ‣ 7. Related Work ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* T. Zhang, Z. Jiang, S. Bai, T. Zhang, L. Lin, Y. Liu, and J. Ren (2024c)
  RAG4ITOps: a supervised fine-tunable and comprehensive rag framework for it operations and maintenance.
  In Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing: Industry Track,
   pp. 738–754.
  Cited by: [§7.2](https://arxiv.org/html/2504.18776v2#S7.SS2.p3.1 "7.2. LLM-based Failure Management ‣ 7. Related Work ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* W. Zhang, Q. Zhang, E. Yu, Y. Ren, Y. Meng, M. Qiu, and J. Wang (2024d)
  LogRAG: semi-supervised log-based anomaly detection with retrieval-augmented generation.
  In 2024 IEEE International Conference on Web Services (ICWS),
   pp. 1100–1102.
  Cited by: [§7.2](https://arxiv.org/html/2504.18776v2#S7.SS2.p4.1 "7.2. LLM-based Failure Management ‣ 7. Related Work ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* W. Zhang, H. Guo, J. Yang, Z. Tian, Y. Zhang, Y. Chaoran, Z. Li, T. Li, X. Shi, L. Zheng, et al. (2024e)
  MABC: multi-agent blockchain-inspired collaboration for root cause analysis in micro-services architecture.
  In Findings of the Association for Computational Linguistics: EMNLP 2024,
   pp. 4017–4033.
  Cited by: [§B.3](https://arxiv.org/html/2504.18776v2#A2.SS3.p2.1 "B.3. Overview of selected publications ‣ Appendix B Systematic Review Process ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"),
  [1st item](https://arxiv.org/html/2504.18776v2#S1.I1.i1.p1.3 "In 1. Introduction ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"),
  [2nd item](https://arxiv.org/html/2504.18776v2#S1.I1.i2.p1.1 "In 1. Introduction ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"),
  [§1](https://arxiv.org/html/2504.18776v2#S1.p4.1 "1. Introduction ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"),
  [§2.5](https://arxiv.org/html/2504.18776v2#S2.SS5.SSS0.Px2.p1.1 "(2) Tool Reasoning Chain Capability. ‣ 2.5. Key Capabilities for LLM-based Failure Localization ‣ 2. Background & Motivation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"),
  [§2.5](https://arxiv.org/html/2504.18776v2#S2.SS5.p2.1 "2.5. Key Capabilities for LLM-based Failure Localization ‣ 2. Background & Motivation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"),
  [Table 1](https://arxiv.org/html/2504.18776v2#S2.T1.1.2.1 "In 2.5. Key Capabilities for LLM-based Failure Localization ‣ 2. Background & Motivation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"),
  [§5.1.2](https://arxiv.org/html/2504.18776v2#S5.SS1.SSS2.p4.1 "5.1.2. Baseline Models and Approaches ‣ 5.1. Experimental Setup ‣ 5. Evaluation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"),
  [§7.1](https://arxiv.org/html/2504.18776v2#S7.SS1.p10.1 "7.1. Root Cause Localization ‣ 7. Related Work ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* X. Zhang, C. Du, Y. Li, Y. Xu, H. Zhang, S. Qin, Z. Li, Q. Lin, Y. Dang, A. Zhou, et al. (2021)
  Halo: hierarchy-aware fault localization for cloud systems.
  In Proceedings of the 27th ACM SIGKDD Conference on Knowledge Discovery & Data Mining,
   pp. 3948–3958.
  Cited by: [§7.1](https://arxiv.org/html/2504.18776v2#S7.SS1.p3.1 "7.1. Root Cause Localization ‣ 7. Related Work ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* Z. Zhang, M. K. Ramanathan, P. Raj, A. Parwal, T. Sherwood, and M. Chabbi (2022)
  {\{crisp}\}: Critical path analysis of {\{large-scale}\} microservice architectures.
  In 2022 USENIX Annual Technical Conference (USENIX ATC 22),
   pp. 655–672.
  Cited by: [§1](https://arxiv.org/html/2504.18776v2#S1.p3.1 "1. Introduction ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"),
  [§5.1.2](https://arxiv.org/html/2504.18776v2#S5.SS1.SSS2.p3.1 "5.1.2. Baseline Models and Approaches ‣ 5.1. Experimental Setup ‣ 5. Evaluation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* W. Zhou, Y. Peng, M. Tao, C. Zhao, H. Dong, M. Tang, and J. Wang (2025)
  LightPlanner: unleashing the reasoning capabilities of lightweight large language models in task planning.
  arXiv preprint arXiv:2503.08508.
  Cited by: [§3.1](https://arxiv.org/html/2504.18776v2#S3.SS1.p1.1 "3.1. Capability of SOTA Lightweight LLMs ‣ 3. Empirical Study ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* X. Zhou, X. Peng, T. Xie, J. Sun, C. Ji, D. Liu, Q. Xiang, and C. He (2019)
  Latent error prediction and fault localization for microservice applications by learning from system trace logs.
  In Proceedings of the 2019 27th ACM joint meeting on European software engineering conference and symposium on the foundations of software engineering,
   pp. 683–694.
  Cited by: [§7.1](https://arxiv.org/html/2504.18776v2#S7.SS1.p4.1 "7.1. Root Cause Localization ‣ 7. Related Work ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").
* D. M. Ziegler, N. Stiennon, J. Wu, T. B. Brown, A. Radford, D. Amodei, P. Christiano, and G. Irving (2019)
  Fine-tuning language models from human preferences.
  arXiv preprint arXiv:1909.08593.
  Cited by: [§2.4](https://arxiv.org/html/2504.18776v2#S2.SS4.p1.1 "2.4. Reinforcement Fine-Tuning ‣ 2. Background & Motivation ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning").

[System] You are a software operations engineer. Your task is to systematically diagnose and identify the root cause of software failures. You have the following tools: search\_traces, search\_fluctuating\_metrics, print\_results. 

[User] Please read the following root trace and identify corresponding root cause service. 
  
timestamp: 1647753157852, cmdb\_id: frontend2-0, span\_id: 0a81f08fc9b7dc5d, duration: 29982953 µs
 

[Tool Call] search\_traces(parent\_span\_id="0a81f08fc9b7dc5d")

[Tool Response]



cmdb\_id
opeartion
duration
span\_id

frontend2-0
RecommendationService/ListRecommendations
29,892,726 µs
9063994c3450e63a

frontend2-0
CurrencyService/GetSupportedCurrencies
1,836 µs
1c7b764e0a11a132

frontend2-0
CartService/GetCart
1,995 µs
0dc30c7af1adbe40

frontend2-0
AdService/GetAds
4,516 µs
a383db1c6acc90a5

frontend2-0
ProductCatalogService/GetProduct
41813 µs
ceed3378cb0c32f9

…
…
…
…
 

[Tool Call] search\_traces(parent\_span\_id="9063994c3450e63a")

[Tool Response]



cmdb\_id
opeartion
duration
span\_id

recommendationservice2-0
RecommendationService/List
29889199 µs
eedd72a7aaa04418
 

[Tool Call] search\_traces(parent\_span\_id="eedd72a7aaa04418")

[Tool Response]



cmdb\_id
opeartion
duration
span\_id

recommendationservice2-0
ProductCatalogService/ListProducts
29887267 µs
fb9693f175e5b84f
 

[Tool Call] search\_fluctuating\_metrics(service\_name="recommendationservice",timestamp="1647753157852")

[Tool Response]



Metric
regular\_mean
current\_mean
Change

node-5.recommendationservice2-0.pgfault
0.675
1.35
×2.0\times 2.0

node-5.recommendationservice-0.pgfault
0.075
0.15
×2.0\times 2.0

node-5.recommendationservice-2.pgfault
0.025
0.05
×2.0\times 2.0

…
…
…
…
 

[Tool Call] search\_traces(parent\_span\_id="fb9693f175e5b84f")

[Tool Response]



cmdb\_id
opeartion
duration
span\_id

productcatalogservice-0
ProductCatalogService/ListProducts
25 µs
12552d251b74a1a4
 

[Tool Call]


```
ΨΨΨΨprint_results([
ΨΨΨΨ{service: "recommendationservice"}, {pod: "recommendationservice-0"},
ΨΨΨΨ{service: "productcatalogservice"}, {pod: "productcatalogservice-0"},
ΨΨΨΨ{service: "currencyservice"},...])
ΨΨΨ
```



Figure 13. Sample Output of a Real Reasoning Case from ThinkFL

## Appendix A Sample Output from ThinkFL

To illustrate how ThinkFL represents and outputs its reasoning, Figure [13](https://arxiv.org/html/2504.18776v2#A0.F13 "Figure 13 ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning") presents a real case—chosen because ThinkFL’s final top-1 prediction is incorrect—to highlight both the transparency and practical utility of its reasoning process. For brevity, we show only the tool-invocation dialogue rather than the internal chain-of-thought. As the figure shows, ThinkFL iteratively invokes diagnostic tools, traverses the trace hierarchy, queries metrics for suspected components, and produces a ranked list of candidate root causes with supporting evidence. Although ThinkFL incorrectly ranks RecommendationService above ProductCatalogService, the true root cause is still evident in the intermediate steps: ThinkFL reaches the critical spans, inspects the associated metrics, and includes ProductCatalogService in the final candidate set, demonstrating that the reasoning path remains informative even when the top-1 prediction is wrong.

## Appendix B Systematic Review Process

In this section, we present our systematic literature review process and findings on LLM-based failure localization for microservice, including the search strategy and scope, the exclusion criteria, and a summary of the publications that satisfied these criteria.

### B.1. Search strategy

To manage the vast body of literature efficiently, we limit our search to three databases444https://ieeexplore.ieee.org/, https://dl.acm.org/, https://arxiv.org/. We select IEEE Xplore and the ACM Digital Library, as they are frequently cited in related literature surveys and cover a broad range of applied research fields. Finally, we include arXiv, given its prominence as the leading pre-print platform in the field of computer science.

![Refer to caption](x16.png)


Figure 14. Search Strategy Utilized to Identify Studies on LLM-based Failure Localization

Based on our preliminary exploration, we derived relevant keywords for searching the literature on LLM-based failure localization and restricted our search to papers matching the search string shown in Figure [14](https://arxiv.org/html/2504.18776v2#A2.F14 "Figure 14 ‣ B.1. Search strategy ‣ Appendix B Systematic Review Process ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"). To ensure comprehensive coverage, we also included broader keywords such as failure diagnosis and root cause analysis. Subsequently, we manually filter out works that fall outside the scope of this paper using exclusion criteria.

### B.2. Exclusion criteria

To ensure relevance, we first screen papers by title and abstract; when unclear, we review the full text. We exclude papers that meet any of the following criteria:

* •

  EC1: The study uses a model with a parameter size smaller than 1 billion.
* •

  EC2: The study is outside the scope of failure localization.
* •

  EC3: The study is unrelated to microservice systems.
* •

  EC4: The study only presents conceptual ideas without experimental results.

Each record is assessed by a primary reviewer, with non-trivial cases discussed with at least one secondary reviewer. The final list of selected papers is validated by all co-authors. These criteria reflect our goal of focusing on practical, LLM-based failure localization research. EC1 excludes studies using smaller models—particularly BERT variants—which are not generally regarded as LLMs. Because our search strategy is intentionally broad, we manually filter out papers unrelated to failure localization, such as those addressing only failure categorization or program repair. EC3 ensures that selected studies center on microservice systems, excluding work from other domains (e.g., robotics or mechanical devices). Finally, EC4 removes low-quality studies that lack experimental evidence.

![Refer to caption](x17.png)


Figure 15. Overview of Paper Selection Procedure

### B.3. Overview of selected publications

We then present an overview of the workflow for selecting the papers and summarize the corresponding results. As shown in Figure [15](https://arxiv.org/html/2504.18776v2#A2.F15 "Figure 15 ‣ B.2. Exclusion criteria ‣ Appendix B Systematic Review Process ‣ ThinkFL: Self-Refining Failure Localization for Microservice Systems via Reinforcement Fine-Tuning"), we initially retrieve 134 papers from three databases. After removing duplicates, 110 papers remain. During the screening phase, we exclude 76 papers based on their titles and abstracts using criteria EC1-EC3. The remaining 34 papers are downloaded for detailed reading, where we find that 26 papers do not align with the scope of our study. Ultimately, 8 new studies satisfy our predefined criteria and are selected for further analysis.

Among the selected papers, six focus directly on failure localization. mABC (Zhang et al., [2024e](https://arxiv.org/html/2504.18776v2#bib.bib24 "MABC: multi-agent blockchain-inspired collaboration for root cause analysis in micro-services architecture")) integrates a dependency query engine with a metric explorer to surface suspicious services. RCAgent (Wang et al., [2024b](https://arxiv.org/html/2504.18776v2#bib.bib44 "Rcagent: cloud root cause analysis by autonomous agents with tool-augmented large language models")) invokes log- and trace-analysis tools to construct structured diagnostic evidence. Flow-of-Action (Pei et al., [2025](https://arxiv.org/html/2504.18776v2#bib.bib100 "Flow-of-action: sop enhanced llm-based multi-agent system for root cause analysis")) coordinates multiple tools through an SOP-style workflow. COCA (Li et al., [2025b](https://arxiv.org/html/2504.18776v2#bib.bib101 "COCA: generative root cause analysis for distributed systems with code knowledge")) extracts code snippets and execution paths for localization. TAMO (Wang et al., [2025](https://arxiv.org/html/2504.18776v2#bib.bib102 "TAMO: fine-grained root cause analysis via tool-assisted llm agent with multi-modality observation data in cloud-native systems")) aligns multi-modal operational signals, and KnowledgeMind (Ren, [2025](https://arxiv.org/html/2504.18776v2#bib.bib104 "The multi-agent fault localization system based on monte carlo tree search approach")) pairs metric/log/trace tools with Monte Carlo Tree Search for guided exploration. Two additional works aim to directly generate full root-cause analysis reports, where failure localization constitutes only one component. GALA (Tian et al., [2025](https://arxiv.org/html/2504.18776v2#bib.bib131 "GALA: can graph-augmented large language model agentic workflows elevate root cause analysis?")) combines statistical causal inference with LLM-guided iterative reasoning to produce root-cause rankings, incident summaries, and recommended actions. SynergyRCA (Xiang et al., [2025](https://arxiv.org/html/2504.18776v2#bib.bib103 "Simplifying root cause analysis in kubernetes with stategraph and llm")) leverages an LLM to identify key resources and retrieves structured causal context from prebuilt StateGraph and MetaGraph representations to support end-to-end RCA.

Generated on Fri Jan 16 02:41:22 2026 by [LaTeXML![Mascot Sammy](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAsAAAAOCAYAAAD5YeaVAAAAAXNSR0IArs4c6QAAAAZiS0dEAP8A/wD/oL2nkwAAAAlwSFlzAAALEwAACxMBAJqcGAAAAAd0SU1FB9wKExQZLWTEaOUAAAAddEVYdENvbW1lbnQAQ3JlYXRlZCB3aXRoIFRoZSBHSU1Q72QlbgAAAdpJREFUKM9tkL+L2nAARz9fPZNCKFapUn8kyI0e4iRHSR1Kb8ng0lJw6FYHFwv2LwhOpcWxTjeUunYqOmqd6hEoRDhtDWdA8ApRYsSUCDHNt5ul13vz4w0vWCgUnnEc975arX6ORqN3VqtVZbfbTQC4uEHANM3jSqXymFI6yWazP2KxWAXAL9zCUa1Wy2tXVxheKA9YNoR8Pt+aTqe4FVVVvz05O6MBhqUIBGk8Hn8HAOVy+T+XLJfLS4ZhTiRJgqIoVBRFIoric47jPnmeB1mW/9rr9ZpSSn3Lsmir1fJZlqWlUonKsvwWwD8ymc/nXwVBeLjf7xEKhdBut9Hr9WgmkyGEkJwsy5eHG5vN5g0AKIoCAEgkEkin0wQAfN9/cXPdheu6P33fBwB4ngcAcByHJpPJl+fn54mD3Gg0NrquXxeLRQAAwzAYj8cwTZPwPH9/sVg8PXweDAauqqr2cDjEer1GJBLBZDJBs9mE4zjwfZ85lAGg2+06hmGgXq+j3+/DsixYlgVN03a9Xu8jgCNCyIegIAgx13Vfd7vdu+FweG8YRkjXdWy329+dTgeSJD3ieZ7RNO0VAXAPwDEAO5VKndi2fWrb9jWl9Esul6PZbDY9Go1OZ7PZ9z/lyuD3OozU2wAAAABJRU5ErkJggg==)](http://dlmf.nist.gov/LaTeXML/)