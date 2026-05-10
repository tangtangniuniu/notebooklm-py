Technical Advancements in Agentic Telecommunications: Synergizing RAG, ReAct, and Formal Verification for Autonomous CLI Fault Diagnosis and Network Operations
The telecommunications sector is currently undergoing a structural transformation from static, human-operated infrastructures to "Agentic Telecom," a paradigm where Large Language Model (LLM) agents act as autonomous reasoning engines capable of managing the immense complexity of 5G and nascent 6G networks.[1, 2] This shift is necessitated by the inherent limitations of traditional rule-based and reactive management systems, which struggle to scale alongside the heterogeneity of modern network functions and the stringent requirements of ultra-reliable low-latency communication (uRLLC).[3, 4, 5] Modern agentic architectures represent a convergence of three critical technologies: Retrieval-Augmented Generation (RAG) for grounding responses in technical truth, the ReAct (Reasoning and Acting) framework for multi-turn autonomous planning, and formal verification tools like Batfish or high-fidelity digital twins for pre-deployment safety.[6, 7, 8, 9] As these systems evolve, they move beyond simple intent translation to a disciplined, layer-by-layer diagnostic methodology that mimics the expertise of a senior network engineer while operating at machine speed.[10, 11]
The Architectural Paradigm of Agentic Orchestration: RAG and ReAct Synergies
The transformation of a high-level operational intent—such as "diagnose and resolve intermittent connectivity in the 5G core"—into a precise sequence of CLI commands requires a transition from model-centric orchestration to agentic orchestration.[7, 12] In this context, the LLM serves as the "brain," utilizing its emergent reasoning capabilities to decompose ambiguous natural language into actionable sub-tasks.[7, 13] This architectural evolution is anchored in the synergy between RAG and the ReAct paradigm, which together facilitate a closed-loop system of observation and action.[6, 7, 14]
Mechanizing the Intent-to-Command Workflow
The workflow of a modern telecom agent begins with the extraction of intent from a natural language prompt or a machine-generated alarm.[6, 15] Unlike one-shot generation, the agent employs the ReAct framework to interleave reasoning traces with tool invocations.[3, 6] The initial thought process involves identifying the scope of the problem by querying a Network Source of Truth (NSOT) such as NetBox to understand the current topology.[14] This is followed by a retrieval step where the agent uses RAG to access relevant vendor-specific manuals or Standard Operating Procedures (SOPs).[14, 15, 16]
The integration of RAG is not merely about providing context but about mitigating the hallucination of CLI syntax.[13, 17] Recent frameworks like Intent-based RAG (IRAG) utilize a well-designed prompt system for configuration splitting and intent extraction, ensuring that each fragment of the source intent is mapped to the correct technical documentation.[16, 18] This two-stage retrieval and voting mechanism identifies the most relevant manuals, which the LLM then uses to generate a candidate command sequence.[15, 16] This process is summarized in the evolutionary progression of network management paradigms.
Management Paradigm
Core Mechanism
Interaction Style
Adaptability
Traditional/Scripted
Predefined rules and Python/Ansible scripts.
Command-and-control.
Static; fails on unforeseen scenarios.[3]
Intent-Based (IBN)
Declarative goals translated via templates.
Configuration-focused.
Limited to explicitly programmed patterns.[1, 3]
Co-pilot (Human-in-Loop)
LLM assists human operators with suggestions.
Interactive chat.
High, but limited by human response speed.[1]
Agentic (Autonomous)
Goal-directed agents with multi-turn planning.
Collaborative/Autonomous.
High; can self-correct via environmental feedback.[7, 19]
The ReAct Cycle in Fault Diagnosis
In a multi-turn diagnostic scenario, the ReAct agent operates in a continuous loop: Thought, Action, and Observation.[6, 7] For a BGP routing fault, the "Thought" might be "The BGP neighbor is down; I must check the physical interface status and then the BGP peering details".[6, 7] The "Action" involves executing a specific CLI command, such as 
display interface brief
 on a Huawei VRP system.[14, 20] The "Observation" is the command output, which the LLM parses to determine the next logical step.[6, 7] This cycle repeats until the root cause is localized, at which point the agent switches from diagnostic commands to remediation snippets.[6, 14] This iterative refinement mirrors human problem-solving, where actions provide the insights necessary for the next stage of reasoning.[6, 7]
