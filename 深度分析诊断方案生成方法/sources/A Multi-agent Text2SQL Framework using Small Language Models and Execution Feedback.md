> Source: https://arxiv.org/html/2512.18622v1

A Multi-agent Text2SQL Framework using Small Language Models and Execution Feedback





1. [1 Introduction](https://arxiv.org/html/2512.18622v1#S1 "In A Multi-agent Text2SQL Framework using Small Language Models and Execution Feedback")
2. [2 Model and Requirements](https://arxiv.org/html/2512.18622v1#S2 "In A Multi-agent Text2SQL Framework using Small Language Models and Execution Feedback")
   1. [2.1 Problem Formulation](https://arxiv.org/html/2512.18622v1#S2.SS1 "In 2. Model and Requirements ‣ A Multi-agent Text2SQL Framework using Small Language Models and Execution Feedback")
   2. [2.2 Requirements](https://arxiv.org/html/2512.18622v1#S2.SS2 "In 2. Model and Requirements ‣ A Multi-agent Text2SQL Framework using Small Language Models and Execution Feedback")
3. [3 The MATS Framework](https://arxiv.org/html/2512.18622v1#S3 "In A Multi-agent Text2SQL Framework using Small Language Models and Execution Feedback")
   1. [3.1 Schema Insight Agent](https://arxiv.org/html/2512.18622v1#S3.SS1 "In 3. The MATS Framework ‣ A Multi-agent Text2SQL Framework using Small Language Models and Execution Feedback")
   2. [3.2 Planner Agent](https://arxiv.org/html/2512.18622v1#S3.SS2 "In 3. The MATS Framework ‣ A Multi-agent Text2SQL Framework using Small Language Models and Execution Feedback")
   3. [3.3 Validator Agent](https://arxiv.org/html/2512.18622v1#S3.SS3 "In 3. The MATS Framework ‣ A Multi-agent Text2SQL Framework using Small Language Models and Execution Feedback")
   4. [3.4 Fix Agent](https://arxiv.org/html/2512.18622v1#S3.SS4 "In 3. The MATS Framework ‣ A Multi-agent Text2SQL Framework using Small Language Models and Execution Feedback")
   5. [3.5 Selection Agent](https://arxiv.org/html/2512.18622v1#S3.SS5 "In 3. The MATS Framework ‣ A Multi-agent Text2SQL Framework using Small Language Models and Execution Feedback")
   6. [3.6 Data Generation for Supervised Fine-Tuning](https://arxiv.org/html/2512.18622v1#S3.SS6 "In 3. The MATS Framework ‣ A Multi-agent Text2SQL Framework using Small Language Models and Execution Feedback")
4. [4 Reinforcement Learning from Execution Feedback](https://arxiv.org/html/2512.18622v1#S4 "In A Multi-agent Text2SQL Framework using Small Language Models and Execution Feedback")
   1. [4.1 Modeling](https://arxiv.org/html/2512.18622v1#S4.SS1 "In 4. Reinforcement Learning from Execution Feedback ‣ A Multi-agent Text2SQL Framework using Small Language Models and Execution Feedback")
   2. [4.2 Action Sampling](https://arxiv.org/html/2512.18622v1#S4.SS2 "In 4. Reinforcement Learning from Execution Feedback ‣ A Multi-agent Text2SQL Framework using Small Language Models and Execution Feedback")
   3. [4.3 Agent Alignment Training](https://arxiv.org/html/2512.18622v1#S4.SS3 "In 4. Reinforcement Learning from Execution Feedback ‣ A Multi-agent Text2SQL Framework using Small Language Models and Execution Feedback")
5. [5 Empirical Evaluation](https://arxiv.org/html/2512.18622v1#S5 "In A Multi-agent Text2SQL Framework using Small Language Models and Execution Feedback")
   1. [5.1 Experimental Setup](https://arxiv.org/html/2512.18622v1#S5.SS1 "In 5. Empirical Evaluation ‣ A Multi-agent Text2SQL Framework using Small Language Models and Execution Feedback")
   2. [5.2 End-to-end comparison](https://arxiv.org/html/2512.18622v1#S5.SS2 "In 5. Empirical Evaluation ‣ A Multi-agent Text2SQL Framework using Small Language Models and Execution Feedback")
   3. [5.3 Evaluation on Robustness Benchmarks](https://arxiv.org/html/2512.18622v1#S5.SS3 "In 5. Empirical Evaluation ‣ A Multi-agent Text2SQL Framework using Small Language Models and Execution Feedback")
   4. [5.4 Hyperparameter Sensitivity](https://arxiv.org/html/2512.18622v1#S5.SS4 "In 5. Empirical Evaluation ‣ A Multi-agent Text2SQL Framework using Small Language Models and Execution Feedback")
   5. [5.5 Improvement after each RLEF Iteration](https://arxiv.org/html/2512.18622v1#S5.SS5 "In 5. Empirical Evaluation ‣ A Multi-agent Text2SQL Framework using Small Language Models and Execution Feedback")
   6. [5.6 Comparison of Alignment Algorithms](https://arxiv.org/html/2512.18622v1#S5.SS6 "In 5. Empirical Evaluation ‣ A Multi-agent Text2SQL Framework using Small Language Models and Execution Feedback")
   7. [5.7 Planner Prompt Comparison](https://arxiv.org/html/2512.18622v1#S5.SS7 "In 5. Empirical Evaluation ‣ A Multi-agent Text2SQL Framework using Small Language Models and Execution Feedback")
   8. [5.8 Database Domain Adaption](https://arxiv.org/html/2512.18622v1#S5.SS8 "In 5. Empirical Evaluation ‣ A Multi-agent Text2SQL Framework using Small Language Models and Execution Feedback")
   9. [5.9 Evaluating on SQL Characteristics](https://arxiv.org/html/2512.18622v1#S5.SS9 "In 5. Empirical Evaluation ‣ A Multi-agent Text2SQL Framework using Small Language Models and Execution Feedback")
6. [6 Related Work](https://arxiv.org/html/2512.18622v1#S6 "In A Multi-agent Text2SQL Framework using Small Language Models and Execution Feedback")
7. [7 Conclusion](https://arxiv.org/html/2512.18622v1#S7 "In A Multi-agent Text2SQL Framework using Small Language Models and Execution Feedback")

# A Multi-agent Text2SQL Framework using Small Language Models and Execution Feedback

Thanh Dat Hoang1,
Thanh Trung Huynh2, Matthias Weidlich3, Thanh Tam Nguyen1, Tong
Chen4, Hongzhi Yin4, Quoc Viet Hung Nguyen1
1Griffith University (Australia), 2VinUniversity (Vietnam),
  
3Humboldt-Universitat zu Berlin (Germany), 4The University of
Queensland, Australia

(2025)

###### Abstract.

Text2SQL, the task of generating SQL queries from natural language text, is a critical challenge in data engineering. Recently, Large Language Models (LLMs) have demonstrated superior performance for this task due to their advanced comprehension and generation capabilities. However, privacy and cost considerations prevent companies from using Text2SQL solutions based on external LLMs offered as a service. Rather, small LLMs (SLMs) that are openly available and can hosted in-house are adopted. These SLMs, in turn, lack the generalization capabilities of larger LLMs, which impairs their effectiveness for complex tasks such as Text2SQL. To address these limitations, we propose MATS, a novel Text2SQL framework designed specifically for SLMs. MATS uses a multi-agent mechanism that assigns specialized roles to auxiliary agents, reducing individual workloads and fostering interaction. A training scheme based on reinforcement learning aligns these agents using feedback obtained during execution, thereby maintaining competitive performance despite a limited LLM size. Evaluation results using on benchmark datasets show that MATS, deployed on a single-GPU server, yields accuracy that are on-par with large-scale LLMs when using significantly fewer parameters. Our source code and data are available at <https://github.com/thanhdath/mats-sql>.

Text2SQL, Small Language Models, Multi-agent Systems

††copyright: none††journalyear: 2025††ccs: Information systems Structured Query Language††ccs: Information systems Language models††ccs: Theory of computation Multi-agent learning

## 1. Introduction

Text2SQL, the task of translating natural language into SQL queries, is a
long-standing research challenge (Zhong et al., [2017](https://arxiv.org/html/2512.18622v1#bib.bib55); Xu et al., [2017](https://arxiv.org/html/2512.18622v1#bib.bib50); Yu et al., [2018a](https://arxiv.org/html/2512.18622v1#bib.bib51), [b](https://arxiv.org/html/2512.18622v1#bib.bib52)). While an increasing complexity of user
queries and database schemas contribute to the task’s
difficulty (Rokis and Kirikova, [2022](https://arxiv.org/html/2512.18622v1#bib.bib40)), recent solutions based on Large
Language Models (LLMs) achieved notable results for
Text2SQL (Pourreza and Rafiei, [2023a](https://arxiv.org/html/2512.18622v1#bib.bib34); Sun et al., [2023](https://arxiv.org/html/2512.18622v1#bib.bib44); Dong et al., [2023](https://arxiv.org/html/2512.18622v1#bib.bib7); Liu et al., [2023](https://arxiv.org/html/2512.18622v1#bib.bib24)).
Text2SQL approaches promise to
enable non-experts to query databases using a natural
language interface (Touvron et al., [2023](https://arxiv.org/html/2512.18622v1#bib.bib46); Papicchio et al., [2025](https://arxiv.org/html/2512.18622v1#bib.bib31)).
Most existing solutions for this task, however, rely on external LLMs
offered as a
service (Naveed et al., [2025](https://arxiv.org/html/2512.18622v1#bib.bib29); Schellaert et al., [2025](https://arxiv.org/html/2512.18622v1#bib.bib42)), primarily variants of OpenAI GPT, to generate SQL queries. These
approaches combine user queries and schema representations with
instructional text to generate SQL
queries (Roziere et al., [2023](https://arxiv.org/html/2512.18622v1#bib.bib41); Li et al., [2023a](https://arxiv.org/html/2512.18622v1#bib.bib23)). However, the use of
external LLM services comes with drawbacks. Privacy concerns arise
when sensitive data, such as database schemas or query logs, are shared
with third-party platforms, potentially violating confidentiality
or exposing data to security risks. Also, the recurring costs of
such services can become a substantial financial burden, especially
for small organizations.

To be independent of external LLM services, recent approaches for Text2SQL
fine-tune open-source LLMs with instructional
data (Kumar et al., [2022](https://arxiv.org/html/2512.18622v1#bib.bib15); Raffel et al., [2020](https://arxiv.org/html/2512.18622v1#bib.bib39); Dong et al., [2024](https://arxiv.org/html/2512.18622v1#bib.bib6)).
Fine-tuning improves the task-specific model performance, but requires
significant computational resources and
technical expertise. In addition, even with models as large as 15 billion
parameters, the accuracy obtained using open-source LLMs is
considerably lower than the one achieved with
external LLM services (Lan et al., [2023](https://arxiv.org/html/2512.18622v1#bib.bib17); Li et al., [2024c](https://arxiv.org/html/2512.18622v1#bib.bib20)).
Striving for a cost-effective solution, one may adopt small Large Language
Models (SLMs) with generally smaller numbers of parameters (typically
100M-5B) (Lu et al., [2024](https://arxiv.org/html/2512.18622v1#bib.bib26)). Such models are optimized to run on a
single-node server that features a single GPU. While the use of SLMs
enlarges the efficiency and, hence, applicability of a Text2SQL solution,
one faces challenges in terms of model effectiveness. SLMs often struggle
with tasks that require deep reasoning or
understanding of complex contexts, such as required for
Text2SQL (Lu et al., [2024](https://arxiv.org/html/2512.18622v1#bib.bib26)).
Their limited capacity makes it challenging to maintain relationships
between tables or fields, especially with large schemas, and they
frequently
miss nuances in natural language inputs, leading to syntax or semantic
errors in SQL generation.

In this paper, we follow the idea of using SLMs for Text2SQL and propose the
Multi-Agent Text2SQL (MATS) framework to
operationalize it. MATS employs a multi-agent
mechanism (Qian et al., [2024](https://arxiv.org/html/2512.18622v1#bib.bib36); Islam et al., [2024](https://arxiv.org/html/2512.18622v1#bib.bib14); Guo et al., [2024](https://arxiv.org/html/2512.18622v1#bib.bib12)) to
decompose the Text2SQL task into sub-tasks, each handled by a specialized
agent: a schema investigator filters irrelevant schema elements and
retrieves relevant column values; a query planner generates multiple SQL
queries step-by-step; a validator evaluates SQL outputs using database
responses; a fix agent refines SQL based on validator feedback; and a
selection agent, at the end of the pipeline, selects the best SQL query from
the final candidates. To enhance the collaboration between the agents, we
design a collaborative training scheme, coined Reinforcement Learning with
Execution Feedback (RLEF). Unlike traditional Reinforcement Learning from
Human Feedback (Ouyang et al., [2022](https://arxiv.org/html/2512.18622v1#bib.bib30)), RLEF generates multiple responses
using automated database feedback, avoiding the need for costly
human-labeled data.

![Refer to caption](motivating_example.png)


Figure 1. Execution accuracy (EX%) of MATS vs. other
approaches on BIRD dev. Methods using open-source models and
proprietary LLMs are separated by the dashed line.

The divide-and-conquer strategy realized in MATS is beneficial in terms of
efficiency
and effectiveness. Due to the specialization of agents and
their focus on a single sub-task, the generalization capabilities of SLMs,
which can be managed efficiently, are sufficient to yield high accuracy. At
the same time, the integration of the agents using reinforcement learning
enables our framework to effectively handle complex user queries and
large-scale datasets. Furthermore, our framework facilitates the adaptation of open-source SLMs, thereby supporting wider applicability on resource-constrained devices and under restricted budgets.

We summarize the contributions of our paper as follows:

* •

  We propose a novel multi-agent framework in which specialized
  agents rely on SLMs to collaboratively solve Text2SQL tasks. The framework
  defines sub-tasks for element filtering, query planing, validation of query
  results, refinement of queries, and query selection.
* •

  We introduce Reinforcement Learning with Execution Feedback (RLEF) as
  a mechanism to enable SLMs agents to collaborate during training,
  significantly improving their performance in Text2SQL tasks.
  It relies on recent advancements for preference
  optimization (Hong et al., [2024](https://arxiv.org/html/2512.18622v1#bib.bib13))
  and instantiates them based on a sampling scheme for appropriate responses.
* •

  We create a comprehensive dataset tailored for training SLMs agents by extending the Spider and BIRD datasets through manual labeling, few-shot prompting, and fine-tuning, ensuring high-quality examples for robust learning.
* •

  We evaluate MATS in comprehensive experiments and observe that it achieves
  results that are on-par with large-scale LLMs, such as GPT-4o +
  CoT (Li et al., [2023b](https://arxiv.org/html/2512.18622v1#bib.bib21)) and CHESS (Talaei et al., [2024](https://arxiv.org/html/2512.18622v1#bib.bib45)), while relying on
  significantly smaller models.
* •

  Our source code and data are available at <https://github.com/thanhdath/mats-sql>.

[Fig. 1](https://arxiv.org/html/2512.18622v1#S1.F1 "Figure 1 ‣ 1. Introduction ‣ A Multi-agent Text2SQL Framework using Small Language Models and Execution Feedback") illustrates the main
insight from our experiments in terms of the relation of the execution
accuracy and the total size of the model in terms of its parameters. With
total model size of 9B, MATS is optimized for resource-constrained
environments. Our experimental results show that MATS enables efficient inference without
sacrificing performance, which renders it
well-suited for cost-sensitive deployments.

In the remainder of the paper, [§ 2](https://arxiv.org/html/2512.18622v1#S2 "2. Model and Requirements ‣ A Multi-agent Text2SQL Framework using Small Language Models and Execution Feedback") formulates the
addressed problem. [§ 3](https://arxiv.org/html/2512.18622v1#S3 "3. The MATS Framework ‣ A Multi-agent Text2SQL Framework using Small Language Models and Execution Feedback") outlines the key components of
the MATS framework and their instantiation.
[§ 4](https://arxiv.org/html/2512.18622v1#S4 "4. Reinforcement Learning from Execution Feedback ‣ A Multi-agent Text2SQL Framework using Small Language Models and Execution Feedback") introduces our approach to Reinforcement Learning with
Execution Feedback (RLEF).
Evaluation results are presented in [§ 5](https://arxiv.org/html/2512.18622v1#S5 "5. Empirical Evaluation ‣ A Multi-agent Text2SQL Framework using Small Language Models and Execution Feedback"), before we review our
contributions in the light of
related work in [§ 6](https://arxiv.org/html/2512.18622v1#S6 "6. Related Work ‣ A Multi-agent Text2SQL Framework using Small Language Models and Execution Feedback") and conclude the paper in
[§ 7](https://arxiv.org/html/2512.18622v1#S7 "7. Conclusion ‣ A Multi-agent Text2SQL Framework using Small Language Models and Execution Feedback").

## 2. Model and Requirements

We first characterize the problem addressed in this work
([§ 2.1](https://arxiv.org/html/2512.18622v1#S2.SS1 "2.1. Problem Formulation ‣ 2. Model and Requirements ‣ A Multi-agent Text2SQL Framework using Small Language Models and Execution Feedback")), before elaborating on requirements for
solutions to it ([§ 2.2](https://arxiv.org/html/2512.18622v1#S2.SS2 "2.2. Requirements ‣ 2. Model and Requirements ‣ A Multi-agent Text2SQL Framework using Small Language Models and Execution Feedback")).

### 2.1. Problem Formulation

Text2SQL addresses the task of generating an SQL query 𝒴\mathcal{Y} that
corresponds to a given natural language question qq. This query
is constructed based on a database schema S{S} and, optionally, an
external knowledge base K{K}. The database schema S{S} is
defined by
a set of tables {T1,T2,…,Tm}\left\{{T}\_{1},{T}\_{2},\ldots,{T}\_{m}\right\},
a set of columns
{C1,C2,…,Cn}\left\{{C}\_{1},{C}\_{2},\ldots,{C}\_{n}\right\}, and
a set of foreign key relations {R1,R2,…,Rk}\left\{{R}\_{1},{R}\_{2},\ldots,{R}\_{k}\right\}.
The optional external
knowledge base K{K} provides context for the schema, aiding in
generating more accurate SQL in ambiguous situations.

Mathematically, the Text2SQL task is formulated as:

|  |  |  |
| --- | --- | --- |
|  | 𝒴=f​(q,S,K∣𝜽),\mathcal{Y}=f(q,{S},{K}\mid\boldsymbol{\theta}), |  |

where the function f(⋅∣𝜽)f(\cdot\mid\boldsymbol{\theta}) represents a
generative model (e.g., a neural network) with learnable parameters
𝜽\boldsymbol{\theta}.

### 2.2. Requirements

We argue that any SLMs-based solution for Text2SQL shall address the
following requirements:

(R1) Large Database Schema.
A Text2SQL solution shall handle large database schemas. This is
challenging as the sheer
number of tables and columns can exceed the model’s context length,
impairing comprehension. Real-world schemas
often include overlapping column names and extensive metadata, further
complicating the respective task. For example, the BIRD
dataset features databases with up to 65 tables and 455 columns, increasing
the likelihood of errors in schema linking and SQL query
generation (Li et al., [2024b](https://arxiv.org/html/2512.18622v1#bib.bib18)).

(R2) Ambiguous Column Names and Values.
A Text2SQL solution shall cope with the ambiguity in column names and
values, especially when multiple columns share similar meanings or
overlapping values. For example, names of organizations may appear in
different roles, and hence, as different columns in database.
Correctly linking queries to columns is then challenging and increases the
risk of incorrect SQL generation.

(R3) Weak Reasoning Capability of SLMs.
A Text2SQL solution based on SLMs needs to address the limited reasoning
capabilities of the respective models.
Specifically, chain-of-thought prompting, which enhances
reasoning in large models, is less effective for SLMs and can even produce
fluent, yet illogical reasoning outputs (Wei et al., [2022](https://arxiv.org/html/2512.18622v1#bib.bib48)). In Text2SQL
tasks, this limitation becomes particularly important and SLMs have been
observed to frequently generate
inaccurate SQL queries for complex database schemas (Li et al., [2024b](https://arxiv.org/html/2512.18622v1#bib.bib18)).

(R4) Low Instruction Following Capability.
SLMs struggle with instruction following due to their limited parameter
size (Murthy et al., [2024](https://arxiv.org/html/2512.18622v1#bib.bib28)), which needs to be incorporated in Text2SQL
solutions using these models. SLMs tend to overfit to specific training
formats and typically lack exposure to diverse instruction-tuning datasets,
such as InFoBench (Qin et al., [2024](https://arxiv.org/html/2512.18622v1#bib.bib37)) or
IFEval (Zhou et al., [2023](https://arxiv.org/html/2512.18622v1#bib.bib56)). Hence, SLMs are limited in their
generalization to new or varied instruction types, as well as instructions
that involve dependencies and sequential logic.

## 3. The MATS Framework

This section presents our Multi-Agent
Text2SQL (MATS) framework. As illustrated in
[Fig. 2](https://arxiv.org/html/2512.18622v1#S3.F2 "Figure 2 ‣ 3. The MATS Framework ‣ A Multi-agent Text2SQL Framework using Small Language Models and Execution Feedback"), it adopts the paradigm of multi-agent
collaboration, i.e., a splits the Text2SQL task into sub-tasks that are
handled by individual agents.

![Refer to caption](MainFlowMATS.drawio.png)


Figure 2. Overview of our multi-agent framework for Text2SQL.

Given a user query and database schema, the
process
begins with the Schema Insight Agent, which
extracts relevant tables and columns, even when the query does not exactly
match stored values. As such, this agent explicitly addresses the
requirements of handling large database schemas (R1) and ambiguous column
names and values (R2).
Next, the Planner
Agent decomposes the reasoning process into a chain
of thoughts. It addresses the weak reasoning capabilities (R3) of SLMs by
generating SQL candidates.
The Validator Agent
then evaluates these candidates and their
execution results, identifying potential errors. Any detected issues are
refined by the Fix Agent. Finally, the
Selection Agent chooses the best SQL
query based on execution responses.

In the remainder of this section, we elaborate on the realization of the
individual agents ([§ 3.1](https://arxiv.org/html/2512.18622v1#S3.SS1 "3.1. Schema Insight Agent ‣ 3. The MATS Framework ‣ A Multi-agent Text2SQL Framework using Small Language Models and Execution Feedback") - [§ 3.5](https://arxiv.org/html/2512.18622v1#S3.SS5 "3.5. Selection Agent ‣ 3. The MATS Framework ‣ A Multi-agent Text2SQL Framework using Small Language Models and Execution Feedback")), before
turning to the creation of training data for fine-tuning
([§ 3.6](https://arxiv.org/html/2512.18622v1#S3.SS6 "3.6. Data Generation for Supervised Fine-Tuning ‣ 3. The MATS Framework ‣ A Multi-agent Text2SQL Framework using Small Language Models and Execution Feedback")), which also caters for the weak
reasoning capabilities (R3) of SLMs.

### 3.1. Schema Insight Agent

Given a question posed by a user as input, the Schema Insight Agent filters
out irrelevant
schema
elements and retrieves relevant column values. To this end, it includes two
components: Schema Filtering and Value Matching.
Schema Filtering eliminates tables and columns
that are unlikely to contribute to generating the correct SQL query. In our
framework, we adopt CodeS (Li et al., [2024c](https://arxiv.org/html/2512.18622v1#bib.bib20)) for this purpose. It uses a
bidirectional encoder to rank tables and columns, and discards those with
low relevance to the given user question.
Value Matching leverages the BM-25 algorithm (Askari et al., [2023](https://arxiv.org/html/2512.18622v1#bib.bib2)) to
identify column
values that closely align with the input query. This functionality is
essential for selecting the appropriate columns for the generation of
accurate SQL queries.
Specifically, given an input question qq, for each column cic\_{i} in
the pruned schema C={c1,c2,…,cn}C=\{c\_{1},c\_{2},\dots,c\_{n}\} that is obtained by
Schema Filtering, we retrieve a set of
candidate values Vci={vi​1,vi​2,…,vi​m}V\_{c\_{i}}=\{v\_{i1},v\_{i2},\dots,v\_{im}\}. We
compute the BM25 relevance score between the question and each
value:

|  |  |  |
| --- | --- | --- |
|  | Score​(q,vi​j)=BM25​(q,vi​j).\text{Score}(q,v\_{ij})=\text{BM25}(q,v\_{ij}). |  |

Then, we select the kk values with highest scores for each
column:

|  |  |  |
| --- | --- | --- |
|  | Vci∗=Topk⁡(Vci,Score​(q,Vci)),V\_{c\_{i}}^{\*}=\operatorname{Top}\_{k}\left(V\_{c\_{i}},\text{Score}(q,V\_{c\_{i}})\right), |  |

where typically k=2k=2.
If no values yield a positive BM25 score, we
select a representative example value from VciV\_{c\_{i}}. The selected
values Vci∗V\_{c\_{i}}^{\*} are then incorporated into the database schema
prompt, providing the model with contextual cues for SQL generation.

### 3.2. Planner Agent

The Planner Agent generates SQL queries by decomposing the reasoning process
into small, step-by-step operations, enabling SLMs to construct accurate and
well-structured queries. As the central component of the system, this agent
is responsible for translating user questions into SQL queries to fulfill
the given task.

We manually design a reasoning process based on few-shot examples that
consists of three steps: 1) identifying the selection goal, 2) analyzing
conditions for the WHERE clause, and 3) determining the necessary tables for
the FROM and JOIN clauses. This systematic approach guides the model
through the process of deciding what to select, which conditions to apply,
and, thus, which tables to use. An example of the thought process is
illustrated in [Fig. 3](https://arxiv.org/html/2512.18622v1#S3.F3 "Figure 3 ‣ 3.2. Planner Agent ‣ 3. The MATS Framework ‣ A Multi-agent Text2SQL Framework using Small Language Models and Execution Feedback").

Let xx represent a data sample containing a question, a database
schema, and, optionally, an external knowledge base. The Planner Agent
generates a plan pp and a SQL query ss as follows:

|  |  |  |  |
| --- | --- | --- | --- |
| (1) |  | p←πp​(x)p\leftarrow\pi\_{p}(x) |  |

|  |  |  |  |
| --- | --- | --- | --- |
| (2) |  | s←πp​(x,p)s\leftarrow\pi\_{p}(x,p) |  |

In our framework, the Planner produces KK SQL queries: one using greedy
decoding and K−1K-1 using multinomial decoding with a temperature 𝒯\mathcal{T}:

|  |  |  |  |
| --- | --- | --- | --- |
| (3) |  | S={s1,s2,…,sK}←πp​(x,p,𝒯).S=\{s\_{1},s\_{2},\dots,s\_{K}\}\leftarrow\pi\_{p}(x,p,\mathcal{T}). |  |

![Refer to caption](planner_color.png)


Figure 3. Example thought process of the Planner.

### 3.3. Validator Agent

The Validator Agent re-evaluates the generated SQL query based on the
response received from the database to identify errors. As such, the
Validator not only verifies the Planner’s reasoning but also detects issues
that require modifications, e.g., related to syntax errors in the query or
queries that yield empty responses.

While the Validator is similar to the Planner in terms of the goal to
validate selection goals, to determine the relevant tables, and to analyze
the conditions of a selection, this redundancy is crucial, as LLMs often
fail on the first attempt on a task (Madaan et al., [2024](https://arxiv.org/html/2512.18622v1#bib.bib27)). The Validator
uses the responses from query evaluation to detect discrepancies, to refine
the SQL queries, and to provide targeted feedback when queries fail.
Specifically, we employ two specialized validator agents.

Validator Selection.
The validator assesses that the generated SQL query accurately selects the
correct columns based on the intent of the question. LLM-generated SQL
queries often contain mistakes, such as the
selection of incorrect or unnecessary columns, the omission of necessary
ones, or the arrangement of columns in the wrong order.

We overcome these issues based on a dedicated thought process for the
validator for the selection, as it is illustrated in
[Fig. 4](https://arxiv.org/html/2512.18622v1#S3.F4 "Figure 4 ‣ 3.3. Validator Agent ‣ 3. The MATS Framework ‣ A Multi-agent Text2SQL Framework using Small Language Models and Execution Feedback"). First, the validator checks the selected
columns of the input SQL query. Next, it performs phrase extraction on the
input question and maps it to the intended columns that need to be selected.
Finally, the validator compares the selected columns with the intended ones
and flags potential issues.

This validator considers only on queries that do not include certain
operations such as min, max, count, avg,
sum, divide, or case when. The reason for this
restriction is that multiple queries selecting different columns may still
produce the same correct result, which could otherwise lead to misjudgment
by the validator. At the end of the validation process, the validator
determines whether the SQL query is correct or not.

Validator Condition.
This validator aims at identifying mistakes related to logical conditions in
SQL queries. In an SQL query, conditions can be used in the WHERE
clause or the SELECT clause (e.g., queries using CASE WHEN
or IF statements).

The thought process behind the validation mechanism for conditions is
illustrated in [Fig. 5](https://arxiv.org/html/2512.18622v1#S3.F5 "Figure 5 ‣ 3.3. Validator Agent ‣ 3. The MATS Framework ‣ A Multi-agent Text2SQL Framework using Small Language Models and Execution Feedback"). First,
the validator extracts the condition from the SELECT clause and
interprets its meaning. Then, it analyzes the condition in the
WHERE clause. After interpreting both conditions, the validator
evaluates the execution response. In most cases, if the execution response
contains None or an empty set, it likely indicates an incorrect
condition (e.g., filtering incorrect values or using the wrong column in the
filter). The validator then identifies potential mistakes in the condition
and suggests ways to fix them. For example, it may recommend adding
conditions such as "column A IS NOT NULL" to filter out
None results or correcting mismatched conditions that were
misinterpreted by the LLM. Finally, the validator takes a decision on
whether the SQL query is considered correct or not.

Combined Validator.
Let vs,vcv\_{s},v\_{c} denote the instructions for the validator selection and
the validator condition, respectively. The validator agent, πv\pi\_{v},
processes these instructions along with the input xx, the SQL query ss, and its corresponding execution response e​rer, generating feedback
signals as follows:

|  |  |  |  |
| --- | --- | --- | --- |
| (4) |  | fs=πv​(vs,x,s,e​r)f\_{s}=\pi\_{v}(v\_{s},x,s,er) |  |

|  |  |  |  |
| --- | --- | --- | --- |
| (5) |  | fc=πv​(vc,x,s,e​r)f\_{c}=\pi\_{v}(v\_{c},x,s,er) |  |

Here, fs,fcf\_{s},f\_{c} represent the feedback for the validator selection and
the validator condition, respectively.

![Refer to caption](validator_selection_color.png)


Figure 4. Example feedback of validator selection.

![Refer to caption](validator_condition_color.png)


Figure 5. Example feedback of validator condition.

### 3.4. Fix Agent

The Fix Agent refines SQL queries using the feedback obtained from the
Validator Agent. It processes the feedback to adjust and improve the SQL
query, aiming at ensuring that no further errors occur in the final output.

The Fix Agent takes the initial input xx, the SQL query ss as generated by
the Planner, and a set of feedback signals as input to generate a corrected
SQL query. This process of the Fix Agent πf\pi\_{f} is captured as:

|  |  |  |  |
| --- | --- | --- | --- |
| (6) |  | sf=πf​(x,s,{f∈{fs,fc}∣f​ indicates an error}),s\_{f}=\pi\_{f}\left(x,s,\left\{f\in\{f\_{s},f\_{c}\}\mid f\text{ indicates an error}\right\}\right), |  |

where sfs\_{f} is the corrected SQL query.

### 3.5. Selection Agent

The Selection Agent is an SLM that chooses the best SQL query from multiple
candidates based on the responses obtained when evaluating them over the
database.

The Selection Agent takes a prompt containing a list of SQL queries S={s1,s2,…,sK}S=\{s\_{1},s\_{2},\dots,s\_{K}\} and their execution responses E​R={e​r1,e​r2,…,e​rK}ER=\{er\_{1},er\_{2},\dots,er\_{K}\} as input, and outputs the index of the best query (or
indicates that no query is correct). When K>kK>k, the agent splits SS into smaller subsets (of size up to kk), selects the best query in
each subset, and repeats this process until only one candidate remains.
Formally, the functionality of the Selection Agent πs\pi\_{s} is captured
as:

|  |  |  |  |
| --- | --- | --- | --- |
| (7) |  | s∗=πs​(S,E​R),s^{\*}=\pi\_{s}(S,ER), |  |

where s∗s^{\*} denotes the chosen query (and its index).

### 3.6. Data Generation for Supervised Fine-Tuning

To mitigate limitations in the reasoning with SLMs, we devise an approach to
generate training data for fine-tuning the models. To this end, we manually
label a small set of training examples per task, enabling SLMs to
adopt a structured reasoning process and reduce errors. For
each task, we construct training data based on the Spider and BIRD
datasets, as discussed in detail in our evaluation.
Since these datasets only provide input questions xx and ground-truth SQL
queries s^\hat{s}, we extend them with additional annotations: the planning
process pp for the Planner, validator feedback vs,vcv\_{s},v\_{c} for different
validation types, and corrected SQL queries based on the feedback. The data
creation process follows three structured steps:

1) Manual Labeling: We annotate up to five representative
examples for each task manually. These high-quality examples act as
references to guide each agent in performing small, incremental reasoning
steps, thereby minimizing error propagation.

2) Few-Shot Prompting: Building on the manually labeled
examples, we use few-shot prompting techniques with OpenAI’s GPT-4o-mini to
generate additional training samples for the rest of the dataset. This
approach ensures broader coverage of various scenarios in the dataset.

3) Fine-Tuning on SLMs: We fine-tune SLMs using the
prompt-response pairs generated during the few-shot prompting phase. The
fine-tuning process focuses on optimizing the completion part of the
model’s output. Here, we adopt a supervised fine-tuning loss, which is
computed as:

|  |  |  |  |
| --- | --- | --- | --- |
| (8) |  | ℒcompletion=−∑t=C+1τlog⁡Pθ​(yt∣y<t,χ),\mathcal{L}\_{\text{completion}}=-\sum\_{t=C+1}^{\tau}\log P\_{\theta}(y\_{t}\mid y\_{<t},\chi), |  |

where CC is the token index marking the end of the prompt; τ\tau
represents the total number of tokens in the sequence which includes the
prompt and the completion tokens; yty\_{t} denotes the target token at position
tt within the completion; χ\chi represents the prompt tokens; and
PθP\_{\theta} is the probability distribution over the vocabulary predicted
by the model parameters θ\theta.

## 4. Reinforcement Learning from Execution Feedback

In the light of the limited capabilities of SLMs in terms of reasoning (R3)
and instruction following (R4), we propose an approach for reinforcement
learning from execution feedback (RLEF) to further refine the agents of the
MATS framework ([Fig. 6](https://arxiv.org/html/2512.18622v1#S4.F6 "Figure 6 ‣ 4. Reinforcement Learning from Execution Feedback ‣ A Multi-agent Text2SQL Framework using Small Language Models and Execution Feedback")). RLEF targets cases where agents fail to generate correct SQL
queries, and relies on feedback from the evaluation of the queries to
identify issues and explore effective corrections.
Below, we first introduce
a respective model for the various agents ([§ 4.1](https://arxiv.org/html/2512.18622v1#S4.SS1 "4.1. Modeling ‣ 4. Reinforcement Learning from Execution Feedback ‣ A Multi-agent Text2SQL Framework using Small Language Models and Execution Feedback")),
before we target the identification of actions to train them
([§ 4.2](https://arxiv.org/html/2512.18622v1#S4.SS2 "4.2. Action Sampling ‣ 4. Reinforcement Learning from Execution Feedback ‣ A Multi-agent Text2SQL Framework using Small Language Models and Execution Feedback")). Finally, we elaborate on the actual training
process ([§ 4.3](https://arxiv.org/html/2512.18622v1#S4.SS3 "4.3. Agent Alignment Training ‣ 4. Reinforcement Learning from Execution Feedback ‣ A Multi-agent Text2SQL Framework using Small Language Models and Execution Feedback")).

![Refer to caption](MainFlowRLEF.drawio.png)


Figure 6. Overview of our approach to Reinforcement Learning from
Execution Feedback.

### 4.1. Modeling

Given a user question and a database schema, we aim to generate an SQL query
that best fulfills the intent. We formulate the task as a
goal-augmented Partially Observable Markov Decision Process:

|  |  |  |
| --- | --- | --- |
|  | M=(𝒮,A,T,R,G,O).M=(\mathcal{S},A,T,R,G,O). |  |

The process definition includes the following components:

* •

  𝒮\mathcal{S} is a set of states;
* •

  A⊂VLA\subset V^{L} represents the action space sampled from the
  language model’s vocabulary VV with LL as the maximum length of the
  generated text;
* •

  T:𝒮×A→𝒮T:\mathcal{S}\times A\rightarrow\mathcal{S} is the
  transition function;
* •

  G⊂VNG\subset V^{N} denotes the goal space;
* •

  R:𝒮×A×G→ℝR:\mathcal{S}\times A\times G\rightarrow\mathbb{R}
  represents the goal-conditioned reward function; and
* •

  OO is a set of observations o∈Oo\in O.

Note that the design of the reward function depends on
the specific algorithm used for training. For instance, the
DPO (Rafailov et al., [2023](https://arxiv.org/html/2512.18622v1#bib.bib38)) and ORPO(Hong et al., [2024](https://arxiv.org/html/2512.18622v1#bib.bib13)) algorithms
do not require an explicit reward model, as the reward is inherently derived
from the language model itself (Rafailov et al., [2023](https://arxiv.org/html/2512.18622v1#bib.bib38)). In this study, we
adopt the ORPO algorithm, so that, in the remainder, we use the
terms ‘chosen action’ and ‘rejected action’ to align with the algorithm’s
framework.

We instantiate the process for the different types of agents in the MATS framework, as follows:

For the Planner, the goal, observations, and actions are defined as:

* •

  GG is the set of completions containing correct SQL queries.
* •

  The observation op∈Opo\_{p}\in O\_{p} is the input sample xx.
* •

  The chosen action is a completion with a correct SQL query
  matching the ground-truth execution; the rejected action is a query
  resulting in a syntax error or differing execution.

For the Validator, the instantiation is done as follows:

* •

  GG is the set of completions that enables the Fix Agent to modify
  the SQL query to a correct version.
* •

  The observation ov∈OVo\_{v}\in O\_{V} is the input prompt to the
  validator, consisting of xx, the execution response of xx, and an
  validation instruction vi∈{vs,vc}v\_{i}\in\{v\_{s},v\_{c}\}.
* •

  The chosen action is feedback that correctly identifies issues and
  assists the Fix Agent in modifying the SQL query. The rejected action is
  feedback that is either incorrect or insufficiently useful for the Fix
  Agent.

For the Fix Agent, we obtain the following realization:

* •

  GG is the set of correct SQL queries.
* •

  The observation of∈OFo\_{f}\in O\_{F} consists of the input sample xx, an
  execution response, and a list of feedback signals indicating that the
  SQL is incorrect.
* •

  The chosen action is an SQL query that matches
  the ground-truth result. The rejected action is a query that results in
  a syntax error or deviates from the ground truth.

### 4.2. Action Sampling

The action space per agent is very large, with a size of |V|L|V|^{L},
so that the identification of effective actions to train the agents is
important. However, random sampling or relying solely on the agent’s
exploration of the action space will generally not yield effective actions.
We therefore adopt two strategies for action generation:

* •

  Multinomial Decoding Strategy: We use a temperature parameter
  𝒯\mathcal{T} to introduce controlled randomness during the decoding
  process of the text generated by SLMs. This helps the trained
  agent in exploring more effective actions.
* •

  Advanced Agent Assistance: A larger, well-trained language model generates higher-quality actions for the task.

Moreover, we introduce three assistant agents that leverage OpenAI
GPT-4o-mini during training:

* •

  An Advanced Planner Agent often produces more accurate SQL queries
  compared to the smaller agent used in inference. For this agent, we rely
  on few-shot prompting.
* •

  An Feedback Editor Agent modifies feedback to help the Fix Agent
  to correct SQL queries more effectively.
* •

  An Advanced Fix Agent repairs SQL queries with a higher chance of
  success. It uses a prompt to refine the SQL query based on the provided
  feedback.

For each agent, given an observation oo, we generate a set of actions using
the multinomial decoding strategy and the associated assistant agent
𝒜\mathcal{A}. That is, we generate an action set AP⊂AA\_{P}\subset A of
size KK, where K−1K-1 actions are sampled from the multinomial decoding
strategy with a temperature 𝒯\mathcal{T}, and one action is sampled from
the assistant agent 𝒜\mathcal{A}.
The resulting action set APA\_{P} may contain both, chosen actions
𝒞\mathcal{C} and rejected actions ℛ\mathcal{R}. We then construct pairs
𝒫={(o,c,r)∣c∈𝒞,r∈ℛ}\mathcal{P}=\{(o,c,r)\mid c\in\mathcal{C},r\in\mathcal{R}\}. If APA\_{P} contains only chosen actions (𝒞\mathcal{C}) or
only rejected actions (ℛ\mathcal{R}), the training sample is
ignored.

### 4.3. Agent Alignment Training

Using a set of chosen-rejected pairs from our sampling strategy, we improve
each agent with ORPO (Hong et al., [2024](https://arxiv.org/html/2512.18622v1#bib.bib13)). We choose ORPO for its
streamlined approach, which simplifies training and reduces computational
complexity compared to methods like PPO (Schulman et al., [2017](https://arxiv.org/html/2512.18622v1#bib.bib43)) or DPO
(Schulman et al., [2017](https://arxiv.org/html/2512.18622v1#bib.bib43)). By integrating supervised fine-tuning loss with
an odds ratio-based penalty, ORPO preserves the accuracy gains from
supervised fine-tuning (SFT), while aligning model outputs to preferences.
This effectively avoids catastrophic forgetting as commonly seen, when
reinforcement learning follows SFT.

Algorithm 1  Iterative Training with ORPO for Planner

1:

2:Training dataset 𝒟={(xi,s^i)∣i=1,…,N}\mathcal{D}=\{(x\_{i},\hat{s}\_{i})\mid i=1,\dots,N\}.

3:Initial policy model πP\pi\_{P}.

4:Advanced Planner 𝒜𝒫\mathcal{A\_{P}}, Temperature 𝒯\mathcal{T}, No. iterations TT.

5:Aligned policy for Planner πp,T\pi\_{p,T}.

6:Initialize πp,0←πP\pi\_{p,0}\leftarrow\pi\_{P}

7:for i←1i\leftarrow 1 to TT do

8:  Dp←∅D\_{p}\leftarrow\emptyset

9:  for (x,s^)∈𝒟(x,\hat{s})\in\mathcal{D} do

10:   true\_response←execute​(s^)\textit{true\\_response}\leftarrow\textit{execute}(\hat{s})

11:   A←Sampling​(x,πp,𝒜𝒫,𝒯)A\leftarrow\textit{Sampling}(x,\pi\_{p},\mathcal{A\_{P}},\mathcal{T})

12:   𝒞←∅\mathcal{C}\leftarrow\emptyset, ℛ←∅\mathcal{R}\leftarrow\emptyset ⊳\triangleright Initialize chosen/rejected actions

13:   for a∈Aa\in A do

14:     pred\_response←execute​(a)\textit{pred\\_response}\leftarrow\textit{execute}(a)

15:     if true\_response=pred\_response\textit{true\\_response}=\textit{pred\\_response} then

16:      𝒞←𝒞∪{a}\mathcal{C}\leftarrow\mathcal{C}\cup\{a\}

17:     else

18:      ℛ←ℛ∪{a}\mathcal{R}\leftarrow\mathcal{R}\cup\{a\}

19:   if |𝒞|>0|\mathcal{C}|>0 then

20:     if |ℛ|=0|\mathcal{R}|=0 then

21:      ℛ←{”​”}\mathcal{R}\leftarrow\{""\} ⊳\triangleright Add empty string if ℛ\mathcal{R} is empty

22:     for c∈𝒞c\in\mathcal{C} do

23:      for r∈ℛr\in\mathcal{R} do

24:       Dp←Dp∪{(x,c,r)}D\_{p}\leftarrow D\_{p}\cup\{(x,c,r)\}

25:  Update policy πp\pi\_{p} using ORPO:
πp,i+1←ORPO​(πp,Dp)\pi\_{p,i+1}\leftarrow\text{ORPO}(\pi\_{p},D\_{p})

26:return πp,T+1\pi\_{p,T+1}

The ORPO algorithm introduces a monolithic preference alignment approach
that eliminates the need for both, a reference model and a reward model,
thereby streamlining the preference optimization process. It employs a loss
function that integrates supervised fine-tuning loss with a log-odds ratio
penalty, enabling the model to effectively differentiate between chosen and
rejected actions. By default, ORPO computes SFT loss over the entire prompt
and completion. However, we modify the loss function to apply SFT loss only
to the completion, allowing the model to focus more directly on generating
high-quality outputs rather than learning the structure of the prompt.

The objective function of ORPO is defined as:

|  |  |  |
| --- | --- | --- |
|  | ℒORPO=𝔼(x,yw,yl)​[ℒcompletion+λ⋅ℒOR]\mathcal{L}\_{\text{ORPO}}=\mathbb{E}\_{(x,y^{w},y^{l})}\left[\mathcal{L}\_{\text{completion}}+\lambda\cdot\mathcal{L}\_{\text{OR}}\right] |  |

where:

* •

  ℒcompletion\mathcal{L}\_{\text{completion}} is the standard supervised
  fine-tuning loss that is computed only on the completion part, implemented
  as
  the negative log-likelihood of generating the favored response ywy^{w}:

  |  |  |  |
  | --- | --- | --- |
  |  | ℒcompletion=−1m​∑t=1mlog⁡Pθ​(ytw∣x,y<tw)\mathcal{L}\_{\text{completion}}=-\frac{1}{m}\sum\_{t=1}^{m}\log P\_{\theta}(y\_{t}^{w}\mid x,y\_{<t}^{w}) |  |
* •

  ℒOR\mathcal{L}\_{\text{OR}} is the log odds ratio penalty,
  encouraging
  the model to increase the odds of generating favored responses over
  disfavored ones:

  |  |  |  |
  | --- | --- | --- |
  |  | ℒOR=−log⁡σ​(log⁡oddsθ​(yw∣x)oddsθ​(yl∣x))\mathcal{L}\_{\text{OR}}=-\log\sigma\left(\log\frac{\text{odds}\_{\theta}(y^{w}\mid x)}{\text{odds}\_{\theta}(y^{l}\mid x)}\right) |  |
* •

  oddsθ​(y∣x)\text{odds}\_{\theta}(y\mid x) is the likelihood odds of generating
  the sequence yy, which is computed as:

  |  |  |  |
  | --- | --- | --- |
  |  | oddsθ​(y∣x)=Pθ​(y∣x)1−Pθ​(y∣x)\text{odds}\_{\theta}(y\mid x)=\frac{P\_{\theta}(y\mid x)}{1-P\_{\theta}(y\mid x)} |  |
* •

  λ\lambda is a hyperparameter controlling the weight of the log odds
  ratio penalty.

Using this mechanism, we iteratively enhance each agent starting with a
given policy π\pi. At each training stage, the policy πt\pi\_{t} is
refined, which yields a policy πt+1\pi\_{t+1}. This process continues in a
loop until the
training dataset size stabilizes, which indicates that
further fine-tuning fails
to correct errors. These persistent errors are often
associated with
semantic issues, which are intrinsically linked to the limitations of small
language models.

The detailed training procedure for the Planner Agent is presented in
[Alg. 1](https://arxiv.org/html/2512.18622v1#alg1 "Algorithm 1 ‣ 4.3. Agent Alignment Training ‣ 4. Reinforcement Learning from Execution Feedback ‣ A Multi-agent Text2SQL Framework using Small Language Models and Execution Feedback"). The training process for the Fix Agent is
similar, except that the observation xx includes the generated SQL query
and feedback signals from the Validator Agent.

Algorithm 2  Action Selection Process for Validator Agent

1:

2:Observation oo; Action sets AsA\_{s}, AcA\_{c} sampled with observation oo.

3:Ground-truth SQL s^\hat{s}; Planner SQL response ss.

4:Fix agent πF,t−1\pi\_{F,t-1}.

5:Chosen sets: 𝒞s\mathcal{C}\_{s}, 𝒞c\mathcal{C}\_{c}.
Rejected sets: ℛs\mathcal{R}\_{s}, ℛc\mathcal{R}\_{c}.

6:true\_response←execute​(s^)\textit{true\\_response}\leftarrow\textit{execute}(\hat{s})

7:planner\_response←execute​(s)\textit{planner\\_response}\leftarrow\textit{execute}(s)

8:if planner\_response=true\_response\textit{planner\\_response}=\textit{true\\_response} then

9:  for a∈{As,Ac}a\in\{A\_{s},A\_{c}\} do

10:   if aa indicates the SQL is correct. then

11:     Add aa to the corresponding chosen set 𝒞\mathcal{C}

12:   else

13:     Add aa to the corresponding rejected set ℛ\mathcal{R}

14:for (as,ac)∈(As,Ac)(a\_{s},a\_{c})\in(A\_{s},A\_{c}) do

15:  sf←πF,t−1(o,s,{a∣a∈{as,ac},s\_{f}\leftarrow\pi\_{F,t-1}(o,s,\{a\mid a\in\{a\_{s},a\_{c}\},

16:      a indicates an error})a\text{ indicates an error}\})

17:  pred\_response←execute​(sf)\textit{pred\\_response}\leftarrow\textit{execute}(s\_{f})

18:  if pred\_response=true\_response\textit{pred\\_response}=\textit{true\\_response} then

19:   Add asa\_{s} to 𝒞s\mathcal{C}\_{s}, aca\_{c} to 𝒞c\mathcal{C}\_{c}

20:  else

21:   Add asa\_{s} to ℛs\mathcal{R}\_{s}, aca\_{c} to ℛc\mathcal{R}\_{c}

22:return 𝒞s,𝒞c,ℛs,ℛc\mathcal{C}\_{s},\mathcal{C}\_{c},\;\mathcal{R}\_{s},\mathcal{R}\_{c}

The training process for the Validator Agent differs as it does not generate
SQL queries to compare with the ground-truth query. To determine the chosen
and rejected actions for the Validator Agent πV,t\pi\_{V,t}, we incorporate
the Fix
Agent from the previous aligned step, πF,t−1\pi\_{F,t-1}. If the actions
generated by the Validator Agent help the Fix Agent write a correct SQL
query, the
actions are chosen; otherwise, they are rejected. This process is described
in [Alg. 2](https://arxiv.org/html/2512.18622v1#alg2 "Algorithm 2 ‣ 4.3. Agent Alignment Training ‣ 4. Reinforcement Learning from Execution Feedback ‣ A Multi-agent Text2SQL Framework using Small Language Models and Execution Feedback").

Note that we do not handle cases where
the planner\_response≠true\_response\textit{planner\\_response}\neq\textit{true\\_response}, as
determining the incorrect feedback among the two types is challenging. For
instance, even with an incorrect SQL query, the selection feedback might be
correct, while the error lies solely in the condition feedback.

## 5. Empirical Evaluation

In this section, we conduct experiments with the aim of answering the
following research questions:

* (RQ1)

  Does MATS outperform baseline methods in terms of accuracy and
  efficiency?
* (RQ2)

  How robust is MATS in handling noisy and realistic queries?
* (RQ3)

  Do hyper-parameters strongly affect our model?
* (RQ4)

  How does RLEF improve SQL generation accuracy?
* (RQ5)

  How do different RL algorithms impact accuracy?
* (RQ6)

  Is our thought process for small agents important?
* (RQ7)

  How does MATS perform in different domains?
* (RQ8)

  How do SQL characteristics influence MATS?

### 5.1. Experimental Setup

Database. We rely on two English Text2SQL benchmarks:
Spider (Yu et al., [2018c](https://arxiv.org/html/2512.18622v1#bib.bib53)) and BIRD (Li et al., [2024a](https://arxiv.org/html/2512.18622v1#bib.bib22)).

* •

  Spider is a popular benchmark for NL2SQL translation, consisting
  of 200 databases with multiple tables that cover 138 diverse domains. Spider
  contains 7000 samples in a training set, a development set with 1024
  samples, and a hidden test set.
* •

  Spider Variants: Spider-DK (Gan et al., [2021a](https://arxiv.org/html/2512.18622v1#bib.bib9)),
  Spider-Syn (Gan et al., [2021b](https://arxiv.org/html/2512.18622v1#bib.bib8)), as well as
  Spider-Realistic (Deng et al., [2021](https://arxiv.org/html/2512.18622v1#bib.bib5)) add real-world challenges
  to the original Spider dataset by introducing synonyms, abbreviations, and
  modified column/value names. Dr.Spider (Chang et al., [2023](https://arxiv.org/html/2512.18622v1#bib.bib3)) adds 17
  perturbations across databases, questions, and SQL queries
  (schema/value-synonyms, sort-order, numerical changes), providing a more
  holistic robustness test.
* •

  BIRD contains 95 databases, cumulatively accounting for 33.4GB
  across 37 professional domains. BIRD contains 9428 samples in
  training set, a development set with 1534 samples and a hidden test set.
  BIRD is more challenging, with each of BIRD’s databases containing around
  549K rows on average, compare to Spider’s limited capacity of just 2k
  rows. Also, BIRD offers evidence for a specific sample to facilitate
  the generation of the right SQL query.

Evaluation Metrics. For the Spider benchmark, we measure the
execution accuracy (EX). It evaluates whether the predicted and ground-truth
SQL queries yield the same execution results on the database. However, EX
can occasionally produce false positives, when incorrect SQL queries
accidentally yield the same results as the ground truth. To address this,
the Spider benchmark also utilizes the Test-Suite accuracy
(TS) (Li et al., [2024c](https://arxiv.org/html/2512.18622v1#bib.bib20)). It assesses whether the predicted SQL query passes
execution across multiple database instances generated through automated
augmentations, making it a more reliable metric by reducing false positives.

The BIRD benchmark primarily relies on execution accuracy (EX) as its
evaluation metric. Additionally, BIRD introduces the Valid Efficiency Score
(VES) to evaluate the execution efficiency of correctly generated SQL
queries. Unlike EX, in VES, the score for a correct SQL query is calculated
as the execution time of the ground-truth divided by the execution time
of the predicted SQL. If the predicted SQL is more efficient, its VES score
surpasses EX.

Baselines. We compare our method with the following baselines:

* •

  Open-Source Fine-Tuning Models. T5 (Li et al., [2024a](https://arxiv.org/html/2512.18622v1#bib.bib22)) is a
  fine-tuned baseline for Text2SQL tasks, tested at various scales (Base,
  Large, 3B). CodeS (Li et al., [2024c](https://arxiv.org/html/2512.18622v1#bib.bib20)) is an open-source model (1B–15B
  parameters) incrementally pre-trained on NL2SQL data to specialize in
  Text2SQL. We do not compare with DeepSeek-R1, even though it is
  considered an open-source model and has a large parameter size
  (671B), because its API was temporarily unavailable at the time of our
  research due to excessive traffic.
* •

  Closed-Source API-Based Methods. ChatGPT + CoT (Li et al., [2024a](https://arxiv.org/html/2512.18622v1#bib.bib22))
  enhances SQL generation with chain-of-thought reasoning for improved
  multi-step problem-solving. DIN-SQL (Pourreza and Rafiei, [2023b](https://arxiv.org/html/2512.18622v1#bib.bib35)) adopts a
  decomposed in-context learning approach, breaking queries into subtasks such
  as schema linking, query classification, and self-correction.
  DAIL-SQL (Gao et al., [2023](https://arxiv.org/html/2512.18622v1#bib.bib10)) integrates prompt engineering with systematic
  fine-tuning, optimizing example selection based on question-query similarity
  and a balanced organizational strategy. MAC-SQL (Wang et al., [2023](https://arxiv.org/html/2512.18622v1#bib.bib47)) employs a
  multi-agent framework featuring a Decomposer for sub-question processing.
  Finally, CHESS (Talaei et al., [2024](https://arxiv.org/html/2512.18622v1#bib.bib45)) utilizes a modular pipeline that
  includes entity/context retrieval, schema selection, and SQL generation,
  leveraging LLMs for schema pruning to minimize noise.

Setup.
The Schema Insight Agent uses
RoBERTa-large (Liu, [2019](https://arxiv.org/html/2512.18622v1#bib.bib25)) (355M parameters), while the Planner and
Selection Agents are fine-tuned on LLaMA-3.2 3B. The Validator and Fix
Agents are fine-tuned on LLaMA-3.2 1B, resulting in a total parameter size
of MATS of 9B. All agents, except the Schema Insight Agent, utilize
bfloat16 precision and FlashAttention (Dao et al., [2022](https://arxiv.org/html/2512.18622v1#bib.bib4)).

For inference, all experiments were conducted on a machine equipped with an
A5000 GPU featuring 24GB of memory. The models were deployed using the VLLM
framework (Kwon et al., [2023](https://arxiv.org/html/2512.18622v1#bib.bib16)). For supervised fine-tuning, we set the
learning rate to 2.0×10−52.0\times 10^{-5}, a batch size of 128, and train the
model for 4 epochs. For ORPO training, we set the learning rate to 5×10−65\times 10^{-6}, λ\lambda to 0.5, and a batch size of 64, and the number of epochs
is 1 or within 800 steps. For the Planner agent, we sample K=10K=10
solutions, one by greedy decoding and the others from multinomial sampling
with a temperature 𝒯=1.0\mathcal{T}=1.0.

### 5.2. End-to-end comparison

[Table 1](https://arxiv.org/html/2512.18622v1#S5.T1 "Table 1 ‣ 5.2. End-to-end comparison ‣ 5. Empirical Evaluation ‣ A Multi-agent Text2SQL Framework using Small Language Models and Execution Feedback") and [Table 2](https://arxiv.org/html/2512.18622v1#S5.T2 "Table 2 ‣ 5.2. End-to-end comparison ‣ 5. Empirical Evaluation ‣ A Multi-agent Text2SQL Framework using Small Language Models and Execution Feedback")
present the performance of MATS in comparison to other baselines. In these
tables, CHESSopen-source refers to the CHESS method that uses
Llama-3-70B and Fine-tuned DeepSeek in its workflow.

Accuracy.
MATS shows a strong performance on both, the Spider and BIRD datasets. On
the Spider development set, MATS reaches an EX% of 87.1, outperforming
other methods, including larger models such as CodeS-15B and MAC-SQL +
GPT-4. On the BIRD development dataset, the MATS model achieves an EX% of
64.73 and a VES% of 66.75. This performance is comparable to CHESS, which
incorporates multiple modules leveraging OpenAI’s GPT-4-turbo. Overall, MATS outperforms all open-source models in both EX% and VES%, while being
on-par with closed-source methods that rely heavily on proprietary models,
such as OpenAI GPT.

Time.
We compare inference time only with other open-source fine-tuning methods,
as closed-source approaches host LLMs on unknown physical devices.
We note that the inference time of MATS is slower than that of CodeS-15B due
to (1) structural differences between Llama and CodeS, and (2) the presence
of multiple agents in MATS. Additionally, the inference time of MATS on
Spider and BIRD differs significantly, averaging 13.9 s/sample on Spider
compared to 22.03 s/sample on BIRD. This is because BIRD contains many large
databases, leading to a higher execution times.

Table 1. Evaluation of MATS on BIRD dev.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Methods | #Params | EX% | VES% | Avg. Time |
|  |  |  |  | (s/sample) |
| Closed-source API-based methods | | | | |
| ChatGPT + CoT | - | 36.64 | 42.30 |  |
| DIN-SQL + GPT-4 | - | 50.72 | 58.79 | - |
| DAIL-SQL + GPT-4 | - | 54.76 | 56.08 | - |
| MAC-SQL + GPT-4 | - | 59.59 | 66.39 | - |
| GPT-4o + CoT | - | 54.43 | 58.73 | - |
| CHESS + GPT-4 | - | 65.00 | 66.69 | - |
| Open-source fine-tuning methods | | | | |
| Fine-tuned T5-3B | 3B | 23.34 | 25.57 | - |
| SFT Llama2-7B | 7B | 45.37 | 46.98 | - |
| SFT Llama2-13B | 13B | 53.91 | 58.77 | - |
| CodeS-1B | 1B | 50.46 | 51.07 | 0.69 |
| CodeS-3B | 3B | 55.02 | 56.54 | 1.06 |
| CodeS-7B | 7B | 57.17 | 58.80 | 1.87 |
| CodeS-15B | 15B | 58.47 | 59.87 | 3.52 |
| CHESSopen-source | 33B + 70B | 59.86 | - | - |
| Ours | | | | |
| MATS | 9B | 64.73 | 66.75 | 22.03 |




Table 2. Evaluation of MATS on Spider dev.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Methods | #Params | EX% | TS% | Avg. Time |
|  |  |  |  | (s/sample) |
| Closed-source API-based methods | | | | |
| GPT-4 (few-shot) | - | 76.8 | 67.4 | - |
| C3 + ChatGPT | - | 81.8 | 71.4 | - |
| DIN-SQL + GPT-4 | - | 82.8 | 74.2 | - |
| DAIL-SQL + GPT-4 | - | 83.1 | 76.6 | - |
| MAC-SQL + GPT-4 | - | 86.75 | - | - |
| Open-source fine-tuning methods | | | | |
| T5-3B + PICARD | 3B | 79.3 | 69.4 | - |
| RESDSQL-3B | 3B | 84.1 | 73.5 | - |
| SFT Llama2-7B | 7B | 77.8 | 73.5 | - |
| SFT Llama2-13B | 13B | 81.6 | 76.6 | - |
| CodeS-1B | 1B | 77.9 | 72.2 | 0.45 |
| CodeS-3B | 3B | 83.4 | 78.1 | 0.71 |
| CodeS-7B | 7B | 85.4 | 80.3 | 1.22 |
| CodeS-15B | 15B | 84.9 | 79.4 | 2.38 |
| Ours | | | | |
| MATS | 9B | 87.1 | 82.3 | 13.9 |




Table 3. GPU memory requirement for serving LMs.

| Method | Float precision | GPU mem. (Gb) |
| --- | --- | --- |
| CodeS-1B | float16 | 2.4 |
| CodeS-3B | float16 | 7.2 |
| CodeS-7B | float16 | 16.8 |
| CodeS-15B | float16 | 36 |
| RESDSQL-3B(Li et al., [2024b](https://arxiv.org/html/2512.18622v1#bib.bib18)) | float32 | 24.66 |
| RESDSQL-3B + NatSQL(Li et al., [2024b](https://arxiv.org/html/2512.18622v1#bib.bib18)) | float32 | 21.59 |
| MATS Planner | bfloat16 | 7.6 |
| MATS | bfloat16 | 21.2 |




Table 4. Evaluation MATS on Spider variants.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Model | Spider-Syn | | Spider-Realistic | | Spider-DK |
|  | EX% | TS% | EX% | TS% | EX% |
| T5-3B + PICARD | 69.8 | 61.8 | 71.4 | 61.7 | 62.5 |
| REDSQL-3B(Li et al., [2023c](https://arxiv.org/html/2512.18622v1#bib.bib19)) | 76.9 | 66.8 | 81.9 | 70.1 | 66 |
| ChatGPT | 58.6 | 48.5 | 63.4 | 49.2 | 62.6 |
| SQL-PaLM | 70.9 | 66.4 | 77.4 | 73.2 | 67.5 |
| CodeS-1B | 66.5 | 59.3 | 70.9 | 61.8 | 64.7 |
| CodeS-3B | 75.7 | 69 | 79.9 | 74.4 | 71.8 |
| CodeS-7B | 76.9 | 70 | 82.9 | 77.2 | 72 |
| CodeS-15B | 77 | 69.4 | 83.1 | 75.6 | 70.7 |
| MATS | 78.5 | 72.0 | 84.4 | 78.0 | 74.0 |

Model Complexity.
The autoregressive models are served using VLLM, with memory requirements
determined by model size and floating-point precision, as shown in
[Table 3](https://arxiv.org/html/2512.18622v1#S5.T3 "Table 3 ‣ 5.2. End-to-end comparison ‣ 5. Empirical Evaluation ‣ A Multi-agent Text2SQL Framework using Small Language Models and Execution Feedback"). The MATS Planner requires 7.6 GB of GPU memory,
comparable to CodeS-3B, while the full MATS framework requires 21.2 GB, so
that, unlike CodeS-15B, it can be deployed on a single GPU. While the
MATS framework has higher memory demands than most of the other open-source
methods, it delivers superior execution accuracy and inference efficiency,
as shown in [Table 1](https://arxiv.org/html/2512.18622v1#S5.T1 "Table 1 ‣ 5.2. End-to-end comparison ‣ 5. Empirical Evaluation ‣ A Multi-agent Text2SQL Framework using Small Language Models and Execution Feedback")
and [Table 2](https://arxiv.org/html/2512.18622v1#S5.T2 "Table 2 ‣ 5.2. End-to-end comparison ‣ 5. Empirical Evaluation ‣ A Multi-agent Text2SQL Framework using Small Language Models and Execution Feedback").

Table 5. Evaluation of MATS on Dr.Spider.

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Type | Perturbation | #Sam. | REDSQL-3B | ChatGPT | CodeS-7B | CodeS-15B | MATS |
|  |  |  | (Li et al., [2023c](https://arxiv.org/html/2512.18622v1#bib.bib19)) | +ZeroNL2SQL(Gu et al., [2023](https://arxiv.org/html/2512.18622v1#bib.bib11)) |  |  |  |
| DB | schema-synonym | 2619 | 68.3 | 69.8 | 67.2 | 66.9 | 73.0 |
| schema-abbreviation | 2853 | 70.0 | 74.8 | 76.8 | 78.7 | 79.2 |
| DBcontent-equivalence | 382 | 40.1 | 56.8 | 46.9 | 47.6 | 52.1 |
| Average | - | 59.4 | 67.1 | 63.6 | 64.4 | 74.7 |
| NLQ | keyword-synonym | 953 | 72.4 | 74.0 | 73.0 | 73.5 | 73.1 |
| keyword-carrier | 399 | 83.5 | 88.2 | 91.5 | 91.7 | 89.5 |
| column-synonym | 563 | 63.1 | 62.7 | 63.2 | 64.7 | 63.8 |
| column-carrier | 579 | 63.9 | 71.7 | 80.7 | 79.1 | 75.3 |
| column-attribute | 119 | 71.4 | 70.6 | 63.0 | 68.9 | 72.3 |
| column-value | 304 | 76.6 | 76.0 | 73.7 | 76.3 | 74.0 |
| value-synonym | 506 | 53.2 | 70.6 | 72.7 | 71.9 | 71.3 |
| multitype | 1351 | 60.7 | 66.4 | 69.5 | 69.4 | 68.1 |
|  | others | 2819 | 79.0 | 79.4 | 81.5 | 81.2 | 81.2 |
|  | Average | - | 69.3 | 73.2 | 74.3 | 76.3 | 75.5 |
| SQL | comparison | 178 | 82.0 | 73.6 | 77.5 | 71.9 | 77.5 |
| sort-order | 192 | 85.4 | 80.2 | 81.8 | 84.9 | 81.2 |
| nonDB-number | 131 | 85.5 | 92.4 | 90.1 | 84.0 | 90.8 |
| DB-text | 911 | 74.3 | 80.7 | 80.5 | 80.7 | 79.3 |
| DB-number | 410 | 88.8 | 86.1 | 84.9 | 85.9 | 91.2 |
|  | Average | - | 83.2 | 82.6 | 83.0 | 81.5 | 87.0 |
| All | Global average | - | 71.7 | 74.9 | 75.0 | 75.1 | 76.0 |

### 5.3. Evaluation on Robustness Benchmarks

In this experiment, we evaluate the execution accuracy of MATS on noisy and
more realistic questions using Spider variants and the Dr.Spider datasets.
[Table 4](https://arxiv.org/html/2512.18622v1#S5.T4 "Table 4 ‣ 5.2. End-to-end comparison ‣ 5. Empirical Evaluation ‣ A Multi-agent Text2SQL Framework using Small Language Models and Execution Feedback") showcases the performance of MATS on
Spider-Syn, Spider-Realistic, and Spider-DK, highlighting its capability to
handle diverse and challenging query variations.

To further assess MATS’s
robustness, we evaluate it on Dr.Spider. Recall that this benchmark
comprising 17 types of perturbations across questions,
database schemas, and SQL queries, including schema-synonym replacements,
value synonyms, and abbreviation updates.
However, our model is trained exclusively on the original Spider dataset,
i.e., without any question or database augmentation.

[Table 5](https://arxiv.org/html/2512.18622v1#S5.T5 "Table 5 ‣ 5.2. End-to-end comparison ‣ 5. Empirical Evaluation ‣ A Multi-agent Text2SQL Framework using Small Language Models and Execution Feedback") compares the execution accuracy of MATS with other
baseline approaches. MATS outperforms all baselines on DB and SQL
perturbations. However, on NLQ perturbations, MATS achieves a slightly lower
accuracy (75.5%) compared to CodeS-15B (76.3%). This highlights the
limitations of SLMs in understanding natural language, particularly when
handling synonyms and linguistic variations. Overall, MATS proves robust and
adaptable to noisy, realistic queries, making it effective for real-world
Text2SQL tasks.

### 5.4. Hyperparameter Sensitivity

Number of candidates.
As the Planner produces multiple responses, increasing the number of
candidates may improve the chances of finding the correct SQL query. We explore the selection effectiveness as follows. We evaluate the
upper bound by measuring recall when generating KK SQL queries and assessing the Selection Agent’s accuracy in identifying
the correct one.

[7(a)](https://arxiv.org/html/2512.18622v1#S5.F7.sf1 "7(a) ‣ Figure 7 ‣ 5.4. Hyperparameter Sensitivity ‣ 5. Empirical Evaluation ‣ A Multi-agent Text2SQL Framework using Small Language Models and Execution Feedback") presents the execution
accuracy of MATS on the BIRD development dataset as the number of candidates
increases. The upper bound represents the recall, indicating the maximum
possible accuracy if the correct query is always included in the candidate
set. Specifically, if at least one of the KK generated candidates
contains the correct SQL query, the sample is considered correct. As
expected, increasing KK improves recall, leading to a higher upper
bound. However, the accuracy of MATS does not consistently follow the same
trend. While recall reaches 77.8% at K=30K=30, MATS achieves only
62.78%, highlighting a gap between potential and actual execution
accuracy. The reason is likely that more incorrect SQL queries are
generated, increasing the
likelihood that the Selection Agent chooses an incorrect query.

![Refer to caption](selection_effect.png)


(a) MATS EX% on BIRD Dev with increasing number of candidates.

![Refer to caption](lambda_sensitivity.png)


(b) EX% on BIRD Dev after finetuning the Planner with RLEF
Iteration 1 while varying λ\lambda.

![Refer to caption](temperature_sensitivity.png)


(c) EX% on BIRD Dev with different temperatures for candidate
generation.

Figure 7. Comparison of different factors affecting EX% on BIRD Dev.

λ\lambda to balance the SFT loss and the log odds ratio penalty.
[7(b)](https://arxiv.org/html/2512.18622v1#S5.F7.sf2 "7(b) ‣ Figure 7 ‣ 5.4. Hyperparameter Sensitivity ‣ 5. Empirical Evaluation ‣ A Multi-agent Text2SQL Framework using Small Language Models and Execution Feedback") presents the impact of varying λ\lambda on
EX% and the number of syntax errors after finetuning the Planner with RLEF
Iteration 1. In this figure, λ=0\lambda=0 means there is no log odds ratio
penalty and only SFT is applied. Introducing λ>0\lambda>0 with the log odds
ratio greatly improves accuracy, reaching a peak at λ=0.25\lambda=0.25.
Meanwhile, the number of syntax errors decreases significantly for λ>0.2\lambda>0.2. However, our results also highlight that the choice of λ\lambda
needs to be made carefully to
balance accuracy and syntactical correctness.

Temperature for candidate generation.
[7(c)](https://arxiv.org/html/2512.18622v1#S5.F7.sf3 "7(c) ‣ Figure 7 ‣ 5.4. Hyperparameter Sensitivity ‣ 5. Empirical Evaluation ‣ A Multi-agent Text2SQL Framework using Small Language Models and Execution Feedback") reports the mean and standard
deviation (std) of EX% across different temperature settings during
candidate generation. Lower temperatures exhibit lower std, indicating more
stable outputs. However, they also make it harder to find a correct
solution, as the generated candidates are less diverse. In contrast, higher
temperatures increase exploration, making it easier to generate correct
solutions among the candidates, though at the cost of greater variability.
Note that even with temperature 0.0, the results remain slightly
non-deterministic due to underlying sampling mechanisms.

### 5.5. Improvement after each RLEF Iteration

[Fig. 8](https://arxiv.org/html/2512.18622v1#S5.F8 "Figure 8 ‣ 5.5. Improvement after each RLEF Iteration ‣ 5. Empirical Evaluation ‣ A Multi-agent Text2SQL Framework using Small Language Models and Execution Feedback") illustrates the impact of each RLEF iteration on the execution accuracy of both the Planner Agent and the entire framework. For the Planner Agent, we report accuracy using greedy decoding. The results demonstrate that RLEF significantly enhances the ability to generate correct SQL queries. On the BIRD dev dataset, RLEF improves the Planner Agent’s EX% from 53.65 to 59.32, while on the Spider dev dataset, it increases from 83.3 to 85.4. The entire framework, MATS, also benefits from RLEF, exhibiting notable improvements across iterations. On Spider dev, MATS progresses from an initial EX% of 85.5 to 87.1, while on BIRD dev, it improves from 59.06 to a peak of 64.73 before slightly stabilizing. These findings confirm that execution feedback is both helpful and essential for improving the execution accuracy of small language models.

![Refer to caption](rlef_improvement.png)


Figure 8. Execution accuracy of MATS Planner with greedy decoding per
iteration of RLEF on BIRD Dev and Spider Dev.

### 5.6. Comparison of Alignment Algorithms

We evaluate the effectiveness of different algorithms including
PPO, DPO, and ORPO in aligning the Planner policy. Here,
ORPOoriginal is the original version of ORPO, and ORPOours is our
modified version of ORPO with the loss computing on the completion part only
(see [§ 4](https://arxiv.org/html/2512.18622v1#S4 "4. Reinforcement Learning from Execution Feedback ‣ A Multi-agent Text2SQL Framework using Small Language Models and Execution Feedback")). For PPO, we use binary rewards, assigning 1 for
correct execution and 0 otherwise. For DPO, we set β=0.1\beta=0.1 with a
learning rate of 5×10−65\times 10^{-6}. All models are trained for one epoch.

As shown in [Table 6](https://arxiv.org/html/2512.18622v1#S5.T6 "Table 6 ‣ 5.6. Comparison of Alignment Algorithms ‣ 5. Empirical Evaluation ‣ A Multi-agent Text2SQL Framework using Small Language Models and Execution Feedback"), our modified ORPO achieves
the highest execution accuracy (56.32%), outperforming PPO and DPO.
Additionally, our modification for ORPO shows that ORPOours consumes
less GPU Memory, while achieving better execution accuracy. PPO provides a
slight improvement over the SFT baseline,
increasing accuracy from 53.65% to 54.95%, but incurs a significantly high
training time (12.2 hours per epoch). DPO, in contrast, suffers from
catastrophic forgetting, causing accuracy to drop to 44.98%. Even if this
issue is mitigated, its GPU memory consumption (67 GB) and training time
(1.8 hours) remain higher than ORPO.

Notably, ORPO eliminates the reference
model, reducing GPU memory usage by nearly half. This enables larger batch
sizes, resulting in faster training (1.5 hours per epoch) while maintaining
compatibility with limited GPU resources, making it a more practical choice
in constrained environments.

Table 6. EX of different alignment training approaches on the MATS planner
model after Iteration 1

|  |  |  |  |
| --- | --- | --- | --- |
| Model | EX% | GPU Memory | Training Time |
|  |  | (Gb) | (h/epoch) |
| MATS Planner (SFT only) | 53.65 | - | - |
| + PPO | 54.95 | 46 | 12.2 |
| + DPO | 44.98 | 67 | 1.8 |
| + ORPOoriginal | 55.02 | 56 | 1.6 |
| + ORPOours | 56.32 | 52 | 1.5 |

### 5.7. Planner Prompt Comparison

In this experiment, we compare different prompting strategies for supervised
fine-tuning the Planner. The input for supervised fine-tuning includes both
the prompt and its corresponding completion. We construct three supervised
fine-tuning datasets with distinct prompting strategies: (1) No Thought,
where the ground-truth SQL queries from the BIRD Train dataset are directly
used as completions; (2) Chain-of-Thoughts, where SQL queries are generated
using CoT prompting on GPT-4o-mini and used for fine-tuning; and (3)
Few-shot Thoughts, where our proposed data generation mechanism, as
described in [§ 3.6](https://arxiv.org/html/2512.18622v1#S3.SS6 "3.6. Data Generation for Supervised Fine-Tuning ‣ 3. The MATS Framework ‣ A Multi-agent Text2SQL Framework using Small Language Models and Execution Feedback"), is used.

![Refer to caption](planner_prompt_comparison.png)


Figure 9. Planner prompt comparison on BIRD Dev.

The results in [Fig. 9](https://arxiv.org/html/2512.18622v1#S5.F9 "Figure 9 ‣ 5.7. Planner Prompt Comparison ‣ 5. Empirical Evaluation ‣ A Multi-agent Text2SQL Framework using Small Language Models and Execution Feedback") show that Few-shot
Thoughts (3) consistently outperforms CoT and No Thought. In simple queries,
adding thought-based prompting provides only a slight improvement, with
execution accuracy increasing from 59.46% (1) to 60.11% (2) and 63.03%
(3). However, for more complex queries, the impact is more significant. In
moderate queries, Few-shot Thoughts achieves 43.75%, improving by 6.25%
over No Thought. In challenging queries, Few-shot Thoughts (3) reaches
38.62%, compared to 37.93% of CoT and 30.34% of No Thought, highlighting
the importance of well-structured thought processes for SQL generation.

### 5.8. Database Domain Adaption

As shown in [Fig. 10](https://arxiv.org/html/2512.18622v1#S5.F10 "Figure 10 ‣ 5.8. Database Domain Adaption ‣ 5. Empirical Evaluation ‣ A Multi-agent Text2SQL Framework using Small Language Models and Execution Feedback"), our method MATS, achieves the
best overall EX% across database domains in the Spider benchmark. While
MATS performs better than existing baselines such as DAILSQL(SC) and
REDSQL-3B + NatSQL in domains like Competition and Social,
its performance is slightly lower in certain domains such as
Geography. This may be due to larger models using in DAIL-SQL and
CodeS-7B, Codes-15B having better background knowledge in Geography. Despite
these variations, MATS demonstrates strong generalization across different
domains.

![Refer to caption](domain_knowledge.png)


Figure 10. EX% comparison on different domains on Spider.

![Refer to caption](SQL_characteristic_spider.png)


Figure 11. EX% comparison on different SQL characteristics on Spider.

![Refer to caption](SQL_characteristics_BIRD.png)


Figure 12. EX% comparison on different SQL characteristics on BIRD.

### 5.9. Evaluating on SQL Characteristics

[Fig. 11](https://arxiv.org/html/2512.18622v1#S5.F11 "Figure 11 ‣ 5.8. Database Domain Adaption ‣ 5. Empirical Evaluation ‣ A Multi-agent Text2SQL Framework using Small Language Models and Execution Feedback")
and [Fig. 12](https://arxiv.org/html/2512.18622v1#S5.F12 "Figure 12 ‣ 5.8. Database Domain Adaption ‣ 5. Empirical Evaluation ‣ A Multi-agent Text2SQL Framework using Small Language Models and Execution Feedback") compare EX% across SQL
characteristics on the Spider and BIRD datasets. MATS (Ours) consistently
surpasses baselines like DAILSQL(SC), CodeS-15B, and REDSQL-3B, especially
on simpler queries without JOINs, ORDER-BY, or logical connectors. However,
subqueries remain a major challenge for all methods, with EX% dropping
10-30% compared to non-nested queries. While MATS outperforms other
approaches in this aspect, it still experiences a noticeable decline,
indicating the inherent difficulty of handling complex SQL structures.

## 6. Related Work

While we already discussed existing methods for Text2SQL, we here focus on
work that is related to the underlying techniques of MATS, i.e., for
reinforcement learning, preference alignment, and the agent collaboration.

Reinforcement Learning with Human Feedback.
Reinforcement Learning with Human Feedback (RLHF) is a widely used approach for aligning language models with human preferences by integrating human evaluations directly into the training process. In RLHF, a reward model is trained on human-labeled data to score outputs based on their alignment with user intent. This reward signal is then used by reinforcement learning algorithms, such as Proximal Policy Optimization (PPO) (Schulman et al., [2017](https://arxiv.org/html/2512.18622v1#bib.bib43)), to optimize the model’s behavior. RLHF has been instrumental in enabling language models to generate responses that are more aligned with human expectations and preferences. For example, this methodology has been successfully applied to instruction-following models like InstructGPT, significantly improving their capability to adhere to user guidelines while performing a broad spectrum of tasks (Ouyang et al., [2022](https://arxiv.org/html/2512.18622v1#bib.bib30)). This technique bridges the gap between general-purpose pretraining and task-specific utility, solidifying RLHF’s role as a pivotal tool in modern AI systems.

Inspired by this paradigm, we propose a new reinforcement learning mechanism using execution feedback (RLEF) to further refine the MATS agents. By using the responses of query execution, we save human efforts in providing labels like RLHF.

Alignment without Reward Models.
To overcome the complexities and instability associated with Reinforcement
Learning with Human Feedback (RLHF), particularly the challenges posed by
Proximal Policy Optimization (PPO) (Schulman et al., [2017](https://arxiv.org/html/2512.18622v1#bib.bib43)), alternative
alignment methods have been proposed.
Direct Policy Optimization (DPO) simplifies the alignment process by
integrating reward modelling directly into the preference learning stage,
eliminating the need for multi-stage training (Rafailov et al., [2023](https://arxiv.org/html/2512.18622v1#bib.bib38)).
ORPO (Hong et al., [2024](https://arxiv.org/html/2512.18622v1#bib.bib13)) builds on DPO by integrating an odds
ratio-based penalty into supervised fine-tuning. ORPO combines SFT loss with
a relative ratio loss, streamlining training by removing the need for
separate reward models or alignment stages, thus enhancing efficiency and
scalability.

In this paper, we propose a new application of ORPO in Text2SQL tasks by imposing the loss on the completion part only. This makes the framework still light-weight while improving the accuracy of agents and simplifying the training process without requiring a separate reward model.

Multi-Agent Systems.
Recent advancements in multi-agent systems have demonstrated their
effectiveness in solving complex tasks by breaking them down into smaller,
specialized subtasks, each handled by an individual agent (Wei et al., [2025](https://arxiv.org/html/2512.18622v1#bib.bib49); Peng et al., [2025](https://arxiv.org/html/2512.18622v1#bib.bib33)). These systems
leverage the capabilities of Large Language Models to enable efficient
collaboration and communication among agents, leading to improved task
accuracy and efficiency.
Multi-agent frameworks have been successfully
applied across various domains, such as software engineering, where tools
like ChatDev (Qian et al., [2024](https://arxiv.org/html/2512.18622v1#bib.bib36)) facilitate collaborative coding and
debugging, and societal simulations, where MAS models human interactions to
evaluate policy outcomes (Park et al., [2023](https://arxiv.org/html/2512.18622v1#bib.bib32)). Moreover, multi-agent
systems have
also been applied in recommendation systems, where agents work
collaboratively to
process user preferences, filter content, and generate personalized
recommendations through effective coordination and task
allocation (Zhang et al., [2024](https://arxiv.org/html/2512.18622v1#bib.bib54)).

Inspired by these advancements, our framework adopts a multi-agent approach
for Text2SQL tasks, assigning dedicated agents for schema filtering, query
generation, validation, and error correction. This collaborative structure
significantly enhances SQL generation accuracy, especially for small
language models, while improving scalability through reinforcement learning
techniques.

## 7. Conclusion

In this work, we introduced MATS, a novel multi-agent framework designed for
Text2SQL tasks. The framework is optimized for small language models. Unlike
traditional LLM-based approaches, MATS efficiently decomposes SQL generation
into specialized agent roles, allowing for effective execution in
resource-constrained environments. That is, agents filter irrelevant schema
elements and retrieve relevant column values; they generate multiple SQL
queries; they evaluate their outputs using database
responses; they refines SQL queries; and they eventually select the best SQL
query from a set of candidates.
Moreover, to further enhance performance, we proposed Reinforcement Learning
with
Execution Feedback, which improves SQL generation by leveraging
execution results as feedback to guide agent alignment.
Through extensive
evaluations on the BIRD and Spider datasets, we demonstrated that MATS achieves execution accuracy comparable to larger, closed-source LLMs while
being deployable on a single 24GB GPU. Our results indicate that MATS outperforms other open-source models in execution accuracy and robustness,
narrowing the gap between closed-sourced solutions that employ proprietary,
external models.

Despite these advancements, challenges remain in further improving
accuracy. Future work shall explore enhancing agent collaboration and
refining selection strategies to maximize execution accuracy. We can also improve the response of the database system itself to increase the quality of execution feedback, help the agents to learn faster and better. Additionally,
we will integrate broader domain-specific knowledge to further improve SQL
generation for real-world applications.

## References

* (1)
* Askari et al. (2023)

  Arian Askari, Amin
  Abolghasemi, Gabriella Pasi, Wessel
  Kraaij, and Suzan Verberne.
  2023.
  Injecting the BM25 score as text improves
  BERT-based re-rankers. In *ECIR*.
  66–83.
* Chang et al. (2023)

  Shuaichen Chang, Jun
  Wang, Mingwen Dong, Lin Pan,
  Henghui Zhu, et al.
  2023.
  Dr.Spider: A Diagnostic Evaluation Benchmark
  towards Text-to-SQL Robustness. In *ICLR*.
* Dao et al. (2022)

  Tri Dao, Dan Fu,
  Stefano Ermon, Atri Rudra, and
  Christopher Ré. 2022.
  Flashattention: Fast and memory-efficient exact
  attention with io-awareness.
  *NeurIPS* 35
  (2022), 16344–16359.
* Deng et al. (2021)

  Xiang Deng, Ahmed Hassan
  Awadallah, Christopher Meek, Oleksandr
  Polozov, Huan Sun, and Matthew
  Richardson. 2021.
  Structure-Grounded Pretraining for Text-to-SQL.
  In *NAACL-HLT*. 1337–1350.
* Dong et al. (2024)

  Guanting Dong, Hongyi
  Yuan, Keming Lu, Chengpeng Li,
  Mingfeng Xue, Dayiheng Liu,
  Wei Wang, Zheng Yuan,
  Chang Zhou, and Jingren Zhou.
  2024.
  How Abilities in Large Language Models are Affected
  by Supervised Fine-tuning Data Composition. In
  *ACL*. 177–198.
* Dong et al. (2023)

  Xuemei Dong, Chao Zhang,
  Yuhang Ge, Yuren Mao,
  Yunjun Gao, Jinshu Lin,
  Dongfang Lou, et al.
  2023.
  C3: Zero-shot text-to-sql with chatgpt.
  *arXiv preprint arXiv:2307.07306*
  (2023).
* Gan et al. (2021b)

  Yujian Gan, Xinyun Chen,
  Qiuping Huang, Matthew Purver,
  John R Woodward, Jinxia Xie, and
  Pengsheng Huang. 2021b.
  Towards robustness of text-to-SQL models against
  synonym substitution.
  *arXiv preprint arXiv:2106.01065*
  (2021).
* Gan et al. (2021a)

  Yujian Gan, Xinyun Chen,
  and Matthew Purver. 2021a.
  Exploring Underexplored Limitations of Cross-Domain
  Text-to-SQL Generalization. In *EMNLP*.
  8926–8931.
* Gao et al. (2023)

  Dawei Gao, Haibin Wang,
  Yaliang Li, Xiuyu Sun,
  Yichen Qian, Bolin Ding, and
  Jingren Zhou. 2023.
  Text-to-sql empowered by large language models: A
  benchmark evaluation.
  *arXiv preprint arXiv:2308.15363*
  (2023).
* Gu et al. (2023)

  Zihui Gu, Ju Fan,
  Nan Tang, Songyue Zhang,
  Yuxin Zhang, Zui Chen,
  Lei Cao, Guoliang Li,
  Sam Madden, and Xiaoyong Du.
  2023.
  Interleaving pre-trained language models and large
  language models for zero-shot nl2sql generation.
  *arXiv preprint arXiv:2306.08891*
  (2023).
* Guo et al. (2024)

  Taicheng Guo, Xiuying
  Chen, Yaqi Wang, Ruidi Chang,
  Shichao Pei, Nitesh V. Chawla,
  Olaf Wiest, and Xiangliang Zhang.
  2024.
  Large Language Model Based Multi-agents: A Survey
  of Progress and Challenges. In *IJCAI*.
  8048–8057.
* Hong et al. (2024)

  Jiwoo Hong, Noah Lee,
  and James Thorne. 2024.
  ORPO: Monolithic Preference Optimization without
  Reference Model. In *EMNLP*.
  11170–11189.
* Islam et al. (2024)

  Md. Ashraful Islam,
  Mohammed Eunus Ali, and Md Rizwan
  Parvez. 2024.
  MapCoder: Multi-Agent Code Generation for
  Competitive Problem Solving. In *ACL*.
  4912–4944.
* Kumar et al. (2022)

  Ananya Kumar, Aditi
  Raghunathan, Robbie Matthew Jones, Tengyu
  Ma, and Percy Liang. 2022.
  Fine-Tuning can Distort Pretrained Features and
  Underperform Out-of-Distribution. In *ICLR*.
* Kwon et al. (2023)

  Woosuk Kwon, Zhuohan Li,
  Siyuan Zhuang, Ying Sheng,
  Lianmin Zheng, Cody Hao Yu,
  Joseph E. Gonzalez, Hao Zhang, and
  Ion Stoica. 2023.
  Efficient Memory Management for Large Language
  Model Serving with PagedAttention. In *SIGOPS*.
* Lan et al. (2023)

  Wuwei Lan, Zhiguo Wang,
  Anuj Chauhan, Henghui Zhu,
  Alexander Li, Jiang Guo,
  Sheng Zhang, Chung-Wei Hang,
  Joseph Lilien, Yiqun Hu, et al.
  2023.
  Unite: A unified benchmark for text-to-sql
  evaluation.
  *arXiv preprint arXiv:2305.16265*
  (2023).
* Li et al. (2024b)

  Boyan Li, Yuyu Luo,
  Chengliang Chai, Guoliang Li, and
  Nan Tang. 2024b.
  The Dawn of Natural Language to SQL: Are We Fully
  Ready?
  *PVLDB* 17,
  11 (2024), 3318–3331.
* Li et al. (2023c)

  Haoyang Li, Jing Zhang,
  Cuiping Li, and Hong Chen.
  2023c.
  Resdsql: Decoupling schema linking and skeleton
  parsing for text-to-sql. In *AAAI*,
  Vol. 37. 13067–13075.
* Li et al. (2024c)

  Haoyang Li, Jing Zhang,
  Hanbing Liu, Ju Fan,
  Xiaokang Zhang, Jun Zhu,
  Renjie Wei, Hongyan Pan,
  Cuiping Li, and Hong Chen.
  2024c.
  Codes: Towards building open-source language models
  for text-to-sql.
  *SIGMOD* 2,
  3 (2024), 1–28.
* Li et al. (2023b)

  Jinyang Li, Binyuan Hui,
  Ge Qu, Jiaxi Yang,
  Binhua Li, Bowen Li,
  Bailin Wang, Bowen Qin,
  Ruiying Geng, Nan Huo, et al.
  2023b.
  Can llm already serve as a database interface? a
  big bench for large-scale database grounded text-to-sqls.
  *NeurIPS* 36
  (2023), 42330–42357.
* Li et al. (2024a)

  Jinyang Li, Binyuan Hui,
  Ge Qu, Jiaxi Yang,
  Binhua Li, Bowen Li,
  Bailin Wang, Bowen Qin,
  Ruiying Geng, Nan Huo, et al.
  2024a.
  Can llm already serve as a database interface? a
  big bench for large-scale database grounded text-to-sqls.
  *NeurIPS* 36
  (2024).
* Li et al. (2023a)

  Raymond Li, Loubna Ben
  Allal, Yangtian Zi, Niklas Muennighoff,
  et al. 2023a.
  Starcoder: may the source be with you!
  *arXiv preprint arXiv:2305.06161*
  (2023).
* Liu et al. (2023)

  Aiwei Liu, Xuming Hu,
  Lijie Wen, and Philip S Yu.
  2023.
  A comprehensive evaluation of ChatGPT’s zero-shot
  Text-to-SQL capability.
  *arXiv preprint arXiv:2303.13547*
  (2023).
* Liu (2019)

  Yinhan Liu.
  2019.
  Roberta: A robustly optimized bert pretraining
  approach.
  *arXiv preprint arXiv:1907.11692*
  364 (2019).
* Lu et al. (2024)

  Zhenyan Lu, Xiang Li,
  Dongqi Cai, Rongjie Yi,
  Fangming Liu, Xiwen Zhang,
  Nicholas D Lane, and Mengwei Xu.
  2024.
  Small language models: Survey, measurements, and
  insights.
  *arXiv preprint arXiv:2409.15790*
  (2024).
* Madaan et al. (2024)

  Aman Madaan, Niket
  Tandon, Prakhar Gupta, Skyler Hallinan,
  Luyu Gao, Sarah Wiegreffe,
  Uri Alon, Nouha Dziri,
  Shrimai Prabhumoye, Yiming Yang,
  et al. 2024.
  Self-refine: Iterative refinement with
  self-feedback.
  *NeurIPS* 36
  (2024).
* Murthy et al. (2024)

  Rudra Murthy, Prince
  Kumar, Praveen Venkateswaran, and
  Danish Contractor. 2024.
  Evaluating the Instruction-following Abilities of
  Language Models using Knowledge Tasks.
  *arXiv preprint arXiv:2410.12972*
  (2024).
* Naveed et al. (2025)

  Humza Naveed, Asad Ullah
  Khan, Shi Qiu, Muhammad Saqib,
  Saeed Anwar, Muhammad Usman,
  Naveed Akhtar, Nick Barnes, and
  Ajmal Mian. 2025.
  A comprehensive overview of large language models.
  *ACM Transactions on Intelligent Systems and
  Technology* 16, 5
  (2025), 1–72.
* Ouyang et al. (2022)

  Long Ouyang, Jeffrey Wu,
  Xu Jiang, Diogo Almeida,
  Carroll Wainwright, et al.
  2022.
  Training language models to follow instructions
  with human feedback.
  *NeurIPS* 35
  (2022), 27730–27744.
* Papicchio et al. (2025)

  Simone Papicchio, Paolo
  Papotti, and Luca Cagliero.
  2025.
  Qatch: Automatic evaluation of sql-centric tasks on
  proprietary data.
  *ACM Transactions on Intelligent Systems and
  Technology* 16, 2
  (2025), 1–26.
* Park et al. (2023)

  Joon Sung Park, Joseph
  O’Brien, Carrie Jun Cai, Meredith Ringel
  Morris, Percy Liang, and Michael S
  Bernstein. 2023.
  Generative agents: Interactive simulacra of human
  behavior. In *UIST*. 1–22.
* Peng et al. (2025)

  Kexing Peng, Shihao Zhu,
  and Tinghuai Ma. 2025.
  STPE-MARL: Spatio-Temporal Multi-Agent Population
  Evolution Reinforcement Learning.
  *ACM Transactions on Intelligent Systems and
  Technology* (2025).
* Pourreza and Rafiei (2023a)

  Mohammadreza Pourreza and
  Davood Rafiei. 2023a.
  DIN-SQL: Decomposed In-Context Learning of
  Text-to-SQL with Self-Correction.
  arXiv:2304.11015 [cs.CL]
* Pourreza and Rafiei (2023b)

  Mohammadreza Pourreza and
  Davood Rafiei. 2023b.
  Din-sql: Decomposed in-context learning of
  text-to-sql with self-correction.
  *NeurIPS* 36
  (2023), 36339–36348.
* Qian et al. (2024)

  Chen Qian, Wei Liu,
  Hongzhang Liu, Nuo Chen,
  Yufan Dang, Jiahao Li,
  Cheng Yang, Weize Chen,
  Yusheng Su, Xin Cong, et al.
  2024.
  Chatdev: Communicative agents for software
  development. In *ACL*.
  15174–15186.
* Qin et al. (2024)

  Yiwei Qin, Kaiqiang Song,
  Yebowen Hu, Wenlin Yao,
  Sangwoo Cho, Xiaoyang Wang,
  Xuansheng Wu, Fei Liu,
  Pengfei Liu, and Dong Yu.
  2024.
  InFoBench: Evaluating Instruction Following
  Ability in Large Language Models. In *ACL*.
  13025–13048.
* Rafailov et al. (2023)

  Rafael Rafailov, Archit
  Sharma, Eric Mitchell, Christopher D
  Manning, Stefano Ermon, and Chelsea
  Finn. 2023.
  Direct preference optimization: Your language model
  is secretly a reward model.
  *NeurIPS* 36
  (2023), 53728–53741.
* Raffel et al. (2020)

  Colin Raffel, Noam
  Shazeer, Adam Roberts, Katherine Lee,
  Sharan Narang, Michael Matena,
  Yanqi Zhou, Wei Li, and
  Peter J Liu. 2020.
  Exploring the limits of transfer learning with a
  unified text-to-text transformer.
  *JMLR* 21,
  140 (2020), 1–67.
* Rokis and Kirikova (2022)

  Karlis Rokis and Marite
  Kirikova. 2022.
  Challenges of low-code/no-code software
  development: A literature review. In *BIR*.
  3–17.
* Roziere et al. (2023)

  Baptiste Roziere, Jonas
  Gehring, Fabian Gloeckle, Sten Sootla,
  Itai Gat, et al. 2023.
  Code llama: Open foundation models for code.
  *arXiv preprint arXiv:2308.12950*
  (2023).
* Schellaert et al. (2025)

  Wout Schellaert, Fernando
  Martínez-Plumed, and José
  Hernández-Orallo. 2025.
  Analysing the predictability of language model
  performance.
  *ACM Transactions on Intelligent Systems and
  Technology* 16, 2
  (2025), 1–26.
* Schulman et al. (2017)

  John Schulman, Filip
  Wolski, Prafulla Dhariwal, Alec Radford,
  and Oleg Klimov. 2017.
  Proximal policy optimization algorithms.
  *arXiv preprint arXiv:1707.06347*
  (2017).
* Sun et al. (2023)

  Ruoxi Sun, Sercan Ö
  Arik, Alex Muzio, Lesly Miculicich,
  Satya Gundabathula, Pengcheng Yin,
  Hanjun Dai, Hootan Nakhost,
  Rajarishi Sinha, Zifeng Wang,
  et al. 2023.
  Sql-palm: Improved large language model adaptation
  for text-to-sql (extended).
  *arXiv preprint arXiv:2306.00739*
  (2023).
* Talaei et al. (2024)

  Shayan Talaei,
  Mohammadreza Pourreza, Yu-Chen Chang,
  Azalia Mirhoseini, and Amin Saberi.
  2024.
  Chess: Contextual harnessing for efficient sql
  synthesis.
  *arXiv preprint arXiv:2405.16755*
  (2024).
* Touvron et al. (2023)

  Hugo Touvron, Thibaut
  Lavril, Gautier Izacard, Xavier
  Martinet, Marie-Anne Lachaux,
  Timothée Lacroix, Baptiste
  Rozière, Naman Goyal, Eric Hambro,
  Faisal Azhar, et al.
  2023.
  Llama: Open and efficient foundation language
  models.
  *arXiv preprint arXiv:2302.13971*
  (2023).
* Wang et al. (2023)

  Bing Wang, Changyu Ren,
  Jian Yang, Xinnian Liang,
  Jiaqi Bai, Qian-Wen Zhang,
  Zhao Yan, and Zhoujun Li.
  2023.
  Mac-sql: Multi-agent collaboration for
  text-to-sql.
  *arXiv preprint arXiv:2312.11242*
  (2023).
* Wei et al. (2022)

  Jason Wei, Xuezhi Wang,
  Dale Schuurmans, Maarten Bosma,
  Fei Xia, Ed Chi, Quoc V
  Le, Denny Zhou, et al.
  2022.
  Chain-of-thought prompting elicits reasoning in
  large language models.
  *NeurIPS* 35
  (2022), 24824–24837.
* Wei et al. (2025)

  Zhaohui Wei, Lizi Liao,
  Xinguang Xiang, and Xiaoyu Du.
  2025.
  Enriching Responses with Crowd-Sourced Knowledge
  for Task-Oriented Conversational Agents.
  *ACM Transactions on Intelligent Systems and
  Technology* 16, 2
  (2025), 1–24.
* Xu et al. (2017)

  Xiaojun Xu, Chang Liu,
  and Dawn Song. 2017.
  Sqlnet: Generating structured queries from natural
  language without reinforcement learning.
  *arXiv preprint arXiv:1711.04436*
  (2017).
* Yu et al. (2018a)

  Tao Yu, Zifan Li,
  Zilin Zhang, Rui Zhang, and
  Dragomir Radev. 2018a.
  TypeSQL: Knowledge-Based Type-Aware Neural
  Text-to-SQL Generation. In *NAACL-HLT*.
  588–594.
* Yu et al. (2018b)

  Tao Yu, Michihiro
  Yasunaga, Kai Yang, Rui Zhang,
  Dongxu Wang, Zifan Li, and
  Dragomir Radev. 2018b.
  SyntaxSQLNet: Syntax Tree Networks for Complex
  and Cross-Domain Text-to-SQL Task. In *EMNLP*.
  1653–1663.
* Yu et al. (2018c)

  Tao Yu, Rui Zhang,
  Kai Yang, Michihiro Yasunaga,
  Dongxu Wang, Zifan Li,
  James Ma, Irene Li,
  Qingning Yao, Shanelle Roman,
  Zilin Zhang, and Dragomir Radev.
  2018c.
  Spider: A Large-Scale Human-Labeled Dataset for
  Complex and Cross-Domain Semantic Parsing and Text-to-SQL Task. In
  *EMNLP*. 3911–3921.
* Zhang et al. (2024)

  Junjie Zhang, Yupeng Hou,
  Ruobing Xie, Wenqi Sun,
  Julian McAuley, Wayne Xin Zhao,
  Leyu Lin, and Ji-Rong Wen.
  2024.
  Agentcf: Collaborative learning with autonomous
  language agents for recommender systems. In *WWW*.
  3679–3689.
* Zhong et al. (2017)

  Victor Zhong, Caiming
  Xiong, and Richard Socher.
  2017.
  Seq2sql: Generating structured queries from natural
  language using reinforcement learning.
  *arXiv preprint arXiv:1709.00103*
  (2017).
* Zhou et al. (2023)

  Jeffrey Zhou, Tianjian
  Lu, Swaroop Mishra, Siddhartha Brahma,
  Sujoy Basu, Yi Luan,
  Denny Zhou, and Le Hou.
  2023.
  Instruction-following evaluation for large language
  models.
  *arXiv preprint arXiv:2311.07911*
  (2023).

Generated on Sun Dec 21 06:39:58 2025 by [LaTeXML![Mascot Sammy](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAsAAAAOCAYAAAD5YeaVAAAAAXNSR0IArs4c6QAAAAZiS0dEAP8A/wD/oL2nkwAAAAlwSFlzAAALEwAACxMBAJqcGAAAAAd0SU1FB9wKExQZLWTEaOUAAAAddEVYdENvbW1lbnQAQ3JlYXRlZCB3aXRoIFRoZSBHSU1Q72QlbgAAAdpJREFUKM9tkL+L2nAARz9fPZNCKFapUn8kyI0e4iRHSR1Kb8ng0lJw6FYHFwv2LwhOpcWxTjeUunYqOmqd6hEoRDhtDWdA8ApRYsSUCDHNt5ul13vz4w0vWCgUnnEc975arX6ORqN3VqtVZbfbTQC4uEHANM3jSqXymFI6yWazP2KxWAXAL9zCUa1Wy2tXVxheKA9YNoR8Pt+aTqe4FVVVvz05O6MBhqUIBGk8Hn8HAOVy+T+XLJfLS4ZhTiRJgqIoVBRFIoric47jPnmeB1mW/9rr9ZpSSn3Lsmir1fJZlqWlUonKsvwWwD8ymc/nXwVBeLjf7xEKhdBut9Hr9WgmkyGEkJwsy5eHG5vN5g0AKIoCAEgkEkin0wQAfN9/cXPdheu6P33fBwB4ngcAcByHJpPJl+fn54mD3Gg0NrquXxeLRQAAwzAYj8cwTZPwPH9/sVg8PXweDAauqqr2cDjEer1GJBLBZDJBs9mE4zjwfZ85lAGg2+06hmGgXq+j3+/DsixYlgVN03a9Xu8jgCNCyIegIAgx13Vfd7vdu+FweG8YRkjXdWy329+dTgeSJD3ieZ7RNO0VAXAPwDEAO5VKndi2fWrb9jWl9Esul6PZbDY9Go1OZ7PZ9z/lyuD3OozU2wAAAABJRU5ErkJggg==)](http://dlmf.nist.gov/LaTeXML/)