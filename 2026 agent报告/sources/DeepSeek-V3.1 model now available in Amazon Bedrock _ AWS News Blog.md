> Source: https://aws.amazon.com/blogs/aws/deepseek-v3-1-now-available-in-amazon-bedrock/

DeepSeek-V3.1 model now available in Amazon Bedrock | AWS News Blog


 [Skip to Main Content](#aws-page-content-main)


* Filter: All



* English
* [Contact us](https://aws.amazon.com/contact-us/?nc2=h_ut_cu)
* [AWS Marketplace](https://aws.amazon.com/marketplace/?nc2=h_utmp)
* Support
* My account

* Search

  Filter: All
* [Sign in to console](https://console.aws.amazon.com/console/home/?nc2=h_si&src=header-signin)
* [Create account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_su&src=header_signup)

AWS Blogs

* [Home](https://aws.amazon.com/blogs/)
* Blogs
* Editions

## [AWS News Blog](https://aws.amazon.com/blogs/aws/)

# DeepSeek-V3.1 model now available in Amazon Bedrock

by [Channy Yun (윤석찬)](https://aws.amazon.com/blogs/aws/author/channy-yun/ "Posts by Channy Yun (윤석찬)") on 18 SEP 2025 in [Amazon Bedrock](https://aws.amazon.com/blogs/aws/category/artificial-intelligence/amazon-machine-learning/amazon-bedrock/ "View all posts in Amazon Bedrock"), [Amazon Machine Learning](https://aws.amazon.com/blogs/aws/category/artificial-intelligence/amazon-machine-learning/ "View all posts in Amazon Machine Learning"), [Announcements](https://aws.amazon.com/blogs/aws/category/post-types/announcements/ "View all posts in Announcements"), [Artificial Intelligence](https://aws.amazon.com/blogs/aws/category/artificial-intelligence/ "View all posts in Artificial Intelligence"), [Featured](https://aws.amazon.com/blogs/aws/category/featured/ "View all posts in Featured"), [Launch](https://aws.amazon.com/blogs/aws/category/news/launch/ "View all posts in Launch"), [News](https://aws.amazon.com/blogs/aws/category/news/ "View all posts in News"), [Open Source](https://aws.amazon.com/blogs/aws/category/open-source/ "View all posts in Open Source"), [Serverless](https://aws.amazon.com/blogs/aws/category/serverless/ "View all posts in Serverless") [Permalink](https://aws.amazon.com/blogs/aws/deepseek-v3-1-now-available-in-amazon-bedrock/)  [Comments](https://aws.amazon.com/blogs/aws/deepseek-v3-1-now-available-in-amazon-bedrock/#Comments)   [Share](#)

|  |
| --- |
| [Voiced by Polly](https://aws.amazon.com/polly/) |

In March, [Amazon Web Services (AWS)](https://aws.amazon.com/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) became the [first cloud service provider to deliver DeepSeek-R1](https://aws.amazon.com/blogs/aws/deepseek-r1-now-available-as-a-fully-managed-serverless-model-in-amazon-bedrock/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) in a serverless way by launching it as a fully managed, generally available model in [Amazon Bedrock](https://aws.amazon.com/bedrock/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el). Since then, customers have used DeepSeek-R1’s capabilities through Amazon Bedrock to build [generative AI](https://aws.amazon.com/ai/generative-ai/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) applications, benefiting from the Bedrock’s robust guardrails and comprehensive tooling for safe AI deployment.

Today, I am excited to announce [DeepSeek-V3.1](https://aws.amazon.com/bedrock/deepseek?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) is now available as a fully managed foundation model in Amazon Bedrock. DeepSeek-V3.1 is a hybrid open weight model that switches between thinking mode (chain-of-thought reasoning) for detailed step-by-step analysis and non-thinking mode (direct answers) for faster responses.

According to [DeepSeek](https://huggingface.co/deepseek-ai/DeepSeek-V3.1-Base), the thinking mode of DeepSeek-V3.1 achieves comparable answer quality with better results, stronger multi-step reasoning for complex search tasks, and big gains in thinking efficiency compared with DeepSeek-R1-0528.

| Benchmarks | DeepSeek-V3.1 | DeepSeek-R1-0528 |
| --- | --- | --- |
| Browsecomp | **30.0** | 8.9 |
| Browsecomp\_zh | **49.2** | 35.7 |
| HLE | **29.8** | 24.8 |
| xbench-DeepSearch | **71.2** | 55.0 |
| Frames | **83.7** | 82.0 |
| SimpleQA | **93.4** | 92.3 |
| Seal0 | **42.6** | 29.7 |
| SWE-bench Verified | **66.0** | 44.6 |
| SWE-bench Multilingual | **54.5** | 30.5 |
| Terminal-Bench | **31.3** | 5.7 |
(c) <https://api-docs.deepseek.com/news/news250821>

DeepSeek-V3.1 model performance in tool usage and agent tasks has significantly improved through post-training optimization compared to previous DeepSeek models. DeepSeek-V3.1 also supports over 100 languages with near-native proficiency, including significantly improved capability in low-resource languages lacking large monolingual or parallel corpora. You can build global applications to deliver enhanced accuracy and reduced hallucinations compared to previous DeepSeek models, while maintaining visibility into its decision-making process.

Here are your key use cases using this model:

* **Code generation** – DeepSeek-V3.1 excels in coding tasks with improvements in software engineering benchmarks and code agent capabilities, making it ideal for automated code generation, debugging, and software engineering workflows. It performs well on coding benchmarks while delivering high-quality results efficiently.
* **Agentic AI tools** – The model features enhanced tool calling through post-training optimization, making it strong in tool usage and agentic workflows. It supports structured tool calling, code agents, and search agents, positioning it as a solid choice for building autonomous AI systems.
* **Enterprise applications** – DeepSeek models are integrated into various chat platforms and productivity tools, enhancing user interactions and supporting customer service workflows. The model’s multilingual capabilities and cultural sensitivity make it suitable for global enterprise applications.

As I mentioned in [my previous post](https://aws.amazon.com/blogs/aws/deepseek-r1-now-available-as-a-fully-managed-serverless-model-in-amazon-bedrock/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el), when implementing publicly available models, give careful consideration to data privacy requirements when implementing in your production environments, check for bias in output, and monitor your results in terms of data security, [responsible AI](https://aws.amazon.com/ai/responsible-ai/), and [model evaluation](https://aws.amazon.com/bedrock/evaluations/).

You can access the [enterprise-grade security features](https://aws.amazon.com/bedrock/security-compliance/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) of Amazon Bedrock and implement safeguards customized to your application requirements and responsible AI policies with [Amazon Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/). You can also evaluate and compare models to identify the optimal model for your use cases by using [Amazon Bedrock model evaluation tools](https://aws.amazon.com/blogs/aws/amazon-bedrock-model-evaluation-is-now-generally-available/).

**Get started with the DeepSeek-V3.1 model in Amazon Bedrock**
  
To test the DeepSeek-V3.1 model in [Amazon Bedrock console](https://console.aws.amazon.com/bedrock/home?#/text-generation-playground&trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el), choose **Chat/Text** under **Playgrounds** in the left menu pane. Then choose **Select model** in the upper left, and select **DeepSeek** as the category and **DeepSeek-V3.1** as the model. Then choose **Apply**.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/09/18/2025-deepseek-v3.1-2-select-model-2.jpg)

Using the selected **DeepSeek-V3.1** model, I run the following prompt example about technical architecture decision.

`Outline the high-level architecture for a scalable URL shortener service like bit.ly. Discuss key components like API design, database choice (SQL vs. NoSQL), how the redirect mechanism works, and how you would generate unique short codes.`

You can turn the thinking on and off by toggling **Model reasoning** mode to generate a response’s chain of thought prior to the final conclusion.

![](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2025/09/15/2025-deepseek-v3.1-3-chat-example.jpg)

You can also access the model using the [AWS Command Line Interface (AWS CLI)](https://aws.amazon.com/cli/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) and [AWS SDK](https://aws.amazon.com/developer/tools/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el). This model supports both the `InvokeModel` and `Converse` API. You can check out a [broad range of code examples](https://docs.aws.amazon.com/bedrock/latest/userguide/service_code_examples.html?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) for multiple use cases and a variety of programming languages.

To learn more, visit [DeepSeek model inference parameters and responses](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-deepseek.html?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) in the AWS documentation.

**Now available**
  
DeepSeek-V3.1 is now available in the US West (Oregon), Asia Pacific (Tokyo), Asia Pacific (Mumbai), Europe (London), and Europe (Stockholm) AWS Regions. Check the [full Region list](https://docs.aws.amazon.com/bedrock/latest/userguide/models-regions.html?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) for future updates. To learn more, check out the [DeepSeek in Amazon Bedrock product page](https://aws.amazon.com/bedrock/deepseek?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) and the [Amazon Bedrock pricing page](https://aws.amazon.com/bedrock/pricing/).

Give the DeepSeek-V3.1 model a try in the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el) today and send feedback to [AWS re:Post for Amazon Bedrock](https://repost.aws/tags/TAQeKlaPaNRQ2tWB6P7KrMag/amazon-bedrock) or through your usual AWS Support contacts.

— [Channy](https://linkedin.com/in/channy/)

**Updated on September 19, 2025** — Removed the model access section. Amazon Bedrock will simplify access to all serverless foundation models, and any new models, by automatically enabling them for every AWS account, eliminating the need to manually activate access through the Bedrock console. The model access page will be retired in October 8, 2025 Account administrators retain full control over model access through [AWS IAM policies](https://docs.aws.amazon.com/bedrock/latest/userguide/security_iam_id-based-policy-examples.html) and [Service Control Policies (SCPs)](https://github.com/aws-samples/service-control-policy-examples/) to restrict model access as needed.

![Channy Yun (윤석찬)](https://d2908q01vomqb2.cloudfront.net/7b52009b64fd0a2a49e6d8a939753077792b0554/2020/06/05/channyun_400x400.jpg)

### [Channy Yun (윤석찬)](https://aws.amazon.com/blogs/aws/author/channy-yun/ "Posts by Channy Yun (윤석찬)")

Channy is a Lead Blogger of AWS News Blog and Principal Developer Advocate for AWS Cloud. As an open web enthusiast and blogger at heart, he loves community-driven learning and sharing of technology.



Loading comments…

### Resources

* [Getting Started](https://aws.amazon.com/getting-started?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=news-resources)
* [What's New](https://aws.amazon.com/new?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=news-resources)
* [Top Posts](https://aws.amazon.com/blogs?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=news-resources)
* [Official AWS Podcast](https://aws.amazon.com/podcasts/aws-podcast?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=news-resources)
* [Case Studies](https://aws.amazon.com/solutions/case-studies?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=news-resources)
* [AWS re:Post](https://repost.aws/ "https://repost.aws/")

---

### Follow

* [Twitter](https://twitter.com/awscloud)
* [Facebook](https://www.facebook.com/amazonwebservices)
* [LinkedIn](https://www.linkedin.com/company/amazon-web-services/)
* [Twitch](https://www.twitch.tv/aws)
* [RSS Feed](https://aws.amazon.com/blogs/aws/feed/)
* [Email Updates](https://pages.awscloud.com/communication-preferences?sc_ichannel=ha&sc_icampaign=acq_awsblogsb&sc_icontent=news-social)

[Create an AWS account](https://signin.aws.amazon.com/signup?request_type=register)

## Learn

* [What Is AWS?](/what-is-aws/?nc1=f_cc)
* [What Is Cloud Computing?](/what-is-cloud-computing/?nc1=f_cc)
* [What Is Agentic AI?](/what-is/agentic-ai/?nc1=f_cc)
* [Cloud Computing Concepts Hub](/what-is/?nc1=f_cc)
* [AWS Cloud Security](/security/?nc1=f_cc)
* [What's New](/new/?nc1=f_cc)
* [Blogs](/blogs/?nc1=f_cc)
* [Press Releases](https://press.aboutamazon.com/press-releases/aws)

## Resources

* [Getting Started](/getting-started/?nc1=f_cc)
* [Training](/training/?nc1=f_cc)
* [AWS Trust Center](/trust-center/?nc1=f_cc)
* [AWS Solutions Library](/solutions/?nc1=f_cc)
* [Architecture Center](/architecture/?nc1=f_cc)
* [Product and Technical FAQs](/faqs/?nc1=f_dr)
* [Analyst Reports](/resources/analyst-reports/?nc1=f_cc)
* [AWS Partners](/partners/work-with-partners/?nc1=f_dr)

## Developers

* [Builder Center](/developer/?nc1=f_dr)
* [SDKs & Tools](/developer/tools/?nc1=f_dr)
* [.NET on AWS](/developer/language/net/?nc1=f_dr)
* [Python on AWS](/developer/language/python/?nc1=f_dr)
* [Java on AWS](/developer/language/java/?nc1=f_dr)
* [PHP on AWS](/developer/language/php/?nc1=f_cc)
* [JavaScript on AWS](/developer/language/javascript/?nc1=f_dr)

## Help

* [Contact Us](/contact-us/?nc1=f_m)
* [File a Support Ticket](https://console.aws.amazon.com/support/home/?nc1=f_dr)
* [AWS re:Post](https://repost.aws/?nc1=f_dr)
* [Knowledge Center](https://repost.aws/knowledge-center/?nc1=f_dr)
* [AWS Support Overview](/premiumsupport/?nc1=f_dr)
* [Get Expert Help](https://iq.aws.amazon.com/?utm=mkt.foot/?nc1=f_m)
* [AWS Accessibility](/accessibility/?nc1=f_cc)
* [Legal](/legal/?nc1=f_cc)

English

Back to top

Amazon is an Equal Opportunity Employer: Minority / Women / Disability / Veteran / Gender Identity / Sexual Orientation / Age.

[x](https://twitter.com/awscloud) [facebook](https://www.facebook.com/amazonwebservices) [linkedin](https://www.linkedin.com/company/amazon-web-services/) [instagram](https://www.instagram.com/amazonwebservices/) [twitch](https://www.twitch.tv/aws) [youtube](https://www.youtube.com/user/AmazonWebServices/Cloud/) [podcasts](/podcasts/?nc1=f_cc) [email](https://pages.awscloud.com/communication-preferences?trk=homepage)

* [Privacy](/privacy/?nc1=f_pr)
* [Site terms](/terms/?nc1=f_pr)
* [Cookie Preferences](#)

© 2026, Amazon Web Services, Inc. or its affiliates. All rights reserved.