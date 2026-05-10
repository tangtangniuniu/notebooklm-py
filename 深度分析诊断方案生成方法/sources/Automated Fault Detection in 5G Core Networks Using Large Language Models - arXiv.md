> Source: https://arxiv.org/html/2512.19697

Automated Fault Detection in 5G Core Networks Using Large Language Models





1. [I Introduction](https://arxiv.org/html/2512.19697v1#S1 "In Automated Fault Detection in 5G Core Networks Using Large Language Models")
2. [II METHODOLOGY](https://arxiv.org/html/2512.19697v1#S2 "In Automated Fault Detection in 5G Core Networks Using Large Language Models")
   1. [II-A OpenAirInterface 5G Core](https://arxiv.org/html/2512.19697v1#S2.SS1 "In II METHODOLOGY ‣ Automated Fault Detection in 5G Core Networks Using Large Language Models")
   2. [II-B Chaos Mesh](https://arxiv.org/html/2512.19697v1#S2.SS2 "In II METHODOLOGY ‣ Automated Fault Detection in 5G Core Networks Using Large Language Models")
   3. [II-C Data Gathering](https://arxiv.org/html/2512.19697v1#S2.SS3 "In II METHODOLOGY ‣ Automated Fault Detection in 5G Core Networks Using Large Language Models")
   4. [II-D Log Filtering](https://arxiv.org/html/2512.19697v1#S2.SS4 "In II METHODOLOGY ‣ Automated Fault Detection in 5G Core Networks Using Large Language Models")
   5. [II-E LLM Fine-Tuning](https://arxiv.org/html/2512.19697v1#S2.SS5 "In II METHODOLOGY ‣ Automated Fault Detection in 5G Core Networks Using Large Language Models")
3. [III Experimental Results](https://arxiv.org/html/2512.19697v1#S3 "In Automated Fault Detection in 5G Core Networks Using Large Language Models")
   1. [III-A Binary Fault Detection](https://arxiv.org/html/2512.19697v1#S3.SS1 "In III Experimental Results ‣ Automated Fault Detection in 5G Core Networks Using Large Language Models")
   2. [III-B Exact Fault Identification](https://arxiv.org/html/2512.19697v1#S3.SS2 "In III Experimental Results ‣ Automated Fault Detection in 5G Core Networks Using Large Language Models")

# Automated Fault Detection in 5G Core Networks Using Large Language Models

Parsa Hatami\*
  
Ahmadreza Majlesara\*
  
Ali Majlesi
  
Babak Hossein Khalaj
\*These authors contributed equally to this work

###### Abstract

With the rapid growth of data volume in modern telecommunication networks and the continuous expansion of their scale, maintaining high reliability has become a critical requirement. These networks support a wide range of applications and services, including highly sensitive and mission-critical ones, which demand rapid and accurate detection and resolution of network errors. Traditional fault-diagnosis methods are no longer efficient for such complex environments.[[1](https://arxiv.org/html/2512.19697v1#bib.bib1)]
In this study, we leverage Large Language Models (LLMs) to automate network fault detection and classification. Various types of network errors were intentionally injected into a Kubernetes-based test network, and data were collected under both healthy and faulty conditions. The dataset includes logs from different network components (pods), along with complementary data such as system descriptions, events, Round Trip Time (RTT) tests, and pod status information. The dataset covers common fault types such as pod failure, pod kill, network delay, network loss, and disk I/O failures.
We fine-tuned the GPT-4.1 nano model via its API on this dataset, resulting in a significant improvement in fault-detection accuracy compared to the base model. These findings highlight the potential of LLM-based approaches for achieving closed-loop, and operator-free fault management, which can enhance network reliability and reduce downtime-related operational costs for service providers.

## I Introduction

Maintaining the continuous operation of modern communication networks—especially advanced infrastructures such as 5G systems—has become both crucial and increasingly challenging. Traditional network monitoring approaches rely heavily on manual inspection of logs, alerts, and performance metrics. Such processes are time-consuming, error-prone, and lack scalability as networks grow in size, complexity, and heterogeneity[[2](https://arxiv.org/html/2512.19697v1#bib.bib2)]. As telecommunication systems continue to evolve, integrating software-defined architectures, virtualization, and containerized services, the rapid identification and mitigation of faults have become even more difficult to achieve.

Recent advancements in artificial intelligence (AI), and particularly in Large Language Models (LLMs), offer a new paradigm for intelligent and automated network management [[3](https://arxiv.org/html/2512.19697v1#bib.bib3)] [[4](https://arxiv.org/html/2512.19697v1#bib.bib4)] [[6](https://arxiv.org/html/2512.19697v1#bib.bib6)]. These models possess the ability to understand natural language, interpret unstructured data such as logs, and even reason about causal relations in complex systems. This capability introduces a significant opportunity to transform traditional network operations—from reactive troubleshooting to proactive, self-healing mechanisms. While earlier studies explored AI-driven monitoring through statistical and deep learning models[[2](https://arxiv.org/html/2512.19697v1#bib.bib2)][[5](https://arxiv.org/html/2512.19697v1#bib.bib5)], LLMs now enable contextual reasoning across multimodal data sources, thereby bridging the gap between human expertise and automated fault diagnosis.

With the global transition from 4G to 5G and beyond, the scale and diversity of telecommunication infrastructures have expanded dramatically. Network environments now integrate cloud-native platforms, such as Kubernetes, where numerous microservices interact dynamically. Configuring, managing, and troubleshooting these environments demand both domain-specific and software-engineering expertise. Leveraging LLMs to automate such complex management tasks has therefore gained significant attention in recent research and industrial discussions, including works such as LLM for 5G: Network Management[[7](https://arxiv.org/html/2512.19697v1#bib.bib7)]. By combining domain knowledge with the reasoning capabilities of LLMs, it becomes feasible to realize autonomous, closed-loop network operations capable of detecting, classifying, and resolving errors in near real time.
  
A review of previous research reveals that no prior work has explored a generalized framework for assessing the overall health of communication networks using Large Language Models (LLMs) to identify potential faults across different layers and components. Most existing studies focus on specific layers—such as the physical or data-link layer—and rely on structured numerical data rather than unstructured system information. Techniques such as anomaly detection and time-series forecasting have been applied successfully[[1](https://arxiv.org/html/2512.19697v1#bib.bib1)][[2](https://arxiv.org/html/2512.19697v1#bib.bib2)] in these limited contexts to detect deviations in predefined performance indicators.

In parallel, several works have investigated log analysis using traditional machine-learning or rule-based approaches[[4](https://arxiv.org/html/2512.19697v1#bib.bib4)] [[5](https://arxiv.org/html/2512.19697v1#bib.bib5)] [[6](https://arxiv.org/html/2512.19697v1#bib.bib6)]. However, these methods typically operate on pre-parsed and highly filtered logs within controlled experimental conditions, requiring significant preprocessing efforts. As a result, their applicability is restricted to detecting a narrow range of explicitly defined errors that appear in standardized log formats. While such techniques can achieve high accuracy in constrained settings, they are not scalable or adaptable to heterogeneous, dynamic network environments.

Recent domain-specific efforts have targeted 5G fault detection and RCA with hybrid ML–LLM pipelines. In the core network, *5G Core Fault Detection and Root Cause Analysis using Machine Learning and Generative AI* combines supervised anomaly detectors with LLM-based summarization to improve diagnosis quality on control/user-plane events, demonstrating that generative models can convert heterogeneous operational traces into operator-ready incident narratives [[8](https://arxiv.org/html/2512.19697v1#bib.bib8)]. Complementary trends extend beyond the core toward cross-domain or cross-vendor settings: *An LLM-based Cross-Domain Fault Localization in Carrier Networks* shows that aligning prompts with topology/context priors improves generalization across environments, while *RCA Copilot* operationalizes LLMs as a copilot over multi-source telemetry (logs, metrics, traces), yielding actionable recommendations rather than raw detections [[9](https://arxiv.org/html/2512.19697v1#bib.bib9), [10](https://arxiv.org/html/2512.19697v1#bib.bib10)]. These systems substantiate the utility of LLMs for interpretability and triage, yet most still depend on structured features, curated parsers, or offline post-processing pipelines, which limits real-time applicability in highly dynamic, cloud-native 5G cores.

A parallel line of work studies LLMs (and tool-augmented LLM agents) for automated RCA and decision support. *RCAgent* integrates tool calls and knowledge retrieval with conversational reasoning to correlate events and surface root causes in complex cloud stacks [[11](https://arxiv.org/html/2512.19697v1#bib.bib11)]. In telecom-adjacent 5G contexts, LLM-driven RCA has also been explored for RAN anomalies using graph/transformer models to represent dependencies, and for verticals such as power-grid 5G where domain knowledge must be fused with network telemetry [[12](https://arxiv.org/html/2512.19697v1#bib.bib12), [13](https://arxiv.org/html/2512.19697v1#bib.bib13)]. *Reasoning Language Models for Root Cause Analysis in 5G Wireless Networks* further argues for explicit chain-of-thought/plan-and-act prompting to improve causal attribution under noisy observability [[14](https://arxiv.org/html/2512.19697v1#bib.bib14)]. Across these works, three gaps remain: (i) reliance on pre-parsed or schema-constrained inputs rather than raw, heterogeneous logs and events; (ii) limited coupling with live orchestrators (e.g., Kubernetes) for closed-loop response; and (iii) scarcity of fine-tuned datasets built from realistic fault injections in operational 5G cores.

In this study, our objective is to design a comprehensive and flexible pipeline capable of processing heterogeneous network inputs—such as raw logs, events, and status reports—without extensive preprocessing or manual parsing. The proposed LLM-based approach acts as an intelligent conversational assistant that enables network operators, even without deep technical expertise, to monitor and diagnose network conditions using simple natural-language queries. Furthermore, the adaptability of LLMs allows new data types or fault categories to be seamlessly integrated into the model, dynamically expanding its operational scope. Finally, this model can be deployed in a closed-loop, real-time monitoring framework, continuously observing the network, identifying anomalies, and generating detailed diagnostic reports whenever faults occur. Such an approach has the potential to revolutionize network management by combining automation, interpretability, and reliability within a single unified system[[3](https://arxiv.org/html/2512.19697v1#bib.bib3)][[7](https://arxiv.org/html/2512.19697v1#bib.bib7)].

## II METHODOLOGY

An LLM is trained on logs from 5G mobile networks to detect the root cause of failures. For training, faults are generated using Chaos Mesh in an OpenAirInterface 5G network deployed on a Kubernetes cluster. The entire training pipeline is shown in Fig. [1](https://arxiv.org/html/2512.19697v1#S2.F1 "Figure 1 ‣ II METHODOLOGY ‣ Automated Fault Detection in 5G Core Networks Using Large Language Models").

![Refer to caption](entire_pipeline.png)

Figure 1: Dataset generation for training an LLM on fault detection using Chaos Mesh.

### II-A OpenAirInterface 5G Core

To evaluate the proposed framework under realistic network conditions, we developed an experimental 5G testbed based on the OpenAirInterface (OAI) 5G Core, an open-source and standards-compliant implementation of the 3GPP Release 15 specification[[15](https://arxiv.org/html/2512.19697v1#bib.bib15)].

Our core network includes the Access and Mobility Management Function (AMF), the Session Management Function (SMF), the User Plane Function (UPF). A dedicated database module maintains subscriber and session information. The radio access layer of the testbed consists of an OAI-based gNodeB (gNB) connected to multiple User Equipments (UEs), forming a fully functional RAN-Core integration.

In our implementation, each network component was deployed as a containerized pod within a Kubernetes cluster, allowing for isolated management, automated scaling, and continuous log collection. These logs, along with performance metrics from the gNB and UEs, served as the primary data source for our LLM-based monitoring and fault-detection pipeline.

![Refer to caption](OAI.png)

  


Figure 2: OpenAirInterface 5G Core Architecture Diagram (adapted from the official OAI documentation [[15](https://arxiv.org/html/2512.19697v1#bib.bib15)]).

### II-B Chaos Mesh

To generate dataset for the proposed LLM-based monitoring framework, controlled fault scenarios were introduced into the experimental testbed using Chaos Mesh, a powerful open-source chaos engineering platform designed for Kubernetes environments[[16](https://arxiv.org/html/2512.19697v1#bib.bib16)]. Chaos Mesh enables the simulation of various failure conditions at the pod, network, and system levels in a safe and repeatable manner.
In this study, five representative categories of faults were selected to emulate common failure conditions in cloud-native 5G systems:

1) Pod Failure:
Simulates unexpected termination or crash of a containerized network function, such as AMF or SMF. This fault type tests the resilience of service recovery mechanisms and the system’s ability to restart or reassign affected pods automatically.

2) Pod Kill:
Represents a forced termination of a specific pod process at runtime. Unlike pod failure, this type mimics operator-triggered or abrupt shutdown scenarios, providing insights into how quickly the orchestration layer (Kubernetes) detects and replaces the terminated component.

3) Network Delay:
Introduces artificial latency into communication between selected pods or components (e.g., between the gNB and the UPF). This allows evaluation of the system’s performance under delayed signaling and degraded transport conditions, reflecting scenarios such as congested backhaul links.

4) Network Loss:
Simulates packet drops within network interfaces to analyze the tolerance of the 5G core control and data planes to unreliable transmission. This experiment helps study how message retransmissions and session stability are affected under partial network loss.

5) I/O Injection:
Injects read/write latency or temporary disk unavailability into containerized components, replicating storage-related anomalies such as database I/O bottlenecks or temporary filesystem access failures. This fault type examines the robustness of stateful services like the core database module.

Each fault type was applied to different components of the OAI 5G Core for predefined time intervals, while comprehensive telemetry data—including system logs, event traces, pod status updates, and round-trip time (RTT) measurements—were collected in parallel. This process yielded a rich dataset containing both normal and abnormal operational states, which was subsequently used for fine-tuning the LLM and validating its fault detection and reasoning capabilities.

Through this controlled and systematic approach, Chaos Mesh provided a reliable means to evaluate the network’s fault response and to train the LLM model under realistic and diverse failure conditions.

### II-C Data Gathering

To build a training and evaluation dataset for our LLM-based fault diagnosis system, we developed an automated data collection pipeline that interacts directly with the Kubernetes-based 5G core deployment. The pipeline remotely controls the testbed, orchestrates experiments, injects faults, and captures multi-source telemetry before and after each fault scenario in a structured and repeatable manner. The multi-source telemetry collection and aggregation design is inspired by cloud-native observability frameworks such as Prometheus and Kubernetes logging best practices.[[17](https://arxiv.org/html/2512.19697v1#bib.bib17)]

The data collection process is executed from a controller machine that connects to the cluster over SSH. Through this interface, the pipeline programmatically issues operational commands to query the state of the system, retrieve runtime information, and persist relevant outputs. The workflow consists of four main stages:

1. 1.

   Network Reset and Initialization: At the start of each experiment, the testbed is brought into a known healthy baseline state. The script tears down and reinstalls the mobile core network (AMF, SMF, UPF, database, gNB) and user equipment (UE) instances using predefined deployment descriptors. After redeployment, the pipeline automatically waits until all critical components are reported as ready by Kubernetes. This ensures that each experiment begins from a consistent configuration and that observed degradations are attributable to injected faults rather than residual transient behavior from previous runs.
2. 2.

   Health Monitoring and Status Capture: The script periodically inspects the lifecycle state of all pods (e.g., Running, CrashLoopBackOff, etc.) to detect any non-running or partially degraded components. Pod status summaries are stored to disk at each experiment step. In addition, a “describe” snapshot is collected for every pod. This kubectl describe pod output includes recent events, restart counts, container-level conditions, resource usage signals, and warning messages generated by Kubernetes. Capturing these descriptions is critical for post hoc reasoning, because they often contain early indicators of faults (for example, repeated restarts, image pull errors, failed liveness probes) that may not yet appear in high-level KPIs.
3. 3.

   Runtime Telemetry and Connectivity Measurements: For each core network function and UE pod, the pipeline retrieves recent logs directly from the workload containers. These logs include authentication traces, session setup messages, mobility management events, forwarding plane messages, and error messages from services such as AMF, SMF, and UPF. In addition to log data, the pipeline actively measures connectivity quality between the core and each UE by executing an RTT (round-trip time) test. RTT results are collected for all UE instances both before and after the fault is injected. This allows us to correlate control-plane or user-plane anomalies with observable service impact at the UE side.
4. 4.

   Event and System-Level Reporting: Alongside pod-local telemetry, the pipeline also records the global Kubernetes event history in the target namespace. The event trace captures cluster-level reactions to faults (e.g., pod eviction, rescheduling attempts, container kills, liveness probe failures, node-level resource pressure). By including these events in the dataset, we provide the model with causal context: not only what failed, but also how the orchestration layer responded.

All collected artifacts from a single experimental run—pod logs, pod descriptions, per-pod status, UE RTT measurements (before/after fault), and namespace-wide event history—are stored for each experiment.

This automated approach has three important properties. First, it guarantees repeatability: each dataset sample corresponds to a known network state and a known injected fault condition. Second, it captures heterogeneous data sources (raw logs, status descriptions, cluster events, RTT measurements) without requiring heavy manual preprocessing or hand-written parsing rules. Third, it produces operator-facing, human-readable traces that can be directly consumed by an LLM. In other words, rather than relying solely on numerical metrics or narrowly structured telemetry, the pipeline aggregates semantically rich, text-based observations that reflect how real engineers would inspect and debug a live 5G core deployment.

These consolidated experiment snapshots form the supervision data used for fine-tuning the LLM. Each snapshot is paired with the ground-truth fault label associated with that experiment (e.g., network delay, pod kill, I/O degradation), enabling supervised training for fault classification and explanatory diagnosis.

### II-D Log Filtering

Log files are typically very large. For instance, within four minutes, the gNodeB generates over 2,500 log lines (amounting to more than 60,000 tokens), costing about $0.001 when processed using gpt-4o-mini. Therefore, the logs are first filtered to retain only the important lines.

![Refer to caption](Fault_detection_pipeline_02.png)

Figure 3: Fault Detection Pipeline

As illustrated in Fig. [4](https://arxiv.org/html/2512.19697v1#S2.F4 "Figure 4 ‣ II-D Log Filtering ‣ II METHODOLOGY ‣ Automated Fault Detection in 5G Core Networks Using Large Language Models"), the gNodeB log lines are color-coded. During filtering, only the colored lines (green, yellow, or red) are kept, as they represent the most relevant information.

![Refer to caption](gnb_logs.png)

Figure 4: Gnode-B logs

Each log line of other network elements contains a tag indicating its level (see Fig. [5](https://arxiv.org/html/2512.19697v1#S2.F5 "Figure 5 ‣ II-D Log Filtering ‣ II METHODOLOGY ‣ Automated Fault Detection in 5G Core Networks Using Large Language Models")). The possible tags include [info] for informational messages, [warn] for warnings, [debug], and [trace]. For LLM processing, only [warn] and [info] lines are retained.

![Refer to caption](amf_logs.png)

  


Figure 5: AMF logs

### II-E LLM Fine-Tuning

As described in the data-gathering section, the following data were collected after injecting a fault, concatenated, and combined with a system prompt. The complete input was then provided to the LLM, which was instructed to identify the source of the problem:

* •

  Pod status: Output of kubectl get pods, listing NAME, READY, STATUS, RESTARTS, and AGE. Used to detect PodFailure and PodKill conditions.
* •

  Pod logs: Logs from individual components (e.g., amf, smf, upf, db, gnb, ue1, ue3), such as oai-amf\_filtered.txt and oai-db\_filtered.txt.
* •

  Pod events: Kubernetes event outputs.
* •

  RTT data: Latency statistics for each UE before and after fault injection, e.g.,
    
  rtt min/avg/max/mdev = 29.168/36.242/52.845/8.537 ms.

Network elements include amf, smf, upf, db (database), gnb, and user equipments (UEs) such as ue1 and ue3.

In the system prompt, each component of the data and the corresponding fault types were briefly described along with the logic for fault detection. A simplified version of the system prompt is shown in Fig. [6](https://arxiv.org/html/2512.19697v1#S2.F6 "Figure 6 ‣ II-E LLM Fine-Tuning ‣ II METHODOLOGY ‣ Automated Fault Detection in 5G Core Networks Using Large Language Models"). The collected data, together with the system prompt, were provided to the LLM to infer and report network errors.

System Prompt (Fault Diagnosis Task Definition)

The model acts as an expert 5G network fault analyzer for OpenAirInterface (OAI) deployments on Kubernetes,
identifying exactly one failure type among five: *IOInjection, NetworkDelay, NetworkLoss, PodFailure,* or *PodKill*.
Input data include pod status (kubectl get pods), pod logs (AMF, SMF, UPF, DB, gNB, UEs), Kubernetes events, and RTT latency statistics.
Detection logic:

•

IOInjection: “Unknown database ’oai\_5g”’ in DB logs.
•

NetworkDelay: RTT after fault ≫\gg RTT before fault.
•

NetworkLoss: “unknown RNTI” in gNB logs or missing RTT data.
•

PodFailure: pod status = RunContainerError, READY count decreases.
•

PodKill: pod status = ContainerCreating or AGE < 2 min.
Exactly one fault type occurs per analysis.
The model outputs a concise diagnostic sentence only, e.g.,
*“Yes, network loss, 60% packets from RAN to AMF lost”*,
without speculation or additional explanation.


Figure 6: System prompt used for the 5G fault‑diagnosis model.

## III Experimental Results

50% of the data were used for training, 25% for validation, and the remaining 25% for testing.

The GPT-4.1-Nano model was fine-tuned on the dataset using the OpenAI API. The dataset contains 118 experiments. As shown in Fig. [7](https://arxiv.org/html/2512.19697v1#S3.F7 "Figure 7 ‣ III Experimental Results ‣ Automated Fault Detection in 5G Core Networks Using Large Language Models"), the data volume for each fault type is uniformly distributed across all fault categories.

![Refer to caption](dataset_composition.png)

Figure 7: Distribution of fault-injection experiment types within the dataset

To evaluate the capability of the fine‑tuned LLM in network fault diagnosis, two evaluation modes were defined:

(i) Binary detection, determining whether any fault exists in the log response, and

(ii) Exact matching, verifying the entire predicted response against the labeled dataset to ensure correct identification of the specific fault type.

### III-A Binary Fault Detection

Fig. [8](https://arxiv.org/html/2512.19697v1#S3.F8 "Figure 8 ‣ III-A Binary Fault Detection ‣ III Experimental Results ‣ Automated Fault Detection in 5G Core Networks Using Large Language Models") summarizes overall performance for binary classification. The fine‑tuned model achieved 93% accuracy and 95% F1‑score, representing a substantial improvement over the non‑tuned baseline (40% accuracy and 45% F1‑score). This indicates that fine‑tuning significantly enhances the model’s consistency in detecting the presence of faults across diverse log inputs.

The improvement in recall from 30% to 93% indicates that the baseline model was weak in fault detection and often misclassified faulty networks as normal.

![Refer to caption](overall_perf.png)

Figure 8: Binary comparison of fine tuned and base model in fault detection.

### III-B Exact Fault Identification

Fig. [9](https://arxiv.org/html/2512.19697v1#S3.F9 "Figure 9 ‣ III-B Exact Fault Identification ‣ III Experimental Results ‣ Automated Fault Detection in 5G Core Networks Using Large Language Models") illustrates the per-fault accuracy comparison between the fine-tuned and baseline GPT-4.1-Nano models across five fault categories. The fine-tuned model consistently outperforms its baseline counterpart for all fault types, achieving near-perfect accuracy for I/O Injection (1.00) and Pod Failure (0.97).
The 100% accuracy achieved for I/O Injection is primarily attributable to the small sample size (10 instances) and the distinctive log pattern observed during this fault, where the database pod’s disk failed due to I/O Injection and the unknown database ’oai’ was displayed in the DB logs. Consequently, the fine-tuned LLM identified this fault easily due to the clear and repetitive textual signature.
The improvement is particularly significant for Pod Kill detection, where the baseline accuracy of 0.23 increases to 0.93 after fine-tuning, indicating a substantial enhancement in recognizing destructive pod-level terminations. Network-related faults, namely Network Loss and Network Delay, also exhibit strong performance stability with accuracies of 0.91 and 0.87, respectively, underscoring the model’s robustness to transient latency and packet-loss anomalies. These results confirm that the fine-tuning process effectively generalized across heterogeneous fault classes, yielding a more reliable and fault-sensitive LLM-based detection system.

![Refer to caption](faultwise_accuracy_comparison.png)

Figure 9: Binary comparison of fine tuned and base model in fault detection.

## References

* [1]

  P. Chakraborty, M. Corici, and T. Magedanz, “System failure prediction within software 5G core networks using time series forecasting,” in Proc. IEEE Int. Conf. Commun. Workshops (ICC Workshops), Montreal, QC, Canada, 2021, pp. 1–7, doi: 10.1109/ICCWorkshops50388.2021.9473530.
* [2]

  Y. Tan, J. Wang, J. Liu, and Y. Li, “Deep learning-based log anomaly detection for 5G core network,” in Proc. IEEE/CIC Int. Conf. Commun. in China (ICCC), Dalian, China, 2023, pp. 1–6, doi: 10.1109/ICCC57788.2023.10233555.
* [3]

  W. Guan, J. Cao, S. Qian, J. Gao, and C. Ouyang, “LogLLM: Log-based anomaly detection using large language models,” arXiv preprint arXiv:2411.08561, 2025. [Online]. Available: https://arxiv.org/abs/2411.08561https://arxiv.org/abs/2411.08561
* [4]

  X. Han, S. Yuan, and M. Trabelsi, “LogGPT: Log anomaly detection via GPT,” in Proc. IEEE Int. Conf. Big Data (BigData), Sorrento, Italy, 2023, pp. 1117–1122, doi: 10.1109/BigData59044.2023.10386543.
* [5]

  H. Guo, S. Yuan, and X. Wu, “LogBERT: Log anomaly detection via BERT,” in Proc. Int. Joint Conf. Neural Networks (IJCNN), Shenzhen, China, 2021, pp. 1–8, doi: 10.1109/IJCNN52387.2021.9534113.
* [6]

  J. Qi, H. Zhu, L. Zhang, J. Guo, R. Chen, Y. Zhu, and Y. Liu, “LogGPT: Exploring ChatGPT for log-based anomaly detection,” in Proc. IEEE Int. Conf. High Performance Computing & Communications, Data Science & Systems, Smart City & Dependability in Sensor, Cloud & Big Data Systems & Application (HPCC/DSS/SmartCity/DependSys), Melbourne, Australia, 2023, pp. 273–280, doi: 10.1109/HPCC-DSS-SmartCity-DependSys60770.2023.00045.
* [7]

  A. Mamaghani, A. Nourian, N. Mohtaram, A. Shokrani, S. M. Nasiri, S. K. Ranjbar, A. Mohammadi, N. Nikaein, and B. H. Khalaj, “LLM for 5G: Network management,” in Proc. IEEE Int. Conf. on Machine Learning for Communication and Networking (ICMLCN), Stockholm, Sweden, May 5–8, 2024.
* [8]

  J. H. R. Isaac, H. Saradagam, and N. Pardhasaradhi,
  “5G core fault detection and root cause analysis using machine learning and generative AI,”
  arXiv preprint arXiv:2508.09152, 2025. [Online]. Available: https://arxiv.org/abs/2508.09152
* [9]

  J. Ma, S. Han, G. Wang, Z. Wang, F. Fan, and S. Ye,
  “An LLM-based cross-domain fault localization in carrier networks,”
  in Proc. 4th Int. Conf. Artif. Intell., Robot., and Commun. (ICAIRC),
  Xiamen, China, 2024, pp. 731–736,
  doi: 10.1109/ICAIRC64177.2024.10900110.
* [10]

  A. Shan, J. Kaur, R. Singh, T. Banka, R. Yavatkar, and T. Sridhar,
  “RCA Copilot: Transforming network data into actionable insights via large language models,”
  arXiv preprint arXiv:2507.03224, 2025. [Online]. Available: https://arxiv.org/abs/2507.03224
* [11]

  Z. Wang, Z. Liu, Y. Zhang, A. Zhong, J. Wang, F. Yin, L. Fan, L. Wu, and Q. Wen,
  “RCAgent: Cloud root cause analysis by autonomous agents with tool-augmented large language models,”
  in Proc. 33rd ACM Int. Conf. Inf. and Knowl. Manage. (CIKM),
  Oct. 2024, pp. 4966–4974,
  doi: 10.1145/3627673.3680016.
* [12]

  A. Hasan, C. Boeira, K. Papry, Y. Ju, Z. Zhu, and I. Haque,
  “Root cause analysis of anomalies in 5G RAN using graph neural network and transformer,”
  arXiv preprint arXiv:2406.15638, 2024. [Online]. Available: https://arxiv.org/abs/2406.15638
* [13]

  Z. Guo, H. Zhang, L. Chen, X. Wang, Y. Li, and X. Zhao,
  “Root cause analysis of power grid 5G network faults based on large language model,”
  in Proc. 28th Int. Conf. Comput. Supported Cooperative Work in Design (CSCWD),
  Compiegne, France, 2025, pp. 624–629,
  doi: 10.1109/CSCWD64889.2025.11033346.
* [14]

  M. Sana, N. Piovesan, A. De Domenico, Y. Kang, H. Zhang, M. Debbah, and F. Ayed,
  “Reasoning language models for root cause analysis in 5G wireless networks,”
  arXiv preprint arXiv:2507.21974, 2025. [Online]. Available: https://arxiv.org/abs/2507.21974
* [15]

  OpenAirInterface, “OpenAirInterface 5G core,” Official Website, 2024. [Online]. Available: https://openairinterface.org
* [16]

  Chaos Mesh, “Chaos Mesh: Cloud-native chaos engineering platform for Kubernetes,” Official Website, 2024. [Online]. Available: https://chaos-mesh.org
* [17]

  Cloud Native Computing Foundation (CNCF), “Kubernetes observability and logging best practices,” 2023. [Online]. Available: https://kubernetes.io/docs/concepts/cluster-administration/logging/

Generated on Mon Nov 24 15:52:28 2025 by [LaTeXML![Mascot Sammy](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAsAAAAOCAYAAAD5YeaVAAAAAXNSR0IArs4c6QAAAAZiS0dEAP8A/wD/oL2nkwAAAAlwSFlzAAALEwAACxMBAJqcGAAAAAd0SU1FB9wKExQZLWTEaOUAAAAddEVYdENvbW1lbnQAQ3JlYXRlZCB3aXRoIFRoZSBHSU1Q72QlbgAAAdpJREFUKM9tkL+L2nAARz9fPZNCKFapUn8kyI0e4iRHSR1Kb8ng0lJw6FYHFwv2LwhOpcWxTjeUunYqOmqd6hEoRDhtDWdA8ApRYsSUCDHNt5ul13vz4w0vWCgUnnEc975arX6ORqN3VqtVZbfbTQC4uEHANM3jSqXymFI6yWazP2KxWAXAL9zCUa1Wy2tXVxheKA9YNoR8Pt+aTqe4FVVVvz05O6MBhqUIBGk8Hn8HAOVy+T+XLJfLS4ZhTiRJgqIoVBRFIoric47jPnmeB1mW/9rr9ZpSSn3Lsmir1fJZlqWlUonKsvwWwD8ymc/nXwVBeLjf7xEKhdBut9Hr9WgmkyGEkJwsy5eHG5vN5g0AKIoCAEgkEkin0wQAfN9/cXPdheu6P33fBwB4ngcAcByHJpPJl+fn54mD3Gg0NrquXxeLRQAAwzAYj8cwTZPwPH9/sVg8PXweDAauqqr2cDjEer1GJBLBZDJBs9mE4zjwfZ85lAGg2+06hmGgXq+j3+/DsixYlgVN03a9Xu8jgCNCyIegIAgx13Vfd7vdu+FweG8YRkjXdWy329+dTgeSJD3ieZ7RNO0VAXAPwDEAO5VKndi2fWrb9jWl9Esul6PZbDY9Go1OZ7PZ9z/lyuD3OozU2wAAAABJRU5ErkJggg==)](http://dlmf.nist.gov/LaTeXML/)