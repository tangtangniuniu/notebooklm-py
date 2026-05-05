White Paper  Cisco Public

AI Infrastructure
for the
Agentic Era

Table of Contents

The emergence of agentic AI

The agentic AI lifecycle

Infrastructure innovations driving AI forward

Explosion of demand for AI infrastructure

AI lifecycle infrastructure considerations

  Mass-scale AI data centers

Large-scale AI data centers

Edge AI data centers

  WAN interconnect for AI

Cisco is meeting the diverse infrastructure needs of the AI lifecycle

AI-ready data centers

  WAN and data center interconnect

Security and assurance

Conclusion

© 2025  Cisco and/or its affiliates. All rights reserved.  |  1

2

3

4

5

6

7

8

8

8

10

12

15

17

19

White Paper  Cisco PublicMaking AI work for you.

The emergence of agentic AI

We are entering the “Internet of Agents” era. Today,

Multimodal GenAI is a natural extension to GenAI.

our workforces are entirely human. Tomorrow, they will

In the real world, people encounter and comprehend

expand exponentially to include a variety of non-human

information through a combination of different

AI “workers”—including apps, agents, robots, and

modalities, such as text, audio, visual, and sensing.

even humanoids. Agentic AI introduces a world where

Multimodal GenAI replicates this process by combining

connected AI agents and people will work together to

and analyzing different types of data inputs to generate

orchestrate all manner of complex workflows. This will

more robust results. A shift is now underway with the

result in massive gains in productivity and capacity,

development of natively multimodal GenAI models such

with considerable shared benefits for organizations,

as OpenAI’s GPT-4o. Gartner estimates that by 2027,

workers, and society alike.

The evolution to agentic AI has been rapid and

40% of GenAI solutions will be multimodal, up from
1% in 2023.1

resolute. When OpenAI released an early demo of

As shown in Figure 1, agentic AI represents the

ChatGPT-3 on November 30, 2022, the generative AI

next frontier in this evolution, providing autonomous

(GenAI) chatbot quickly went viral. Within five days,

decision-making, planning, and adaptive execution

ChatGPT had introduced one million users to its

to complete multi-step processes. By 2028, at least

powerful ability to create original content on demand.

15% of day-to-day business decisions will be made

This marked the beginning of the Cambrian-like

autonomously through agentic AI machine workflows

explosion of GenAI applications.

for rule-based tasks, up from 0% in 2024, according
to Gartner.2

<2022

2022-2023

2024

2025+

l

e
u
a
V
s
s
e
n
s
u
B

i

Agentic
AI

Multimodal
Generative AI

Single-Modal
Generative AI

Traditional
AI

Figure 1.  The evolution to agentic AI is driving greater business value

© 2025  Cisco and/or its affiliates. All rights reserved.  |  2

White Paper  Cisco PublicMaking AI work for you.
These AI agents, powered by large language

Enterprises use retrieval-augmented generation

models (LLMs) and equipped with increasingly

(RAG) and other inferencing techniques that augment

advanced reasoning capabilities, will be able to

contextual information from proprietary databases to

discover and learn individually. Then, over time, AI

generate more accurate and relevant responses that

agents will collaborate with each other by forming

extend beyond the scope of the original model.

Agentic AI workflows provide the ability to make

autonomous business decisions and can greatly

benefit from collaboration with connected agents

working across multiple devices, types, and locations.

The powerful ability to combine the intelligence

of agents with specialized knowledge to make

decisions and act in real time has the potential to

drive substantial business impact across every

aspect of the organization.

chains of operations, which will enable them to

automate business functions. This new “Internet

of Agents” era is defined by Cisco as an “open,

interoperable internet for agent-agent and

agent-human quantum-safe communication” that

enables secure agent collaboration while preserving
organizational autonomy.3

The agentic AI lifecycle

The agentic AI lifecycle builds on current AI LLM and

inferencing models (Figure 2). The foundational element

for agentic AI architecture is the pre-training of large

datasets that create general purpose foundational and

frontier LLMs. These LLMs are fine-tuned based

on additional domain-specific data to create

domain-specific or job-specific LLMs.

Model creation

Pre-training

Fine-tuning

General purpose
foundational
models

Model serving

Inferencing

AI agents

Retrieval-augmented
generation

Prompt engineering

Frontier models

Domain-specific or
job-specific models

Inference model(s)

Inference model(s)

Inference model(s)

High

Infrastructure scale and complexity

Figure 2.  Agentic AI lifecycle builds on current models

Rule-based
agents

Low

© 2025  Cisco and/or its affiliates. All rights reserved.  |  3

White Paper  Cisco PublicMaking AI work for you.Infrastructure innovations driving
AI forward

New and rapid innovations across the complete AI

