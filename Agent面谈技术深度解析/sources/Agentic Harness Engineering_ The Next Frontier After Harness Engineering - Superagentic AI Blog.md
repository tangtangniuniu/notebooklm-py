> Source: https://shashikantjagtap.net/agentic-harness-engineering-the-next-frontier-after-harness-engineering/

Agentic Harness Engineering: The Next Frontier After Harness Engineering – Superagentic AI Blog



[Skip to content](#content)

#### [Introducing SuperOpt: Research on Agentic Environment Optimization for Autonomous AI Agents](https://shashikantjagtap.net/introducing-superopt-research-on-agentic-environment-optimization-for-autonomous-ai-agents/)

[![Superagentic AI Blog](http://shashikantjagtap.net/wp-content/uploads/2025/05/superagenticai-logo.png)](https://shashikantjagtap.net/ "Superagentic AI Blog")

# [Superagentic AI Blog](https://shashikantjagtap.net/)

## Full Stack Agentic AI, Agent Optimization, Agent Engineering and Agent Experience.

* [Home](http://shashikantjagtap.net/)
* [Superagentic AI](https://shashikantjagtap.net/disclaimer/)

Search for:

![](https://shashikantjagtap.net/wp-content/uploads/2026/04/AHE-820x547.png)

# Agentic Harness Engineering: The Next Frontier After Harness Engineering

[April 30, 2026May 1, 2026](https://shashikantjagtap.net/agentic-harness-engineering-the-next-frontier-after-harness-engineering/)  [Shashikant Jagtap](https://shashikantjagtap.net/author/shashikant86/)

Harness Engineering has become AI trend these days and now it reached to the next level. In our earlier post, [Harness Engineering: The Hottest Topic in AI Agent Engineering](https://super-agentic.ai/resources/super-posts/harness-engineering-hottest-topic-ai-agent-engineering), we covered that the model is no longer the whole story. Agent performance is shaped by the system around it: tools, memory, instructions, constraints, execution runtime, evaluation, and feedback loops.

The new paper [Agentic Harness Engineering:Observability-Driven Automatic Evolution of Coding-Agent Harnesses](https://arxiv.org/abs/2604.25850), on April 29 pushes that argument forward. Its central claim is: the bottleneck in self-improving coding-agent harnesses is not only agent capability but also observability. In other words, coding agents cannot reliably improve their own harnesses if the harness is a black box, the action space is unclear, the execution traces are unstructured, and edits are not tied to measurable predictions. Once the system exposes the right surfaces, a separate evolution agent can begin to improve the harness itself. This is the jump from Harness Engineering to Agentic Harness Engineering. Harness Engineering asks how humans design better environments for agents. Agentic Harness Engineering asks how we build environments that agents can inspect, revise, test, and improve over time.

## What The AHE Paper Introduces: Probably GEPA for Coding Agent harness

The paper introduces Agentic Harness Engineering, or AHE, as a closed-loop system for evolving coding-agent harnesses. It holds the base model fixed and lets an evolution loop edit the harness around that model. That distinction matters. AHE is not a new model. It is not just prompt optimization or one-off benchmark  
trick. It sounds like  a framework for modifying the external system that controls how a coding agent sees the repository, calls tools, uses memory, manages risk, and reacts to execution results. The authors frame the hard part as a three-part observability problem:

1. Component observability
2. Experience observability
3. Decision observability

Together, these make harness evolution inspectable enough for another agent to operate on.

## Pillar 1: Component Observability

Most agent harnesses are tangled. The system prompt, tool descriptions, tool implementations, middleware, memory, skills, and sub-agent routing often live as one inseparable blob of code and configuration. That makes automated improvement difficult. If a run fails, the optimizer cannot tell whether the problem came from  
the prompt, a missing tool affordance, an unsafe middleware policy, an unhelpful memory entry, or an execution-time  
guard. AHE addresses this by representing editable harness components as file-level artifacts. The paper’s NexAU substrate  
exposes seven component types:

* System prompt
* Tool description
* Tool implementation
* Middleware
* Skill
* Sub-agent configuration
* Long-term memory

This turns the harness into an explicit action space. An evolution agent can edit a specific component, inspect the  
diff, test the result, and roll it back if needed. This is one of the most important engineering ideas in the paper. Self-improvement does not start with autonomy. It  
starts with decomposition. If the harness cannot be decomposed, the optimizer cannot assign credit.

## Pillar 2: Experience Observability

Coding-agent runs produce enormous traces. A long-horizon coding task may include shell commands, file edits, test failures, environment assumptions, partial fixes, retries, tool errors, and final verification attempts. Raw traces are not enough. They contain signal, but they are too large and too messy for a future optimization step to  
consume directly.

AHE introduces an Agent Debugger role that distills rollout trajectories into a layered evidence corpus. Instead of asking the evolution agent to read millions of raw tokens, the system produces structured reports that support drill-down:

* Task-level outcomes
* Success and failure patterns
* Root-cause analysis
* Benchmark-level summaries
* Evidence linked back to the underlying trajectory

This is the difference between logging and observability. Logging says: here is everything that happened. Observability says: here is the structure that helps another actor understand why it happened. For agent harnesses, this matters because the next improvement may depend on a repeated pattern. Maybe the agent keeps  
destroying a verified state after a success. Maybe it repeatedly guesses dependency setup instead of inspecting the project. Maybe it wastes turns rediscovering the same repository structure. Maybe it misses that a shell command sequence creates cross-step risk. Those are harness problems, but they only become visible when the trajectory is distilled into a form that can be acted on.

## Pillar 3: Decision Observability

The most interesting part of AHE is not only that it edits the harness. It requires edits to make predictions. Each change is paired with a self-declared expectation about what should improve in the next round. Later, the system checks that prediction against task-level outcomes. That turns a harness edit into a falsifiable contract. This is a major step toward making agentic self-improvement more scientific. Without decision observability, an evolution loop can become a pile of trial-and-error patches. With decision observability, every edit has a reason, an expected effect, and a later verification point. For teams building production coding-agent systems, this is the habit worth adopting immediately: do not only record what changed. Record why it changed, what the change predicted, and whether the next run confirmed it.

## The Results: Why This Paper Is Special

The paper reports a 10-iteration AHE campaign on Terminal-Bench 2, starting from a minimal bash-only seed harness called NexAU0. The paper’s component ablation is especially revealing:

* Swapping in AHE’s long-term memory alone improves the seed by +5.6 percentage points
* Swapping in AHE’s tools alone improves the seed by +3.3 percentage points
* Swapping in AHE’s middleware alone improves the seed by +2.2 percentage points
* Swapping in AHE’s system prompt alone regresses by -2.3 percentage points

That last result should be uncomfortable for anyone still treating agent improvement as mostly prompt work. The gain did not live in the prose alone. It lived in the executable and operational structure around the model.

## Transfer Matters More Than The Leaderboard

The paper also reports transfer experiments. The evolved AHE harness was frozen and moved to SWE-bench-verified without re-evolution. It achieved the highest aggregate success rate in the reported comparison while using fewer tokens than the seed. The paper reports 75.6% aggregate success for AHE versus 75.2% for NexAU0, with token usage dropping from 526k to 461k. The cross-model story is also notable. When the AHE harness was evaluated with alternate model families, the paper reports gains ranging from +2.3 to +10.1 percentage points. The largest gains appeared on weaker or less saturated base models. That suggests the evolved harness is not only memorizing a benchmark. It is encoding reusable coordination patterns: how to protect verified state, how to manage shell risk, how to structure tool use, and how to make progress through long-horizon software tasks. This is the real promise of Agentic Harness Engineering. If the harness captures reusable engineering experience, then harness evolution becomes a way to improve many agents, not just one model on one benchmark.

## How This Connects To Meta-Harness

AHE arrives only weeks after the [Meta- Harness paper](https://arxiv.org/abs/2603.28052), which introduced an outer-loop system for optimizing model harness code. Meta-Harness argued that  
harness search needs richer access to prior experience than classic text optimizers provide. Instead of compressing feedback into tiny summaries or scalar scores, Meta Harness gives an agentic proposer filesystem access to prior candidate code, traces, and scores. That idea is directly aligned with what we have been building in the open source [Superagentic MetaHarness library](https://github.com/ SuperagenticAI/metaharness). MetaHarness is a filesystem-first Python library for optimizing executable harnesses around agentic coding systems. It  
treats files like `AGENTS.md`, `GEMINI.md`, bootstrap scripts, validation scripts, test flows, routing logic, and benchmark glue as optimization targets. The current OSS implementation already reflects several principles that AHE now makes even sharper.

### Component observability

Why it matters: the editable harness surface must be explicit and revertible. MetaHarness alignment today: candidate workspaces, diffs, `allowed_write_paths`, instruction files, scripts, and helper code are stored as concrete files. Next opportunity: add a clearer component taxonomy for prompts, tools, middleware, memory, skills, and runtime policies.

### Experience observability

Why it matters: future optimization needs structured evidence, not raw chaos. MetaHarness alignment today: runs store manifests, validation results, evaluation results, diffs, bootstrap snapshots, parent artifacts, ledgers, and compare outputs. Next opportunity: add richer trajectory distillation and root-cause summaries inspired by AHE’s Agent Debugger.

### Decision observability

Why it matters: every edit should declare a prediction and be checked later. MetaHarness alignment today: MetaHarness already records outcomes such as `keep`, `discard`,  
`crash`, `timeout`, `no-change`, and `scope-violation`.

Next opportunity: add per-edit prediction manifests and next-round verification reports.

This makes AHE less like a distant academic result and more like a product roadmap for practical harness optimization. Meta-Harness showed that harness code should be optimized as code. AHE shows that self-optimizing harnesses need observability across components, experience, and decisions.

Superagentic MetaHarness sits naturally between those ideas: a practical OSS workbench where harnesses are stored, mutated, evaluated, compared, and made inspectable.

## Where HALO Fits

[HALO](https://github.com/context-labs/HALO), or Hierarchical Agent Loop Optimization, is highly related to this same movement.

HALO is an RLM-based method for recursively improving agent harnesses from execution traces. Its loop is:

1. Collect traces from an agent harness, using OpenTelemetry-compatible tracing
2. Feed those traces into the HALO-RLM engine
3. Have the RLM decompose the traces and identify common failure modes
4. Feed the findings into a coding agent such as Cursor, Claude Code, or a similar code-editing agent
5. Redeploy the harness, gather more traces, and repeat

The reported AppWorld results are strong: the HALO README reports Sonnet 4.6 moving from 73.7% to 89.5% on dev SGC, and Gemini 3 Flash moving from 36.8% to 52.6%. On the held-out `test_normal` proxy, the README reports +10.7 point gains for both models. Conceptually, HALO is very close to AHE’s experience-observability pillar. Both systems are based on the same core intuition: the most valuable harness improvements often come from analyzing the agent’s own execution traces, finding repeated systemic failures, and converting those failures into harness edits. The difference is mostly where each system places the strongest abstraction.

### HALO

Primary abstraction: RLM over trace data. What it optimizes: harness failures surfaced from OpenTelemetry-style traces. Current shape: trace analysis report, then coding-agent-driven harness updates.

### AHE

Primary abstraction: observable self-evolution loop. What it optimizes: system prompt, tools, middleware, memory, skills, and other harness components. Current shape: component, experience, and decision observability in one closed loop.

### Meta-Harness

Primary abstraction: filesystem-backed harness search. What it optimizes: executable harness code and candidate workspaces. Current shape: agentic proposer reads prior code, traces, scores, and artifacts.

### Superagentic MetaHarness

Primary abstraction: practical OSS outer-loop optimizer. What it optimizes: instruction files, scripts, validation flows, routing logic, and benchmark glue. Current shape: candidate workspaces, diffs, manifests, ledgers, outcomes, and run comparison.

So yes: HALO is part of the same concept family. It is best understood as an operationally useful trace-to-feedback layer for harness optimization. AHE is a broader research framework that also insists on explicit editable components and prediction-linked decisions. Meta-Harness and Superagentic MetaHarness provide the filesystem-backed optimization environment where those ideas can become reusable engineering workflows.

The convergence is the important story. Meta-Harness, AHE, and HALO all point in the same direction: future agent improvement will come from trace-aware, evidence-driven harness evolution, not just bigger models or better one-shot prompts.

## Where RLM Code Fits

[RLM Code](https://github.com/SuperagenticAI/rlm-code) is also relevant to this direction. RLM Code provides an interactive environment for running LLM-powered agents in a REPL loop, benchmarking them,  
comparing results, replaying trajectories, and inspecting observability data. It also includes a coding-agent harness path through `/harness run`, plus a CodeMode strategy with MCP tool discovery, guarded code execution, and side-by-side benchmark telemetry. The upcoming RLM Code release also adds a HALO-style `trace_analysis` environment. It can read OpenTelemetry-shaped JSONL traces, build a sidecar index, query trace summaries, search individual traces, view selected spans, and produce an evidence report without blindly loading huge traces into context. That makes RLM Code a useful lab for the experience-observability side of Agentic Harness Engineering.

In practical terms:

* MetaHarness is the outer-loop optimizer for executable harness artifacts
* RLM Code is a runtime and research environment for agent execution, trajectory capture, replay, comparison, and HALO-  
  style trace diagnosis
* Superagentic MetaHarness can consume the resulting trace report through `--trace-evidence`, copying it  
  into each candidate workspace and embedding it in the proposer prompt
* Together, they point toward an end-to-end workflow: run agents, collect trajectories, distill failures, evolve  
  harness files, verify changes, and keep a durable evidence trail

A typical workflow looks like this:

```
/rlm run "Find systemic harness failures trace=./traces.jsonl" env=trace_analysis steps=6
```

```
uv run metaharness run examples/python_fixture_benchmark \
    --backend codex \
    --hosted \
    --trace-evidence ./trace_evidence.md \
    --budget 1 \
    --run-name trace-grounded-codex
```

That is the shape of serious agent engineering: traces become evidence, evidence becomes candidate changes, candidate changes become evaluated artifacts, and the whole process stays inspectable.

## Bigger Than Coding Benchmarks

The AHE paper focuses on coding agents, and that is the right place to start. Coding agents expose concrete artifacts, deterministic tests, shell traces, repository state, and measurable pass or fail outcomes. But the pattern generalizes. Any production agent harness has components:

* Tools
* Memory
* Retrieval
* Runtime policies
* Permissions
* Handoff rules
* Validation checks
* Retry strategies
* Evaluator feedback
* User-facing state

Any production agent also produces experience:

* Task traces
* Tool errors
* Failed plans
* Unsafe actions
* Repeated corrections
* Unresolved edge cases
* Successful patterns

And any mature team needs decision observability:

* What changed?
* Who or what changed it?
* Why was it changed?
* What was expected to improve?
* Did it actually improve?
* Should we keep, revise, or revert?

This is why Harness Engineering is becoming a core line inside Agent Engineering. Agents are not only prompted but  operated, evaluated, constrained. They are given tools and memory. They are routed through workflows. They need rollback, telemetry, and accountability. AHE gives the field a concrete research vocabulary for that reality.

## The Caution: AHE Is Powerful, But Not Magic

The paper is careful about limitations, and builders should be too. AHE is still a controlled research prototype. It adds engineering and compute overhead because each iteration requires benchmark execution, trajectory analysis, and workspace management. It expands the adaptation surface, which creates more opportunity for benchmark-specific tuning. It includes governance mechanisms such as bounded edits, attribution, and rollback, but it is not a complete guardrail stack. Autonomous harness evolution should not mean “let the agent rewrite everything and hope.” It should mean:

* Bounded editable surfaces
* Explicit component ownership
* Structured trajectory evidence
* Cheap validation before expensive evaluation
* Candidate ledgers
* Rollback paths
* Prediction manifests
* Human-reviewable diffs
* Repeatable benchmark runs

The future is not uncontrolled self-modifying agents. The future is observable, testable, reviewable self-improving harnesses.

## What Builders Should Do Now

If you are building coding agents, this paper suggests a practical checklist.

* Make your harness file-addressable. Prompts, tool definitions, middleware policies, memory seeds, skills, and runtime configs should be inspectable artifacts, not hidden constants.
* Store candidate history. Keep the code, diffs, evaluation scores, validation output, and execution traces for every attempted improvement.
* Add outcome discipline. Classify candidates as kept, discarded, timed out, crashed, unchanged, or out of scope.
* Turn logs into evidence. Raw traces are useful, but future optimization needs summaries that preserve root causes and allow drill-down.
* Require change predictions. Every proposed harness edit should say what it expects to improve. Later runs should check that claim.
* Separate cheap validation from expensive evaluation. Do not spend full benchmark cycles on candidates that fail basic syntax, scope, or safety checks.
* Treat tools, middleware, and memory as first-class optimization targets. The AHE ablation results are awarning: the strongest improvements may not live in the system prompt.

## Why We Are Hosting A Harness Engineering Event

This is exactly why Agent Engineering HQ is hosting [Harness Engineering: State of the Art in Agent Harnesses](https://luma.com/rtd0f6ka) at AWS Builder Loft in San Francisco. The event is focused on the technical reality behind modern coding-agent harnesses: orchestration, memory, tool design, verification, error recovery, execution runtimes, trace analysis, and self-optimizing harnesses. We will be discussing the recent wave of harness research, including Meta-Harness, Natural-Language Agent Harnesses,  
HALO, and now Agentic Harness Engineering. More importantly, we want to bring together the engineers and researchers  
actively building these systems in practice. If you care about reliable coding agents, agent evaluation, memory and harness alignment, self-healing agent systems,  
or production-grade agent infrastructure, this is the room to be in.

**RSVP here:** <https://luma.com/rtd0f6ka>

Space is limited. RSVP early.

## Final Thought

Harness Engineering made the model-plus-harness equation visible. Meta-Harness showed that the harness itself can be optimized as executable code. HALO shows that trace analysis can turn messy agent runs into concrete harness improvement reports. Agentic Harness Engineering now shows what the next phase requires: observability that lets agents improve the harness without collapsing into blind trial and error. The future of agent performance will not come only from larger models. It will come from better harnesses, better evidence, better feedback loops, and better engineering discipline around the systems that let models act. That is the next frontier of Agent Engineering.

## Sources And Further Reading

* [Agentic Harness Engineering paper](https://arxiv.org/abs/2604.25850)
* [AHE code  
  link from the paper](https://github.com/china-qijizhifeng/agentic-harness-engineering)
* [Meta-Harness paper](https://arxiv.org/abs/2603.28052)
* [HALO repository](https://github.com/context-labs/HALO)
* [HALO PyPI package](https://pypi.org/project/halo-engine/)
* [HALO AppWorld dataset](https://huggingface.co/datasets/inference-net/HALO-Gemini-3-Flash-AppWorld)
* [Superagentic MetaHarness](https://github.com/SuperagenticAI/metaharness)
* [MetaHarness docs](https://superagenticai.github.io/metaharness/)
* [RLM Code](https://github.com/SuperagenticAI/rlm-code)
* [Harness Engineering event RSVP](https://luma.com/rtd0f6ka)
* [Previous Superagentic Harness Engineering post](https://super-agentic.ai/resources/super-posts/harness-engineering-hottest-topic-ai-agent-engineering)


 [Agent Engineering](https://shashikantjagtap.net/category/agent-engineering/), [Agent Frameowork](https://shashikantjagtap.net/category/agent-frameowork/), [Agent Memory](https://shashikantjagtap.net/category/agent-memory/), [Agent Optimization](https://shashikantjagtap.net/category/agent-optimization/), [Agentic AI](https://shashikantjagtap.net/category/agentic-ai/), [Agentic DevOps](https://shashikantjagtap.net/category/agentic-devops/), [AI](https://shashikantjagtap.net/category/ai/)



# Post navigation

[← Launching the London Agentic AI Community Website](https://shashikantjagtap.net/launching-the-london-agentic-ai-community-website/)

[Bringing HALO and Agentic Harness Engineering Concepts Into Our Open Harness Stack →](https://shashikantjagtap.net/bringing-halo-and-agentic-harness-engineering-concepts-into-our-open-harness-stack/)

### Super-Agentic AI Blog

Super-Agentic AI Blog is back in action.This blog was previously called XCBlog, all about Apple developer tools. The blog was quiet since July 2019-April 2025 as author (Shashi) was working for   Apple. Now, Shashi is back and started blogging about Agentic and Quantum AI for his company ***[Superagentic AI](https://super-agentic.ai).***

### Superagentic AI

[![Superagentic](https://shashikantjagtap.net/wp-content/uploads/2025/05/superagenticai-logo.png)](https://super-agentic.ai)

### ABOUT ME

[![](https://shashikantjagtap.net/wp-content/uploads/2026/01/400_profile.png)](https://www.linkedin.com/in/shashikantjagtap/)

[![RSS](https://shashikantjagtap.net/wp-content/plugins/ultimate-social-media-icons/images/icons_theme/default/default_rss.png "RSS")](https://shashikantjagtap.net/feed/)

[![Follow by Email](https://shashikantjagtap.net/wp-content/plugins/ultimate-social-media-icons/images/icons_theme/default/default_email.png "Follow by Email")](http://www.specificfeeds.com/widgets/emailSubscribeEncFeed/T1pGZXVOVW9McSs2WUdpU0xvWEJQcFovRnkwY1ZvSytZcXAwbzdEN0QwNVhpcDBIRzc1R0xNdE5qdml0aFpsNktvUHFmOXNMRjdLMHp6S2djcGh2YXNSRkIzeURYMXdtVnVqOEhGMnBYcmpJRE9CYi9zNVMxVWRodlNGaE5ySHJ8RzZCVWdBei9YVUc2WjM0Y0wwRUtFV3FEYytpcExBcXhtY05Xb202ajdZVT0=/OA==/)

[![Facebook](https://shashikantjagtap.net/wp-content/plugins/ultimate-social-media-icons/images/icons_theme/default/default_facebook.png "Facebook")](https://en-gb.facebook.com/shashikantjagtaplondon/)

[![Twitter](https://shashikantjagtap.net/wp-content/plugins/ultimate-social-media-icons/images/icons_theme/default/default_twitter.png "Twitter")](https://twitter.com/Shashikant86)

[![LinkedIn](https://shashikantjagtap.net/wp-content/plugins/ultimate-social-media-icons/images/icons_theme/default/default_linkedin.png "LinkedIn")](https://www.linkedin.com/in/shashikantjagtap)

### Tags

[Accessibility](https://shashikantjagtap.net/tag/accessibility/)
[Agent Bricks](https://shashikantjagtap.net/tag/agent-bricks/)
[Agent Engineering](https://shashikantjagtap.net/tag/agent-engineering/)
[Agent Framework](https://shashikantjagtap.net/tag/agent-framework/)
[Agentic AI](https://shashikantjagtap.net/tag/agentic-ai/)
[AI/ML](https://shashikantjagtap.net/tag/ai-ml/)
[Ansible](https://shashikantjagtap.net/tag/ansible/)
[Appium](https://shashikantjagtap.net/tag/appium/)
[Behat](https://shashikantjagtap.net/tag/behat/)
[Carthage](https://shashikantjagtap.net/tag/carthage/)
[CI-Olympics](https://shashikantjagtap.net/tag/ci-olympics/)
[CI/CD](https://shashikantjagtap.net/tag/ci-cd/)
[CLI](https://shashikantjagtap.net/tag/cli/)
[CocoaPods](https://shashikantjagtap.net/tag/cocoapods/)
[codesigning](https://shashikantjagtap.net/tag/codesigning/)
[CoreML](https://shashikantjagtap.net/tag/coreml/)
[CreateML](https://shashikantjagtap.net/tag/createml/)
[Cucumber](https://shashikantjagtap.net/tag/cucumber/)
[DevTools](https://shashikantjagtap.net/tag/devtools/)
[Docker](https://shashikantjagtap.net/tag/docker/)
[dspy](https://shashikantjagtap.net/tag/dspy/)
[Fastlane](https://shashikantjagtap.net/tag/fastlane/)
[inference](https://shashikantjagtap.net/tag/inference/)
[iOSBDD](https://shashikantjagtap.net/tag/iosbdd/)
[iOSDev](https://shashikantjagtap.net/tag/iosdev/)
[iOSDevOps](https://shashikantjagtap.net/tag/iosdevops/)
[iOSDevUK](https://shashikantjagtap.net/tag/iosdevuk/)
[Jenkins](https://shashikantjagtap.net/tag/jenkins/)
[Machine Learning](https://shashikantjagtap.net/tag/machine-learning/)
[PackageManager](https://shashikantjagtap.net/tag/packagemanager/)
[PHP](https://shashikantjagtap.net/tag/php/)
[Ruby](https://shashikantjagtap.net/tag/ruby/)
[SuperOptiX](https://shashikantjagtap.net/tag/superoptix/)
[Swift](https://shashikantjagtap.net/tag/swift/)
[Testing](https://shashikantjagtap.net/tag/testing/)
[Vagrant](https://shashikantjagtap.net/tag/vagrant/)
[WWDC19](https://shashikantjagtap.net/tag/wwdc19/)
[WWDC2018](https://shashikantjagtap.net/tag/wwdc2018/)
[Xcode](https://shashikantjagtap.net/tag/xcode/)
[Xcode10](https://shashikantjagtap.net/tag/xcode10/)
[Xcode11](https://shashikantjagtap.net/tag/xcode11/)
[XcodeServer](https://shashikantjagtap.net/tag/xcodeserver/)
[XCTEQ](https://shashikantjagtap.net/tag/xcteq/)
[XCTest](https://shashikantjagtap.net/tag/xctest/)
[XCUITest](https://shashikantjagtap.net/tag/xcuitest/)

### Categories

* [Agent Engineering](https://shashikantjagtap.net/category/agent-engineering/) (77)
* [Agent Frameowork](https://shashikantjagtap.net/category/agent-frameowork/) (73)
* [Agent Memory](https://shashikantjagtap.net/category/agent-memory/) (27)
* [Agent Optimization](https://shashikantjagtap.net/category/agent-optimization/) (43)
* [Agentic AI](https://shashikantjagtap.net/category/agentic-ai/) (79)
* [Agentic DevOps](https://shashikantjagtap.net/category/agentic-devops/) (27)
* [AI](https://shashikantjagtap.net/category/ai/) (63)
* [BDD](https://shashikantjagtap.net/category/bdd/ "The post related to Behaviour Driven Development are catogorised into it. It may be regading behat, mink, Cucumber, Selenium. BDD") (52)
* [Build Automation](https://shashikantjagtap.net/category/build-automation/) (67)
* [Conferences](https://shashikantjagtap.net/category/conferences/) (5)
* [Continuous Integration](https://shashikantjagtap.net/category/continuous-integration/) (34)
* [Developer Tools](https://shashikantjagtap.net/category/developer-tools/) (71)
* [DSPy](https://shashikantjagtap.net/category/dspy/) (19)
* [Featured](https://shashikantjagtap.net/category/featured/) (43)
* [GEPA](https://shashikantjagtap.net/category/gepa/) (12)
* [Harness Engineering](https://shashikantjagtap.net/category/harness-engineering/) (1)
* [inference](https://shashikantjagtap.net/category/inference/) (1)
* [iOS DevOps](https://shashikantjagtap.net/category/devops/) (108)
* [LangGraph](https://shashikantjagtap.net/category/langgraph/) (1)
* [Machine Learning](https://shashikantjagtap.net/category/machine-learning/) (5)
* [Multi-Agent](https://shashikantjagtap.net/category/multi-agent/) (7)
* [Personal](https://shashikantjagtap.net/category/personal/) (4)
* [Prompt Optimization](https://shashikantjagtap.net/category/prompt-optimization/) (8)
* [Quantum AI](https://shashikantjagtap.net/category/quantum-ai/) (2)
* [Test Automation](https://shashikantjagtap.net/category/test-automation/ "Mix posts about Test Automation") (130)
* [WWDC19](https://shashikantjagtap.net/category/wwdc19/) (5)

### Privacy & Cookie Policy

Superagentic Blog uses cookies to improve your experience. Find out more about Superagentic Blog Privacy and Cookie Policy [Here](https://shashikantjagtap.net/privacy-policy/)

### Archives

Archives

Select Month
 May 2026  (8)
 April 2026  (10)
 March 2026  (10)
 February 2026  (7)
 January 2026  (3)
 December 2025  (9)
 November 2025  (8)
 October 2025  (6)
 September 2025  (4)
 August 2025  (6)
 July 2025  (8)
 June 2025  (7)
 May 2025  (1)
 July 2019  (1)
 June 2019  (5)
 May 2019  (3)
 April 2019  (4)
 March 2019  (3)
 February 2019  (3)
 December 2018  (4)
 November 2018  (3)
 October 2018  (7)
 September 2018  (5)
 August 2018  (1)
 July 2018  (3)
 June 2018  (5)
 May 2018  (7)
 April 2018  (5)
 March 2018  (5)
 February 2018  (8)
 January 2018  (7)
 December 2017  (7)
 November 2017  (2)
 October 2017  (6)
 September 2017  (9)
 August 2017  (3)
 July 2017  (4)
 June 2017  (10)
 May 2017  (2)
 April 2017  (4)
 March 2017  (3)
 February 2017  (3)
 January 2017  (10)
 October 2016  (2)
 September 2016  (1)
 August 2016  (2)
 July 2016  (1)
 June 2016  (2)
 April 2016  (2)
 March 2016  (1)
 February 2016  (2)
 October 2015  (1)
 August 2015  (1)
 May 2015  (3)
 April 2015  (1)
 March 2015  (1)
 November 2014  (1)
 October 2014  (1)
 July 2014  (2)
 May 2014  (1)
 April 2014  (1)
 March 2014  (3)
 February 2014  (2)
 December 2013  (2)
 September 2013  (1)
 August 2013  (2)
 July 2013  (1)
 May 2013  (1)
 April 2013  (1)
 March 2013  (5)
 February 2013  (1)
 October 2012  (1)
 April 2012  (1)
 January 2012  (1)



[Proudly powered by WordPress](http://wordpress.org/) 
 | 
Theme: [FlyMag](http://themeisle.com/themes/flymag/) by Themeisle.