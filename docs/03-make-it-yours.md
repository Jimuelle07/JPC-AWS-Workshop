# Level 3 and wrap-up: Make it yours (25 minutes)

Goal: turn the demo into your own assistant. Work alone or in pairs.

## Level 3: Customize Campus Buddy (15 minutes)

Run the full chat version:

```bash
python step3_campus_buddy.py
```

This one has three ready-made tools (`get_requirements`, `get_schedule`, `get_canteen_price`, defined in `campus_buddy/tools.py`) and remembers the conversation, so follow-up questions work. Try:

- `Ano ang schedule ng BSCS?`
- `Magkano ang sinigang?`
- `Ano ang schedule ko?` (it should ask which course you mean)

Type `exit` to stop.

### Pick your challenge

Choose at least one:

**Challenge A: Change the personality.**
Edit `campus_buddy/prompt.py`. Try a different tone or a new rule. Run it again and see the difference.

**Challenge B: Change the data.**
Edit `campus_buddy/data.py`. Add a new canteen item, change a schedule, or add a course.

**Challenge C: Add your own tool.** (the main challenge)
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

### Optional demo: MCP servers (facilitator only)

The facilitator may show a 5-minute live demo of an MCP server. MCP is a standard way to plug ready-made tools into an agent so you do not write each one yourself. You do not need to do anything for this part, just watch. The full hands-on version is in the AWS workshop guide linked in the README.

## Wrap-up (10 minutes)

### Cleanup (do this today)

- Close your terminal. Your short-term API key expires on its own.
- If you created a long-term key or used your own AWS account, delete the API key in the Bedrock console and sign out.
- Never commit an API key to GitHub. If you ever do, delete the key right away and create a new one.

### Costs, in plain words

Amazon Bedrock charges based on how much text you send and receive. What we did today is tiny, but real projects can add up. Habits worth building: use short-lived keys, delete what you do not need, and set a budget alert in your AWS account.

### What to build next

- Give Campus Buddy real data from a file or a database.
- Put a simple web page or a Messenger bot in front of it.
- Enter a hackathon with an agent that solves a local problem, such as typhoon advisories, commute help or budget planning.
- Join the AWS Cloud Club community to learn with other student builders.

### Share what you built

Show a classmate your tool or your favorite prompt. Teaching it is the fastest way to learn it.

Salamat sa pagsali!