Denser and faster infrastructure is also driving the

infrastructure stack (Figure 3) are making the evolution

need for innovations in direct-to-chip liquid cooling to

to agentic AI a reality. Innovations in accelerated

significantly reduce the energy required for cooling. At

compute are leading to the densification of racks,

the same time, the evolution to agentic AI is resulting

which provides the level of performance required

in increasingly complex workflows between distributed

to support all aspects of the agentic AI lifecycle.

agents and LLMs, requiring fast, reliable, secure wide

The increasing speed and scale of accelerators like

area network (WAN) connectivity from the cloud to the

graphics processing units (GPUs) is driving dramatic

edge and everywhere in between. Importantly, these

performance and scale improvements in scale-up

distributed workflows also require innovative new

and scale-out networks, spurring demand for more

approaches to making the infrastructure, workloads,

advanced network switching silicon and higher

and data more secure and assured.

data-rate optics.

AI Models

Pre-training

Fine-tuning

RAG

Inferencing

AI frameworks and management tools

Virtualization and Kubernetes

AI infrastructure

Management

Security

Assurance

Large/Edge AI Data Centers

Mass-Scale AI Data Centers

Front end

Compute

Accelerators

Storage

Network fabric

Optics

AI
back end

Front end

Compute

Accelerators

Storage

Network fabric

Optics

AI
back end

Edge

SD-WAN/SASE

Data Center Interconnect/WAN
Routing, mobile
Optical systems

Coherent optics

Inter-
cluster

Inter-data center

Silicon

Figure 3.  AI evolution requires infrastructure innovation across the full stack

© 2025  Cisco and/or its affiliates. All rights reserved.  |  4

White Paper  Cisco PublicMaking AI work for you.Explosion of demand for AI infrastructure

Agentic AI is proving to be a major driver for data

Meanwhile, the data center infrastructure and

center infrastructure build-outs and expansion.

internetworking services of colocation providers and

According to McKinsey & Company, global data center

communications service providers (CSP) are in high

capacity demands could more than triple by 2030, with
70% of that growth being driven by AI workloads.4 This
demand is driving the emergence of new mass-scale

demand due to the enormous space, power, and cooling

demands of AI workloads, as well as WAN connectivity

across data centers and regions. This demand is being

data center hubs, where the availability of sustainable

propelled by the growing global deficit in modern

power and cooling are the main selection criteria. In

AI-ready data center facilities to host enterprise inference

addition to these large investments being made in data

models, and also by data sovereignty requirements that

centers to run LLMs, LLMs are creating demand for the

are creating the need for regional “sovereign clouds” to

private and public cloud AI infrastructure required to

address specific industry or governmental regulatory and

run inferencing models.

Gartner expects that the use of GenAI models will

influence over 90% of organizations to pursue hybrid

cloud environments through 2027, in turn creating

compliance needs. At the same time, the emergence of

distributed agentic architectures with demanding latency,

security, and regulatory requirements is driving new

intelligent internet and private backbone architectures.

demand for data center interconnect (DCI) networks

From training scale to test-time scale

that transport data between distributed, hybrid and
cloud data center architectures.5 Meanwhile, the
approaching tsunami of distributed AI agents at the

edge is causing infrastructure investments across the

cloud-to-edge continuum to ratchet up. By 2026, at

least 50% of edge computing deployments will involve
machine learning, compared to just 5% in 2022.6

The AI industry continues to explore the limits of scale

and opportunities to improve the accuracy and usefulness

of foundational models. Pre-training and post-training

(i.e., fine-tuning) were the initial phases where scale was

being exploited. Now there is a transformational shift

toward test-time scale. This involves scaling compute and

network resources during the inference phase (or test

The infrastructure requirements for providing

time) based on business criteria.

AI services vary significantly by provider type.

Hyperscaler cloud providers such as Microsoft,

Google, Meta, and Amazon are making significant

investments to scale data center AI clusters and even

extend clusters across metro areas. More recently,

so-called “neocloud” GPU-as-a-service providers

and foundational model providers are emerging to

rival the AI cloud infrastructure scale of hyperscalers to
address the growing LLM and inferencing demands.7
At the same time, as enterprise and public sector

organizations ramp up their AI initiatives, they are

choosing to meet their inference modelling needs

through private, public, or hybrid cloud approaches.

A good example of the benefits of test-time scale is

OpenAI’s o3 breakthrough model, which achieved

unprecedented results in adaptability and generalization
in the ARC-AGI-1 benchmark.8 The implications of this
shift to multi-step test-time computing are significant

and will multiply the requirements for infrastructure to

create substantially more tokens while returning results

within a desired time. According to Gartner, more than

80% of workload accelerators deployed in data centers
will be used to execute AI inference workloads by 2028.9
Additionally, agentic AI means that multiple AI agents

