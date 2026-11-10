"""Level 3: make Campus Buddy your own.

    python step3_campus_buddy.py

This is a small chat loop. The agent remembers the conversation, so you can ask
follow-up questions. Type "exit" to stop.

Your tasks (pick any, in any order):
  1. Change the system prompt in campus_prompt.py (new tone, new rules).
  2. Edit the sample data in campus_data.py with details you care about.
  3. Add a NEW tool of your own. Copy one of the tools below, change the
     function name, docstring and what it returns, then add it to the
     tools=[...] list at the bottom.

Ideas for a new tool: library hours, clinic schedule, org events, a simple
budget helper, a "what to eat today" picker.
"""

from strands import Agent, tool
from strands.models import BedrockModel

from campus_data import lookup_canteen_price, lookup_requirements, lookup_schedule
from campus_prompt import SYSTEM_PROMPT
from config import MODEL_ID, REGION


@tool
def get_requirements(course: str) -> str:
    """Get the enrollment requirements for a course.

    Args:
        course: The course code, for example BSIT, BSCS or BSCpE.
    """
    return lookup_requirements(course)


@tool
def get_schedule(course: str) -> str:
    """Get the class schedule for a course.

    Args:
        course: The course code, for example BSIT, BSCS or BSCpE.
    """
    return lookup_schedule(course)


@tool
def get_canteen_price(item: str) -> str:
    """Get the price of an item sold in the school canteen.

    Args:
        item: The name of the food or drink, for example "pancit canton".
    """
    return lookup_canteen_price(item)


# ---- YOUR TOOL HERE -------------------------------------------------------
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
    tools=[get_requirements, get_schedule, get_canteen_price],  # add your tool here
)

print("Campus Buddy is ready. Type your question, or 'exit' to stop.\n")
while True:
    question = input("\nYou: ").strip()
    if question.lower() in ("exit", "quit", ""):
        break
    print("\nCampus Buddy: ", end="")
    agent(question)

print("\nSalamat! See you at the next build.")
