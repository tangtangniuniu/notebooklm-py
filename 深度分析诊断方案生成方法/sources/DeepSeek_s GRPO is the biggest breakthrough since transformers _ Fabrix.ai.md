> Source: https://fabrix.ai/blog/deepseeks-grpo-is-the-biggest-breakthrough-since-transformers/

 

DeepSeek’s GRPO is the biggest breakthrough since transformers | Fabrix.ai



* Scroll to top

[Skip to content](#main)


[![Fabrix.ai](https://fabrix.ai/blog/wp-content/uploads/2025/12/Fx-logo-white.png)

![Fabrix.ai](https://fabrix.ai/blog/wp-content/uploads/2025/12/Fx-logo-white.png)

![Fabrix.ai](https://fabrix.ai/blog/wp-content/uploads/2025/12/Fx-logo-white.png)

![Fabrix.ai](https://fabrix.ai/blog/wp-content/uploads/2025/12/Fx-logo-white.png)

![Fabrix.ai](https://fabrix.ai/blog/wp-content/uploads/2025/12/Fx-logo-white.png)

![Fabrix.ai](https://fabrix.ai/blog/wp-content/uploads/2025/12/Fx-logo-white.png)](https://fabrix.ai/blog/)

* [Visit Website](https://fabrix.ai/)

© 2015-2025, [Fabrix.ai](https://www.fabrix.ai)

All right reserved.

Search for

[Miscellaneous](https://fabrix.ai/blog/category/miscellaneous/)

5 min read

# DeepSeek’s GRPO is the biggest breakthrough since transformers

* ![Shailesh Manjrekar](https://fabrix.ai/blog/wp-content/uploads/2022/06/shailesh_forbes-120x120.jpg)
* Author
  Shailesh Manjrekar
* Published
  March 14, 2025

1. [Home](https://fabrix.ai/blog/)
2. [Miscellaneous](https://fabrix.ai/blog/category/miscellaneous/)
3. DeepSeek’s GRPO is the biggest breakthrough since transformers

GRPO is a new reinforcement learning technique that replaces traditional methods like Proximal Policy Optimization (PPO)

DeepSeek’s Group Relative Policy Optimization (GRPO) represents a paradigm shift in reinforcement learning (RL) for large language models, addressing key limitations of Proximal Policy Optimization (PPO) through innovative simplifications and efficiency gains. Here’s why GRPO stands out:

#### **Core Innovations in GRPO**

**1. Elimination of the Critic Model**  
GRPO removes the need for a separate value function (critic model) required in PPO, reducing memory and computational overhead by ~50%. Instead of training two models (policy + critic), GRPO uses:

* **Group-based reward baselines**: Multiple responses per prompt are generated, with their average reward serving as a dynamic baseline.
* **Monte Carlo estimation**: Advantages are calculated directly from sampled completions, avoiding complex value function training.

**2. Stability Through Relative Ranking**  
GRPO introduces a comparative framework:

* Responses are ranked within groups, emphasizing relative performance over absolute rewards.
* A simplified reward system combining **accuracy** (correct answers) and **format compliance** (structured reasoning traces) reduces reward engineering complexity.

**3. Memory and Cost Efficiency**

|  |  |  |
| --- | --- | --- |
| Feature | PPO (e.g., OpenAI o1) | GRPO (DeepSeek R1) |
| Models Trained | 2 (policy + critic) | 1 (policy only) |
| Training Speed | Slower | 2-3× faster |
| VRAM Requirements | High | Up to 50% lower |
| Scalability | Limited | Large-scale optimized |

Real-world results show GRPO enables training a 1B-parameter reasoning model with just 16GB VRAM, democratizing RL training for smaller organizations.

#### **Technical Advantages Over PPO**

* **Simplified advantage calculation**: Uses mean group rewards instead of value function outputs.
* **Built-in KL divergence control**: Directly penalizes deviations from a reference policy without additional components.
* **Structured reasoning enforcement**: Mandates step-by-step explanations within <reasoning> tags, improving interpretability and self-verification.

#### **Impact on Model Performance** –

DeepSeek-R1, trained with GRPO, demonstrates:

* State-of-the-art mathematical reasoning (DeepSeekMath benchmark)
* Improved factual accuracy through self-verification mechanisms
* 93% cost reduction compared to equivalent PPO-based training

While GRPO builds on PPO’s foundation—retaining clipping and policy constraints—its group-relative approach and critic elimination make RL training more accessible. This breakthrough enables efficient scaling while maintaining stability, positioning GRPO as a transformative advancement in RL for language models.

Tagged with: [DeepSeek](https://fabrix.ai/blog/tag/deepseek/)[FabrixAI](https://fabrix.ai/blog/tag/fabrixai/)

![Shailesh Manjrekar](https://fabrix.ai/blog/wp-content/uploads/2022/06/shailesh_forbes-80x80.jpg)

###### Shailesh Manjrekar

Shailesh Manjrekar, Chief Marketing Officer is responsible for CloudFabrix's AI and SaaS Product thought leadership, Marketing, and Go To Market strategy for Data Observability and AIOps market. Shailesh Manjrekar is a seasoned IT professional who has over two decades of experience in building and managing emerging global businesses. He brings an established background in providing effective product and solutions marketing, product management, and strategic alliances spanning AI and Deep Learning, FinTech, Lifesciences SaaS solutions. Manjrekar is an avid speaker at AI conferences like NVIDIA GTC and Storage Developer Conference and is also a Forbes Technology Council contributor since 2020, an invitation only organization of leading CxO's and Technology Executives.

#### Recent Posts

[![](https://fabrix.ai/blog/wp-content/uploads/2025/03/multi-domain-datasets-blog-bg-1024x576.jpg)

* ![Shailesh Manjrekar](https://fabrix.ai/blog/wp-content/uploads/2022/06/shailesh_forbes-80x80.jpg)
* Posted by
  Shailesh Manjrekar](https://fabrix.ai/blog/fine-tuning-or-retrieval-augmented-generation-when-dealing-with-multi-domain-datasets/)

March 24, 2025

17 min read

#### [Fine Tuning (RAG) or Retrieval Augmented Generation when dealing with multi-domain datasets?](https://fabrix.ai/blog/fine-tuning-or-retrieval-augmented-generation-when-dealing-with-multi-domain-datasets/)

[Read More](https://fabrix.ai/blog/fine-tuning-or-retrieval-augmented-generation-when-dealing-with-multi-domain-datasets/)

[![](https://fabrix.ai/blog/wp-content/uploads/2025/03/2670189_390768-PCDJJK-338-02-1024x683.png)

* ![Shailesh Manjrekar](https://fabrix.ai/blog/wp-content/uploads/2022/06/shailesh_forbes-80x80.jpg)
* Posted by
  Shailesh Manjrekar](https://fabrix.ai/blog/when-to-choose-rag-or-lora-for-training/)

March 14, 2025

8 min read

#### [When to choose RAG or LoRA for training?](https://fabrix.ai/blog/when-to-choose-rag-or-lora-for-training/)

[Read More](https://fabrix.ai/blog/when-to-choose-rag-or-lora-for-training/)

© Copyright 2015-2025, [Fabrix.ai](https://www.fabrix.ai)