The complexity of these interactions necessitates a hierarchical multi-agent framework.[3, 8] In such systems, a "Master Orchestrator" decomposes the intent and assigns specialized tasks to "Specialist Agents," such as a RoutingAgent for connectivity issues or an OptimizationAgent for performance tuning.[3, 14] This specialization prevents the performance degradation often seen when a single LLM attempts to manage broad, cross-domain terminologies, a phenomenon known as semantic interference.[2]
Verification and Safety: Pre-flight Checks via Batfish and Digital Twins
In high-stakes telecommunications environments, the primary inhibitor of autonomous automation is the fear of misconfiguration and subsequent service outages.[1, 10] To solve this, the agentic workflow is augmented with a verification-based evaluation pipeline.[21] This pipeline ensures that every command generated by the agent is subjected to a "pre-flight check" before deployment to production.[9, 14, 22]
Formal Verification with Batfish
Batfish serves as the foundational tool for formal network verification within these workflows.[8, 9, 14] It utilizes Header Space Analysis (HSA) to build a mathematical model of the network's data and control planes.[8, 23, 24] By analyzing device configurations without requiring direct network access, Batfish can answer complex questions about reachability, security policies, and routing behavior.[9]
Within an agentic loop, the RoutingAgent submits a candidate configuration change to Batfish.[14] Batfish evaluates this change against a "golden" reference state to detect any specification violations.[14, 21] This differential data-plane analysis identifies symptoms such as "A cannot reach B" or "Traffic is no longer load-balanced," providing the agent with precise feedback.[21] The agent then uses this feedback to adjust its reasoning and generate a corrected configuration.[14, 21, 25] This process captures approximately 90% of syntactically incorrect or logically flawed configurations before they impact the live network.[14]
Integrating Network Digital Twins (NDT)
While Batfish is highly effective for Layer 3 verifications, it is fundamentally limited by its inability to simulate temporal aspects such as protocol convergence time or vendor-specific implementation quirks.[8, 22] To address this, the Aether framework and similar systems integrate agentic AI with a multi-functional Network Digital Twin (NDT).[8, 26] The NDT provides a unified sandbox that integrates modeling (Batfish), simulation (NS3), and high-fidelity emulation (Mininet or containerized NOS images).[8, 24, 26]
Verification Mechanism
Methodology
Fidelity
Primary Use Case
Batfish (HSA)
Static configuration analysis using transfer functions.
Theoretical/Model-based.
Proving invariants (reachability, ACL correctness).[8, 9, 23]
NS3 / RouteNet
Simulation of traffic patterns and protocol interactions.
Statistical.
Performance analysis (latency, jitter, packet loss).[8, 24, 27]
Mininet / Kathará
Container-based emulation using real NOS images.
High.
Validating multi-turn CLI interactions and edge cases.[8, 10, 28]
Physical Lab
Replicated hardware infrastructure.
Absolute.
Final stage validation for critical hardware-dependent features.[8]
The Aether architecture employs a modular compositional approach, where complex tasks are decomposed into smaller verifications that are independently analyzed and then combined for end-to-end assurance.[27] For example, verifying an SRv6 overlay might involve using Batfish for the underlay forwarding logic while using a specialized emulation sandbox for the segment routing logic.[8, 27] This integrated architecture has demonstrated 100% error detection and 92-96% diagnostic coverage in major ISP environments, completing validations in 6-7 minutes that previously took weeks.[26]
Frontiers of 2025-2026: ALE, NetArena, and NetLLM in 5G and BGP Resilience
The advancement of LLM capabilities has led to the development of specialized frameworks and benchmarks tailored for the rigors of production-grade network operations. These systems address the critical gap between general-purpose language models and the disciplined methodology required for network troubleshooting.[10, 11]
ALE: The Agentic Learning Ecosystem
The Agentic Learning Ecosystem (ALE) is a foundational infrastructure designed to optimize the end-to-end production pipeline for agent LLMs.[29, 30] ALE recognizes that agentic crafting is an iterative process requiring models to plan, execute, and self-correct over long horizons.[30, 31] The ecosystem is comprised of three core components:
ROLL (Reinforcement Learning Optimization for Large-Scale Learning)
: This framework facilitates post-training weight optimization using a novel policy optimization algorithm called IPA (Interaction-based Policy Alignment).[29, 30] Unlike standard RL that assigns credit at the token level, IPA assigns credit over semantic interaction chunks, significantly improving training stability for long-horizon tasks.[30]
ROCK (Reinforcement Open Construction Kit)
: A secure, sandboxed execution environment used for trajectory generation and validation.[29, 30] ROCK allows for the synthesis of executable, tool-grounded trajectories that serve as high-quality training data.[30]
iFlow CLI
: An agent framework that enables efficient context engineering for environment interaction, providing the user-facing interface for real-world workflows.[29, 30]
Through ALE, researchers have released the ROME model (ROME is Obviously an Agentic ModEl), which has demonstrated superior performance on mainstream benchmarks like Terminal-Bench 2.0, outperforming models twice its size.[30] ALE enables a continuous optimization loop where user feedback and environmental observations are fed back into the training pipeline to adapt to new network failure patterns.[29, 30]
NetArena: The Era of Dynamic Benchmarking
One of the most significant milestones in 2025 was the introduction of NetArena, the first dynamic benchmark generation framework for network operation tasks.[28, 32] NetArena addresses the "contamination risk" of static benchmarks, where models might have seen evaluation data during pre-training.[28, 32] By defining a unified state-action abstraction, NetArena can generate unlimited queries on demand across diverse applications, including datacenter capacity planning and routing misconfiguration.[28, 32]
When evaluating state-of-the-art models like GPT-4o and Qwen-72B, NetArena found that even the best models achieved only 13-38% average correctness in realistic queries.[28, 32] This underscores the complexity of production-level networking tasks and highlights the need for specialized agents like MeshAgent or ROME, which use program synthesis and environment-grounded learning to improve performance.[28, 30] NetArena provides runtime feedback on correctness, safety, and latency, offering a multidimensional view of agent reliability.[28, 32]
Case Studies in 5G Core and BGP Fault Analysis
The practical application of these frameworks is evident in recent case studies involving 5G network element failures and BGP routing instability.[10, 33] In 5G Core (5GC) environments, faults such as AMF (Access and Mobility Management Function) or SMF (Session Management Function) pod crashes can be diagnosed using fine-tuned LLMs trained on realistic fault injections.[33, 34] By using Chaos Mesh to inject errors into Kubernetes-based testbeds, researchers have built datasets covering pod kills, network delays, and disk I/O failures.[33, 34] A fine-tuned GPT-4.1-Nano model showed significant improvement in fault detection and classification compared to base models, demonstrating the value of domain-specific fine-tuning.[33, 34]
For BGP failures, the SADE (Symptom-Aware Diagnostic Escalation) agent introduces a disciplined troubleshooting methodology.[10, 11, 35] SADE argues that free-form deliberation often leads to "hypothesis commitment" before sufficient evidence is gathered.[10, 11] Instead, SADE implements a phase-gated diagnostic workflow:
Initial Scan
: Rapidly identifies symptoms across the physical and data link layers.[10, 11]
Deep Network Scan
: Probes higher-layer protocol states, such as BGP peering or OSPF adjacencies.[10, 11]
Symptom-to-Fault-Family Matching
: Correlates observed symptoms with known failure patterns using a library of specialized "fault-family skills".[10, 11]
Root Cause Analysis
: Uses high-yield diagnostic helpers to pinpoint the exact configuration error or resource contention.[11]
In evaluations on the NIKA benchmark, SADE improved the root-cause F1 score by 37 percentage points over traditional ReAct baselines, proving that a structured policy is essential for navigating the complex diagnostic trees of a modern network.[11, 35]
Protocol-Specific SOPs: Parsing Unstructured CLI and Logic Inference
A fundamental challenge for any LLM agent is the parsing of unstructured CLI output from diverse vendors, such as Huawei VRP's 
display
 commands or Cisco IOS's 