will work together to solve harder and harder problems.

© 2025  Cisco and/or its affiliates. All rights reserved.  |  5

White Paper  Cisco PublicMaking AI work for you.AI lifecycle infrastructure considerations

The comprehensive agentic AI lifecycle view is

Each of these architectures has an important part

supported by four key architectures:

to play in delivering on generative and agentic AI,

•  Mass-scale cloud AI data centers

•  Large-scale AI data centers

•  Edge AI data centers

and each has unique requirements. The complete

lifecycle depends on each of the participants in the

AI ecosystem contributing their part. This ecosystem

includes hyperscalers, neocloud and model providers,

enterprise and public sector organizations, CSPs, and

•

Interconnecting wide area networks (WANs)

colocation providers. Figure 4 shows the primary AI

infrastructure requirements for each.

Ecosystem
Participant

Primary AI
Focus

Enterprise and Public Sector

Communications
Service Providers

Colocation
Service Providers

AI
Model Builders

Neocloud
Providers

Hyperscalers and Tier 2
Cloud Providers

• Use generative and agentic AI solutions
building on large language models to
improve business processes

• Offer connectivity
services to power
agentic AI

• Offer colocation
services and
sovereign clouds

• Offer AI

data center
infrastructure
services and
interconnect services

• Build general

purpose frontier
and foundational
models

• Offer cloud-delivered AI infrastructure
services such as GPU-as-a-service

Agentic AI Phase

Fine-Tuning and Inferencing

Pre-training, Fine-Tuning, and Inferencing

Infrastructure
Focus

Large-Scale and Edge AI Data Centers

Mass–Scale AI Data Centers

Data Center Interconnect/WAN

• Small to large clusters: 8 GPUs to 5k+ GPUs

• Cloud-to-edge

• Power efficiency and

• Mass-scale clusters: 5K-100K+ GPUs

Primary
Infrastructure
Requirements

• Simplified deployment and operations

• Integrated infrastructure stack*

• End-to-end security

• AI workflow service levels

secure
AI connectivity

• Automation

and assurance

cooling

• Multi-tenancy

security

• Cloud interconnect

• Infrastructure performance efficiency

• Multi-tenancy security and reliability

• Power efficiency

* Integrated stack combines compute/accelerator, networking, optics, and storage for a complete AI cluster

Figure 4.  AI Infrastructure requirements depend on the specific needs of the ecosystem participant

© 2025  Cisco and/or its affiliates. All rights reserved.  |  6

White Paper  Cisco PublicMaking AI work for you.Mass-scale AI data centers

Mass-scale AI data center infrastructures for

Today, pre-training and fine-tuning for most

pre-training and fine-tuning LLMs differ in scale and

LLM models happens in hyperscaler or neocloud

architecture from traditional data centers. This is

environments due to the massive scale and investment

especially the case in the deployment of back-end AI

required. Hyperscalers, Tier 2 cloud providers, and

training clusters that scale and optimize performance

some large neocloud providers buy components

by distributing training processes across many

and use open-source solutions to build high-density

thousands of GPUs in parallel (Figure 5).

architectures. These architectures are fully optimized

and automated and feature custom management

solutions which address scalability and performance

and reduce the total cost of ownership (TCO).

Data center
interconnect

Front-end
network

AI compute
accelerator
clusters

AI back-end
network

Storage

InfiniBand or Ethernet
network fabric with
400/800G optical
connections

AI training cluster

Figure 5.  The AI-ready data center architecture and technology stack differ significantly from traditional data centers

© 2025  Cisco and/or its affiliates. All rights reserved.  |  7

White Paper  Cisco PublicMaking AI work for you.
Large-scale AI data centers

WAN interconnect for AI

Today, organizations that are focusing their AI build

While much of the AI infrastructure attention has

initiatives on creating their own inferencing capabilities

been on data center infrastructure requirements,

typically need to invest less in infrastructure than those

as AI workflows become more distributed there is

building their own LLMs. However, as inferencing

a growing need for different classes of connectivity

techniques become more powerful and increasingly

between cloud, enterprise, and edge environments.

use iterative reasoning techniques, such as

The emergence of distributed AI agents and iterative

test-time scale, the infrastructure investments required

run-time inferencing models will further expand the

to support them will increase too. Likewise, enterprises

requirements for interconnectivity across the

are increasingly aware of the need to protect their AI

cloud-edge continuum.

applications, data, and infrastructure from attack.

For enterprises, this means choosing affordable,

Enterprises that are building out their own models can

scalable networking services or self-owned secure

do so in their own data centers, in colocation facilities,

networking solutions that address the run-time nature

or in hyperscaler and neocloud facilities. Large

of distributed AI-enabled processes and the need

