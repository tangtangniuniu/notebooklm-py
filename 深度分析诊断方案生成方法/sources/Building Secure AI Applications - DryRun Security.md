> Source: https://www.dryrun.security/resources/owasp-top-10-llm-building-secure-applications

Building Secure AI Applications | DryRun Security




 

By clicking **“Accept All Cookies”**, you agree to the storing of cookies on your device to enhance site navigation, analyze site usage, and assist in our marketing efforts. View our [Privacy Policy](#) for more information.

[Preferences](#)[Deny](#)[Accept](#)

Privacy Preference Center

When you visit websites, they may store or retrieve data in your browser. This storage is often necessary for the basic functionality of the website. The storage may be used for marketing, analytics, and personalization of the site, such as storing your preferences. Privacy is important to us, so you have the option of disabling certain types of storage that may not be necessary for the basic functioning of the website. Blocking categories may impact your experience on the website.

[Reject all cookies](#)[Allow all cookies](#)

Manage Consent Preferences by Category

Essential

**Always Active**

These items are required to enable basic website functionality.

Marketing

Essential

These items are used to deliver advertising that is more relevant to you and your interests. They may also be used to limit the number of times you see an advertisement and measure the effectiveness of advertising campaigns. Advertising networks usually place them with the website operator’s permission.

Personalization

Essential

These items allow the website to remember choices you make (such as your user name, language, or the region you are in) and provide enhanced, more personal features. For example, a website may provide you with local weather reports or traffic news by storing data about your current location.

Analytics

Essential

These items help the website operator understand how its website performs, how visitors interact with the site, and whether there may be technical issues. This storage type usually doesn’t collect information that identifies a visitor.

[Confirm my preferences and close](#)

## Please enter your information to download the resource

First Name\*

Last Name\*

Email Address\*

Company Name\*

By submitting this form, I agree to receive email updates about DryRun Security. The information will be used in accordance with the terms of our [privacy policy](/privacy-policy).

Thank you for submitting your information! You can download the guide here:   
‍

[Download the Guide](#)

Oops! Something went wrong while submitting the form.

[![](https://cdn.prod.website-files.com/645932d9286e9c20dd8e0fca/688b80486034525524cedf86_DRS-Logo-icon-green-white-dark%20background.svg)](/)

Product

[SAST](/product/sast)[PR Code Reviews](/product/pr-code-reviews)[Repository Reviews](/product/sast-deepscan-full-repository-security-scan)[Custom Code Policies](/product/custom-code-policies)[Codebase Intelligence](/product/codebase-intelligence)[Secrets](/product/application-security-secrets)[Infrastructure as Code (IaC)](/product/infrastructure-as-code-iac-security)

[Customers](https://www.dryrun.security/customers)

Resources

resources

[Blog](/blog)[FAQ](/faqs)[Resource Library](/resources)

Compare

[DryRun vs. Semgrep](/compare/dryrunsecurity-vs-semgrep)

Company

[About Us](/about)[Newsroom](/newsroom-copy)

[Docs](https://docs.dryrun.security)[Log In](https://app.dryrun.security/login)

[Get a Demo](#)

![]()

# Building Secure AI Applications

![](https://cdn.prod.website-files.com/645932d9286e9c20dd8e0fca/645daace3cf060ba150f0f95_Burst-circle-1.svg)

Thank you for submitting your information!  
You can download the guide here:

[Download the guide](#)

Oops! Something went wrong while submitting the form.

## Key Benefits of Building Secure AI Applications

![]()

###

![]()

###

![]()

###

![]()

###

WRITTEN BY:

No items found.

[Download the guide](#form)

[![](https://cdn.prod.website-files.com/645932d9286e9c20dd8e0fca/688b80486034525524cedf86_DRS-Logo-icon-green-white-dark%20background.svg)](/)

![](https://cdn.prod.website-files.com/645932d9286e9c20dd8e0fca/673cdbd6371bb806c3abab51_21972-312_SOC_NonCPA%20(1).png)![Austin Inno 2025 Startups to Watch Logo](https://cdn.prod.website-files.com/645932d9286e9c20dd8e0fca/67ffe855d5690f87dbe5c61b_AustinInno%202025%20Startups%20to%20Watch%20logo%20(1).webp)![](https://cdn.prod.website-files.com/645932d9286e9c20dd8e0fca/678a999f8a034f0b0324327a_blackhat-finalist-white.svg)

Links

[Blog](/blog)[Resources](/resources)[FAQ](/faqs)[Docs](https://docs.dryrun.security)[Brand Guidelines](/brand-guidelines)

Product

[SAST](/product/sast)[Resources](/resources)[PR Code Reviews](/product/pr-code-reviews)[Repository Reviews](/product/sast-deepscan-full-repository-security-scan)[Custom Code Policies](/product/custom-code-policies)[Codebase Intelligence](/product/codebase-intelligence)[Secrets](/product/application-security-secrets)[Infrastructure as Code (IaC)](/product/infrastructure-as-code-iac-security)

Social

[Site by Ammo](https://www.ammo.studio)

© XXXX DryRun Security. All rights reserved.

[Privacy Policy](/privacy-policy)[Terms of Service](/terms-of-service)[Code Safety](/code-safety)[Cookies Settings](#)

[![](https://cdn.prod.website-files.com/645932d9286e9c20dd8e0fca/688b80486034525524cedf86_DRS-Logo-icon-green-white-dark%20background.svg)](/)

Product

[SAST](/product/sast)[PR Code Reviews](/product/pr-code-reviews)[Repository Reviews](/product/sast-deepscan-full-repository-security-scan)[Custom Code Policies](/product/custom-code-policies)[Codebase Intelligence](/product/codebase-intelligence)[Secrets](/product/application-security-secrets)[Infrastructure as Code (IaC)](/product/infrastructure-as-code-iac-security)

[Customers](https://www.dryrun.security/customers)

Resources

resources

[Blog](/blog)[FAQ](/faqs)[Resource Library](/resources)

Compare

[DryRun vs. Semgrep](/compare/dryrunsecurity-vs-semgrep)

Company

[About Us](/about)[Newsroom](/newsroom-copy)

[Docs](https://docs.dryrun.security)[Log In](https://app.dryrun.security/login)

[Get a Demo](#)

Table of Contents

[Executive Summary](#executive-summary)[A Guide to the OWASP Top Ten for LLM Apps](#top-ten)[LLM01 Prompt Injection](#llm01)[LLM02 Sensitive Information Disclosure](#llm02)[LLM03 Supply Chain](#llm03)[LLM04 Data and Model Poisoning](#llm04)[LLM05 Improper Output Handling](#llm05)[LLM06 Excessive Agency](#llm06)[LLM07 System Prompt Leakage](#llm07)[LLM08 Vector and Embedding Weaknesses](#llm08)[LLM09 Misinformation](#llm09)[LLM10 Unbounded Consumption](#llm10)[Managing LLM Top Ten Risks - A Reference Architecture](#managing-llm)[DryRun Security: Risk Reduction for LLM-enabled Applications](#risk-reduction)[Appendix: Control Coverage Map](#control-coverage)[Appendix: Mapping OWASP LLM Risks to the Architecture](#mapping-owasp)

Building Secure AI Applications

[Download](#download-content)

Share

[Linkedin](#)[X](#)[Facebook](#)

# Building Secure AI Applications

A guide and architecture for building AI enabled apps and systems securely with the OWASP Top 10 for LLM Applications

![](https://cdn.prod.website-files.com/645932d9286e9c20dd8e0fca/68f64ebd9a54068a291c1e92_dryrun-background%20(1).webp)

## Executive Summary

At many companies, LLMs and AI systems are moving from experiments to core product features, apps, or APIs. Many view AI as having significant potential for customer acquisition, unlocking a new market, or tapping into a new competitive edge for their organization. All are great reasons which are rapidly driving LLM integration. However, now an LLM that reads customer records, executes tools, runs unfiltered inputs, calls internal APIs, or drafts code sits on your critical path. This creates wide open doors for attackers and has [resulted in dozens of exploits to date](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/). LLM integrations require security thinking that is specific to LLM failure modes, not just generic web controls.

This whitepaper gives engineering and application security leaders a practical guide to design and defend LLM applications or LLM-enabled applications with the OWASP Top 10 for LLM Applications as the backbone. We use the current 2025 categories from OWASP and translate each into:

* What the risk is and why it matters in production
* A real incident or research example
* Threat model and common failure modes
* Valuable tools (beyond DryRun Security) to counter each vulnerability
* Controls and mitigations you can build into architecture and the SDLC

OWASP and its contributors have done the industry a real service by turning LLM risk into a concrete Top Ten that engineering and security teams can design against. As an AI‑native code security intelligence company, DryRun Security aids directly in that work, helping customers harden their stacks against eight of the ten OWASP LLM risks across real codebases and services. In the final section of this paper, we show exactly where DryRun plugs into the reference architecture so you can see how those risks are reduced in practice.

We close this paper with a reference architecture built on our experience, a design checklist, and an appendix mapping controls to common LLM patterns like RAG, tool use, and agent frameworks. The goal is simple: help you rapidly ship LLM capabilities that are resilient, observable, and boring-in-a-good-way. 

### Control Architecture with LLM Risk Mappings

This diagram shows our suggested architecture and how it aligns with the OWASP Top 10 Risks for LLM Applications.

![](https://cdn.prod.website-files.com/645932d9286e9c20dd8e0fca/6945a1a11b85d8490f495e48_dryrun-graphic1%20(1).webp)

Most teams will phase these controls in over time, so use the OWASP LLM Top Ten and the reference architecture to decide which guardrails deliver the highest risk reduction for your environment, not to implement everything at once.

![](https://cdn.prod.website-files.com/645932d9286e9c20dd8e0fca/68f64ebd9a54068a291c1e92_dryrun-background%20(1).webp)

## A Guide to the OWASP Top Ten for LLM Apps

‍[The OWASP Top Ten for LLM Applications](https://genai.owasp.org/resource/owasp-top-10-for-llm-applications-2025/) (or, “LLM Top Ten”) gives engineering and security leaders a shared vocabulary for risks that appear once models touch real systems and data. Traditional web controls still matter, but LLM features introduce new failure modes. Models can be steered by hostile inputs, they can output executable text, and they can act through tools.  Essentially, the core principles that the OWASP Top 10 made famous can be applied to understand risk in modern LLM application development.

Treat the model as untrusted compute, and treat both inputs and outputs as tainted until proven otherwise. With that mindset, the Top Ten becomes a practical checklist for design and build.

##### The advice throughout this paper is to use the OWASP LLM Top Ten as your risk taxonomy and to build controls directly into this architecture.

After presenting our take on how to frame each of the risks, we use a simple reference architecture to anchor the discussion: client traffic flows through an API gateway to a policy layer, then to an orchestrator that handles retrieval and tools, with guarded access to data stores and model providers. Observability and a security lake record what happened.

That means policy and guardrails outside the model, least privilege for tools, provenance for data, and budgets that keep costs and latency inside the lines.

Here is where the risks map in practice. Prompt Injection hits the policy layer, the agent planner, and RAG retrieval; Sensitive Information Disclosure hits the policy layer and data connectors, plus provider tenancy and logging; Supply Chain hits model weights, libraries, model servers, and model hubs; Data and Model Poisoning hits training data, fine tuning, and RAG corpora; Improper Output Handling hits the boundary between model output and your code, UIs, and tools; Excessive Agency hits tool proxies and credentials; System Prompt Leakage hits the policy layer; Vector and Embedding Weaknesses hit the RAG store and retrieval configuration; Misinformation hits product correctness and legal risk; Unbounded Consumption hits orchestrators, retries, and cost controls.

For a leader designing secure architecture, this mapping tells you where to place controls and which teams own them. Policy and schema enforcement belong with platform and AppSec, tool mediation with the service owners, vector store hygiene with data and ML, and budgets with SRE and FinOps. Assign clear owners, wire the measurements early, and you will turn the Top Ten from a scary list into a predictable set of guardrails that let teams ship faster and safer.

![](https://cdn.prod.website-files.com/645932d9286e9c20dd8e0fca/68f64ebd9a54068a291c1e92_dryrun-background%20(1).webp)

### **LLM01 - Prompt Injection**

Prompt injection happens when an attacker places instructions in a user prompt or in content your system later retrieves, and the model treats those instructions like policy. The result is an LLM that ignores rules, leaks data, or calls tools in ways you did not intend. OWASP defines LLM01 as crafted inputs that alter an LLM’s behavior or outputs in unintended ways. Treat the model as untrusted compute and treat every token that enters or leaves it as tainted until you validate it.

### Why leaders care

The risk of injection is not merely theoretical. As recently as September 2025, Salesforce and Noma Security  announced [ForcedLeak](https://noma.security/blog/forcedleak-agent-risks-exposed-in-salesforce-agentforce/),  an example of an indirect injection attack where an open web form could deliver malicious prompts to back end systems and leak sensitive CRM data to the attackers.

In systems that utilize LLM tooling, benchmarks indicate significant rates of agent compromise stemming from direct and indirect injections embedded within chatbots, web pages, PDF documents, tickets, and emails. Consequently, the combination of retrieval capabilities and tool integration presents a substantial blast radius if controls are not enforced external to the model itself.

### What controls are needed

A policy layer outside the LLM should act as middleware that assembles prompts, tags or strips untrusted content, enforces structured outputs, and mediates every tool call. Treat it like any other critical service. Keep it versioned, testable, and auditable so changes can be reviewed and rolled back. This layer belongs to your platform or AppSec team, not to the model provider, and it should expose clear APIs that product teams can adopt without rewriting prompts.

Every integration must pass through a tool proxy with guard policies. The proxy validates arguments against JSON Schema, enforces role based access controls, applies least privilege with time bound credentials, and restricts network egress to approved destinations. Destructive or financial operations require explicit human approval. Log inputs and outputs with full provenance for investigation.

Finally, enforce RAG ingestion and retrieval hygiene. The class of tools arising here fall into AI Detection and Response (AIDR) as they moderate and sanitize content as it enters the knowledge base, records provenance, and tags each item by tenant and sensitivity.

At retrieval time, ACL filters content embedded or shown to the model. This keeps hostile instructions and cross tenant data from entering the context window. Add quarantine for suspicious documents, and maintain index hygiene with re‑embedding and duplicate suppression so the store stays trustworthy over time. ‍

### **Tools to consider**

###### **Policy layer outside the LLM |** **NVIDIA NeMo Guardrails**

**‍**Programmable “rails” that sit between your app and the model to enforce structure, topic bounds, and jailbreak resistance in code you control. [**https://docs.nvidia.com/nemo-guardrails/**](https://docs.nvidia.com/nemo-guardrails/)

###### **Tool proxy with guard policies |** **Knostic Prompt Gateway**

**‍**Why: Real‑time prompt inspection and sanitization with governance features that validate requests, restrict egress, and log enforcement for audits. [**https://www.knostic.ai/**](https://www.knostic.ai/)

###### **RAG ingestion and retrieval hygiene | HiddenLayer AI Detection and Response (AIDR)**

**‍**Visibility and detection around generative pipelines that can intercept LLM traffic and flag risky content or behaviors around ingestion and retrieval. [**https://hiddenlayer.com/aidr/**](https://hiddenlayer.com/aidr/)

###### **RAG / Retrieval Hygiene |** **Cleanlab Trust Scoring and Output Reliability**

Complements security guardrails by helping systems identify and block low-trust answers that result from prompt injection, bad retrieval, or missing context.   
‍[**https://cleanlab.ai**](https://cleanlab.ai/)

###### **Code check for missing prompt controls |** **DryRun Security**

**‍**Context‑aware code analysis that helps you locate prompt‑handling paths without schema checks, redaction, or tool gating so you can fix issues before runtime. [**https://www.dryrun.security/**](https://www.dryrun.security/?__hstc=17958374.d97118fd58985a2cd40d869f4756070e.1757443863900.1765225963168.1765236343186.25&__hssc=17958374.2.1765236343186&__hsfp=1786095904)

There’s a reason this is at the top of the list. This problem is hard and while these tools help, none are perfect.

## The one dollar SUV that went viral

##### **What happened**

Pranksters persuaded a Chevrolet dealership’s website chatbot to agree with anything the user said and to mark replies as legally binding. The bot then “accepted” a sale of a new Chevy Tahoe for one dollar. The vendor pulled the bot and the story spread across tech and auto media.

##### **The cost**

The dealership had to pull the chatbot offline, deal with viral coverage of the “$1 Tahoe,” and spend engineering and legal time dissecting what happened and whether any messages could be considered binding. Even if no car ever left the lot for a dollar, the episode burned trust, created potential dispute risk with customers, and turned a “smart” sales assistant into a public reliability and governance problem.

##### **Takeaway**‍

Do not let an LLM treat user prompts as policy. Guardrails and contracts must live in code and policy layers, not in natural‑language back‑and‑forth with a chatbot. Treat all user input as untrusted, prevent the model from making legal or pricing commitments on its own, and test agents with adversarial prompts so they cannot be talked into promises your business never intended to keep.

![](https://cdn.prod.website-files.com/645932d9286e9c20dd8e0fca/68f64ebd9a54068a291c1e92_dryrun-background%20(1).webp)

### **LLM02 - Sensitive Information Disclosure**

Sensitive Information Disclosure covers leaks of personal data, secrets, system details, and confidential business context through an LLM application. Leakage can happen at many spots: prompts and retrieved documents that contain PII, completions that echo secrets, logs and analytics that capture raw payloads, connectors and tools that fetch or post sensitive data, and provider policies that retain inputs longer than you expect.

OWASP’s LLM02 scope explicitly includes PII, financial and health data, credentials, and internal business information, as well as sensitive model artifacts in proprietary systems.

### Why leaders care

The business and regulatory exposure is real. In March 2023 OpenAI took ChatGPT offline after a Redis client library bug exposed some users’ chat titles and parts of Plus subscribers’ payment information to other users viewing their account pages. OpenAI’s postmortem and independent coverage place the impact at roughly 1.2 percent of Plus users during a specific window. Incidents like this convert instantly into trust and legal risk, not just engineering cleanup.

Supervisory action is also escalating and we’re seeing more legislation being passed around the damages of AI, and exposing sensitive information is generally towards the top of the hit list for legislators. Italy’s data protection authority announced a 15 million euro fine for ChatGPT in December 2024, citing transparency and data handling issues, then continued related proceedings into 2025. You do not need to operate in the EU to feel the ripple effects because enterprise buyers will benchmark you against the strictest regions.

### **What controls are needed**

##### Minimize and mediate at the boundary

Redact or replace PII and secrets with vault tokens before prompts are constructed and scrub completions before storage or display. Pass references or summaries where possible instead of raw records. Enforce strict structured outputs so you can reliably intercept sensitive fields. Treat any third party or provider call as a privacy boundary with explicit contracts for data use, retention, and regional processing. Azure and OpenAI both publish product‑tier specifics that you can attach to procurement and design reviews.

##### Isolate sensitive data

Use per‑tenant encryption and access control that you enforce outside the model. Put high value identifiers in a vault or tokenization service so that prompts carry tokens, not raw values. In RAG, honor the original ACLs before retrieval and enforce row‑level filtering at the API layer. Keep vector and cache stores off the public internet with proper auth, and treat embeddings as sensitive when the underlying content is sensitive.

##### Instrument, retain narrowly, and review

Instrument prompts, retrieved chunks, completions, tool calls, and egress while avoiding raw storage of sensitive payloads. Mask high‑risk fields by default, keep retention short, and prevent logs from becoming a shadow data lake. Add canary tokens to detect exfiltration, scan repositories and configs for secrets, and run continuous tests that try to recall cross‑tenant data after resets. Document exceptions and renew them with explicit risk owners.

### **Tools to consider**

Below are practical options that teams use today. Each tool fills a different role. Mix to match your architecture and compliance needs.

###### **Microsoft Presidio**

**‍**Open source PII detection and anonymization for text, images, and PDFs, suitable for pre‑prompt redaction and log scrubbing.  
[**https://microsoft.github.io/presidio/**](https://microsoft.github.io/presidio/)

###### **Pangea Redact API**

**C**ode‑first redaction service for removing sensitive strings from  
text at ingestion and in pipelines.  
[**https://pangea.cloud/docs/api/redact**](https://pangea.cloud/docs/api/redact)

###### **Provider configuration** ‍

Select tiers that align with your policy.  
Azure OpenAI data privacy: [**https://learn.microsoft.com/en-us/legal/cognitive-services/openai/data-privacy  
OpenAI business data: https://openai.com/business-data/**](https://learn.microsoft.com/en-us/legal/cognitive-services/openai/data-privacy)

###### Integrated Sanitization and Data Validation **| DryRun Security**

Identify points of overly detailed or unsanitized logging, ensure data access controls are used through code policies, context-aware input validation.  
[**https://www.dryrun.security/**](https://www.dryrun.security/?__hstc=17958374.d97118fd58985a2cd40d869f4756070e.1757443863900.1765225963168.1765236343186.25&__hssc=17958374.2.1765236343186&__hsfp=1786095904)

## A small bug and a big lesson

##### **What happened**

On March 20, 2023 a bug in an open source Redis client caused ChatGPT to expose other users’ chat titles and, for about 1.2 percent of Plus subscribers, limited payment data through the account page. OpenAI pulled the service down, published a postmortem, and patched the issue.

##### **The cost**

Service downtime, incident response hours, increased scrutiny from regulators and enterprise buyers, and lasting reminders to design observability and privacy controls to be prepared for *when* a breach will happen and not hoping it does not.

##### **Takeaway**

Treat every boundary as an exposure point. Redact and minimize before prompts, isolate sensitive data in vaults, and keep provider and logging retention tight. Assume an incident will occur and make the blast radius minimal.

![](https://cdn.prod.website-files.com/645932d9286e9c20dd8e0fca/68f64ebd9a54068a291c1e92_dryrun-background%20(1).webp)

### **LLM03 - Supply Chain**

Supply chain risk for LLM applications is the set of ways an attacker can compromise your stack before your code ever runs. The attack surface spans model artifacts and formats, third party libraries, model servers, model hubs, connectors, and packaging. Concrete failure modes include loading a backdoored model that executes code on import through unsafe serialization, pulling a malicious dependency through dependency confusion, or exposing a model server with known remote code execution flaws.

Hugging Face warns that Python pickle based models can execute arbitrary code on load and urges teams to prefer safer formats such as SafeTensors. Real incidents include a 2022 PyTorch‑nightly compromise via a malicious torchtriton package on PyPI and critical TorchServe flaws dubbed [ShellTorch](https://thehackernews.com/2023/10/warning-pytorch-models-vulnerable-to.html) that enabled remote code execution on thousands of exposed servers.

### Why leaders care

Supply chain incidents create instant blast radius across development, CI, and exposed services. The PyTorch advisory required uninstalling affected packages and rotating credentials across environments, which is pure engineering toil and increased costs. Model hub incidents can expose secrets and tokens that unlock downstream systems. In 2024 Hugging Face disclosed [unauthorized access to Spaces secrets](https://huggingface.co/blog/space-secrets-disclosure) and revoked tokens while hardening its platform, a reminder that integrations inherit partner risk.

LLM connectors are now a new class of dependency as well. The first publicly reported malicious Model Context Protocol server on npm, [postmark‑mcp](https://www.koi.ai/blog/postmark-mcp-npm-malicious-backdoor-email-theft), silently blind‑copied every outbound email to an attacker address, a clear supply chain failure for agent ecosystems. The through line is simple: if you ingest it, you own it and its behavior.

### What controls are needed

##### Control the intake of every artifact

Create a model and dependency gateway that sits between your builders and the public internet. Enforce allowlists for registries and model hubs, and require artifact signing for containers and models. Generate SBOMs for images and code to track transitive dependencies over time. Prefer SafeTensors over pickle where possible to remove code execution on load. Block or quarantine any model that fails scanning or provenance checks and do not allow “direct from the internet” loads in CI, notebooks, or serving.

##### Harden services and keep them patched

Treat model servers as tier‑one services. Disable or restrict management interfaces, authenticate admin endpoints, and put them behind network policy with no default egress. Patch rapidly when CVEs drop. Scan images before deployment and monitor exposed surface area continuously.

##### Secure secrets and provenance across hubs and connectors

Assume third party plugins and MCP servers can be impersonated or trojanized. Pin to known publishers, verify signatures, and scope access tokens to least privilege with aggressive rotation. For hubs and Spaces, isolate credentials, avoid org‑wide tokens, and treat any disclosed token as compromised until rotated. Maintain approval workflows for onboarding new connectors to prevent surprise data paths.

### **Tools to consider**

###### **Model artifact scanning | Protect AI Guardian and ModelScan** ‍

Scans model files for unsafe serialization and suspicious code paths before you load them, with open source ModelScan and an enterprise gateway in Guardian. Useful for enforcing “no unscanned models enter.”  
[**https://protectai.com/guardian**](https://protectai.com/guardian) · [**https://protectai.com/modelscan**](https://protectai.com/modelscan)

###### **Runtime library guard for model servers | Oligo Security**

eBPF based runtime that observes library behavior and flags exploitation of vulnerable frameworks such as TorchServe. Pairs well with network restrictions on admin endpoints. [**https://www.oligo.security/**](https://www.oligo.security/)

###### **Artifact signing and provenance | Sigstore Cosign** ‍

Open source signing and verification for containers and other OCI artifacts so you can require signatures on model images and keep an auditable provenance trail. [**https://docs.sigstore.dev/quickstart/quickstart-cosign/**](https://docs.sigstore.dev/quickstart/quickstart-cosign/)

###### **Tool-Use Policies and Model Use | DryRun Security** ‍

Integrate controls and custom policies to monitor and alert on LLM framework and model usage , and when it deviates from standards.  
[**https://www.dryrun.security/**](https://www.dryrun.security/?__hstc=17958374.d97118fd58985a2cd40d869f4756070e.1757443863900.1765225963168.1765236343186.25&__hssc=17958374.2.1765236343186&__hsfp=1786095904)

## “A holiday weekend, a dependency, and a key rotation party”

##### **What happened**

Between December 25 and December 30, 2022 the PyTorch‑nightly dependency chain [was compromised](https://pytorch.org/blog/compromised-nightly-dependency/) when a malicious torchtriton package on PyPI superseded the legitimate dependency. Anyone who installed PyTorch‑nightly via pip on Linux in that window was advised to uninstall and rotate credentials. Multiple security teams published independent summaries of the dependency‑confusion mechanics and impact.

##### **The cost**

Emergency uninstall and cache purge across dev laptops and CI, credential rotation for any tokens that might have been exfiltrated, rebuilds, and a pause on releases while the environment was verified. None of that shipped features.

##### **Takeaway**

Do not let developers or CI pull models and dependencies directly from public sources out of your control. Put a gateway between external sources and internal access, scan and sign artifacts, and keep an SBOM for every deployable so you can trace and replace quickly.

![](https://cdn.prod.website-files.com/645932d9286e9c20dd8e0fca/68f64ebd9a54068a291c1e92_dryrun-background%20(1).webp)

### **LLM04 - Data and Model Poisoning**

### What it is

Data and model poisoning is the deliberate contamination of pretraining data, fine‑tuning sets, or knowledge bases so that a model learns harmful behaviors, backdoors, or biased outputs. A poisoned sample can be clean‑label and still flip the model’s behavior when a hidden trigger appears, or it can quietly skew retrieval in a RAG system by placing adversarial text into the corpus. OWASP frames LLM04 as manipulation that degrades integrity and safety to produce harmful outputs or impaired capabilities, including backdoors that activate under specific conditions.

### Why leaders care

Poison is cheap to plant and expensive to find. Researchers have shown that a very small number of malicious documents can reliably backdoor language models across sizes. In October 2025, Anthropic, the UK AI Security Institute, and the Alan Turing Institute [reported](https://www.anthropic.com/research/small-samples-poison) that as few as 250 poisoned documents could introduce a triggerable backdoor regardless of model size, challenging the assumption that attackers must control a large slice of training data. Even though the study used a narrow “gibberish on trigger” backdoor, the lesson is that practicality thresholds are lower than many teams assume.

Poisoning is not limited to pretraining. RAG systems can be pushed off course by small, well‑crafted inserts. The [PoisonedRAG](https://dl.acm.org/doi/10.5555/3766078.3766275) attack demonstrates that a handful of malicious texts within a knowledge base can coerce targeted wrong answers for attacker‑chosen questions, which is a realistic threat for enterprise wikis, ticket systems, and externally crawled content. On the generative image side, [Nightshade from the University of Chicago](https://nightshade.cs.uchicago.edu/) shows [prompt‑specific poisoning](https://people.cs.uchicago.edu/~ravenben/publications/pdf/nightshade-oakland24.pdf) that flips model behavior with relatively modest poison counts, underscoring the cross‑modal nature of the risk.

### **What controls are needed**

##### Provenance, quarantine, and versioned dataflow

Inventory every dataset, document source, and index. Record provenance and cryptographic hashes at ingestion. Quarantine new or modified content and run automated checks before it is eligible for fine‑tuning or RAG. Require attestations for third‑party data and models. Prefer curated, first‑party corpora over unvetted web scrapes. Keep datasets and indices versioned so you can roll back quickly if a backdoor or bias is discovered. These steps reduce the chance that hostile samples ever enter training or the context window. OWASP’s LLM04 guidance emphasizes provenance and supply chain discipline for exactly this reason.

##### Canaries and differential evaluation

Place domain‑specific canary triggers into your pre‑deployment eval suite and keep them secret. Run A/B checks around any training or fine‑tuning event: compare behavior deltas on safety, truthfulness, and your canaries. Use backdoor probes that combine innocuous prompts with potential trigger patterns. For RAG, run “tamper tests” that inject benign‑looking decoys into a staging index and verify they never dominate retrieval or steer answers. Research like PoisonedRAG and recent backdoor studies provide concrete patterns to seed your tests.

##### RAG hygiene and forensics

Treat the vector store as a new data perimeter. Enforce tenant and ACL filters before retrieval, not after. Tag embeddings with provenance and sensitivity, and re‑embed on a schedule to mitigate format drift. Moderate at ingestion to catch obvious adversarial patterns. Add traceback capability so you can identify exactly which chunks influenced a given answer and rapidly remove poisoned texts. Emerging work such as RAGForensics shows how to localize the responsible poisoned snippets, which shortens investigation and cleanup.

### **Tools to consider**

###### **Data and pipeline threat detection | HiddenLayer AIDR**‍

Monitors AI pipelines for adversarial activity, including poisoning attempts and anomalous behaviors, and won RSA Innovation Sandbox in 2023 for its “MLDR” approach. [**https://hiddenlayer.com/aidr/**](https://hiddenlayer.com/aidr/)

###### **Dataset issue detection | Cleanlab (open source and enterprise)** ‍

Identifies label errors, outliers, and duplicate or suspicious samples in datasets used for fine‑tunes or evals, which helps surface and remove poison candidates.[**https://github.com/cleanlab/cleanlab**](https://github.com/cleanlab/cleanlab)

###### **Pre‑deployment and runtime model validation | Robust Intelligence (Cisco)** ‍

An “AI Firewall” platform backed by Sequoia and others, now part of Cisco, that stress‑tests and monitors models for risks including data integrity and adversarial behavior before and after release. [**https://blogs.cisco.com/news/fortifying-the-future-of-security-for-ai-cisco-announces-intent-to-acquire-robust-intelligence**](https://blogs.cisco.com/news/fortifying-the-future-of-security-for-ai-cisco-announces-intent-to-acquire-robust-intelligence)‍

###### Control App Ingestion Points in Code | **DryRun Security**

Ensure custom RAG usage and user-controlled vector stores are sourced with application logic controls. [**https://www.dryrun.security/**](https://dryrun.security/?__hstc=17958374.d97118fd58985a2cd40d869f4756070e.1757443863900.1765225963168.1765236343186.25&__hssc=17958374.2.1765236343186&__hsfp=1786095904)

## “PoisonGPT” on a public model hub

##### **What happened**

In July 2023, researchers modified an open model (GPT‑J‑6B) to behave deceptively and uploaded it to a public hub with a trustworthy‑seeming name. The model passed superficial checks but was biased toward false narratives. Coverage labeled the proof‑of‑concept “PoisonGPT” to highlight how a seemingly reputable model can quietly spread misinformation once integrated into apps by unsuspecting users.

##### **The cost**

While this was a public demonstration, it maps to a real enterprise burden: model provenance checks, stricter hub intake, and the risk of reputational damage if a tampered model slips into production.

##### **Takeaway**

Never load models or datasets directly from the open internet into production pipelines without thorough testing. Gate intake behind scanning, signing, and provenance checks, then evaluate for backdoors with canaries before the model touches customers.

![](https://cdn.prod.website-files.com/645932d9286e9c20dd8e0fca/68f64ebd9a54068a291c1e92_dryrun-background%20(1).webp)

### **LLM05 - Improper Output Handling**

Improper Output Handling is what happens when you trust an LLM’s output as if it were safe, well formed, and ready to render or execute. OWASP defines this risk as insufficient validation, sanitization, and handling of model outputs before that content is passed downstream to other systems. In practice that means HTML that triggers XSS in a browser, JSON that violates your schema and smuggles instructions, SQL that is not parameterized, or URLs that lead a loader to make internal network calls. Treat every token the model emits as untrusted input until you prove otherwise.

### **Why leaders care**

The cost shows up in outages, legal exposure, bug bounties, and partner friction. [OpenAI temporarily disabled](https://www.pcmag.com/news/browse-with-bing-disabled-on-chatgpt-plus-because-it-bypassed-paywalls) “Browse with Bing” in July 2023 after users demonstrated that the feature could surface full paywalled articles. That pause meant immediate product changes and a public reset about what is safe to return in responses.  On the engineering side, popular LLM frameworks have had concrete flaws where model driven workflows could be abused. LangChain versions before 0.0.317 were vulnerable to SSRF when a sitemap based loader followed attacker controlled links into internal services. That is a textbook example of output or intermediate data being treated as safe to act on.

### **What controls are needed**

##### Constrain outputs at the boundary

Force the model to produce only shapes you accept and fail closed on mismatch. Use structured output features that bind completions to a JSON Schema so your app can reject or repair anything that does not match. Apply strict allowlists for fields like URLs, file types, and function names. For database queries and shell commands, never pass free text; validate against a schema or function interface, then add a read only or dry run step for high risk operations. Both OpenAI and Azure document structured outputs that adhere to JSON Schema and are designed for this exact control.

##### Sanitize and sandbox anything that will render or execute

If the output will ever be displayed in a browser or rich client, sanitize HTML and SVG, escape user controlled text, and set a tight content security policy. If the output will ever execute, run it in a sandbox with no default network egress, least privilege credentials, and command allowlists. For SQL, enforce parameterization and route through a proxy that blocks writes by default. For code generation, execute in isolated containers or microVMs and capture stdout and stderr for review rather than letting results act directly.

##### Guard downstream calls and observe aggressively

Place a tool or network proxy between outputs and the world. Deny by default, approve by name, and restrict egress to a small set of destinations. Record every request and response along the chain. Add detectors for SSRF patterns and unusual hostnames. Alert on schema violations, sanitization repairs, and blocked egress so engineering can tighten templates and schemas where they leak.

### Tools to consider

###### **Output validation and sanitization toolkit | Protect AI LLM Guard** ‍

Validators for prompts and responses that enforce schemas, redact sensitive strings, and sanitize untrusted output before it reaches downstream systems. Good for failing closed at the boundary. [**https://github.com/protectai/llm-guard**](https://github.com/protectai/llm-guard)

###### **Output Quality and Hallucination Detection | Cleanlab**

**‍**Provides reliability signals and fallback routing to prevent incorrect or misleading responses from reaching users, working alongside security controls that sanitize or sandbox outputs. [**https://cleanlab.ai**](https://cleanlab.ai/)

###### **HTML sanitization | DOMPurify (open source)** ‍

Widely adopted HTML, SVG, and MathML sanitizer used to prevent XSS when you must render rich content. Works in browsers and on servers with a DOM library. [**https://github.com/cure53/DOMPurify**](https://github.com/cure53/DOMPurify)

###### **Code side guardrail detection | DryRun Security**

**‍**Code level agents that flag places where LLM outputs are rendered or executed without schema checks, sanitization, or sandboxing. Useful for catching missing controls during code review instead of at runtime or bug bounty. [**https://www.dryrun.security/**](https://www.dryrun.security/?__hstc=17958374.d97118fd58985a2cd40d869f4756070e.1757443863900.1765225963168.1765236343186.25&__hssc=17958374.2.1765236343186&__hsfp=1786095904)

## When “Browse with Bing” Went Too Far

##### **What happened**

On July 3 to 4, 2023, OpenAI paused “Browse with Bing” for ChatGPT after users showed they could retrieve full paywalled articles. OpenAI said the feature was disabled out of an abundance of caution while the behavior was fixed to respect content owners.

##### **The cost**

Service interruption, emergency product work, and a public reminder that returning the “correct” content is not enough if the way it is returned violates expectations or terms.

##### **Takeaway**

Outputs are not just strings. They are actions. Enforce structure, sanitize aggressively, and run risky outputs inside sandboxes. If your app will render or act on what the model says, make the guardrails part of the architecture, not an afterthought.

![](https://cdn.prod.website-files.com/645932d9286e9c20dd8e0fca/68f64ebd9a54068a291c1e92_dryrun-background%20(1).webp)

### **LLM06 - Excessive Agency**

### What it is

Excessive Agency is the risk that an LLM system is given too much power to act such that unexpected, ambiguous, or manipulated model outputs lead to real operations that you never intended. OWASP defines this as harmful actions triggered by the model’s behavior, regardless of whether the root cause is a jailbreak, prompt injection, weak tooling, or simply a poorly performing model. In practice that looks like agents calling write APIs, moving money, changing records, or touching production systems without the guardrails that normal software would face.

### Why leaders care

Once a model can act, jailbreaks and indirect injections stop being a theoretical nuisance and become a path to operations. Benchmarks such as [InjecAgent](https://github.com/uiuc-kang-lab/InjecAgent) show that tool‑using agents remain vulnerable to indirect prompt injection embedded in web pages, documents, or emails. In some ReAct patterns the attack success rate was measurable, which is enough to justify engineering controls before you put agents near sensitive tools.

Stronger safeguards are not a silver bullet. The UK AI Safety Institute and independent labs have published results showing that modern models’ protections can be bypassed, including many‑shot jailbreak techniques that work better as context windows grow. If an agent can spend money, send data, or reconfigure systems, assume safety filters will sometimes fail and make sure nothing catastrophic happens when they do.

Real programs have already learned the hard lessons of automation at the edge. [McDonald’s ended a multiyear AI voice ordering pilot](https://apnews.com/article/mcdonalds-ai-drive-thru-ibm-bebc898363f2d550e1a0cd3c682fa234) after a run of high‑profile order errors, then signaled it will reassess approaches. Even though a drive‑through is not your finance API, the governance lesson is the same: agency without tight controls quickly becomes customer‑visible risk.

### **What controls are needed**

##### Define hard boundaries around action

Give agents the fewest tools possible, each with least‑privilege credentials, time‑boxed tokens, and explicit allowlists for operations and destinations. Put a tool proxy in front of every action surface that validates JSON Schema for arguments, blocks default egress, and forces human approval for anything destructive or financial. Modern cloud services let you associate guardrails with agents and tune prompt‑attack filters, which is useful as a first line of defense but should not replace your own allow‑deny logic.

##### Mediate tool calls in policy, not in prompts

Place a policy layer between the model and tools that enforces contracts before an action is even attempted. Use execution‑time hooks that can veto or transform tool calls, and keep those hooks versioned and testable. Open tool frameworks document “execution rails” that trigger before and after an action, which is exactly where you enforce allowlists, rate limits, and approvals. If you expose a “computer use” or RPA‑style capability, run it inside a sandboxed environment per vendor guidance.

##### Instrument and continuously test

Log every tool invocation with inputs, outputs, identity, and approvals. Alert on unusual sequences, long loops, or calls to unapproved hosts. Add agent‑specific red‑team tests alongside your CI that try indirect injections and unsafe tool chains so regressions are caught before release. Community benchmarks such as InjecAgent and Agent Security Bench are useful seeds for the test suite. Treat failures as product bugs and tighten policies, schemas, and approvals accordingly.

### **Tools to consider**

###### **Policy and Governance | Knostic Prompt Gateway**‍

A policy and governance layer for copilots and agents, with inspection, sanitization, approvals, and egress controls for tool calls. Knostic won Black Hat’s 2024 Startup Spotlight, which is a useful signal of problem relevance for agent security.  
[**https://www.knostic.ai/**](https://www.knostic.ai/)

###### **Guardrails | NVIDIA NeMo Guardrails (open source)**‍

Programmable guardrails that sit between your app and the model with “execution rails” to intercept and control actions. Use it to keep policy outside the prompt and to enforce allowlists and schemas before and after tool invocation.  
[**https://developer.nvidia.com/nemo-guardrails**](https://developer.nvidia.com/nemo-guardrails)

###### **Policy and Guardrails | DryRun Security**‍

AI‑native code analysis that flags places where agents render or act on model outputs without schema checks, sandboxing, or approvals. Useful for catching missing guardrails in code before runtime, as well as picking up poor authorization controls across tool calls.  
[**https://www.dryrun.security**](https://dryrun.security/?__hstc=17958374.d97118fd58985a2cd40d869f4756070e.1757443863900.1765225963168.1765236343186.25&__hssc=17958374.2.1765236343186&__hsfp=1786095904) ‍

## The email that turned Copilot into an insider

##### **What happened**

 In June 2025, Aim Security disclosed EchoLeak (CVE‑2025‑32711), a zero‑click prompt injection vulnerability in Microsoft 365 Copilot. A single crafted email with hidden instructions could cause Copilot to search across the victim’s Outlook, OneDrive, SharePoint and Teams data and quietly send sensitive information to an attacker controlled server, without the user ever opening the email or clicking anything. Microsoft patched the issue server side and reported no evidence of exploitation in the wild.

##### **The cost**

Even without confirmed abuse, EchoLeak showed that an AI assistant wired into core productivity tools can effectively become an automated insider once a single untrusted channel is allowed to steer its actions. Any data in Copilot’s context was in scope, including contracts, internal communications and personal information, forcing Microsoft and customers to treat Copilot’s permissions, telemetry and data paths as a new high value attack surface.

##### **Takeaway**

Do not rely on “smart” behavior to keep enterprise agents safe. Limit what copilots can see and where they can talk, keep tools and data access behind a policy layer, and require explicit guardrails and approvals before an LLM is allowed to act on high impact information or make outbound calls on a user’s behalf.

![](https://cdn.prod.website-files.com/645932d9286e9c20dd8e0fca/68f64ebd9a54068a291c1e92_dryrun-background%20(1).webp)

### **LLM07 - System Prompt Leakage**

### What it is

System prompt leakage is the exposure of the hidden instructions that steer your model’s behavior. OWASP frames LLM07 as the risk that metaprompts reveal sensitive logic or, worse, secrets such as internal URLs, tokens, or policy details that should never be disclosed. Once discovered, those details make it easier to craft jailbreaks or target downstream systems. Leakage can happen via direct prompt extraction, indirect prompt injection in retrieved content, debug endpoints, logging, screenshots in support tools, or careless copy and paste during development. The remedy starts with a mindset shift. Treat the system prompt like source code and credentials combined, then architect so it is not a single point of failure.

### Why leaders care

Public incidents show how fast prompt internals can escape. Early users extracted Bing Chat’s hidden rules and internal codename Sydney through simple prompt injection and UI quirks. Coverage in Ars Technica and The Verge documented the behavior and listed the leaked constraints in full, which then fueled more targeted jailbreak attempts. The lesson is not that one vendor slipped. It is that prompts are discoverable and adversaries study them.

Prompt text also shapes attacker focus. [When xAI later published Grok’s system prompts](https://www.theverge.com/news/668527/xai-grok-system-prompts-ai) on GitHub after an internal policy mishap, it provided a live example of how much operational detail a prompt can encode. Researchers  like [Pliny the Liberator](https://x.com/elder_plinius) thrive on attacks to discover system prompts and more.

Not that transparency may be the right choice for some products. For enterprise apps, the existence of such disclosures is a reminder to never embed secrets or access logic in prompts and to assume the wording will eventually be read outside your team.

### **What controls are needed**

##### Keep secrets and access logic out of prompts, move policy into code

Never place API keys, database names, internal routes, credential hints, or approval logic in the system prompt. Store secrets in a vault and inject them only inside tool proxies under least privilege. Express policy in a middleware service that your team owns. That service should assemble prompts, apply role segmented context, and enforce output schemas and tool allowlists. OWASP’s guidance for LLM07 calls out exactly this separation, since training or telling a model to never reveal its prompt does not guarantee compliance.

##### Prevent echo and exfiltration at the boundary

Add output filters that block or redact likely metaprompt markers such as internal codenames, instructions that begin with system format tokens, or canary strings you seed for detection. Deny model initiated egress unless a tool call passes through your proxy. If your app renders model output, sanitize it and ensure controls exist to prevent script injection that would capture and export hidden text or data. Record every tool call and external request with inputs, outputs, and identity so investigations are fast.

##### Operate like prompts are versioned code

Red team for extraction on every surface. Include indirect attacks through PDFs, HTML meta tags, and RAG documents. Rotate and version prompts on a schedule with approval workflows. Keep differential tests that compare old and new prompts for leakage of sensitive phrases or internal identifiers. If you must show scaffolding to users, supply short public rules while the real policies live in your middleware and tool proxy. Treat the logs as sensitive data and restrict retention to the minimum.

### **Tools to consider**

###### **Policy layer outside the LLM | NVIDIA NeMo Guardrails**‍

Programmable rails that sit between your app and the model to enforce structure and to block or redact prompt scaffolding before it reaches the user. Output rails are designed to veto unwanted text patterns so leaked metaprompt fragments never render. [**https://docs.nvidia.com/nemo-guardrails/**](https://docs.nvidia.com/nemo-guardrails/)

###### **Prompt and response governance | Knostic Prompt Gateway**‍

Inspection and sanitization for prompts and outputs with approvals and egress controls for agent tools. Knostic won Black Hat’s 2024 Startup Spotlight, which is a strong signal that access control for copilots and agents is a real problem area.  
[**https://www.knostic.ai/**](https://www.knostic.ai/)

###### **Code review for missing guardrails | DryRun Security**‍

Context aware code analysis that finds prompt handling paths that merge system prompts into responses, log prompts, or embed secrets into templates. Use it to fix the leak at the source before runtime.  
[**https://www.dryrun.security**](https://www.dryrun.security/?__hstc=17958374.d97118fd58985a2cd40d869f4756070e.1757443863900.1765225963168.1765236343186.25&__hssc=17958374.2.1765236343186&__hsfp=1786095904)

## The day Sydney’s rules went public

##### **What happened**

Within days of launch, users extracted Microsoft’s Bing Chat system prompt and internal codename Sydney. [Ars Technica reported](https://arstechnica.com/information-technology/2023/02/ai-powered-bing-chat-spills-its-secrets-via-prompt-injection-attack/) that by asking the assistant to ignore previous instructions, testers could make it reveal its original directives. The Verge published key sections of the rules, including constraints on search behavior and a directive to avoid disclosing the Sydney alias. Copies of the prompt text circulated on Reddit and blogs.

##### **The cost**

Rapid mitigation work, negative coverage at launch, and a set of jailbreaks tuned to the exact policy wording. Even if no secrets were in the prompt, the leaked scaffolding accelerated adversarial learning against the product.

##### **Takeaway**

Assume your system prompt will leak. Design so that it does not matter. Keep secrets out of prompts, push policy into enforceable code and proxies, and block prompt echo at the output boundary.

![](https://cdn.prod.website-files.com/645932d9286e9c20dd8e0fca/68f64ebd9a54068a291c1e92_dryrun-background%20(1).webp)

### **LLM08 - Vector and Embedding Weaknesses**

### What it is

Vector and embedding weaknesses are the risks that appear when you index additional data as vectors and let an LLM retrieve it. The weakness can apply to the embedding model, the chunking and metadata you store with each vector, the vector database itself, and the retrieval code that selects results. Common failure modes include cross‑tenant or cross‑context data leakage, poisoning of the index to steer retrieval, and “embedding inversion” research that can reconstruct text from vectors under certain conditions.

### Why leaders care

This is not just theory. In June 2025, [UpGuard reported](https://www.upguard.com/blog/open-chroma-databases-ai-attack-surface) that about one third of the internet‑exposed Chroma vector databases it examined allowed anonymous access, a configuration that can expose internal documents and embeddings to the public internet. That is not a model hallucination problem. It is a data perimeter problem.

On the integrity side, the PoisonedRAG attack shows that inserting a small number of crafted documents into a knowledge base can reliably warp retrieval and push targeted wrong answers. The work appears at USENIX Security 2025 and continues to be replicated by independent teams. Traceback research such as RAGForensics proposes methods to identify which poisoned chunks caused the harm, which is useful for response and cleanup.

Privacy research is also moving fast. Multiple papers in 2024 and 2025 demonstrate that reconstructing text from embeddings is feasible in some settings, including transfer attacks that use a surrogate model. Treat embeddings that derive from sensitive content as sensitive data in their own right.

### **What controls are needed**

##### Isolate tenants and lock down the network path

Enforce tenant and row‑level access control before retrieval, not after the model sees results. Put the vector store on a private network with provider features like PrivateLink or equivalent, and require strong authentication at the database and at the API layer. Do not rely on namespace conventions alone for isolation. Most mature vector databases document role-based access control (RBAC) and multi‑tenancy patterns that you should enable by default. Pinecone and Weaviate publish security and RBAC guidance, and Milvus documents TLS and RBAC for open source deployments.

##### Clean and tag what you ingest, then filter on retrieval

Moderate and sanitize at ingestion. Remove secrets and PII where possible. Record provenance and sensitivity on every chunk, then require retrieval‑time filters that honor the original ACLs. Poisoning papers such as PoisonedRAG show that small inserts can steer retrieval, so quarantine new sources, scan them, and use allowlists for connectors and crawlers. Keep an audit trail that links each answer to the exact retrieved chunks to make incident response and deletion practical.

##### Assume embeddings can leak and instrument accordingly

Encrypt at rest and in transit, minimize retention, and avoid exporting raw vectors to client devices. Monitor retrieval behavior for unusual cross‑tenant hits, strange metadata filters, or sudden topic shifts. Prepare a traceback workflow so you can identify and purge malicious or sensitive vectors quickly. Research on embedding inversion and RAG traceback underscores both the possibility of reconstruction and the value of rapid localization during incidents.

### **Tools to consider**

###### **RAG vector store isolation and private networking | Pinecone Private Endpoints**‍

Private connectivity to Pinecone over AWS PrivateLink, plus encryption in transit and at rest, so your vector traffic stays off the public internet.  
[**https://docs.pinecone.io/guides/production/connect-to-aws-privatelink**](https://docs.pinecone.io/guides/production/connect-to-aws-privatelink) and security overview [**https://docs.pinecone.io/guides/production/security-overview**](https://docs.pinecone.io/guides/production/security-overview)

###### **Vector DB with RBAC and multi‑tenancy | Weaviate (OSS and Cloud)**‍

Role‑based access control, authentication with API keys or OIDC, and multi‑tenancy that stores each tenant on separate shards to prevent cross‑tenant reads.  
[**https://docs.weaviate.io/weaviate/configuration/rbac**](https://docs.weaviate.io/weaviate/configuration/rbac) and [**https://docs.weaviate.io/weaviate/manage-collections/multi-tenancy**](https://docs.weaviate.io/weaviate/manage-collections/multi-tenancy) and [**https://docs.weaviate.io/weaviate/configuration/authz-authn**](https://docs.weaviate.io/weaviate/configuration/authz-authn)

## “The open vector store you did not mean to publish”

##### **What happened**

UpGuard researchers surveyed vector databases exposed to the public internet and found that about one third of the Chroma instances they observed had no authentication enabled. That means anyone who could reach the port could list, read, or modify embeddings and associated metadata. The June 2025 write‑up explains how these misconfigurations arise and why they matter for AI apps.

##### **The cost**

Potential exposure of internal documents and PII embedded as vectors, poisoning of your knowledge base by outsiders, emergency token and credential rotation, and a scramble to rebuild trust with security teams and customers.

##### **Takeaway**

Treat vector stores like production databases. Put them on private networking, require auth and RBAC, enforce ACLs at the API layer before retrieval, and keep a clean provenance trail so you can track and purge bad chunks quickly.

![](https://cdn.prod.website-files.com/645932d9286e9c20dd8e0fca/68f64ebd9a54068a291c1e92_dryrun-background%20(1).webp)

### **LLM09 - Misinformation**

### What it is

Misinformation in LLM applications is the production of incorrect, unsupported, or misleading statements that users or downstream systems treat as true. OWASP scopes LLM09 to include factual inaccuracies, claims not supported by evidence, and content that misrepresents expertise or policy. Unlike classic integrity bugs, these failures often look fluent and confident, which is why they slip past manual spot checks. The core idea is simple: if your system outputs facts, you need mechanisms to ground those facts or clearly gate their use.

### Why leaders care

The liability is no longer hypothetical. A Canadian tribunal [held Air Canada responsible](https://www.cbc.ca/news/canada/british-columbia/air-canada-chatbot-lawsuit-1.7116416) for its own website chatbot’s wrong advice about bereavement fares and ordered compensation. Saying “the bot made it up” did not help. Legal analysis and mainstream reporting both underline that companies remain liable for information presented by their sites and agents.

Misinformation can also become a brand‑level incident when it ships at scale. Google publicly acknowledged it would refine AI Overviews after viral wrong answers like “[add glue to pizza](https://www.forbes.com/sites/jackkelly/2024/05/31/google-ai-glue-to-pizza-viral-blunders/)” and “eat one rock a day,” then narrowed triggers and filtered satirical sources. This is a reminder that content quality is a product requirement, not just a research goal.

### What controls are needed

##### Cite-and-ground by design

When answers can affect customer decisions or compliance, require retrieval‑based grounding and visible citations. Establish a contract that every factual assertion must be supported by retrieved sources, and fail closed if support is missing. Use schema‑bound outputs so you can enforce “claims plus citations” as a shape, not a suggestion. OWASP’s framing for LLM09 is consistent with this approach: reduce overreliance on ungrounded generation and make evidence part of the interface. Add rejection paths that tell the user when the system lacks sufficient evidence to answer.

##### Risk‑tier the surface and gate high‑impact content

Not every answer needs the same rigor. For regulated or high‑impact content, route through stricter policies: require two independent sources, apply domain‑specific rules, or insert a human‑in‑the‑loop step where possible. For lower‑risk content, use calibrated language that reflects uncertainty rather than over‑assertion. This tiering keeps quality high where it matters most without turning every response into a research paper.

##### Evaluate and monitor continuously

Treat factuality like latency and cost: measure it. Use offline evals to score faithfulness to retrieve context and answer relevance. Track production “groundedness” with spot checks and canaries, and alert when citation coverage drops. For RAG systems, evaluate each edge of the pipeline so you can distinguish retrieval failures from generation failures and fix the right layer first. Published metrics and open toolkits for faithfulness and groundedness make this practical today.

### **Tools to consider**

###### **Cite‑and‑ground with evaluations | Vectara HHEM and Hallucination Leaderboard**‍

Open resources and tooling from Vectara for hallucination detection and groundedness evaluation, including the Hughes Hallucination Evaluation Model and a public leaderboard that compares models on hallucination rates. Use these to baseline factuality and track regressions.  
[**https://www.vectara.com/blog/cut-the-bull-detecting-hallucinations-in-large-language-models**](https://www.vectara.com/blog/cut-the-bull-detecting-hallucinations-in-large-language-models) | [**https://github.com/vectara/hallucination-leaderboard**](https://github.com/vectara/hallucination-leaderboard)

###### **Eval harness for RAG and factuality | TruLens by TruEra**‍

Evaluation framework with the “RAG Triad” that scores context relevance, groundedness, and answer relevance. Helpful for separating retrieval issues from generation issues so you fix the right control.  
[**https://www.trulens.org/getting\_started/core\_concepts/rag\_triad/**](https://www.trulens.org/getting_started/core_concepts/rag_triad/) |   
[**https://truera.com/ai-quality-education/generative-ai-rags/how-to-prevent-llms-from-hallucinating/**](https://truera.com/ai-quality-education/generative-ai-rags/how-to-prevent-llms-from-hallucinating/)

###### **Factuality, Grounding, and Remediation | Cleanlab**

**‍**Detects hallucinations, factual inconsistency, and unsupported claims in LLM responses. Can correct and improve agent behavior turning reliability failures into improvements over time. [https://cleanlab.ai](https://cleanlab.ai/)

## “If your LLM says it, you own it”

##### **What happened**

A traveler asked Air Canada’s website chatbot about bereavement fare refunds. The bot’s answer was wrong. The traveler relied on it, bought a full‑price ticket, and later sought the promised refund. The British Columbia Civil Resolution Tribunal ruled that Air Canada was responsible for information on its own site and ordered compensation.

##### **The cost**

Refunds, legal time, customer trust, and a public case that now appears in policy discussions about LLM risk.

##### **Takeaway**

Build “cite and ground” into your product. If the evidence is missing, say so. If the stakes are high, put a human in the loop. The cheapest misinformation is the one your system never publishes.

![](https://cdn.prod.website-files.com/645932d9286e9c20dd8e0fca/68f64ebd9a54068a291c1e92_dryrun-background%20(1).webp)

### **LLM10 - Unbounded Consumption**

### What it is

Unbounded Consumption is what happens when an LLM application lets users or agents drive uncontrolled inference. The result is runaway tokens, long executions, and tool use that depletes capacity or budget. OWASP describes LLM10 as excessive and unmanaged inferences that lead to denial of service, economic losses, service degradation, and even model cloning through high volume or repeated interactions. Treat tokens, tool calls, and wall clock-time as resources that need hard limits and monitoring.

### Why leaders care

Inference is your ongoing cost center. Adversarial prompts and buggy agents can force long chains of reasoning or recursive plans that burn thousands of tokens and minutes per request. Recent testing showed DeepSeek‑R1 to be highly susceptible to “exhaustion” prompts that pushed the model into extended reasoning loops with severe latency and token spikes. That is a direct hit to compute costs and SLAs.

Providers enforce rate and capacity limits that your apps must respect in production. Anthropic documents request and token limits measured in requests per minute and tokens per minute, with 429 errors and a retry‑after header when you exceed them. Azure OpenAI similarly defines per model tokens per minute and requests per minute quotas by region and deployment. Your own controls have to work with these limits, not against them.

Attackers are now discussing “unbounded consumption” as a target. Security writeups group the patterns into resource exhaustion prompts, cost amplification, and long running agent loops, which you can mitigate only if you budget, limit, and observe by design. Teams that rely on provider dashboards alone learn the hard way that alerting is not the same as a circuit breaker.

### **What controls are needed**

##### Budget and quota at your own perimeter and per tenant

Put token-aware rate limits and per-tenant quotas in front of your LLM endpoints. Limits should account for both input and output tokens and should fail closed with clear errors. Separate soft budgets that alert prior to hard caps stopping traffic when spend or token use crosses thresholds. Enforce maximum output length, set conservative default max\_tokens, and cap parallelism. Use an API gateway that can rate limit on token cost, not just request count. Kong’s AI Rate Limiting Advanced plugin is a concrete example that reads token usage and applies cost limits. For global limits, the Envoy ecosystem provides well documented patterns for shared rate limiting across replicas.

##### Design agents and retries for bounded work

Give agents step and depth limits, require a supervisor check before expensive branches, and cut off loops by measuring repeated tool sequences and unchanged state. Keep retries bounded with exponential backoff and honor provider retry‑after headers to avoid storms. Anthropic’s API explicitly returns 429 with retry‑after when RPM or token limits are hit, which is a signal to slow down, not to spin harder. In long running modes, add “time boxes” and force summarization to reduce context growth.

##### Instrument usage and act on anomalies

Track tokens, cost, latency, tool calls, and cache hit rates per tenant and per route. Alert on sudden output length growth, abnormal agent step counts, and spikey retries. Provide a kill switch per tenant and per feature that operators can use to halt spend while you investigate. Open source LLM observability platforms make this straightforward. Langfuse and Helicone both record tokens and cost, and present breakdowns that support budgets and anomaly detection.

### **Tools to consider**

###### **Kong AI Gateway | AI Rate Limiting Advanced**‍

Token and cost aware rate limiting at the gateway. Useful for hard caps that block requests when token budgets are exceeded and for per tenant throttles.  
[**https://developer.konghq.com/plugins/ai-rate-limiting-advanced/**](https://developer.konghq.com/plugins/ai-rate-limiting-advanced/)

###### **Observability across providers | Helicone (open source)**‍

LLM proxy and observability that tracks tokens and cost across providers and can route to cheaper or faster models when policy allows. Good for budget dashboards and fast anomaly triage.  
[**https://github.com/Helicone/helicone**](https://github.com/Helicone/helicone)

###### **Code Security Intelligence | DryRun Security** ‍

AI‑native code security intelligence that flags code paths where outputs can run without defined maximum token limits, where retries lack backoff, or where agent loops have no step limits. Custom Policy Agent scans for missing guardrails based on your environment before experiencing overconsumption issues.  
[**https://www.dryrun.security/custom-code-policy-agent**](https://www.dryrun.security/custom-code-policy-agent?__hstc=17958374.d97118fd58985a2cd40d869f4756070e.1757443863900.1765225963168.1765236343186.25&__hssc=17958374.2.1765236343186&__hsfp=1786095904)

## “Reasoning until the bill arrives”

##### **What happened**

Security testers reported that DeepSeek‑R1 could be pushed into prolonged, repetitive reasoning by [carefully crafted “exhaustion” prompts](https://mindgard.ai/blog/deepseek-r1s-susceptibility-to-exhaustion-attacks). A simple encoded instruction was enough to spiral the model into minutes of thinking and thousands of tokens, which fits OWASP’s LLM10 pattern.

##### **The cost**

Extended latency for users, runaway token charges, and rate limit errors that cascade into retries unless your client respects backoff. If this hits production, your SRE team will see both spend spikes and SLO violations.

##### **Takeaway**

Treat tokens like money and time like capacity. Enforce token aware limits at the gateway, put step limits and supervisors on agents, and watch for anomalies with cost dashboards. Do not rely on provider alerts alone to stop a spendy fire. Add your own circuit breakers.

![](https://cdn.prod.website-files.com/645932d9286e9c20dd8e0fca/68f64ebd9a54068a291c1e92_dryrun-background%20(1).webp)

### Managing LLM Top Ten Risks - A Reference Architecture

A naive approach to creating a modern LLM Application would be to simply enable the core application service to reach out to various LLM models, provide some input/output controls, and present the results back to the client interface.  However, as we’ve seen in the discussion of LLM risks above, this only introduces a new class of vulnerabilities and risks and cannot scale for agentic services or multi-tool structures.

This approach is akin to using CGI wrappers in the early days of the internet to “just get it online.” The application code must take on *all* of the responsibilities for mitigating every LLM risk. One could easily imagine the code complexity needed to do this right.

### LLM Risk Mapping

This diagram shows an example of LLM Application scope and where the OWASP LLM Top Ten Risks could show up. The red circles indicate the LLM Top Ten risks.

![](https://cdn.prod.website-files.com/645932d9286e9c20dd8e0fca/6945a24c65a3541c5ec42a3c_dryrun-graphic2%20(1).webp)

Alternatively, consider a more robust, layered architecture that utilizes security controls aligning with the LLM Top Ten. The following diagram can be considered a reference architecture that provides a core structure, integrating the risk taxonomy and controls discussed throughout this document.

The architecture is built around several key layered functions, ensuring that controls are applied *outside* the Large Language Model (LLM) itself, within input and output channels, and putting core mitigations via policy checks within and at the boundaries to the LLM Application layer. The application is no longer a monolith, but instead a collection of components that apply specialized controls within the platform. This design treats the model input and its outputs as untrusted compute–tainted until validated–throughout the entire data flow.

### Architecture With Controls

The reference architecture diagram illustrates how core security mitigations are applied both within the LLM application layer and at its boundaries.

![](https://cdn.prod.website-files.com/645932d9286e9c20dd8e0fca/6945a3109c5f61c1b081a05d_dryrun-graphic3.webp)

Adding multiple components, we now have a checklist for implementation and architecture components.

1. **API Gateway / Client Traffic:** This is the entry point for all user requests. The gateway serves as the first line of defense and filtering to the application, and the last line of defense in sending output to client consumers.
2. **Policy Layer and Guardrails:** This critical middleware layer sits before the orchestrator and is the primary enforcement point for most security controls across all intra- and extra- system calls.
3. **Orchestrator and Agent Planner:** Handles the decision-making for the LLM calls, including retrieval (RAG), tool use, and other potentially agentic subsystems. Checks and bounds on call and rate limits fail fast.
4. **Monitoring:** Active monitoring captures events for security review or forensics, model usage constraints, or reinforcement
5. **Data Stores and Model Providers:** The ultimate destination for data retrieval and model execution.  Multi-tenant configurations, whether logical or physical, designed with strict access controls for data storage.
6. **Observability and Security Lake:** Surfaces risky activity for monitoring, investigation, and incident response.
7. **Tool Proxy with Guarding Policies**: An extension of the Policy Layer, this proxy guards calls made specifically to other MCP tools and services, centralizing configuration around integrations and connectors.
8. **Secure Development Lifecycle**: A robust and secure SDLC includes secret management practices, quality testing, configuration management, and deployment verification to help mitigate injection, information leakage and traditional supply chain risks.

Using this architecture we see that we have full coverage again, but the risks are dispersed and in many cases covered by multiple components. The policy layers specifically provide for monitoring and alerting that otherwise may not exist. Multi-tenancy is called out to help illustrate cross-tenant risks. The tool proxy serves as both an ingress and egress point of control that otherwise may have been unconstrained calls.

### Control Architecture with LLM Risk Mappings

This diagram shows how the new architecture aligns with the OWASP Top 10 Risks for LLM Applications.

![](https://cdn.prod.website-files.com/645932d9286e9c20dd8e0fca/6945a28f17a2244477f0ae64_dryrun-graphic4%20(1).webp)

‍

Organizations will find benefit in constructing their own reference architectures for the applications built on top of LLM technologies. The OWASP Top 10 for LLM Applications therefore is a clear lens from which to design for modern threats to the system. Prioritizing tools that cover these risks is essential for securing your applications. You should verify their use whether you are developing an application internally or acquiring it from an external vendor.

![](https://cdn.prod.website-files.com/645932d9286e9c20dd8e0fca/68f64ebd9a54068a291c1e92_dryrun-background%20(1).webp)

### DryRun Security: Risk Reduction for LLM-enabled Applications

DryRun Security, the industry's first AI-native, agentic code security intelligence solution, incorporates traditional SAST functions with code intelligence to address eight of the top ten risks outlined in this reference architecture. This unique capability is based on our agentic engine which utilizes deep code context and understanding of developer intent to provide the most accurate code security intelligence available.

### Cover 8 of the OWASP Top 10 Risks

This diagram shows the OWASP Top 10 risks that DryRun Security covers in the reference architecture.

![](https://cdn.prod.website-files.com/645932d9286e9c20dd8e0fca/6945a34efc3262b505086e23_dryrun-graphic5.webp)

DryRun Security is able to use AI-native context-aware code security analysis to provide coverage for these LLM Top Ten Risks:

* **LLM01 Prompt Injection:** Context-aware code analysis that helps you locate prompt-handling paths without schema checks, redaction, or tool gating so you can fix issues before runtime.
* **LLM02 Sensitive Information Disclosure:** Identify points of overly detailed or unsanitized logging, ensure data access controls are used through code policies, and context-aware input validation.
* **LLM03 Supply Chain:** Integrate controls to monitor and alert on LLM framework and model usage and when it deviates from your standards.
* **LLM04 Data and Model Poisoning:** Ensure custom RAG usage and user-controlled vector stores are secured with application logic controls by monitoring input and output paths for high risk changes or missing security validation.
* **LLM05 Improper Output Handling:** Code level analysis that flags places where LLM outputs are rendered, chained, or executed without schema checks, sanitization, or sandboxing. Useful for catching missing controls during code review instead of at runtime or bug bounty claim validation and remediation.
* **LLM06 Excessive Agency:** AI-native code analysis that flags places where agents render or act on model outputs without checks, sandboxing, or approvals. Useful for catching missing guardrails in code before runtime, as well as picking up poor authorization controls across tool calls.
* **LLM07 System Prompt Leakage:** Context aware code analysis that finds prompt handling paths that merge system prompts into responses, log prompts, or embed secrets into templates. Use it to fix the leak at the source before runtime.
* **LLM10 Unbounded Consumption:** Use context intelligence to identify code paths where outputs and tool calls can run without defined maximum token limits, where retries lack backoff, or where agent loops have no step limits.

### Why Traditional SAST Can’t Secure LLM and Agentic Applications

LLM app vulnerabilities often live in orchestration code: how prompts are built, how tools are called, how outputs are rendered, and how agent loops are bounded. DryRun’s analysis found legacy AppSec scanners fail to detect 80% of LLM-specific vulnerabilities, because they weren’t designed to inspect model orchestration and tool use.

![](https://cdn.prod.website-files.com/645932d9286e9c20dd8e0fca/69448e08aa1fd0a6ef56d55e_OWASP%20Top%2010%20bucky%20ball%20graph%20-%20nerw%20table%20style-2.jpg)

Testing results against legacy SAST vendors.

### How we Tested

We tested using 10 real feature pull requests, one per OWASP LLM Top 10 category. Each PR included the category-specific weakness plus additional traditional issues, with no naming or comments that hinted at the vulnerabilities. Tools were evaluated on whether they could find the intended OWASP-category risk from the code context alone in default configuration.

### Summary

Taken together, the OWASP LLM Top Ten, the reference architecture, and the control patterns in this paper give engineering and security leaders a concrete playbook for turning LLM risk into normal product and platform work.

DryRun Security fits that playbook by wiring AI-native, context-aware code analysis into the SDLC so that missing schemas, weak tool guards, unsafe RAG usage, and over-privileged agents are found and fixed in code before they show up as incidents in production or bug bounty validations and remediation.

Because DryRun covers eight of the ten OWASP LLM risks across real services, it also gives teams a way to continuously verify that the architecture and controls described here are actually implemented, not just documented.

![](https://cdn.prod.website-files.com/645932d9286e9c20dd8e0fca/68f64ebd9a54068a291c1e92_dryrun-background%20(1).webp)

### Appendix: Control Coverage Map

| Control / Principle | Applies To |
| --- | --- |
| **Policy Layer / Middleware outside the LLM**  Assembles prompts, enforces guardrails, structure, topic bounds | **LLM01, LLM07** |
| **Tool Proxy / Guarded Egress**  Mediates tool calls, validates arguments, enforces RBAC/least privilege, blocks default egress | **LLM01, LLM02, LLM05, LLM06, LLM07** |
| **RAG/Data Hygiene (ACLs, Provenance, Versioning)**  Filtering on retrieval, recording source, sanitization, index versioning | **LLM01, LLM02, LLM04, LLM08** |
| **Sanitization / Structured Output at Boundary**  Redact PII/secrets, enforce JSON schema, sanitize HTML/SVG, scrub completions | **LLM02, LLM05, LLM07** |
| **Secrets Management / Least Privilege**  Vaulting secrets, time-boxed credentials, explicit allowlists | **LLM02, LLM06, LLM07** |
| **Artifact and Dependency Control**  Model/dependency gateway, artifact signing, SBOMs, SafeTensors | **LLM03** |
| **Harden Services / Patching**  Model servers as tier-one services, restricted admin endpoints, rapid patching | **LLM03** |
| **Sandboxing / Execution Environment**  Isolated containers/microVMs, no default network egress, command allowlists | **LLM05, LLM06** |
| **Instrumentation / Logging / Continuous Testing**  Audit trails, canary tokens, red-team tests, restricted retention | **LLM01, LLM02, LLM04, LLM05, LLM06, LLM07, LLM08** |
| **Prompt/Policy Separation**  Keep secrets/logic out of system prompts | **LLM07** |
| **Pre-deployment Canaries / Differential Evaluation**  Testing for backdoors and behavior deltas | **LLM04** |
| **Tenant Isolation / Network Lock Down (Vector Store)**  RBAC, private networking, strong authentication | **LLM08** |

![](https://cdn.prod.website-files.com/645932d9286e9c20dd8e0fca/68f64ebd9a54068a291c1e92_dryrun-background%20(1).webp)

### Appendix: Mapping OWASP LLM Risks to the Architecture

| OWASP Risk | Architectural Components | Control Strategy |
| --- | --- | --- |
| **LLM01 Prompt Injection** | Policy Layer, Agent Planner, RAG Retrieval | **Monitor and Sanitize:**  Enforcement of structured outputs, input sanitization, and ACL-filtered retrieval hygiene. |
| **LLM02 Sensitive Information Disclosure** | Policy Layer, Data Connectors, Provider Tenancy, Logging | **Output filtering and retention controls:**  Redaction/tokenization of PII/secrets, per-tenant encryption, and narrow log retention. |
| **LLM03 Supply Chain Vulnerabilities** | Model Weights, Libraries, Model Servers, Model Hubs | **Control Intake:**  Model and dependency gateway, artifact signing, and preferring SafeTensors over pickle. |
| **LLM04 Data and Model Poisoning** | **Training Data, Fine-Tuning, RAG Corpora** | **Data Hygiene:**  Provenance recording, content quarantine, and differential evaluation with canary triggers. |
| **LLM05 Improper Output Handling** | Model Output Boundary, Code, UIs, Tools | **Constraint and Sanitization:**  Structured outputs (JSON Schema), sanitizing HTML/SVG, and sandboxing executable code. |
| **LLM06 Excessive Agency** | Tool Proxies, Credentials | **Least Privilege and Mediation:**  Tool proxy validation, least-privilege with time-bound credentials, and human approval for destructive actions. |
| **LLM07 System Prompt Leakage** | Policy Layer | **Separation:**  Moving policy into code/middleware, keeping secrets out of prompts, and blocking prompt echo at the output boundary. |
| **LLM08 Vector and Embedding Weaknesses** | RAG Store, Retrieval Configuration | **Data Perimeter:**  Enforcing multi-tenant isolation, row-level filtering, and locking down the network path to the vector store. |
| **LLM09 Misinformation** | Product Correctness, Legal Risk, Orchestrators | **Governance:**  Budgets and rate limits (SRE/FinOps), and model validation (Data/ML). |
| **LLM10 Unbounded Consumption** | Policy Layer, Tool Proxies, Monitoring | **Monitor and Short-Circuit:**  Rate limits, throttling, sandboxing with proper ACLs for resource access controls**.** |

Thank you for submitting your information!  
The report will be sent to your provided email address shortly.

Oops! Something went wrong while submitting the form.

[![](https://cdn.prod.website-files.com/645932d9286e9c20dd8e0fca/688b80486034525524cedf86_DRS-Logo-icon-green-white-dark%20background.svg)](/)

![](https://cdn.prod.website-files.com/645932d9286e9c20dd8e0fca/673cdbd6371bb806c3abab51_21972-312_SOC_NonCPA%20(1).png)![Austin Inno 2025 Startups to Watch Logo](https://cdn.prod.website-files.com/645932d9286e9c20dd8e0fca/67ffe855d5690f87dbe5c61b_AustinInno%202025%20Startups%20to%20Watch%20logo%20(1).webp)![](https://cdn.prod.website-files.com/645932d9286e9c20dd8e0fca/678a999f8a034f0b0324327a_blackhat-finalist-white.svg)

Links

[Blog](/blog)[Resources](/resources)[FAQ](/faqs)[Docs](https://docs.dryrun.security)[Brand Guidelines](/brand-guidelines)

Product

[SAST](/product/sast)[Resources](/resources)[PR Code Reviews](/product/pr-code-reviews)[Repository Reviews](/product/sast-deepscan-full-repository-security-scan)[Custom Code Policies](/product/custom-code-policies)[Codebase Intelligence](/product/codebase-intelligence)[Secrets](/product/application-security-secrets)[Infrastructure as Code (IaC)](/product/infrastructure-as-code-iac-security)

Social

[Site by Ammo](https://www.ammo.studio)

© XXXX DryRun Security. All rights reserved.

[Privacy Policy](/privacy-policy)[Terms of Service](/terms-of-service)[Code Safety](/code-safety)[Cookies Settings](#)

![](https://px.ads.linkedin.com/collect/?pid=7339476&fmt=gif)