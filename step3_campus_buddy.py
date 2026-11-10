"""Level 3: make Campus Buddy your own.

    python step3_campus_buddy.py

This is a small chat loop. The agent remembers the conversation, so you can ask
follow-up questions. Type "exit" to stop.

It already has three tools (see campus_buddy/tools.py):
get_requirements, get_schedule and get_canteen_price.

Your tasks (pick any, in any order):
  1. Change the system prompt in campus_buddy/prompt.py (new tone, new rules).
  2. Edit the sample data in campus_buddy/data.py with details you care about.
  3. Add a NEW tool of your own in the section below, then add it to the
     tools list at the bottom.

Ideas for a new tool: library hours, clinic schedule, org events, a simple
budget helper, a "what to eat today" picker.
"""

from strands import Agent, tool
from strands.models import BedrockModel

from campus_buddy.config import MODEL_ID, REGION
from campus_buddy.prompt import SYSTEM_PROMPT
from campus_buddy.tools import ALL_TOOLS


# ---- YOUR TOOL HERE -------------------------------------------------------
# Remove the # signs, rename the function, write a clear docstring, and
# return some text. Then add my_new_tool to the tools list below.
#
# @tool
# def my_new_tool(something: str) -> str:
#     """Say clearly what this tool does and when to use it.
#
#     Args:
#         something: Explain what the agent should pass in.
#     """
#     return "Your answer here"
# ---------------------------------------------------------------------------


model = BedrockModel(model_id=MODEL_ID, region_name=REGION, temperature=0.3)

agent = Agent(
    model=model,
    system_prompt=SYSTEM_PROMPT,
    tools=ALL_TOOLS + [],  # add your tool inside the [ ], for example [my_new_tool]
)

print("Campus Buddy is ready. Type your question, or 'exit' to stop.\n")
while True:
    question = input("\nYou: ").strip()
    if question.lower() in ("exit", "quit", ""):
        break
    print("\nCampus Buddy: ", end="")
    agent(question)

print("\nSalamat! See you at the next build.")
