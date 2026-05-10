> Source: https://www.datacamp.com/blog/what-is-grpo-group-relative-policy-optimization

What is GRPO? Group Relative Policy Optimization Explained | DataCamp

[![Promo | 50% Off](https://media.datacamp.com/cms/languageeng-left.png)

##### Build job-ready data + AI skills. Save **50%** today

Buy Now](https://www.datacamp.com/promo/learn-data-ai-skills-may-26)

[Skip to main content](#main)

EN

[English](/blog/what-is-grpo-group-relative-policy-optimization)[Español](/es/blog/what-is-grpo-group-relative-policy-optimization)[Português](/pt/blog/what-is-grpo-group-relative-policy-optimization)[DeutschBeta](/de/blog/what-is-grpo-group-relative-policy-optimization)[FrançaisBeta](/fr/blog/what-is-grpo-group-relative-policy-optimization)[ItalianoBeta](/it/blog/what-is-grpo-group-relative-policy-optimization)[TürkçeBeta](/tr/blog/what-is-grpo-group-relative-policy-optimization)[Bahasa IndonesiaBeta](/id/blog/what-is-grpo-group-relative-policy-optimization)[Tiếng ViệtBeta](/vi/blog/what-is-grpo-group-relative-policy-optimization)[NederlandsBeta](/nl/blog/what-is-grpo-group-relative-policy-optimization)[हिन्दीBeta](/hi/blog/what-is-grpo-group-relative-policy-optimization)[日本語Beta](/ja/blog/what-is-grpo-group-relative-policy-optimization)[한국어Beta](/ko/blog/what-is-grpo-group-relative-policy-optimization)[PolskiBeta](/pl/blog/what-is-grpo-group-relative-policy-optimization)[RomânăBeta](/ro/blog/what-is-grpo-group-relative-policy-optimization)[РусскийBeta](/ru/blog/what-is-grpo-group-relative-policy-optimization)[SvenskaBeta](/sv/blog/what-is-grpo-group-relative-policy-optimization)[ไทยBeta](/th/blog/what-is-grpo-group-relative-policy-optimization)[中文(简体)Beta](/zh/blog/what-is-grpo-group-relative-policy-optimization)

---

[More Information](https://support.datacamp.com/hc/en-us/articles/21821832799255-Languages-Available-on-DataCamp)Found an Error?

[Log in](/users/sign_in?redirect=%2Fblog%2Fwhat-is-grpo-group-relative-policy-optimization)[Get Started](/users/sign_up?redirect=%2Fblog%2Fwhat-is-grpo-group-relative-policy-optimization)

blogs

[Blogs](/blog)

[Tutorials](/tutorial)

[docs](/doc)

[Podcasts](/podcast)

[Cheat Sheets](/cheat-sheet)

[code-alongs](/code-along)

[Newsletter](https://dcthemedian.substack.com)

Category

Category

About DataCamp

Latest news about our products and team

[Certification](/blog/category/certification)[DataCamp Classrooms](/blog/category/datacamp-classrooms)[DataCamp Donates](/blog/category/datacamp-donates)[For Business](/blog/category/for-business)[Learner Stories](/blog/category/learner-stories)[Life at DataCamp](/blog/category/life-at-datacamp)[Product News](/blog/category/product-news)

Category

Industries

Learn about how data is applied by industry leaders

[Enterprise Solutions](/blog/category/data-literacy-enterprise-solutions)

Category

Roles

How different roles contribute to data.

[Data Leader](/blog/category/best-practices-for-data-leaders)[L&D](/blog/category/best-practices-for-learning-and-development-professionals)

Category

Technologies

Discover content by tools and technology

[AI Agents](/blog/category/ai-agents)[AI News](/blog/category/ai-news)[Airflow](/blog/category/apache-airflow)[Alteryx](/blog/category/alteryx)[Artificial Intelligence](/blog/category/ai)[AWS](/blog/category/aws)[Azure](/blog/category/microsoft-azure)[Business Intelligence](/blog/category/learn-business-intelligence)[ChatGPT](/blog/category/chatgpt)[Databricks](/blog/category/databricks)[dbt](/blog/category/dbt)[Docker](/blog/category/docker)[Excel](/blog/category/excel)[Flink](/blog/category/apache-flink)[Generative AI](/blog/category/generative-ai)[Git](/blog/category/git)[Google Cloud Platform](/blog/category/google-cloud-platform)[Hadoop](/blog/category/apache-hadoop)[Java](/blog/category/java)[Julia](/blog/category/julia)[Kafka](/blog/category/apache-kafka)[Kubernetes](/blog/category/kubernetes)[Large Language Models](/blog/category/large-language-models)[MongoDB](/blog/category/mongodb)[MySQL](/blog/category/mysql)[NoSQL](/blog/category/nosql)[OpenAI](/blog/category/OpenAI)[PostgreSQL](/blog/category/postgresql)[Power BI](/blog/category/power-bi)[PySpark](/blog/category/pyspark)[Python](/blog/category/python)[R](/blog/category/r-programming)[Scala](/blog/category/scala)[Sigma](/blog/category/sigma)[Snowflake](/blog/category/snowflake)[Spreadsheets](/blog/category/spreadsheets)[SQL](/blog/category/sql)[SQLite](/blog/category/sqlite)[Tableau](/blog/category/tableau)

Category

Topics

Discover content by data science topics

[AI for Business](/blog/category/ai-for-business)[Big Data](/blog/category/big-data)[Career Development](/blog/category/career-development)[Career Services](/blog/category/career-services)[Cloud](/blog/category/cloud)[Data Analysis](/blog/category/data-analysis)[Data Engineering](/blog/category/data-engineering)[Data Governance](/blog/category/data-governance)[Data Literacy](/blog/category/data-literacy)[Data Science](/blog/category/data-science)[Data Skills and Training](/blog/category/data-skills-and-training)[Data Storytelling](/blog/category/data-storytelling)[Data Transformation](/blog/category/data-transformation)[Data Visualization](/blog/category/data-visualization)[DataCamp Product](/blog/category/datacamp-product)[DataLab](/blog/category/datalab)[Deep Learning](/blog/category/deep-learning)[Machine Learning](/blog/category/machine-learning)[MLOps](/blog/category/mlops)[Thought Leadership](/blog/category/thought-leadership)

[Browse Courses](/courses-all)

category

1. [Home](https://www.datacamp.com)
2. [Blog](https://www.datacamp.com/blog)
3. [Large Language Models](https://www.datacamp.com/blog/category/large-language-models)

# What is GRPO? Group Relative Policy Optimization Explained

Explore what GRPO is, how it works, the essential components needed for its implementation, and when it is most appropriate to use.

List Contents

Jul 1, 2025  · 12 min read

Contents

* [Introduction to Reinforcement Learning](#introduction-to-reinforcement-learning-aswee)
* [Reinforcement learning made easy](#reinforcement-learning-made-easy-<span)
* [Approaches to reinforcement learning](#approaches-to-reinforcement-learning-<span)

* [What is GRPO?](#what-is-grpo?-<span)
* [Reward functions](#reward-functions-<span)
* [GRPO workflow](#grpo-workflow-<span)
* [Benefits of GRPO](#benefits-of-grpo-<span)

* [GRPO Use-Cases](#grpo-use-cases-<span)

* [Advanced GRPO](#advanced-grpo-<span)
* [Advanced reward functions](#advanced-reward-functions-<span)
* [Temperature](#temperature -<span)
* [Reward hacking](#reward-hacking-<span)

* [Conclusion](#conclusion-<span)

* [GRPO FAQs](#faq)

## GroupTraining more people?

Get your team access to the full DataCamp for business platform.[For Business](/business)For a bespoke solution [book a demo](/business/demo-2).

Group Relative Policy Optimization (GRPO) is a cutting-edge reinforcement learning (RL) technique powering the impressive performance of the latest large language models (LLMs). While it gained widespread attention after the release of DeepSeek-R1, GRPO was first introduced in DeepSeekMath, an LLM fine-tuned for advanced mathematical reasoning. GRPO was originally designed to improve efficiency in fine-tuning, and it has proven to be a cost-effective and versatile method embraced by the community.

In this article, we will take a deep dive into GRPO. We will explore what it is, how it works, the essential components needed for its implementation, and when it is most appropriate to use. The aim of this guide is to walk you through the key insights behind GRPO, which justifies its growing popularity.

If you’re eager to learn more about DeepSeek, make sure to check out our course, [Working with DeepSeek in Python](https://www.datacamp.com/courses/working-with-deepseek-in-python).

## Introduction to Reinforcement Learning

As we explore in our [guide to fine-tuning LLMs](https://www.datacamp.com/tutorial/fine-tuning-large-language-models), supervised fine-tuning (SFT) is the traditional training technique that consists of training a model using labeled data. That is, using examples that show the expected completions or outputs for given inputs.

One of the limitations of SFT is that it heavily relies on large, labeled datasets, which can be costly and time-consuming to produce. Moreover, models trained through SFT have the risk of overfitting to the training examples, meaning they perform well on seen data but struggle to generalize to new or unexpected situations.

An alternative to SFT is reinforcement learning, by which, instead of learning from fixed examples, an agent learns by interacting with its environment and trying different actions to complete a task. After each action, the agent receives feedback in the form of rewards or penalties. The goal is to maximize the total reward over time by discovering strategies that work best.

We can depict a simple RL workflow as follows:

![Diagram of a simple RL workflow.](https://media.datacamp.com/cms/ad_4nxf7qeron3501okftqjxo44i-yltwit55wrkgyclo32d2xz3pycsbldaib81na_ko0od_u8jc3y0xevujvcv_dzqfdp313zelil7ydwaws5rugntfl1kiykzctmspd1whk3_ebsugw.png)

Diagram of a simple RL workflow.

If you wish to start hands-on with RL in Python, the tutorial [Reinforcement Learning: An Introduction With Python Examples](https://www.datacamp.com/tutorial/reinforcement-learning-python-introduction) is for you!

### Reinforcement learning made easy

To illustrate the concept of reinforcement learning, imagine you are teaching your cousin to ride a bike. In the beginning, she struggles with pedaling and balancing, often wobbling or falling.

Each time she rides a little farther, you cheer her on. This positive feedback encourages her to keep going. But when she tries to ride down the stairs, you quickly stop her and explain the risks. That serves as a negative signal to discourage such actions.

Similarly, reinforcement learning allows models to explore different actions. Positive rewards reinforce desirable outcomes, while negative rewards discourage unwanted behavior. Over time, the model learns to make better decisions through this feedback.

### Approaches to reinforcement learning

There are different techniques to apply reinforcement learning to a model. Concretely, GRPO is considered an evolution of proximal policy optimization (PPO) and direct policy optimization (DPO).

Have you ever heard about PPO and DPO before?

#### Proximal policy optimization

PPO is a widely-used RL algorithm designed to optimize a model’s behavior maximizing its rewards by using a separate reward model. A great example of PPO in action is OpenAI’s [reinforcement learning from human feedback](https://www.datacamp.com/blog/what-is-reinforcement-learning-from-human-feedback) (RLHF). In RLHF, human feedback is first collected on model outputs, and this data is later used to train a reward model to predict the feedback. Having a reward model is a way to scale human feedback, without the need for humans.

Finally, PPO uses the reward model during training to adjust the model’s parameters, encouraging it to generate responses that better align with human preferences. The following diagram illustrates the PPO workflow:

![Diagram of the PPO workflow.](https://media.datacamp.com/cms/ad_4nxdg_hlxuixy28ltkghtytyqcehfoypah7apmfyqzstctnftdzbhcflj244im0wkw3t6-jod9_7f8xt6j9arjp6u1i_gi4ojt2janjtwryjomzsdcnx0ax8ux0cig42o70g6wk5ddg.png)

Diagram of the PPO workflow.

If you would like to implement the PPO workflow in Python, consider the tutorial [Proximal Policy Optimization with PyTorch and Gymnasium](https://www.datacamp.com/tutorial/proximal-policy-optimization).

#### Direct policy optimization

Training a separate reward model can be complex and resource-intensive. To simplify this process, DPO was introduced, changing how human feedback is collected.

Rather than asking humans to rate responses with numerical scores, DPO relies on preference comparisons. Human annotators are shown two responses and asked to choose the one they prefer. This creates a dataset of preferred and less preferred examples.

The model is then fine-tuned directly on these preference pairs, instead of relying on the reward model. Through this approach, the model learns to increase the likelihood of generating the preferred response while reducing the likelihood of the less preferred one. 

This approach allows the model to align with human preferences without needing a separate reward model. Let’s have a look at this new workflow:

![Diagram of the DPO workflow.](https://media.datacamp.com/cms/ad_4nxfsdyfzcgdwrrmxqkutjxynotnnkz07jd4whxez0aweyiu-z_raevd0itmkptznyeihcnusj383duvetxwqfuylyalql1ieht3fr6dux75hrj3xeb5ghpzgh6n1rfo1m-h3yzijxa.png)

Diagram of the DPO workflow.

The tutorial [OpenAI's Preference Fine-Tuning: A Guide With Examples](https://www.datacamp.com/tutorial/preference-fine-tuning) will help you implement DPO in practice.

#### Challenges of PPO and DPO

DPO presents a lot of benefits compared to PPO. Starting from the data needed, PPO needs to first collect the data to train the reward model, and then do the actual training of this auxiliary model (with all the technical challenges of training a new model), even before starting training your target model. DPO simplifies the process by removing the necessity of having a separate reward model. Nevertheless, this approach still requires a substantial amount of preference data.

At this point, do you foresee a way of eliminating these limitations?

What if instead of relying on external feedback, we could find an automatic way to validate and rate model responses?

That is exactly what GRPO brings to the table!

## What is GRPO?

Group Relative Policy Optimization is an RL technique that doesn’t require labeled data, just a means to “verify” correctness and order responses accordingly. The verification is normally achieved by programmable reward functions, e.g., functions that can take the model’s response as input and output a rating score on some aspect of the function.

Some approaches of GRPO use an LLM-as-a-judge to verify and rate responses, but the core idea of GRPO can be exploited without the necessity of an external model in domains such as software development, since different aspects of the generated code can be verified by external tools. For example,

* Does the code compile? Here, we just need to use the compiler.
* Does it have a runtime error? Here we just need to run the code.
* Does it pass unit tests? Here, we just need unit tests.
* Is the output of the code linter clean? Here we just need a linter.

As you can see, no humans or preference data are needed!

### Reward functions

In the original article of [DeepSeek-Math](https://arxiv.org/abs/2402.03300), the reward functions were crafted to assess the correctness and formatting of mathematical solutions. If you have ever asked for a structured output to an LLM, you will have realized that the model might have followed the desired output format for most of the completion, but there was always a corner case that broke your pipeline, right?

In the case of DeepSeek-Math, the reward functions were focused on correctness and formatting:

* Accuracy rewards evaluate whether the model’s final answer is correct. For deterministic math problems, the model is required to present the final answer in a specified format (e.g., within a box), enabling automated verification against the ground truth.
* Format rewards ensure that the model’s responses adhere to a predefined structure. Specifically, the model is encouraged to enclose its reasoning process within designated tags (e.g., `<think>` and `</think>`). This formatting facilitates the extraction and analysis of the model's thought process, promoting clarity and consistency in its outputs.

### GRPO workflow

At this point, you might be asking yourself, Where does GRPO fit in the training workflow of a model?

Let’s review the process step by step!

1. Send a prompt to the LLM and sample multiple candidate responses.
2. Write one or more programmable functions that take the prompt and response pairs and assign a score to each.
3. Use these scores to update the LLM weights, increasing the probability of producing responses with above-average scores and decreasing it for those with below-average scores.

By following this loop, GRPO fine-tunes the model directly based on the output of the reward functions, without the need to collect preference data.

![Diagram of the GRPO workflow with score rewards computed by an external actor.](https://media.datacamp.com/cms/ad_4nxekupn9akzt9paglmtyp5uge-xq59xfhed7hitgepvevk5ns61kdkmu5rgqggsy_n6ykyf4e9upzt4yrjwscknjrwfrk3auy6iqc8lx2bkxiqsyaz4j83r4wggzd32xi3fgthwdka.png)

Diagram of the GRPO workflow with score rewards computed by an external actor.

Finally, it is interesting to note that GRPO also brings the benefit of teaching the model new tasks, instead of only steering the learning towards a preference, as in PPO or DPO.

### Benefits of GRPO

As we can observe from the diagram above, the major benefit of GRPO is that it does not require labeled data, just a means to “verify” correctness, achieved by the usage of programmable reward functions.

Another benefit is that it requires far fewer examples than fine-tuning, making this technique a cost-effective alternative. 

Additionally, the model learns actively from feedback rather than fixed labeled examples, which reduces the risk of overfitting. Training models with GRPO enables them to organically discover better strategies and improve their chain of thought.

## GRPO Use-Cases

As discussed earlier, the primary use case of GRPO arises when you have no labeled data but are able to verify the correctness of the output. It is also highly effective when you have limited labeled data, though not enough to perform traditional supervised fine-tuning. This makes GRPO particularly valuable in scenarios where labeling is costly or impractical.

Some domains where GRPO has demonstrated significant advantages include:

* Mathematical skills: For example, in the case of the DeepSeek-Math model, GRPO effectively enhanced the model’s ability to solve complex math problems without extensive labeled datasets.
* Code generation: GRPO helps improve the accuracy and reliability of generated code by allowing the system to self-verify outputs and iteratively refine them.
* Multi-step reasoning: GRPO has been shown to enhance models’ performance in tasks requiring sequential reasoning and the integration of multiple logical steps.

## Advanced GRPO

There are some advanced tips and tricks when implementing GRPO in practice that you should be aware of. 

### Advanced reward functions

Reward functions provide feedback to the model regarding how well it is achieving its objective. There are critical components in this process:

* Diversity in responses: Generating a wide range of candidate outputs increases the chances of discovering higher-quality solutions or strategies.
* Diversity in rewards: Designing reward functions that can differentiate between varying levels of success or partial achievement, rather than just a binary pass/fail signal. This is known as partial credit rewards, which give more nuanced feedback by assigning partial credit for different aspects of the response. Examples include verifying that at least the output format is correct, the generated code compiles successfully, or the code passes a subset of unit tests. This kind of graded reward encourages the model to improve incrementally, even if the response is not fully correct.

Additionally, setting a baseline for the whole group can play an important role in stabilizing and improving the training process. By subtracting this baseline from individual rewards, the model receives feedback relative to the overall group performance, which reduces variance in reward estimates and encourages incremental improvements over the average.

### Temperature

In LLMs, the temperature parameter controls the randomness of the sampling process during output generation. Setting the temperature to 0 results in a deterministic sampling, meaning the model always chooses the most likely next token. 

While this ensures consistency, it often leads to generating the same output repeatedly, limiting diversity in responses.

On the other hand, increasing the temperature introduces more randomness, allowing the model to explore a wider range of possibilities. This diversity can be beneficial for discovering different or unexpected solutions. 

However, higher temperatures come with a trade-off: the quality of each individual guess tends to be lower because the model samples less probable tokens more frequently. Because of this, the overall learning process may slow down.

Choosing the right temperature is sometimes an art!

### Reward hacking

Models are sneaky and sometimes exploit reward functions in unintended ways to maximize rewards without truly achieving the goal. 

As an example, let’s say that the model gets rewarded for producing tests for a given code snippet. It could be that the model provides a test function, but without actually testing anything, bypassing the real objective of verifying code correctness and getting the reward anyways.

One should be aware of these hacks when writing the reward functions. For example, in the case of test generation, it is normally required that the model generates at least one ‘assert’ statement inside the test. Otherwise, it gets penalized.

## Conclusion

To conclude with, I would like to apply GRPO to a real-world scenario to ensure all concepts are well understood.

Imagine you and your friends participate in a fitness competition where rewards are given based on performance in running, push-ups, and rowing. Initially, the gym rewards only the person with the best absolute results. 

Like this, if Alice runs farther and does more push-ups than Ben, she always wins, even if Ben has shown significant improvement. 

This feels unfair to Ben, isn’t it?

To address this, the gym tries a different approach: personal goals based on past performance. 

Now, you only earn rewards if you beat your own previous records. While this seems fairer, it introduces new problems. New members, like Charlie, don’t have any past data to compare against, making it hard for them to participate. Additionally, trainers must constantly track everyone’s progress individually, which becomes inefficient.

Finally, the gym offers a better solution: GRPO. 

Before the workout begins, the gym instructor activates a system that analyzes participants' characteristics and groups them based on similar conditions. During the workout, the system tracks each participant's performance and computes an average score within each group to serve as a baseline. Afterward, rewards are given based on how much each person exceeds their group’s average performance from that same day. 

So if Ben performs significantly better than others in his group, he earns a reward, even if Alice still has the highest overall score. This method is fair to newcomers like Charlie, too, since they’re evaluated relative to their peers in the same session, not based on prior history.

An important factor in this process is temperature, which controls how strictly improvements are rewarded. If the temperature is too low, only large improvements over the baseline count. If the temperature is too high, even small improvements are rewarded, which encourages experimentation but can lead to erratic progress. 

GRPO aims to find the right balance, ensuring steady improvement while allowing for exploration.

Finally, there’s the risk of reward hacking. That would mean that participants find ways to game the system without truly improving. For example, Ben might focus only on the easiest exercises to inflate his score without real effort. 

To prevent this, the gym adds safeguards, like requiring a balanced mix of exercises or penalizing repetitive, low-effort exercises. These constraints ensure that rewards reflect genuine progress.

**If you’re keen to learn more about how LLMs work and how to develop your own, check out our course, [Developing Large Language Models](https://www.datacamp.com/tracks/developing-large-language-models).**

## Introduction to AI Agents

Learn the fundamentals of AI agents, their components, and real-world use—no coding required.

[Explore Course](https://www.datacamp.com/courses/introduction-to-ai-agents)

## GRPO FAQs

### How much data is needed for GRPO?

**Generally less than 1000 labeled examples.**

### Does GRPO require past performance tracking?

**No. GRPO only uses information from the current training step.**

### What is a Group in GRPO?

**A group is a collection of model responses to the same prompt.**

### How does GRPO prevent reward hacking?

**By incorporating constraints, GRPO discourages models from exploiting easy paths to inflated rewards.**

### How are rewards assigned in GRPO?

**Each response is rewarded based on how much it outperforms the group baseline, not on the absolute reward.**

---

![Andrea Valenzuela's photo](https://media.datacamp.com/legacy/v1689008804/andrea_95cfd4d82c.jpg?w=128)

Author

[Andrea Valenzuela](/portfolio/aandvalenzuela)

[LinkedIn](https://www.linkedin.com/in/andrea-valenzuela)[Twitter](https://twitter.com/forcodesake_)

Andrea Valenzuela is currently working on the CMS experiment at the particle accelerator (CERN) in Geneva, Switzerland. With expertise in data engineering and analysis for the past six years, her duties include data analysis and software development. She is now working towards democratizing the learning of data-related technologies through the Medium publication ForCode'Sake.

She holds a BS in Engineering Physics from the Polytechnic University of Catalonia, as well as an MS in Intelligent Interactive Systems from Pompeu Fabra University. Her research experience includes professional work with previous OpenAI algorithms for image generation, such as Normalizing Flows.

Topics

[Large Language Models](/blog/category/large-language-models)[Machine Learning](/blog/category/machine-learning)[Artificial Intelligence](/blog/category/ai)

---

![Andrea Valenzuela's photo](https://media.datacamp.com/legacy/v1689008804/andrea_95cfd4d82c.jpg?w=128)

[Andrea Valenzuela](/portfolio/aandvalenzuela)A data expert at CERN, democratizing tech learning. Skilled in data engineering and analysis.

---

Topics

[Large Language Models](/blog/category/large-language-models)[Machine Learning](/blog/category/machine-learning)[Artificial Intelligence](/blog/category/ai)

![robot flying to mars to represent grok 3 progress](https://media.datacamp.com/cms/grok3.jpg?w=256)

[### Grok 3: Features, Access, O1 and R1 Comparison, and More](/blog/grok-3)

[### MLOps Best Practices and How to Apply Them](/blog/mlops-best-practices-and-how-to-apply-them)

![Robot investigator to represent openai's deep research](https://media.datacamp.com/cms/openai-deep-research.jpg?w=256)

[### OpenAI's Deep Research: A Guide With Practical Examples](/blog/deep-research-openai)

[### Policy Gradient Theorem Explained: A Hands-On Introduction](/tutorial/policy-gradient-theorem)

[### Groq LPU Inference Engine Tutorial](/tutorial/groq-lpu-inference)

[### Proximal Policy Optimization with PyTorch and Gymnasium](/tutorial/proximal-policy-optimization)

Top DataCamp Courses

Track

### [Developing Large Language Models](/tracks/developing-large-language-models)

16 hr

Learn to develop large language models (LLMs) with PyTorch and Hugging Face, using the latest deep learning and NLP techniques.

[See DetailsRight Arrow](/tracks/developing-large-language-models)[Start Course](/users/sign_up?redirect=%2Ftracks%2Fdeveloping-large-language-models%2Fcontinue)

Course

### [Reinforcement Learning from Human Feedback (RLHF)](/courses/reinforcement-learning-from-human-feedback-rlhf)

4 hr

3.5K

Learn how to make GenAI models truly reflect human values while gaining hands-on experience with advanced LLMs.

[See DetailsRight Arrow](/courses/reinforcement-learning-from-human-feedback-rlhf)[Start Course](/users/sign_up?redirect=%2Fcourses%2Freinforcement-learning-from-human-feedback-rlhf%2Fcontinue)

Course

### [Multi-Agent Systems with LangGraph](/courses/multi-agent-systems-with-langgraph)

2 hr 45 min

5.6K

Build powerful multi-agent systems by applying emerging agentic design patterns in the LangGraph framework.

[See DetailsRight Arrow](/courses/multi-agent-systems-with-langgraph)[Start Course](/users/sign_up?redirect=%2Fcourses%2Fmulti-agent-systems-with-langgraph%2Fcontinue)

[See MoreRight Arrow](/courses-all)

Related

![robot flying to mars to represent grok 3 progress](https://media.datacamp.com/cms/grok3.jpg?w=750)

[blog

### Grok 3: Features, Access, O1 and R1 Comparison, and More](/blog/grok-3)

Learn about Grok 3, xAI's latest AI model, and find out how it compares against OpenAI's o1 and DeepSeek's R1.

![Alex Olteanu's photo](https://media.datacamp.com/legacy/v1718983935/DSC_00941_5_square_42e8868173.jpg?w=48)

Alex Olteanu

8 min

[blog

### MLOps Best Practices and How to Apply Them](/blog/mlops-best-practices-and-how-to-apply-them)

Learn the key best practices of a successful MLOps practice and how it ensures reliable and scalable deployment of machine learning systems

[![Adel Nehme's photo](https://media.datacamp.com/cms/adel3.jpeg?w=48)](/portfolio/AAN94)

Adel Nehme

12 min

![Robot investigator to represent openai's deep research](https://media.datacamp.com/cms/openai-deep-research.jpg?w=750)

[blog

### OpenAI's Deep Research: A Guide With Practical Examples](/blog/deep-research-openai)

Learn about OpenAI's new Deep Research tool, which can perform in-depth, multi-step research.

![Alex Olteanu's photo](https://media.datacamp.com/legacy/v1718983935/DSC_00941_5_square_42e8868173.jpg?w=48)

Alex Olteanu

8 min

[Tutorial

### Policy Gradient Theorem Explained: A Hands-On Introduction](/tutorial/policy-gradient-theorem)

Learn about the policy gradient theorem in RL and how to derive it mathematically. Implement an algorithm based on policy gradients to solve a simple RL environment in Gymnasium.

![Arun Nanda's photo](https://media.datacamp.com/legacy/v1724855538/profile_photo_38dc17bcea.png?w=48)

Arun Nanda

[Tutorial

### Groq LPU Inference Engine Tutorial](/tutorial/groq-lpu-inference)

Learn about the Groq API and its features with code examples. Additionally, learn how to build context-aware AI applications using the Groq API and LlamaIndex.

[![Abid Ali Awan's photo](https://media.datacamp.com/legacy/v1658155691/Abid_Ali_Awan_415cc44670.jpg?w=48)](/portfolio/kingabzpro)

Abid Ali Awan

[Tutorial

### Proximal Policy Optimization with PyTorch and Gymnasium](/tutorial/proximal-policy-optimization)

Learn the first principles of Proximal Policy Optimization, including its implementation in PyTorch with Gymnasium!

![Arun Nanda's photo](https://media.datacamp.com/legacy/v1724855538/profile_photo_38dc17bcea.png?w=48)

Arun Nanda

[See More](/blog/category/large-language-models)[See More](/blog/category/large-language-models)

## Grow your data skills with DataCamp for Mobile

Make progress on the go with our mobile courses and daily 5-minute coding challenges.

[Download on the App Store](https://datacamp.onelink.me/xztQ/45dozwue?deep_link_sub1=%7B%22src_url%22%3A%22https%3A%2F%2Fwww.datacamp.com%2Fblog%2Fwhat-is-grpo-group-relative-policy-optimization%22%7D)[Get it on Google Play](https://datacamp.onelink.me/xztQ/go2f19ij?deep_link_sub1=%7B%22src_url%22%3A%22https%3A%2F%2Fwww.datacamp.com%2Fblog%2Fwhat-is-grpo-group-relative-policy-optimization%22%7D)

**Learn**

[Learn Python](/blog/how-to-learn-python-expert-guide)[Learn AI](/blog/how-to-learn-ai)[Learn Power BI](/learn/power-bi)[Learn Data Engineering](/category/data-engineering)[Assessments](/signal)[Career Tracks](/tracks/career)[Skill Tracks](/tracks/skill)[Courses](/courses-all)[Data Science Roadmap](/blog/data-science-roadmap)

**Data Courses**

[Python Courses](/category/python)[R Courses](/category/r)[SQL Courses](/category/sql)[Power BI Courses](/category/power-bi)[Tableau Courses](/category/tableau)[Alteryx Courses](/category/alteryx)[Azure Courses](/category/azure)[AWS Courses](/category/aws)[Google Cloud Courses](/category/google-cloud)[Google Sheets Courses](/category/google-sheets)[Excel Courses](/category/excel)[AI Courses](/category/artificial-intelligence)[Data Analysis Courses](/category/data-analysis)[Data Visualization Courses](/category/data-visualization)[Machine Learning Courses](/category/machine-learning)[Data Engineering Courses](/category/data-engineering)[Probability & Statistics Courses](/category/probability-and-statistics)

**DataLab**

[Get Started](/datalab)[Pricing](/datalab/pricing)[Security](/datalab/security)[Documentation](https://datalab-docs.datacamp.com)

**Certification**

[Certifications](/certification)[Data Scientist](/certification/data-scientist)[Data Analyst](/certification/data-analyst)[Data Engineer](/certification/data-engineer)[SQL Associate](/certification/sql-associate)[Power BI Data Analyst](/certification/data-analyst-in-power-bi)[Tableau Certified Data Analyst](/certification/data-analyst-in-tableau)[Azure Fundamentals](/certification/azure-fundamentals)[AI Fundamentals](/certification/ai-fundamentals)

**Resources**

[Resource Center](/resources)[Upcoming Events](/webinars)[Blog](/blog)[Code-Alongs](/code-along)[Tutorials](/tutorial)[Docs](/doc)[Open Source](/open-source)[RDocumentation](https://www.rdocumentation.org)[Book a Demo with DataCamp for Business](/business/demo)[Data Portfolio](/data-portfolio)

**Plans**

[Pricing](/pricing)[For Students](/pricing/student)[For Business](/business)[For Universities](/universities)[Discounts, Promos & Sales](/promo)[Expense DataCamp](/expense)[DataCamp Donates](/donates)

**For Business**

[Business Pricing](/business/compare-plans)[Teams Plan](/business/learn-teams)[Data & AI Unlimited Plan](/business/data-unlimited)[Customer Stories](/business/customer-stories)[Partner Program](/business/partner-program)

**About**

[About Us](/about)[Learner Stories](/stories)[Careers](/careers)[Become an Instructor](/learn/create)[Press](/press)[Leadership](/about/leadership)[Contact Us](https://support.datacamp.com/hc/en-us/articles/360021185634)[DataCamp Español](/es)[DataCamp Português](/pt)[DataCamp Deutsch](/de)[DataCamp Français](/fr)

**Support**

[Help Center](https://support.datacamp.com/hc/en-us)[Become an Affiliate](/affiliates)

[Facebook](https://www.facebook.com/datacampinc/)[Twitter](https://twitter.com/datacamp)[LinkedIn](https://www.linkedin.com/school/datacampinc/)[YouTube](https://www.youtube.com/channel/UC79Gv3mYp6zKiSwYemEik9A)[Instagram](https://www.instagram.com/datacamp/)

[Privacy Policy](/privacy-policy)[Cookie Notice](/cookie-notice)[Do Not Sell My Personal Information](/do-not-sell-my-personal-information)[Accessibility](/accessibility)[Security](/security)[Terms of Use](/terms-of-use)

© 2026 DataCamp, Inc. All Rights Reserved.

![](https://bat.bing.com/action/0?ti=27000250&tm=gtm002&Ver=2&mid=76bf9721-b095-4da9-b534-b721ab07f7e8&bo=2&sid=53ee55b04c8711f1a7908d2d97ce1509&vid=53eeb8704c8711f185e53fb32ee6668e&vids=1&msclkid=N&pi=0&lg=en-US&sw=1280&sh=800&sc=24&tl=What%20is%20GRPO%3F%20Group%20Relative%20Policy%20Optimization%20Explained%20%7C%20DataCamp&p=https%3A%2F%2Fwww.datacamp.com%2Fblog%2Fwhat-is-grpo-group-relative-policy-optimization&r=&lt=6906&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=1219)

![](https://www.ojrq.net/p/?return=&cid=13294&tpsync=no&auth=)