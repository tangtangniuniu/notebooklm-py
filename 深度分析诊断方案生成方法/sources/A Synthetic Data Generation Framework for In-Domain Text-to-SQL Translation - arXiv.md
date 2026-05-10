> Source: https://arxiv.org/html/2509.25672v1

SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation





1. [1 Introduction](https://arxiv.org/html/2509.25672v1#S1 "In SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation")
2. [2 Related Work](https://arxiv.org/html/2509.25672v1#S2 "In SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation")
   1. [2.1 Synthetic Data Generation for Text-to-SQL](https://arxiv.org/html/2509.25672v1#S2.SS1 "In 2. Related Work ‣ SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation")
   2. [2.2 LLM Post-Training for Text-to-SQL](https://arxiv.org/html/2509.25672v1#S2.SS2 "In 2. Related Work ‣ SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation")
   3. [2.3 Text-to-SQL Systems](https://arxiv.org/html/2509.25672v1#S2.SS3 "In 2. Related Work ‣ SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation")
      1. [2.3.1 Schema Linking](https://arxiv.org/html/2509.25672v1#S2.SS3.SSS1 "In 2.3. Text-to-SQL Systems ‣ 2. Related Work ‣ SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation")
      2. [2.3.2 SQL Generation and Selection](https://arxiv.org/html/2509.25672v1#S2.SS3.SSS2 "In 2.3. Text-to-SQL Systems ‣ 2. Related Work ‣ SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation")
3. [3 In-Domain Text-to-SQL Synthesis Framework](https://arxiv.org/html/2509.25672v1#S3 "In SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation")
   1. [3.1 Sub-Schema Generation](https://arxiv.org/html/2509.25672v1#S3.SS1 "In 3. In-Domain Text-to-SQL Synthesis Framework ‣ SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation")
      1. [3.1.1 Table Level Sub-Schema Generation](https://arxiv.org/html/2509.25672v1#S3.SS1.SSS1 "In 3.1. Sub-Schema Generation ‣ 3. In-Domain Text-to-SQL Synthesis Framework ‣ SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation")
      2. [3.1.2 Column Level Sub-Schema Generation](https://arxiv.org/html/2509.25672v1#S3.SS1.SSS2 "In 3.1. Sub-Schema Generation ‣ 3. In-Domain Text-to-SQL Synthesis Framework ‣ SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation")
   2. [3.2 Synthetic Text-to-SQL Generation](https://arxiv.org/html/2509.25672v1#S3.SS2 "In 3. In-Domain Text-to-SQL Synthesis Framework ‣ SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation")
4. [4 Data Statistics](https://arxiv.org/html/2509.25672v1#S4 "In SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation")
5. [5 Text-to-SQL Translation](https://arxiv.org/html/2509.25672v1#S5 "In SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation")
   1. [5.1 Schema Linking](https://arxiv.org/html/2509.25672v1#S5.SS1 "In 5. Text-to-SQL Translation ‣ SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation")
   2. [5.2 Candidate Generation](https://arxiv.org/html/2509.25672v1#S5.SS2 "In 5. Text-to-SQL Translation ‣ SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation")
6. [6 Experiment Settings](https://arxiv.org/html/2509.25672v1#S6 "In SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation")
   1. [6.1 Dataset](https://arxiv.org/html/2509.25672v1#S6.SS1 "In 6. Experiment Settings ‣ SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation")
   2. [6.2 Evaluation Metrics](https://arxiv.org/html/2509.25672v1#S6.SS2 "In 6. Experiment Settings ‣ SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation")
   3. [6.3 Models and Hyperparameters](https://arxiv.org/html/2509.25672v1#S6.SS3 "In 6. Experiment Settings ‣ SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation")
7. [7 Results](https://arxiv.org/html/2509.25672v1#S7 "In SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation")
   1. [7.1 Text-to-SQL Translation Performance](https://arxiv.org/html/2509.25672v1#S7.SS1 "In 7. Results ‣ SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation")
   2. [7.2 Schema Filtering Performance](https://arxiv.org/html/2509.25672v1#S7.SS2 "In 7. Results ‣ SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation")
   3. [7.3 Context Management](https://arxiv.org/html/2509.25672v1#S7.SS3 "In 7. Results ‣ SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation")
8. [8 Discussion and Limitations](https://arxiv.org/html/2509.25672v1#S8 "In SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation")
9. [9 Conclusion](https://arxiv.org/html/2509.25672v1#S9 "In SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation")
10. [A Flawed SQL-to-Text Translation](https://arxiv.org/html/2509.25672v1#A1 "In SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation")
11. [B Illogical SQL-to-Text Pairs](https://arxiv.org/html/2509.25672v1#A2 "In SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation")
12. [C Separation of Columns Highly Used Together Limitation Example](https://arxiv.org/html/2509.25672v1#A3 "In SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation")
13. [D Schema Filtering Performance on Synthetic Data](https://arxiv.org/html/2509.25672v1#A4 "In SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation")
14. [E Sub-Schema and Synthetic Data Statistics](https://arxiv.org/html/2509.25672v1#A5 "In SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation")
15. [F Column Coverage Comparison for California Schools Database (Bird vs. Synthetic Dataset)](https://arxiv.org/html/2509.25672v1#A6 "In SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation")
16. [G Context Management Study](https://arxiv.org/html/2509.25672v1#A7 "In SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation")
17. [H Schema Table Column Filtration Prompt Template](https://arxiv.org/html/2509.25672v1#A8 "In SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation")
18. [I SQL Generation Prompt Template](https://arxiv.org/html/2509.25672v1#A9 "In SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation")

# SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation

Hasan Alp Caferoğlu
Bilkent UniversityAnkaraTurkey06800
[alp.caferoglu@bilkent.edu.tr](mailto:alp.caferoglu@bilkent.edu.tr)
, 
Mehmet Serhat Çelik
Bilkent UniversityAnkaraTurkey06800
[serhat.celik@ug.bilkent.edu.tr](mailto:serhat.celik@ug.bilkent.edu.tr)
 and 
Özgür Ulusoy
Bilkent UniversityAnkaraTurkey06800
[oulusoy@cs.bilkent.edu.tr](mailto:oulusoy@cs.bilkent.edu.tr)

###### Abstract.

Translating natural language questions into SQL has become a core challenge in enabling non-technical users to query databases. While recent work has explored large-scale synthetic data generation to improve model performance through post-training, most efforts emphasize cross-domain generalization. This leaves a gap for real-world enterprise scenarios, where models need to specialize to a single database schema and organizations require to be able to evaluate their Text-to-SQL systems on their own databases. To address this, we introduce SING-SQL1, a fully automated two-stage framework for generating high-quality, high-coverage synthetic Text-to-SQL data for any target database, without relying on SQL logs or manual annotations. Our approach hierarchically partitions a database schema into sub-schemas, synthesizes SQL queries across multiple complexity levels, and applies a quality-aware pipeline that includes LLM-as-a-judge validation, executability checks, automatic repair, and column balancing. We further release SingSQL-LM, a family of compact language models fine-tuned on the synthetic data, achieving strong in-domain generalization. On the subset of the BIRD benchmark, SingSQL-LM-3B-R64 reaches 82.87% Soft F1 and 73.03% EX upper bound with 32 candidates, outperforming the best 3B-scale baseline by +16.21 in Soft F1 and +12.36 in EX. At the 1.5B scale, SingSQL-LM-1.5B-R64 improves over prior systems by +9.30 in Soft F1 and +4.49 in EX. On synthetic evaluation sets, SingSQL-LMs exceed prior systems by wide margins, establishing state-of-the-art performance among open models at comparable scales. Moreover, our study of context management strategies reveals that schema-free fine-tuning combined with schema-only inference provides the most robust results. Together, these findings establish SING-SQL as a scalable, database-agnostic paradigm for producing and evaluating enterprise-grade Text-to-SQL systems.

11footnotetext: Artifacts have been made available at <https://github.com/HasanAlpCaferoglu/SING-SQL>.

## 1. Introduction

Translating natural language queries into structured query language (Text-to-SQL) has become a key area of interest for both academia and industry, as it enables non-technical users to query relational databases using natural language. Typical Text-to-SQL systems consist of several core components, including schema linking, SQL generation, SQL correction, and SQL selection. To improve performance at each stage of this workflow, fine-tuning large language models (LLMs) on task-specific data has become a common practice. However, such improvements often come at the cost of obtaining large-scale, high-quality annotated datasets, which are expensive and time-consuming to collect.

While prior work has proposed frameworks to synthetically generate labeled Text-to-SQL data  (Li et al., [2024c](https://arxiv.org/html/2509.25672v1#bib.bib18), [2025](https://arxiv.org/html/2509.25672v1#bib.bib17); Guo et al., [2025](https://arxiv.org/html/2509.25672v1#bib.bib10); Yang et al., [2024](https://arxiv.org/html/2509.25672v1#bib.bib43); Cheng et al., [2025](https://arxiv.org/html/2509.25672v1#bib.bib5)), most focus on the cross-domain setting—targeting generalization across diverse and unrelated databases. However, this setting does not reflect the needs of many real-world applications, where models are deployed in narrowly scoped environments and are expected to serve a specific organization operating on one or a few domain-specific databases. For example, an e-commerce company is unlikely to require querying a Formula 1 database, but instead needs highly accurate query generation over its internal, proprietary schema. In such scenarios, domain-specialized models trained with high-coverage in-domain data are far more beneficial than broadly generalized models.

To address this need, we introduce SING-SQL (Synthetic IN-domain Data Generation for Text-to-SQL), a framework designed to generate high-quality synthetic Text-to-SQL data tailored to any specific relational database. In addition, we present SingSQL-LM, a family of compact language models fine-tuned on the data produced by SING-SQL. We evaluate our approach on a subset of the BIRD benchmark as well as on our own synthetically generated in-domain dataset. Experimental results demonstrate that SING-SQL enables the creation of large volumes of high-quality, high-coverage domain-specific Text-to-SQL pairs. Such data can be leveraged by enterprises to fine-tune internal language models or to evaluate the performance of agentic systems operating in Text-to-SQL workflows.

In SING-SQL, we design a two-stage synthetic data generation framework. In the first stage, the target database is systematically partitioned into a diverse collection of sub-schemas, each defined by a unique combination of tables and column subsets. This decomposition is performed at two levels: first, at the table level, where joinable subsets of tables are selected; and second, at the column level, where a sliding window strategy is applied over non-key columns to generate multiple column-wise variations for each table. This hierarchical partitioning enables fine-grained control over the schema context of each example, reduces generation noise, and ensures semantic alignment between input questions and the underlying schema. By systematically varying both table and column configurations, the process promotes full database coverage across the synthesized dataset while keeping the generation process tractable and interpretable. In the second stage, we generate SQL queries for each sub-schema across multiple complexity levels—simple, moderate, challenging, and window—and translate them into natural language questions. To ensure data quality, we apply a series of filtering steps: first, an LLM-as-a-judge module evaluates the logical validity and semantic alignment of each SQL–Text pair; next, we test the executability of each SQL query and invoke automatic repair for non-executable cases when possible. For the subset of validated and executable examples, we instruct the model to generate step-by-step reasoning traces using a divide-and-conquer prompting strategy, enhancing interpretability and instructional value. Finally, to address schema imbalance, we perform a second round of column-focused SQL generation, targeting underrepresented columns based on usage frequency thresholds. Together, these components produce a high-quality, high-coverage synthetic dataset tailored for in-domain Text-to-SQL tasks.

Our key contributions can be summarized as follows:

* •

  We propose SING-SQL, a two-stage synthetic data generation framework designed for in-domain Text-to-SQL tasks. It generates high-quality, high-coverage SQL–Text pairs tailored to any specific relational database.
* •

  We introduce a hierarchical sub-schema construction strategy that partitions the database at both table and column levels, enabling controllable and semantically meaningful data generation while ensuring comprehensive schema coverage.
* •

  With SING-SQL, we present a quality-aware SQL–Text generation pipeline that incorporates complexity-controlled SQL synthesis, LLM-as-a-judge validation, executability checks, automatic SQL repair, and reasoning trace generation.
* •

  We address schema imbalance through a column-focused generation step, which targets underrepresented columns using frequency-based thresholds to improve column-level data coverage.
* •

  We release SingSQL-LM, a family of compact language models fine-tuned on the synthetic data produced by SING-SQL, and demonstrate their effectiveness on a subset of the BIRD benchmark and in-domain synthetic datasets.

## 2. Related Work

### 2.1. Synthetic Data Generation for Text-to-SQL

Large language models (LLMs) for Text-to-SQL often benefit from fine-tuning on curated datasets, either drawn from existing benchmarks (Pourreza and Rafiei, [2024](https://arxiv.org/html/2509.25672v1#bib.bib27); Pourreza et al., [2025a](https://arxiv.org/html/2509.25672v1#bib.bib25)) or synthesized to expand coverage across domains. A series of recent works propose diverse strategies for generating synthetic training data.

CODES (Li et al., [2024c](https://arxiv.org/html/2509.25672v1#bib.bib18)) constructs data from two sources: SQL-related corpora and NL-to-code datasets. It introduces a bi-directional augmentation procedure. In the question-to-SQL direction, proprietary LLMs generate user-like questions from real examples, followed by SQL generation. In the SQL-to-question direction, SQL queries are paired with template-based questions, which are then rephrased by LLMs to improve naturalness. Yang et al.  (Yang et al., [2024](https://arxiv.org/html/2509.25672v1#bib.bib43)) synthesizes training data in two complementary phases. First, strong proprietary LLMs are used to synthesize diverse, high-quality Text-to-SQL pairs across domains, thereby avoiding over-representation of specific schemas. This strong data is used to enhance the base model’s Text-to-SQL translation capabilities. Next, through preference learning, weak data is generated from smaller LLMs by sampling candidate SQLs, labeling them through execution agreement with gold queries, and applying Direct Preference Optimization (DPO) on positive/negative pairs. OMNISQL(Li et al., [2025](https://arxiv.org/html/2509.25672v1#bib.bib17)) scales up data generation by first synthesizing realistic databases from web tables via LLMs, ensuring broad domain coverage. SQL queries are then produced with complexity-aware strategies to balance query difficulty, followed by back-translation into natural questions. To enrich linguistic diversity, questions are paraphrased in different language styles. Additionally, chain-of-thought (CoT) rationales(Kojima et al., [2022](https://arxiv.org/html/2509.25672v1#bib.bib14); Wei et al., [2024](https://arxiv.org/html/2509.25672v1#bib.bib41)) are generated alongside each question-SQL pair to provide auxiliary training signals and interpretability. A synthetic Text-to-SQL framework SQLForge  (Guo et al., [2025](https://arxiv.org/html/2509.25672v1#bib.bib10)) focus on the reliability and diversity of the generated data in four-stage. Initially, An AST-based SQL Parser turns seed queries into grammar-preserving templates and enriches them by subtree crossover. Secondly, SQL foundry stage, iteratively explores new domains by jointly proposing domain names with auxiliary SQL to prevent domain drift. Then, for the synthesized SQL statements, corresponding database schema expression is generated via schema architect stage. Finally, a schema-aware reverse translator produces human-readable questions that reflect the SQL’s intent. SQLord (Cheng et al., [2025](https://arxiv.org/html/2509.25672v1#bib.bib5)) addresses data scarcity by exploiting developer-authored SQL queries and their comments. A model called RevLLM is trained on a small set of SQL–comment pairs to generate natural questions for SQL queries. Using RevLLM, large-scale pseudo-labeled question–SQL pairs are synthesized, which in turn train a specialized Text-to-SQL model. Shkapenyuk et al. (Shkapenyuk et al., [2025](https://arxiv.org/html/2509.25672v1#bib.bib36)) take a different angle by focusing on metadata extraction through profiling, query log analysis, and SQL-to-text generation.

Most prior works primarily focus on cross-domain data synthesis to improve generalization across databases. However, in enterprise contexts, organizations often require models specialized for their own databases. Recent efforts move in this direction. TailorSQL (Vaidya et al., [2025](https://arxiv.org/html/2509.25672v1#bib.bib38)) constructs a workload-aware retrieval corpus by synthesizing documents from both schema and query logs, using LLMs to generate natural-language questions conditioned on SQL and schema. However, it primarily improves performance through prompt augmentation rather than large-scale data generation and post-training. Having a similar objective to our work, SelectCraft (Chafik et al., [2025](https://arxiv.org/html/2509.25672v1#bib.bib4)) introduces a domain-specific data generation framework that synthesizes SQL queries by mimicking real-world query distributions over existing databases. Its controllability is limited to distributional aspects of SQL components (e.g., operators, conditions, join counts and types), but it does not enable fine-grained control over database elements such as tables or columns, nor does it address scalability to large and complex schemas. In parallel, SiriusBI (Jiang et al., [2025](https://arxiv.org/html/2509.25672v1#bib.bib13)) introduces an automated pipeline for domain-specific data generation, with optional manual verification to further enhance quality assurance. The system aims to mitigate the sharp performance drops often observed when models are transferred across domains with limited generalization capacity. However, SiriusBI primarily leverages SQL query logs, which are not always available, and it lacks mechanisms for fine-grained control over schema elements. As a result, while it provides a practical solution for reducing domain transfer bottlenecks, its capacity for scaling to complex schemas or enforcing systematic schema coverage remains limited.

Our work, SING-SQL, addresses this gap by enabling enterprises to curate Text-to-SQL data tailored to their schema without relying on prior workloads. It enforces comprehensive schema coverage through hierarchical sub-schema construction and targeted column balancing, while ensuring complexity-controlled data via quality-aware SQL–Text synthesis, thereby moving beyond the cross-domain paradigm.

### 2.2. LLM Post-Training for Text-to-SQL

Out-of-the-box, open-source LLMs generally underperform proprietary counterparts on Text-to-SQL benchmarks. Recent work shows, however, that with targeted post-training strategies using synthetic data, open-source models can achieve competitive or even superior performance.

Supervised fine-tuning (SFT) has been the most widely used method for adapting models to Text-to-SQL corpora (Pourreza and Rafiei, [2024](https://arxiv.org/html/2509.25672v1#bib.bib27); Gao et al., [2024](https://arxiv.org/html/2509.25672v1#bib.bib8); Wang et al., [2024](https://arxiv.org/html/2509.25672v1#bib.bib39); Talaei et al., [2024](https://arxiv.org/html/2509.25672v1#bib.bib37); Pourreza et al., [2025a](https://arxiv.org/html/2509.25672v1#bib.bib25); Li et al., [2025](https://arxiv.org/html/2509.25672v1#bib.bib17); Liu et al., [2025b](https://arxiv.org/html/2509.25672v1#bib.bib21); Sheng et al., [2025](https://arxiv.org/html/2509.25672v1#bib.bib34)). Beyond SFT, direct preference optimization (DPO), a preference learning technique, has been utilized to further align models with desired behaviors (Rafailov et al., [2023](https://arxiv.org/html/2509.25672v1#bib.bib30); Yang et al., [2024](https://arxiv.org/html/2509.25672v1#bib.bib43)). More recently, reinforcement learning (RL) methods have been explored to strengthen LLM reasoning. Group Relative Policy Optimization (GRPO)(Shao et al., [2024](https://arxiv.org/html/2509.25672v1#bib.bib31)) has been applied to incorporate reward signals, demonstrating promising improvements in Text-to-SQL systems (Yao et al., [2025](https://arxiv.org/html/2509.25672v1#bib.bib45); Pourreza et al., [2025b](https://arxiv.org/html/2509.25672v1#bib.bib28)). Hybrid post-training pipelines that combine SFT with RL-based optimization also explored to enhance model performance by leveraging both supervised and reward-driven signals (Sheng and Xu, [2025a](https://arxiv.org/html/2509.25672v1#bib.bib32), [b](https://arxiv.org/html/2509.25672v1#bib.bib33); Ma et al., [2025](https://arxiv.org/html/2509.25672v1#bib.bib22); Papicchio et al., [2025](https://arxiv.org/html/2509.25672v1#bib.bib24)).

Despite these advances, reinforcement learning methods can be computationally expensive and difficult to scale for small enterprise settings. In our work, we adopt a parameter-efficient alternative: supervised fine-tuning with Low-Rank Adaptation (LoRA) (Hu et al., [2022](https://arxiv.org/html/2509.25672v1#bib.bib11)), enabling scalable specialization of open-source models to enterprise databases without the overhead of RL training.

### 2.3. Text-to-SQL Systems

#### 2.3.1. Schema Linking

As the context length and capabilities of LLMs increase, more information can be inserted into prompt. The contextual information becomes important and effect the system performance (Chung et al., [2025](https://arxiv.org/html/2509.25672v1#bib.bib6)). One of the component of the context for the Text-to-SQL systems is database schema. Although there are works  (Caferoğlu and Özgür Ulusoy, [2025](https://arxiv.org/html/2509.25672v1#bib.bib2); Maamari et al., [2024](https://arxiv.org/html/2509.25672v1#bib.bib23)) stating the schema filtering is not needed as the the model capabilities and context length increase since models can identify relevant schema component during SQL generation, best performing Text-to-SQL systems  (Pourreza et al., [2025a](https://arxiv.org/html/2509.25672v1#bib.bib25); Shkapenyuk et al., [2025](https://arxiv.org/html/2509.25672v1#bib.bib36); Liu et al., [2025b](https://arxiv.org/html/2509.25672v1#bib.bib21); Talaei et al., [2024](https://arxiv.org/html/2509.25672v1#bib.bib37); Pourreza et al., [2025b](https://arxiv.org/html/2509.25672v1#bib.bib28)) shows the effectiveness of schema filtering and utilize it to achieve high performance. TA-SQL (Qu et al., [2024](https://arxiv.org/html/2509.25672v1#bib.bib29)) leverages initially generated dummy SQL queries to improve schema linking performance. Similarly, with the help of an LLM, Gen-SQL  (Shi et al., [2025](https://arxiv.org/html/2509.25672v1#bib.bib35)) construct a pseudo-SQL and then pseudo-schema solely based on the question without providing the database schema. Leveraging embedding based retriever to eliminate the irrelevant schema components, pseudo-schema is grounded in actual database schema. ExSL (Glass et al., [2025](https://arxiv.org/html/2509.25672v1#bib.bib9)) proposes a decoder-only approach that reformulates schema linking as an extraction task rather than a generative one. ExSL treats all schema columns as candidates and predicts their relevance using hidden states from the LLM, enabling efficient probability estimation. PSM-SQL  (Yang et al., [2025](https://arxiv.org/html/2509.25672v1#bib.bib44)) couples multi-granularity semantics with a chain-loop pruning strategy for schema linking. Solid-SQL  (Liu et al., [2025a](https://arxiv.org/html/2509.25672v1#bib.bib20)) enhances schema linking by parsing gold SQL to obtain supervision and fine-tuning a schema selector with paraphrase-augmented data to improve robustness against synonyms and rephrasings. Schema linking model predictions are integrated into prompts via a “focus on” mechanism that highlights selected tables and columns while retaining full-schema context for fault tolerance. RSL-SQL (Cao et al., [2024](https://arxiv.org/html/2509.25672v1#bib.bib3)) introduces bidirectional schema linking that unions an LLM-extracted schema with a schema parsed from a preliminary SQL, producing a pruned schema that preserves high recall. For schema linking, CHESS (Talaei et al., [2024](https://arxiv.org/html/2509.25672v1#bib.bib37)) employs an LLM-based schema selector that filters relevant tables and columns, guided by candidate values retrieved through an LSH-based entity matching mechanism and enriched with column descriptions extracted from a vector database. In our work, we adopt the LSH-based entity matching mechanism from CHESS  (Talaei et al., [2024](https://arxiv.org/html/2509.25672v1#bib.bib37)) and incorporate synthetic Text-to-SQL data to enhance LLM-based column filtering.

#### 2.3.2. SQL Generation and Selection

For a single user question, generating multiple SQL queries is best practice for the Text-to-SQL translation systems in order to improve system performance.  (Wang et al., [2024](https://arxiv.org/html/2509.25672v1#bib.bib39); Li et al., [2024b](https://arxiv.org/html/2509.25672v1#bib.bib16); Lee et al., [2024](https://arxiv.org/html/2509.25672v1#bib.bib15); Talaei et al., [2024](https://arxiv.org/html/2509.25672v1#bib.bib37); Pourreza et al., [2025a](https://arxiv.org/html/2509.25672v1#bib.bib25); Liu et al., [2025b](https://arxiv.org/html/2509.25672v1#bib.bib21); Sheng and Xu, [2025a](https://arxiv.org/html/2509.25672v1#bib.bib32), [b](https://arxiv.org/html/2509.25672v1#bib.bib33)). As the number of candidate SQL query increases, the system performance increases upto a point.  (Talaei et al., [2024](https://arxiv.org/html/2509.25672v1#bib.bib37); Pourreza et al., [2025a](https://arxiv.org/html/2509.25672v1#bib.bib25)). In addition to multiple SQL generation, Text-to-SQL systems contain self-correction  (Caferoğlu and Özgür Ulusoy, [2025](https://arxiv.org/html/2509.25672v1#bib.bib2); Pourreza et al., [2025a](https://arxiv.org/html/2509.25672v1#bib.bib25); Pourreza and Rafiei, [2023](https://arxiv.org/html/2509.25672v1#bib.bib26); Li et al., [2024b](https://arxiv.org/html/2509.25672v1#bib.bib16)) module to fix or refine the generated SQL queries to improve the system performance. Self-consistency (Wang et al., [2023](https://arxiv.org/html/2509.25672v1#bib.bib40)) is another technique utilized largely by Text-to-SQL systems (Dong et al., [2023](https://arxiv.org/html/2509.25672v1#bib.bib7); Lee et al., [2024](https://arxiv.org/html/2509.25672v1#bib.bib15); Xie et al., [2025](https://arxiv.org/html/2509.25672v1#bib.bib42)). In our work, we do not employ self-consistency or self-correction to solely measure the model Text-to-SQL translation capability.

![Refer to caption](figures/synthetic_t2s_generation.png)


Figure 1. Overview of the Synthetic Data Generation Framework

## 3. In-Domain Text-to-SQL Synthesis Framework

To enable comprehensive supervision over all components of a target database, we introduce a two-stage framework for in-domain synthetic Text-to-SQL generation. The first stage involves partitioning the database into a diverse set of sub-schemas, varying in size and structure, to capture different combinations of schema elements. This step ensures that each table and column is systematically included in at least one context. In the second stage, we generate synthetic Text-to-SQL examples conditioned on each sub-schema, enabling fine-grained alignment between natural language questions and the underlying database structure. The resulting dataset achieves high coverage and semantic diversity, enabling more reliable post-training and comprehensive evaluation. The SING-SQL framework is further detailed in Algorithm [1](https://arxiv.org/html/2509.25672v1#alg1 "Algorithm 1 ‣ 3. In-Domain Text-to-SQL Synthesis Framework ‣ SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation").

Algorithm 1  General Synthetic Data Generation Algorithm for Single Database

1:window ww, stride ss, table counts for sub-schemas t​ctc

2:t2sExamples

3:subSchemas ←\leftarrow ConstructSubSchemas(ww, ss, t​ctc)

4:t2sExamples ←\leftarrow GenT2S(SubSchemas)

5:columnCounts ←\leftarrow CountCols(t2sExamples)

6:focusColumns ←\leftarrow GetFocusCols(columnCounts)
⊳\triangleright Identify underrepresented or critical columns

7:focusSubSchemas ←\leftarrow FindFocusSchemas(focusColumns)
⊳\triangleright Sub-schemas that include the targeted columns

8:colFocusedT2SExamples ←\leftarrow GenT2S(focusSubSchemas)
⊳\triangleright Generate more examples focusing on underused columns

9:t2sExamples ←\leftarrow t2sExamples ++ colFocusedT2SExamples

10:t2sExamples ←\leftarrow filter(t2sExamples)
⊳\triangleright Removing logically/syntactically incorrect pairs

### 3.1. Sub-Schema Generation

Effective in-domain Text-to-SQL synthesis demands controllability, semantic fidelity, and comprehensive schema coverage. However, considering the entire database schema when generating synthetic data is often impractical—especially for large-scale databases—due to the context length limitations of large language models (LLMs), reduced control over the generation process, and challenges in maintaining high semantic alignment between natural language questions and their corresponding SQL queries.

To address these issues, we introduce a sub-schema generation approach that partitions the original database into smaller, manageable segments. Each sub-schema is composed of a limited number of relationally connected tables and portions of their columns, enabling focused and interpretable contexts for generation. This strategy offers several key advantages. First, it provides fine-grained control over the scope of each example, allowing the generation process to focus on specific parts of the schema. Second, by narrowing the schema context, it reduces noise and improves the semantic alignment between natural language questions and their corresponding SQL queries. Third, by systematically varying the structure and composition of sub-schemas, we ensure that all schema elements appear across diverse relational settings. This not only enhances the diversity of the generated data but also ensures thorough coverage of the database, which is especially important for large and complex schemas. Overall, this step lays a strong foundation for generating high-quality, diverse, and semantically grounded Text-to-SQL pairs. The complete sub-schema generation procedure is formally described in Algorithms  [2](https://arxiv.org/html/2509.25672v1#alg2 "Algorithm 2 ‣ 3.1. Sub-Schema Generation ‣ 3. In-Domain Text-to-SQL Synthesis Framework ‣ SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation"),  [3](https://arxiv.org/html/2509.25672v1#alg3 "Algorithm 3 ‣ 3.1.1. Table Level Sub-Schema Generation ‣ 3.1. Sub-Schema Generation ‣ 3. In-Domain Text-to-SQL Synthesis Framework ‣ SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation") and  [4](https://arxiv.org/html/2509.25672v1#alg4 "Algorithm 4 ‣ 3.1.2. Column Level Sub-Schema Generation ‣ 3.1. Sub-Schema Generation ‣ 3. In-Domain Text-to-SQL Synthesis Framework ‣ SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation"), and is further illustrated in Figure  [1](https://arxiv.org/html/2509.25672v1#S2.F1 "Figure 1 ‣ 2.3.2. SQL Generation and Selection ‣ 2.3. Text-to-SQL Systems ‣ 2. Related Work ‣ SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation") to provide a visual understanding of the process.

Algorithm 2  Sub-Schema Construction Algorithm (ConstructSubSchemas)

1:window ww, stride ss, table counts for sub-schemas t​ctc

2:columnLevelSubSchemas

3:tableLevelSubSchemas ←\leftarrow GenTableLevelSubSchemas(t​ctc)

4:columnLevelSubSchemas ←\leftarrow GenColumnLevelSubSchemas(tableLevelSubSchemas, ww, ss)

#### 3.1.1. Table Level Sub-Schema Generation

We begin sub-schema construction at the table level by identifying meaningful subsets of tables that preserve database integrity and relational connectivity. As outlined in Algorithm [3](https://arxiv.org/html/2509.25672v1#alg3 "Algorithm 3 ‣ 3.1.1. Table Level Sub-Schema Generation ‣ 3.1. Sub-Schema Generation ‣ 3. In-Domain Text-to-SQL Synthesis Framework ‣ SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation"), all joinable tables are first extracted using the foreign key constraints defined in the database schema. In cases where foreign key information is incomplete or missing, the schema must be updated or manually annotated to restore valid join paths and ensure relational completeness. This step is essential for constructing sub-schemas capable of supporting executable and semantically meaningful SQL queries. In the next step, we enumerate all valid table combinations that maintain joinability—i.e., every table within a combination must be transitively joinable with the others.

To ensure practical relevance and avoid overly complex sub-schemas, we introduce a hyperparameter that limits the maximum number of tables per sub-schema. This constraint reflects the observation that real-world SQL queries rarely involve all tables in a schema, especially in large databases. For instance, in the Card Games database from the BIRD dev set, which contains 6 tables, setting the maximum number of tables per sub-schema to 3 can lead to more manageable and potentially more realistic combinations. While this value may vary depending on the schema complexity and target use case, it serves as a practical upper bound that helps constrain the sub-schema space. In addition to guiding the realism of generated queries, this hyperparameter also prevents an explosion in the number of possible sub-schemas, making the overall synthesis process more computationally feasible. To offer further insights, Appendix [E](https://arxiv.org/html/2509.25672v1#A5 "Appendix E Sub-Schema and Synthetic Data Statistics ‣ SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation") presents sub-schema statistics across a range of SING-SQL parameters.

Algorithm 3  Table Level Sub Schema Construction (Generation) Algorithm (GenTableLevelSubSchemas)

1:table counts for sub-schemas t​ctc

2:tableLevelSubSchemas
⊳\triangleright tlss = table level sub-schemas

3:joinableTables ←\leftarrow GetJoinableTables

4:AllTableCombinations ←\leftarrow GetAllDBTableComb

5:tableLevelSubSchemas ←\leftarrow FindSubSchemas(joinableTables, AllTableCombinations) ⊳\triangleright Ensure that all tables in a table combination can joinable and are able to construct a sub-schema

#### 3.1.2. Column Level Sub-Schema Generation

Building on the table-level sub-schemas, we further refine the schema context by selecting subsets of columns for each table, yielding column-level sub-schemas. For each table in a given table-level sub-schema, we begin by including all connection columns, defined as primary keys and columns participating in foreign key relationships. These columns are essential for preserving the relational structure across tables and ensuring that the synthesized SQL queries will be executable and semantically valid.

The remaining non-connection columns are then considered for selective inclusion using a controlled sliding window strategy. Two hyperparameters govern this process: the window size ww, which specifies the number of non-connection columns selected at a time, and the stride ss, which determines the number of positions the window shifts after each selection. Prior to windowing, the non-connection columns of each table are randomly shuffled to increase variation. The sliding window is then applied to generate multiple column subsets for each table.

These subsets are combined across tables using a Cartesian product to yield diverse column-level sub-schemas derived from the original table-level sub-schema. Compared to an exhaustive enumeration of all possible column combinations—which would lead to a combinatorial explosion in the number of sub-schemas, making exhaustive enumeration impractical—this strategy offers a scalable and tunable mechanism for achieving both coverage and diversity in the generated data.

This hierarchical construction—first over tables, and then over columns—yields a rich and diverse collection of sub-schemas with varying granularity. It enables fine-grained control over schema exposure during data generation while maintaining syntactic validity and semantic coherence. A visual overview of this process is provided in Figure [1](https://arxiv.org/html/2509.25672v1#S2.F1 "Figure 1 ‣ 2.3.2. SQL Generation and Selection ‣ 2.3. Text-to-SQL Systems ‣ 2. Related Work ‣ SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation"), and the full column-level sub-schema construction procedure is detailed in Algorithm [4](https://arxiv.org/html/2509.25672v1#alg4 "Algorithm 4 ‣ 3.1.2. Column Level Sub-Schema Generation ‣ 3.1. Sub-Schema Generation ‣ 3. In-Domain Text-to-SQL Synthesis Framework ‣ SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation").In Appendix [E](https://arxiv.org/html/2509.25672v1#A5 "Appendix E Sub-Schema and Synthetic Data Statistics ‣ SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation"), we present sub-schema statistics for various SING-SQL parameters to provide further insights.

Algorithm 4  Column-Level Sub-Schema Construction (GenColumnLevelSubSchemas)

1:window size ww, stride ss, tableLevelSubSchemas

2:columnLevelSubSchemas

3:Initialize columnLevelSubSchemas ←\leftarrow [ ]

4:for each tlss in tableLevelSubSchemas do

5:  Initialize tableColumnParts ←\leftarrow empty dictionary

6:  for each table in tlss do

7:   connCols ←\leftarrow GetConnectionColumns(table)

8:   nonConnCols ←\leftarrow AllColumns(table) ∖\setminus connCols

9:   if nonConnCols is empty then

10:     tableColumnParts[table] ←\leftarrow [connCols]

11:   else

12:     Randomly shuffle nonConnCols

13:     Initialize colParts ←\leftarrow [ ]

14:     i←0i\leftarrow 0

15:     while i<i< len(nonConnCols) do

16:      portion ←\leftarrow nonConnCols[ii : i+wi+w]

17:      portion ←\leftarrow connCols ++ portion

18:      Append portion to colParts

19:      i←i+si\leftarrow i+s

20:     end while

21:     tableColumnParts[table] ←\leftarrow colParts

22:   end if

23:  end for

24:  colLevelSchemas ←\leftarrow Cartesian product of all table-column partitions in tableColumnParts

25:  for each schema in colLevelSchemas do

26:   Append newSchema to columnLevelSubSchemas

27:  end for

28:end for

29:return columnLevelSubSchemas

### 3.2. Synthetic Text-to-SQL Generation

Following the construction of diverse sub-schemas, the second stage of our framework focuses on synthesizing high-quality natural language and SQL query pairs. Unlike prior work (Li et al., [2024c](https://arxiv.org/html/2509.25672v1#bib.bib18); Yang et al., [2024](https://arxiv.org/html/2509.25672v1#bib.bib43)) that typically follows a Text-to-SQL approach—generating natural language questions first and then deriving the corresponding SQL—we adopt the reverse paradigm. Specifically, we first generate SQL queries and subsequently translate them into natural language questions. This decision is motivated by findings from prior work such as OMNI-SQL (Li et al., [2025](https://arxiv.org/html/2509.25672v1#bib.bib17)), which demonstrate that SQL-to-Text generation is generally more reliable due to the greater flexibility and expressiveness of natural language.

For each sub-schema, the large language model (LLM) is prompted to generate NN SQL queries spanning four predefined complexity levels: simple, moderate, challenging, and window. The first three levels are consistent with those adopted in established benchmarks such as BIRD, while the window level is introduced to explicitly control for the inclusion of window functions—an area where LLMs tend to struggle when left unguided. By defining this complexity level explicitly, we avoid relying solely on model inference to ensure such queries are included. In our work, we use N=3N=3, resulting twelve SQL-Text pair generation for each sub-schema. To encourage broad schema coverage, we explicitly instruct the model to utilize all available tables and columns in the sub-schema during SQL generation.

Although SQL-to-Text synthesis yields more semantically aligned pairs compared to the reverse direction, errors may still occur—such as flawed natural language translations or illogical SQL-question pairs (see Appendix [A](https://arxiv.org/html/2509.25672v1#A1 "Appendix A Flawed SQL-to-Text Translation ‣ SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation") and Appendix [B](https://arxiv.org/html/2509.25672v1#A2 "Appendix B Illogical SQL-to-Text Pairs ‣ SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation")). To identify and eliminate such issues, we introduce a validation stage in which the LLM is employed as a judge (LLM-as-a-judge). Each SQL–Text pair is evaluated within the context of its sub-schema, and pairs exhibiting misalignment, ambiguity, or logical flaws are discarded.

Subsequently, we assess the executability of each synthetic SQL query. Queries that fail to execute are passed through an automated repair step using the LLM. If the query remains non-executable after correction attempts, it is excluded from the dataset. Once a validated and executable set of SQL–Text pairs is obtained, we further enrich the dataset by generating accompanying reasoning traces. These traces are constructed using a divide-and-conquer prompting strategy inspired by CHASE-SQL (Pourreza et al., [2025a](https://arxiv.org/html/2509.25672v1#bib.bib25)), which aims to improve the interpretability of the data and instructional signal of the synthetic examples for LLMs.

To promote sufficient schema coverage in the final dataset, we introduce an additional column-focused synthesis step. Following the first data generation round, we calculate the occurrence frequency of each column within the synthesized SQL queries. Columns that appear fewer times than a predefined threshold are considered underrepresented and are flagged for targeted inclusion. Sub-schemas containing these low-frequency columns are then reselected, and a second round of SQL–Text generation is performed. During this iteration, the LLM is explicitly instructed to focus on incorporating the underused columns into the generated SQL queries. While this strategy does not guarantee equal representation across all columns, it effectively eliminates extremely low-frequency cases and enforces a minimum level of exposure for each column, thereby improving overall schema coverage.

An overview of the complete synthesis workflow is illustrated in Figure [1](https://arxiv.org/html/2509.25672v1#S2.F1 "Figure 1 ‣ 2.3.2. SQL Generation and Selection ‣ 2.3. Text-to-SQL Systems ‣ 2. Related Work ‣ SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation"), and the corresponding procedure is detailed in Algorithm [5](https://arxiv.org/html/2509.25672v1#alg5 "Algorithm 5 ‣ 3.2. Synthetic Text-to-SQL Generation ‣ 3. In-Domain Text-to-SQL Synthesis Framework ‣ SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation").

Algorithm 5  Synthetic Text-to-SQL Generation Algorithm (GenT2S)

1:columnLevelSubSchemas

2:t2sExamples

3:Initialize t2sExamples ←\leftarrow []

4:for each subSchema in columnLevelSubSchemas do

5:  SQL2TextExamples ←\leftarrow GenerateWithLLM

6:  for each SQL2TextItem in SQL2TextExamples do

7:   isLogical ←\leftarrow EvaluateSQL2TextItem(SQL2TextItem)

8:   if isLogical then

9:     isExecutable ←\leftarrow ExecuteSQL(SQL)

10:     if isExecutable is False then

11:      SQL2TextItem ←\leftarrow FixSQL(SQL2TextItem)

12:     end if

13:     GenerateReasoning(SQL2TextItem)

14:     Append SQL2TextItem to t2sExamples

15:   end if

16:  end for

17:end for

18:return t2sExamples

## 4. Data Statistics

To better understand the characteristics of our synthetic dataset and to compare it with the BIRD benchmark, we analyze both dataset composition and SQL query statistics across multiple dimensions. In particular, we examine question distributions across levels, join counts, and aggregation usage, which are widely adopted indicators of SQL complexity and diversity. We also investigate schema coverage, as incomplete coverage may hinder reliable evaluation.

Table [1](https://arxiv.org/html/2509.25672v1#S4.T1 "Table 1 ‣ 4. Data Statistics ‣ SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation") summarizes the distribution of questions across levels for the California Schools database. BIRD-Dev is dominated by simple and moderate queries (94.4% in total), with very few challenging (5) or window (2) queries. In contrast, our synthetic splits yield a substantially larger number of questions with a more balanced distribution, including large number of challenging and window queries. This broader coverage ensures that models trained on the synthetic dataset are exposed to a wider variety of SQL patterns. This also enables evaluation under more realistic data analysis scenarios, where complex queries involving multiple tables and conditions are prevalent.

Figure [2](https://arxiv.org/html/2509.25672v1#S4.F2 "Figure 2 ‣ 4. Data Statistics ‣ SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation") reports the average number of joins per SQL across different difficulty levels. We observe that the synthetic data exhibits comparable or slightly higher join complexity than BIRD, except simple questions. This suggests that our generation process successfully incorporates complex relational reasoning patterns.

Similarly, Figure [3](https://arxiv.org/html/2509.25672v1#S4.F3 "Figure 3 ‣ 4. Data Statistics ‣ SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation") illustrates the distribution of queries with aggregation operators. While BIRD-Dev has a larger fraction of aggregations in the simple category (31.48%), our synthetic data introduces a higher proportion of aggregation in moderate, challenging, and window queries, reaching up to 78.76% in the challenging level.

Table [2](https://arxiv.org/html/2509.25672v1#S4.T2 "Table 2 ‣ 4. Data Statistics ‣ SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation") further highlights a limitation of the BIRD development split: 15 columns (16.85% of the schema) in the California Schools database remain completely unused. This under-utilization implies that BIRD-Dev cannot fully measure the performance of Text-to-SQL systems on queries involving these columns, nor capture potential interactions among them. In contrast, our synthetic dataset achieves complete coverage across all columns in the train, dev, and test splits, thereby enabling more comprehensive evaluation and supervision over the entire schema. Column coverage comparison for California Schools database provided in Appendix [F](https://arxiv.org/html/2509.25672v1#A6 "Appendix F Column Coverage Comparison for California Schools Database (Bird vs. Synthetic Dataset) ‣ SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation").

Together, these results demonstrate that the synthetic dataset is not only well aligned with the BIRD benchmark but also offers richer coverage of SQL constructs and schema elements at higher complexity levels, providing stronger supervision for training and evaluation of Text-to-SQL systems. Moreover, since our SING-SQL framework is database-agnostic, it can be applied to arbitrary databases, facilitating better schema alignment for LLMs and enabling more comprehensive evaluation.

Table 1. Question counts per difficulty level for the California Schools database in BIRD-Dev and synthetic splits.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Dataset | Overall | Simple | Moderate | Challenging | Window |
| BIRD-Dev | 89 | 54 | 30 | 5 | 2 |
| Synthetic Train | 34,266 | 8,685 | 8,556 | 8,046 | 9,286 |
| Synthetic Dev | 1,124 | 297 | 259 | 259 | 319 |
| Synthetic Test | 1,124 | 299 | 248 | 248 | 340 |

![Refer to caption](figures/join_cnt_per_sql_per_level.png)


Figure 2. Join Count Comparison of Bird and Synthetic Data

![Refer to caption](figures/agg_percentage_for_each_level_across_dataset.png)


Figure 3. Aggregation Comparison of Bird and Synthetic Data




Table 2. Unused column statistics for the California Schools database.

|  |  |  |
| --- | --- | --- |
| Dataset | Unused Column Count | Unused Column Rate (%) |
| Bird-Dev | 15 | 16.85 |
| Synthetic Train | 0 | 0.0 |
| Synthetic Dev | 0 | 0.0 |
| Synthetic Test | 0 | 0.0 |

![Refer to caption](figures/sing_sql_schema_filtering.png)


Figure 4. Overview of the SING-SQL Schema Filtering

## 5. Text-to-SQL Translation

A typical Text-to-SQL translation pipeline consists of four core components: schema linking, candidate generation, candidate refinement, and candidate selection. In this work, our focus is on evaluating the SQL generation capabilities of models without constructing a full agentic pipeline. Therefore, we restrict our experiments to the schema linking and candidate generation stages. As detailed in Section [2](https://arxiv.org/html/2509.25672v1#S2 "2. Related Work ‣ SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation"), unlike prior studies, our approach leverages synthetically generated *in-domain* Text-to-SQL data for both schema linking and the construction of few-shot examples for SQL generation.

### 5.1. Schema Linking

Our schema linking process is partly driven by synthetically generated in-domain Text-to-SQL pairs. To retrieve relevant synthetic examples and associated database items, we first extract keywords from the input question following the approach in CHESS (Talaei et al., [2024](https://arxiv.org/html/2509.25672v1#bib.bib37)). Relying solely on individual keywords can be limiting, as questions often contain multiple terms whose combinational usage influences retrieval quality. To address this, we expand the search space by forming *keyword pairs*, enabling more precise matching against synthetic examples.

For retrieving synthetic question–SQL pairs, we implement a retrieval process that operates over both the question and SQL text. Specifically, we experiment with two methods: (1) BM25 lexical matching, and (2) semantic search using dense vector representations. While both approaches are capable of identifying relevant examples, semantic search is substantially slower in practice. Considering real-world deployment scenarios, we therefore adopt BM25 as our primary retrieval method due to its efficiency. In parallel, we retrieve relevant database columns and entities, following CHESS (Talaei et al., [2024](https://arxiv.org/html/2509.25672v1#bib.bib37)), to further enhance the schema linking process. Finally, we filter the candidate database tables using the retrieved synthetic examples, relevant columns, and entities, ensuring a focused and schema-consistent context for downstream SQL generation.

### 5.2. Candidate Generation

After schema filtering, we generate multiple SQL candidates following the general strategy adopted in prior work  (Wang et al., [2024](https://arxiv.org/html/2509.25672v1#bib.bib39); Li et al., [2024b](https://arxiv.org/html/2509.25672v1#bib.bib16); Lee et al., [2024](https://arxiv.org/html/2509.25672v1#bib.bib15); Talaei et al., [2024](https://arxiv.org/html/2509.25672v1#bib.bib37); Pourreza et al., [2025a](https://arxiv.org/html/2509.25672v1#bib.bib25); Liu et al., [2025b](https://arxiv.org/html/2509.25672v1#bib.bib21); Sheng and Xu, [2025a](https://arxiv.org/html/2509.25672v1#bib.bib32), [b](https://arxiv.org/html/2509.25672v1#bib.bib33)). Here again, our in-domain synthetic dataset plays a central role. Using the same keyword-pair retrieval process described in the schema linking stage, we identify the most relevant synthetic examples for the input question. We then rank these examples by similarity and select the top-kk as few-shot demonstrations for the LLM. This targeted retrieval ensures that the few-shots are both semantically relevant and schema-consistent. In addition, we incorporate detailed column metadata—such as semantic descriptions or representative values—into the prompt, providing richer context for the model during SQL generation.

## 6. Experiment Settings

### 6.1. Dataset

We conduct experiments on the California Schools database from the BIRD development benchmark (Li et al., [2024a](https://arxiv.org/html/2509.25672v1#bib.bib19)), as well as on our synthetically generated in-domain dataset produced by the database-agnostic SING-SQL framework. While BIRD-Dev provides a limited set of 89 questions, heavily skewed toward simple and moderate difficulty, our synthetic dataset achieves full schema coverage and a more balanced distribution across difficulty levels, including a substantial number of challenging and window queries, as shown in Table [1](https://arxiv.org/html/2509.25672v1#S4.T1 "Table 1 ‣ 4. Data Statistics ‣ SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation").

### 6.2. Evaluation Metrics

We evaluate model performance using two official metrics from the BIRD (Li et al., [2024a](https://arxiv.org/html/2509.25672v1#bib.bib19)) benchmark: Execution Accuracy (EX) and Soft F1-score. Execution Accuracy (EX) measures whether the execution results of predicted SQL queries exactly match those of the gold queries. While EX accounts for the semantic equivalence of structurally different SQLs, it remains a strict metric: a single discrepancy, such as column order variation, leads to a score of zero even if the query produces an otherwise correct result. This rigidity makes EX useful for measuring exact correctness but less suitable for reflecting practical robustness.

To address these limitations, the BIRD benchmark introduced the Soft F1-score, which compares the overlap between predicted and gold result tables in a precision–recall framework. By tolerating column reordering and minor inconsistencies such as missing values, Soft F1 provides a more faithful estimate of how well a model captures the intended semantics of a query. For example, when a predicted query retrieves the correct tuples but orders or partially aligns columns differently, Soft F1 still rewards the overlap instead of reducing the score to zero.

In this work, we primarily rely on the Soft F1-score for evaluation. We argue that Soft F1 better reflects the reliability of Text-to-SQL systems in real-world deployments, where users care about retrieving semantically correct answers rather than perfectly ordered result tables. Execution Accuracy is still reported for completeness and comparability with prior work, but we consider Soft F1 to be a more informative measure of model performance and a stronger indicator of progress in in-domain Text-to-SQL translation.

### 6.3. Models and Hyperparameters

For synthetic data generation, we employ the Gemini-2.5-Flash model across all stages of the SING-SQL framework, ensuring efficient and consistent synthesis of SQL–Text pairs with high semantic fidelity. Again, we employ Gemini-2.5-Flash in LLM-based schema filtering for accurate and comparable filtering performance. For downstream Text-to-SQL translation, we adopt Qwen2.5-Coder-1.5B Instruct and Qwen2.5-Coder-3B Instruct (Hui et al., [2024](https://arxiv.org/html/2509.25672v1#bib.bib12)) as the base model.
To adapt this backbone to in-domain settings, we apply supervised fine-tuning (SFT), yielding specialized variants that we refer to as SingSQL-LM.

The fine-tuning process is carried out using parameter-efficient Low-Rank Adaptation (LoRA) (Hu et al., [2022](https://arxiv.org/html/2509.25672v1#bib.bib11)), explored under two configurations: LoRA rank 32 and LoRA rank 64. In the rank-32 setting, we configure LoRA Alpha as 32, a learning rate of 1.0×10−41.0\times 10^{-4}, an effective batch size of 8, a warm-up ratio of 0.1, and cosine scheduling. In the rank-64 setting, we set LoRA Alpha as 64, a learning rate of 7.5×10−57.5\times 10^{-5}, an effective batch size of 8, a warm-up ratio of 0.1, and the same cosine scheduler.
All models are trained for two epochs. Fine-tuning is performed using the Unsloth1 library to enable efficient large-scale adaptation.

All experiments are conducted on a single NVIDIA A40 GPU equipped with 48 GB of VRAM.

## 7. Results

In Section [7.1](https://arxiv.org/html/2509.25672v1#S7.SS1 "7.1. Text-to-SQL Translation Performance ‣ 7. Results ‣ SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation"), we report the performance of the fine-tuned SingSQL-LM models on Bird benchmark (Li et al., [2024a](https://arxiv.org/html/2509.25672v1#bib.bib19)) and synthetic datasets. Section [7.2](https://arxiv.org/html/2509.25672v1#S7.SS2 "7.2. Schema Filtering Performance ‣ 7. Results ‣ SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation") presents an evaluation of schema filtering techniques that leverage the generated synthetic data. Section [7.3](https://arxiv.org/html/2509.25672v1#S7.SS3 "7.3. Context Management ‣ 7. Results ‣ SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation") examines the effect of different context management strategies on model performance.

### 7.1. Text-to-SQL Translation Performance

Table 3. Comparison of system performance on the California Schools subset of the BIRD development benchmark.

System
Candidate Count = 8
Candidate Count = 16
Candidate Count = 32

EX UB
EX LB
F1 UB
F1 LB
EX UB
EX LB
F1 UB
F1 LB
EX UB
EX LB
F1 UB
F1 LB

CODES-1B
43.82
6.74
49.40
9.32
44.94
3.37
51.90
5.02
50.56
1.12
60.72
44.94

SLM-SQL-1.5B †
40.45
0.0
47.08
0.0
52.81
0.0
59.84
0.0
59.55
0.0
64.52
0.0

CODES-3B
50.56
11.24
56.46
14.50
56.18
3.37
62.17
5.80
60.67
1.12
66.66
1.77

OmniSQL-7B ‡
73.03
35.96
80.36
44.81
–
–
–
–
–
–
–
–

CscSQL-Grpo-Qwen2.5-Coder-7B-Instruct
66.29
1.12
72.02
1.12
74.15
0.0
76.99
0.0
77.55
0.0
81.45
0.0

CHESS
61.80
23.60
73.04
32.83
69.66
14.61
75.73
18.32
76.40
11.24
82.63
16.13

SingSQL-LM-1.5B-R32
41.57
0.0
53.26
0.0
52.80
0.0
64.75
0.0
59.55
0.0
67.55
0.0

SingSQL-LM-1.5B-R64
53.93
0.0
63.89
0.0
58.43
0.0
67.20
0.0
64.04
0.0
73.82
0.0

SingSQL-LM-3B-R32
58.42
0.0
71.06
1.00
67.42
0.0
77.61
0.56
70.79
0.0
81.76
0.0

SingSQL-LM-3B-R64
64.04
1.12
73.61
6.26
68.54
0.0
79.21
0.85
73.03
0.0
82.87
0.0

R represents the LoRA rank. UB represents upper bound and LB represents lower bound. We do not provide 3B models of CSC-SQL as we found its output inconsistent.† Only the SQL generator model is used for SLM-SQL. ‡ The values are calculated from candidate SQL queries directly given by the OmniSQL authors in Github2.

11footnotetext: <https://unsloth.ai>22footnotetext: <https://github.com/RUCKBReasoning/OmniSQL/tree/main/OmniSQL_prediction_results>



Table 4. Comparison of system performance (Candidate SQL count is 8) on the Synthetic California Schools Development and Test Sets of SING Framework.

System
SING-Dev
SING-Test

EX UB
EX LB
F1 UB
F1 LB
EX UB
EX LB
F1 UB
F1 LB

CODES-1B
17.97
0.53
28.70
1.96
16.73
0.36
27.11
1.79

SLM-SQL-1.5B
24.02
0.44
30.24
0.69
22.15
0.27
27.89
0.43

CODES-3B
22.42
0.53
34.57
2.18
20.20
0.71
33.07
2.80

CscSQL-Grpo-Qwen2.5-Coder-7B-Instruct
30.60
0.80
39.61
1.04
27.85
0.36
37.29
0.59

CHESS
38.70
10.23
53.44
16.79
40.75
9.16
55.24
18.24

SingSQL-LM-1.5B-R32
55.43
1.69
65.90
3.38
55.07
0.98
65.27
2.28

SingSQL-LM-1.5B-R64
56.85
2.22
68.05
4.04
58.10
1.60
66.59
3.00

SingSQL-LM-3B-R32
62.99
3.73
73.14
8.95
63.52
3.83
71.74
7.84

SingSQL-LM-3B-R64
65.21
5.25
75.33
10.58
64.08
5.16
72.37
9.87

In evaluating translation performance, we restrict our analysis to SQL generation stage where filtered schema used, deliberately excluding candidate selection mechanisms. This ensures that results reflect the intrinsic quality of the generated SQL queries, rather than the effectiveness of downstream ranking or selection modules. We report both Execution Accuracy (EX) and Soft F1-score  (Li et al., [2024a](https://arxiv.org/html/2509.25672v1#bib.bib19)), under lower- and upper-bound settings, across varying candidate counts. Results are presented on the California Schools subset of the BIRD development benchmark and on the synthetic California Schools data generated with the SING framework in Table [3](https://arxiv.org/html/2509.25672v1#S7.T3 "Table 3 ‣ 7.1. Text-to-SQL Translation Performance ‣ 7. Results ‣ SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation") and Table [4](https://arxiv.org/html/2509.25672v1#S7.T4 "Table 4 ‣ 7.1. Text-to-SQL Translation Performance ‣ 7. Results ‣ SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation"), respectively.

On BIRD-Dev, shown in Table [3](https://arxiv.org/html/2509.25672v1#S7.T3 "Table 3 ‣ 7.1. Text-to-SQL Translation Performance ‣ 7. Results ‣ SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation"), SingSQL-LM consistently outperforms comparable baselines. Among 1.5B-scale models, SingSQL-LM deliver substantial gains, reaching up to 73.82% Soft F1 UB and 64.04% EX UB with 32 candidates—9.30% and 4.49% gain over SLM-SQL-1.5B (64.52% Soft F1 UB, 59.55% EX UB) in terms of Soft F1 and EX respectively and clearly surpassing CODES-1B and 3B. At the 3B scale, SingSQL-LM achieves state-of-the-art performance among open models. With 32 candidates, SingSQL-LM-3B-R64 obtains 82.87% Soft F1 UB and 73.03% EX UB, outperforming the best 3B-scale baseline by +16.21 in Soft F1 and +12.36 in EX. Remarkably, SingSQL-LM-3B-R64 surpasses the 7B-scale CscSQL model, demonstrating that compact models can achieve superior performance with targeted in-domain supervision. Lower-bound scores remain close to zero across most settings due to the absence of refinement or self-consistency, but the strong upper bounds demonstrate that the models reliably generate high-quality SQL candidates.

On the synthetic evaluation splits, given in Table [4](https://arxiv.org/html/2509.25672v1#S7.T4 "Table 4 ‣ 7.1. Text-to-SQL Translation Performance ‣ 7. Results ‣ SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation"), the advantages of SingSQL-LM become even more pronounced. SingSQL-LM-1.5B-R64 achieves 68.05% Soft F1 UB and 56.85% EX UB on SING-Dev, and 66.59% Soft F1 UB and 58.10% EX UB on SING-Test, outperforming larger baselines such as CscSQL-Grpo-7B-Instruct, which remain below 40% Soft F1 and 31% EX. The 3B-scale variants further improve these results, with SingSQL-LM-3B-R64 reaching 75.33% Soft F1 UB and 65.21% EX UB on SING-Dev, and 72.37% Soft F1 UB and 64.08% EX UB on SING-Test. These results exceed all reported baselines by wide margins, underscoring that fine-tuning on SING-SQL’s high-coverage synthetic data enables robust in-domain generalization and offers a reliable evaluation path for database-specific performance.

Together, these findings emphasize two main points. First, SingSQL-LM demonstrates state-of-the-art performance among open models, while rivaling or surpassing 7B-scale systems. Second, the substantial improvements observed on the synthetic development and test sets underscore the value of database-specific supervision: models fine-tuned with SING-SQL not only outperform cross-domain baselines but also demonstrate consistent robustness across synthetic evaluation splits. This confirms the utility of synthetic in-domain data as a scalable path toward enterprise-grade Text-to-SQL systems.

### 7.2. Schema Filtering Performance

Table [5](https://arxiv.org/html/2509.25672v1#S7.T5 "Table 5 ‣ 7.2. Schema Filtering Performance ‣ 7. Results ‣ SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation") reports schema filtering results on the California Schools database from the BIRD development split, comparing multiple filtering strategies that leverage synthetic Text-to-SQL pairs. We evaluate recall and precision at both the table and column levels, along with strict schema recall rate (SRR) (Cao et al., [2024](https://arxiv.org/html/2509.25672v1#bib.bib3)). While both precision and recall are informative, recall is particularly critical in Text-to-SQL systems (Chung et al., [2025](https://arxiv.org/html/2509.25672v1#bib.bib6)), as omitting any part of the ground-truth schema inevitably leads to incorrect translations.

As described in Section [5.1](https://arxiv.org/html/2509.25672v1#S5.SS1 "5.1. Schema Linking ‣ 5. Text-to-SQL Translation ‣ SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation"), our schema linking process relies on synthetically generated Text-to-SQL pairs. We evaluate schema filtering performance under different retrieval methods. Since our approach does not filter tables, table recall remains consistently at 100%. For each keyword pair, we extract a single synthetic Text-to-SQL example. When all retrieved examples are considered, column recall reaches 87.23% with BM25 and 94.20% with vector-based retrieval. However, augmenting prompts with all retrieved examples is impractical for downstream tasks due to increased inference time and cost. To this end, we restrict the context to the top-6 most relevant examples, which reduces column recall to 71.93% (BM25) and 70.53% (vector retrieval). These results indicate that relying solely on synthetic examples retrieved via basic similarity methods yields limited effectiveness and can negatively impact overall Text-to-SQL translation.

To mitigate this, we incorporate an LLM-based filtering stage on top of retrieval. This hybrid strategy significantly improves the recall with the limited number of example. Specifically, BM25-Top6+LLM achieves 97.45% column recall with 46.77% precision, corresponding to an SRR of 88.76. Similarly, Vec-Top6+LLM reaches 97.91% recall with 47.52% precision, yielding the best SRR of 91.01. Since all tables are always included in the filtered schema along with their primary and foreign key columns, our precision scores are lower compared to systems that apply stricter pruning. The performance of schema filtering across different mechanisms on synthetic datasets is further detailed in Appendix [D](https://arxiv.org/html/2509.25672v1#A4 "Appendix D Schema Filtering Performance on Synthetic Data ‣ SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation").

Table 5. Schema Filtering Performance on California Schools database in Bird Development Split.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Method | TR | TP | CR | CP | SRR |
| RSL-SQL♢\diamondsuit | – | – | – | – | 91.80 |
| CHESS♢\diamondsuit | 97.69 | 89.72 | 97.12 | 69.43 | 89.70 |
| MCS♢\diamondsuit | – | – | 89.80 | – | – |
| BM25-Top6 | 100 | 58.82 | 71.93 | 27.33 | 25.84 |
| Vec-Top6 | 100 | 59.29 | 70.53 | 28.90 | 24.72 |
| BM25-All | 100 | 56.18 | 87.23 | 14.86 | 51.68 |
| Vec-All | 100 | 56.39 | 94.20 | 12.59 | 73.03 |
| BM25-Top6 + LLM | 100 | 58.37 | 97.45 | 46.77 | 88.76 |
| Vec-Top6 + LLM | 100 | 57.03 | 97.91 | 47.52 | 91.01 |

♢\diamondsuit Given metrics are for the whole development set of BIRD benchmark.

All our methods retrieve few-shots using *user-question keyword pairs*. “BM25” retrieves examples using BM25 algorithm; “Vec” retrieves examples using semantic similarity over a vector database. “All” uses all retrieved few-shots to construct filtered schema while “Top6” uses the top-6 most similar examples to the user question. “+LLM” applies LLM-based table column filtering leveraging retrieved synthetic examples. “TR” and “TP” represent Table Recall and Precision respectively. Similarly, “CR” and “CP” represent Column Recall and Precision respectively. “SRR” denotes strict schema recall rate  (Cao et al., [2024](https://arxiv.org/html/2509.25672v1#bib.bib3)).

Overall, these results highlight that combining synthetic in-domain supervision with the LLM-based filtering produces robust schema linking. By coupling efficient retrieval with targeted LLM refinement, SING-SQL achieves strong schema coverage while ensuring practical scalability, thus establishing a reliable foundation for downstream SQL generation.

### 7.3. Context Management

We evaluate the effect of different contextual signals on SQL generation, focusing on schema, few-shot demonstrations and few-shot reasoning traces.

For the base model, schema grounding provides the most stable supervision. As shown in Table [9](https://arxiv.org/html/2509.25672v1#A7.T9 "Table 9 ‣ Appendix G Context Management Study ‣ SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation"), supplying six few-shots with reasoning consistently reduces performance, while providing few-shots without reasoning improves the performance slightly, suggesting that few-shots can offer marginal benefits but reasoning traces can introduce noise.

When fine-tuned models are considered, schema-only inference emerges as the most effective configuration across all training regimes. Adding few-shots at inference consistently lowers accuracy, particularly when reasoning traces are included as seen in Table [9](https://arxiv.org/html/2509.25672v1#A7.T9 "Table 9 ‣ Appendix G Context Management Study ‣ SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation"). An important observation is that training with schema-aware data (T2SWS) leads to intermediate performance, whereas models fine-tuned on schema-free data (T2S) achieve the highest scores under schema-only inference. This indicates that schema-free fine-tuning allows the model to internalize SQL patterns and leverage schema more effectively during inference, while explicit schema supervision during training provides less robust transfer.

Overall, three findings stand out. First, schema grounding is the most robust contextual signal, outperforming configurations with additional few-shots for fine-tuned models. Second, schema-free fine-tuning combined with schema-only inference yields the strongest generalization to in-domain queries. Third, few-shots especially with reasoning traces tend to destabilize performance, limiting their utility once schema context is explicitly provided. Additional experiments with other fine-tuned models confirm these patterns, as detailed in Appendix [G](https://arxiv.org/html/2509.25672v1#A7 "Appendix G Context Management Study ‣ SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation").

Table 6. Comparison of model performance across different training and inference contexts (candidate SQL count = 8).

Training Context
Inference Context
Performance

Dataset
FS-C
FS-R
Schema
FS-C
FS-R
EX UB
F1 UB

Base Model
✓
6
✓
38.20
43.20

Base Model
✓
6
✓
47.19
54.94

Base Model
✓
0
NA
46.06
54.37

T2SWS
6
×\times
✓
6
✓
40.44
52.55

T2SWS
6
×\times
✓
6
×\times
33.70
46.38

T2SWS
6
×\times
✓
0
NA
46.07
56.00

T2SWS
0
NA
✓
6
✓
35.96
49.87

T2SWS
0
NA
✓
6
×\times
40.45
53.29

T2SWS
0
NA
✓
0
NA
51.69
63.20

T2SWS, T2S
6
×\times
✓
6
✓
30.34
43.49

T2SWS, T2S
6
×\times
✓
6
×\times
42.69
54.10

T2SWS, T2S
6
×\times
✓
0
NA
47.19
59.57

T2SWS, T2S
0
NA
✓
6
✓
33.70
46.01

T2SWS, T2S
0
NA
✓
6
×\times
46.07
56.50

T2SWS, T2S
0
NA
✓
0
NA
46.08
59.03

T2S
6
×\times
✓
6
✓
41.57
56.67

T2S
6
×\times
✓
6
×\times
42.69
55.40

T2S
6
×\times
✓
0
NA
52.80
69.63

T2S
0
NA
✓
6
+
39.33
55.58

T2S
0
NA
✓
6
–
48.31
62.83

T2S
0
NA
✓
0
NA
60.67
72.35

Qwen2.5-Coder-Instruct-3B serves as the base model. FS denotes few-shot examples. FS-C is the number of few-shot examples, and FS-R indicates whether reasoning traces of few-shots are included in the prompt. T2S refers to the fine-tuning dataset without schema context, whereas T2SWS includes filtered schema context. All fine-tuned models use LoRA (Rank = 32, Alpha = 32) with a learning rate of 1.0×10−41.0\times 10^{-4}, two training epochs, and an effective batch size of 8.

## 8. Discussion and Limitations

One limitation of the proposed framework arises when foreign-key constraints are absent or not explicitly defined in the database schema. Since the initial stage of SING-SQL relies on foreign-key relationships to guide schema partitioning, the lack of such constraints restricts the ability of the framework to construct accurate sub-schemas. In practice, this limitation can be mitigated by manually specifying foreign-key relationships, enabling the framework to proceed with schema partitioning even in databases where constraints are incompletely defined.

Another limitation of our framework arises when a set of columns within a table are semantically or functionally related and should be frequently queried together. Our current schema partitioning strategy applies a sliding window at the column level to generate sub-schemas. However, this approach does not consider inherent relationships among columns, which may result in separating fields that are typically used together. However, similar limitation can also be observed in the BIRD benchmark, despite being curated by domain experts. Appendix [C](https://arxiv.org/html/2509.25672v1#A3 "Appendix C Separation of Columns Highly Used Together Limitation Example ‣ SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation") illustrates this issue with the Schools table in the California Schools database (part of the BIRD dev set), where administrator-related fields are split across different sub-schemas. Consequently, a question requiring all administrator email addresses may yield only partial results, reducing the semantic fidelity of question-SQL pairs.

A potential solution is to first identify and group semantically related columns before partitioning the columns via sliding window. This would help preserve meaningful column groupings within sub-schemas and avoid undesirable separation. However, such an approach generally requires domain knowledge and manual intervention, making it labor-intensive and not easily scalable.

Additionally, grouping semantically related columns would likely reduce the number of distinct sub-schemas and, in turn, the number of synthesized examples. To maintain data volume and diversity, this reduction could be addressed by generating larger amount of question-SQL pairs per sub-schema with variations in query focus or changing the parameters of the SING-SQL. Incorporating diverse natural language styles—similar to those used in OMNI-SQL (Li et al., [2025](https://arxiv.org/html/2509.25672v1#bib.bib17))—can further enhance the richness of the dataset without sacrificing structural coherence.

As future work, automated techniques could be developed to detect and preserve column groupings using LLMs, thereby mitigating this limitation without relying on manual effort or domain-specific expertise.

We do not study the effect of decoding hyperparameters such as temperature or top-p. These are fixed throughout our experiments to ensure consistency.

Reasoning traces are generated only through the divide-and-conquer prompting strategy. Exploring multiple reasoning paths could improve robustness and diversity but would substantially increase cost, and is therefore left as future work.

While schema linking could potentially be enhanced by incorporating LLM-based table filtering, optimizing linking performance is not the primary focus of this work. Instead, our goal is to demonstrate the effectiveness of different schema linking strategies when supported by synthetic data, rather than to develop the strongest possible schema linking system.

Additionally, we do not incorporate reinforcement learning (e.g., GRPO (Shao et al., [2024](https://arxiv.org/html/2509.25672v1#bib.bib31))) as a post-training step. While such methods could further improve SQL generation by aligning outputs with execution results, we leave this as future work.

## 9. Conclusion

In this work, we introduced SING-SQL, a two-stage synthetic data generation framework tailored for in-domain Text-to-SQL tasks. By hierarchically partitioning target databases into diverse sub-schemas and generating SQL–Text pairs across multiple complexity levels, SING-SQL achieves both comprehensive schema coverage and semantic alignment. To ensure data quality, our framework integrates LLM-as-a-judge validation, executability checks, automatic repair, and column-focused balancing, resulting in datasets that are both high-coverage and structurally reliable.

We further released SingSQL-LM, a family of compact language models efficiently fine-tuned on the synthetic data produced by our framework. Extensive experiments on both the BIRD benchmark and our synthetic evaluation splits demonstrate consistent improvements in in-domain generalization. On the BIRD development subset, SingSQL-LM-3B-R64 attains 82.87% Soft F1 and 73.03% EX upper bound with 32 candidates, surpassing the best 3B-scale baseline by +16.21 points in Soft F1 and +12.36 points in EX. At the 1.5B scale, SingSQL-LM-1.5B-R64 improves over prior systems by +9.30 in Soft F1 and +4.49 in EX. On the synthetic evaluation splits, SingSQL-LM models further extend these gains. These results confirm high-coverage synthetic supervision not only benefits small-scale models but also establishes state-of-the-art performance among open models at comparable scales.

Notably, schema-free fine-tuning combined with schema-only inference yields the strongest results. This setting allows the model to internalize SQL patterns during training without being overly dependent on explicit schema supervision, while still leveraging schema context effectively at inference time. Our experiments show that synthetically generated few-shots and reasoning traces often destabilize performance once schema is provided, whereas schema-only inference consistently offers the most robust and scalable configuration for fine-tuned model. These findings underscore the practicality of schema-free training, as it reduces prompt complexity and cost at deployment while maintaining strong accuracy in domain-specific databases.

Beyond performance gains, our findings highlight the broader utility of synthetic database-specific data generation: it enables robust schema filtering with the help of LLM, enhances SQL generation, and offers a practical path for enterprises to adapt open-source LLMs without costly learning pipelines or large-scale manual annotation. Moreover, by combining parameter-efficient fine-tuning with compact models, we provide a viable solution for low-resource environments where annotated data or computational capacity is limited, making domain-specialized Text-to-SQL systems accessible even to organizations with constrained resources.

While our work addresses critical challenges in domain specialization, limitations remain. Current sub-schema partitioning may separate semantically related columns, and reasoning traces are generated through a single prompting strategy. Future work can explore automated column grouping, diverse reasoning styles, and reinforcement learning to further strengthen robustness.

Overall, SING-SQL establishes a scalable and database-agnostic paradigm for generating high-quality in-domain data, providing a strong foundation for advancing Text-to-SQL translation in real-world enterprise settings.

###### Acknowledgements.

We thank TÜBİTAK ULAKBIM for granting access to the High Performance and Grid Computing Center (TRUBA), and Koç University High Performance Computing Center for providing GPU resources used in this work.

## References

* (1)
* Caferoğlu and Özgür Ulusoy (2025)

  Hasan Alp Caferoğlu and Özgür Ulusoy. 2025.
  E-SQL: Direct Schema Linking via Question Enrichment in Text-to-SQL.


  arXiv:2409.16751 [cs.CL]
  <https://arxiv.org/abs/2409.16751>
* Cao et al. (2024)

  Zhenbiao Cao, Yuanlei Zheng, Zhihao Fan, Xiaojin Zhang, and Wei Chen. 2024.
  RSL-SQL: Robust Schema Linking in Text-to-SQL Generation.
  *arXiv preprint arXiv:2411.00073* (2024).
* Chafik et al. (2025)

  Salmane Chafik, Saad Ezzini, and Ismail Berrada. 2025.
  Towards Automating Domain-Specific Data Generation for Text-to-SQL: A Comprehensive Approach.
  *ACM Trans. Softw. Eng. Methodol.* (June 2025).

  <https://doi.org/10.1145/3746226>
  Just Accepted.
* Cheng et al. (2025)

  Song Cheng, Qiannan Cheng, Linbo Jin, Lei Yi, and Guannan Zhang. 2025.
  SQLord: A Robust Enterprise Text-to-SQL Solution via Reverse Data Generation and Workflow Decomposition *(WWW ’25)*. Association for Computing Machinery, New York, NY, USA, 919–923.

  <https://doi.org/10.1145/3701716.3715541>
* Chung et al. (2025)

  Yeounoh Chung, Gaurav Tarlok Kakkar, Yu Gan, Brenton Milne, and Fatma Ozcan. 2025.
  Is Long Context All You Need? Leveraging LLM’s Extended Context for NL2SQL.
  *Proc. VLDB Endow.* 18, 8 (2025), 2735–2747.

  <https://www.vldb.org/pvldb/vol18/p2735-ozcan.pdf>
* Dong et al. (2023)

  Xuemei Dong, Chao Zhang, Yuhang Ge, Yuren Mao, Yunjun Gao, lu Chen, Jinshu Lin, and Dongfang Lou. 2023.
  C3: Zero-shot Text-to-SQL with ChatGPT.


  arXiv:2307.07306 [cs.CL]
  <https://arxiv.org/abs/2307.07306>
* Gao et al. (2024)

  Dawei Gao, Haibin Wang, Yaliang Li, Xiuyu Sun, Yichen Qian, Bolin Ding, and Jingren Zhou. 2024.
  Text-to-SQL Empowered by Large Language Models: A Benchmark Evaluation.
  *Proc. VLDB Endow.* 17, 5 (may 2024), 1132–1145.

  <https://doi.org/10.14778/3641204.3641221>
* Glass et al. (2025)

  Michael Glass, Mustafa Eyceoz, Dharmashankar Subramanian, Gaetano Rossiello, Long Vu, and Alfio Gliozzo. 2025.
  Extractive Schema Linking for Text-to-SQL.


  arXiv:2501.17174 [cs.DB]
  <https://arxiv.org/abs/2501.17174>
* Guo et al. (2025)

  Yu Guo, Dong Jin, Shenghao Ye, Shuangwu Chen, Jianyang Jianyang, and Xiaobin Tan. 2025.
  SQLForge: Synthesizing Reliable and Diverse Data to Enhance Text-to-SQL Reasoning in LLMs. In *Findings of the Association for Computational Linguistics: ACL 2025*, Wanxiang Che, Joyce Nabende, Ekaterina Shutova, and Mohammad Taher Pilehvar (Eds.). Association for Computational Linguistics, Vienna, Austria, 8441–8452.

  <https://doi.org/10.18653/v1/2025.findings-acl.443>
* Hu et al. (2022)

  Edward J Hu, yelong shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang, and Weizhu Chen. 2022.
  LoRA: Low-Rank Adaptation of Large Language Models. In *International Conference on Learning Representations*.

  <https://openreview.net/forum?id=nZeVKeeFYf9>
* Hui et al. (2024)

  Binyuan Hui, Jian Yang, Zeyu Cui, Jiaxi Yang, Dayiheng Liu, Lei Zhang, Tianyu Liu, Jiajun Zhang, Bowen Yu, Keming Lu, Kai Dang, Yang Fan, Yichang Zhang, An Yang, Rui Men, Fei Huang, Bo Zheng, Yibo Miao, Shanghaoran Quan, Yunlong Feng, Xingzhang Ren, Xuancheng Ren, Jingren Zhou, and Junyang Lin. 2024.
  Qwen2.5-Coder Technical Report.


  arXiv:2409.12186 [cs.CL]
  <https://arxiv.org/abs/2409.12186>
* Jiang et al. (2025)

  Jie Jiang, Haining Xie, Siqi Shen, Yu Shen, Zihan Zhang, Meng Lei, Yifeng Zheng, Yang Li, Chunyou Li, Danqing Huang, Yinjun Wu, Wentao Zhang, Bin Cui, and Peng Chen. 2025.
  SiriusBI: A Comprehensive LLM-Powered Solution for Data Analytics in Business Intelligence.
  *Proc. VLDB Endow.* 18, 12 (Sept. 2025), 4860–4873.

  <https://doi.org/10.14778/3750601.3750610>
* Kojima et al. (2022)

  Takeshi Kojima, Shixiang (Shane) Gu, Machel Reid, Yutaka Matsuo, and Yusuke Iwasawa. 2022.
  Large Language Models are Zero-Shot Reasoners. In *Advances in Neural Information Processing Systems*, S. Koyejo, S. Mohamed, A. Agarwal, D. Belgrave, K. Cho, and A. Oh (Eds.), Vol. 35. Curran Associates, Inc., 22199–22213.

  <https://proceedings.neurips.cc/paper_files/paper/2022/file/8bb0d291acd4acf06ef112099c16f326-Paper-Conference.pdf>
* Lee et al. (2024)

  Dongjun Lee, Choongwon Park, Jaehyuk Kim, and Heesoo Park. 2024.
  MCS-SQL: Leveraging Multiple Prompts and Multiple-Choice Selection For Text-to-SQL Generation.


  arXiv:2405.07467 [cs.CL]
  <https://arxiv.org/abs/2405.07467>
* Li et al. (2024b)

  Boyan Li, Yuyu Luo, Chengliang Chai, Guoliang Li, and Nan Tang. 2024b.
  The Dawn of Natural Language to SQL: Are We Fully Ready?. In *Proceedings of the VLDB Endowment (PVLDB)*, Vol. 17.

  <https://doi.org/10.14778/3681954.3682003>
* Li et al. (2025)

  Haoyang Li, Shang Wu, Xiaokang Zhang, Xinmei Huang, Jing Zhang, Fuxin Jiang, Shuai Wang, Tieying Zhang, Jianjun Chen, Rui Shi, Hong Chen, and Cuiping Li. 2025.
  OmniSQL: Synthesizing High-quality Text-to-SQL Data at Scale.


  arXiv:2503.02240 [cs.CL]
  <https://arxiv.org/abs/2503.02240>
* Li et al. (2024c)

  Haoyang Li, Jing Zhang, Hanbing Liu, Ju Fan, Xiaokang Zhang, Jun Zhu, Renjie Wei, Hongyan Pan, Cuiping Li, and Hong Chen. 2024c.
  CodeS: Towards Building Open-source Language Models for Text-to-SQL.
  *Proc. ACM Manag. Data* 2, 3, Article 127 (may 2024), 28 pages.

  <https://doi.org/10.1145/3654930>
* Li et al. (2024a)

  Jinyang Li, Binyuan Hui, Ge Qu, Jiaxi Yang, Binhua Li, Bowen Li, Bailin Wang, Bowen Qin, Ruiying Geng, Nan Huo, et al. 2024a.
  Can llm already serve as a database interface? a big bench for large-scale database grounded text-to-sqls.
  *Advances in Neural Information Processing Systems* 36 (2024).
* Liu et al. (2025a)

  Geling Liu, Yunzhi Tan, Ruichao Zhong, Yuanzhen Xie, Lingchen Zhao, Qian Wang, Bo Hu, and Zang Li. 2025a.
  Solid-SQL: Enhanced Schema-linking based In-context Learning for Robust Text-to-SQL. In *Proceedings of the 31st International Conference on Computational Linguistics*, Owen Rambow, Leo Wanner, Marianna Apidianaki, Hend Al-Khalifa, Barbara Di Eugenio, and Steven Schockaert (Eds.). Association for Computational Linguistics, Abu Dhabi, UAE, 9793–9803.

  <https://aclanthology.org/2025.coling-main.654/>
* Liu et al. (2025b)

  Yifu Liu, Yin Zhu, Yingqi Gao, Zhiling Luo, Xiaoxia Li, Xiaorong Shi, Yuntao Hong, Jinyang Gao, Yu Li, Bolin Ding, and Jingren Zhou. 2025b.
  XiYan-SQL: A Novel Multi-Generator Framework For Text-to-SQL.
  (2025).
  arXiv:2507.04701 [cs.CL]
  <https://arxiv.org/abs/2507.04701>
* Ma et al. (2025)

  Peixian Ma, Xialie Zhuang, Chengjin Xu, Xuhui Jiang, Ran Chen, and Jian Guo. 2025.
  SQL-R1: Training Natural Language to SQL Reasoning Model By Reinforcement Learning.


  arXiv:2504.08600 [cs.DB]
  <https://arxiv.org/abs/2504.08600>
* Maamari et al. (2024)

  Karime Maamari, Fadhil Abubaker, Daniel Jaroslawicz, and Amine Mhedhbi. 2024.
  The Death of Schema Linking? Text-to-SQL in the Age of Well-Reasoned Language Models. In *NeurIPS 2024 Third Table Representation Learning Workshop*.

  <https://openreview.net/forum?id=fglyh5pa7d>
* Papicchio et al. (2025)

  Simone Papicchio, Simone Rossi, Luca Cagliero, and Paolo Papotti. 2025.
  Think2SQL: Reinforce LLM Reasoning Capabilities for Text2SQL.


  arXiv:2504.15077 [cs.LG]
  <https://arxiv.org/abs/2504.15077>
* Pourreza et al. (2025a)

  Mohammadreza Pourreza, Hailong Li, Ruoxi Sun, Yeounoh Chung, Shayan Talaei, Gaurav Tarlok Kakkar, Yu Gan, Amin Saberi, Fatma Ozcan, and Sercan O Arik. 2025a.
  CHASE-SQL: Multi-Path Reasoning and Preference Optimized Candidate Selection in Text-to-SQL. In *The Thirteenth International Conference on Learning Representations*.

  <https://openreview.net/forum?id=CvGqMD5OtX>
* Pourreza and Rafiei (2023)

  Mohammadreza Pourreza and Davood Rafiei. 2023.
  DIN-SQL: Decomposed In-Context Learning of Text-to-SQL with Self-Correction. In *Advances in Neural Information Processing Systems*, A. Oh, T. Naumann, A. Globerson, K. Saenko, M. Hardt, and S. Levine (Eds.), Vol. 36. Curran Associates, Inc., 36339–36348.

  <https://proceedings.neurips.cc/paper_files/paper/2023/file/72223cc66f63ca1aa59edaec1b3670e6-Paper-Conference.pdf>
* Pourreza and Rafiei (2024)

  Mohammadreza Pourreza and Davood Rafiei. 2024.
  DTS-SQL: Decomposed Text-to-SQL with Small Large Language Models.


  arXiv:2402.01117 [cs.CL]
  <https://arxiv.org/abs/2402.01117>
* Pourreza et al. (2025b)

  Mohammadreza Pourreza, Shayan Talaei, Ruoxi Sun, Xingchen Wan, Hailong Li, Azalia Mirhoseini, Amin Saberi, and Sercan ”O. Arik. 2025b.
  Reasoning-SQL: Reinforcement Learning with SQL Tailored Partial Rewards for Reasoning-Enhanced Text-to-SQL.


  arXiv:2503.23157 [cs.LG]
  <https://arxiv.org/abs/2503.23157>
* Qu et al. (2024)

  Ge Qu, Jinyang Li, Bowen Li, Bowen Qin, Nan Huo, Chenhao Ma, and Reynold Cheng. 2024.
  Before Generation, Align it! A Novel and Effective Strategy for Mitigating Hallucinations in Text-to-SQL Generation. In *Findings of the Association for Computational Linguistics ACL 2024*, Lun-Wei Ku, Andre Martins, and Vivek Srikumar (Eds.). Association for Computational Linguistics, Bangkok, Thailand and virtual meeting, 5456–5471.

  <https://aclanthology.org/2024.findings-acl.324>
* Rafailov et al. (2023)

  Rafael Rafailov, Archit Sharma, Eric Mitchell, Christopher D Manning, Stefano Ermon, and Chelsea Finn. 2023.
  Direct Preference Optimization: Your Language Model is Secretly a Reward Model. In *Thirty-seventh Conference on Neural Information Processing Systems*.

  <https://openreview.net/forum?id=HPuSIXJaa9>
* Shao et al. (2024)

  Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan Zhang, Y. K. Li, Y. Wu, and Daya Guo. 2024.
  DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models.


  arXiv:2402.03300 [cs.CL]
  <https://arxiv.org/abs/2402.03300>
* Sheng and Xu (2025a)

  Lei Sheng and Shuai-Shuai Xu. 2025a.
  CSC-SQL: Corrective Self-Consistency in Text-to-SQL via Reinforcement Learning.


  arXiv:2505.13271 [cs.CL]
  <https://arxiv.org/abs/2505.13271>
* Sheng and Xu (2025b)

  Lei Sheng and Shuai-Shuai Xu. 2025b.
  SLM-SQL: An Exploration of Small Language Models for Text-to-SQL.


  arXiv:2507.22478 [cs.CL]
  <https://arxiv.org/abs/2507.22478>
* Sheng et al. (2025)

  Lei Sheng, Shuai-Shuai Xu, and Wei Xie. 2025.
  BASE-SQL: A powerful open source Text-To-SQL baseline approach.


  arXiv:2502.10739 [cs.CL]
  <https://arxiv.org/abs/2502.10739>
* Shi et al. (2025)

  Jie Shi, Bo Xu, Jiaqing Liang, Yanghua Xiao, Jia Chen, Chenhao Xie, Peng Wang, and Wei Wang. 2025.
  Gen-SQL: Efficient Text-to-SQL By Bridging Natural Language Question And Database Schema With Pseudo-Schema. In *Proceedings of the 31st International Conference on Computational Linguistics*, Owen Rambow, Leo Wanner, Marianna Apidianaki, Hend Al-Khalifa, Barbara Di Eugenio, and Steven Schockaert (Eds.). Association for Computational Linguistics, Abu Dhabi, UAE, 3794–3807.

  <https://aclanthology.org/2025.coling-main.256/>
* Shkapenyuk et al. (2025)

  Vladislav Shkapenyuk, Divesh Srivastava, Theodore Johnson, and Parisa Ghane. 2025.
  Automatic Metadata Extraction for Text-to-SQL.


  arXiv:2505.19988 [cs.DB]
  <https://arxiv.org/abs/2505.19988>
* Talaei et al. (2024)

  Shayan Talaei, Mohammadreza Pourreza, Yu-Chen Chang, Azalia Mirhoseini, and Amin Saberi. 2024.
  CHESS: Contextual Harnessing for Efficient SQL Synthesis.
  *arXiv preprint arXiv:2405.16755* (2024).

  <https://arxiv.org/abs/2405.16755>
  Preprint arXiv:2405.16755.
* Vaidya et al. (2025)

  Kapil Vaidya, Jialin Ding, Sebastian Kosak, David Kernert, Chuan Lei, Xiao Qin, Abhinav Tripathy, Ramesh Balan, Balakrishnan Narayanaswamy, and Tim Kraska. 2025.
  TailorSQL: An NL2SQL System Tailored to Your Query Workload.


  arXiv:2505.23039 [cs.DB]
  <https://arxiv.org/abs/2505.23039>
* Wang et al. (2024)

  Bing Wang, Changyu Ren, Jian Yang, Xinnian Liang, Jiaqi Bai, Linzheng Chai, Zhao Yan, Qian-Wen Zhang, Di Yin, Xing Sun, and Zhoujun Li. 2024.
  MAC-SQL: A Multi-Agent Collaborative Framework for Text-to-SQL.


  arXiv:2312.11242 [cs.CL]
* Wang et al. (2023)

  Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc V Le, Ed H. Chi, Sharan Narang, Aakanksha Chowdhery, and Denny Zhou. 2023.
  Self-Consistency Improves Chain of Thought Reasoning in Language Models. In *The Eleventh International Conference on Learning Representations*.

  <https://openreview.net/forum?id=1PL1NIMMrw>
* Wei et al. (2024)

  Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, Fei Xia, Ed H. Chi, Quoc V. Le, and Denny Zhou. 2024.
  Chain-of-thought prompting elicits reasoning in large language models. In *Proceedings of the 36th International Conference on Neural Information Processing Systems* (New Orleans, LA, USA) *(NIPS ’22)*. Curran Associates Inc., Red Hook, NY, USA, Article 1800, 14 pages.
* Xie et al. (2025)

  Xiangjin Xie, Guangwei Xu, Lingyan Zhao, and Ruijie Guo. 2025.
  OpenSearch-SQL: Enhancing Text-to-SQL with Dynamic Few-shot and Consistency Alignment.
  *Proc. ACM Manag. Data* 3, 3, Article 194 (June 2025), 24 pages.

  <https://doi.org/10.1145/3725331>
* Yang et al. (2024)

  Jiaxi Yang, Binyuan Hui, Min Yang, Jian Yang, Junyang Lin, and Chang Zhou. 2024.
  Synthesizing Text-to-SQL Data from Weak and Strong LLMs. In *Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, Lun-Wei Ku, Andre Martins, and Vivek Srikumar (Eds.). Association for Computational Linguistics, Bangkok, Thailand, 7864–7875.

  <https://doi.org/10.18653/v1/2024.acl-long.425>
* Yang et al. (2025)

  Zhuopan Yang, Yuanzhen Xie, Ruichao Zhong, Yunzhi Tan, Enjie Liu, Zhenguo Yang, Mochi Gao, Bo Hu, and Zang Li. 2025.
  PSM-SQL: Progressive Schema Learning with Multi-granularity Semantics for Text-to-SQL.


  arXiv:2502.05237 [cs.DB]
  <https://arxiv.org/abs/2502.05237>
* Yao et al. (2025)

  Zhewei Yao, Guoheng Sun, Lukasz Borchmann, Zheyu Shen, Minghang Deng, Bohan Zhai, Hao Zhang, Ang Li, and Yuxiong He. 2025.
  Arctic-Text2SQL-R1: Simple Rewards, Strong Reasoning in Text-to-SQL.


  arXiv:2505.20315 [cs.CL]
  <https://arxiv.org/abs/2505.20315>

## Appendix A Flawed SQL-to-Text Translation

When synthesizing Text-to-SQL pairs, one common strategy is to first generate SQL queries based on the database schema and subsequently produce corresponding natural language questions. This direction is often preferred as translating from SQL to natural language is considered a relatively simpler task compared to the inverse. However, SQL-to-text generation does not always yield high-quality question formulations. Accurate translation requires a deep semantic understanding of the database schema—specifically, what each column represents. In our experiments, we observed that even state-of-the-art large language models (LLMs) occasionally fail to capture these semantics accurately, resulting in flawed natural language questions. An illustrative example is provided in [Figure 5](https://arxiv.org/html/2509.25672v1#A1.F5 "Figure 5 ‣ Appendix A Flawed SQL-to-Text Translation ‣ SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation"), where a SQL query generated by Gemini-2.5-Pro selects the enroll12 column from the satscores table. This column denotes the total number of students enrolled from 1st through 12th grade. However, the corresponding generated question incorrectly refers only to 12th-grade enrollment, demonstrating a semantic misinterpretation of the column’s meaning and resulting in low-quality data.

SQL:
SELECT T1.AdmEmail1, T2.dname, T2.enroll12 FROM schools AS T1 INNER JOIN satscores AS T2 ON T1.CDSCode = T2.cds INNER JOIN frpm AS T3 ON T1.CDSCode = T3.CDSCode WHERE T2.cname = ’Los Angeles’ AND T3.’District Type’ = ’Unified School District’;
Question:
Show me the administrator’s email, the district name, and the 12th-grade enrollment for all schools located in Los Angeles county that are part of a Unified School District.


Figure 5. Example of flawed SQL-to-Text translation where the model misinterprets column semantics.

## Appendix B Illogical SQL-to-Text Pairs

In the process of generating Text-to-SQL training data, some SQL queries—though syntactically correct and semantically aligned with their corresponding questions—can still be illogical from an analytical or real-world perspective. These pairs are referred to as illogical SQL-to-text pairs. Unlike flawed translations that arise from misinterpretations of column semantics, illogical pairs emerge when the intent or logic of the SQL query lacks analytical validity or practical utility.

One scenario involves performing numerical operations, such as computing an average, on values that are not inherently quantitative. This misstep often arises from a superficial interpretation of a column’s name or datatype (e.g., treating textual identifiers as numerically meaningful). While language models may generate SQL and natural language questions that are mutually consistent, the underlying query logic may not serve a meaningful purpose in practice.

An illustrative example is shown in [Figure 6](https://arxiv.org/html/2509.25672v1#A2.F6 "Figure 6 ‣ Appendix B Illogical SQL-to-Text Pairs ‣ SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation"). Here, the SQL query attempts to calculate the average charter school identification number for district types that have more than 500 schools. While technically executable and syntactically valid, the query is conceptually flawed—charter school identification numbers are unique IDs and not numerical attributes that should be averaged. Thus, the question generated from this query, despite being a literal translation, is illogical from an analytical standpoint.

SQL:
SELECT "District Type", AVG(CASE WHEN "Charter School Number" IS NOT NULL THEN CAST("Charter School Number" AS REAL) ELSE NULL END) AS AverageCharterSchoolNumber FROM frpm GROUP BY "District Type" HAVING COUNT(CDSCode) > 500;
Question:
Which school district types have more than 500 schools, and what is their average charter school identification number (if available)?


Figure 6. Example of an illogical SQL-to-Text pair. The SQL and question are semantically aligned but reflect an implausible analytical intent—averaging unique identifiers.

## Appendix C Separation of Columns Highly Used Together Limitation Example

As discussed in Section [8](https://arxiv.org/html/2509.25672v1#S8 "8. Discussion and Limitations ‣ SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation"), one drawback of our column-wise schema partitioning arises when semantically or functionally related columns are separated across different sub-schemas. In the California Schools dataset (from the BIRD dev set), the Schools table contains the following administrator-related columns:
AdmFName1, AdmLName1, AdmEmail1, AdmFName2, AdmLName2, AdmEmail2, AdmFName3, AdmLName3, AdmEmail3.

If not clearly stated, these columns should be often used together in queries that involve administrative contact information. However, because our current framework partitions columns using a sliding window without considering such semantic groupings, they may be split across multiple sub-schemas. However, similar limitation can also be observed in the BIRD benchmark, despite being curated by domain experts.

Figure [7](https://arxiv.org/html/2509.25672v1#A3.F7 "Figure 7 ‣ Appendix C Separation of Columns Highly Used Together Limitation Example ‣ SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation") illustrates an example of inconsistent handling of semantically related columns in the BIRD benchmark. The question asks for the common first names among school administrators, yet the provided SQL query only considers the first administrator (AdmFName1). This mismatch introduces ambiguity: either the SQL should aggregate across all administrator first-name columns, or the question should explicitly restrict the scope to the first administrator. A third possibility is to adopt a schema-level convention (e.g., defaulting to the first administrator unless otherwise specified), but such rules should be explicitly stated to avoid misinterpretation.
Figure [8](https://arxiv.org/html/2509.25672v1#A3.F8 "Figure 8 ‣ Appendix C Separation of Columns Highly Used Together Limitation Example ‣ SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation") presents a synthetic example illustrating this limitation. The example question asks for administrator email addresses and unique identifiers for schools classified as ’County Community School’. Yet the corresponding SQL query only returns one email field (AdmEmail3), as the sub-schema does not include the other administrator email columns. This mismatch reduces the fidelity of the synthesized question-SQL pair and can negatively impact model training and evaluation when such examples appear in the train, dev, or test splits.

Question:
What are the two most common first names among the school administrators? Indicate the district to which they administer.
SQL:
SELECT DISTINCT T1.AdmFName1, T1.District FROM schools AS T1 INNER JOIN ( SELECT admfname1 FROM schools GROUP BY admfname1 ORDER BY COUNT(admfname1) DESC LIMIT 2 ) AS T2 ON T1.AdmFName1 = T2.admfname1;


Figure 7. Data example in Bird development set for the separation of semantically related columns problem.



Sub-Schema:
”frpm”: [
”CDSCode”,
”Percent (%) Eligible FRPM (Ages 5-17)”,
”High Grade”
],
”satscores”: [
”cds”,
”AvgScrWrite”,
”NumTstTakr”
],
”schools”: [
”CDSCode”,
”EdOpsCode”,
”AdmEmail3”
]
SQL:
SELECT T1.AdmEmail3, T1.CDSCode FROM schools AS T1 WHERE T1.EdOpsCode = ’COMM’;
Question:
What are the administrator email addresses and unique identifiers for schools classified as ’County Community School’?


Figure 8. Synthetic Data Example for a separation of semantically related columns.

## Appendix D Schema Filtering Performance on Synthetic Data

Table 7. Schema Filtering Performance on the Synthetically generated Text-to-SQL data for the California Schools database in Bird Dev Split.
All methods retrieve few-shots using *user-question keyword pairs*.
“BM25” retrieves examples using BM25; “All” uses all retrieved few-shots to construct filtered schema while “Top6” uses the top-6 most similar examples to the user question. “+LLM” applies LLM-based table filtering leveraging retrieval. ”TR” and ”TP”represents Table Recall and Precision respectively. Similarly, ”CR” and ”CP” represents Column Recall and Precision respectively. ”SRR” represents strict schema recall rate

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Method | TR | TP | CR | CP | SRR |
| Synthetic Train Dataset | | | | | |
| BM25-Top6 | 96.50 | 68.48 | 89.41 | 39.15 | 75.65 |
| BM25-All | 97.14 | 64.96 | 93.10 | 16.88 | 87.78 |
| BM25-Top6 + LLM | 97.09 | 65.92 | 92.08 | 45.59 | 83.66 |
| Synthetic Dev Dataset | | | | | |
| BM25-Top6 | 95.51 | 65.71 | 86.94 | 37.01 | 71.97 |
| BM25-All | 96.20 | 62.26 | 90.99 | 15.70 | 84.51 |
| BM25-Top6 + LLM | 96.20 | 63.35 | 90.20 | 45.59 | 81.93 |
| Synthetic Test Dataset | | | | | |
| BM25-Top6 | 96.12 | 66.63 | 89.03 | 37.78 | 75.71 |
| BM25-All | 96.67 | 62.50 | 92.88 | 15.96 | 89.05 |
| BM25-Top6 + LLM | 96.63 | 63.59 | 91.13 | 40.03 | 82.74 |

## Appendix E Sub-Schema and Synthetic Data Statistics

While synthetic Text-to-SQL data is generated only for the California Schools database in the development set of the BIRD benchmark, Table [8](https://arxiv.org/html/2509.25672v1#A5.T8 "Table 8 ‣ Appendix E Sub-Schema and Synthetic Data Statistics ‣ SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation") reports statistics across multiple databases to illustrate how sub-schema generation varies with different parameter choices. For the experiments in this work, we specifically use the configuration in the first row of Table [8](https://arxiv.org/html/2509.25672v1#A5.T8 "Table 8 ‣ Appendix E Sub-Schema and Synthetic Data Statistics ‣ SING-SQL: A Synthetic Data Generation Framework for In-Domain Text-to-SQL Translation"): the California Schools database with 3 tables and 89 columns (an average of 29.66 columns per table). With a sliding window length of 3 and stride of 2, we obtain 2,249 sub-schemas and ultimately generate 39,734 synthetic examples.

Table 8. Sub-Schema and Synthetic Data Statistics

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Database Properties | | | Sub-Schema and Synthetic Data Generation Parameters | | | | Resulting Statistics | |
| Database | Table  Count | Column  Count | Avg. Cols  per Table | Table-Level Sub-Schema  Table Counts | Sliding  Window  Length | Stride | Min Col  Example  Count | Sub-Schema  Count | Synthetic  Data  Count |
| California Schools | 3 | 89 | 29.66 | [3, 2, 1] | 3 | 2 | 400 | 2249 | 39734 |
| California Schools | 3 | 89 | 29.66 | [3, 2, 1] | 3 | 1 | – | 11420 | – |
| Card Games | 6 | 115 | 19.16 | [3, 2, 1] | 3 | 2 | – | 2938 | – |
| Card Games | 6 | 115 | 19.16 | [3, 2, 1] | 2 | 1 | – | 13352 | – |
| Codebase Community | 8 | 71 | 8.875 | [4, 3, 2, 1] | 3 | 2 | – | 3533 | – |
| Codebase Community | 8 | 71 | 8.875 | [3, 2, 1] | 3 | 2 | – | 1134 | – |

## Appendix F Column Coverage Comparison for California Schools Database (Bird vs. Synthetic Dataset)

![Refer to caption](figures/column_coverage_comparison_california_schools.png)


Figure 9. Column Coverage Comparison for California Schools Database (Bird vs. Synthetic Dataset)

## Appendix G Context Management Study

Table 9. Comparison of model performance across different training and inference contexts (candidate SQL count = 8).

Training Context
Inference Context
Performance-R32
Performance-R64

Dataset
FS-C
FS-R
Schema
FS-C
FS-R
EX UB
F1 UB
EX UB
F1 UB

T2SWS
6
×\times
✓
6
✓
40.44
52.55
38.20
45.65

T2SWS
6
×\times
✓
6
×\times
33.70
46.38
44.94
57.93

T2SWS
6
×\times
✓
0
NA
46.07
56.00
47.19
60.23

T2SWS
0
NA
✓
6
✓
35.96
49.87
39.32
49.18

T2SWS
0
NA
✓
6
×\times
40.45
53.29
44.94
55.07

T2SWS
0
NA
✓
0
NA
51.69
63.20
51.68
62.81

T2SWS, T2S
6
×\times
✓
6
✓
30.34
43.49
42.01
51.11

T2SWS, T2S
6
×\times
✓
6
×\times
42.69
54.10
42.76
53.05

T2SWS, T2S
6
×\times
✓
0
NA
47.19
59.57
43.82
55.63

T2SWS, T2S
0
NA
✓
6
✓
33.70
46.01
43.82
52.33

T2SWS, T2S
0
NA
✓
6
×\times
46.07
56.50
35.95
50.73

T2SWS, T2S
0
NA
✓
0
NA
46.08
59.03
48.31
61.64

T2S
6
×\times
✓
6
✓
41.57
56.67
46.06
64.57

T2S
6
×\times
✓
6
×\times
42.69
55.40
49.44
61.40

T2S
6
×\times
✓
0
NA
52.80
69.63
52.81
64.06

T2S
0
NA
✓
6
+
39.33
55.58
46.07
59.49

T2S
0
NA
✓
6
–
48.31
62.83
44.94
61.07

T2S
0
NA
✓
0
NA
60.67
72.35
64.04
73.61

Qwen2.5-Coder-Instruct-3B serves as the base model. FS denotes few-shot examples. FS-C is the number of few-shot examples, and FS-R indicates whether reasoning traces of few-shots are included in the prompt. T2S refers to the fine-tuning dataset without schema context, whereas T2SWS includes filtered schema context.

## Appendix H Schema Table Column Filtration Prompt Template

[⬇](data:text/plain;base64,IyMjIFlvdSBhcmUgYW4gZXhjZWxsZW50IGRhdGEgc2NpZW50aXN0LiBZb3UgY2FuIGNhcHR1cmUgdGhlIGxpbmsgYmV0d2VlbiB1c2VyIHF1ZXN0aW9uIGFuZCBkYXRhYmFzZSBlbGVtZW50cyAoY29sdW1ucykuIFlvdSBkZXRlcm1pbmUgdGhlIHJlbGV2YW50IGRhdGFiYXNlIGNvbHVtbnMgcGVyZmVjdGx5LiBZb3VyIG9iamVjdGl2ZSBpcyB0byBhbmFseXplIGFuZCB1bmRlcnN0YW5kIHRoZSBlc3NlbmNlIG9mIHRoZSBnaXZlbiBxdWVzdGlvbiwgc2luZ2xlIGRhdGFiYXNlIHRhYmxlIHNjaGVtYSwgZXhhbXBsZXMgYW5kIHRoZW4gc2VsZWN0IHRoZSByZWxldmFudCBjb2x1bW5zIG9mIGEgZ2l2ZW4gdGFibGUuCgojIyMgRm9sbG93IHRoZSBpbnN0cnVjdGlvbnMgYmVsb3cgc3RlcCBieSBzdGVwOgojIFN0ZXAgMSAtIFJlYWQgdGhlIFF1ZXN0aW9uIENhcmVmdWxseToKICAgICogVW5kZXJzdGFuZCB0aGUgcHJpbWFyeSBmb2N1cyBhbmQgc3BlY2lmaWMgZGV0YWlscyBvZiB0aGUgcXVlc3Rpb24uIElkZW50aWZ5IG5hbWVkIGVudGl0aWVzICggc3VjaCBhcyBvcmdhbml6YXRpb25zLCBsb2NhdGlvbnMsIGV0Yy4pLCB0ZWNobmljYWwgdGVybXMsIGFuZCBvdGhlciBrZXkgcGhyYXNlcyB0aGF0IGVuY2Fwc3VsYXRlIGltcG9ydGFudCBhc3BlY3RzIG9mIHRoZSBpbnF1aXJ5IHRvIGVzdGFibGlzaCBhIGNsZWFyIGxpbmsgYmV0d2VlbiB0aGUgcXVlc3Rpb24gYW5kIHRoZSB0YWJsZSBjb2x1bW5zLgogICAgKiBJZiBhIGhpbnQgaXMgZ2l2ZW4gd2l0aCB0aGUgcXVlc2l0b24sIHJldmlldyBpdC4gVGhlIGhpbnQgcHJvdmlkZXMgc3BlY2lmaWMgaW5mb3JtYXRpb24gYW5kIGRpcmVjdHMgYXR0ZW50aW9uIHRvd2FyZCBjZXJ0YWluIGVsZW1lbnRzIHJlbGV2YW50IHRvIHRoZSBxdWVzdGlvbiBhbmQgaXRzIGFuc3dlci4gVXNlIHRoZSBoaW50IHRvIHVuZGVyc3RhbmQgdGhlIHJlbGF0aW9uIGJldHdlZW4gdGhlIHF1ZXN0aW9uLCB0aGUgaGludCwgYW5kIHRoZSBnaXZlbiB0YWJsZSBjb2x1bW5zLiBBbHdheXMgZm9sbG93IHN1Y2ggbG9naWMgZXhwbGljaXRseS4KIyBTdGVwIDIgLSBBbmFseXplIHRoZSBUYWJsZSBTY2hlbWE6CiAgICAqIFlvdSBhcmUgZ2l2ZW4gYSBzY2hlbWEgb2YgYSBzaW5nbGUgdGFibGUgaW4gYSBkYXRhYmFzZS4gRXhhbWluZSB0aGUgdGFibGUgc2NoZW1hIGFuZCBkZXRhaWxlZCBpbmZvcm1hdGlvbiBhYm91dCB0aGUgY29sdW1ucyB0byBpZGVudGlmeSByZWxldmFudCBjb2x1bW5zIHRoYXQgYXJlIHBlcnRpbmVudCB0byB0aGUgcXVlc3Rpb24uCiAgICAqIFVuZGVyc3RhbmQgdGhlIG1lYW5pbmcgYW5kIHB1cnBvc2Ugb2YgdGhlIGNvbHVtbiwgbm90IGp1c3QgaXRzIG5hbWUuCiMgU3RlcCAzIC0gRXhhbWluZSB0aGUgRXhhbXBsZXM6CiAgICAqIFJldmlldyBlYWNoIFRleHQtdG8tU1FMIGV4YW1wbGUgdGhhdCB1c2UgdGhlIGRhdGFiYXNlIGVsZW1lbnRzIHRoZSB0YWJsZSBjb21lIGZyb20uCiAgICAqIEFuYWx5emUgZWFjaCBxdWVzdGlvbi1TUUwgcGFpciB0byB1bmRlcnN0YW5kIHRoZSB0YWJsZSBjb2x1bW5zIGFuZCBsZWFybiBob3cgdGhleSBhcmUgdXNlZCwgaW4gd2hpY2ggY29udGV4dHMgdGhleSBhcmUgdXNlZC4KICAgICogVXNlIGV4YW1wbGVzIHRvIGd1aWRlIHlvdXIgZGVjaXNpb24sIGJ1dCAqKmRvIG5vdCByZXN0cmljdCB5b3Vyc2VsZioqIHRvIG9ubHkgY29sdW1ucyBzZWVuIGluIGV4YW1wbGVzLgojIFN0ZXAgNCAtIFNlbGVjdCBVc2VmdWwgQ29sdW1uczoKICAgICogQ29uc2lkZXIgZWFjaCBjb2x1bW4gb25lIGJ5IG9uZSBpbiBkZXRhaWwgdG8gZGV0ZXJtaW5lIGl0IGlzIHVzZWZ1bCBhbmQgcmVxdWlyZWQgdG8gYW5zd2VyIHRoZSBxdWVzdGlvbnMuIFdoZW4gaXRlcmF0aW5nIHRocm91Z2ggZWFjaCBjb2x1bW4sIHdyaXRlIGRldGFpbGVkIHJlYXNvbmluZyB3aHkgYSBjb2x1bW4gaXMgbmVjZXNzYXJ5IGFuZCB1c2VmdWwgb3Igbm90LiBXaGlsZSBldmFsdWF0aW5nIGEgY29sdW1uLCB5b3UgY2FuIHRha2UgdGhlIGFkdmFudGFnZSBmcm9tIHRoZSBleGFtcGxlcy4KICAgICAgICAtIEF0IGVhY2ggbmV3IGxpbmUsIHN0YXJ0IHdpdGggY29sdW1uIG5hbWUgdGhhdCB5b3UgY29uc2lkZXIuIEdvIHRocm91Z2ggdGhlIGluZm9ybWF0aW9uIGFib3V0IHRoZSBjb2x1bW4gYW5kIHN0YXRlIHRoZSBwcm9wZXJ0aWVzIG9mIHRoZSBjb2x1bW4uIFRoZW4gc3RhcnQgcmVhc29uaW5nIHdoZXRoZXIgaXQgaXMgcmVsYXRlZCB0byB0aGUgcXVlc3RvaW4gb3Igbm90LgogICAgKiBGb3IgZWFjaCBjb2x1bW4gaW4gdGhlIGdpdmVuIHRhYmxlIHNjaGVtYSwgYXNrIHlvdXJzZWxmOiBJcyB0aGlzIGNvbHVtbiBkaXJlY3RseSBuZWNlc3Nhcnkgb3IgaW5kaXJlY3RseSBoZWxwZnVsIHRvIGFuc3dlciB0aGUgcXVlc3Rpb24/CiAgICAgICAgLSBJZiB5ZXMsIGluY2x1ZGUgaXQuCiAgICAgICAgLSBJZiB0aGUgcXVlc3Rpb24gb3IgaGludCBzcGVjaWZpZXMgdGhpcyBjb2x1bW4sIGluY2x1ZGUgaXQuCiAgICAgICAgLSBJZiBpdCdzIHBhcnQgb2YgYSBmb3JtdWxhIG9yIGNvbXB1dGF0aW9uLCBpbmNsdWRlIGl0LgogICAgICAgIC0gSWYgeW91J3JlIHVuc3VyZSwgZXJyIG9uIHRoZSBzaWRlIG9mIGluY2x1ZGluZyBpdC4KICAgICogV2hlbiB1bnN1cmUgYWJvdXQgYSBjb2x1bW4sIHByZWZlciB0byBpbmNsdWRlIGEgY29sdW1uIHVubGVzcyBpdCBleHBsaWNpdGx5IGNvbnRyYWRpY3RzIHRoZSBxdWVzdGlvbiBvciBoaW50LiBVc2UgZXhhbXBsZXMgdG8gaW5mb3JtIHlvdXIganVkZ21lbnQsIGJ1dCBkbyBub3Qgb3ZlcmZpdCB0byB0aGVtLgogICAgKiBBbHdheXMgZm9sbG93IHRoZSBmb3JtdWxhIG9yIGNhbGN1bGF0aW9uIGxvZ2ljIGV4cGxpY2l0bHkgcHJvdmlkZWQgaW4gdGhlIHF1ZXN0aW9uIG9yIGhpbnQuCiAgICAgICAgKiAqKklNUE9SVEFOVCoqIElmIHRoZSBxdWVzdGlvbiBhbmQgaGludCBkZXNjcmliZSBhIGZvcm11bGEgdXNpbmcgc3BlY2lmaWMgY29sdW1uIG5hbWVzLCB5b3UgbXVzdCBzZWxlY3QgdGhvc2UgZXhhY3QgY29sdW1ucywgZXZlbiBpZiBhbHRlcm5hdGl2ZSBvciByZWR1bmRhbnQgY29sdW1ucyAoZS5nLiwgcGVyY2VudGFnZSwgcmF0ZSwgYXZlcmFnZSkgYXJlIHByZXNlbnQgaW4gdGhlIHNjaGVtYS4gKipEbyBub3QqKiBhc3N1bWUgdGhhdCBzaW1pbGFyLWxvb2tpbmcgY29sdW1ucyBzYXRpc2Z5IHRoZSByZXF1aXJlbWVudC4KICAgICogSWYgYSBxdWVzdGlvbiByZXF1aXJlcyBhZ2dyZWdhdGUgZnVuY3Rpb24gb24gYSBjb2x1bW4sIHlvdSAqKm11c3QqKiBzZWxlY3QgdGhhdCBjb2x1bW4uCiAgICAgICAgKiBEZXRlcm1pbmUgYSBxdWVzdGlvbiByZXF1aXJlcyBhZ2dyZWdhdGUgZnVuY3Rpb24sIHRoZW4gdGhpbmsgYW5kIGVsYWJvcmF0ZSBvbiB3aGljaCBjb2x1bW4gYWdncmV0YXRpb24gc2hvdWxkIGJlIGFwcGxpZWQuCiAgICAgICAgKiBGb3IgZXhhbXBsZSwgaWYgYSB1c2VyIHF1ZXN0aW9uIG5lZWRzIGNvdW50aW5nIChyZXF1aXJpbmcgQ09VTlQgYWdncmVnYXRlIGZ1bmN0aW9uKSwgdGhlbiBzZWxlY3QgYSBjb2x1bW4gb24gd2hpY2ggYWdncmVnYXRlIGZ1bmN0aW9uIHNob3VsZCBiZSBhcHBsaWVkLiBZb3UgKiptdXN0KiogbGlzdCB0aGF0IGNvbHVtbiBpbiB5b3VyIGFuc3dlci4KICAgICAgICAqIFdoZW4gdGhlIHF1ZXN0aW9uIHJlcXVpcmVzIHVuaXF1ZSB2YWx1ZXMgKGUuZy4sIElEcywgVVJMcyksIHRoZSBjb3JyZXNwb25kaW5nIFNRTCBxdWVyeSB3aWxsIHVzZSBgU0VMRUNUIERJU1RJTkNUYC4gUmVmZXIgdG8gY29sdW1uIHN0YXRpc3RpY3MgKCJWYWx1ZSBTdGF0aWNzIikgdG8gZGV0ZXJtaW5lIGlmIGBESVNUSU5DVGAgaXMgbmVjZXNzYXJ5LgogICAgKiBJZiBhbGwgY29sdW1ucyBvZiB0aGUgdGFibGUgYXJlIGlycmVsZXZhbnQgdG8gdGhlIHF1ZXN0aW9uLCB0aGVuIHJldHVybiBlbXB0eSBQeXRob24gTGlzdCBmb3IgdGhlIHNlbGVjdGVkX2NvbHVtbnMga2V5IGluIHRoZSByZXNwb25zZS4KIyBTdGVwIDU6IE91dHB1dCBGb3JtYXQ6CiAgICAqIEdpdmUgeW91ciByZXNwb25zZSBpbiBKU09OIGZvcm1hdCB3aXRoIHR3byBmb2xsb3dpbmcga2V5czogInJlYXNvbmluZyIgYW5kICJzZWxlY3RlZF9jb2x1bW5zIiB3aGVyZSB2YWx1ZSBvZiBhIHNlbGVjdGVkX2NvbHVtbnMgKiptdXN0KiogYmUgYSBQeXRob24gTGlzdCBhbmQgdGhlIHZhbHVlIG9mIHRoZSAicmVhc29uaW5nIiBzaG91bGQgYmUgc3RyaW5nIHJlYXNvbmluZyBvbiBlYWNoIGNvbHVtbiBhbmQgdGhlaXIgdXNlZnVsbmVzcy4KCi0gKipJTVBPUlRBTlQgTk9URToqKiBTb21lIGNvbHVtbnMgbWlnaHQgbm90IGJlIHVzZWQgaW4gdGhlIGV4YW1wbGVzIGdpdmVuLCBidXQgaXQgY2FuIGJlIG5lY2Vzc2FyeSBvciB1c2VmdWwuIEFsdGhvdWdoIGEgY29sdW1uIGlzIG5vdCB1c2VkIGluIGV4YW1wbGVzLCBpdCBtaWdodCBiZSBuZWNlc3Nhcnkgb3IgdXNlZnVsIHRvIGFuc3dlciB0aGUgcXVlc3Rpb25zLiBQYXkgYXR0ZW50aW9uIG9uIHRoZSB0aG9zZSBjb2x1bW5zIHRoYXQgYXJlIG5vdCBzZWVuIGluIHRoZSBleGFtcGxlcyBidXQgaW1wb3J0YW50IHRvIGFuc3dlciB0aGUgdXNlciBxdWVzdGlvbi4KLSAqKklNUE9SVEFOVCBOT1RFOioqIFlvdSBzaG91bGQgb3V0cHV0IHRoZSBjb2x1bW4gbmFtZXMgYXMgaXQgaXMgZ2l2ZW4gaW4gdGhlIFRhYmxlIFNjaGVtYS4KLSAqKklNUE9SVEFOVCBOT1RFOioqICoqSWYgYSBoaW50IGdpdmVuLCB5b3UgKipNVVNUKiogYWRkIGFsbCBjb2x1bW5zIG1lbnRpb25lZCBvciBleGlzdCBpbiB0aGUgaGludCBkaXJlY3RseS4gVGhpcyBpcyBhIHN0cmljdCBydWxlLioqCi0gKipJTVBPUlRBTlQgTk9URToqKiAqKklOIHlvdXIgcmVhc29uaW5nIHBhcnQsIHN0YXJ0IG5ldyBsaW5lIGFuZCBldmFsdWF0ZSBhIHNpbmdsZSBjb2x1bW4gaW4gZGV0YWlsIGJ5IGZpcnN0IHdyaXRpbmcgaXRzIG5hbWUsIHByb3BlcnRpZXMsIHlvdXIgdW5kZXJzdGFuZGluZyBhYm91dCB0aGUgY29sdW1uIGFuZCB0aGVuIHRoZSByZWFzb25zIGZvciB3aHkgdGhlIGNvbHVtbiBpcyByZWxhdmVudCBvciBpcnJlbGV2YW50IHRvIHRoZSBxdWVzdGlvbiBieSBzdHJpY3RseSBmb2xsb3dpbmcgdGhlIGluc3RydWN0aW9uIHN0ZXBzIGFib3ZlIG9uZSBieSBvbmUuKioKCntUQUJMRV9TQ0hFTUF9Cgp7RVhBTVBMRVN9CgpVc2VyIFF1ZXN0aW9uOgp7UVVFU1RJT05fQU5EX0hJTlR9CgojIyMgTm93LCBpdCBpcyB5b3VyIHR1cm4uCiMjIyBSZXNwb25kIGluIHRoZSBKU09OIGZvcm1hdCBhcyBmb2xsb3dzOgp7ewogICAgInJlYXNvbmluZyI6ICJJdGVyYXRlIG92ZXIgZWFjaCBjb2x1bW4gaW4gdGhlIHRhYmxlIGFuZCBwcm92aWRlIHJlYXNvbmluZyB3aGV0aGVyIHRoZSBjb2x1bW4gaXMgdXNlZnVsIGFuZCBuZWNlc3NhcnkgdG8gYW5zd2VyIHRoZSB1c2VyIHF1ZXN0aW9uLiBJZiB5b3UgYXJlIG5vdCBzdXJlIGFib3V0IHRoZSB1c2VmdWxuZXNzIG9mIGEgY29sdW1uLCB5b3Ugc2hvdWxkIGFkZCBpdCBhcyB3ZWxsLiBXaGlsZSBldmFsdWF0aW9uIGNvbHVtbiwgdGFrZSBhZHZhbnRhZ2UgZnJvbSB0aGUgZXhhbXBsZXMuIiwKICAgICJzZWxlY3RlZF9jb2x1bW5zIjogWyJjb2x1bW5fMSIsICJjb2x1bW5fMiIsICJjb2x1bW5fMyIsIC4uLl0KfX0=)
### You are an excellent data scientist. You can capture the link between user question and database elements (columns). You determine the relevant database columns perfectly. Your objective is to analyze and understand the essence of the given question, single database table schema, examples and then select the relevant columns of a given table.


### Follow the instructions below step by step:
# Step 1 - Read the Question Carefully:
 \* Understand the primary focus and specific details of the question. Identify named entities ( such as organizations, locations, etc.), technical terms, and other key phrases that encapsulate important aspects of the inquiry to establish a clear link between the question and the table columns.
 \* If a hint is given with the quesiton, review it. The hint provides specific information and directs attention toward certain elements relevant to the question and its answer. Use the hint to understand the relation between the question, the hint, and the given table columns. Always follow such logic explicitly.
# Step 2 - Analyze the Table Schema:
 \* You are given a schema of a single table in a database. Examine the table schema and detailed information about the columns to identify relevant columns that are pertinent to the question.
 \* Understand the meaning and purpose of the column, not just its name.
# Step 3 - Examine the Examples:
 \* Review each Text-to-SQL example that use the database elements the table come from.
 \* Analyze each question-SQL pair to understand the table columns and learn how they are used, in which contexts they are used.
 \* Use examples to guide your decision, but \*\*do not restrict yourself\*\* to only columns seen in examples.
# Step 4 - Select Useful Columns:
 \* Consider each column one by one in detail to determine it is useful and required to answer the questions. When iterating through each column, write detailed reasoning why a column is necessary and useful or not. While evaluating a column, you can take the advantage from the examples.
 - At each new line, start with column name that you consider. Go through the information about the column and state the properties of the column. Then start reasoning whether it is related to the questoin or not.
 \* For each column in the given table schema, ask yourself: Is this column directly necessary or indirectly helpful to answer the question?
 - If yes, include it.
 - If the question or hint specifies this column, include it.
 - If it’s part of a formula or computation, include it.
 - If you’re unsure, err on the side of including it.
 \* When unsure about a column, prefer to include a column unless it explicitly contradicts the question or hint. Use examples to inform your judgment, but do not overfit to them.
 \* Always follow the formula or calculation logic explicitly provided in the question or hint.
 \* \*\*IMPORTANT\*\* If the question and hint describe a formula using specific column names, you must select those exact columns, even if alternative or redundant columns (e.g., percentage, rate, average) are present in the schema. \*\*Do not\*\* assume that similar-looking columns satisfy the requirement.
 \* If a question requires aggregate function on a column, you \*\*must\*\* select that column.
 \* Determine a question requires aggregate function, then think and elaborate on which column aggretation should be applied.
 \* For example, if a user question needs counting (requiring COUNT aggregate function), then select a column on which aggregate function should be applied. You \*\*must\*\* list that column in your answer.
 \* When the question requires unique values (e.g., IDs, URLs), the corresponding SQL query will use ‘SELECT DISTINCT‘. Refer to column statistics ("Value Statics") to determine if ‘DISTINCT‘ is necessary.
 \* If all columns of the table are irrelevant to the question, then return empty Python List for the selected\_columns key in the response.
# Step 5: Output Format:
 \* Give your response in JSON format with two following keys: "reasoning" and "selected\_columns" where value of a selected\_columns \*\*must\*\* be a Python List and the value of the "reasoning" should be string reasoning on each column and their usefulness.


- \*\*IMPORTANT NOTE:\*\* Some columns might not be used in the examples given, but it can be necessary or useful. Although a column is not used in examples, it might be necessary or useful to answer the questions. Pay attention on the those columns that are not seen in the examples but important to answer the user question.
- \*\*IMPORTANT NOTE:\*\* You should output the column names as it is given in the Table Schema.
- \*\*IMPORTANT NOTE:\*\* \*\*If a hint given, you \*\*MUST\*\* add all columns mentioned or exist in the hint directly. This is a strict rule.\*\*
- \*\*IMPORTANT NOTE:\*\* \*\*IN your reasoning part, start new line and evaluate a single column in detail by first writing its name, properties, your understanding about the column and then the reasons for why the column is relavent or irrelevant to the question by strictly following the instruction steps above one by one.\*\*


{TABLE\_SCHEMA}


{EXAMPLES}


User Question:
{QUESTION\_AND\_HINT}


### Now, it is your turn.
### Respond in the JSON format as follows:
{{
 "reasoning": "Iterate over each column in the table and provide reasoning whether the column is useful and necessary to answer the user question. If you are not sure about the usefulness of a column, you should add it as well. While evaluation column, take advantage from the examples.",
 "selected\_columns": ["column\_1", "column\_2", "column\_3", ...]
}}

## Appendix I SQL Generation Prompt Template

[⬇](data:text/plain;base64,KioqIFlvdSBhcmUgYW4gZXhwZXJ0IFNRTCBnZW5lcmF0b3IuIFlvdXIgdGFzayBpcyB0byBnZW5lcmF0ZSBhIFNRTCBxdWVyeSBmb3IgdGhlIGdpdmVuIHVzZXIgcXVlc3Rpb24sIGNvbnNpZGVyaW5nICpvbmx5KiB0aGUge0RCX0lEfSBkYXRhYmFzZS4KCiMjIyBJTlRSVUNUSU9OUzoKKiBVbmRlcnN0YW5kIHRoZSBxdWVzdGlvbjoKICAgIC0gQ2FyZWZ1bGx5IHJlYWQgYW5kIGludGVycHJldCB0aGUgdXNlcidzIG5hdHVyYWwgbGFuZ3VhZ2UgcXVlc3Rpb24uCiAgICAtIENvbnNpZGVyIG9ubHkgdGhlIHtEQl9JRH0gZGF0YWJhc2Ugd2hlbiBhbmFseXppbmcgdGhlIHF1ZXN0aW9uLgogICAgLSBBbmFseXplIHRoZSByZWxhdGlvbiBiZXR3ZWVuIHF1ZXN0aW9uIGFuZCBkYXRhYmFzZSBpdGVtcy4KKiBEZXRlcm1pbmUgdGhlIHJlcXVpcmVkIGRhdGFiYXNlIGl0ZW1zOgogICAgLSBJbiBvcmRlciB0byBjb25zdHJ1Y3QgdGhlIFNRTCBxdWVyeSB0byBhbnN3ZXIgdGhlIHVzZXIgcXVlc3Rpb24sIERldGVybWluZSB3aGljaCB0YWJsZXMsIGNvbHVtbnMsIGFuZCB2YWx1ZXMgZnJvbSB0aGUgZGF0YWJhc2UgYXJlIG5lZWRlZCB0byBhbnN3ZXIgdGhlIHF1ZXN0aW9uLgogICAgLSBBbmFseXplIHRoZSByZWxhdGlvbnMgYmV0d2VlbiBzZWxlY3RlZCB0YWJsZXMgYW5kIGNvbHVtbnMKKiBBcHBseSBMb2dpY2FsIEZpbHRlcmluZzoKICAgIC0gSWRlbnRpZnkgdGhlIHJlcXVpcmVkIGZpbHRlcmluZyBjb25kaXRpb25zLCBhZ2dyZWdhdGlvbnMsIGdyb3VwaW5ncywgd2luZG93IGZ1bmN0aW9ucywgb3JkZXJpbmdzIG9yIGxpbWl0IG5lZWRlZCB0byBmdWxmaWxsIHRoZSBpbnRlbnQgb2YgdGhlIHF1ZXN0aW9uLgoqIENvbnN0cnVjdCB0aGUgU1FMIHF1ZXJ5OgogICAgLSBDb25zdHJ1Y3QgYSB2YWxpZCBhbmQgZXhlY3V0YWJsZSBTUUxpdGUgU1FMIHF1ZXJ5IHRoYXQgZGlyZWN0bHkgYW5zd2VycyB0aGUgcXVlc3Rpb24gdXNpbmcgb25seSB0aGUgcmVsZXZhbnQgcGFydHMgb2YgdGhlIHNjaGVtYS4KCgp7QVVHTUVOVEFUSU9OfQoKIyMjIEdlbmVyYXRlIFNRTGl0ZSBTUUwgcXVlcnkgZm9yIHRoZSBmb2xsb3dpbmcgcXVlc3Rpb24gY29uc2lkZXJpbmcgKipvbmx5Kioge0RCX0lEfSBkYXRhYmFzZS4KKioqIFF1ZXN0aW9uICoqKgp7UVVFU1RJT059CgojIyMgUmVzcG9uZCBpbiB0aGUgZm9sbG93aW5nIGZvcm1hdDoKPHJlYXNvbmluZz4KQW5hbHlzaXMgYWJvdXQgdGhlIHF1ZXN0aW9uIHB1cnBvc2UgYW5kIHJlbGF0aW9uIGJldHdlZW4gZGF0YWJhc2UgaXRlbXMuIFN0ZXBzIHRvIGFuc3dlciB0aGUgdXNlciBxdWVzdGlvbiBhbmQgY3JlYXRlIGNvcnJlY3QgU1FMIHF1ZXJ5IGluIGRldGFpbC4gVmVyeSBkZXRhaWxlZCByZWFzb25pbmcgYW5kIGxvZ2ljIHRvIGNyZWF0ZSBjb3JyZWN0IFNRTGl0ZSBTUUwgcXVlcnkuIFRoZSByZWFzb25zIGZvciBzZWxlY3RpbmcgZGF0YWJhc2UgaXRlbXMgKHRhYmxlcyBhbmQgY29sdW1ucykuIEZpbHRlcnMsIGFnZ3JlZ2F0aW9ucyBhbmQgd2luZG93IGZ1bmN0aW9ucyB0aGF0IHNob3VsZCBiZSB1dGlsaXplZCBhbmQgYXBwbGllZCB3aXRoIHRoZWlyIHJlYXNvbmluZy4KPC9yZWFzb25pbmc+CjxhbnN3ZXI+CkdlbmVyYXRlZCBTUUxpdGUgU1FMIHF1ZXJ5IHRvIGFuc3dlciB0aGUgcXVlc3Rpb24uCjwvYW5zd2VyPgoKIyMjIE5vdyBpcyB5b3VyIHR1cm4gdG8gcmVzcG9uZCBpbiB0aGUgYWJvdmUgZm9ybWF0Og==)
\*\*\* You are an expert SQL generator. Your task is to generate a SQL query for the given user question, considering \*only\* the {DB\_ID} database.


### INTRUCTIONS:
\* Understand the question:
 - Carefully read and interpret the user’s natural language question.
 - Consider only the {DB\_ID} database when analyzing the question.
 - Analyze the relation between question and database items.
\* Determine the required database items:
 - In order to construct the SQL query to answer the user question, Determine which tables, columns, and values from the database are needed to answer the question.
 - Analyze the relations between selected tables and columns
\* Apply Logical Filtering:
 - Identify the required filtering conditions, aggregations, groupings, window functions, orderings or limit needed to fulfill the intent of the question.
\* Construct the SQL query:
 - Construct a valid and executable SQLite SQL query that directly answers the question using only the relevant parts of the schema.




{AUGMENTATION}


### Generate SQLite SQL query for the following question considering \*\*only\*\* {DB\_ID} database.
\*\*\* Question \*\*\*
{QUESTION}


### Respond in the following format:
<reasoning>
Analysis about the question purpose and relation between database items. Steps to answer the user question and create correct SQL query in detail. Very detailed reasoning and logic to create correct SQLite SQL query. The reasons for selecting database items (tables and columns). Filters, aggregations and window functions that should be utilized and applied with their reasoning.
</reasoning>
<answer>
Generated SQLite SQL query to answer the question.
</answer>


### Now is your turn to respond in the above format:

Generated on Tue Sep 30 02:04:10 2025 by [LaTeXML![Mascot Sammy](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAsAAAAOCAYAAAD5YeaVAAAAAXNSR0IArs4c6QAAAAZiS0dEAP8A/wD/oL2nkwAAAAlwSFlzAAALEwAACxMBAJqcGAAAAAd0SU1FB9wKExQZLWTEaOUAAAAddEVYdENvbW1lbnQAQ3JlYXRlZCB3aXRoIFRoZSBHSU1Q72QlbgAAAdpJREFUKM9tkL+L2nAARz9fPZNCKFapUn8kyI0e4iRHSR1Kb8ng0lJw6FYHFwv2LwhOpcWxTjeUunYqOmqd6hEoRDhtDWdA8ApRYsSUCDHNt5ul13vz4w0vWCgUnnEc975arX6ORqN3VqtVZbfbTQC4uEHANM3jSqXymFI6yWazP2KxWAXAL9zCUa1Wy2tXVxheKA9YNoR8Pt+aTqe4FVVVvz05O6MBhqUIBGk8Hn8HAOVy+T+XLJfLS4ZhTiRJgqIoVBRFIoric47jPnmeB1mW/9rr9ZpSSn3Lsmir1fJZlqWlUonKsvwWwD8ymc/nXwVBeLjf7xEKhdBut9Hr9WgmkyGEkJwsy5eHG5vN5g0AKIoCAEgkEkin0wQAfN9/cXPdheu6P33fBwB4ngcAcByHJpPJl+fn54mD3Gg0NrquXxeLRQAAwzAYj8cwTZPwPH9/sVg8PXweDAauqqr2cDjEer1GJBLBZDJBs9mE4zjwfZ85lAGg2+06hmGgXq+j3+/DsixYlgVN03a9Xu8jgCNCyIegIAgx13Vfd7vdu+FweG8YRkjXdWy329+dTgeSJD3ieZ7RNO0VAXAPwDEAO5VKndi2fWrb9jWl9Esul6PZbDY9Go1OZ7PZ9z/lyuD3OozU2wAAAABJRU5ErkJggg==)](http://dlmf.nist.gov/LaTeXML/)