show
 commands.[20, 36, 37] These outputs lack a formal structure, often containing repetitive patterns and varying dramatically across software versions.[17, 38]
SOP for LLM-Based CLI Data Extraction
The Standard Operating Procedure (SOP) for parsing involves a mixture of structured prompting and a programmatic feedback loop.[17] This process is critical for transforming raw text into the JSON/YAML formats required for machine consumption and further reasoning.[37]
Step 1: Contextual Framing and Schema Definition
: The agent is prompted with the raw CLI output and a desired JSON schema representing the objects to be extracted (e.g., BGP neighbor IP, state, up/down time).[17, 37]
Step 2: Hierarchical Chunking
: Large configuration or "show" files are split into chunks based on syntax delimiters (e.g., interface blocks or BGP peer groups) with sufficient overlap to preserve context.[17]
Step 3: Verification and Recursive Feedback
: The extracted JSON is validated against the schema. If validation fails, the LLM is re-prompted with the error message, allowing it to re-parse the section.[17]
Step 4: Cross-Vendor Mapping
: The agent uses an internal knowledge base to translate vendor-specific terminology into a unified data model.[16, 36]
Operational Task
Cisco IOS Command
Huawei VRP Command
Logic/Inference Goal
System View
configure terminal
system-view
Enter mode for global parameter modification.[20, 36, 39]
Peer Review
show cdp neighbors
display lldp neighbor
Topology verification; check for link mismatches.[20, 38]
BGP State
show ip bgp summary
display bgp peer
Diagnose peering status (Established, Active, Idle).[20]
Traffic Audit
show interface status
display interface description
Check physical port availability and admin state.[20]
Resource Monitor
show processes cpu
display cpu-usage
Identify resource contention or control plane overload.[20]
Persistence
wr
 / 
