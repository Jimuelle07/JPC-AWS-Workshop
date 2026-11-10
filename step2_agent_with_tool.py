"""Level 2, part B: give the agent a custom tool.

    python step2_agent_with_tool.py

A tool is just a Python function with the @tool decorator. The agent reads the
function name and its docstring to decide WHEN to call it. Write a clear
docstring and the model will use the tool well.

Run it and watch the output: you should see the agent decide to call
get_requirements, then answer using the data it got back.
"""

from strands import Agent, tool
from strands.models import BedrockModel

from campus_buddy.data import lookup_requirements
from campus_buddy.prompt import SYSTEM_PROMPT
from campus_buddy.config import MODEL_ID, REGION


@tool
def get_requirements(course: str) -> str:
    """Get the enrollment requirements for a course.

    Args:
        course: The course code, for example BSIT, BSCS or BSCpE.
    """
    return lookup_requirements(course)


model = BedrockModel(model_id=MODEL_ID, region_name=REGION, temperature=0.3)

agent = Agent(model=model, system_prompt=SYSTEM_PROMPT, tools=[get_requirements])

agent("Ano ang mga requirements para mag-enroll bilang first-year BSIT student?")
