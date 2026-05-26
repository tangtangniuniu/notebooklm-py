> Source: https://dev.to/sreeni5018/the-architecture-of-agent-memory-how-langgraph-really-works-59ne

The Architecture of Agent Memory: How LangGraph Really Works - DEV Community






[Skip to content](#main-content)

Navigation menu

[![DEV Community](https://media2.dev.to/dynamic/image/quality=100/https://dev-to-uploads.s3.amazonaws.com/uploads/logos/resized_logo_UQww2soKuUsjaOGNB38o.png)](/)

Search

[Powered by Algolia
Search](https://www.algolia.com/developers/?utm_source=devto&utm_medium=referral)

[Log in](https://dev.to/enter?signup_subforem=1)
[Create account](https://dev.to/enter?signup_subforem=1&state=new-user)

## DEV Community

Close

![](https://assets.dev.to/assets/heart-plus-active-9ea3b22f2bc311281db911d416166c5f430636e76b15cd5df6b3b841d830eefa.svg)




Add reaction

![](https://assets.dev.to/assets/sparkle-heart-5f9bee3767e18deb1bb725290cb151c25234768a0e9a2bd39370c382d02920cf.svg)


Like


![](https://assets.dev.to/assets/multi-unicorn-b44d6f8c23cdd00964192bedc38af3e82463978aa611b4365bd33a0f1f4f3e97.svg)


Unicorn


![](https://assets.dev.to/assets/exploding-head-daceb38d627e6ae9b730f36a1e390fca556a4289d5a41abb2c35068ad3e2c4b5.svg)


Exploding Head


![](https://assets.dev.to/assets/raised-hands-74b2099fd66a39f2d7eed9305ee0f4553df0eb7b4f11b01b6b1b499973048fe5.svg)


Raised Hands


![](https://assets.dev.to/assets/fire-f60e7a582391810302117f987b22a8ef04a2fe0df7e3258a5f49332df1cec71e.svg)


Fire

Jump to Comments








Save







Boost

More...

Copy link
Copy link

Copied to Clipboard

[Share to X](https://twitter.com/intent/tweet?text=%22The%20Architecture%20of%20Agent%20Memory%3A%20How%20LangGraph%20Really%20Works%22%20by%20Seenivasa%20Ramadurai%20%23DEVCommunity%20https%3A%2F%2Fdev.to%2Fsreeni5018%2Fthe-architecture-of-agent-memory-how-langgraph-really-works-59ne)
[Share to LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fdev.to%2Fsreeni5018%2Fthe-architecture-of-agent-memory-how-langgraph-really-works-59ne&title=The%20Architecture%20of%20Agent%20Memory%3A%20How%20LangGraph%20Really%20Works&summary=A%20deep%20dive%20into%20state%2C%20reducers%2C%20and%20why%20your%20AI%20agent%20keeps%20forgetting%20things%20%20To%20understand...&source=DEV%20Community)
[Share to Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fdev.to%2Fsreeni5018%2Fthe-architecture-of-agent-memory-how-langgraph-really-works-59ne)
[Share to Mastodon](https://s2f.kytta.dev/?text=https%3A%2F%2Fdev.to%2Fsreeni5018%2Fthe-architecture-of-agent-memory-how-langgraph-really-works-59ne)



[Share Post via...](#)
[Report Abuse](/report-abuse)



[![Cover image for The Architecture of Agent Memory: How LangGraph Really Works](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fxmxlyc1kmdkhqfize6se.png)](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fxmxlyc1kmdkhqfize6se.png)

[![Seenivasa Ramadurai](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F1829954%2F564a03dc-062e-4c58-b28e-be52605aefa8.jpg)](/sreeni5018)

[Seenivasa Ramadurai](/sreeni5018)

Posted on Dec 14, 2025

![](https://assets.dev.to/assets/sparkle-heart-5f9bee3767e18deb1bb725290cb151c25234768a0e9a2bd39370c382d02920cf.svg)
 
 ![](https://assets.dev.to/assets/multi-unicorn-b44d6f8c23cdd00964192bedc38af3e82463978aa611b4365bd33a0f1f4f3e97.svg)
 
 ![](https://assets.dev.to/assets/exploding-head-daceb38d627e6ae9b730f36a1e390fca556a4289d5a41abb2c35068ad3e2c4b5.svg)
 
 ![](https://assets.dev.to/assets/raised-hands-74b2099fd66a39f2d7eed9305ee0f4553df0eb7b4f11b01b6b1b499973048fe5.svg)
 
 ![](https://assets.dev.to/assets/fire-f60e7a582391810302117f987b22a8ef04a2fe0df7e3258a5f49332df1cec71e.svg)

# The Architecture of Agent Memory: How LangGraph Really Works

[#ai](/t/ai)
[#agents](/t/agents)
[#llm](/t/llm)
[#architecture](/t/architecture)

**A deep dive into state, reducers, and why your AI agent keeps forgetting things**

To understand LangGraph's power, one must first understand its **memory** system. When developers first explore LangGraph, they naturally focus on visible components the **Nodes** where reasoning happens, the **Edges** that define flow, and the **Tools** an agent uses to act. But beneath these lies the execution memory, simply called state, and this is what truly determines how an agent thinks, evolves, persists, and ultimately behaves across time.

**State** is not just a bucket for data. It is the living record of an agent's reasoning every input it receives, every intermediate thought it produces, every tool output it collects, and every decision it makes as the graph is traversed. This chapter explains why state is designed the way it is in LangGraph, how updates are applied, what reducers are, and why traditional Python models like **Pydantic** or **Dataclass** often fail for state in agent workflows.

## What State Is And What It Isn't

In LangGraph, the state represents the shared memory of the agent as it executes through nodes. Each node receives the current state as input, performs its logic, and returns only the part of the state it wants to update. LangGraph then merges that update into the existing state according to rules defined by the schema you provided. This isn't a simple assignment; it is a controlled, deterministic update that can append, overwrite, or combine data depending on how the state is defined.

The simplest form of state definition uses a Python TypedDict:

```
from typing_extensions import TypedDict

class State(TypedDict):
    messages: list
    extra_field: int
```

Enter fullscreen mode

Exit fullscreen mode

This defines the shape of the memory the agent will carry through its execution.

State can also store more than just conversation history. It can accumulate tool outputs, metadata, task status, counters, retrieved documents, and more all in the same object that flows through the graph. In more complex applications, managing this state effectively becomes the agent's core cognitive function, similar to how a human remembers what happened earlier in a conversation.

## Why We Don't Rely on Pydantic or Dataclass for State

LangGraph documentation notes that state can in principle be defined using a **Pydantic** model or a **Dataclass** in addition to TypedDict. But this flexibility comes with trade offs that are important in real use cases.

## The Problem of Efficiency and Partial Updates

**Pydantic** models and **Dataclasses** are designed for validated object representation, where each field is expected to be complete and consistent at instantiation. This means that to update even one field, you typically end up reconstructing the entire model or mutating it in place.

In agent workflows, state updates are frequent and often tiny. For example, a node might only want to add a few messages to the history or increment a counter. With **Pydantic** or **Dataclass**, you either mutate the **whole object**, breaking immutability guarantees that LangGraph relies on for deterministic merging, or reconstruct the object with an updated field, which is expensive and often redundant. This is particularly bad when state includes long histories or large collections.

**TypedDict**, in contrast, allows partial updates easily nodes just return a dict with the keys they want to update. LangGraph then knows how to merge these changes back into the full state object.

## Potential Caching Considerations with Pydantic

Some developers have reported that using **Pydantic** models as state can occasionally lead to unexpected behavior with caching. This may happen because **Pydantic** internal metadata can vary between instantiations, potentially causing LangGraph to treat logically identical states differently. While this is not universal, it is worth being aware of when choosing your state representation approach.

## Reducer Semantics Are Harder to Attach to Rich Models

LangGraph's state merging is driven by reducers functions that define how to combine existing state with new updates. Attaching reducer semantics to **Dataclass** or **Pydantic** fields is possible via annotations, but it is much clearer and more natural in a **TypedDict** declared state where each field's type and reducer annotation are explicit.

For these reasons, most production **LangGraph** graphs use **TypedDict** for state schemas, and rely on reducers to control how fields evolve.

## What Are Reducers and Why They Matter

Reducers are the core mechanism for merging updates into state. When nodes produce updates, LangGraph looks at each key and either overwrites the value or calls a reducer function to combine the existing value with the new one.

Each reducer function has this signature:

```
def reducer(current_value, new_value) -> merged_value
```

Enter fullscreen mode

Exit fullscreen mode

By default, if no reducer is specified for a state key, any update to that key will overwrite the existing value. This is fine for simple scalar fields that should be replaced, like status flags or task names.

However, for many common use cases—such as appending messages, accumulating lists of results, or concatenating arrays—overwrite makes no sense. You don't want the history wiped every time a node runs; you want the new data merged into the existing memory.

To do this, LangGraph uses Python's Annotated type with a reducer function:

```
from typing import Annotated
from operator import add
from typing_extensions import TypedDict

class State(TypedDict):
    history: Annotated[list[str], add]
    count: int
```

Enter fullscreen mode

Exit fullscreen mode

Here, history will use Python's operator.add function to combine old and new lists. Now, if two nodes produce updates to the history key, LangGraph will append new values rather than overwrite.

## The Built-in add\_messages Reducer

While operator.add works well for simple lists, LangGraph provides a specialized built-in reducer called add\_messages specifically designed for handling conversation messages. This reducer is smarter than simple concatenation because it handles message deduplication by ID, which is essential when working with LangChain message objects like HumanMessage, AIMessage, and ToolMessage.

To use it, import add\_messages from langgraph.graph:

```
from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import add_messages

class State(TypedDict):
    messages: Annotated[list, add_messages]
```

Enter fullscreen mode

Exit fullscreen mode

The add\_messages reducer understands LangChain message formats and intelligently merges them. If a new message has the same ID as an existing message, it replaces the old one rather than creating a duplicate. This behavior is particularly important in agentic workflows where tool calls and responses need to be tracked correctly.

For most conversational agents built with LangGraph, add\_messages is the recommended reducer for the messages field. It handles edge cases that operator.add would miss, such as message updates during streaming or tool response matching.

## Reducers in Action A Detailed Example

Imagine an agent with three nodes. The first logs the start of a workflow, the second logs a step and returns a count increment, and the third logs completion.

Define the state like this:

```
from operator import add
from typing import Annotated
from typing_extensions import TypedDict

class MyState(TypedDict):
    logs: Annotated[list[str], add]
    counter: Annotated[int, add]
Each node returns only the changes it cares about:

def start_node(state: MyState):
    return {"logs": ["Started"], "counter": 1}

def step_node(state: MyState):
    return {"logs": ["Step done"], "counter": 2}

def finish_node(state: MyState):
    return {"logs": ["Finished"], "counter": 3}
```

Enter fullscreen mode

Exit fullscreen mode

As the graph executes, the state evolves. After start\_node runs, logs contains just "Started" and counter equals 1. After step\_node, logs becomes ["Started", "Step done"] and counter becomes 3. After finish\_node completes, logs holds all three entries and counter totals 6.

Reducers made this possible. The logs were appended and counter values accumulated. Without reducers, each new update would overwrite the previous, discarding history.

## Reducer Functions Beyond Simple Add

LangGraph doesn't restrict reducers to simple operations like add. You can write custom reducers to handle almost any merging logic you need. For example, you might want to remove old conversation context when a list grows too long, merge dictionaries while preserving keys, only accumulate distinct items, or handle complex transformations like parsing and stored summaries.

Here is an example of a custom reducer that removes duplicates:

```
def unique_merge(old_list, new_list):
    merged = old_list + new_list
    return list(dict.fromkeys(merged))

class State(TypedDict):
    unique_items: Annotated[list[str], unique_merge]
```

Enter fullscreen mode

Exit fullscreen mode

When updates arrive, unique\_merge combines them into a deduplicated list. You also don't have to limit reducer functions to built-ins; custom logic lets you handle domain-specific merging strategies.

## Short-Term vs Long-Term Memory

Aside from reducer driven merging, agents often need to persist memory across conversations or sessions. Here LangGraph distinguishes two memory scopes.

**Short-term memory** is the state that flows through your graph during a single invocation or thread. It persists conversation history, tool outputs, and intermediate values. LangGraph supports thread-scoped checkpoints, so even if an agent execution is paused or interrupted, the state can be resumed later.

**Long-term memory** is memory that persists across sessions or threads, often stored in a database or vector store. Long-term memory lets agents recall user preferences or facts from earlier conversations, enabling personalization. It isn't stored in the core state object itself; rather, it's integrated through stores that the agent can query and update.

Imagine building an assistant that greets a user, adds the greeting to memory, counts each interaction, and summarizes the history at the end.

Define the state:

```
from operator import add
from typing import Annotated
from typing_extensions import TypedDict

class AssistantState(TypedDict):
    conversation: Annotated[list[str], add]
    count: Annotated[int, add]
```

Enter fullscreen mode

Exit fullscreen mode

```
Nodes might look like:

def greet(state: AssistantState):
    return {"conversation": ["Hello!"], "count": 1}

def chat_step(state: AssistantState):
    user_msg = state["conversation"][-1] + " user said hi"
    return {"conversation": [user_msg], "count": 1}

def summarize(state: AssistantState):
    summary = f"Total interactions: {state['count']}"
    return {"conversation": [summary]}
```

Enter fullscreen mode

Exit fullscreen mode

As the graph runs, each node produces only the updates it cares about. The reducer accumulates conversation history and interaction counts, producing a coherent memory at the end.

## Why Reducers Matter in Real Workflows

Reducers solve a core semantic problem: how to combine updates from different parts of an agent's reasoning process so nothing is lost. Without reducers, only the last update would be retained for each state field, making conversation history, tool outputs, and incremental accumulations impossible to track reliably.

Reducers also support more complex workflows like parallel node execution, where multiple branches update the same key in the same cycle. Without a clear merge strategy, this would lead to conflicts. Reducers ensure updates are merged according to policy, avoiding silent overwrites.

## Summary

State in LangGraph isn't just a static data object. It is the execution memory of the agent, persisted as it moves through the graph and updated in a controlled fashion using reducers. Compared to Pydantic and **Dataclasses**, **TypedDict** with annotated reducers provides lightweight, partial updates without unnecessary validation overhead, deterministic merging semantics for concurrent and incremental updates, and support for both ***short-term*** and ***long-term***memory patterns.

| Use Case | Recommended Type | Why |
| --- | --- | --- |
| **Execution state of agent** | TypedDict | Lightweight, supports partial updates, compatible with reducers |
| **Input validation** | Pydantic | Ensures correct structure before execution |
| **Output validation** | Pydantic | Ensures final results adhere to schema |
| **Node-internal structured objects** | Dataclass | Provides type safety and immutability within nodes |
| **Merging incremental updates** | TypedDict + Reducers | Ensures deterministic accumulation without overwriting |

Reducers are the mechanism that turns isolated node outputs into a coherent story—a central function in LangGraph's memory architecture and the foundation for building **robust**, **stateful** **agents**.

## Example 1: Basic Reducer Demonstration

```
"""
Example 1: Basic Reducer Demonstration
======================================
Shows how reducers accumulate values instead of overwriting.
"""

from operator import add
from typing import Annotated
from typing_extensions import TypedDict

print("=" * 60)
print("BASIC REDUCER DEMONSTRATION")
print("=" * 60)

# Define State with Reducers
class State(TypedDict):
    logs: Annotated[list[str], add]      # Will APPEND
    counter: Annotated[int, add]          # Will SUM
    status: str                           # Will OVERWRITE (no reducer)

# Simulate node outputs
def start_node(state: State) -> dict:
    return {
        "logs": ["🚀 Started"],
        "counter": 1,
        "status": "running"
    }

def process_node(state: State) -> dict:
    return {
        "logs": ["⚙️ Processing"],
        "counter": 1,
        "status": "processing"
    }

def finish_node(state: State) -> dict:
    return {
        "logs": ["✅ Finished"],
        "counter": 1,
        "status": "done"
    }

# Simulate LangGraph's reducer behavior
def apply_reducer(current_state: dict, update: dict, state_class) -> dict:
    """Simulates how LangGraph applies reducers to merge updates."""
    new_state = current_state.copy()

    for key, new_value in update.items():
        if key in current_state:
            # Check if field has a reducer annotation
            annotations = state_class.__annotations__.get(key)
            if hasattr(annotations, '__metadata__'):
                # Has reducer - apply it
                reducer_fn = annotations.__metadata__[0]
                new_state[key] = reducer_fn(current_state[key], new_value)
            else:
                # No reducer - overwrite
                new_state[key] = new_value
        else:
            new_state[key] = new_value

    return new_state

# Run simulation
print("\n📍 Initial State:")
state = {"logs": [], "counter": 0, "status": "init"}
print(f"   {state}")

print("\n📍 After start_node:")
update = start_node(state)
print(f"   Node returned: {update}")
state = apply_reducer(state, update, State)
print(f"   State now: {state}")

print("\n📍 After process_node:")
update = process_node(state)
print(f"   Node returned: {update}")
state = apply_reducer(state, update, State)
print(f"   State now: {state}")

print("\n📍 After finish_node:")
update = finish_node(state)
print(f"   Node returned: {update}")
state = apply_reducer(state, update, State)
print(f"   State now: {state}")

print("\n" + "=" * 60)
print("RESULTS:")
print("=" * 60)
print(f"✅ logs APPENDED: {state['logs']}")
print(f"✅ counter SUMMED: {state['counter']} (1+1+1=3)")
print(f"✅ status OVERWROTE: '{state['status']}' (only last value)")
print("=" * 60)
```

Enter fullscreen mode

Exit fullscreen mode

## Example 2: Custom Reducers

```
"""
Example 2: Custom Reducers
==========================
Shows how to create custom reducer functions for specialized merge logic.
"""

from typing import Annotated
from typing_extensions import TypedDict

print("=" * 60)
print("CUSTOM REDUCERS DEMONSTRATION")
print("=" * 60)

# Custom Reducer 1: Keep only unique items
def unique_merge(old_list: list, new_list: list) -> list:
    """Merge lists keeping only unique items (preserves order)."""
    combined = old_list + new_list
    return list(dict.fromkeys(combined))

# Custom Reducer 2: Keep last N items
def keep_last_5(old_list: list, new_list: list) -> list:
    """Keep only the last 5 items."""
    combined = old_list + new_list
    return combined[-5:]

# Custom Reducer 3: Merge dictionaries
def merge_dicts(old_dict: dict, new_dict: dict) -> dict:
    """Deep merge dictionaries."""
    result = old_dict.copy()
    result.update(new_dict)
    return result

# Custom Reducer 4: Max value
def keep_max(old_val: int, new_val: int) -> int:
    """Keep the maximum value."""
    return max(old_val, new_val)

# Define State with custom reducers
class State(TypedDict):
    visited_urls: Annotated[list[str], unique_merge]
    recent_messages: Annotated[list[str], keep_last_5]
    metadata: Annotated[dict, merge_dicts]
    high_score: Annotated[int, keep_max]

# Simulate updates
def simulate_reducer(current, new_value, reducer_fn, name):
    result = reducer_fn(current, new_value)
    print(f"\n📍 {name}:")
    print(f"   Current: {current}")
    print(f"   New:     {new_value}")
    print(f"   Result:  {result}")
    return result

print("\n" + "-" * 60)
print("1️⃣  UNIQUE MERGE (removes duplicates)")
print("-" * 60)
urls = ["google.com", "github.com"]
new_urls = ["github.com", "stackoverflow.com", "google.com"]
urls = simulate_reducer(urls, new_urls, unique_merge, "visited_urls")

print("\n" + "-" * 60)
print("2️⃣  KEEP LAST 5 (sliding window)")
print("-" * 60)
messages = ["msg1", "msg2", "msg3"]
new_messages = ["msg4", "msg5", "msg6", "msg7"]
messages = simulate_reducer(messages, new_messages, keep_last_5, "recent_messages")

print("\n" + "-" * 60)
print("3️⃣  MERGE DICTS (combine dictionaries)")
print("-" * 60)
meta = {"user": "john", "role": "admin"}
new_meta = {"role": "superadmin", "team": "engineering"}
meta = simulate_reducer(meta, new_meta, merge_dicts, "metadata")

print("\n" + "-" * 60)
print("4️⃣  KEEP MAX (maximum value)")
print("-" * 60)
score = 85
new_score = 72
score = simulate_reducer(score, new_score, keep_max, "high_score (72 < 85)")

score = 85
new_score = 95
score = simulate_reducer(score, new_score, keep_max, "high_score (95 > 85)")

print("\n" + "=" * 60)
print("SUMMARY: Custom reducers give you full control over merging!")
print("=" * 60)
```

Enter fullscreen mode

Exit fullscreen mode

## Example 3: Full LangGraph Workflow with Reducers

```
"""
Example 3: Full LangGraph Workflow with Reducers
================================================
A complete working LangGraph example demonstrating state and reducers.
"""

from operator import add
from typing import Annotated
from typing_extensions import TypedDict

try:
    from langgraph.graph import StateGraph, END
    LANGGRAPH_AVAILABLE = True
except ImportError:
    LANGGRAPH_AVAILABLE = False
    print("⚠️  LangGraph not installed. Running simulation mode.")
    print("   Install with: pip install langgraph")
    print()

print("=" * 60)
print("FULL LANGGRAPH WORKFLOW WITH REDUCERS")
print("=" * 60)

# 1. Define State with Reducers
class AgentState(TypedDict):
    messages: Annotated[list[str], add]      # Conversation history
    tool_outputs: Annotated[list[str], add]  # Tool results
    iteration: Annotated[int, add]           # Step counter
    status: str                              # Current status (overwrites)

# 2. Define Node Functions
def think_node(state: AgentState) -> dict:
    """Reasoning node - analyzes the situation."""
    iteration = state.get("iteration", 0) + 1
    thought = f"🧠 Thinking... (iteration {iteration})"
    print(f"   [think_node] {thought}")
    return {
        "messages": [thought],
        "iteration": 1,
        "status": "thinking"
    }

def act_node(state: AgentState) -> dict:
    """Action node - executes a tool."""
    action = "🔧 Executed tool: search_database"
    print(f"   [act_node] {action}")
    return {
        "tool_outputs": [action],
        "status": "acting"
    }

def respond_node(state: AgentState) -> dict:
    """Response node - generates final output."""
    iterations = state.get("iteration", 0)
    tools_used = len(state.get("tool_outputs", []))
    response = f"✅ Completed: {iterations} iterations, {tools_used} tools used"
    print(f"   [respond_node] {response}")
    return {
        "messages": [response],
        "status": "complete"
    }

if LANGGRAPH_AVAILABLE:
    # 3. Build the Graph
    print("\n📍 Building LangGraph...")

    graph = StateGraph(AgentState)

    # Add nodes
    graph.add_node("think", think_node)
    graph.add_node("act", act_node)
    graph.add_node("respond", respond_node)

    # Define edges
    graph.set_entry_point("think")
    graph.add_edge("think", "act")
    graph.add_edge("act", "respond")
    graph.add_edge("respond", END)

    # Compile
    agent = graph.compile()
    print("   ✅ Graph compiled successfully!")

    # 4. Run the Agent
    print("\n📍 Running Agent...")
    print("-" * 60)

    initial_state = {
        "messages": ["👤 User: What is the weather?"],
        "tool_outputs": [],
        "iteration": 0,
        "status": "starting"
    }

    result = agent.invoke(initial_state)

    print("-" * 60)
    print("\n📍 Final State:")
    print(f"   messages: {result['messages']}")
    print(f"   tool_outputs: {result['tool_outputs']}")
    print(f"   iteration: {result['iteration']}")
    print(f"   status: {result['status']}")

else:
    # Simulation mode without LangGraph
    print("\n📍 Simulating workflow (LangGraph not installed)...")
    print("-" * 60)

    state = {
        "messages": ["👤 User: What is the weather?"],
        "tool_outputs": [],
        "iteration": 0,
        "status": "starting"
    }

    # Simulate node execution with reducers
    def apply_update(state, update):
        new_state = state.copy()
        for key, value in update.items():
            if key in ["messages", "tool_outputs", "iteration"]:
                # These have add reducer
                new_state[key] = state[key] + value if isinstance(value, list) else state[key] + value
            else:
                # No reducer - overwrite
                new_state[key] = value
        return new_state

    # Run nodes
    update = think_node(state)
    state = apply_update(state, update)

    update = act_node(state)
    state = apply_update(state, update)

    update = respond_node(state)
    state = apply_update(state, update)

    print("-" * 60)
    print("\n📍 Final State:")
    print(f"   messages: {state['messages']}")
    print(f"   tool_outputs: {state['tool_outputs']}")
    print(f"   iteration: {state['iteration']}")
    print(f"   status: {state['status']}")

print("\n" + "=" * 60)
print("KEY OBSERVATIONS:")
print("=" * 60)
print("✅ messages: APPENDED (user msg + thought + response)")
print("✅ tool_outputs: APPENDED (all tool results collected)")
print("✅ iteration: SUMMED (0 + 1 = 1)")
print("✅ status: OVERWROTE (only 'complete' remains)")
print("=" * 60)
```

Enter fullscreen mode

Exit fullscreen mode

**Thanks  
Sreeni Ramadorai**

## Top comments (0)

Subscribe

![pic](https://media2.dev.to/dynamic/image/width=256,height=,fit=scale-down,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F8j7kvp660rqzt99zui8e.png)

Personal
Trusted User
[Create template](/settings/response-templates)

Templates let you quickly answer FAQs or store snippets for re-use.

Submit
Preview
[Dismiss](/404.html)

[Code of Conduct](/code-of-conduct)
•
[Report abuse](/report-abuse)

Are you sure you want to hide this comment? It will become hidden in your post, but will still be visible via the comment's [permalink](#).

Hide child comments as well

Confirm

For further actions, you may consider blocking this person and/or [reporting abuse](/report-abuse)



[![](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F1829954%2F564a03dc-062e-4c58-b28e-be52605aefa8.jpg)

Seenivasa Ramadurai](/sreeni5018)

Follow

AI Solution Architect with 20+ yrs across Azure, AWS, GCP, AI/ML, LLMs, GenAI, Agentic AI, MCP, A2A, NLP, RAG, LangChain, LangGraph, Vector DBs, MS-Foundry, Bedrock AgentCore, Microsvc, REST, gRPC.

* Location

  Dallas. Texas
* Education

  M.Sc Computer Science
* Joined

  Jul 24, 2024

### More from [Seenivasa Ramadurai](/sreeni5018)

[How My Career Evolved Like an AI (LLM Architectures)System

#ai
#architecture
#career
#llm](/sreeni5018/my-journeymy-ai-architecture-125l)
[The Parallel Road: A Girl, A Machine, and the Architecture of Mind

#agents
#ai
#architecture
#machinelearning](/sreeni5018/the-parallel-road-a-girl-a-machine-and-the-architecture-of-mind-3aa0)
[Choosing the Right RAG Strategy A Complete Decision Guide to Chunking, Agentic RAG, and GraphRAG

#ai
#architecture
#llm
#rag](/sreeni5018/choosing-the-right-rag-strategy-a-complete-decision-guide-to-chunking-agentic-rag-and-graphrag-386d)

💎 DEV Diamond Sponsors

Thank you to our Diamond Sponsors for supporting the DEV Community

[![Google AI - Official AI Model and Platform Partner](https://media2.dev.to/dynamic/image/width=880%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fxjlyhbdqehj3akhz166w.png)](https://aistudio.google.com/?utm_source=partner&utm_medium=partner&utm_campaign=FY25-Global-DEVpartnership-sponsorship-AIS&utm_content=-&utm_term=-&bb=146443)

Google AI is the official AI Model and Platform Partner of DEV

[![Neon - Official Database Partner](https://media2.dev.to/dynamic/image/width=880%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fbnl88cil6afxzmgwrgtt.png)](https://neon.tech/?ref=devto&bb=146443)

Neon is the official database partner of DEV

[![Algolia - Official Search Partner](https://media2.dev.to/dynamic/image/width=880%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fv30ephnolfvnlwgwm0yz.png)](https://www.algolia.com/developers/?utm_source=devto&utm_medium=referral&bb=146443)

Algolia is the official search partner of DEV

[DEV Community](/) — A space to discuss and keep up software development and manage your software career

- [Home](/)
- [DEV Challenges](/challenges)
- [DEV++](/++)
- [Videos](/videos)
- [DEV Education Tracks](/deved)
- [DEV Help](/help)
- [Advertise on DEV](/advertise)
- [Organization Accounts](/organizations)
- [DEV Showcase](/showcase)
- [About](/about)
- [Contact](/contact)
- [Free Postgres Database](/free-postgres-database-tier)
- [DEV Shop](https://shop.forem.com/)
- [MLH](https://mlh.io/)

- [Code of Conduct](/code-of-conduct)
- [Privacy Policy](/privacy)
- [Terms of Use](/terms)

Built on [Forem](https://www.forem.com) — the [open source](https://dev.to/t/opensource) software that powers [DEV](https://dev.to) and other inclusive communities.

Made with love and [Ruby on Rails](https://dev.to/t/rails). DEV Community © 2016 - 2026.

![DEV Community](https://media2.dev.to/dynamic/image/width=190,height=,fit=scale-down,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F8j7kvp660rqzt99zui8e.png)

We're a place where coders share, stay up-to-date and grow their careers.

[Log in](https://dev.to/enter?signup_subforem=1)
[Create account](https://dev.to/enter?signup_subforem=1&state=new-user)

![](https://assets.dev.to/assets/sparkle-heart-5f9bee3767e18deb1bb725290cb151c25234768a0e9a2bd39370c382d02920cf.svg)