> Source: https://arxiv.org/html/2501.08760v1

Leveraging LLM Agents for Translating Network Configurations





1. [1 Introduction](https://arxiv.org/html/2501.08760v1#S1 "In Leveraging LLM Agents for Translating Network Configurations")
2. [2 Background and Motivation](https://arxiv.org/html/2501.08760v1#S2 "In Leveraging LLM Agents for Translating Network Configurations")
   1. [2.1 Network Device Configuration](https://arxiv.org/html/2501.08760v1#S2.SS1 "In 2 Background and Motivation ‣ Leveraging LLM Agents for Translating Network Configurations")
   2. [2.2 Configuration Translation](https://arxiv.org/html/2501.08760v1#S2.SS2 "In 2 Background and Motivation ‣ Leveraging LLM Agents for Translating Network Configurations")
   3. [2.3 Opportunities and Challenges](https://arxiv.org/html/2501.08760v1#S2.SS3 "In 2 Background and Motivation ‣ Leveraging LLM Agents for Translating Network Configurations")
3. [3 Design and Implementation](https://arxiv.org/html/2501.08760v1#S3 "In Leveraging LLM Agents for Translating Network Configurations")
   1. [3.1 System Overview](https://arxiv.org/html/2501.08760v1#S3.SS1 "In 3 Design and Implementation ‣ Leveraging LLM Agents for Translating Network Configurations")
   2. [3.2 IRAG](https://arxiv.org/html/2501.08760v1#S3.SS2 "In 3 Design and Implementation ‣ Leveraging LLM Agents for Translating Network Configurations")
      1. [3.2.1 Configuration Intent Extraction](https://arxiv.org/html/2501.08760v1#S3.SS2.SSS1 "In 3.2 IRAG ‣ 3 Design and Implementation ‣ Leveraging LLM Agents for Translating Network Configurations")
      2. [3.2.2 Target Manual Retrieval](https://arxiv.org/html/2501.08760v1#S3.SS2.SSS2 "In 3.2 IRAG ‣ 3 Design and Implementation ‣ Leveraging LLM Agents for Translating Network Configurations")
      3. [3.2.3 Incremental Translation](https://arxiv.org/html/2501.08760v1#S3.SS2.SSS3 "In 3.2 IRAG ‣ 3 Design and Implementation ‣ Leveraging LLM Agents for Translating Network Configurations")
   3. [3.3 Verification](https://arxiv.org/html/2501.08760v1#S3.SS3 "In 3 Design and Implementation ‣ Leveraging LLM Agents for Translating Network Configurations")
   4. [3.4 Implementation Details](https://arxiv.org/html/2501.08760v1#S3.SS4 "In 3 Design and Implementation ‣ Leveraging LLM Agents for Translating Network Configurations")
4. [4 Evaluation](https://arxiv.org/html/2501.08760v1#S4 "In Leveraging LLM Agents for Translating Network Configurations")
   1. [4.1 Experimental Setup](https://arxiv.org/html/2501.08760v1#S4.SS1 "In 4 Evaluation ‣ Leveraging LLM Agents for Translating Network Configurations")
   2. [4.2 End-to-End Evaluation](https://arxiv.org/html/2501.08760v1#S4.SS2 "In 4 Evaluation ‣ Leveraging LLM Agents for Translating Network Configurations")
   3. [4.3 Ablation Study](https://arxiv.org/html/2501.08760v1#S4.SS3 "In 4 Evaluation ‣ Leveraging LLM Agents for Translating Network Configurations")
   4. [4.4 Deep Dive](https://arxiv.org/html/2501.08760v1#S4.SS4 "In 4 Evaluation ‣ Leveraging LLM Agents for Translating Network Configurations")
5. [5 Conclusion](https://arxiv.org/html/2501.08760v1#S5 "In Leveraging LLM Agents for Translating Network Configurations")
6. [A Appendix](https://arxiv.org/html/2501.08760v1#A1 "In Leveraging LLM Agents for Translating Network Configurations")
   1. [A.1 Manual Examples](https://arxiv.org/html/2501.08760v1#A1.SS1 "In Appendix A Appendix ‣ Leveraging LLM Agents for Translating Network Configurations")
   2. [A.2 Intent Extraction Details](https://arxiv.org/html/2501.08760v1#A1.SS2 "In Appendix A Appendix ‣ Leveraging LLM Agents for Translating Network Configurations")
   3. [A.3 Incremental Translation Details](https://arxiv.org/html/2501.08760v1#A1.SS3 "In Appendix A Appendix ‣ Leveraging LLM Agents for Translating Network Configurations")
   4. [A.4 Verification Details](https://arxiv.org/html/2501.08760v1#A1.SS4 "In Appendix A Appendix ‣ Leveraging LLM Agents for Translating Network Configurations")
   5. [A.5 Case Study](https://arxiv.org/html/2501.08760v1#A1.SS5 "In Appendix A Appendix ‣ Leveraging LLM Agents for Translating Network Configurations")

# Leveraging LLM Agents for Translating Network Configurations

Yunze Wei
Department of Computer Science and Technology, Tsinghua University

Xiaohui Xie


Yiwei Zuo
School of Computing, Australian National University

Tianshuo Hu
Department of Computer Science and Technology, Tsinghua University

Xinyi Chen
Department of Computer Science and Technology, Tsinghua University

Kaiwen Chi
Department of Computer Science and Technology, Tsinghua University

Yong Cui

###### Abstract

Configuration translation is a critical and frequent task in network operations.
When a network device is damaged or outdated, administrators need to replace it to maintain service continuity. The replacement devices may originate from different vendors, necessitating configuration translation to ensure seamless network operation.
However, translating configurations manually is a labor-intensive and error-prone process.
In this paper, we propose an intent-based framework for translating network configuration with Large Language Model (LLM) Agents.
The core of our approach is an Intent-based Retrieval Augmented Generation (IRAG) module that systematically splits a configuration file into fragments, extracts intents, and generates accurate translations.
We also design a two-stage verification method to validate the syntax and semantics correctness of the translated configurations.
We implement and evaluate the proposed method on real-world network configurations.
Experimental results show that our method achieves 97.74%percent97.7497.74\%97.74 % syntax correctness, outperforming state-of-the-art methods in translation accuracy.

11footnotetext: Corresponding authors: Xiaohui Xie (xiexiaohui@tsinghua.edu.cn) and Yong Cui (cuiyong@tsinghua.edu.cn)

## 1 Introduction

Configuration translation has become increasingly critical in modern network operations and maintenance.
With the rapid evolution of network technologies, organizations often face the challenge of replacing obsolete or damaged devices [[10](https://arxiv.org/html/2501.08760v1#bib.bib10)].
Cross-vendor device replacement, primarily motivated by pricing concerns, requires configuration translation due to discrepancies in Command Line Interface (CLI) configurations.

CLI configuration translation is challenging.
Network experts must understand the functionality and intent of the complex source device configuration [[3](https://arxiv.org/html/2501.08760v1#bib.bib3)] and translate it into the corresponding configuration for the target device.
However, the vendor-dependent nature of CLI syntax means that configurations vary dramatically across different device systems, requiring deep expertise in multiple vendor architectures.
In addition, core router configuration can consist of tens of thousands of lines [[6](https://arxiv.org/html/2501.08760v1#bib.bib6)].
Together, these factors make manual configuration translation not only extremely time-consuming but also highly susceptible to errors that could potentially disrupt network operations.

While both industry and academia are actively exploring automated methods for configuration translation, existing research remains inadequate for achieving practical automated translation.
NAssim [[6](https://arxiv.org/html/2501.08760v1#bib.bib6)] constructs device configuration models and uses NetBERT to recommend target configurations, but it is not an end-to-end approach and requires manual intervention.
ConfigTrans [[20](https://arxiv.org/html/2501.08760v1#bib.bib20)] uses a heuristic method and LLM to translate different types of commands but lacks understanding of the configuration logic and has a limited ability to generalize.

The rapid development of LLM has brought novel opportunities for automated configuration translation.
Recent advances in LLM’s reasoning capabilities [[13](https://arxiv.org/html/2501.08760v1#bib.bib13)] and successful applications of LLM-based multi-agent systems [[11](https://arxiv.org/html/2501.08760v1#bib.bib11), [26](https://arxiv.org/html/2501.08760v1#bib.bib26)] have demonstrated their potential for complex task automation.
Building on these developments, we propose an intent-based network configuration translation framework leveraging LLM agents.
While LLMs offer promising capabilities, applying them to configuration translation presents three key challenges: the instability of intent extraction, the difficulty of manual retrieval, and the inaccuracy of translation.
To address these challenges, we develop an Intent-based Retrieval Augmented Generation (IRAG) module with three components: (a) a well-designed prompt system for configuration splitting and intent extraction, (b) an enhanced manual retrieval mechanism combining filtering and voting strategies, and (c) an incremental translation process that preserves contextual dependencies.
We also design a two-stage verification module to improve translation accuracy.
Experimental results demonstrate the effectiveness of our approach, which achieves 97.74% syntax correctness and superior translation accuracy compared to state-of-the-art methods.

The main contributions of this paper are as follows:

1. 1.

   We analyze the root causes of difficulties in translating network configuration across vendors.
2. 2.

   We propose an intent-based configuration translation framework with LLM agents, implement the system\*\*\*Our code will be open-sourced after the review process. and evaluate on real datasets.
3. 3.

   We design the IRAG module to recall target manuals and generate translations based on intent.
4. 4.

   We design a two-stage verification to improve the syntax and semantic accuracy of configuration translation.

## 2 Background and Motivation

### 2.1 Network Device Configuration

Network device configuration is an essential part of network operation, covering the entire lifecycle of network devices, including setup, maintenance, and troubleshooting.

There are several ways to configure network devices.
The most traditional and widely used method is the Command Line Interface (CLI), which requires administrators to manually input commands or import configuration files.
The NETCONF [[9](https://arxiv.org/html/2501.08760v1#bib.bib9)] protocol and the YANG [[5](https://arxiv.org/html/2501.08760v1#bib.bib5), [25](https://arxiv.org/html/2501.08760v1#bib.bib25)] language are designed for future network device configuration and widely used in SDN for data center or campus network operation.
Although new protocols provide more convenient possibilities for network configuration, the CLI is still indispensable in scenarios that require device initialization.

A CLI command of network device usually consists of keywords, parameters, and the view in which it takes effect.
A single CLI command line usually consists of keywords, parameters, and many mandatory/optional items.
The following is a command template for the Huawei NE40E Router [[16](https://arxiv.org/html/2501.08760v1#bib.bib16)].
In this template, `ip address` is the keyword, `<ip-address>` is the mandatory parameter.
`{ <mask> | <mask-length> }` means that one of the parameter is required, and
`[ <sub> ]` means that the parameter is optional.

```
    ip address <ip-address>
        { <mask> | <mask-length> } [ <sub> ]
```

CLI often has multiple views, each of which contains a cluster of specific commands.
For example, the above command can be found in the interface view, Mtunnel view, and ACL address pool view, but the resulting behaviors are different.

### 2.2 Configuration Translation

Network device configuration translation is the process of converting source device configuration to target device configuration, ensuring consistent behaviour.
Network administrators often replace network devices across vendors due to factors such as functionality updates, disaster recovery, and pricing concerns, necessitating configuration translation.

However, the configuration syntax of different vendors is protected by patents [[18](https://arxiv.org/html/2501.08760v1#bib.bib18)], making direct mapping based on device configuration models impractical.
The general process of translating configurations manually includes the following four steps:
(1) Extract the configuration from the source device and understand the intent/function of the configuration;
(2) Manually translate the configuration of the source device into the configuration of the target device by consulting configuration manuals;
(3) Analyze the correctness of the translated configuration;
(4) Apply the translated configuration to the target device and verify the correctness of the configuration.
Configuration translation is not straightforward and requires a lot of expert experience.
We summarize the difficulties in configuration translation as follows.

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Method | |  | | --- | | End-to-end | | Translation | | |  | | --- | | Logic Difference | | Understanding | | |  | | --- | | Migration | | Overhead | |
| NAssim [[6](https://arxiv.org/html/2501.08760v1#bib.bib6)] | ✗ | ✗ | Mid |
| ConfigTrans [[20](https://arxiv.org/html/2501.08760v1#bib.bib20)] | ✓ | ✗ | High |
| Ours | ✓ | ✓ | Low |

Table 1: Comparison with existing methods.

![Refer to caption](x1.png)


Figure 1: Examples of diverse behavioral patterns in vendor-specific device configurations.

Difficulties of Configuration Translation. 
The difficulties of configuration translation stem from the significant differences in the behavioral logic of configuration models from different vendors, which can lead to significant differences in configuration commands.
Let’s take the configuration of OSPF and BFD protocols in Figure [1](https://arxiv.org/html/2501.08760v1#S2.F1 "Figure 1 ‣ 2.2 Configuration Translation ‣ 2 Background and Motivation ‣ Leveraging LLM Agents for Translating Network Configurations") as an example.
Nokia adopts a service-centric approach.
It first configures logical interfaces in a router instance and sets BFD protocol-related parameters in the logical interface.
Then, it creates an OSPF instance, binds the previously configured logical interface in it, and enables the BFD protocol.
In contrast, Huawei adopts a resource-centric approach.
It first creates an OSPF instance, then enables the OSPF instance in a physical interface, and enables the BFD protocol with related parameters.
Accurately translating configurations requires a deep understanding of the configuration logic of device systems from different vendors.

Moreover, there are also some detailed difficulties, such as the “one-to-many mapping” problem.
A command from one vendor may contain multiple optional keywords or parameters, which may require multiple commands to complete on another vendor’s device.
Such detailed problems also increase the workload and complexity of configuration translation.

Existing methods. 
As shown in Table [1](https://arxiv.org/html/2501.08760v1#S2.T1 "Table 1 ‣ 2.2 Configuration Translation ‣ 2 Background and Motivation ‣ Leveraging LLM Agents for Translating Network Configurations"), existing configuration translation methods can not fully address the difficulties of configuration translation.
NAssim [[6](https://arxiv.org/html/2501.08760v1#bib.bib6)] constructs the device model as a semantics-enhanced tree structure and uses NetBERT (fine-tuned SBERT [[24](https://arxiv.org/html/2501.08760v1#bib.bib24)]) to map the nodes of Vendor Device Models (VDM) and Unified Device Model (UDM).
Although NAssim achieves a 9.1x speed-up in the translation process, it only provides a recommended set of top-k target commands, still requiring a lot of follow-up manual work.
Based on NAssim, ConfigTrans [[20](https://arxiv.org/html/2501.08760v1#bib.bib20)] goes further with VDM models of two vendors to achieve end-to-end translation.
It uses a heuristic method to translate commands with parameters and translates commands without parameters with the help of LLMs.
However, ConfigTrans relies on pre-built parameter correspondence tables and requires a lot of up-front manual work.
Although it solves the “many-to-many” mapping problem in configuration translation in its scope,
its heuristic algorithms have limited generalization ability and cannot solve the essential translation problem caused by logic differences of configuration models.

In contrast, our work achieves end-to-end configuration translation, understands logic differences based on configuration manuals, and has lower migration overhead.

### 2.3 Opportunities and Challenges

This section introduces the opportunities of LLM agents in configuration translation and three new challenges.

Opportunities of LLM.
The development of LLM brings new opportunities for addressing network related problem [[19](https://arxiv.org/html/2501.08760v1#bib.bib19)].
Considering the significant advancements in the reasoning ability of LLMs [[13](https://arxiv.org/html/2501.08760v1#bib.bib13)], we aim to leverage LLM agents in place of human engineers for interpreting configuration intent and referencing target device manuals for automated configuration generation.
In this process, we identified the following new challenges:

Challenge #1: 
Instability of intent description.
While LLMs demonstrate proficiency in extracting configuration commands’ intent when provided with corresponding manual pages, the generated intent descriptions exhibit significant variation in their granularity and focus.
LLMs oscillate between high-level architectural descriptions and detailed implementation specifics.
Additionally, the linguistic style tends to align closely with the source device’s manual terminology, which introduces complexity in subsequent target manual retrieval and configuration translation tasks.

Challenge #2: 
Difficulty in retrieving relevant manuals.
Retrieving appropriate target device configuration manuals following source intent extraction presents substantial difficulties.
This complexity is two-fold:
(1) the extensive volume of manual pages of the target device requires efficient filtering mechanisms to eliminate irrelevant documentation while maintaining semantic accuracy, and (2) the same command frequently appears across multiple views or contexts, introducing ambiguity in manual selection and requiring sophisticated disambiguation strategies.

Challenge #3: 
Inaccuracy of generated configurations.
The hallucinations manifested by LLMs in configuration translation tasks present critical challenges to system reliability.
For example, LLMs may generate syntactically valid but semantically incorrect command parameters or combine incompatible configuration elements. A comprehensive feedback mechanism incorporating both syntactic validation and semantic verification is necessary to guide LLM in generating accurate and implementable configurations.

## 3 Design and Implementation

![Refer to caption](x2.png)


Figure 2: System workflow.

### 3.1 System Overview

The workflow of our system is shown in Figure [2](https://arxiv.org/html/2501.08760v1#S3.F2 "Figure 2 ‣ 3 Design and Implementation ‣ Leveraging LLM Agents for Translating Network Configurations").
The system consists of three main components: the config parser, the Intent-based RAG (IRAG), and the verification module.

Workflow.
The configuration to be translated is parsed by the parser,
which first constructs a device command tree based on the source device’s command manual and VDM.
Then it matches the lines to the command tree,
obtaining the view structure and corresponding manuals of each command.
The parsed commands then enter the IRAG module (§ [3.2](https://arxiv.org/html/2501.08760v1#S3.SS2 "3.2 IRAG ‣ 3 Design and Implementation ‣ Leveraging LLM Agents for Translating Network Configurations")).
IRAG uses the LLM Agent to extract the intent, retrieve the corresponding target device manuals, and incrementally translate the command fragments into the target device’s commands.
The translated configuration is then verified (§ [3.3](https://arxiv.org/html/2501.08760v1#S3.SS3 "3.3 Verification ‣ 3 Design and Implementation ‣ Leveraging LLM Agents for Translating Network Configurations")).
Syntax verification is performed during the incremental translation process, and semantic verification is performed after the entire configuration is translated.

Manuals.
We use two types of manuals.
Command Manuals contain syntax definitions and functional descriptions of all commands of the device, mainly used for constructing the configuration syntax tree.
Configuration Manuals contain the configuration procedure required to implement a certain function, mainly used for configuration generation.
Examples of the two types of manuals are shown in Appendix [A.1](https://arxiv.org/html/2501.08760v1#A1.SS1 "A.1 Manual Examples ‣ Appendix A Appendix ‣ Leveraging LLM Agents for Translating Network Configurations").

### 3.2 IRAG

IRAG is the core module of our system.
Inspired by existing works [[17](https://arxiv.org/html/2501.08760v1#bib.bib17), [2](https://arxiv.org/html/2501.08760v1#bib.bib2)], we use configurations intent to bridge the significant differences between the configuration models of devices from different vendors.
We first split the configuration into fragments based on functionality and extract the intent of each fragment (§ [3.2.1](https://arxiv.org/html/2501.08760v1#S3.SS2.SSS1 "3.2.1 Configuration Intent Extraction ‣ 3.2 IRAG ‣ 3 Design and Implementation ‣ Leveraging LLM Agents for Translating Network Configurations")).
Then we retrieve the corresponding configuration manuals of the target device based on the intent (§ [3.2.2](https://arxiv.org/html/2501.08760v1#S3.SS2.SSS2 "3.2.2 Target Manual Retrieval ‣ 3.2 IRAG ‣ 3 Design and Implementation ‣ Leveraging LLM Agents for Translating Network Configurations")).
Finally, we incrementally translate the fragments into the target device’s configuration (§ [3.2.3](https://arxiv.org/html/2501.08760v1#S3.SS2.SSS3 "3.2.3 Incremental Translation ‣ 3.2 IRAG ‣ 3 Design and Implementation ‣ Leveraging LLM Agents for Translating Network Configurations")).

#### 3.2.1 Configuration Intent Extraction

We use LLM to analyze the parsed configuration with corresponding command manuals,
split the configuration into fragments based on functionality, and extract the intent of each fragment.
However, as described in Challenge #1 (§[2.3](https://arxiv.org/html/2501.08760v1#S2.SS3 "2.3 Opportunities and Challenges ‣ 2 Background and Motivation ‣ Leveraging LLM Agents for Translating Network Configurations")),
LLM exhibits substantial stochastic variability during the extraction of intent.
The level of detail and linguistic style of the extracted intent varies widely, making subsequent manual retrieval and translation difficult.
To address this issue, we use the In-Context Learning (ICL) method [[8](https://arxiv.org/html/2501.08760v1#bib.bib8), [4](https://arxiv.org/html/2501.08760v1#bib.bib4)],
providing templates and examples of intent extraction to guide LLM to extract formatted and unified intent.
We also ask LLM to extract intents at different levels: a general description of the entire configuration fragment and a detailed description of each sub-module in the fragment.
This helps to improve the recall rate of the subsequent manual retrieval step.
The prompt template is shown in Appendix [A.2](https://arxiv.org/html/2501.08760v1#A1.SS2 "A.2 Intent Extraction Details ‣ Appendix A Appendix ‣ Leveraging LLM Agents for Translating Network Configurations").

![Refer to caption](x3.png)


Figure 3: Detailed workflow of target manual retrieval.

#### 3.2.2 Target Manual Retrieval

Accurately retrieving the target manual is crucial for the success of configuration translation.
General LLMs lack precise knowledge of the network configuration domain, so external manual knowledge injection is needed to assist the translation process.
To address Challenge #2 (§[2.3](https://arxiv.org/html/2501.08760v1#S2.SS3 "2.3 Opportunities and Challenges ‣ 2 Background and Motivation ‣ Leveraging LLM Agents for Translating Network Configurations")),
we designed a LLM-based manual filtering method and a voting mechanism to enhance the embedding-based manual retrieval.
The detailed workflow is shown in Figure [3](https://arxiv.org/html/2501.08760v1#S3.F3 "Figure 3 ‣ 3.2.1 Configuration Intent Extraction ‣ 3.2 IRAG ‣ 3 Design and Implementation ‣ Leveraging LLM Agents for Translating Network Configurations").

LLM-based Manual Filtering.
The configuration manuals of network devices are massive.
For example, Huawei’s NE40E router configuration manual contains 7300+ pages [[15](https://arxiv.org/html/2501.08760v1#bib.bib15)], making it difficult to retrieve the target manual pages accurately.
However, the configuration manual is organized as a directory tree.
Inspired by the human pattern of reading manuals,
we leverage LLM to traverse k𝑘kitalic\_k layers of the manual directory tree, selecting and entering the relevant subdirectories.
This progressively narrows the retrieval scope.
The filtered manual is ∼10%similar-toabsentpercent10\sim 10\%∼ 10 % of the original manual.
This improves the accuracy of manual retrieval in the subsequent process.

BGE Embedding Context.
Our goal is to match the corresponding manual page descriptions with the previously extracted intents.
We use the BGE model [[7](https://arxiv.org/html/2501.08760v1#bib.bib7)] based on BERT for encoding intent information and manual context, and use cosine similarity for ranking and retrieval.
To address the problem that a similar function appears in multiple views, we augmented the context with file path, which contains view-specific information and can filter out irrelevant views.
In summary, the manual context we use includes: the title of a manual page, page description, and manual file path.

Voting Mechanism.
The granularity of the intents of manual pages varies a lot.
To further improve the manual recall rate, we make full use of the multi-level intent descriptions extracted in the previous step.
We retrieve the top-k manuals for each intent description extracted from the fragment and use all the retrieval results for voting.
We use the similarity score of each retrieval as the voting weight to obtain a comprehensive retrieval result (new top-k manuals).
This method can effectively improve the manual retrieval rate (§ [4.3](https://arxiv.org/html/2501.08760v1#S4.SS3 "4.3 Ablation Study ‣ 4 Evaluation ‣ Leveraging LLM Agents for Translating Network Configurations")).

#### 3.2.3 Incremental Translation

Incremental translation is the final stage of IRAG, which translates source configuration fragments into target device configurations.
We construct a comprehensive prompt by combining source device configuration commands, corresponding manuals, and previously extracted target device documentation.
Then we use LLM’s understanding, analysis, and generation capabilities for translation.
Since LLMs have context length limits [[12](https://arxiv.org/html/2501.08760v1#bib.bib12)],
we opted for a fragment-by-fragment rather than full-text translation approach.
While translating each fragment independently is possible, we observe significant inter-fragment dependencies in practice.
Therefore, we choose the incremental translation approach, i.e., after translating a fragment, we use the translation result as the context input for the translation of the next fragment.
Our prompt template is shown in Appendix [A.3](https://arxiv.org/html/2501.08760v1#A1.SS3 "A.3 Incremental Translation Details ‣ Appendix A Appendix ‣ Leveraging LLM Agents for Translating Network Configurations").

### 3.3 Verification

To improve translation quality, we implement a two-stage verification process: syntax verification during incremental translation and semantic verification after the complete translation.
The prompt templates of this module are shown in Appendix [A.4](https://arxiv.org/html/2501.08760v1#A1.SS4 "A.4 Verification Details ‣ Appendix A Appendix ‣ Leveraging LLM Agents for Translating Network Configurations").

Syntax Verification.
This stage validates whether the translated configuration adheres to the target device’s syntax and view specifications.
For a given target device, we first construct a command syntax tree based on the target device’s command manual and build a configuration parser for it (the right side of Figure [2](https://arxiv.org/html/2501.08760v1#S3.F2 "Figure 2 ‣ 3 Design and Implementation ‣ Leveraging LLM Agents for Translating Network Configurations")).
During the incremental translation process, we input the partial translation into the configuration parser to check for correctness.
For command lines that do not conform to the syntax or view, we provide corresponding annotations and try to correct them by LLM.
We use LLM’s multi-round dialogue capability, i.e. the historical memory of the previous translation process is retained and only the incorrect part is entered in the correction process.
After correction, we verify again using the syntax tree to ensure that the syntax correctness is better than the previous version.

Semantic Verification.
While direct configuration translation with LLM shows limitations, we discover that LLM excels at analyzing configuration differences between vendors.
Therefore, we design a semantic verification module based on LLM, which includes two steps:
(1) Configuration difference analysis: we provide the original and the translated configuration with corresponding manual pages to LLM,
allowing it to analyze the differences between the two configurations and provide explanations.
(2) Semantic correction: based on the analysis results, we annotate the commands with semantic inconsistencies and provide the corresponding configuration manual pages as contexts to LLM.
Different from the translation process, we only use manual pages of the incorrect commands in this step and increase the proportion of relevant manual pages (i.e., increase top-k) to enhance error correction.

### 3.4 Implementation Details

We implement our system in Python with ∼3500similar-toabsent3500\sim 3500∼ 3500 Lines of Code (LoC).
In the parser, we build the configuration tree based on the open-source configuration models from NAssim [[6](https://arxiv.org/html/2501.08760v1#bib.bib6)] and write the corresponding parser for each vendor.
In IRAG module, we use BGE-m3 [[7](https://arxiv.org/html/2501.08760v1#bib.bib7)] as the sentence embedding model.
We used OpenAI’s SDK to call several LLMs, including GPT-4o [[22](https://arxiv.org/html/2501.08760v1#bib.bib22)], Qwen-Max [[1](https://arxiv.org/html/2501.08760v1#bib.bib1)], etc.
Our system has a relatively low migration cost.
To fit a new vendor, we only need to scrape the corresponding vendor’s configuration manual and command manual and write the corresponding parser (about 200 LoC in Python) without the finetuning process.
The parsers for different vendors are specific in the view structure, and the command syntax parsing module can be reused.

## 4 Evaluation

### 4.1 Experimental Setup

Manuals and Dataset.
We use Nokia 7750 SR [[21](https://arxiv.org/html/2501.08760v1#bib.bib21)] and Huawei NE40E [[14](https://arxiv.org/html/2501.08760v1#bib.bib14)] routers as our source and target devices.
The command manuals and configuration models (hierarchy of command manuals) come from the open-source dataset from NAssim [[6](https://arxiv.org/html/2501.08760v1#bib.bib6)].
We scrape the configuration manual of NE40E from the Huawei website as the configuration tutorial for IRAG module.
Our dataset includes 1063106310631063 lines of configuration commands from 53535353 files, where 33333333 files are real configuration files from the industry and 20202020 files from ConfigTrans [[20](https://arxiv.org/html/2501.08760v1#bib.bib20)].
The size of our dataset is comparable to existing work [[20](https://arxiv.org/html/2501.08760v1#bib.bib20), [6](https://arxiv.org/html/2501.08760v1#bib.bib6)].
The configurations cover various settings of the routers, including basic system information, interface, route policy, filter policy, BGP/IGP protocols, VPRN, etc.

Metrics.
The metrics we use consider both the similarity with the reference configuration and the correctness of the syntax and view:
(1) Tree Match (TM): the matching rate on the configuration tree, which checks the correctness of syntax and view.
(2) Syntax Correctness (SC):
the syntax matching rate. This metric is designed to measure pure syntax correctness because view errors caused by some commands may affect the matching of subsequent syntax-correct commands on the configuration tree.
(3) BLEU [[23](https://arxiv.org/html/2501.08760v1#bib.bib23)]: a metric that focuses on precision, often used to evaluate the output quality of machine translation tasks.
(4) Exact Match (EM): the strict matching rate, focuses on the recall rate of a full command line.
We also use Recall@Top-k to evaluate the manual retrieval module.

Methods and Baselines.
We use GPT-4o [[22](https://arxiv.org/html/2501.08760v1#bib.bib22)] as the baseline for end-to-end comparison with our proposed full method (GPT-4o+IRAG+Syntax and Semantic Verification).
In the ablation study, we test the partial methods of our system: GPT-4o+IRAG and GPT-4o+IRAG+Syn. (Syntax Verification).
For a comprehensive evaluation, we also use Qwen-Max [[1](https://arxiv.org/html/2501.08760v1#bib.bib1)] as an alternative base model and include ConfigTrans [[20](https://arxiv.org/html/2501.08760v1#bib.bib20)] as an additional baseline method.
Since ConfigTrans only supports configuration translation within its own scope, we conducted experiments on its dataset for separate comparisons.

### 4.2 End-to-End Evaluation

| Method | TM | SC | BLEU-2 | EM |
| --- | --- | --- | --- | --- |
| GPT-4o (baseline) | 0.6445 | 0.7867 | 0.6513 | 0.4611 |
| GPT-4o + IRAG | 0.7814 | 0.8944 | 0.7217 | 0.5978 |
| GPT-4o + IRAG + Syn. | 0.9133 | 0.9688 | 0.7350 | 0.6576 |
| Our full method (GPT-4o) | 0.9177 | 0.9774 | 0.7562 | 0.6730 |
| Qwen-Max (baseline) | 0.5661 | 0.7198 | 0.6350 | 0.4380 |
| Qwen-Max + IRAG | 0.7585 | 0.8908 | 0.6913 | 0.5582 |
| Qwen-Max + IRAG + Syn. | 0.8896 | 0.9519 | 0.7338 | 0.5536 |
| Our full method (Qwen-Max) | 0.8947 | 0.9540 | 0.7349 | 0.5739 |

Table 2: End-to-end evaluation.

Results.
The result of the end-to-end evaluation is shown in Table [2](https://arxiv.org/html/2501.08760v1#S4.T2 "Table 2 ‣ 4.2 End-to-End Evaluation ‣ 4 Evaluation ‣ Leveraging LLM Agents for Translating Network Configurations").
Our full method has a significant improvement in syntax and view metrics compared to the baseline with GPT-4o.
The syntax correctness rate reaches 97.74%percent97.7497.74\%97.74 %
which is 19.07%percent19.0719.07\%19.07 % higher than the baseline (GPT-4o).
The exact match rate also increases from 46.11%percent46.1146.11\%46.11 % to 67.30%percent67.3067.30\%67.30 % compared to the baseline.
However, the exact match results are for reference only, as sometimes the correct answer for the configuration translation is not unique.
In addition, our method also achieves relatively good results on Qwen-Max, indicating that it can adapt to different base models.

Comparison with ConfigTrans.
We conduct experiments on the dataset used in ConfigTrans (BGP and OSPF commands)
and the accuracy reaches 83.50%percent83.5083.50\%83.50 %, outperforming ConfigTrans’s 82.47%percent82.4782.47\%82.47 %.
However, it should be noted that our method does not rely on a pre-built parameter correspondence table,
which has stronger generalization and migration ability.

Case Study.
In Appendix [A.5](https://arxiv.org/html/2501.08760v1#A1.SS5 "A.5 Case Study ‣ Appendix A Appendix ‣ Leveraging LLM Agents for Translating Network Configurations"), we use a concrete example to show how our framework
makes the correct translation step by step.

### 4.3 Ablation Study

![Refer to caption](x4.png)


(a) Manual recall rate.

![Refer to caption](x5.png)


(b) View error rate.

Figure 4: Performance of the intent-based retrieval module.

IRAG Module.
We can see from Table [2](https://arxiv.org/html/2501.08760v1#S4.T2 "Table 2 ‣ 4.2 End-to-End Evaluation ‣ 4 Evaluation ‣ Leveraging LLM Agents for Translating Network Configurations") that the method with only IRAG has a great improvement in translation performance compared to the baseline.
In the GPT-4o + IRAG method, TM increases 13.69%percent13.6913.69\%13.69 % compared to the baseline (GPT-4o), and the EM also increases 13.67%percent13.6713.67\%13.67 %.
This result indicates that the IRAG module successfully enhances the ability of LLMs in configuration translation by introducing relevant target device manual information.

To verify the effectiveness of the LLM filter and voting mechanism in the process of target manual retrieval (§[3.2.2](https://arxiv.org/html/2501.08760v1#S3.SS2.SSS2 "3.2.2 Target Manual Retrieval ‣ 3.2 IRAG ‣ 3 Design and Implementation ‣ Leveraging LLM Agents for Translating Network Configurations")),
we labeled 156 lines of real configuration commands of Nokia with the corresponding Huawei manuals as our mini-benchmark for
evaluating the target manual recall rate.
Figure [4(a)](https://arxiv.org/html/2501.08760v1#S4.F4.sf1 "In Figure 4 ‣ 4.3 Ablation Study ‣ 4 Evaluation ‣ Leveraging LLM Agents for Translating Network Configurations") shows that both the voting and filter mechanisms have a significant improvement on the recall rate.
The top-20 recall rate of our full method reaches 70.33%percent70.3370.33\%70.33 %, which is 19.45%percent19.4519.45\%19.45 % higher than the baseline (BGE model [[7](https://arxiv.org/html/2501.08760v1#bib.bib7)]).
Figure [4(b)](https://arxiv.org/html/2501.08760v1#S4.F4.sf2 "In Figure 4 ‣ 4.3 Ablation Study ‣ 4 Evaluation ‣ Leveraging LLM Agents for Translating Network Configurations") shows that our method is also effective in suppressing view errors.
Considering the trade-offs between the recall rate and context length limit of LLM, we use k=20𝑘20k=20italic\_k = 20 as the default top-k parameter in incremental translation and increase it to 30 in the semantic verification module to enhance the probability of error correction and improve performance.

Verification Module.
Table [2](https://arxiv.org/html/2501.08760v1#S4.T2 "Table 2 ‣ 4.2 End-to-End Evaluation ‣ 4 Evaluation ‣ Leveraging LLM Agents for Translating Network Configurations") also shows that our verification module has a significant effect on improving the correctness of syntax and view.
With syntax verification, the syntax correctness rate (SC) increases 7.44% and the syntax tree matching rate (TM) increases 13.19% (GPT-4o).
This indicates that the syntax verification module can not only correct syntax errors but also improve the correctness of the view.
With semantic verification, BLEU-2 and EM increase 2.12%percent2.122.12\%2.12 % and 1.54%percent1.541.54\%1.54 % (GPT-4o), respectively.
This indicates that the semantic verification module also has effect on improving the accuracy of configuration translation.

### 4.4 Deep Dive

![Refer to caption](x6.png)


Figure 5: Deep dive into different types of configurations.

To further verify the performance of our method on different difficulty types of configuration translation problems, we divide the whole dataset according to the following three types:
  
(1) one source command maps one target command (1v1);
  
(2) one source command maps M𝑀Mitalic\_M target commands (1vM);
  
(3) N𝑁Nitalic\_N source commands map M𝑀Mitalic\_M target commands (NvM).
1vM also includes the cases where M𝑀Mitalic\_M source commands map one target command.
The results on the divided dataset are shown in Figure [5](https://arxiv.org/html/2501.08760v1#S4.F5 "Figure 5 ‣ 4.4 Deep Dive ‣ 4 Evaluation ‣ Leveraging LLM Agents for Translating Network Configurations").
It can be seen that our method has a great improvement compared to GPT-4o on all three different types of datasets.
On the most difficult NvM type, our method has the largest improvement in syntax correctness, with ∼17%similar-toabsentpercent17\sim 17\%∼ 17 % increase compared to GPT-4o (from 80.67% to 97.63%).
The significant improvement in the challenging dataset highlights the effectiveness of our method.

## 5 Conclusion

In this paper, we analyze the requirements and difficulties of cross-vendor network configuration translation.
The core challenge lies in the significant differences between the configuration models of vendors’ device systems.
We propose an LLM-driven intent-based network configuration translation framework, including the parser, IRAG, and verification modules. The designed system is verified on a real dataset and has a significant improvement compared to existing methods.

## References

* [1]

  Alibaba Group.
  Qwen-max.
  <https://bailian.console.aliyun.com/model-market/detail/qwen-max#/model-market/detail/qwen-max>, 2024.
* [2]

  Kaikai An, Fangkai Yang, Junting Lu, Liqun Li, Zhixing Ren, Hao Huang, Lu Wang, Pu Zhao, Yu Kang, Hua Ding, et al.
  Nissist: An incident mitigation copilot based on troubleshooting guides.
  ECAI Demo Track, 2024.
* [3]

  Theophilus Benson, Aditya Akella, and David A Maltz.
  Unraveling the complexity of network management.
  In NSDI, pages 335–348, 2009.
* [4]

  Amanda Bertsch, Maor Ivgi, Uri Alon, Jonathan Berant, Matthew R Gormley, and Graham Neubig.
  In-context learning with long-context models: An in-depth exploration.
  arXiv preprint arXiv:2405.00200, 2024.
* [5]

  Martin Björklund.
  YANG - A Data Modeling Language for the Network Configuration Protocol (NETCONF).
  RFC 6020, October 2010.
* [6]

  Huangxun Chen, Yukai Miao, Li Chen, Haifeng Sun, Hong Xu, Libin Liu, Gong Zhang, and Wei Wang.
  Software-defined network assimilation: bridging the last mile towards centralized network configuration management with nassim.
  In Proceedings of the ACM SIGCOMM 2022 Conference, pages 281–297, 2022.
* [7]

  Jianlv Chen, Shitao Xiao, Peitian Zhang, Kun Luo, Defu Lian, and Zheng Liu.
  Bge m3-embedding: Multi-lingual, multi-functionality, multi-granularity text embeddings through self-knowledge distillation, 2024.
* [8]

  Qingxiu Dong, Lei Li, Damai Dai, Ce Zheng, Jingyuan Ma, Rui Li, Heming Xia, Jingjing Xu, Zhiyong Wu, Baobao Chang, et al.
  A survey on in-context learning.
  Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing, pages 1107–1128, 2024.
* [9]

  Rob Enns.
  NETCONF Configuration Protocol.
  RFC 4741, December 2006.
* [10]

  Joseph C Hartman and Chin Hon Tan.
  Equipment replacement analysis: a literature review and directions for future research.
  The engineering economist, 59(2):136–153, 2014.
* [11]

  Sirui Hong, Mingchen Zhuge, Jonathan Chen, Xiawu Zheng, Yuheng Cheng, Jinlin Wang, Ceyao Zhang, Zili Wang, Steven Ka Shing Yau, Zijuan Lin, Liyang Zhou, Chenyu Ran, Lingfeng Xiao, Chenglin Wu, and Jürgen Schmidhuber.
  MetaGPT: Meta programming for a multi-agent collaborative framework.
  In The Twelfth International Conference on Learning Representations, 2024.
* [12]

  Cheng-Ping Hsieh, Simeng Sun, Samuel Kriman, Shantanu Acharya, Dima Rekesh, Fei Jia, Yang Zhang, and Boris Ginsburg.
  Ruler: What’s the real context size of your long-context language models?
  arXiv preprint arXiv:2404.06654, 2024.
* [13]

  Jie Huang and Kevin Chen-Chuan Chang.
  Towards reasoning in large language models: A survey.
  In 61st Annual Meeting of the Association for Computational Linguistics, ACL 2023, pages 1049–1065. Association for Computational Linguistics (ACL), 2023.
* [14]

  Huawei Technologies Co., Ltd.
  Ne40e-m2 product documentation.
  <https://support.huawei.com/hedex/hdx.do?docid=EDOC1100331639>, 2024.
* [15]

  Huawei Technologies Co., Ltd.
  Ne40e-m2 product documentation - configuration.
  <https://support.huawei.com/hedex/hdx.do?docid=EDOC1100331639&id=EN-US_TOPIC_0000001501814785>, 2024.
* [16]

  Huawei Technologies Co., Ltd.
  Ne40e-m2 product documentation - ip address (interface view).
  <https://support.huawei.com/hedex/hdx.do?docid=EDOC1100331639&id=EN-US_CLIREF_0000001759559309>, 2024.
* [17]

  Arthur S Jacobs, Ricardo J Pfitscher, Rafael H Ribeiro, Ronaldo A Ferreira, Lisandro Z Granville, Walter Willinger, and Sanjay G Rao.
  Hey, lumi! using natural language for intent-based network management.
  In 2021 USENIX Annual Technical Conference (USENIX ATC 21), pages 625–639, 2021.
* [18]

  Jim Duffy, Network World.
  Cisco sues huawei over intellectual property.
  <https://www.computerworld.com/article/1335175/cisco-sues-huawei-over-intellectual-property.html>, 2003.
* [19]

  Chang Liu, Xiaohui Xie, Xinggong Zhang, and Yong Cui.
  Large language models for networking: Workflow, advances and challenges.
  IEEE Network, 2024.
* [20]

  Zheng Naigong, Li Fuliang, Li Ziming, Yang Yu, Hao Yimo, Liu Chenyang, and Wang Xingwei.
  Configtrans: Network configuration translation based on large language models and constraint solving.
  In The 32nd IEEE International Conference on Network Protocols (ICNP 2024), 2024.
* [21]

  Nokia.
  Nokia sr os 24-7 configuration guide.
  <https://documentation.nokia.com/sr/24-7/index.html>, 2024.
* [22]

  OpenAI.
  Gpt-4o.
  <https://openai.com/index/hello-gpt-4o/>, 2024.
* [23]

  Kishore Papineni, Salim Roukos, Todd Ward, and Wei-Jing Zhu.
  Bleu: a method for automatic evaluation of machine translation.
  In Proceedings of the 40th annual meeting of the Association for Computational Linguistics, pages 311–318, 2002.
* [24]

  Nils Reimers and Iryna Gurevych.
  Sentence-BERT: Sentence embeddings using Siamese BERT-networks.
  In Kentaro Inui, Jing Jiang, Vincent Ng, and Xiaojun Wan, editors, Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP), pages 3982–3992, Hong Kong, China, November 2019. Association for Computational Linguistics.
* [25]

  Philip A. Shafer.
  An Architecture for Network Management Using NETCONF and YANG.
  RFC 6244, June 2011.
* [26]

  Qingyun Wu, Gagan Bansal, Jieyu Zhang, Yiran Wu, Beibin Li, Erkang Zhu, Li Jiang, Xiaoyun Zhang, Shaokun Zhang, Jiale Liu, Ahmed Hassan Awadallah, Ryen W White, Doug Burger, and Chi Wang.
  Autogen: Enabling next-gen LLM applications via multi-agent conversation.
  In ICLR 2024 Workshop on Large Language Model (LLM) Agents, 2024.

## Appendix A Appendix

### A.1 Manual Examples

We use two types of manuals in our work: Command Manuals and Configuration Manuals. We use Huawei NE40E Router manuals as examples to illustrate them.

Command Manuals. Contains syntax definitions and functional descriptions of all commands of the device, mainly used for constructing the configuration syntax tree in the parser.
As we can parser the source device’s configuration before translation and get the corresponding command manuals of each command line, the
command manuals are mainly used to let LLM understand the source device’s command syntax and semantics.
A command manual example is shown in Figure [6](https://arxiv.org/html/2501.08760v1#A1.F6 "Figure 6 ‣ A.1 Manual Examples ‣ Appendix A Appendix ‣ Leveraging LLM Agents for Translating Network Configurations").

Configuration Manuals. Contains configuration steps required to implement a certain function.
We use extracted intents to retrieve the corresponding configuration manuals, which are used to generate the configuration.
LLM reads the related configuration manuals to understand the target device’s configuration syntax and semantics, together with important view information.
A configuration manual example is shown in Figure [7](https://arxiv.org/html/2501.08760v1#A1.F7 "Figure 7 ‣ A.1 Manual Examples ‣ Appendix A Appendix ‣ Leveraging LLM Agents for Translating Network Configurations").

![Refer to caption](x7.png)


Figure 6: Command manual example.

![Refer to caption](x8.png)


Figure 7: Configuration manual example.

### A.2 Intent Extraction Details

We use the In-Context Learning (ICL) method to extract a formatted and unified intent for manual retrieval.
To achieve this, we design a prompt template shown in Figure [8](https://arxiv.org/html/2501.08760v1#A1.F8 "Figure 8 ‣ A.2 Intent Extraction Details ‣ Appendix A Appendix ‣ Leveraging LLM Agents for Translating Network Configurations") (simplified).
In the prompt, we provide LLM with a JSON format instruction and an output timplate.
We also provide LLM with intent examples to align with the linguistic style of the target device’s manuals.
To increase the robustness of the method, we have added a retry mechanism to ensure the correctness of output, making sure it can be parsed by a JSON decoder.

![Refer to caption](x9.png)


Figure 8: Prompt template for intent extraction.

### A.3 Incremental Translation Details

The prompt template of incremental translation is shown in Figure [9](https://arxiv.org/html/2501.08760v1#A1.F9 "Figure 9 ‣ A.3 Incremental Translation Details ‣ Appendix A Appendix ‣ Leveraging LLM Agents for Translating Network Configurations").
We provide LLM with the source configuration fragment to translate with corresponding manuals, preceding translations, and the retrieved target manual pages.
We also include command conventions to help LLM understand the syntax of command templates in the target device’s configuration manuals.
We ask LLM to incorporate the translated Huawei configuration fragment seamlessly into the preceding translations, ensuring the completeness and correctness of the generated configuration.

![Refer to caption](x10.png)


Figure 9: Prompt template for incremental translation.

### A.4 Verification Details

In syntax verification, we use LLM together with config syntax tree (in the parser module) to analyze and refine the syntax errors. The prompt template is shown in Figure [10](https://arxiv.org/html/2501.08760v1#A1.F10 "Figure 10 ‣ A.4 Verification Details ‣ Appendix A Appendix ‣ Leveraging LLM Agents for Translating Network Configurations").
In semantic verification, we use LLMs to analyze and refine the semantic errors. The prompt template for semantic verification is shown in Figure [12](https://arxiv.org/html/2501.08760v1#A1.F12 "Figure 12 ‣ A.4 Verification Details ‣ Appendix A Appendix ‣ Leveraging LLM Agents for Translating Network Configurations") and the prompt template for semantic correction is shown in Figure [11](https://arxiv.org/html/2501.08760v1#A1.F11 "Figure 11 ‣ A.4 Verification Details ‣ Appendix A Appendix ‣ Leveraging LLM Agents for Translating Network Configurations").

![Refer to caption](x11.png)


Figure 10: Prompt template for syntax correction.

![Refer to caption](x12.png)


Figure 11: Prompt template for semantic correction.

![Refer to caption](x13.png)


Figure 12: Prompt template for semantic verification.

### A.5 Case Study

We provide a case study of the configuration translation process of our method in Figure [13](https://arxiv.org/html/2501.08760v1#A1.F13 "Figure 13 ‣ A.5 Case Study ‣ Appendix A Appendix ‣ Leveraging LLM Agents for Translating Network Configurations").
To translate the fragment in NOKIA Source Configuration, the intent extraction module extracts the intent from the fragment.
Then the target manual retrieval module uses the general intent “Configure OSPF protocol and its parameters within a specific area for an interface” to retrieve the corresponding configuration manual page “Enabling OSPF” at top 4.
The incremental translation module uses the retrieved manual page and the source configuration fragment to generate the translated configuration fragment.
The target command `ospf enable` is translated successfully with correct views. This is because both the command and view information are included in the manual page.
In contrast, the translation result of GPT-4o not only misses this command but also provides incorrect view information.

![Refer to caption](x14.png)


Figure 13: A case study of the configuration translation process of our method.

Generated on Wed Jan 15 12:26:43 2025 by [LaTeXML![Mascot Sammy](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAsAAAAOCAYAAAD5YeaVAAAAAXNSR0IArs4c6QAAAAZiS0dEAP8A/wD/oL2nkwAAAAlwSFlzAAALEwAACxMBAJqcGAAAAAd0SU1FB9wKExQZLWTEaOUAAAAddEVYdENvbW1lbnQAQ3JlYXRlZCB3aXRoIFRoZSBHSU1Q72QlbgAAAdpJREFUKM9tkL+L2nAARz9fPZNCKFapUn8kyI0e4iRHSR1Kb8ng0lJw6FYHFwv2LwhOpcWxTjeUunYqOmqd6hEoRDhtDWdA8ApRYsSUCDHNt5ul13vz4w0vWCgUnnEc975arX6ORqN3VqtVZbfbTQC4uEHANM3jSqXymFI6yWazP2KxWAXAL9zCUa1Wy2tXVxheKA9YNoR8Pt+aTqe4FVVVvz05O6MBhqUIBGk8Hn8HAOVy+T+XLJfLS4ZhTiRJgqIoVBRFIoric47jPnmeB1mW/9rr9ZpSSn3Lsmir1fJZlqWlUonKsvwWwD8ymc/nXwVBeLjf7xEKhdBut9Hr9WgmkyGEkJwsy5eHG5vN5g0AKIoCAEgkEkin0wQAfN9/cXPdheu6P33fBwB4ngcAcByHJpPJl+fn54mD3Gg0NrquXxeLRQAAwzAYj8cwTZPwPH9/sVg8PXweDAauqqr2cDjEer1GJBLBZDJBs9mE4zjwfZ85lAGg2+06hmGgXq+j3+/DsixYlgVN03a9Xu8jgCNCyIegIAgx13Vfd7vdu+FweG8YRkjXdWy329+dTgeSJD3ieZ7RNO0VAXAPwDEAO5VKndi2fWrb9jWl9Esul6PZbDY9Go1OZ7PZ9z/lyuD3OozU2wAAAABJRU5ErkJggg==)](http://dlmf.nist.gov/LaTeXML/)