copy run start
save
Ensure intended state survives a device reboot.[20]
Logic Inference and Causal Relationships
Beyond simple parsing, the agent must perform causal inference based on the parsed data.[11, 36] For example, in Huawei VRP, if the 
display current-configuration
 shows an OSPF process but 
display ospf peer
 shows no neighbors, the agent must infer whether the issue is a physical link failure, a subnet mismatch, or a firewall blocking protocol hellos.[20, 36]
This reasoning is increasingly facilitated by "probabilistic Semantic Query Routing," which dynamically selects the relevant context domain based on the query intent.[2] In uRLLC scenarios, where response speed is critical, this routing reduces response generation latency to approximately 3.47 seconds by filtering out irrelevant technical documentation, ensuring that the agent's logic remains focused on the specific failure domain.[2]
Security and Integrity in Agentic Workflows
As agents are given "write primitives"—the ability to execute actions that modify the network state—new security vulnerabilities emerge.[40] Unlike traditional chatbots, an agent with tool access can be manipulated through prompt injection to leak sensitive configuration data or perform unauthorized changes.[40] Even if the chat interface is "locked down" with templated responses, the model's agency allows it to write arbitrary data into form fields or log entries, which can serve as exfiltration channels.[40]
Mitigating these risks requires architectural constraints, such as supervisor LLMs that analyze agent outputs for data leakage and strict output validation using hard filters.[40, 41] In the Aether framework, security is handled through a "Human-in-the-Loop" gate, where every remedial action must be explicitly approved via a dashboard or notification agent.[14] This ensures that while the agent can reason and plan autonomously, the final decision to modify production infrastructure remains with a human engineer.[1, 14]
Strategic Implications of Agentic Telecom
The convergence of agentic AI and telecommunications marks a fundamental transition from purely statistical machine learning to semantic-aware, proactive management.[2] This "One Model for All Tasks" philosophy is being incorporated into global standards, such as ETSI GR ENI 045, which formally integrates LLMs as reasoning engines within the Operational Administration Maintenance and Provisioning (OAMP) architecture.[2]
The transition to agentic telecom is driven by three converging forces:
Dynamic Network Demands
: The rise of AI workloads, multi-cloud adoption, and edge computing creates demand patterns that static, rule-based systems cannot accommodate.[1, 5]
Maturity of Automation
: APIs, orchestration engines, and NSOT systems have reached a level of reliability that enables real-time, programmatic control by AI agents.[1, 41]
Linguistic Interpretation of Intent
: LLMs have bridged the gap between non-technical business intents and low-level technical execution, making network management accessible to a broader range of personnel.[1, 33]
As large language models deepen their understanding of network design patterns and historical performance, their ability to suggest smarter architectures and anticipate failures before they occur will only strengthen.[1, 18] The ongoing evolution toward 6G will further solidify the role of agentic AI as the central nervous system of global connectivity, enabling a "zero-touch" reality where the network not only builds itself but also heals and optimizes itself with minimal human intervention.[3, 42, 43]
Conclusions and Technical Outlook
The research indicates that LLM-based agents are no longer experimental novelties but are rapidly becoming the primary interface for telecom network automation. The integration of ReAct and RAG provides a robust architectural foundation for converting ambiguous intents into multi-turn CLI sequences, while the use of Batfish and Network Digital Twins addresses the critical safety requirements of mission-critical infrastructure. The progress seen in frameworks like NetArena and ALE suggests a move toward specialized, high-fidelity ecosystems where agents are trained on realistic, executable trajectories and evaluated against dynamic, contamination-resistant benchmarks.
For practitioners, the immediate focus should be on the implementation of structured diagnostic policies, such as SADE, and the adoption of robust SOPs for parsing the heterogeneous CLI output of multi-vendor environments. The transition to agentic telecom will ultimately be defined by the ability to balance autonomous speed with human-centric safety, ensuring that the "Global Kill Switch" remains firmly under human oversight while the AI agents handle the grueling complexity of 5G and 6G operations. As these systems continue to mature, the focus will likely shift toward more efficient credit assignment in RLHF (Reinforcement Learning from Human Feedback) and the development of multimodal agents capable of interpreting topology diagrams and physical hardware layouts alongside textual CLI data.

