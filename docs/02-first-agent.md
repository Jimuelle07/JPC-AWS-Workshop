# Setup check and Level 2: Your first agent (40 minutes)

Goal: confirm your laptop can talk to Bedrock, then build an agent that uses a tool you write yourself.

## Setup check (15 minutes)

If you finished the pre-work, this is a quick confirmation. If not, a volunteer will help you catch up.

1. Open a terminal in the project folder and activate your virtual environment (the prompt should start with `(.venv)`).
2. Make sure your two environment variables are set in this terminal: `AWS_BEARER_TOKEN_BEDROCK` and `AWS_REGION`. See Step 5 of the [pre-work](00-pre-work.md).
3. Run:

```bash
python step0_check_setup.py
```

4. You should see a greeting from the model and **Setup OK**.

Raise your hand when you see "Setup OK". If you see an error, read the hint it prints, check the troubleshooting table in the pre-work, or call a volunteer.

If the model ID does not work in your Region, open the Bedrock console, find the exact model ID (or inference profile ID) for the Nova model you used in the playground, and set it:

Windows (PowerShell):

```powershell
$env:MODEL_ID = "paste-the-model-id-here"
```

macOS or Linux:

```bash
export MODEL_ID="paste-the-model-id-here"
```

## Level 2, part A: An agent with no tools (10 minutes)

Run the first agent:

```bash
python step1_hello_agent.py
```

Now open `step1_hello_agent.py` and read it. It is short. There are three ideas:

1. **A model:** `BedrockModel(...)` says which model on Amazon Bedrock to use.
2. **Instructions:** the `system_prompt` is the Campus Buddy prompt from Level 1 (see `campus_buddy/prompt.py`).
3. **An agent:** `Agent(model=..., system_prompt=...)` ties them together. Calling `agent("...")` sends a question and prints the answer.

**Look closely at the answer.** It asked for BSIT enrollment requirements. Did the agent give a confident list? Remember: it has no data about our campus, so that list is a guess. Sounding sure is not the same as being right.

## Level 2, part B: Add a tool (15 minutes)

A **tool** lets the agent call your code to get real information. The agent decides when to use it.

Run the version with a tool:

```bash
python step2_agent_with_tool.py
```

Watch the output. You should see the agent decide to call `get_requirements`, receive the data, and then write its answer based on that data. Same question, much better answer.

Now open `step2_agent_with_tool.py`. The key part is this:

```python
@tool
def get_requirements(course: str) -> str:
    """Get the enrollment requirements for a course.

    Args:
        course: The course code, for example BSIT, BSCS or BSCpE.
    """
    return lookup_requirements(course)
```

Three things to notice:

- `@tool` turns a normal Python function into something the agent can call.
- The **docstring** (the text in triple quotes) is how the agent learns what the tool does and when to use it. Clear docstring, better tool use.
- The function **returns text**. The agent reads that text and uses it in its answer.

The real data lives in `campus_buddy/data.py`. Open it and look at the `REQUIREMENTS` dictionary. This is sample data, so you can change it.

### Try it yourself

1. In `step2_agent_with_tool.py`, change the question at the bottom to ask about `BSCS`, then run it again.
2. Ask about a course that does not exist, such as `BSN`. What does the agent say? (Check how `lookup_requirements` handles unknown courses.)
3. Ask something the tool cannot answer, such as `Magkano ang tuition?` Does the agent admit it does not know, or does it invent something? Your system prompt rules matter here.

### What you learned

- An agent is a model plus instructions plus tools.
- Tools connect the model to real data, so it stops guessing.
- The docstring is the tool's instruction manual for the model.

Next: [docs/03-make-it-yours.md](03-make-it-yours.md)
