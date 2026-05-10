> Source: https://huggingface.co/learn/llm-course/chapter12/3b

 
Advanced Understanding of Group Relative Policy Optimization (GRPO) in DeepSeekMath · Hugging Face



[![Hugging Face's logo](/front/assets/huggingface_logo-noborder.svg) Hugging Face](/)

* [Models](/models)
* [Datasets](/datasets)
* [Spaces](/spaces)
* [Buckets new](/storage)
* [Docs](/docs)
* [Enterprise](/enterprise)
* [Pricing](/pricing)
* ---
* [Log In](/login)
* [Sign Up](/join)

      

LLM Course documentation

Advanced Understanding of Group Relative Policy Optimization (GRPO) in DeepSeekMath

# LLM Course

 🏡 View all resourcesAgents CourseAudio CourseCommunity Computer Vision CourseContext CourseDeep RL CourseDiffusion CourseLLM CourseML for 3D CourseML for Games CourseOpen-Source AI CookbookRobotics Coursea smol course

Search documentation

ARBNDEENESFAFRGJHEHIIDITJAKOMYNEPLPTRORURUMTETHTRVIZH-CNZH-TW

 

0. Setup

1. Transformer models

2. Using 🤗 Transformers

3. Fine-tuning a pretrained model

4. Sharing models and tokenizers

5. The 🤗 Datasets library

6. The 🤗 Tokenizers library

7. Classical NLP tasks

8. How to ask for help

9. Building and sharing demos

10. Curate high-quality datasets

11. Fine-tune Large Language Models

12. Build Reasoning Models new

[Introduction](/learn/llm-course/chapter12/1)[Reinforcement Learning on LLMs](/learn/llm-course/chapter12/2)[The Aha Moment in the DeepSeek R1 Paper](/learn/llm-course/chapter12/3)[Advanced Understanding of GRPO in DeepSeekMath](/learn/llm-course/chapter12/3b)[Implementing GRPO in TRL](/learn/llm-course/chapter12/4)[Practical Exercise to Fine-tune a model with GRPO](/learn/llm-course/chapter12/5)[Practical Exercise with Unsloth](/learn/llm-course/chapter12/6)[Coming soon...](/learn/llm-course/chapter12/7)

Course Events

![Hugging Face's logo](/front/assets/huggingface_logo-noborder.svg)

Join the Hugging Face community

and get access to the augmented documentation experience

Collaborate on models, datasets and Spaces

Faster examples with accelerated inference

Switch between documentation themes

[Sign Up](/join)

to get started

Copy page

# Advanced Understanding of Group Relative Policy Optimization (GRPO) in DeepSeekMath

> This section dives into the technical and mathematical details of GRPO. It was authored by [Shirin Yamani](https://huggingface.com/shirinyamani).

Let’s deepen our understanding of GRPO so that we can improve our model’s training process.

GRPO directly evaluates the model-generated responses by comparing them within groups of generation to optimize policy model, instead of training a separate value model (Critic). This approach leads to significant reduction in computational cost!

GRPO can be applied to any verifiable task where the correctness of the response can be determined. For instance, in math reasoning, the correctness of the response can be easily verified by comparing it to the ground truth.

Before diving into the technical details, let’s visualize how GRPO works at a high level:

![deep](https://huggingface.co/reasoning-course/images/resolve/main/grpo/16.png)

Now that we have a visual overview, let’s break down how GRPO works step by step.

## The GRPO Algorithm

The core innovation of GRPO is its approach to evaluating and learning from multiple generated responses simultaneously. Instead of relying on a separate reward model, it compares outputs within the same group to determine which ones should be reinforced.

Let’s walk through each step of the algorithm in detail:

### Step 1: Group Sampling

The first step is to generate multiple possible answers for each question. This creates a diverse set of outputs that can be compared against each other.

For each questionq q q, the model will generate G G G outputs (group size) from the trained policy: {o1,o2,o3,…,oGπθold {o\_1, o\_2, o\_3, \dots, o\_G}\pi\_{\theta\_{\text{old}}} o1​,o2​,o3​,…,oG​πθold​​ },G=8 G=8 G=8 where eachoi o\_i oi​ represents one completion from the model.

#### Example

To make this concrete, let’s look at a simple arithmetic problem:

**Question** q q q :Calculate 2+2×6 \text{Calculate}\space2 + 2 \times 6 Calculate 2+2×6

**Outputs** (G=8) (G = 8) (G=8):{o1:14 (correct),o2:16 (wrong),o3:10 (wrong),…,o8:14 (correct)} \{o\_1:14 \text{ (correct)}, o\_2:16 \text{ (wrong)}, o\_3:10 \text{ (wrong)}, \ldots, o\_8:14 \text{ (correct)}\} {o1​:14 (correct),o2​:16 (wrong),o3​:10 (wrong),…,o8​:14 (correct)}

Notice how some of the generated answers are correct (14) while others are wrong (16 or 10). This diversity is crucial for the next step.

### Step 2: Advantage Calculation

Once we have multiple responses, we need a way to determine which ones are better than others. This is where the advantage calculation comes in.

#### Reward Distribution

First, we assign a reward score to each generated response. In this example, we’ll use a reward model, but as we learnt in the previous section, we can use any reward returning function.

Assign a RM score to each of the generated responses based on the correctnessri r\_i ri​ *(e.g. 1 for correct response, 0 for wrong response)* then for each of theri r\_i ri​ calculate the following Advantage value.

#### Advantage Value Formula

The key insight of GRPO is that we don’t need absolute measures of quality - we can compare outputs within the same group. This is done using standardization:
Ai=ri−mean({r1,r2,…,rG})std({r1,r2,…,rG})A\_i = \frac{r\_i - \text{mean}(\{r\_1, r\_2, \ldots, r\_G\})}{\text{std}(\{r\_1, r\_2, \ldots, r\_G\})}Ai​=std({r1​,r2​,…,rG​})ri​−mean({r1​,r2​,…,rG​})​

#### Example

Continuing with our arithmetic example for the same example above, imagine we have 8 responses, 4 of which is correct and the rest wrong, therefore;

| Metric | Value |
| --- | --- |
| Group Average | mean(ri)=0.5 mean(r\_i) = 0.5 mean(ri​)=0.5 |
| Standard Deviation | std(ri)=0.53 std(r\_i) = 0.53 std(ri​)=0.53 |
| Advantage Value (Correct response) | Ai=1−0.50.53=0.94 A\_i = \frac{1 - 0.5}{0.53}= 0.94 Ai​=0.531−0.5​=0.94 |
| Advantage Value (Wrong response) | Ai=0−0.50.53=−0.94 A\_i = \frac{0 - 0.5}{0.53}= -0.94 Ai​=0.530−0.5​=−0.94 |

#### Interpretation

Now that we have calculated the advantage values, let’s understand what they mean:

This standardization (i.e.Ai A\_i Ai​ weighting) allows the model to assess each response’s relative performance, guiding the optimization process to favorable responses that are better than average (high reward) and discourage those that are worse. For instance ifAi>0 A\_i > 0 Ai​>0, then theoi o\_i oi​ is better response than the average level within its group; and ifAi<0 A\_i < 0 Ai​<0, then theoi o\_i oi​ then the quality of the response is less than the average (i.e. poor quality/performance).

For the example above, ifAi=0.94(correct output) A\_i = 0.94 \text{(correct output)} Ai​=0.94(correct output) then during optimization steps its generation probability will be increased.

With our advantage values calculated, we’re now ready to update the policy.

### Step 3: Policy Update

The final step is to use these advantage values to update our model so that it becomes more likely to generate good responses in the future.

The target function for policy update is:
JGRPO(θ)=[1G∑i=1Gmin⁡(πθ(oi∣q)πθold(oi∣q)Aiclip(πθ(oi∣q)πθold(oi∣q),1−ϵ,1+ϵ)Ai)]−βDKL(πθ∥∥πref)J\_{GRPO}(\theta) = \left[\frac{1}{G} \sum\_{i=1}^{G} \min \left( \frac{\pi\_{\theta}(o\_i|q)}{\pi\_{\theta\_{old}}(o\_i|q)} A\_i \text{clip}\left( \frac{\pi\_{\theta}(o\_i|q)}{\pi\_{\theta\_{old}}(o\_i|q)}, 1 - \epsilon, 1 + \epsilon \right) A\_i \right)\right]- \beta D\_{KL}(\pi\_{\theta} \|\| \pi\_{ref})JGRPO​(θ)=[G1​i=1∑G​min(πθold​​(oi​∣q)πθ​(oi​∣q)​Ai​clip(πθold​​(oi​∣q)πθ​(oi​∣q)​,1−ϵ,1+ϵ)Ai​)]−βDKL​(πθ​∥∥πref​)

This formula might look intimidating at first, but it’s built from several components that each serve an important purpose. Let’s break them down one by one.

## Key Components of the Target Function

The GRPO update function combines several techniques to ensure stable and effective learning. Let’s examine each component:

### 1. Probability Ratio

The probability ratio is defined as:
(πθ(oi∣q)πθold(oi∣q)) \left(\frac{\pi\_{\theta}(o\_i|q)}{\pi\_{\theta\_{old}}(o\_i|q)}\right) (πθold​​(oi​∣q)πθ​(oi​∣q)​)

Intuitively, the formula compares how much the new model’s response probability differs from the old model’s response probability while incorporating a preference for responses that improve the expected outcome.

#### Interpretation

* If ratio>1 \text{ratio} > 1 ratio>1, the new model assigns a higher probability to responseoi o\_i oi​ than the old model.
* If ratio<1 \text{ratio} < 1 ratio<1, the new model assigns a lower probability tooi o\_i oi​

This ratio allows us to control how much the model changes at each step, which leads us to the next component.

### 2. Clip Function

The clipping function is defined as:
clip(πθ(oi∣q)πθold(oi∣q),1−ϵ,1+ϵ) \text{clip}\left( \frac{\pi\_{\theta}(o\_i|q)}{\pi\_{\theta\_{old}}(o\_i|q)}, 1 - \epsilon, 1 + \epsilon\right) clip(πθold​​(oi​∣q)πθ​(oi​∣q)​,1−ϵ,1+ϵ)

Limit the ratio discussed above to be within[1−ϵ,1+ϵ] [1 - \epsilon, 1 + \epsilon] [1−ϵ,1+ϵ] to avoid/control drastic changes or crazy updates and stepping too far off from the old policy. In other words, it limit how much the probability ratio can increase to help maintaining stability by avoiding updates that push the new model too far from the old one.

#### Example (ε = 0.2)

Let’s look at two different scenarios to better understand this clipping function:

* **Case 1**: if the new policy has a probability of 0.9 for a specific response and the old policy has a probabiliy of 0.5, it means this response is getting reinforeced by the new policy to have higher probability, but within a controlled limit which is the clipping to tight up its hands to not get drastic
  -Ratio:πθ(oi∣q)πθold(oi∣q)=0.90.5=1.8→Clip 1.2 \text{Ratio}: \frac{\pi\_{\theta}(o\_i|q)}{\pi\_{\theta\_{old}}(o\_i|q)} = \frac{0.9}{0.5} = 1.8 → \text{Clip}\space1.2 Ratio:πθold​​(oi​∣q)πθ​(oi​∣q)​=0.50.9​=1.8→Clip 1.2 (upper bound limit 1.2)
* **Case 2**: If the new policy is not in favour of a response (lower probability e.g. 0.2), meaning if the response is not beneficial the increase might be incorrect, and the model would be penalized.
  -Ratio:πθ(oi∣q)πθold(oi∣q)=0.20.5=0.4→Clip 0.8 \text{Ratio}: \frac{\pi\_{\theta}(o\_i|q)}{\pi\_{\theta\_{old}}(o\_i|q)} = \frac{0.2}{0.5} = 0.4 →\text{Clip}\space0.8 Ratio:πθold​​(oi​∣q)πθ​(oi​∣q)​=0.50.2​=0.4→Clip 0.8 (lower bound limit 0.8)

#### Interpretation

* The formula encourages the new model to favour responses that the old model underweighted **if they improve the outcome**.
* If the old model already favoured a response with a high probability, the new model can still reinforce it **but only within a controlled limit[1−ϵ,1+ϵ] [1 - \epsilon, 1 + \epsilon] [1−ϵ,1+ϵ],(e.g., ϵ=0.2, so [0.8−1.2]) \text{(e.g., }\epsilon = 0.2, \space \text{so} \space [0.8-1.2]) (e.g., ϵ=0.2, so [0.8−1.2])**.
* If the old model overestimated a response that performs poorly, the new model is **discouraged** from maintaining that high probability.
* Therefore, intuitively, By incorporating the probability ratio, the objective function ensures that updates to the policy are proportional to the advantageAi A\_i Ai​ while being moderated to prevent drastic changes. T

While the clipping function helps prevent drastic changes, we need one more safeguard to ensure our model doesn’t deviate too far from its original behavior.

### 3. KL Divergence

The KL divergence term is:
βDKL(πθ∥∥πref) \beta D\_{KL}(\pi\_{\theta} \|\| \pi\_{ref}) βDKL​(πθ​∥∥πref​)

In the KL divergence term, theπref \pi\_{ref} πref​ is basically the pre-update model’s output, `per_token_logps` andπθ \pi\_{\theta} πθ​ is the new model’s output, `new_per_token_logps`. Theoretically, KL divergence is minimized to prevent the model from deviating too far from its original behavior during optimization. This helps strike a balance between improving performance based on the reward signal and maintaining coherence. In this context, minimizing KL divergence reduces the risk of the model generating nonsensical text or, in the case of mathematical reasoning, producing extremely incorrect answers.

#### Interpretation

* A KL divergence penalty keeps the model’s outputs close to its original distribution, preventing extreme shifts.
* Instead of drifting towards completely irrational outputs, the model would refine its understanding while still allowing some exploration

#### Math Definition

For those interested in the mathematical details, let’s look at the formal definition:

Recall that KL distance is defined as follows:DKL(P∥∥Q)=∑x∈XP(x)log⁡P(x)Q(x)D\_{KL}(P \|\| Q) = \sum\_{x \in X} P(x) \log \frac{P(x)}{Q(x)}DKL​(P∥∥Q)=x∈X∑​P(x)logQ(x)P(x)​
In RLHF, the two distributions of interest are often the distribution of the new model version, P(x), and a distribution of the reference policy, Q(x).

#### The Role of β Parameter

The coefficientβ \beta β controls how strongly we enforce the KL divergence constraint:

* **Higher β (Stronger KL Penalty)**
  + More constraint on policy updates. The model remains close to its reference distribution.
  + Can slow down adaptation: The model may struggle to explore better responses.
* **Lower β (Weaker KL Penalty)**
  + More freedom to update policy: The model can deviate more from the reference.
  + Faster adaptation but risk of instability: The model might learn reward-hacking behaviors.
  + Over-optimization risk: If the reward model is flawed, the policy might generate nonsensical outputs.
* **Original** [DeepSeekMath](https://arxiv.org/abs/2402.03300) paper set thisβ=0.04 \beta= 0.04 β=0.04

Now that we understand the components of GRPO, let’s see how they work together in a complete example.

## Worked Example with GRPO

To solidify our understanding of GRPO, let’s walk through a complete example from start to finish.

### Example Problem

Q: Calculate 2+2×6\text{Q: Calculate}\space2 + 2 \times 6Q: Calculate 2+2×6

### Step 1: Group Sampling

First, we generate multiple responses from our model.

Generate (G=8) (G = 8) (G=8) responses,4 4 4 of which are correct answer (\( 14, \text{reward=} 1 \)) and4 4 4 incorrect(reward= 0) \text{(reward= 0)} (reward= 0), Therefore:
o1:14(correct),o2:10(wrong),o3:16(wrong),...oG:14(correct){o\_1:14(correct), o\_2:10 (wrong), o\_3:16 (wrong), ... o\_G:14(correct)}o1​:14(correct),o2​:10(wrong),o3​:16(wrong),...oG​:14(correct)

### Step 2: Advantage Calculation

Next, we calculate the advantage values to determine which responses are better than average:

| Statistic | Value |
| --- | --- |
| Group Average | mean(ri)=0.5 mean(r\_i) = 0.5 mean(ri​)=0.5 |
| Standard Deviation | std(ri)=0.53 std(r\_i) = 0.53 std(ri​)=0.53 |
| Advantage Value (Correct response) | Ai=1−0.50.53=0.94 A\_i = \frac{1 - 0.5}{0.53}= 0.94 Ai​=0.531−0.5​=0.94 |
| Advantage Value (Wrong response) | Ai=0−0.50.53=−0.94 A\_i = \frac{0 - 0.5}{0.53}= -0.94 Ai​=0.530−0.5​=−0.94 |

### Step 3: Policy Update

Finally, we update our model to reinforce the correct responses:

* Assuming the probability of old policy (\( \pi*{\theta*{old}} \)) for a correct outputo1 o\_1 o1​ is0.5 0.5 0.5 and the new policy increases it to0.7 0.7 0.7 then:Ratio:0.70.5=1.4→after Clip 1.2 (ϵ=0.2)\text{Ratio}: \frac{0.7}{0.5} = 1.4 →\text{after Clip}\space1.2 \space (\epsilon = 0.2)Ratio:0.50.7​=1.4→after Clip 1.2 (ϵ=0.2)
* Then when the target function is re-weighted, the model tends to reinforce the generation of correct output, and theKL Divergence \text{KL Divergence} KL Divergence limits the deviation from the reference policy.

With the theoretical understanding in place, let’s see how GRPO can be implemented in code.

## Implementation Example

Let’s put everything together in a practical example. The following code demonstrates how to implement GRPO in PyTorch.

### 1. Loading the Model and Generating Responses

First, we need to load a model and generate multiple responses for a given question:

Copied

```
import torch
import torch.nn.functional as F
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load the model and tokenizer
model_name = "Qwen/Qwen2-Math-1.5B"
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
model.eval()

# Move model to GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Input prompt
prompt = "Solve y = 2x + 1 for x = 2, y = "  # Correct answer: 5
inputs = tokenizer(prompt, return_tensors="pt", padding=True)
input_ids = inputs["input_ids"].to(device)  # Shape: (1, prompt_len)
attention_mask = inputs["attention_mask"].to(device)

# Step 1: Generate 8 responses (B = 2 groups, G = 4 responses per group)
batch_size, num_generations = 2, 4
outputs = model.generate(
    input_ids=input_ids,  # Shape: (1, prompt_len)
    attention_mask=attention_mask,
    max_new_tokens=1,  # seq_len = 1 (single token per response)
    num_return_sequences=batch_size * num_generations,  # 8 responses total
    do_sample=True,
    top_k=10,
    temperature=0.7,
    pad_token_id=tokenizer.eos_token_id,
    return_dict_in_generate=True,
    output_scores=True,
)
```

this initial Generation (Before Any Steps) will output sth like this:

Copied

```
Output 1: 5.0
Output 2: 6.0
Output 3: 7.0
Output 4: 5.0
Output 5: 10.0
Output 6: 2.0
Output 7: 5.0
Output 8: 5.0
```

### 2. Calculating Rewards

Now, we need to determine which responses are correct and assign rewards accordingly:

With GRPO, with the same sample prompt, we generate multiple completions. So for instance, for our prompts of `"Solve y = 2x + 1 for x = 2, y = "` and `Solve y = 2x + 1 for x = 4, y = "` we have two group of generated outputs for the given prompt one is say

* `[5, 6, 7, 5]` and the other is
* `[10, 2, 9, 9]` while the correct answer is 5 and 9.

Note that in practice these reward scores are achieved by a rule-based reward function that assigns rewards based on the correctness of the response or a more complex neural network-based model that can be trained to assign rewards based on the correctness of the response or a mixed of both. But for sake of simplicity let’s say our reward per response is 1 if the response is correct and 0 if it is wrong, therefore;

Copied

```
reward_1 = [1, 0, 0, 1]
reward_2 = [0, 0, 1, 1]
```

next we get the group\_wise mean and std of the rewards;

Copied

```
# Shape: (B * G,) = (8,) bc we have 2 groups of 4 generations that we flatten
rewards = torch.tensor([1, 0, 0, 1, 0, 0, 1, 1], dtype=torch.float32)
num_generations = 4

# Group rewards: Shape (B, G) = 2, 4)
rewards_grouped = rewards.view(-1, num_generations)

# Mean per group: Shape (B,) = (2,)
mean_grouped_rewards = rewards_grouped.mean(dim=1)

# Std per group: Shape (B,) = (2,)
std_grouped_rewards = rewards_grouped.std(dim=1)

# Broadcast to match rewards and normalize: Shape (B * G,) = (8,)
# why we need to broadcast? because we need to calculate the advantage values for each response within the group
mean_grouped_rewards = mean_grouped_rewards.repeat_interleave(num_generations, dim=0)
std_grouped_rewards = std_grouped_rewards.repeat_interleave(num_generations, dim=0)
```

this will output:

Copied

```
Grouped Rewards: tensor([[1., 0., 0., 1.],
                        [0., 0., 1., 1.]])
Mean per group: tensor([0.5000, 0.5000])
Std per group: tensor([0.5774, 0.5774])
Broadcasted Mean: tensor([0.5000, 0.5000, 0.5000, 0.5000, 0.5000, 0.5000, 0.5000, 0.5000])
Broadcasted Std: tensor([0.5774, 0.5774, 0.5774, 0.5774, 0.5774, 0.5774, 0.5774, 0.5774])
```

Now we can calculate the advantage values for each response:

Copied

```
# Advantages: Shape (B * G,) = (8,)
advantages = (rewards - mean_grouped_rewards) / (std_grouped_rewards + 1e-8)
```

this will output:

Copied

```
Advantages: tensor([ 0.8659, -0.8660, -0.8660,  0.8659, -0.8660, -0.8660,  0.8659,  0.8659])
```

which is coming from the Advantage formula above, so:

Copied

```
For reward_1 = [1, 0, 0, 1]:
1 - 0.5 / 0.5774 ≈ 0.8659
0 - 0.5 / 0.5774 ≈ -0.8660
For reward_2 = [0, 0, 1, 1]: Same pattern.
```

however, the shape here is `(B*G,) = (8,)` but in practice, we need to have the shape of `(B, G) = (2, 4)` to match the logits shape, right? Therefore, we need to unsqueeze the advantages tensor to have the shape of `(B*G, 1) = (8, 1)` to match the logits shape.

Copied

```
# Shape (B * G, 1) = (8, 1) to match the logits shape
advantages = advantages.unsqueeze(1)
```

which will output:

Copied

```
Advantages: tensor([[ 0.8659],
                    [-0.8660],
                    [-0.8660],
                    [ 0.8659],
                    [-0.8660],
                    [-0.8660],
                    [ 0.8659],
                    [ 0.8659]])
```

now we are good, let’s move to the next step of updating the policy model based on the advantage values.

### 3. Updating the Policy

Finally, we use the advantage values to update our model:

Copied

```
# Compute probability ratio between new and old policies
ratio = torch.exp(
    new_per_token_logps - per_token_logps
)  # Shape: (B*G, seq_len) seq_len is the length of the output i.e. the num of generated tokens so here for simplicity let's assume it is 1 # (8, 1)
```

Note that the `per_token_logps` can be achieved by passing the generated outputs to the model and get the logits and then apply the softmax function to get the probabilities `F.softmax(logits, dim=-1)`.

Copied

```
# Clipping Function
eps = self.cliprange  # e.g. 0.2
pg_losses1 = -advantages * ratio  # Shape: (B*G, seq_len)  #(8, 1)
pg_losses2 = -advantages * torch.clamp(
    ratio, 1.0 - eps, 1.0 + eps
)  # Shape: (B*G, seq_len) #(8, 1)
pg_loss_max = torch.max(pg_losses1, pg_losses2)  # Shape: (B*G, seq_len) #(8, 1)


# Now Combine with KL penalty # Shape: (B*G, seq_len) #(8, 1)
per_token_loss = pg_loss_max + self.beta * per_token_kl
```

`per_token_kl` can also be calculated as follows:

Copied

```
# Shape: (B*G, seq_len) #(8, 1)
per_token_kl = F.kl_div(
    F.log_softmax(new_per_token_logps, dim=-1),
    F.softmax(per_token_logps, dim=-1),
    reduction="none",
).sum(dim=-1, keepdim=True)
```

Complete example can be found [here](./basic_example.py). GRPO is also implemented by the excellent TRL team, you can check the implementation [TRL/GRPO\_trainer](https://github.com/huggingface/trl/blob/main/trl/trainer/grpo_trainer.py) for more details.

## Summary and Next Steps

Congratulations! You’ve now learned about Group Relative Policy Optimization (GRPO). To recap what we’ve covered:

1. GRPO compares multiple outputs within a group to determine which ones are better than others, without requiring a separate value model.
2. The advantage calculation standardizes rewards to identify which responses are above or below average.
3. The policy update uses a clipped objective function with a KL divergence penalty to ensure stable learning.

This approach is particularly powerful for mathematical reasoning tasks, where correctness can be objectively verified. The GRPO method allows for more efficient training compared to traditional RLHF approaches that require a separate critic model.

As you continue exploring GRPO, consider experimenting with different group sizes, reward functions, and KL penalty coefficients to see how they affect your model’s performance.

Happy training! 🚀

## References

1. [RLHF Book by Nathan Lambert](https://github.com/natolambert/rlhf-book)
2. [DeepSeek-V3 Technical Report](https://huggingface.co/papers/2412.19437)
3. [DeepSeekMath](https://huggingface.co/papers/2402.03300)

 [Update on GitHub](https://github.com/huggingface/course/blob/main/chapters/en/chapter12/3b.mdx)

[←The Aha Moment in the DeepSeek R1 Paper](/learn/llm-course/chapter12/3) [Implementing GRPO in TRL→](/learn/llm-course/chapter12/4)

[Advanced Understanding of Group Relative Policy Optimization (GRPO) in DeepSeekMath](#advanced-understanding-of-group-relative-policy-optimization-grpo-in-deepseekmath)[The GRPO Algorithm](#the-grpo-algorithm)[Step 1: Group Sampling](#step-1-group-sampling)[Example](#example)[Step 2: Advantage Calculation](#step-2-advantage-calculation)[Reward Distribution](#reward-distribution)[Advantage Value Formula](#advantage-value-formula)[Example](#example)[Interpretation](#interpretation)[Step 3: Policy Update](#step-3-policy-update)[Key Components of the Target Function](#key-components-of-the-target-function)[1. Probability Ratio](#1-probability-ratio)[Interpretation](#interpretation)[2. Clip Function](#2-clip-function)[Example (ε = 0.2)](#example-ε--02)[Interpretation](#interpretation)[3. KL Divergence](#3-kl-divergence)[Interpretation](#interpretation)[Math Definition](#math-definition)[The Role of β Parameter](#the-role-of-β-parameter)[Worked Example with GRPO](#worked-example-with-grpo)[Example Problem](#example-problem)[Step 1: Group Sampling](#step-1-group-sampling)[Step 2: Advantage Calculation](#step-2-advantage-calculation)[Step 3: Policy Update](#step-3-policy-update)[Implementation Example](#implementation-example)[1. Loading the Model and Generating Responses](#1-loading-the-model-and-generating-responses)[2. Calculating Rewards](#2-calculating-rewards)[3. Updating the Policy](#3-updating-the-policy)[Summary and Next Steps](#summary-and-next-steps)[References](#references)