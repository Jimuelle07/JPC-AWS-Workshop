# Facilitator and volunteer notes

Event: Thursday, November 12, 2026. Workshop block: **60 minutes**, 10:20 AM to 11:20 AM.

With about 70 people, one shared Wi-Fi and one hour, setup is the biggest risk. The plan below assumes most students finished the pre-work (Python and packages installed). We do not install Python during the session.

## Workshop run of show

| Time | Min | Block | Lead | Notes |
|---|---|---|---|---|
| 10:20 - 10:25 | 5 | Kickoff | Facilitator | What we build today. Agent = model + instructions + tools. Announce the Region and model ID. Hands up: who finished the pre-work? |
| 10:25 - 10:37 | 12 | Levels 0 and 1: Playground and system prompt | Facilitator demos, students follow | Quick tour (2 min), then paste the Campus Buddy system prompt and compare answers. No model comparison |
| 10:37 - 10:47 | 10 | API key and setup check | Volunteers help | Students create a short-term key (they are already in the Bedrock console), set it, run `step0_check_setup.py`. Hands up for Setup OK |
| 10:47 - 11:02 | 15 | Level 2: First agent and a tool | Facilitator | Run step 1 (it guesses), then step 2 (it looks it up). Pause on the `@tool` docstring. One "try it": ask about tuition |
| 11:02 - 11:15 | 13 | Level 3: Make it yours | Everyone | Run step 3, ask 2-3 questions, then Challenge A (prompt) or B (data). Challenge C is for fast finishers |
| 11:15 - 11:20 | 5 | Wrap-up | Facilitator | Cleanup (keys), one line on costs, what to build next, point to the take-home extras |

**Hard stop at 11:20.** Keep the end time even if the room is behind, so the rest of the program starts on time.

## If you fall behind (cut in this order)

1. **Setup check runs long:** at 10:50 at the latest, start Level 2 on the projector anyway. Volunteers keep helping students who are stuck; they catch up by watching, then run the scripts.
2. **Level 3 shrinks first:** if Level 2 ends after 11:05, run `step3_campus_buddy.py` yourself on the projector, ask the audience for 2-3 questions, and assign Challenge A or B as take-home.
3. **Never cut:** the step 1 vs step 2 comparison (the core lesson of the hour) and the cleanup reminder about API keys.

Decision point at 10:47: if a student still has no Setup OK and the fix is not quick (no Python, broken install, no AWS access), move them to the browser-only track below instead of debugging during Level 2.

## What was cut from the 90-minute version

| Cut | Where it went |
|---|---|
| Separate 10-minute Bedrock tour | Folded into the playground block as a 2-minute demo |
| Comparing two models side by side | Take-home extra in `01-tour-and-prompting.md` |
| Iterating on the system prompt (Step 4) | Take-home extra in `01-tour-and-prompting.md` |
| Installing Python or packages during the session | Pre-work only. Students who could not do it use the browser-only track |
| Extra tries in Level 2 (BSCS, unknown course BSN) | Take-home extras in `02-first-agent.md`. One try kept (tuition) |
| Challenge C, adding your own tool | Stretch for fast finishers, and take-home |
| MCP server demo | Cut. Students can follow it in the AWS workshop guide linked in the README |
| Longer talk on costs | One line in the wrap-up |

## Volunteers

- Before 10:20, give each volunteer a section of rows so every student knows whom to call.
- During the setup check, volunteers carry the troubleshooting table below. Most problems are the API key set in a different terminal window, or the wrong Region or model ID.
- Spend at most 3 minutes on one student's problem. If it is not fixed by then, pair the student with a neighbor or move them to the browser-only track.

## Before the event (day before)

- [ ] Decide account access: event-provided accounts (AWS Workshop Studio) or students' own accounts. This changes everything about setup.
- [ ] Confirm the **Region** and the exact **model ID** for the Amazon Nova model. Update the defaults in `campus_buddy/config.py`, or announce the values to set as `AWS_REGION` and `MODEL_ID`.
- [ ] Run the whole hour yourself once on a fresh account and laptop, with a timer, including `step0_check_setup.py`.
- [ ] Confirm Bedrock quotas can handle about 60 people calling at once. If unsure, ask your AWS contact or Cloud Club for guidance.
- [ ] Send the pre-work reminder to students (message template below). Stress that it is required.
- [ ] Test venue Wi-Fi capacity for about 70 devices. Bring a mobile hotspot for the technical volunteer.
- [ ] Download the Python installer and a ZIP of this repo onto a few USB drives as an offline fallback for the registration table (8:30 to 9:00), not for the workshop hour.
- [ ] Replace the sample data in `campus_buddy/data.py` with real JPC information, or keep it clearly labeled as sample.

## Pre-work message for students

```
Hi CEATS students! The hands-on part of the AWS Seminar-Workshop on Nov 12 is only one hour,
so please set up BEFORE the event. There is no time to install Python during the session.
Bring a charged laptop and charger, then follow this guide (about 20 minutes):
https://github.com/Jimuelle07/JPC-AWS-Workshop/blob/main/docs/00-pre-work.md
Finish at least Steps 1 to 4 (Python 3.10+, the project, and the packages installed).
Stuck? Message Jimuelle Patron, or come early (8:30 AM) and we will help you at registration.
```

## Common problems and quick fixes

| Problem | Fix |
|---|---|
| Student has no Python or an old version | Not fixable in the hour. Browser-only track. (At registration: offline installer on USB, tick "Add Python to PATH") |
| `pip install` is slow or fails | Wi-Fi congestion. Use a hotspot if it is quick, otherwise browser-only track or pair with a neighbor |
| PowerShell blocks the venv activate script | `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`, then activate again |
| "No AWS credentials found" | They set the variable in a different terminal window. Set it again in the current one |
| `ValidationException` or model not found | Wrong Region or model ID. Set `AWS_REGION` and `MODEL_ID` to the announced values |
| `AccessDeniedException` | Key lacks access to that model or Region. Check the account and model choice |
| `ThrottlingException` | Everyone is calling at once. Ask students to wait a few seconds and retry, and stagger runs |
| Agent does not call the tool | The docstring is unclear. Rewrite it to state exactly when to use the tool |
| Student cannot get set up at all | Pair them with a neighbor, or use the browser-only track below |

## Browser-only track (fallback)

For students who cannot run Python (or for the whole room if Wi-Fi fails): stay in the Bedrock chat playground. Do Levels 0 and 1 as written, then upload a short document (for example, a student handbook page) in the chat playground and ask Campus Buddy questions about it. During Level 2 they watch the projector or pair with a neighbor. Everyone still sees the main idea: giving the model real data stops it from guessing.

## After the event

- Delete or expire all API keys and event accounts.
- Delete volunteer form responses within 30 days after the event (per the privacy notice).
- Send thank-yous to the speakers and volunteers.