enterprises, CSPs, and colocation providers often

for data integrity, authenticity, confidentiality, and

choose to adopt vertically integrated technology stacks

compliance. Organizations need to choose solutions

and build high-density architectures to align with

that can secure their AI WAN traffic everywhere

scalability and time-to-market requirements.

through cloud-based security and segmentation and

Edge AI data centers

As inferencing models become more advanced,

multiple forces are pushing toward more distributed

and regionalized inference closer to the edge;

among them are power and space density, user

scale, data regulation and sovereignty, and over

time, network performance and latency. Edge AI

deployments distribute smaller-scale compute and

networking resources closer to the data, end users,

and devices. This reduces the strain on centralized

cloud and data center infrastructures, addresses data

privacy concerns, and allows for more real-time data

processing and decision-making. At the same time,

the distributed nature of data and GPU resources at

the edge requires additional attention to security.

assure AI performance with end-to-end visibility

and the optimization of AI flows across owned and

unowned networks.

To help meet these interconnectivity requirements,

CSPs will need a converged transport network

spanning access and metro to unify what were

traditionally layered silos. In addition, CSPs will need

to implement architectural changes that allow for the

extension of services more deeply into the metro

to reduce latency, increase protection, and ensure

regulatory compliance of specific flows. End-to-end

security that goes beyond traditional protocols,

like IPsec and MACsec, will also be essential for

addressing future threats, such as those posed

by quantum computing.

© 2025  Cisco and/or its affiliates. All rights reserved.  |  8

White Paper  Cisco PublicMaking AI work for you.There are three primary interconnectivity use cases,

As inference models become more advanced and

as shown in Figure 6:

•

Inter-cluster connectivity

iterative, the performance requirements of inter-data

center connectivity become increasingly important.

Running high-density and power-hungry

•  Edge AI connectivity

AI workloads often necessitates the use of multiple

Edge AI deployments require secure, real-time

data centers within a metro area. The goal is to

connectivity to ensure that any remote inferencing

create larger GPU resource pools by extending

models and agents running on an edge data center

AI clusters using multiple highly secure,

or an IoT or end-user device have consistent, secure

ultra-high-bandwidth optical connections.

connectivity to central data centers. And as agentic

AI increasingly requires agents to collaborate,

optimized end-to-end network service levels and

security are also critical requirements for edge

AI connectivity.

•

Inter-data center connectivity

Reliable high-speed connectivity is required

between all data centers that contribute to the

AI lifecycle, whether for the data lifecycle, the

agentic AI lifecycle, or both. Large volumes of data

are collected, consolidated, cleaned, normalized,

and duplicated across data centers. In addition,

foundation models need to be distributed to further

fine-tune the model to create domain-specific

models and address inference requirements.

Security

Large enterprise
AI data centers
Inferencing, AI agents

Metro

Core

Mass-scale
AI data centers

Cluster interconnect

Edge AI
data centers

Inferencing,
AI agents

AI agents

Colocation/sovereign
AI data centers
Inferencing, AI agents

Mass-scale
AI data centers

Edge connectivity

Inter-data center connectivity

Inter-cluster connectivity

Figure 6.  AI network connectivity across the cloud-to-edge continuum

© 2025  Cisco and/or its affiliates. All rights reserved.  |  9

White Paper  Cisco PublicMaking AI work for you.Cisco is meeting the diverse infrastructure needs of the AI lifecycle

As organizations move forward on their journey through

The fast pace of AI innovation and architectures requires

generative, multimodal, and now agentic AI, they

strong collaboration between technology partners to keep

need well-suited solutions that minimize risk and cost,

the evolving needs of organizations at the forefront.

maximize speed and efficiency, improve security, and

Cisco is expanding on established technology

address regulatory compliance.

partnerships and building new ones to ensure customers

The time is now. According to the 2024 McKinsey

Global survey, 75% of respondents believe AI will

usher in a disruptive change in their industry, and those

organizations that lag in AI adoption will risk becoming
irrelevant.10 And yet, according to the Cisco 2024 AI
Readiness Index, only 13% of companies are ready to

leverage AI-powered technologies to their full potential

have tried-and-tested technology stacks and timely

access to the most advanced AI technologies, including

accelerated compute, networking, storage, software

platforms, and liquid cooling, among others. Cisco has

established a deep partnership with NVIDIA to help

organizations accelerate and secure their AI initiatives by

delivering a secure AI factory.

today, while 85% of respondents say they have less

Cisco continues to innovate and support the full

spectrum of organizations and use cases that make

up the AI lifecycle ecosystem. Whether it’s training in

the cloud, inferencing in the enterprise data center, or

agents at the edge, Cisco solutions span everything

inside and between the largest to smallest cloud, data

center, and edge environments.

