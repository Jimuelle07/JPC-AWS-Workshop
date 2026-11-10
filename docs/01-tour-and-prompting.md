# Levels 0 and 1: Tour and prompting (25 minutes, no code)

Goal: see what an AI model can do in the browser, then learn the most important skill in AI building: telling the model who it is and how to behave.

## Level 0: Tour of Amazon Bedrock (10 minutes)

**What is Amazon Bedrock?** A service on AWS that gives you access to many AI models through one place, without managing any servers. You pick a model, send it text, and get an answer back.

Steps:

1. Sign in to the AWS console and open **Amazon Bedrock**.
2. Check the **Region** in the top-right corner. Use the one the facilitator announced.
3. Open the **Playground** and choose **Chat**.
4. Click **Select model**. Browse the providers and pick an **Amazon Nova** model (the facilitator will confirm which one).
5. Ask it a few questions and notice the speed, tone and detail:
   - `Explain cloud computing to a first-year student in three sentences.`
   - `Give me three project ideas for a BSIT capstone.`
   - `Sagutin mo sa Tagalog: ano ang AI?`

Quick discussion: what did it do well? Where did it sound unsure or wrong?

Note: some models, such as Anthropic's, ask you to submit a one-time usage form the first time you use them. Amazon Nova models do not, so we use them today.

## Level 1: Give the model a personality (15 minutes)

A **system prompt** is a set of instructions the model follows for the whole conversation. It sets the role, tone and rules.

### Step 1: See the model without instructions

In the chat playground, ask:

```
Ano ang mga requirements para mag-enroll bilang first-year BSIT student?
```

Notice that it gives a general answer. It does not know anything about our campus.

### Step 2: Add a system prompt

Find the **System prompt** box (it may be under **Configurations**). Paste this:

```
You are Campus Buddy, a friendly assistant for college students at John Paul College (CEATS).

Style:
- Reply in simple Taglish (a natural mix of Tagalog and English).
- Keep answers short: three to five sentences, or a short list.
- Be warm and encouraging, like a helpful upperclassman.

Rules:
- If you do not know something, say so honestly and suggest asking the registrar or the department office.
- Never make up requirements, schedules, prices, or deadlines.
```

Now ask the same question again, plus these:

- `Pwede ba akong mag-enroll kahit late na ng isang linggo?`
- `Magkano ang pancit canton sa canteen?`
- `Pwede mo ba akong tulungan sa assignment ko sa Python?`

What changed? Did it follow the Taglish and short-answer rules? Did it admit when it did not know the canteen price?

### Step 3: Compare two models

Open a second chat panel (use **Compare mode** if available) and select a different model. Send the same question to both. Which answer do you prefer, and why? Models differ in speed, cost and style, and choosing between them is a real skill.

### Step 4: Improve your prompt

Edit the system prompt and test one change at a time. Try:

- Change the personality (a strict professor, a funny kuya, a calm guidance counselor).
- Add a rule, such as `End every answer with one tip for studying.`
- Ask for a format, such as `Always answer in exactly three bullet points.`

Save your favorite version of the prompt. We will reuse it in code.

### What you learned

- A system prompt shapes behavior without writing any code.
- The model does not know our campus. It can only guess unless we give it real data.

That second point leads straight into Level 2.

Next: [docs/02-first-agent.md](02-first-agent.md)
