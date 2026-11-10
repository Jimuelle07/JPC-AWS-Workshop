"""Agent tools for Campus Buddy.

Each tool is a normal Python function with the @tool decorator. The agent
reads the function name and docstring to decide when to call it, so keep
docstrings clear and specific.

You first build a tool by hand in step2_agent_with_tool.py. Step 3 imports
these ready-made versions so you can focus on adding your own.
"""

from strands import tool

from campus_buddy.data import lookup_canteen_price, lookup_requirements, lookup_schedule


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


ALL_TOOLS = [get_requirements, get_schedule, get_canteen_price]