than 18 months to deploy an AI strategy before they
will see negative business effects.11

Cisco is revolutionizing how infrastructure and data

connect and protect organizations in the AI era.

Our AI infrastructure innovations and solutions are

helping organizations power and secure AI across

the continuum of highly varied needs from

hyperscalers, neoclouds, and enterprises to service

providers and colocation providers.

Our solutions build on technologies and products that

range from silicon to complete AI systems and span

networking, compute, optics, data center interconnect

systems, security, and observability. Organizations can

choose to adopt these technologies as validated

full-stack solutions with the option for simplified,

integrated management or as components that can

be used to build an optimized full stack. In either case,

organizations deploying their own AI infrastructure can

choose to use proven Cisco Validated Designs (CVDs)

and industry-leading AI reference architectures to

accelerate and streamline successful deployment.

© 2025  Cisco and/or its affiliates. All rights reserved.  |  10

White Paper  Cisco PublicMaking AI work for you.As a service

Integrated stack

Customizable solutions

Security

Assurance

AI Data Centers

Edge       |       Large-scale      |      Mass-scale

Wide Area Network/Data Center Interconnect

Cisco Silicon One unified architecture

Figure 7.  Cisco addresses AI infrastructure needs both within and between data centers at all scales and with a choice of deployment models

The Cisco AI infrastructure portfolio (Figure 7)

Specifically, the Cisco Silicon One G200 powers

provides organizations a choice of solutions and

ultra-high-performance Ethernet-based AI back-end

deployment models from cloud to core to edge that

networks that require advanced congestion avoidance

best meet specific business and technical workload

and fault recovery techniques to ensure maximum GPU

requirements. It also delivers the resilience needed

efficiency and low job completion times.

to operate securely at scale and at peak performance

within data centers, between them, and across the

entire connected landscape. It offers choices and

innovations that help accelerate time to deployment,

value, and full realization of the business opportunities

unlocked by AI.

Cisco Silicon One

G200-based switches support 800G port speeds, and

at 512, the industry’s highest radix. In comparison to a

256-radix switch, this reduces a large AI cluster from a

three-layer network to a two-layer network, requiring 50%

less optics and 40% fewer switches, which drastically

reduces the environmental footprint and latency of the
AI cluster.12

Cisco Silicon One provides a single cutting-edge

Cisco is partnering with NVIDIA to enable Cisco

semiconductor architecture that can be deployed

across a broad range of networks, from back-end and

front-end networks to data center interconnect

Silicon One-based switches to be coupled with NVIDIA
SuperNICs to become part of the NVIDIA SpectrumTM-X
Ethernet networking platform. Cisco is the only partner

and WANs. As AI workloads and networks evolve,

silicon included in NVIDIA Spectrum-X.

organizations can continue to evolve their AI infrastructure

with the Silicon One programmable architecture.

© 2025  Cisco and/or its affiliates. All rights reserved.  |  11

White Paper  Cisco PublicMaking AI work for you.AI-ready data centers

Cisco helps organizations efficiently deploy and

This allows organizations to either adopt an integrated

operate the best-performing Ethernet-connected data

AI full stack from Cisco or build their own AI stacks

centers at edge, regional, and centralized locations to

based on Cisco and partner technologies, depending

support both AI and traditional workloads. We provide

on their business and technology priorities.

the building blocks of silicon, networking, compute,

optics, and security, as well as fully integrated modular

and scalable stacks (Figure 8) that are purpose-built

for AI workloads.

Security

Assurance

AI Data Centers

Edge AI data centers
8–100 GPUs

Large-scale AI data centers
101–5000 GPUs

Mass-scale AI (cloud) data centers
5001–100,000+ GPUs

Cisco Secure AI Factory with NVIDIA

Full stack

Cisco Nexus Hyperfabric AI

Cisco AI PODs

Compute

AI network
fabric

Optics

Cisco AI-optimized UCS servers

Cisco 8000 Series with SONiC

Cisco Nexus 9000 Series Switches with Nexus Dashboard

Cisco optical transceivers

Wide Area Network/Data Center Interconnect

Cisco Silicon One unified architecture

Figure 8.  The Cisco AI data center portfolio delivers choice and innovation across mass-scale, large, and edge deployments

© 2025  Cisco and/or its affiliates. All rights reserved.  |  12

White Paper  Cisco PublicMaking AI work for you.Cisco AI network fabrics

Cisco Nexus 9000 Series Switches running the

widely adopted Nexus Operating System (NXOS) or

application-centric infrastructure (ACI) and Cisco 8000

Series platforms running Software for Open Networking

in the Cloud (SONiC) are engineered to meet the most

Meanwhile, the Cisco optics family also includes high-

speed QSFP modules for AI server connectivity. Cisco

