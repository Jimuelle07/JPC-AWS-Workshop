"""Level 2, part A: your first agent (no tools yet).

    python step1_hello_agent.py

An agent is a model plus instructions. Here we give the model the Campus Buddy
system prompt and ask a question it cannot truly answer.

Watch what happens: with no tool and no data, it may sound confident but it is
guessing. That is exactly the problem tools solve in the next step.
"""

from strands import Agent
from strands.models import BedrockModel

from campus_buddy.prompt import SYSTEM_PROMPT
from campus_buddy.config import MODEL_ID, REGION

model = BedrockModel(model_id=MODEL_ID, region_name=REGION, temperature=0.3)

agent = Agent(model=model, system_prompt=SYSTEM_PROMPT)

agent("Ano ang mga requirements para mag-enroll bilang first-year BSIT student?")
