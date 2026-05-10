> Source: https://www.hiberus.com/en/blog/ai-agent-for-text2sql/

AI Agent for Text2SQL: The Magical Recipe for Natural Database Interactions - hiberus blog - Exploring Technology, AI, and Digital Experiences









[![hiberus blog – Exploring Technology, AI, and Digital Experiences](https://www.hiberus.com/en/blog/wp-content/uploads/2023/04/Hiberus_blog-logo.png)![hiberus blog – Exploring Technology, AI, and Digital Experiences](https://www.hiberus.com/en/blog/wp-content/uploads/2023/04/Hiberus_blog-logo.png)](https://www.hiberus.com/en/blog/)

[About hiberus](https://www.hiberus.com/en/)

[Digital](https://www.hiberus.com/en/blog/category/hiberus/)[Generative AI](https://www.hiberus.com/en/blog/category/generative-ai/)

# AI Agent for Text2SQL: The Magical Recipe for Natural Database Interactions

By [Nour Eddine Zekaoui](https://www.hiberus.com/en/blog/author/nour-eddine-zekaoui/ "Posts by Nour Eddine Zekaoui")

Mar 05, 2025

3 Mins read

Find out how we can help you harness the potential of AI to boost your business.

[Contact us!](https://www.hiberus.com/en/experts-generative-ai-ld)

Have you ever dreamed of talking to your database like you’d chat with a colleague? The rise of text-to-SQL solutions has brought us excitingly close to this reality – a world where business users can gain insights from their data without writing a single line of SQL code.

As an AI developer working at the intersection of language models and databases, I’ve observed a fascinating transformation in how we interact with data. When ChatGPT burst onto the scene, one of my clients asked a seemingly simple question: “Could we connect ChatGPT to our databases for natural language queries?” While many might reach for a RAG (Retrieval-Augmented Generation) pipeline, I discovered that building a dedicated AI agent would yield far more powerful results.

Join me as I share my journey of creating a robust Text2SQL AI Agent using LangChain and LangGraph – a solution you can adapt for your own projects.

## The Power of AI Agents

In the rapidly evolving AI landscape, AI agents stand out as game-changers. **Harrison Chase**, co-founder of LangChain, offers a compelling definition:

> “An AI Agent is a system that uses an LLM to decide the control flow of an application.”

This isn’t just another buzzword. AI agents surpass simple text completion – they’re decision-making engines that orchestrate complex workflows. When you feed an input to a Large Language Model (LLM), it doesn’t just predict the next word; it makes strategic decisions about actions and pathways to achieve your goal.

![Diagram AI Agents](https://www.hiberus.com/en/blog/wp-content/uploads/2025/03/1-text-to-sql-1024x753.png)

## The Four Pillars of Success

Every good AI agent is built on four fundamental pillars:

### 1. The Brain (LLM)

* Powers decision-making and understanding
* In our case, we’re using Azure OpenAI’s GPT-4
* Adaptable to other models like [DeepSeek R1](https://www.hiberus.com/en/blog/deepseek-r1-vs-v3-choosing-the-right-model-for-your-ai-needs/)

### 2. Planning

* Strategizes the sequence of actions needed
* Breaks down complex queries into manageable steps
* Determines the optimal approach for each query
* For example, when asked about sales data:
  + First, identify relevant tables (customers, sales, employees)
  + Then, determine necessary joins
  + Finally, plan aggregations and filtering

### 3. The Tools

* The agent’s practical capabilities
* For our SQL agent, includes:
  + Database table listing
  + Schema information retrieval
  + Query validation
  + Query execution

### 4. The Memory

* Enables contextual understanding
* Maintains conversation state
* Facilitates natural dialogue about data
* Remembers previous queries for context

To illustrate how these pillars work together, let’s analyse a real example with the question: *“Which customers spent the most in each country?”*

#### 1. The LLM processes the question and understands:

* We need to find customer spending.
* Group by country.
* Identify the highest spenders in each group.

#### 2. Planning comes into play:

* It needs to identify tables containing customer, invoice, and location data.
* It will require aggregating spending by customer.
* It must group results by country.
* It needs to rank customers within each country group.
* It plans the sequence: customer location → purchase data → aggregation → ranking.

#### 3. Tools execute in sequence:

* First, it lists available tables.
* It retrieves schema information for relevant tables (e.g., Customer, Invoice).
* It constructs and validates the query (iterating and improving until a valid query is generated).

#### 4. Memory stores:

* The tables used.
* The relationship between customers and invoices.
* The fact that we are interested in customer spending.
* This context helps with **follow-up questions** like “Show me their recent purchases.”

![Example with the question: "Which customers spent the most in each country?"](https://www.hiberus.com/en/blog/wp-content/uploads/2025/03/2-text-to-sql-1024x444.png)

## Building the Magic

Let’s dive into the implementation. We’ll use LangChain for core functionality and LangGraph for workflow orchestration. Here’s our agent’s foundation:

![LangChain for core functionality and LangGraph for workflow orchestration.](https://www.hiberus.com/en/blog/wp-content/uploads/2025/03/3-text-to-sql.png)

The real magic happens in our tools’ implementation:

![Tools' implementation](https://www.hiberus.com/en/blog/wp-content/uploads/2025/03/4-text-to-sql.png)

## The Agent at Work

When a user poses a question like *“Which sales agent made the most in sales in 2009?”*, our agent springs into action:

1. 1Surveys the database landscape (lists available tables)
2. Understands the data structure (retrieves schema information)
3. Crafts and validates the perfect SQL query
4. Executes the query and presents results in plain English

## Powerful Features, Real Benefits

Our implementation delivers several key advantages:

1. **Rock-Solid Security:** Query validation prevents SQL injection and errors
2. **Adaptable Design:** Works with various databases and schemas
3. **Easy Maintenance:** Clean, modular code structure
4. **Contextual Intelligence:** Maintains conversation history
5. **Natural Interaction:** Understands plain English queries

## Real-World Impact

This Text2SQL agent transforms various business scenarios:

* **Business Intelligence:** Democratizes data access for non-technical users
* **Data Analysis:** Simplifies complex query construction
* **Customer Service:** Enables quick, accurate data retrieval
* **Database Administration:** Streamlines routine operations

## See It in Action

I’ve prepared a demonstration that showcases our agent handling various queries:

1. “Show me the top 5 best-selling tracks of all time”
2. “What was the total revenue for each genre in 2009?”
3. “Which customers spent the most in each country?”

The demo highlights how we’ve bridged the gap between technical SQL capabilities and user-friendly interaction, making database querying accessible to everyone in your organization.

## Conclusion

Building an efficient Text2SQL AI Agent isn’t just about connecting an LLM to a database – it’s about carefully orchestrating the interaction between language understanding, tool capabilities, and memory. Through LangChain and LangGraph, we’ve created a solution that makes database interactions feel natural and accessible.

At [hiberus](https://www.hiberus.com/en), we are ready to help you implement AI in your organization. Our expertise in [generative AI](https://www.hiberus.com/en/partners/aws) allows us to design personalized solutions that drive your business toward the future. Have questions or ideas for improvements? Let’s connect and collaborate! 

**Contact us to discover how AI can revolutionize your business!**

### Want to learn more about AI Agents?

Contact with our GenIA team

I have read and accept the [Privacy Policy](https://www.hiberus.com/en/policy)

I would like to receive marketing communications from Hiberus and about its products, services and events.

[AI](https://www.hiberus.com/en/blog/tag/ai/)

5627

3

* [![](https://www.hiberus.com/en/blog/wp-content/uploads/2024/05/ia-generativa.jpg)](https://www.hiberus.com/en/experts-generative-ai-ld)

![](https://www.hiberus.com/en/blog/wp-content/uploads/2025/03/neddine_1-300x300-1-150x150.jpg)

1 posts

[Nour Eddine Zekaoui](https://www.hiberus.com/en/blog/author/nour-eddine-zekaoui/ "Posts by Nour Eddine Zekaoui")

Data Scientist en hiberus

## Related posts

[Digital](https://www.hiberus.com/en/blog/category/hiberus/)

### [hiberus and QPR Software, a partnership to drive operational excellence](https://www.hiberus.com/en/blog/partnership-qpr-software/)

By [Sofía Villarreal](https://www.hiberus.com/en/blog/author/sofia-villarreal/ "Posts by Sofía Villarreal")

Jan 20, 2026

1 Mins read

In an age driven by data and AI, truly understanding your operations is the ultimate competitive advantage. Yet many organizations still operate…

[Case Studies](https://www.hiberus.com/en/blog/category/case-studies/)[Generative AI](https://www.hiberus.com/en/blog/category/generative-ai/)

### [Success Story: Content moderation with AI for retail and social platforms](https://www.hiberus.com/en/blog/success-story-content-moderation-with-ai-for-retail-and-social-platforms/)

By [Rebeca Sarai González Guerra](https://www.hiberus.com/en/blog/author/rgonzalezg/ "Posts by Rebeca Sarai González Guerra")

Jul 16, 2025

3 Mins read

In an increasingly globalized, hyper-connected and exposed digital ecosystem, the visual and textual content that a brand or community publishes not only…

[Case Studies](https://www.hiberus.com/en/blog/category/case-studies/)[Generative AI](https://www.hiberus.com/en/blog/category/generative-ai/)

### [Success Story: We use AI to generate SQL queries from natural language](https://www.hiberus.com/en/blog/success-story-we-use-ai-to-generate-sql-queries-from-natural-language/)

By [Miriam Arroyo](https://www.hiberus.com/en/blog/author/miriam-arroyo/ "Posts by Miriam Arroyo")

Jul 02, 2025

4 Mins read

In an increasingly data-driven environment, accessing the right information quickly and accurately is key to decision making. However, many organizations still rely…

Leave a Reply [Cancel reply](/en/blog/ai-agent-for-text2sql/#respond)

Your email address will not be published. Required fields are marked \*

Name\*

Email\*

Website

Save my name, email, and website in this browser for the next time I comment.

### Don't miss anything!

We keep you up to date with trends and news about the future of work, ways to grow your business, digital leadership and much more.

Newsletter

I have read and accept the [**Privacy policy**](https://www.hiberus.com/en/policy)

* + ABOUT US
    - [About hiberus](https://www.hiberus.com/en/digital-agency)
    - [Our group](https://www.hiberus.com/en/about-hiberus)
    - [Mission, vision and values](https://www.hiberus.com/en/mission-vision)
    - [Our Story](https://www.hiberus.com/en/about-hiberus)
* + [SECTORS](https://www.hiberus.com/en/solutions)
    - [Government](https://www.hiberus.com/en/sectors/public-administration)
    - [Banking and Finantial Services](https://www.hiberus.com/en/sectors/banking)
    - [Media and Communications](https://www.hiberus.com/en/sectors/telecommunications)
    - [Transport and Logistics](https://www.hiberus.com/en/sectors/transport)
    - [Retail and Distribution](https://www.hiberus.com/en/sectors/retail)
    - [Industry](https://www.hiberus.com/en/sectors/manufacturing)
    - [Leisure and Travel](https://www.hiberus.com/en/sectors/leisure-tourism)
* + [BUSINESS AREAS](#)
    - [Cloud Services](https://www.hiberus.com/en/systems/infrastructure)
    - [Application Management](https://www.hiberus.com/en)
    - [Enterprise Efficiency](https://www.hiberus.com/en/enterprise-efficiency)
    - [Data Intelligence](https://www.hiberus.com/en/data-ai)
    - [Total Experience](https://www.hiberus.com/en/digital-agency)
* + [SOLUTIONS](https://www.hiberus.com/en/solutions)
    - [Xalok, Global Publishing Platform](https://www.xalok.com/english)
    - [Travel One Inventory, solution for touroperators](https://www.hiberus.com/en/solutions/travel-one-inventory)
    - [Aficion 360, solutions for sports clubs](https://www.hiberus.com/en/solutions/aficion-360)
    - [Tiketee, Solution for the sale and booking of tickets](https://www.hiberus.com/en/solutions/tiketee)
    - [KVP, Shift management and schedule quadrants](https://www.hiberus.com/en/solutions/kvp)
    - [Sintra, software for customer attention an appointments](https://www.hiberus.com/en/solutions/sintra)
    - [Gisir, Reverse logistics management system](https://www.hiberus.com/en/solutions/gisir)
    - [Atlas, Cloud-based Contract and Document Management Software](https://www.hiberus.com/en/solutions/atlas)
    - [Bookme, Corporate booking software](https://www.hiberus.com/en/solutions/bookme)
    - [Hube, Virtualization and optimization of construction sector](https://www.hiberus.com/en/solutions/hube)
* + [CONTACT](https://www.hiberus.com/en/contact)

![Hiberus Tecnología](/en/blog/wp-content/uploads/2023/04/logo-hiberus.png "Hiberus Tecnología")

Contact us...

[HQ: +34 902 877 392](tel:+34902877392)

[USA: +1 305 586 8241](tel:+13055868241)

* [Cookies Policy](https://www.hiberus.com/en/cookies)
* [Legal Notice](https://www.hiberus.com/en/legal-notice)
* [Privacy and Security Policy](https://www.hiberus.com/en/policy)
* [Quality Policy](https://www.hiberus.com/en/policy)