--------------------------------------------------------------------------------

From AI Prompt to Real-Time Provisioning: Welcome to the Era of Agentic Telecom, 
https://www.lightreading.com/ai-machine-learning/from-ai-prompt-to-real-time-provisioning-welcome-to-the-era-of-agentic-telecom
https://www.lightreading.com/ai-machine-learning/from-ai-prompt-to-real-time-provisioning-welcome-to-the-era-of-agentic-telecom
Bridging the Semantic Gap in 5G: A Hybrid RAG Framework for Dual-Domain Understanding of O-RAN Standards and srsRAN Implementation - MDPI, 
https://www.mdpi.com/2076-3417/16/7/3275
https://www.mdpi.com/2076-3417/16/7/3275
Agentic AI Empowered Intent-Based Networking for 6G - arXiv, 
https://arxiv.org/html/2601.06640v1
https://arxiv.org/html/2601.06640v1
Eureka Journal of Artificial Intelligence and Data Innovation (EJAIDI), 
https://eurekaoa.com/index.php/11/article/download/534/586
https://eurekaoa.com/index.php/11/article/download/534/586
Generative AI Empowered Network Digital Twins: Architecture, Technologies, and Applications | Request PDF - ResearchGate, 
https://www.researchgate.net/publication/387921537_Generative_AI_Empowered_Network_Digital_Twins_Architecture_Technologies_and_Applications
https://www.researchgate.net/publication/387921537_Generative_AI_Empowered_Network_Digital_Twins_Architecture_Technologies_and_Applications
ReACT agent LLM: Making GenAI react quickly and decisively - K2view, 
https://www.k2view.com/blog/react-agent-llm/
https://www.k2view.com/blog/react-agent-llm/
What is a ReAct Agent? | IBM, 
https://www.ibm.com/think/topics/react-agent
https://www.ibm.com/think/topics/react-agent
Aether: Network Validation Using Agentic AI and Digital Twin - arXiv, 
https://arxiv.org/html/2604.18233v1
https://arxiv.org/html/2604.18233v1
How Batfish Fits into Your Network Automation Plan, 
https://networktocode.com/blog/batfish-fits-network-automation-plan/
https://networktocode.com/blog/batfish-fits-network-automation-plan/
SADE: Symptom-Aware Diagnostic Escalation for LLM-Based Network Troubleshooting - arXiv, 
https://arxiv.org/pdf/2605.04530
https://arxiv.org/pdf/2605.04530
[2605.04530] SADE: Symptom-Aware Diagnostic Escalation for LLM-Based Network Troubleshooting - arXiv, 
https://arxiv.org/abs/2605.04530
https://arxiv.org/abs/2605.04530
Top 10+ Agentic Orchestration Frameworks & Tools - AIMultiple, 
https://aimultiple.com/agentic-orchestration
https://aimultiple.com/agentic-orchestration
Managing Complex Failure Analysis Workflows with LLM-based Reasoning and Acting Agents - arXiv, 
https://arxiv.org/html/2506.15567v1
https://arxiv.org/html/2506.15567v1
“The Era of AI Agents for Network Engineering”: Intent ... - TechRxiv, 
https://www.techrxiv.org/doi/pdf/10.36227/techrxiv.177004277.71795055
https://www.techrxiv.org/doi/pdf/10.36227/techrxiv.177004277.71795055
INTA: Intent-Based Translation for Network Configuration with LLM Agents - arXiv, 
https://arxiv.org/html/2501.08760v2
https://arxiv.org/html/2501.08760v2
Leveraging LLM Agents for Translating Network Configurations - arXiv, 
https://arxiv.org/html/2501.08760v1
https://arxiv.org/html/2501.08760v1
Is Accurate Network Data Extraction with LLMs Possible? | by Amar Abane | Medium, 
https://medium.com/@amar.abane.phd/is-accurate-network-data-extraction-with-llms-possible-ca8e3161e973
https://medium.com/@amar.abane.phd/is-accurate-network-data-extraction-with-llms-possible-ca8e3161e973
Configtrans: Network Configuration Translation Based on Large Language Models and Constraint Solving | Request PDF - ResearchGate, 
https://www.researchgate.net/publication/388697274_Configtrans_Network_Configuration_Translation_Based_on_Large_Language_Models_and_Constraint_Solving
https://www.researchgate.net/publication/388697274_Configtrans_Network_Configuration_Translation_Based_on_Large_Language_Models_and_Constraint_Solving
Agentic AI Driving Paradigm Shift in Mobile AI, Transforming 5G Network Evolution, 
https://counterpointresearch.com/en/insights/Agentic-AI-Driving-Paradigm-Shift-in-Mobile-AI-Transforming-5G-Network-Evolution
https://counterpointresearch.com/en/insights/Agentic-AI-Driving-Paradigm-Shift-in-Mobile-AI-Transforming-5G-Network-Evolution
Cheatsheet Huawei/Cisco Commands - Netcamp, 
https://netcamp.ch/component/phocadownload/category/3-public?download=8:cheatsheet-huawei-cisco-commands&Itemid=284
https://netcamp.ch/component/phocadownload/category/3-public?download=8:cheatsheet-huawei-cisco-commands&Itemid=284
Benchmarking LLM-Driven Network Configuration Repair - arXiv, 
https://arxiv.org/html/2604.22513v1
https://arxiv.org/html/2604.22513v1
AI Network Digital Twin — Change Validation, What-If, Dev/Test | NetPilot, 
https://www.netpilot.io/network-digital-twin
https://www.netpilot.io/network-digital-twin
Header Space Analysis: Static Checking For Networks | Request PDF - ResearchGate, 
https://www.researchgate.net/publication/262242767_Header_Space_Analysis_Static_Checking_For_Networks
https://www.researchgate.net/publication/262242767_Header_Space_Analysis_Static_Checking_For_Networks
BRKNWT-2502 Agentic AI and NetDevOps: Enabling a New Era of Network Change Validation - Cisco Live, 
https://www.ciscolive.com/c/dam/r/ciscolive/global-event/docs/2025/pdf/BRKNWT-2502.pdf
https://www.ciscolive.com/c/dam/r/ciscolive/global-event/docs/2025/pdf/BRKNWT-2502.pdf
Lessons from the evolution of the Batfish configuration analysis tool - ResearchGate, 
https://www.researchgate.net/publication/373611204_Lessons_from_the_evolution_of_the_Batfish_configuration_analysis_tool
https://www.researchgate.net/publication/373611204_Lessons_from_the_evolution_of_the_Batfish_configuration_analysis_tool
Aether: Network Validation Using Agentic AI and Digital Twin, 
https://www.researchgate.net/publication/404022424_Aether_Network_Validation_Using_Agentic_AI_and_Digital_Twin
https://www.researchgate.net/publication/404022424_Aether_Network_Validation_Using_Agentic_AI_and_Digital_Twin
Aether: Network Validation Using Agentic AI and Digital Twin - arXiv, 
https://arxiv.org/pdf/2604.18233
https://arxiv.org/pdf/2604.18233
NetArena: Dynamic Benchmarks for AI Agents in Network Automation | OpenReview, 
https://openreview.net/forum?id=BPVPOtzoOz
https://openreview.net/forum?id=BPVPOtzoOz
Let It Flow: Agentic Crafting on Rock and Roll Building the ROME Model within an Open Agentic Learning Ecosystem - arXiv, 
https://arxiv.org/html/2512.24873v3
https://arxiv.org/html/2512.24873v3
Let It Flow: Agentic Crafting on Rock and Roll, Building the ROME Model within an Open Agentic Learning Ecosystem - arXiv, 
https://arxiv.org/pdf/2512.24873
https://arxiv.org/pdf/2512.24873
Daily Papers - Hugging Face, 
https://huggingface.co/papers?q=agentic
https://huggingface.co/papers?q=agentic
NetArena: Dynamic Benchmarks for AI Agents in Network Automation - arXiv, 
https://arxiv.org/pdf/2506.03231
https://arxiv.org/pdf/2506.03231
Automated Fault Detection in 5G Core Networks Using Large Language Models - arXiv, 
https://arxiv.org/html/2512.19697
https://arxiv.org/html/2512.19697
Automated Fault Detection in 5G Core Networks Using Large Language Models, 
https://www.researchgate.net/publication/399026421_Automated_Fault_Detection_in_5G_Core_Networks_Using_Large_Language_Models
https://www.researchgate.net/publication/399026421_Automated_Fault_Detection_in_5G_Core_Networks_Using_Large_Language_Models
NetGenius: Routing Configuration Recommendation Based on Graph Neural Network | Request PDF - ResearchGate, 
https://www.researchgate.net/publication/392648039_NetGenius_Routing_Configuration_Recommendation_Based_on_Graph_Neural_Network
https://www.researchgate.net/publication/392648039_NetGenius_Routing_Configuration_Recommendation_Based_on_Graph_Neural_Network
Cisco vs Huawei Command Comparison | PDF | Booting - Scribd, 
https://www.scribd.com/document/513773566/Cisco
https://www.scribd.com/document/513773566/Cisco
Understanding Network CLI Configurations with ML, ANN, and LLMs - Generative AI with Large Language Models - DeepLearning.AI Community, 
https://community.deeplearning.ai/t/understanding-network-cli-configurations-with-ml-ann-and-llms/832469
https://community.deeplearning.ai/t/understanding-network-cli-configurations-with-ml-ann-and-llms/832469
ttp/docs/source/Writing templates/How to parse show commands output.rst at master, 
https://github.com/dmulyalin/ttp/blob/master/docs/source/Writing%20templates/How%20to%20parse%20show%20commands%20output.rst
https://github.com/dmulyalin/ttp/blob/master/docs/source/Writing%20templates/How%20to%20parse%20show%20commands%20output.rst
README v6.85.6 2026-04-23 | NED READMEs - Cisco Crosswork NSO Documentation, 
https://nso-docs.cisco.com/neds/cisco-provided-neds/huawei-vrp/huawei-vrp
https://nso-docs.cisco.com/neds/cisco-provided-neds/huawei-vrp/huawei-vrp
Exploiting LLM Write Primitives: System Prompt Extraction When Chat Output Is Locked Down | Praetorian, 
https://www.praetorian.com/blog/exploiting-llm-write-primitives-system-prompt-extraction-when-chat-output-is-locked-down/
https://www.praetorian.com/blog/exploiting-llm-write-primitives-system-prompt-extraction-when-chat-output-is-locked-down/
Herve Hildenbrand hervehildenbrand - GitHub, 
https://github.com/hervehildenbrand
https://github.com/hervehildenbrand
Agentic AI for Autonomous Telecom Network Management - ResearchGate, 
https://www.researchgate.net/publication/400630531_Agentic_AI_for_Autonomous_Telecom_Network_Management
https://www.researchgate.net/publication/400630531_Agentic_AI_for_Autonomous_Telecom_Network_Management
NetAgentBench: A State-Centric Benchmark for Evaluating Agentic Network Configuration - arXiv, 
https://arxiv.org/pdf/2604.09678
https://arxiv.org/pdf/2604.09678