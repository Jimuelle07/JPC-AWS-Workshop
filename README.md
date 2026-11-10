# Build Your Campus Buddy

**JPC AWS Seminar-Workshop | November 12, 2026**
John Paul College, College of Engineering, Architecture, Technology and Sciences (CEATS)

In about 90 minutes you will build **Campus Buddy**, a Taglish-friendly AI assistant that answers student questions. You start in the browser with no code, then build the same idea as a small Python agent that can use tools. You will use **Amazon Bedrock** for the AI model and the **Strands Agents SDK** to build the agent.

You do not need to know AI or the cloud. If you can run a Python script, you can do this.

## What you will build

| Level | Time | What you do | Code needed |
|---|---|---|---|
| 0. Tour | 10 min | Explore Amazon Bedrock and its playground | None |
| 1. Prompting | 15 min | Give the model a personality with a system prompt | None |
| Setup check | 15 min | Confirm your laptop can talk to Bedrock | Run one script |
| 2. Agent with tools | 25 min | Build an agent that calls your own Python function | About 15 lines |
| 3. Make it yours | 15 min | Customize the prompt, data and tools | Copy and edit |
| Wrap-up | 10 min | Costs, cleanup, what to build next | None |

## Start here

1. **Before the workshop:** follow [docs/00-pre-work.md](docs/00-pre-work.md). It takes about 20 minutes.
2. **At the workshop:** follow the guides in order.
   - [docs/01-tour-and-prompting.md](docs/01-tour-and-prompting.md) (Levels 0 and 1)
   - [docs/02-first-agent.md](docs/02-first-agent.md) (setup check and Level 2)
   - [docs/03-make-it-yours.md](docs/03-make-it-yours.md) (Level 3 and wrap-up)

Facilitators and volunteers: see [docs/facilitator-notes.md](docs/facilitator-notes.md).

## What is in this repo

| File | What it is |
|---|---|
| `check_setup.py` | Checks Python, credentials and one real call to Bedrock |
| `config.py` | Region and model ID, changeable with environment variables |
| `campus_prompt.py` | The Campus Buddy system prompt |
| `campus_data.py` | Sample requirements, schedules and canteen prices |
| `step1_hello_agent.py` | Your first agent, no tools |
| `step2_agent_with_tool.py` | The same agent with one custom tool |
| `step3_campus_buddy.py` | A chat loop with three tools and a spot for yours |
| `requirements.txt` | Python packages to install |

## Important notes

- The data in `campus_data.py` is **sample data**, not official JPC information.
- Never put your API key in a file or share it. Set it only as an environment variable. It is deleted or expires after the workshop.
- Amazon Bedrock charges for usage. A workshop like this costs very little per student, but delete your API key when you are done.

## Links

- Workshop guide (AWS Workshop Studio): https://catalog.us-east-1.prod.workshops.aws/workshops/083b80d7-5a90-402b-9bb4-19fb53092808/en-US/setup
- Strands Agents Python quickstart: https://strandsagents.com/docs/user-guide/quickstart/python/
- Amazon Bedrock API keys: https://aws.amazon.com/blogs/machine-learning/accelerate-ai-development-with-amazon-bedrock-api-keys/
