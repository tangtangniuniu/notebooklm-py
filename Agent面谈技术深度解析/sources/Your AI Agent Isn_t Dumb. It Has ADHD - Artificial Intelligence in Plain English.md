> Source: https://ai.plainenglish.io/your-ai-agent-isnt-dumb-it-has-adhd-4686585bc5f2

LLM context drift: why AI agents forget instructions | Artificial Intelligence in Plain English

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fai.plainenglish.io%2Fyour-ai-agent-isnt-dumb-it-has-adhd-4686585bc5f2&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fai.plainenglish.io%2Fyour-ai-agent-isnt-dumb-it-has-adhd-4686585bc5f2&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## Artificial Intelligence in Plain English](https://ai.plainenglish.io/?source=post_page---publication_nav-78d064101951-4686585bc5f2---------------------------------------)

·

Follow publication

[![Artificial Intelligence in Plain English](https://miro.medium.com/v2/resize:fill:76:76/1*9zAmnK08gUCmZX7q0McVKw@2x.png)](https://ai.plainenglish.io/?source=post_page---post_publication_sidebar-78d064101951-4686585bc5f2---------------------------------------)

New AI, ML and Data Science articles every day. Follow to join our 3.5M+ monthly readers.

Follow publication

## THE STANFORD RESEARCH ON WHY LLMS LOSE TRACK OF INSTRUCTIONS MID-CONVERSATION, AND THE FIXES THAT ACTUALLY WORK.

# Your AI Agent Isn’t Dumb. It Has ADHD

[![Kuldeepsinh Jadeja](https://miro.medium.com/v2/resize:fill:64:64/1*p_6gFTCfXFQWGUqSDUKzQw@2x.jpeg)](https://medium.com/@kuldeepjadeja7?source=post_page---byline--4686585bc5f2---------------------------------------)

[Kuldeepsinh Jadeja](https://medium.com/@kuldeepjadeja7?source=post_page---byline--4686585bc5f2---------------------------------------)

Follow

5 min read

·

Apr 9, 2026

70

2

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D4686585bc5f2&operation=register&redirect=https%3A%2F%2Fai.plainenglish.io%2Fyour-ai-agent-isnt-dumb-it-has-adhd-4686585bc5f2&source=---header_actions--4686585bc5f2---------------------post_audio_button------------------)

Share

Press enter or click to view image in full size

![Around message 40, something changes | Kuldeepsinh Jadeja](https://miro.medium.com/v2/resize:fit:700/1*ZEZCBT78mGLqnH43AdfXHA@2x.jpeg)

Around message 40, something changes.

The AI that was following your rules precisely at the beginning starts bending them. Then ignoring them. By message 60, it’s doing something you never asked for confidently, fluently, completely off-brief.

You didn’t break it. It just forgot.

## The Problem Has a Name

I spent weeks blaming my prompts.

I’d rewrite them, tighten them, move instructions around. Sometimes things got better. Sometimes they got worse. There was no consistent pattern, just the same maddening drift where the AI would nail the first few steps and then completely abandon the constraints I’d set by step eight.

> Then I found the research. And it explained everything.

A 2023 Stanford study called “***Lost in the Middle***” measured how well LLMs recall information based on where it sits in the context window. The result was striking: performance drops by more than 30% when critical information lands in the middle of the conversation. Accuracy is high at the start. High at the end. It collapses in the middle – exactly like working memory overflow.

A 2025 follow-up by Laban et al. made it worse. In multi-turn conversations, instructions from early turns don’t just weaken – they get actively diluted by everything that comes after. The more turns, the worse the recall. Your carefully written system prompt is fighting a losing battle against its own conversation history.

Here’s the part that stopped me cold: 65% of enterprise AI failures in 2025 were attributed to context drift during multi-step reasoning.

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:700/1*E2CdM45ExugESlE7evuJNg@2x.jpeg)

The ‘Lost in the Middle’ effect, attention is high at the edges, collapsed in the center.

Not hallucination. Not model capability. Forgetting.

## Why the ADHD Parallel Isn’t Just a Metaphore

When I described this to a non-technical friend, I reached for the closest thing I knew: “*It’s like ADHD executive dysfunction. Strong pattern recognition. Weak control over long sequences.*”

The interesting thing is that this isn’t entirely a metaphor.

Transformer attention has a documented recency bias, It weights tokens near the start and end of the context window more heavily than those in the middle. Mid-context instructions don’t compete well for attention. They get buried under the accumulating weight of the conversation that came after them.

This is structurally similar to how working memory in ADHD brains handles dense instruction streams: high performance on the immediate task, degraded recall of earlier constraints when the cognitive load rises. The mechanism is different. The failure pattern is almost identical.

One comment I saw while researching this framed it cleanly: “**At some point it stops being about intelligence and starts being about signal density. Too much prose, too many loosely ranked instructions, and the model starts losing what actually matters.**”

That’s exactly right. And it tells you precisely where to attack the problem.

Press enter or click to view image in full size

![The model doesn’t need better instructions. It needs better information architecture | Kuldeepsinh Jadeja](https://miro.medium.com/v2/resize:fit:700/1*EY8bthS_KtsZ9y39vWCROA.jpeg)

The model doesn’t need better instructions. It needs better information architecture.

## Three Fixes That Actually Work

I tried a lot of things. Here’s what moved the needle.

1. **The Echo of Prompt technique**

The simplest fix: re-inject a condensed version of your original instructions before every major decision point in the workflow. Yes, it burns extra tokens. Yes, it feels inelegant. The completion quality goes up anyway.

## Get Kuldeepsinh Jadeja’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Subscribe

Remember me for faster sign in

Think of it as giving the AI a sticky note that follows it through the conversation. The core constraints never drift into the middle, you keep moving them back to the top.

```
CORE_CONSTRAINTS = """  
Always respond in JSON.  
Never skip validation steps.  
Flag uncertainty before proceeding.  
"""  
  
def build_prompt(history, new_user_message):  
    return [  
        {"role": "system", "content": CORE_CONSTRAINTS},  
        *history[-10:],  # Trim old context aggressively  
        {"role": "user", "content": new_user_message}  
    ]
```

**2. Checkpoint-and-Reload**

Instead of one continuous conversation, break the workflow at natural checkpoints. Each stage ends by writing its output to a structured file. The next stage starts fresh, loading that file as context.

```
def run_stage(stage_name, input_data, instructions):  
    response = call_llm(  
        system=instructions,  
        user=f"Input: {json.dumps(input_data)}"  
    )  
    output = parse_response(response)  
    save_checkpoint(stage_name, output)  
    return output  
  
# Each stage is a fresh context window  
stage1_output = run_stage("extract", raw_data, EXTRACT_INSTRUCTIONS)  
stage2_output = run_stage("validate", stage1_output, VALIDATE_INSTRUCTIONS)  
stage3_output = run_stage("format", stage2_output, FORMAT_INSTRUCTIONS)
```

More overhead upfront. Zero instruction drift. The tradeoff is obvious once you’ve lost a 30-step workflow to context rot at step 22.

**3. Aggressive Context Trimming**

The longer the conversation, the noisier the signal. Most agentic workflows carry far more history than they need – every intermediate response, every clarification, every redundant step.

Trim ruthlessly. Keep the last 8–12 turns of meaningful exchange, not the full transcript. Summarize older turns into a compact state block rather than preserving them verbatim. The model doesn’t need to re-read everything it said – it needs to know where it is.

```
def compress_history(history, keep_last=10):  
    if len(history) <= keep_last:  
        return history  
      
    old_turns = history[:-keep_last]  
    summary = summarize_to_state(old_turns)  
      
    return [  
        {"role": "system", "content": f"Previous context: {summary}"},  
        *history[-keep_last:  
	]
```

This is the approach that makes the “Lost in the Middle” research work in your favour, by ensuring critical information never drifts into the middle in the first place.

## What This Changes About How You Build

Here’s what I’ve seen in real agentic systems: the developers who run into the fewest context drift problems aren’t using better prompts. They’re using shorter conversations.

They design workflows that naturally surface constraints at decision points. They treat the context window as a limited resource – not a transcript. They build checkpoints in, not as a fix but as a feature.

The ADHD parallel is actually useful beyond the metaphor. Strategies that work for executive function challenges – externalising memory, breaking tasks into discrete steps, regular re-orientation – map almost perfectly onto what makes agentic AI workflows reliable.

Your AI doesn’t need better instructions. It needs better information architecture.

Press enter or click to view image in full size

![Design workflows that surface constraints at decision points — not ones that bury them | Kuldeepsinh Jadeja](https://miro.medium.com/v2/resize:fit:700/1*rixvdjIUzJs5aD79Fb57SA.png)

Design workflows that surface constraints at decision points, not ones that bury them.

Context drift is the most underrated failure mode in agentic AI. The model isn’t getting dumber – your instructions are getting buried. Re-inject core constraints at decision points, break long workflows into checkpointed stages, and treat context history as a signal to manage, not a transcript to preserve. These three changes will do more for your workflow reliability than any prompt rewrite.

> Around message 40, something changes.

> **Now you know why and, more importantly, what to do about it before you get there.**

**A message from our Founder**

Hey, [Sunil](https://linkedin.com/in/sunilsandhu) here. I wanted to take a moment to thank you for reading until the end and for being a part of this community. Did you know that our team run these publications as a volunteer effort to over 3.5m monthly readers? We don’t receive any funding, we do this to support the community.

If you want to show some love, please take a moment to follow me on [LinkedIn](https://linkedin.com/in/sunilsandhu), [TikTok](https://tiktok.com/@messyfounder), [Instagram](https://instagram.com/sunilsandhu). You can also subscribe to our [weekly newsletter](https://newsletter.plainenglish.io/). And before you go, don’t forget to clap and follow the writer️!

[Artificial Intelligence](https://medium.com/tag/artificial-intelligence?source=post_page-----4686585bc5f2---------------------------------------)

[Programming](https://medium.com/tag/programming?source=post_page-----4686585bc5f2---------------------------------------)

[Machine Learning](https://medium.com/tag/machine-learning?source=post_page-----4686585bc5f2---------------------------------------)

[Software Development](https://medium.com/tag/software-development?source=post_page-----4686585bc5f2---------------------------------------)

[Ai Agents](https://medium.com/tag/ai-agent?source=post_page-----4686585bc5f2---------------------------------------)

70

70

2

[![Artificial Intelligence in Plain English](https://miro.medium.com/v2/resize:fill:96:96/1*9zAmnK08gUCmZX7q0McVKw@2x.png)](https://ai.plainenglish.io/?source=post_page---post_publication_info--4686585bc5f2---------------------------------------)

[![Artificial Intelligence in Plain English](https://miro.medium.com/v2/resize:fill:128:128/1*9zAmnK08gUCmZX7q0McVKw@2x.png)](https://ai.plainenglish.io/?source=post_page---post_publication_info--4686585bc5f2---------------------------------------)

Follow

[## Published in Artificial Intelligence in Plain English](https://ai.plainenglish.io/?source=post_page---post_publication_info--4686585bc5f2---------------------------------------)

[44K followers](/followers?source=post_page---post_publication_info--4686585bc5f2---------------------------------------)

·[Last published 5 hours ago](/google-built-an-agent-os-at-i-o-2026-the-models-are-just-the-marketing-7c976c3a622f?source=post_page---post_publication_info--4686585bc5f2---------------------------------------)

New AI, ML and Data Science articles every day. Follow to join our 3.5M+ monthly readers.

Follow

[![Kuldeepsinh Jadeja](https://miro.medium.com/v2/resize:fill:96:96/1*p_6gFTCfXFQWGUqSDUKzQw@2x.jpeg)](https://medium.com/@kuldeepjadeja7?source=post_page---post_author_info--4686585bc5f2---------------------------------------)

[![Kuldeepsinh Jadeja](https://miro.medium.com/v2/resize:fill:128:128/1*p_6gFTCfXFQWGUqSDUKzQw@2x.jpeg)](https://medium.com/@kuldeepjadeja7?source=post_page---post_author_info--4686585bc5f2---------------------------------------)

Follow

[## Written by Kuldeepsinh Jadeja](https://medium.com/@kuldeepjadeja7?source=post_page---post_author_info--4686585bc5f2---------------------------------------)

[201 followers](https://medium.com/@kuldeepjadeja7/followers?source=post_page---post_author_info--4686585bc5f2---------------------------------------)

·[43 following](https://medium.com/@kuldeepjadeja7/following?source=post_page---post_author_info--4686585bc5f2---------------------------------------)

Building AI systems that actually work in production. Writing about automation, agents, and hidden failure modes. Not hype. Just reality.

Follow

[Help](https://help.medium.com/hc/en-us?source=post_page-----4686585bc5f2---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----4686585bc5f2---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----4686585bc5f2---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----4686585bc5f2---------------------------------------)

[Press](mailto:pressinquiries@medium.com)

[Blog](https://blog.medium.com/?source=post_page-----4686585bc5f2---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----4686585bc5f2---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----4686585bc5f2---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----4686585bc5f2---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----4686585bc5f2---------------------------------------)