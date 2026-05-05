6
2
0
2

n
a
J

3
1

]

C
D
.
s
c
[

2
v
6
2
5
7
0
.
1
0
6
2
:
v
i
X
r
a

January 14, 2026

MEGAFLOW: LARGE-SCALE DISTRIBUTED
ORCHESTRATION SYSTEM FOR THE AGENTIC ERA

Lei Zhang1,2∗, Mouxiang Chen3, Ruisheng Cao3, Jiawei Chen3, Fan Zhou3, Yiheng Xu3,
Jiaxi Yang1,2, Zeyao Ma3, Liang Chen3, Changwei Luo3, Kai Zhang3, Fan Yan3,
KaShun SHUM3, Jiajun Zhang3, Zeyu Cui3, Feng Hu3,
Junyang Lin3, Binyuan Hui3†, Min Yang1,2†
1 Shenzhen Institutes of Advanced Technology, Chinese Academy of Sciences
2 University of Chinese Academy of Sciences, 3 Alibaba Group
{lei.zhang2, min.yang}@siat.ac.cn, binyuan.hby@alibaba-inc.com

ABSTRACT

The rapid development of interactive and autonomous AI systems signals our
entry into the agentic era. Training and evaluating agents on complex agentic
tasks such as software engineering and computer use requires not only efficient
model computation but also sophisticated infrastructure capable of coordinating
vast agent-environment interactions. However, no open-source infrastructure can
effectively support large-scale training and evaluation on such complex agentic
tasks. To address this challenge, we present MegaFlow, a large-scale distributed
orchestration system that enables efficient scheduling, resource allocation, and
fine-grained task management for agent-environment workloads. MegaFlow ab-
stracts agent training infrastructure into three independent services (Model Ser-
vice, Agent Service, and Environment Service) that interact through unified inter-
faces, enabling independent scaling and flexible resource allocation across diverse
agent-environment configurations. In our agent training deployments, MegaFlow
successfully orchestrates tens of thousands of concurrent agent tasks while main-
taining high system stability and achieving efficient resource utilization. By en-
abling such large-scale agent training, MegaFlow addresses a critical infrastruc-
ture gap in the emerging agentic AI landscape.

Figure 1: The proposed three-service architecture for agent training. (left) The Environment Service
provides diverse interactive execution environments and returns feedback (observations, rewards,
termination signals) in response to actions. (middle) The Agent Service orchestrates interaction,
collects trajectories, and manages experiences. (right) The Model Service supports both inference
(returning policies from context) and training (updating from experiences).

1

INTRODUCTION

The rapid development of interactive and autonomous AI systems signals our entry into the agen-
tic era, where intelligent agents must be trained and evaluated on increasingly complex real-world
tasks (Wang et al., 2024a; Xi et al., 2025). This transformation is driven by remarkable advances in
large language models, reinforcement learning, and multi-agent coordination, enabling the develop-
ment of agents capable of sophisticated reasoning and planning across diverse domains (Dorri et al.,

∗Work done during an internship at Alibaba Qwen.
†Correspondence to Min Yang and Binyuan Hui.

1

Environment ServiceAgent ServiceModel ServiceActionFeedbackExperiencePolicy

January 14, 2026

2018). Training these agents on complex agentic tasks such as software engineering (Jimenez et al.,
2023) and computer use (Xie et al., 2024) requires not only efficient model computation but also
sophisticated infrastructure capable of orchestrating vast agent-environment interactions at unprece-
dented scale (Gao et al., 2024; Sun et al., 2025). The promise of large-scale agent training lies in its
potential to develop more capable and versatile AI systems through massive parallel training across
heterogeneous environments and tasks. Realizing this vision requires sophisticated infrastructure
capable of supporting large-scale agent training and evaluation. However, no existing infrastructure
can effectively support the large-scale training and evaluation demands of such complex agentic
tasks.

Traditional approaches to agent training work well for simple tasks such as single-turn function
calling (Patil et al.) and basic question answering (Mialon et al., 2023). Nonetheless, they fail to
address the unique challenges of orchestrating massive numbers of concurrent agent-environment
interactions required for effective training on complex multi-step tasks at scale. The core challenge
lies not merely in computational power (modern distributed computing frameworks have adequately
addressed model training and inference scalability) but in the complex coordination of dynamic,
interdependent processes that characterize large-scale agentic training workloads. Our experience
training agents on complex tasks such as software engineering and computer use automation re-
veals three critical infrastructure bottlenecks that exemplify the broader scalability challenges facing
large-scale agent training: (1) Security and Isolation Constraints: Complex agent training requires
containerized environments to provide secure, isolated execution contexts for agent-environment
interactions. However, security policies in typical training clusters prohibit the execution of ar-
bitrary containers, creating a fundamental incompatibility between large-scale agent training re-
(2) Storage Scalability Limitations: Each
quirements and existing computational infrastructure.
complex agent task instance requires corresponding containerized environments containing spe-
cific software dependencies and execution contexts. Even relatively modest datasets such as SWE-
bench (Jimenez et al., 2023) and SWE-Gym (Pan et al., 2024) require over 25TB of storage for
their associated container images. Storage requirements grow dramatically as training scales to
larger and more diverse task sets, creating prohibitive infrastructure costs and management over-
head. (3) Computational Throughput Bottlenecks: The resource-intensive nature of containerized
agent-environment interactions severely limits concurrent training throughput, preventing the mas-
sive parallelism necessary for effective large-scale agent training.

To address these fundamental infrastructure challenges, we present MegaFlow, a large-scale dis-
tributed orchestration system that enables efficient scheduling, resource allocation, and fine-grained
task management for agent training workloads. MegaFlow abstracts agent training infrastructure
into three independent services (Model Service, Agent Service, and Environment Service) that inter-
act through unified interfaces, enabling independent scaling and flexible resource allocation across
diverse agent-environment configurations. The Environment Service provides diverse interactive ex-
ecution environments and returns feedback (observations, rewards, termination signals) in response
to actions. The Agent Service orchestrates interactions, collects experiences, and manages experi-
ence data throughout the training process. The Model Service supports both inference (returning
policies from context) and training (updating model parameters from collected experiences). While
existing approaches treat agent training as monolithic computational tasks, this modular architecture
enables independent optimization and scaling of each component according to its specific computa-
tional requirements. The key insight underlying MegaFlow is that the primary scalability bottleneck
in large-scale agent training lies not in model computation (which existing distributed frameworks
handle well) but in the efficient coordination of dynamic agent-environment interactions. By pro-
viding unified APIs for the orchestration of these three services, MegaFlow enables researchers and
practitioners to focus on algorithmic development rather than infrastructure complexity.

This work makes the following key contributions to large-scale agent training infrastructure:

• Overcoming Security and Isolation Constraints: We address the fundamental incom-
patibility between agent training requirements and cluster security policies by migrating
containerized workloads to elastic cloud compute services. This enables secure, isolated
agent execution without requiring specialized cluster configurations or compromising ex-
isting security frameworks.

• Solving Storage Scalability Limitations: We implement on-demand container image pro-
visioning using cloud registry services with high-bandwidth internal network access, elim-

2

January 14, 2026

inating the need for massive local storage. This approach transforms storage requirements
from a fixed infrastructure cost to an elastic, usage-based model that scales efficiently with
training demands.

• Breaking Computational Throughput Bottlenecks: We introduce a distributed orches-
tration system that coordinates thousands of lightweight instances rather than relying on
high-specification machines. Our many-small-instances approach achieves superior re-
source utilization and eliminates the availability constraints that limit traditional centralized
methods to hundreds of concurrent tasks.

• System Performance Validation: We design and implement MegaFlow, a three-service
architecture that enables independent scaling of model serving, agent coordination, and
environment provisioning. Our evaluation demonstrates 32% cost reduction and consistent
scaling to tens of thousands of concurrent tasks, with production validation across over 2
million agent training executions.

2 MEGAFLOW

(bottom) The Model Service provides inference and
Figure 2: The architecture of MegaFlow.
training capabilities through various engines and distributed frameworks. (middle) The Agent Ser-
vice coordinates execution strategies, integrates with agent frameworks, and manages experience
feedback loops. (top) The Environment Service provides containerized execution environments and
handles distributed task scheduling.

2.1 SYSTEM OVERVIEW

Figure 2 illustrates the overall architecture of MegaFlow’s three-service ecosystem. The system
operates through three independent services, each with specialized responsibilities:

Model Service This service handles the computational aspects of agent intelligence, providing
inference capabilities through various inference engines such as Transformers (Wolf et al., 2020),
vLLM (Kwon et al., 2023), and SGLang (Zheng et al., 2024), while supporting training operations
via distributed training frameworks including VeRL (Sheng et al., 2025), FSDP (Zhao et al., 2023),
and Megatron (Shoeybi et al., 2019). It focuses purely on model computation and parameter updates,
abstracting away the complexities of agent-environment interactions.

3

Task SelectorDistributed SchedulerDistributed Cloud Compute ServiceVirtualized Agent EnvironmentEvent BridgeSend Cloud EventsDistributed StorageRollout OutputsSubmit TaskTrajectories and RewardsRollout RequestsvLLMSGLangTransformersFSDPMegatronVeRLInference ServiceTraining ServiceScaﬀold SelectorOpenHandsSWE-AgentQwen CodeNASObject StorageMongoDBModel Service API ResponsesModel Service API CallsRedisAgent OutputsQuery StatesReceive Cloud EventsUpdate StatesJanuary 14, 2026

Agent Service This service acts as the intelligent coordinator that manages agent execution strate-
gies based on task requirements.
It integrates with various agent frameworks such as Open-
Hands (Wang et al., 2024b), SWE-Agent (Yang et al., 2024a), and Qwen Code (Yang et al., 2025a)
for different task types (training, evaluation, or data synthesis) and coordinates rollout execution
across specified datasets. The Agent Service processes rollout outputs, aggregating evaluation met-
rics and feeding experience data back to the Model Service for training iterations.

Environment Service This service represents the most resource-intensive component, responsible
for the physical execution of agent tasks. It queues tasks in a distributed system and employs sophis-
ticated scheduling to monitor resource availability and dispatch tasks to cloud compute instances.
Each instance executes multiple concurrent agent tasks through containerized environments that
provide isolated execution contexts for agent-environment interactions.

MegaFlow Orchestration MegaFlow orchestrates the interaction between these three services
through unified APIs. It manages the complete lifecycle of agent training: from receiving requests
and provisioning environments, to monitoring progress through event-driven updates, and collecting
results for downstream processing. The system leverages cloud-native services for elastic compute,
real-time monitoring, and distributed storage. While our current implementation is built on Alibaba
Cloud, the abstracted APIs enable straightforward migration to other major cloud providers such as
Amazon Web Services, Microsoft Azure, and Google Cloud Platform.

This architecture enables: (1) elastic scaling through dynamic resource allocation, (2) fault tolerance
via event-driven monitoring, (3) resource efficiency through intelligent scheduling, and (4) service
isolation allowing independent optimization of each component.

2.2 KEY DESIGN PRINCIPLES

The design of MegaFlow is guided by four key principles that reflect our understanding of large-
scale agent training requirements and distinguish our approach from traditional distributed systems.

Elastic Resource Strategy MegaFlow adopts a many-small-instances approach with standardized
compute configurations, providing superior elasticity and cost optimization compared to few-large-
instances models. This design aligns with containerized agent workload characteristics and enables
rapid resource provisioning and deallocation.

Hybrid Execution Model The system implements dual execution modes: ephemeral execution
for perfect task isolation and persistent execution for resource efficiency. This hybrid approach
optimizes both reliability and resource utilization based on task characteristics.

Event-Driven Coordination Rather than complex consensus protocols, MegaFlow employs
event-driven coordination with distributed state management, eliminating polling overhead while
providing strong consistency guarantees for resource allocation and task scheduling.

Specialized Component Delegation MegaFlow strategically delegates domain-specific opera-
tions to specialized systems (agent frameworks for container orchestration, cloud services for storage
and monitoring), focusing on the unique challenges of agent-environment coordination rather than
reimplementing general-purpose solutions.

2.3 ARCHITECTURE DESIGN

Based on these design principles, the MegaFlow architecture implements five core components that
work in concert to provide scalable, fault-tolerant orchestration of agent training workloads.

Task Scheduler At the heart of MegaFlow lies a high-performance asynchronous scheduler that
enables massive concurrency for task processing. The system implements a FIFO scheduling policy,
which proves sufficient for our workloads while maintaining simplicity and predictability.

The scheduler intelligently handles two distinct task categories with optimized resource allocation
strategies. For Ephemeral Tasks, the system follows an ephemeral compute model: upon receiving
a task request, a dedicated compute instance is provisioned, executes the single task, and is imme-
diately deallocated, eliminating resource contention and providing perfect isolation. For Persistent

4

January 14, 2026

Tasks, which require sustained execution, the scheduler maintains a pool of persistent compute in-
stances and employs pool-based allocation, efficiently reusing resources while maintaining isolation
through containerization.

Resource Manager The resource management subsystem employs distributed coordination mech-
anisms to maintain real-time visibility into system state and resource availability. Rather than im-
plementing complex resource monitoring and allocation algorithms, our design adopts a uniform
resource allocation strategy with standardized compute instances. This standardization simplifies
scheduling decisions, improves resource predictability, and aligns with containerized workload char-
acteristics where each instance typically executes a single agent task.

The system implements sophisticated concurrency control through a three-tier limiting mechanism:
(1) User-specified parameters control the rate of Model Service API calls, preventing downstream
bottlenecks; (2) Distributed semaphores ensure that task execution never exceeds available compute
capacity; and (3) Administrative quotas provide control over resource usage, preventing system
abuse while enabling fair resource sharing.

Environment Manager Our environment management strategy demonstrates a key architectural
insight: by delegating container lifecycle operations to proven open-source agent frameworks,
MegaFlow focuses on what it does best (orchestration and coordination). The system pre-provisions
all required container images in cloud registry services, enabling rapid deployment through high-
bandwidth internal network access.

Environment isolation is achieved through a layered approach: each compute instance provides
resource isolation, while containerization within instances provides process and filesystem isolation.
This dual-layer isolation ensures that agent operations (including code editing, command execution,
and file system modifications) remain completely contained within their designated environments.

Event-Driven Monitoring MegaFlow employs cloud event services to implement reactive sys-
tem behavior through two critical event streams.
Instance lifecycle events enable the system to
track compute instance state transitions, ensuring tasks are only dispatched to fully operational in-
stances. Task completion events provide real-time notification of task outcomes, enabling immediate
resource reclamation and result processing.

This event-driven architecture eliminates the need for expensive polling operations while providing
near-instantaneous response to state changes. The system supplements event notifications with direct
API calls for detailed task execution information, striking an optimal balance between real-time
responsiveness and comprehensive monitoring.

Data Persistence The system architecture separates concerns between operational data and result
artifacts through specialized storage systems. Operational metadata (including task specifications,
execution state, and compute instance information) is managed through document databases with
schema validation and type safety. Task queues are implemented using in-memory storage systems,
leveraging high-performance operations for rapid task dispatch.

Agent execution artifacts are persisted to cloud object storage, providing durable, scalable storage
for trajectory data, evaluation results, and training artifacts. This separation allows the Agent Service
to retrieve results asynchronously while maintaining system responsiveness during peak execution
periods.

3 EVALUATION

We evaluate MegaFlow’s performance on large-scale complex agent training tasks, focusing on
multi-step software engineering scenarios that require containerized environments and sustained
agent-environment interactions. These tasks present unique infrastructure challenges due to their
need for sophisticated orchestration at concurrent execution scale. Since no existing infrastructure
provides comparable functionality for such agent training orchestration, our evaluation compares
MegaFlow against traditional high-specification centralized approaches and analyzes system perfor-
mance characteristics.

5

January 14, 2026

Figure 3: Throughput scaling and cost comparison between MegaFlow and centralized approaches.
(Left) Total execution time showing MegaFlow’s consistent performance versus centralized degra-
dation. (Right) Total cost comparison with 32% cost reduction at 2,000 concurrent tasks. Data
represents bootstrap sampling from over 130,000 production records.

3.1 EXPERIMENTAL SETUP
Task Definition and Datasets We evaluate MegaFlow using software engineering agent training
tasks that require containerized environments and sustained agent-environment interactions. Our
evaluation leverages large-scale software engineering datasets (Jimenez et al., 2023; Pan et al., 2024;
Zhang et al., 2025a; Yang et al., 2025b; Zan et al., 2025; Zhang et al., 2025b), conducting exper-
iments with workloads scaling up to tens of thousands of concurrent tasks to demonstrate system
performance at scale.

Agent Framework Compatibility MegaFlow supports major agent frameworks including SWE-
Agent (Yang et al., 2024a), OpenHands (Wang et al., 2024b), Mini-SWE-Agent (Yang et al., 2024a),
Qwen Code (Yang et al., 2025a), and Claude Code (Anthropic, 2025) across all evaluated benchmark
suites, validating our architecture’s generalizability and broad compatibility with existing tools.

Baseline Configurations Since no comparable infrastructure exists for large-scale agent training
orchestration, we establish baselines through systematic comparison of execution strategies:

• High-Spec Centralized: High-specification machines (208-core CPU, 3TB memory, 1
Gbps network bandwidth) with maximum sustainable parallelism of 50 concurrent tasks
per instance.

• MegaFlow Distributed: Standardized 8-core, 16GB instances (100 Mbps network band-
width each) with dynamic elastic scaling, where each instance handles 1 concurrent task.

Data Collection and Analysis Our evaluation is based on production deployment records com-
prising over 130,000 ephemeral execution tasks and over 2 million persistent execution tasks. Ex-
periments utilized up to 40 high-specification instances for centralized approaches and up to 10,000
standardized instances for distributed approaches. Performance metrics are computed using boot-
strap sampling (100 iterations per data point) with 95% confidence intervals. All experiments were
conducted on Alibaba Cloud. Unless otherwise stated, we use ecs.re6.52xlarge instances for high-
specification centralized approaches and ecs.c8a.2xlarge, ecs.c8i.2xlarge instances for distributed
approaches.

3.2 THROUGHPUT AND SCALABILITY ANALYSIS

We evaluate MegaFlow’s scalability by measuring system performance across varying workload
sizes, examining both throughput and latency characteristics under different concurrency levels.

Performance and Scalability Figure 3 demonstrates MegaFlow’s superior characteristics com-
pared to traditional centralized approaches. MegaFlow maintains consistent execution times of ap-
proximately 100 minutes across 1 to 10,000 tasks, while high-specification centralized methods
exhibit degradation from 100 to 110 minutes due to resource contention bottlenecks. Centralized
approaches suffer from network bandwidth congestion during container image pulls and resource

6

Total Execution Time (minutes)90100110120130Number of Tasks1105010050010002000500010000High-Spec CentralizedMegaFlow DistributedTotal Cost (USD)032064096012801600Number of Tasks11050100500100020001,005.8502.9251.350.225.15.10.51,469.6734.8367.473.436.730.630.6High-Spec CentralizedMegaFlow DistributedJanuary 14, 2026

Figure 4: Resource utilization patterns across normalized execution time. (Left) CPU utilization:
centralized peak at 25% versus MegaFlow’s stable 5-10%. (Right) Memory utilization: centralized
peak at 50% versus MegaFlow’s consistent 12%. Shaded areas represent 95% confidence intervals.

competition during initialization. MegaFlow’s distributed architecture eliminates these bottlenecks
by providing dedicated resources per task.

The centralized approach faces fundamental scalability constraints, limited to 2,000 concurrent tasks
due to instance availability (40 high-specification instances maximum). MegaFlow’s standardized
instances enabled provisioning up to 10,000 instances, demonstrating superior elastic scaling capa-
bilities.

Cost Efficiency At 2,000 tasks, MegaFlow achieves 32% cost reduction (1,005 vs 1,470 USD),
with cost advantages increasing at larger scales. Beyond direct savings, MegaFlow eliminates re-
source availability constraints that prevent traditional methods from scaling to large workloads.

3.3 RESOURCE UTILIZATION ANALYSIS

We analyze resource utilization patterns throughout task execution lifecycles to evaluate the effi-
ciency of different architectural approaches. Figure 4 presents CPU and memory utilization rates
across normalized execution time for both approaches.

Utilization Pattern Analysis The resource utilization patterns reveal fundamental differences be-
tween centralized and distributed approaches. High-specification centralized instances exhibit pro-
nounced resource usage spikes, with CPU utilization peaking at 25% during the initial 30% of
execution time before declining to near-zero levels. Memory utilization follows a similar pattern,
reaching 50% peak usage during mid-execution (20-40% of total time) then dropping sharply.

In contrast, MegaFlow’s distributed architecture maintains consistent resource utilization throughout
execution cycles. CPU utilization remains stable at 5-10% across the entire execution period, while
memory utilization maintains approximately 12% with minimal variation.

Resource Efficiency Implications The contrasting utilization patterns highlight significant effi-
ciency differences. Centralized approaches demonstrate typical ”bursty” resource consumption with
substantial idle periods, leading to poor overall resource efficiency despite high-specification hard-
ware. The large confidence intervals in centralized approaches indicate high variability in resource
demand, making capacity planning challenging.

MegaFlow’s stable utilization patterns with narrow confidence intervals demonstrate predictable
resource consumption, enabling more efficient capacity planning and resource allocation. While
individual instances operate at lower peak utilization rates, the distributed model achieves better
overall resource efficiency through consistent utilization across the execution lifecycle.

7

Utilization Rate (%)0.016.032.048.064.080.0Normalized Time (0-100% of total execution)0.10.20.30.40.50.60.70.80.91.0High-spec MemoryMegaFlow MemoryUtilization Rate (%)0.010.020.030.040.050.0Normalized Time (0-100% of total execution)0.10.20.30.40.50.60.70.80.91.0High-spec CPUMegaFlow CPUJanuary 14, 2026

Figure 5: End-to-end latency breakdown and environment startup scaling comparison. (Left) Total
execution times: MegaFlow Persistent (75 min), Ephemeral (90 min), and High-Spec Centralized
(110 min). (Right) Environment startup time scaling showing centralized degradation (1-13 min)
versus MegaFlow’s stable performance.

3.4 END-TO-END LATENCY ANALYSIS

We analyze the complete task execution pipeline to identify performance bottlenecks and validate
our hybrid execution model design. Figure 5 presents latency breakdown across different execution
phases and environment startup scaling characteristics.

Latency Breakdown Analysis The latency decomposition reveals significant differences in ex-
ecution efficiency across approaches. MegaFlow’s persistent execution mode achieves the lowest
total latency at approximately 75 minutes, with minimal infrastructure overhead. The ephemeral
execution mode requires approximately 90 minutes total, with additional environment startup costs,
while high-specification centralized approaches exhibit the highest latency at 110 minutes due to
resource contention across all execution phases.

Task execution represents the dominant component of total latency across all approaches, but in-
frastructure overheads vary substantially. Centralized approaches suffer from extended submission,
scheduling, and environment startup phases due to resource competition and coordination bottle-
necks.

Environment Startup Scaling Environment startup times demonstrate critical scalability differ-
ences between execution strategies. High-specification centralized approaches exhibit severe startup
time degradation, increasing from 1 minute for single tasks to 13 minutes at 1,000 concurrent tasks
due to resource contention during container image pulls and initialization. MegaFlow’s ephemeral
mode shows modest startup time growth from 1 to 6 minutes, while persistent execution maintains
consistently low startup times below 1 minute across all concurrency levels through environment
reuse.

The scaling patterns reveal multiple bottleneck sources. The modest increase in MegaFlow’s
ephemeral startup times suggests that cloud container registry services experience some perfor-
mance degradation under high concurrent pull requests, but remain relatively stable. However, the
dramatic startup time increase in centralized approaches indicates that the primary bottleneck lies
in local resource constraints (network bandwidth limitations and resource contention within high-
specification instances) rather than cloud service limitations. This analysis reinforces the effective-
ness of MegaFlow’s distributed approach in avoiding local resource bottlenecks through dedicated
per-task resource allocation.

Hybrid Execution Model Validation These results validate our hybrid execution model design
principle. Persistent execution provides optimal performance for sustained workloads through envi-
ronment reuse, while ephemeral execution offers better isolation guarantees at moderate overhead.
The ability to select execution modes based on task characteristics enables MegaFlow to optimize
both performance and resource utilization according to specific workload requirements.

8

Environment Startup Time (minutes)48121620Number of Tasks110501005001000High-Spec CentralizedMegaFlow EphemeralMegaFlow PersistentHigh-Spec CentralizedMegaFlow EphemeralMegaFlow PersistentAverage Task Latency (minutes)024487296120SubmissionSchedulingEnvironment StartupTask ExecutionJanuary 14, 2026

3.5 DISCUSSION

Our evaluation demonstrates that MegaFlow successfully addresses the scalability challenges of
large-scale agent training through distributed orchestration and hybrid execution models. The results
validate our core design principles and provide several key insights for agent training infrastructure.

The many-small-instances approach achieves superior cost efficiency (32% reduction) while main-
taining consistent performance, contrasting with centralized methods that suffer from resource con-
tention bottlenecks. Resource utilization analysis reveals that stable, predictable consumption pat-
terns enable more efficient capacity planning than bursty high-peak usage, challenging conventional
assumptions about resource optimization in agent training systems.

Our bottleneck analysis identifies coordination overhead rather than raw computational power as
the primary scalability constraint, with the distinction between cloud service limitations and local
resource constraints providing important design guidance. MegaFlow’s broad compatibility across
agent frameworks validates the practical value of infrastructure-level solutions for the research com-
munity.

Future work should explore orchestration of multi-environment agent tasks with complex service
dependencies, potentially leveraging container orchestration paradigms like Kubernetes (Kubernetes
Project, 2014) for dependency management. Additional directions include dynamic execution mode
switching and multi-cloud deployment strategies to further enhance system flexibility.

4 RELATED WORK

Our work intersects several research areas, including distributed systems orchestration, container-
ization technologies, and infrastructure for AI workloads. We briefly review the most relevant prior
work in each area, with additional comprehensive coverage provided in Appendix B.

Distributed Container Orchestration Traditional container orchestration systems like Kuber-
netes (Kubernetes Project, 2014; Verma et al., 2015; Burns et al., 2016), Docker Swarm (Docker,
2025), and Apache Mesos (Mesos, 2025) focus on general-purpose workload management across
distributed clusters. While these systems provide powerful abstractions for resource allocation and
service discovery, they are not optimized for the unique characteristics of agent training workloads,
such as rapid environment provisioning, heterogeneous execution requirements, and tight integration
with model serving infrastructure.

Cloud-Native AI Infrastructure Systems like Kubeflow (Kubeflow Project, 2018), MLflow (Za-
haria et al., 2018; Chen et al., 2020), and Ray (Moritz et al., 2018) have advanced machine learning
infrastructure by providing distributed training, model serving, and workflow orchestration capabil-
ities. However, these systems primarily target traditional ML pipelines rather than interactive agent
training workloads that require dynamic environment creation, containerized execution contexts,
and complex agent-environment interaction patterns.

Multi-Agent System Infrastructure Prior work on multi-agent systems has largely focused on
coordination algorithms, communication protocols, and simulation environments (Sun et al., 2025).
While recent efforts have explored infrastructure for LLM-based agents (Tran et al., 2025), these
works primarily address single-agent scenarios or small-scale interactions. The infrastructure chal-
lenges of executing thousands of concurrent agent training tasks across distributed environments
remain largely unaddressed.

Large-Scale AI Training Systems Distributed training frameworks such as Horovod (Sergeev &
Del Balso, 2018), FairScale (Facebook Research, 2020), and Megatron-LM (Shoeybi et al., 2019)
have demonstrated the feasibility of coordinating AI workloads across large clusters. However, these
systems focus on model training rather than agent execution, and their synchronous, tightly-coupled
architectures are poorly suited to the asynchronous, loosely-coupled nature of agent-environment
interactions.

Unlike existing approaches, MegaFlow provides a specialized three-service architecture that decou-
ples model serving, agent coordination, and environment provisioning, enabling independent scaling
and optimization for large-scale agent training workloads.

9

January 14, 2026

5 CONCLUSION

In this paper, we presented MegaFlow, a large-scale distributed orchestration system that addresses
the fundamental scalability challenges facing agent training infrastructure through a three-service
architecture that decouples Model Service, Agent Service, and Environment Service. Through com-
prehensive evaluation using over 130,000 production task records, we demonstrated that MegaFlow
overcomes critical infrastructure bottlenecks, achieving 32% cost reduction and consistent perfor-
mance scaling to 10,000 concurrent tasks compared to traditional centralized approaches. By estab-
lishing unified APIs and eliminating orchestration bottlenecks, MegaFlow provides a production-
ready foundation for large-scale agent training research and enables the development of sophisti-
cated AI agents at unprecedented scale.

REFERENCES

Anthropic. Claude code. https://claude.com/product/claude-code, 2025.

Ibragim Badertdinov, Alexander Golubev, Maksim Nekrashevich, Anton Shevtsov, Simon Karasik,
Andrei Andriushchenko, Maria Trofimova, Daria Litvintseva, and Boris Yangel. Swe-rebench:
An automated pipeline for task collection and decontaminated evaluation of software engineering
agents. arXiv preprint arXiv:2505.20411, 2025.

Brendan Burns, Brian Grant, David Oppenheimer, Eric Brewer, and John Wilkes. Borg, omega, and

kubernetes. Communications of the ACM, 59(5):50–57, 2016.

Andrew Chen, Andy Chow, Aaron Davidson, Arjun DCunha, Ali Ghodsi, Sue Ann Hong, Andy
Konwinski, Clemens Mewald, Siddharth Murching, Tomas Nykodym, et al. Developments in
In Proceedings of the fourth
mlflow: A system to accelerate the machine learning lifecycle.
international workshop on data management for end-to-end machine learning, pp. 1–4, 2020.

Xiang Deng, Yu Gu, Boyuan Zheng, Shijie Chen, Sam Stevens, Boshi Wang, Huan Sun, and Yu Su.
Mind2web: Towards a generalist agent for the web. Advances in Neural Information Processing
Systems, 36:28091–28114, 2023.

Docker. Docker swarm. https://docs.docker.com/engine/swarm/, 2025.

Ali Dorri, Salil S Kanhere, and Raja Jurdak. Multi-agent systems: A survey. Ieee Access, 6:28573–

28593, 2018.

Facebook Research. Fairscale: A general purpose modular pytorch library for high performance and
large scale training. https://github.com/facebookresearch/fairscale, 2020.
Accessed: 2025-01-01.

Chen Gao, Xiaochong Lan, Nian Li, Yuan Yuan, Jingtao Ding, Zhilun Zhou, Fengli Xu, and Yong
Li. Large language models empowered agent-based modeling and simulation: A survey and
perspectives. Humanities and Social Sciences Communications, 11(1):1–24, 2024.

Carlos E Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, and Karthik
Narasimhan. Swe-bench: Can language models resolve real-world github issues? arXiv preprint
arXiv:2310.06770, 2023.

Kubeflow Project. Kubeflow: Machine learning toolkit for kubernetes.

https://www.

kubeflow.org, 2018.

Kubernetes Project. Kubernetes, 2014. URL http://kubernetes.io.

Woosuk Kwon, Zhuohan Li, Siyuan Zhuang, Ying Sheng, Lianmin Zheng, Cody Hao Yu, Joseph
Gonzalez, Hao Zhang, and Ion Stoica. Efficient memory management for large language model
serving with pagedattention. In Proceedings of the 29th symposium on operating systems princi-
ples, pp. 611–626, 2023.

Apache Mesos. Apache mesos. https://mesos.apache.org, 2025.

10

January 14, 2026

Gr´egoire Mialon, Cl´ementine Fourrier, Thomas Wolf, Yann LeCun, and Thomas Scialom. Gaia:
In The Twelfth International Conference on Learning

a benchmark for general ai assistants.
Representations, 2023.

Philipp Moritz, Robert Nishihara, Stephanie Wang, Alexey Tumanov, Richard Liaw, Eric Liang,
Melih Elibol, Zongheng Yang, William Paul, Michael I Jordan, et al. Ray: A distributed frame-
work for emerging {AI} applications. In 13th USENIX symposium on operating systems design
and implementation (OSDI 18), pp. 561–577, 2018.

Jiayi Pan, Xingyao Wang, Graham Neubig, Navdeep Jaitly, Heng Ji, Alane Suhr, and Yizhe
arXiv preprint

Zhang. Training software engineering agents and verifiers with swe-gym.
arXiv:2412.21139, 2024.

Shishir G Patil, Huanzhi Mao, Fanjia Yan, Charlie Cheng-Jie Ji, Vishnu Suresh, Ion Stoica, and
Joseph E Gonzalez. The berkeley function calling leaderboard (bfcl): From tool use to agen-
tic evaluation of large language models. In Forty-second International Conference on Machine
Learning.

Alibaba Qwen Team. Qwen-agent. https://github.com/QwenLM/Qwen-Agent, 2025.

Alexander Sergeev and Mike Del Balso. Horovod: fast and easy distributed deep learning in tensor-

flow. arXiv preprint arXiv:1802.05799, 2018.

Guangming Sheng, Chi Zhang, Zilingfeng Ye, Xibin Wu, Wang Zhang, Ru Zhang, Yanghua Peng,
Haibin Lin, and Chuan Wu. Hybridflow: A flexible and efficient rlhf framework. In Proceedings
of the Twentieth European Conference on Computer Systems, pp. 1279–1297, 2025.

Mohammad Shoeybi, Mostofa Patwary, Raul Puri, Patrick LeGresley, Jared Casper, and Bryan
Catanzaro. Megatron-lm: Training multi-billion parameter language models using model par-
allelism. arXiv preprint arXiv:1909.08053, 2019.

Lijun Sun, Yijun Yang, Qiqi Duan, Yuhui Shi, Chao Lyu, Yu-Cheng Chang, Chin-Teng Lin, and
Yang Shen. Multi-agent coordination across diverse applications: A survey. arXiv preprint
arXiv:2502.14743, 2025.

The Terminal-Bench Team. Terminal-bench: A benchmark for ai agents in terminal environments,

Apr 2025. URL https://github.com/laude-institute/terminal-bench.

Khanh-Tung Tran, Dung Dao, Minh-Duong Nguyen, Quoc-Viet Pham, Barry O’Sullivan, and
Hoang D Nguyen. Multi-agent collaboration mechanisms: A survey of llms. arXiv preprint
arXiv:2501.06322, 2025.

Abhishek Verma, Luis Pedrosa, Madhukar Korupolu, David Oppenheimer, Eric Tune, and John
Wilkes. Large-scale cluster management at google with borg. In Proceedings of the tenth euro-
pean conference on computer systems, pp. 1–17, 2015.

Lei Wang, Chen Ma, Xueyang Feng, Zeyu Zhang, Hao Yang, Jingsen Zhang, Zhiyuan Chen, Jiakai
Tang, Xu Chen, Yankai Lin, et al. A survey on large language model based autonomous agents.
Frontiers of Computer Science, 18(6):186345, 2024a.

Xingyao Wang, Boxuan Li, Yufan Song, Frank F Xu, Xiangru Tang, Mingchen Zhuge, Jiayi Pan,
Yueqi Song, Bowen Li, Jaskirat Singh, et al. Openhands: An open platform for ai software
developers as generalist agents. arXiv preprint arXiv:2407.16741, 2024b.

Thomas Wolf, Lysandre Debut, Victor Sanh, Julien Chaumond, Clement Delangue, Anthony Moi,
Pierric Cistac, Tim Rault, Remi Louf, Morgan Funtowicz, et al. Transformers: State-of-the-art
In Proceedings of the 2020 conference on empirical methods in
natural language processing.
natural language processing: system demonstrations, pp. 38–45, 2020.

Zhiheng Xi, Wenxiang Chen, Xin Guo, Wei He, Yiwen Ding, Boyang Hong, Ming Zhang, Junzhe
Wang, Senjie Jin, Enyu Zhou, et al. The rise and potential of large language model based agents:
A survey. Science China Information Sciences, 68(2):121101, 2025.

11

January 14, 2026

Tianbao Xie, Danyang Zhang, Jixuan Chen, Xiaochuan Li, Siheng Zhao, Ruisheng Cao, Toh J Hua,
Zhoujun Cheng, Dongchan Shin, Fangyu Lei, et al. Osworld: Benchmarking multimodal agents
for open-ended tasks in real computer environments. Advances in Neural Information Processing
Systems, 37:52040–52094, 2024.

An Yang, Anfeng Li, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu,
arXiv preprint

Chang Gao, Chengen Huang, Chenxu Lv, et al. Qwen3 technical report.
arXiv:2505.09388, 2025a.

John Yang, Carlos E Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan,
and Ofir Press. Swe-agent: Agent-computer interfaces enable automated software engineering.
Advances in Neural Information Processing Systems, 37:50528–50652, 2024a.

John Yang, Carlos E Jimenez, Alex L Zhang, Kilian Lieret, Joyce Yang, Xindi Wu, Ori Press,
Niklas Muennighoff, Gabriel Synnaeve, Karthik R Narasimhan, et al. Swe-bench multimodal:
Do ai systems generalize to visual software domains? arXiv preprint arXiv:2410.03859, 2024b.

John Yang, Kilian Leret, Carlos E Jimenez, Alexander Wettig, Kabir Khandpur, Yanzhe Zhang,
Binyuan Hui, Ofir Press, Ludwig Schmidt, and Diyi Yang. Swe-smith: Scaling data for software
engineering agents. arXiv preprint arXiv:2504.21798, 2025b.

Shunyu Yao, Noah Shinn, Pedram Razavi, and Karthik Narasimhan. tau-bench: A benchmark for

tool-agent-user interaction in real-world domains. arXiv preprint arXiv:2406.12045, 2024.

Matei Zaharia, Andrew Chen, Aaron Davidson, Ali Ghodsi, Sue Ann Hong, Andy Konwinski, Sid-
dharth Murching, Tomas Nykodym, Paul Ogilvie, Mani Parkhe, et al. Accelerating the machine
learning lifecycle with mlflow. IEEE Data Eng. Bull., 41(4):39–45, 2018.

Daoguang Zan, Zhirong Huang, Wei Liu, Hanwu Chen, Linhao Zhang, Shulin Xin, Lu Chen, Qi Liu,
Xiaojian Zhong, Aoyan Li, et al. Multi-swe-bench: A multilingual benchmark for issue resolving.
arXiv preprint arXiv:2504.02605, 2025.

Lei Zhang, Jiaxi Yang, Min Yang, Jian Yang, Mouxiang Chen, Jiajun Zhang, Zeyu Cui, Binyuan
Hui, and Junyang Lin. Swe-flow: Synthesizing software engineering data in a test-driven manner.
arXiv preprint arXiv:2506.09003, 2025a.

Linghao Zhang, Shilin He, Chaoyun Zhang, Yu Kang, Bowen Li, Chengxing Xie, Junhao Wang,
arXiv preprint

Maoquan Wang, Yufan Huang, Shengyu Fu, et al. Swe-bench goes live!
arXiv:2505.23419, 2025b.

Yanli Zhao, Andrew Gu, Rohan Varma, Liang Luo, Chien-Chin Huang, Min Xu, Less Wright,
Hamid Shojanazeri, Myle Ott, Sam Shleifer, et al. Pytorch fsdp: experiences on scaling fully
sharded data parallel. arXiv preprint arXiv:2304.11277, 2023.

Chujie Zheng, Shixuan Liu, Mingze Li, Xiong-Hui Chen, Bowen Yu, Chang Gao, Kai Dang,
Yuqiong Liu, Rui Men, An Yang, et al. Group sequence policy optimization. arXiv preprint
arXiv:2507.18071, 2025.

Lianmin Zheng, Liangsheng Yin, Zhiqiang Xie, Chuyue Livia Sun, Jeff Huang, Cody Hao Yu, Shiyi
Cao, Christos Kozyrakis, Ion Stoica, Joseph E Gonzalez, et al. Sglang: Efficient execution of
structured language model programs. Advances in neural information processing systems, 37:
62557–62583, 2024.

Shuyan Zhou, Frank F Xu, Hao Zhu, Xuhui Zhou, Robert Lo, Abishek Sridhar, Xianyi Cheng,
Tianyue Ou, Yonatan Bisk, Daniel Fried, et al. Webarena: A realistic web environment for build-
ing autonomous agents. arXiv preprint arXiv:2307.13854, 2023.

12

January 14, 2026

A DEFINITIONS

This section provides formal definitions for the key concepts underlying MegaFlow’s architecture
and the agent training tasks it supports.

Definition A.1: Three-Service Architecture

An agentic system is decomposed into three modular services with well-defined interfaces:
Model Service (M): Provides policy inference and training capabilities.

Inference: Minfer : S × Θ → Π(A)
Training: Mtrain : D × Θ → Θ′

(1)

(2)

where S is the state space, Θ represents model parameters, Π(A) is a policy distribution over
actions, and D is training data.
Agent Service (A): Manages agent coordination and experience collection.

A : T × M → D × R

(3)

where T is an agent task specification, and the output includes collected experiences D and
execution results R.
Environment Service (E): Provides interactive environments and feedback signals.

E : Espec × A → S ′ × R

(4)

where Espec is the environment specification, A is an action, and the output includes the next
state S ′ and reward signal R.

To support large-scale execution of agent tasks across distributed infrastructure, MegaFlow decom-
poses the traditional monolithic agent system into three specialized services. This architectural sep-
aration enables independent scaling and optimization of each component while maintaining clear
interfaces for coordination.

Definition A.2: Agent Task

An Agent Task is an interactive problem-solving environment defined as a six-tuple

T = (E, D, G, S, A, T ),

where:

• E is the environment specification that defines the interactive context in which the agent
operates, including containerized execution environments, software repositories, or sim-
ulation parameters;

• D is the task description that provides natural language instructions, problem state-

ments, or objectives that guide the agent’s behavior;

• G is the goal and evaluation criteria that specify success conditions, reward functions,

or metrics used to assess task completion and performance;

• S is the state space representing all possible configurations of the environment and agent

context during task execution;

• A is the action space defining the set of permissible operations the agent can perform

within the environment;

• T : S × A → S is the transition function that specifies how the task state evolves
given an agent action a ∈ A, capturing the deterministic or stochastic dynamics of the
environment.

An agent task execution produces a trajectory τ = {(s0, a0), (s1, a1), . . . , (sT , aT )} where
st ∈ S and at ∈ A. Task termination is controlled by the agent framework, either through
explicit completion decisions or upon reaching the maximum step limit. During execution, the
environment processes each action to generate state transitions, while the final reward signal
R = G(τ ) is computed only upon task completion using the complete trajectory.

13

January 14, 2026

Table 1: Compatibility matrix of agent frameworks with software engineering datasets

Dataset

SWE-bench
SWE-Gym
SWE-rebench
SWE-smith
SWE-bench Multilingual
Multi-SWE-Bench
Multi-SWE-RL
SWE-bench-live
SWE-Flow
Terminal-bench

SWE-Agent OpenHands Mini-SWE-Agent Qwen Code Claude Code
✔
✔
✔
✔
✔
✔
✔
✔
✔
✔

✔
✔
✔
✔
✔
✔
✔
✔
✔
✔

✔
✔
✔
✔
✔
✔
✔
✔
✔
✔

✔
✔
✔
✔
✔
✔
✔
✔
✔
✔

✔
✔
✔
✔
✔
✔
✔
✔
✔
✔

B ADDITIONAL RELATED WORK

This section provides comprehensive coverage of related work in software engineering agent sys-
tems, computer use automation, and benchmark datasets that complement the core infrastructure
focus of our main paper.

Software Engineering Agent Systems The field of software engineering automation has seen
significant advancement with the development of specialized agent frameworks. SWE-Agent (Yang
et al., 2024a) pioneered the application of language models to software engineering tasks through
interactive code editing and testing. OpenHands (Wang et al., 2024b) provides a comprehensive plat-
form for building generalist AI agents that can write code, interact with command lines, and browse
the web, with support for multi-agent coordination and extensive evaluation benchmarks. More
recent efforts include Qwen-Agent (Qwen Team, 2025), which focuses on Chinese language sup-
port, and specialized frameworks like Cursor and GitHub Copilot that target specific development
workflows. While these frameworks demonstrate the potential of AI-assisted software development,
they primarily operate at small scales and lack the infrastructure support for large-scale distributed
training and evaluation.

Software Engineering Benchmarks and Datasets The development of standardized benchmarks
has been crucial for advancing software engineering AI. SWE-bench (Jimenez et al., 2023) es-
tablished the foundation with real-world GitHub issues and corresponding fixes. SWE-gym (Pan
et al., 2024) extended this with interactive environments for iterative development. Recent efforts
have expanded coverage with SWE-bench Multimodal (Yang et al., 2024b), SWE-bench Multi-
lingual (Yang et al., 2025b), Multi-SWE-bench (Zan et al., 2025), and language-specific variants.
Terminal-bench (Team, 2025) evaluates command-line interactions, while Tau-bench (Yao et al.,
2024) focuses on tool use capabilities essential for software development workflows. These datasets
provide the foundation for systematic evaluation but require sophisticated infrastructure for large-
scale concurrent execution.

Computer Use and Browser Automation Beyond software engineering, agent systems have ex-
panded to general computer use automation. WebArena (Zhou et al., 2023) introduced realistic
web-based task environments for agent evaluation. Mind2Web (Deng et al., 2023) focuses on web
navigation and interaction tasks. OSWorld (Xie et al., 2024) provides comprehensive operating sys-
tem interaction benchmarks. Recent work on computer use agents includes Anthropic’s computer
use capabilities and similar efforts from other organizations. Browser automation frameworks like
Playwright and Selenium provide the underlying execution capabilities, but lack the orchestration
infrastructure for large-scale agent training scenarios.

C AGENT FRAMEWORK COMPATIBILITY

Table 1 demonstrates MegaFlow’s comprehensive compatibility across major agent frameworks and
software engineering datasets. The system’s unified API abstraction enables seamless integration

14

January 14, 2026

Table 2: Overview of the RL training environments before and after filtering. Instances with pass
rate equal to 1 (very easy) or 0 (very difficult) are removed to stabilize large-scale rollouts.

Dataset

Environments (Before) Environments (After)

SWE-Gym
SWE-rebench
Multi-SWE-RL
Synthesized (Internal)

Total

2,438
21,336
4,723
30,274

58,771

1,219
6,390
924
15,017

23,550

with diverse agent implementations, including SWE-Agent (Yang et al., 2024a), OpenHands (Wang
et al., 2024b), Mini-SWE-Agent (Yang et al., 2024a), Qwen Code (Qwen Team, 2025), and Claude
Code (Anthropic, 2025), across all evaluated benchmark suites.

This broad compatibility validates MegaFlow’s architectural design principle of specialized compo-
nent delegation, where the system focuses on orchestration and coordination rather than reimple-
menting agent-specific logic. By abstracting infrastructure complexity behind standardized inter-
faces, MegaFlow enables researchers to leverage their preferred agent frameworks while benefiting
from large-scale distributed execution capabilities.

D REINFORCEMENT LEARNING FOR AGENT TRAINING

In our reinforcement learning setup, we leverage MegaFlow to orchestrate large-scale Agentic Rein-
forcement Learning, enabling end-to-end training of coding agents directly within realistic software
engineering environments. The system’s distributed execution model allows us to run high-cost
SWE environments (requiring real compilation, testing, and verification) at scale, a capability that
conventional RL training infrastructures cannot provide.

D.1 TRAINING SETUP

Dataset The RL training corpus combines several publicly available SWE-style datasets, includ-
ing SWE-Gym (Pan et al., 2024), Multi-SWE-RL (Zan et al., 2025), and SWE-rebench (Badertdinov
et al., 2025) (using data released prior to March 2025), together with a large collection of inter-
nally synthesized SWE-style repair tasks. Before training, the combined corpus contains 2,438
environments from SWE-Gym, 21,336 from SWE-rebench, 4,723 from Multi-SWE-RL, and 30,274
synthesized environments. To stabilize large-scale RL rollouts, we filter out instances that are ei-
ther very easy (pass rate equal to 1) or very difficult (pass rate equal to 0). Table 2 summarizes
the environment counts before and after filtering. After filtering, approximately 1,219 SWE-Gym
environments, 6,390 SWE-rebench environments, 924 Multi-SWE-RL environments, and 15,017
synthesized environments remain. All filtered environments are merged into a single unified rollout
pool, and instances are sampled uniformly at random during RL training. Since sampling is per-
formed without weighting or curriculum, the effective training distribution is directly determined by
the post-filtering dataset sizes.

Algorithm and Hyperparameters We train the agent using the Group Sequence Policy Opti-
mization (GSPO) (Zheng et al., 2025) algorithm and integrate multiple agentic coding frameworks,
including OpenHands (Wang et al., 2024b), SWE-agent (Yang et al., 2024a), mini-SWE-agent (Yang
et al., 2024a), Qwen Code (Qwen Team, 2025), and Claude Code (Anthropic, 2025), ensuring broad
generalization across heterogeneous agent designs. During RL training, MegaFlow orchestrates a
total of 1024 parallel SWE environments for each training step. These environments correspond to
64 distinct SWE instances, and for each instance MegaFlow launches n = 16 independent rollout
replicas. This hierarchical parallelism structure (64 tasks × 16 replicas) enables the agent to explore
multiple trajectories per problem while sustaining extremely high throughput across heterogeneous
software environments. We then apply GSPO for policy optimization using a minibatch size of 64
and 2 PPO epochs. The agent is allowed up to 100 interaction rounds per task, with a 128k-token
context window enabling long-range reasoning over repository state, intermediate tool outputs, and

15

January 14, 2026

Figure 6: RL training dynamics on SWE-bench Verified. Model A is a 235 billion parameters
MoE model and Model B is a 30 billion parameters MoE model. Scores are evaluated using the
OpenHands scaffold across training steps 0–100.

prior attempts. The sampling temperature is set to 1.0, and the maximum response length per turn
is limited to 4096 tokens. If the agent does not explicitly terminate the task within 100 rounds (i.e.,
does not call finish / submit), a fixed penalty of −0.5 is applied. We optimize the model using
a learning rate of 1e−6, with positive and negative reward clipping thresholds set to 4e−4 and 2e−4
respectively.

D.2 TRAINING RESULTS

Figure 6 reports the RL training dynamics evaluated on SWE-bench Verified using the OpenHands
scaffold. We compare two models of different scales: Model A, a 235 billion parameters MoE
model, and Model B, a 30 billion parameters MoE model. Both models show consistent improve-
ment during RL training, with the larger model achieving substantially higher scores throughout
training. These results demonstrate the effectiveness of large-scale agentic RL training for SWE-
style tasks and highlight MegaFlow’s ability to sustain stable, fault-tolerant, and high-throughput
distributed rollouts across heterogeneous agent frameworks.

16

Score on SWE-bench Verified (%)0.500.550.600.650.70Training Step5101520253035404550556065707580859095100Model AModel B