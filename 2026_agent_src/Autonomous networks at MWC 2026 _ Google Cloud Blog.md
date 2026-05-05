> Source: https://cloud.google.com/blog/topics/telecommunications/autonomous-networks-at-mwc-2026

Autonomous networks at MWC 2026 | Google Cloud Blog[Jump to Content](./#content)

[Cloud](https://cloud.google.com/ "Google Cloud")

[Blog](https://cloud.google.com/blog/ "Google Cloud Blog")

[Contact sales](https://cloud.google.com/contact/) [Get started for free](https://console.cloud.google.com/freetrial/)

[Cloud](https://cloud.google.com/ "Google Cloud")

[Blog](https://cloud.google.com/blog/ "Google Cloud Blog")

* Solutions & technology
  + [AI & Machine Learning](https://cloud.google.com/blog/products/ai-machine-learning)
  + [API Management](https://cloud.google.com/blog/products/api-management)
  + [Application Development](https://cloud.google.com/blog/products/application-development)
  + [Application Modernization](https://cloud.google.com/blog/products/application-modernization)
  + [Chrome Enterprise](https://cloud.google.com/blog/products/chrome-enterprise)
  + [Compute](https://cloud.google.com/blog/products/compute)
  + [Containers & Kubernetes](https://cloud.google.com/blog/products/containers-kubernetes)
  + [Data Analytics](https://cloud.google.com/blog/products/data-analytics)
  + [Databases](https://cloud.google.com/blog/products/databases)
  + [DevOps & SRE](https://cloud.google.com/blog/products/devops-sre)
  + [Maps & Geospatial](https://cloud.google.com/blog/topics/maps-geospatial)
  + Security
    - [Security & Identity](https://cloud.google.com/blog/products/identity-security)
    - [Threat Intelligence](https://cloud.google.com/blog/topics/threat-intelligence)
  + [Infrastructure](https://cloud.google.com/blog/products/infrastructure)
  + [Infrastructure Modernization](https://cloud.google.com/blog/products/infrastructure-modernization)
  + [Networking](https://cloud.google.com/blog/products/networking)
  + [Productivity & Collaboration](https://cloud.google.com/blog/products/productivity-collaboration)
  + [SAP on Google Cloud](https://cloud.google.com/blog/products/sap-google-cloud)
  + [Storage & Data Transfer](https://cloud.google.com/blog/products/storage-data-transfer)
  + [Sustainability](https://cloud.google.com/blog/topics/sustainability)
* Ecosystem
  + [IT Leaders](https://cloud.google.com/transform)
  + Industries
    - [Financial Services](https://cloud.google.com/blog/topics/financial-services)
    - [Healthcare & Life Sciences](https://cloud.google.com/blog/topics/healthcare-life-sciences)
    - [Manufacturing](https://cloud.google.com/blog/topics/manufacturing)
    - [Media & Entertainment](https://cloud.google.com/blog/products/media-entertainment)
    - [Public Sector](https://cloud.google.com/blog/topics/public-sector)
    - [Retail](https://cloud.google.com/blog/topics/retail)
    - [Supply Chain](https://cloud.google.com/blog/topics/supply-chain-logistics)
    - [Telecommunications](https://cloud.google.com/blog/topics/telecommunications)
  + [Partners](https://cloud.google.com/blog/topics/partners)
  + [Startups & SMB](https://cloud.google.com/blog/topics/startups)
  + [Training & Certifications](https://cloud.google.com/blog/topics/training-certifications)
  + [Inside Google Cloud](https://cloud.google.com/blog/topics/inside-google-cloud)
  + [Google Cloud Next & Events](https://cloud.google.com/blog/topics/google-cloud-next)
  + [Google Cloud Consulting](https://cloud.google.com/blog/topics/consulting)
  + [Google Maps Platform](https://mapsplatform.google.com/resources/blog/)
  + [Google Workspace](https://workspace.google.com/blog)
* [Developers & Practitioners](https://cloud.google.com/blog/topics/developers-practitioners)
* [Transform with Google Cloud](https://cloud.google.com/transform)

[Contact sales](https://cloud.google.com/contact/) [Get started for free](https://console.cloud.google.com/freetrial/)

Telecommunications

# From framework to scale: Accelerating autonomous networks at MWC 26

March 3, 2026

##### Muninder Sambi

VP, PM and GM, Networking, Google Cloud

##### Dave Weissman

Principal Engineer, Google Cloud

Last year, we [unveiled](https://cloud.google.com/blog/topics/telecommunications/the-autonomous-network-operations-framework-for-csps?e=48754805) our Autonomous Network Operations framework — a blueprint for Communication Service Providers (CSPs) to move beyond siloed automation toward self-healing, "zero-touch" networks. Today, we’re pivoting from networks that merely use AI for insights to intelligent agents capable of sensing, reasoning, and taking autonomous action.

As we head into [Mobile World Congress (MWC) Barcelona](https://www.mwcbarcelona.com/attend/?utm_source=google&utm_medium=cpc&utm_campaign=2026_branded_keywords&gad_source=1&gad_campaignid=23289977275&gbraid=0AAAAABWXNX9yakkuYJL0MGAUWVSt7SisT&gclid=Cj0KCQiAtfXMBhDzARIsAJ0jp3D4qzEKG5dZEUsgaCYorrGm__5_MphC7fa8M_l7c_N2itmwNiTVgdwaAo1xEALw_wcB), we’re demonstrating how this shift is becoming a reality. By embedding AI into the heart of operations, companies like [Deutsche Telekom](https://www.telekom.com/en) and [Vodafone](https://www.vodafone.com/) are reducing operational complexity and turning connectivity from a utility into a value-creating engine.

### **Product innovation: The engine of the agentic telco**

A key goal of the industry is to achieve [Level 4 to 5 autonomy](https://www.tmforum.org/wp-content/uploads/2019/05/22553-Autonomous-Networks-whitepaper.pdf): a network that identifies, diagnoses, and fixes its own problems without human intervention. To do this, the underlying data platform must be as dynamic as the network itself. Over the last year, we’ve evolved our [Cloud Spanner Graph](https://cloud.google.com/products/spanner/graph) and [Vertex AI](https://cloud.google.com/vertex-ai) to handle the "dual nature" of telcos: the need for high-speed, real-time response for alarm correlation, combined with deep, historical pattern detection.

Today, we’re refining our platform to support these autonomous operations through:

* **The network digital twin:** The network digital twin has evolved from a static map into a dynamic, temporal graph that represents the network’s live physical and logical state. It captures real-time performance and fault conditions while allowing agents to query historical states — such as the network’s appearance five hours or days ago — to perform instant, accurate root-cause analysis.
* **Unified graph data layer:** We’re breaking down the silos between operational and analytical data. By leveraging Spanner Graph for digital twins and federated graph analytics through [BigQuery](https://cloud.google.com/bigquery?e=48754805), telcos can interoperate between real-time updates and deep historical analysis without complex, slow ETL (Extract, Transform, Load) processes.
* **Real-time predictions with GNN:** Operators can now train [Graph Neural Networks](https://research.google/blog/graph-neural-networks-in-tensorflow/) (GNNs) on their network digital twin data in Vertex AI. They can then use the trained GNN models, along with Spanner’s [ML.PREDICT](https://docs.cloud.google.com/spanner/docs/ml-tutorial) capability and the real-time data in the network digital twin, to move from monitoring to predicting, mathematically tracking how a failure might propagate, and resolving it before it impacts subscribers.

### **Solution updates: Accelerating time-to-value**

One of the biggest hurdles to achieving Level 4 to 5 autonomy is manual delays caused by disconnected legacy systems. We’re launching new tools to replace bottlenecks with a unified, automated system:

* **Open-source data foundation:** To accelerate adoption, we’re [releasing](https://github.com/GoogleCloudPlatform/telco-autonomous-networks-data-demo) our telco data pipeline and data models source code on GitHub. CSPs can now implement unified industry-standard ontologies without manual schema mapping.
* **New telco agents:** In partnership with [FutureConnections](https://futureconnections.com/), we’re launching two new proof-of-value agents:
  + **Data steward agent:** An agentic workflow that automates data governance to ensure digital twins remain accurate.
  + **Autonomous network agents:** Currently being trialed by [One NZ](https://one.nz/), these agents manage voice core and OSS networks, moving beyond monitoring to active execution — like independently rerouting traffic or resetting network settings to restore call quality the moment a drop is detected.

### **Ecosystem momentum: Innovation in action**

True autonomy requires a vibrant ecosystem. This year, we’re highlighting several key milestones:.

* **MasOrange & NetAI:** We’re working with [NetAI](https://www.netai.ai/) to deliver GraphML-based AIOps. Together, we’ve launched a pilot project with [MasOrange](https://masorange.es/en/) that demonstrates how specialized partner models can run on Google Cloud’s AI stack to resolve network incidents while providing the confidence for autonomous action.
* **Nokia "Network as Code":** We’re partnering with Nokia to make networks fully programmable by turning complex technical code into AI agents that understand everyday language. This allows telcos to simply ask the network to perform complex tasks — like prioritizing network resources for critical services like emergency response or remote healthcare — without needing any manual engineering.

### **Looking ahead**

The agentic AI era is here. By embedding AI into the fabric of a telco’s network, we’re helping operators transform from connectivity utilities into intelligent service providers that continue to delight customers.

Join us at MWC: Visit booth #2H40 in Hall 2 to see these solutions in action, including live demonstrations of multi-agent systems, digital twins, and physical AI robots. You can also dive deeper into our approach by downloading our latest [whitepaper](https://services.google.com/fh/files/misc/autonomous_network_operations.pdf).

#### 2026 AI Agent Trends in Telecommunications

Leading telecommunications companies are moving beyond debating AI's possibilities and are now deploying semi-autonomous AI agents to drive measurable business value—delivering everything from concierge-style customer service to A2A-powered agentic networks.

[Read it now.](https://cloud.google.com/resources/content/ai-agent-trends-telecommunications-2026)

![https://storage.googleapis.com/gweb-cloudblog-publish/images/Confirmation_email_500x450_bAmzURz.max-500x500.png](https://storage.googleapis.com/gweb-cloudblog-publish/images/Confirmation_email_500x450_bAmzURz.max-500x500.png)

Posted in

* [Telecommunications](https://cloud.google.com/blog/topics/telecommunications)
* [Partners](https://cloud.google.com/blog/topics/partners)

##### Related articles

[![https://storage.googleapis.com/gweb-cloudblog-publish/images/24_-_Networking_vCB4Wjq.max-700x700.jpg](https://storage.googleapis.com/gweb-cloudblog-publish/images/24_-_Networking_vCB4Wjq.max-700x700.jpg)

Networking

### The AI-native core: Highly resilient telco architecture using Google Kubernetes Engine

By Abhi Maras • 5-minute read](https://cloud.google.com/blog/products/networking/gke-for-telco-building-a-highly-resilient-ai-native-core)

[![https://storage.googleapis.com/gweb-cloudblog-publish/images/36_-_Telecommunications_JbrVct8.max-700x700.jpg](https://storage.googleapis.com/gweb-cloudblog-publish/images/36_-_Telecommunications_JbrVct8.max-700x700.jpg)

Telecommunications

### Fueling the autonomous network: Google Cloud and DigitalRoute simplify data readiness for AI

By Manisha Gupta • 4-minute read](https://cloud.google.com/blog/topics/telecommunications/partnering-with-digitalroute-on-reusable-data-pipelines)

[![https://storage.googleapis.com/gweb-cloudblog-publish/images/36_-_Telecommunications_JbrVct8.max-700x700.jpg](https://storage.googleapis.com/gweb-cloudblog-publish/images/36_-_Telecommunications_JbrVct8.max-700x700.jpg)

Telecommunications

### The rise of the autonomous network: How GraphML is redefining telecom operations

By Naresh Rao • 5-minute read](https://cloud.google.com/blog/topics/telecommunications/graphml-and-digital-twins-enable-autonomous-networks)

[![https://storage.googleapis.com/gweb-cloudblog-publish/images/36_-_Telecommunications_JbrVct8.max-700x700.jpg](https://storage.googleapis.com/gweb-cloudblog-publish/images/36_-_Telecommunications_JbrVct8.max-700x700.jpg)

Telecommunications

### Scaling the autonomous network: Introducing the Data Steward and Core Network Agents

By Naresh Rao • 5-minute read](https://cloud.google.com/blog/topics/telecommunications/new-agents-for-the-autonomous-network-operations-framework)

### Footer Links

#### Follow us

* [Google Cloud](https://cloud.google.com/)
* [Google Cloud Products](https://cloud.google.com/products/)
* [Privacy](https://myaccount.google.com/privacypolicy?hl=en-US)
* [Terms](https://myaccount.google.com/termsofservice?hl=en-US)
* [Cookies management controls](#)

* [Help](https://support.google.com)
* Language‪English‬‪Deutsch‬‪Français‬‪한국어‬‪日本語‬