is also innovating terabit speed pluggable optics and

contributing to new advances such as linear pluggable

optics (LPO) capabilities that can help improve AI fabric

switch power efficiencies.

stringent front-end and back-end networking demands

Cisco compute

Cisco AI-optimized servers are designed for

demanding use cases like AI fine-tuning and

inferencing, among others. With their future-ready,

highly modular architecture and their blend of high-

performance CPUs and optional GPU acceleration,

Cisco servers deliver efficient resource allocation for

diverse workloads. As an example, the Cisco Unified

Computing System (Cisco UCS) C885A M8 Rack Server

is a dense-GPU server designed to deliver scalable

accelerated compute capabilities to address the most

demanding AI workloads. For environments that require

flexible configurations across a broad range of AI use

cases, the Cisco UCS C845A M8 Rack Server, based

on NVIDIA MGX reference architecture, provides a

highly scalable, modular, and customizable platform.

With software-defined automation and streamlined

management, the Cisco Intersight cloud operations

platform provides Cisco servers with a simplified and

flexible operational environment.

of large-scale AI workloads. Specifically, Nexus 9000

and Cisco 8000 systems built on the Cisco Silicon One

G200 programmable ASIC supporting high-density

400G and 800G fabrics and a massive 512 radix makes

them ideal for scalable, next-generation leaf-and-spine

network designs. These switches use advanced load

balancing, innovative congestion management, and

flow control algorithms to help improve job completion

times (JCTs). They also provide the low latency and

telemetry needed to meet the design and operational

requirements of AI fabrics.

Cisco data center optics

Cisco optics innovation delivers on the key requirements

for AI optics—low power, performance, scale, and

reliability. In addition to technology innovation with

silicon photonics platforms, Cisco’s rigorous optics

testing, robust monitoring, enhanced reliability, and

additional performance margins are essential for AI

networks. Cisco enables a broad set of AI use cases

by supporting the two module form factors widely used

to connect clients and switches with high port density

and optimized thermal management. The Cisco OSFP

800G transceiver modules are based on the OSFP

specification commonly used in AI applications, while

the Cisco family of QSFP-DD modules maximize port

density for 100G and 800G with backward compatibility

to lower-speed QSFP modules.

© 2025  Cisco and/or its affiliates. All rights reserved.  |  13
© 2025 Cisco and/or its affiliates. All rights reserved.

White Paper  Cisco PublicMaking AI work for you.Cisco full-stack architecture—Cisco Nexus

Recognizing the unique paths organizations take in their

Hyperfabric AI

Cisco Nexus Hyperfabric AI is a vertically integrated

AI cluster designed to accelerate and simplify

deployments with plug-and-play cloud management.

With Cisco Nexus Hyperfabric AI clusters, organizations

are able to streamline the entire infrastructure lifecycle

process by deploying an innovative full stack that

AI journey, Cisco Secure AI Factory with NVIDIA offers

deployment flexibility by offering a complete vertically

integrated solution or a flexible modular AI architecture

tailored to support a broad range of needs. The

vertically integrated option integrates the Cisco AI

security portfolio into the Cisco Nexus Hyperfabric AI

full-stack solution.

integrates Cisco compute with NVIDIA GPUs and

Cisco full-stack architecture for

DPUs, Silicon One-based Cisco 6000 Series Switches,

inferencing—Cisco AI PODs

Cisco optics, and VAST Data storage. The reference

architecture includes NVIDIA AI Enterprise deployed

and supported on NVIDIA-certified Cisco UCS C885A

M8 Rack Servers and adheres to the NVIDIA Enterprise

Reference Architecture (Enterprise RA) for NVIDIA

HGX™ and Spectrum-X.

Cisco helps organizations get their inferencing

environments up and running with less time, effort,

and human error with Cisco AI PODs. With validated

configurations, rapid and consistent refreshes, and a

single support model, Cisco AI PODs help mitigate the

complexities of AI integration and deployment and deliver

Cisco full-stack architecture—Cisco Secure

a secure and scalable path from initial deployment to

AI Factory with NVIDIA

support for the most advanced applications.

Cisco is partnering with NVIDIA to empower

organizations to implement, optimize, and secure AI

deployments. Cisco Secure AI Factory with NVIDIA is

a secure and high-performance AI infrastructure that

integrates security, networking, compute, AI software,

and storage into a scalable full-stack system. Featuring

built-in security at every layer, superior networking,

and seamless integration with the NVIDIA AI Enterprise

software platform, it is purposefully designed to

enable organizations to streamline the development,

deployment, and protection of AI workloads.

© 2025  Cisco and/or its affiliates. All rights reserved.  |  14

White Paper  Cisco PublicMaking AI work for you.WAN and data center interconnect

