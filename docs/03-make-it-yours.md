# Level 3 and wrap-up: Make it yours (18 minutes)

Goal: turn the demo into your own assistant. Work alone or in pairs.

## Level 3: Customize Campus Buddy (13 minutes)

Run the full chat version:

```bash
python step3_campus_buddy.py
```

This one has three ready-made tools (`get_requirements`, `get_schedule`, `get_canteen_price`, defined in `campus_buddy/tools.py`) and remembers the conversation, so follow-up questions work. Try two or three of these:

- `Ano ang schedule ng BSCS?`
- `Magkano ang sinigang?`
- `Ano ang schedule ko?` (it should ask which course you mean)

Type `exit` to stop.

### Pick one challenge

Each one takes about 5 minutes. After your edit, run `python step3_campus_buddy.py` again and see the difference.

**Challenge A: Change the personality.**
Edit `SYSTEM_PROMPT` in `campus_buddy/prompt.py`. Try a different tone (a funny kuya, a strict professor) or add a new rule, such as `End every answer with one tip for studying.`

**Challenge B: Change the data.**
Edit `campus_buddy/data.py`. Add a new item to `CANTEEN` (for example `"lumpia": 25`), change a schedule, or add a course. Then ask Campus Buddy about it.

### Stretch: add your own tool (if you finish early, or at home)

1. Open `step3_campus_buddy.py` and find the section marked `YOUR TOOL HERE`.
2. Remove the `#` signs to turn the example into real code.
3. Rename the function and write a clear docstring that says what it does and when to use it.
4. Make it return some text. It can be hardcoded.
5. Add its name inside the empty `[ ]` at the bottom, for example `tools=ALL_TOOLS + [my_new_tool]`.
6. Run the script and ask a question that should trigger your tool.

Tool ideas:

- `get_library_hours()` returns when the library is open.
- `get_org_events()` returns upcoming student org events.
- `get_study_tip(subject)` returns a tip for a subject.
- `get_budget_advice(amount)` suggests how to spend a daily allowance at the canteen.

If your tool is not being used, the usual fix is a clearer docstring. Describe exactly when the agent should call it.

## Wrap-up (5 minutes)

### Cleanup (do this today)

- Close your terminal. Your short-term API key expires on its own.
- If you created a long-term key or used your own AWS account, delete the API key in the Bedrock console and sign out.
- Never commit an API key to GitHub. If you ever do, delete the key right away and create a new one.

**About costs:** Amazon Bedrock charges for the text you send and receive. Today's usage is tiny, but real projects add up, so use short-lived keys and set a budget alert in your own AWS account.

### What to build next

- Finish the take-home extras at the bottom of [01](01-tour-and-prompting.md) and [02](02-first-agent.md), and the stretch challenge above.
- Give Campus Buddy real data from a file or a database.
- Put a simple web page or a Messenger bot in front of it.
- Learn MCP, a standard way to plug ready-made tools into an agent. The "MCP servers" part of the AWS workshop guide (linked in the [README](../README.md)) walks you through it.
- Enter a hackathon with an agent that solves a local problem, such as typhoon advisories, commute help or budget planning.
- Join the AWS Learning Club community to learn with other student builders.

Salamat sa pagsali!
