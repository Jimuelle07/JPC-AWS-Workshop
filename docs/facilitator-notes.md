# Facilitator and volunteer notes

Event: Thursday, November 12, 2026. Workshop block: 10:20 AM to 11:50 AM (90 minutes).

## Workshop run of show

| Time | Block | Lead | Notes |
|---|---|---|---|
| 10:20 - 10:30 | Level 0: Bedrock tour | Facilitator | Live demo on the projector, students follow along |
| 10:30 - 10:45 | Level 1: Prompting | Facilitator | Play with the system prompt, compare two models |
| 10:45 - 11:00 | Setup check | Volunteers help | Everyone runs `check_setup.py`. Hands up for Setup OK |
| 11:00 - 11:25 | Level 2: Agent and tools | Facilitator | Step 1 guess, step 2 tool. Pause to explain the docstring |
| 11:25 - 11:40 | Level 3: Make it yours | Everyone | Challenge A, B or C. Optional 5-minute MCP demo |
| 11:40 - 11:50 | Wrap-up | Facilitator | Cleanup, costs, next steps |

Tip: if setup runs slow, the setup check absorbs the delay. Level 3 is the safest block to shorten. Keep the 11:50 end so the Q&A starts on time.

## Before the event (day before)

- [ ] Decide account access: event-provided accounts (AWS Workshop Studio) or students' own accounts. This changes everything about setup.
- [ ] Confirm the **Region** and the exact **model ID** for the Amazon Nova model. Update the defaults in `config.py`, or announce the values to set as `AWS_REGION` and `MODEL_ID`.
- [ ] Run Levels 1 and 2 yourself on a fresh account and laptop, including `check_setup.py`.
- [ ] Confirm Bedrock quotas can handle about 60 people calling at once. If unsure, ask your AWS contact or Cloud Club for guidance.
- [ ] Send the pre-work to students (message template below).
- [ ] Test venue Wi-Fi capacity for about 70 devices. Bring a mobile hotspot for the technical volunteer.
- [ ] Download the Python installer and a ZIP of this repo onto a few USB drives as an offline fallback.
- [ ] Replace the sample data in `campus_data.py` with real JPC information, or keep it clearly labeled as sample.

## Pre-work message for students

```
Hi CEATS students! Please prepare before the AWS Seminar-Workshop on Nov 12.
Bring a charged laptop and charger, then follow this guide (about 20 minutes):
https://github.com/Jimuelle07/JPC-AWS-Workshop/blob/main/docs/00-pre-work.md
You need Python 3.10 or newer and the project installed.
Stuck? Message Jimuelle Patron, or come early and we will help you at registration.
```

## Common problems and quick fixes

| Problem | Fix |
|---|---|
| Student has no Python or an old version | Install from python.org, tick "Add Python to PATH". Offline installer on USB |
| `pip install` is slow or fails | Wi-Fi congestion. Use a hotspot, or install from a USB wheel cache if prepared |
| PowerShell blocks the venv activate script | `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`, then activate again |
| "No AWS credentials found" | They set the variable in a different terminal window. Set it again in the current one |
| `ValidationException` or model not found | Wrong Region or model ID. Set `AWS_REGION` and `MODEL_ID` to the announced values |
| `AccessDeniedException` | Key lacks access to that model or Region. Check the account and model choice |
| `ThrottlingException` | Everyone is calling at once. Ask students to wait a few seconds and retry, and stagger runs |
| Agent does not call the tool | The docstring is unclear. Rewrite it to state exactly when to use the tool |
| Student cannot get set up at all | Pair them with a neighbor, or use the no-code fallback below |

## No-code fallback

If Wi-Fi or Python setup fails for a student (or for the whole room), run the session in the Bedrock playground only: Level 0 and Level 1 as written, then let students upload a document (for example, a student handbook) in the chat playground and ask questions about it. Everyone still builds and learns.

## MCP demo (optional, facilitator only)

A 5-minute live demo of connecting an MCP server to a Strands agent, following the "MCP servers" part of the AWS workshop guide linked in the README. Practice it beforehand. Skip it if the room is behind schedule.

## After the event

- Delete or expire all API keys and event accounts.
- Delete volunteer form responses within 30 days after the event (per the privacy notice).
- Send thank-yous to the speakers and volunteers.