Cisco delivers a full portfolio of WAN and Data Center

Cisco coherent pluggable optics

Interconnect (DCI) products and solutions to ensure

an uninterrupted and secure AI workflow across

distributed data center and edge environments.

The Cisco family of coherent pluggable optics plays a

significant role in enabling connectivity between data

centers and AI clusters. These optical transceivers

These solutions are designed to provide exceptionally

promote high-speed transmission, optimize power

reliable, secure, and intelligent connectivity for all three

efficiency, and simplify network architecture and

use cases: inter-cluster connectivity, any-to-any data

operations. They provide solutions for a wide range

center connectivity, and edge AI connectivity.

of data rates and AI applications over local intra-data

center, metro, long-haul, and ultra-long-haul reaches.

Security

Assurance

AI Data Centers

Edge       |       Large      |      Mass-scale

Wide Area Network/Data Center Interconnect

Pluggable Digital Coherent Optics (DCO), Optical Systems (Cisco NCS), Cisco 8000 Series, Routed Optical Networks

Cisco Agile Services Networking

Cisco Silicon One unified architecture

Figure 9.  Cisco Agile Services Networking delivers secure and flexible connectivity across the complete agentic AI workflow

© 2025  Cisco and/or its affiliates. All rights reserved.  |  15

White Paper  Cisco PublicMaking AI work for you.Cisco optical systems

Cisco Agile Services Networking and Cisco Routed

As data center interconnect requirements expand

Optical Networking

beyond the scale and distance addressed by

The Cisco Agile Services Networking architecture

coherent pluggable optics solutions, Cisco offers

enables flexibility in the deployment of large-scale

the Network Convergence System (NCS), a dense

infrastructures. This architecture features a highly

wavelength-division multiplexing (DWDM) line system.

efficient routing portfolio based on the Cisco 8000

The Cisco NCS 1000 Series are optimized to efficiently

platform and Cisco IOS XR, along with advanced

interconnect multiple AI data centers across a variety

technologies like segment routing SRv6 for scalability,

of use cases, distances, and throughputs ranging from

programmability, and resiliency. When combined with

2 Tbps to 28 Tbps.

Cisco SD-WAN

Cisco SD-WAN provides organizations with a robust

framework that can support the deployment and

management of agentic AI workflows combined with

other enterprise and cloud traffic by simplifying and

securing reliable connectivity between all locations.

Cisco SD-WAN optimizes network resources and

routes traffic intelligently so that AI workflows can

function effectively. The integration of Cisco SD-WAN

and Cisco Secure Access capabilities delivers a

cloud-native, integrated secure access service

edge (SASE) approach that protects AI data and

workflows across the cloud-to-edge continuum and

delivers network and security policy management and

enforcement consistently across all environments.

Cisco Routed Optical Networking innovations, this

architecture helps service providers significantly

lower TCO.

With the Cisco Agile Services Networking architecture,

service providers and organizations with large-scale

networking needs can optimize the delivery of assured

networking to customers and users. A single operating

system and unified management across both routing

and optical layers simplifies operations. Additionally,

Agile Services Networking integrates AI-enabled

assurance and automation with the Cisco Provider

Connectivity Assurance and Crosswork Network

Automation suites, enabling seamless and intelligent

network operations.

© 2025  Cisco and/or its affiliates. All rights reserved.  |  16

White Paper  Cisco PublicMaking AI work for you.Security and assurance

As AI becomes central to the running of almost

Cisco security and assurance solutions (Figure 10)

every organization, the ability to protect and ensure

can help organizations deliver AI-driven outcomes

the end-to-end service levels of AI workflows

consistently across the complete workflow with

becomes critical. The distribution of AI workflows

confidence and lower risk. That includes protecting

and agents across on-premises, hybrid, and

the data and maintaining the performance of training

multicloud environments attracts the increased

or inferencing clusters within data centers, interactions

risk of security threats and the need to ensure data

between inferencing and training models over a WAN,

integrity and confidentiality at every touch point.

or edge agents that are continually collaborating on

autonomous processes.

Security

Cisco Hypershield

Isovalent

Splunk

Assurance

Cisco ThousandEyes

Cisco AI Defense

Cisco DC Firewalls

Cisco Provider Connectivity Assurance

AI Data Centers

Edge       |       Large-scale      |      Mass-scale

Wide Area Network/Data Center Interconnect

Cisco Silicon One unified architecture

Figure 10.  Cisco security and assurance solutions deliver comprehensive digital resilience for AI workflows

© 2025  Cisco and/or its affiliates. All rights reserved.  |  17

White Paper  Cisco PublicMaking AI work for you.With the Cisco Cloud Protection Suite, organizations

AI workflows are becoming increasingly distributed

can dynamically protect applications and users wherever

and complex, requiring visibility and assurance at every

they are located. By automating segmentation and

stage to consistently ensure the required service levels.

using consistent zero-trust policies with an advanced

This is the case for the performance of training or

AI-enabled security architecture, organizations can

inferencing clusters within a data center, interactions

protect modern applications and AI-scale data centers

over a WAN between inferencing and LLMs,

across public, private, and hybrid clouds.

or for edge agents that are collaborating on an

The suite includes Cisco Hypershield and the Isovalent

autonomous process.

platform, both based on the extended Berkeley Packet

Cisco Splunk Observability Cloud delivers real-time

Filter (eBPF) technology that offers a modern approach

correlated visibility and insights across the complete

to securing cloud-native environments.

infrastructure to ensure the fastest time to troubleshoot

Cisco Hypershield delivers a unique, distributed,

AI-native security architecture based on Kubernetes

that is built specifically for AI workloads and designed

to put security wherever it needs to be. The solution is

designed to be AI-powered to automate security policy

lifecycle and security infrastructure upgrades. The

Isovalent platform provides zero-trust networking and

lightweight, highly efficient network observability and

security tools, all tailor-made for Kubernetes and

cloud environments.

and remediate issues. It integrates, aggregates, and

correlates data from a broad set of Cisco and third-

party monitoring and assurance tools, including

Cisco Nexus Dashboard, Cisco Provider Connectivity

Assurance, and Cisco ThousandEyes.

© 2025  Cisco and/or its affiliates. All rights reserved.  |  18

White Paper  Cisco PublicMaking AI work for you.Conclusion

No single architecture will satisfy all requirements of

Cisco is helping organizations build their AI capabilities

the variety of participants in the agentic AI ecosystem.

at all scales. Combinations of our Cisco 8000, Silicon

Mass-scale AI data center architectures required by

One, optics, and optical systems are being deployed

hyperscalers and neocloud providers for pre-training

by five of the largest hyperscalers in their mass-scale

and fine-tuning LLMs will differ substantially from those

back-end training networks. Our complete portfolio

required by enterprises for inferencing at the edge.

of Cisco-developed AI infrastructure technologies,

And these in turn will differ from the converged,

from silicon to full-stack systems, is designed to help

intelligent transport network spanning access and

AI ecosystem participants thrive in the agentic AI

metro and a highly scalable, future-proof IP core

era by delivering innovative solutions that meet the

required by communication service providers.

unique demands of complex and resource-intensive AI

workflows. These cutting-edge solutions span vertically

integrated full-stack systems, high-performance silicon,

optics, compute, networking, and software to meet AI

needs across the full spectrum of organizations

and use cases.

Explore how the Cisco AI infrastructure portfolio and mass-scale AI infrastructure

solutions can help your organization build efficient, high-performance AI

infrastructure faster while minimizing risk and maximizing ROI.

© 2025  Cisco and/or its affiliates. All rights reserved.  |  19

White Paper  Cisco Public© 2025 Cisco and/or its affiliates. All rights reserved. Notes

  1  Gartner Predicts 40% of Generative AI Solutions Will Be Multimodal By 2027, Gartner, September 9, 2024.

  2  Gartner Identifies the Top 10 Strategic Technology Trends for 2025, Gartner, October 21, 2024.

  3  Building a scalable foundation for AI’s future, Outshift, January 22, 2025.

  4  AI power: Expanding data center capacity to meet growing demand, McKinsey & Company, October 19, 2024.

  5  Gartner Forecasts Worldwide Public Cloud End-User Spending to Total $723 Billion in 2025, Gartner, November 19, 2024.

  6  Hype Cycle for Edge Computing, 2024, Gartner, July 15, 2024.

  7  AI Neocloud Playbook and Anatomy, SemiAnalysis, October 3, 2024.

  8  OpenAI o3 Breakthrough High Score on ARC-AGI-Pub, ARC Prize, December 20, 2024.

  9  Forecast Analysis: AI Semiconductors, Worldwide, Gartner, May 6, 2024.

10  The state of AI in 2023: Generative AI’s breakout year, McKinsey & Company, August 1, 2023.

11  Cisco 2024 AI Readiness Index, Cisco, 2024.

12  Cisco Silicon One Breaks the 51.2 Tbps Barrier, June 20, 2023.

White Paper  Cisco Public© 2025 Cisco and/or its affiliates. All rights reserved. Cisco and the Cisco logo are trademarks or registered trademarks of Cisco and/or its affiliates in the U.S. and other countries. To view a list of Cisco trademarks, go to this URL: www.cisco.com/go/trademarks. Third-party trademarks mentioned are the property of their respective owners. The use of the word partner does not imply a partnership relationship between Cisco and any other company. (1110R)  04/25