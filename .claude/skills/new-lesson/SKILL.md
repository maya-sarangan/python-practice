---
name: new-lesson
description: Add a new world of practice quests after the student finishes a freeCodeCamp Python section. Use when the teacher names a completed lesson or section (e.g. "/new-lesson Dictionaries and Sets", "the kid finished error handling, add exercises", "generate quests for classes and objects") or pastes a freeCodeCamp curriculum link. Pulls the real concept list from the freeCodeCamp source, updates CURRICULUM.md, then writes quests, checks and solutions and verifies them.
---

# Add a new lesson's quests

Turn a finished freeCodeCamp section into a new world of auto-graded quests.

Read `CLAUDE.md` first — it holds the quality rules, the voice guide and the
scope contract. This skill is the procedure; `CLAUDE.md` is the standard.
Read `reference/authoring.md` for the exact file templates.

Argument: the lesson name as the teacher says it ("Dictionaries and Sets",
"Error Handling"). A pasted freeCodeCamp URL is a bonus, not a requirement —
the concept list comes from the curriculum source either way.

## Step 1 — Find the real concept list

Never guess what a section taught, and never rely on fetching the
`freecodecamp.org/learn/...` page (it is JavaScript-rendered and returns
nothing useful).

```bash
python3 tools/fcc_lesson.py modules
```

Find the module matching the lesson name and note its `review-*` block. Then:

```bash
python3 tools/fcc_lesson.py concepts review-<slug>   # compact inventory
python3 tools/fcc_lesson.py review   review-<slug>   # full detail with examples
```

Read the full review. It is the definitive list of what the student may now be
asked about, including the exact method names and error types the course showed.

If the tool cannot reach the network, stop and tell the teacher. Do not invent
a concept list — a wrong scope is worse than no quests.

## Step 2 — Decide the shape, then confirm it

Work out and state plainly:

- the new world number, name, badge emoji and one-line `teaches` string
- the quest number range, starting from the "Next free quest number" line in
  `CURRICULUM.md`
- how many quests (10–15 for a substantial section; match the concept count)
- a one-line title per quest, each naming the concept it drills

Show the teacher this list before writing files. It is cheap to redirect a list
and expensive to redirect 15 finished quests. If they asked for a specific
count, use it.

## Step 3 — Update the scope contract first

In `CURRICULUM.md`:

1. Add the lesson under "Completed lessons" with its concept inventory and the
   quest range.
2. Remove the now-taught items from "Not taught yet".
3. Add the world to the allocation table.
4. Update the "Next free quest number" and "Next free world number" line.

Doing this before writing quests is what keeps scope honest.

## Step 4 — Write the quests

In this order, following `reference/authoring.md`:

1. `checks/worldN.py` — specs, cases and hints.
2. `checks/stories.py` — one story hook per new quest id.
3. `checks/registry.py` — append the world to `WORLDS` and to `_build()`.
4. `solutions/qNN_slug.py` — one worked answer per quest.

Earlier quests in a world teach one idea each; later quests combine two or
three. End the world with one quest that uses most of it. Mark roughly one in
six `"playable": True` and give it a `demo()` that calls the student's function.

## Step 5 — Generate and verify

```bash
python3 tools/make_stubs.py              # safe: only creates missing stubs
python3 practice.py check
```

`check` must print `✅ answer key verified: N/N` and
`✅ all N quest stubs present`.

When it fails, read the diff it prints and decide whether the **check** or the
**solution** is wrong. Fixing a check to match a buggy solution silently ships
a broken quest. Expected-value typos in checks are the most common cause.

Then sanity-check the student's view on two or three quests:

```bash
python3 practice.py <first new id>          # should say "Not started yet"
python3 practice.py <first new id> --hint
python3 practice.py <a playable id> --solution
```

## Step 6 — Report

Tell the teacher:

- the new world, its quests and the total bank size
- the concepts now drilled, and anything from the section you deliberately left
  out and why (for example: a concept the course only mentioned in passing)
- `python3 practice.py check` result
- the command to show the student: `python3 practice.py next`

## Guardrails

- A quest may only use concepts marked covered in `CURRICULUM.md`. Check the
  "Not taught yet" list before using anything clever.
- Never run `python3 tools/make_stubs.py --force` without quest numbers; it
  overwrites the student's own answers.
- Never renumber or delete existing quests.
- Never add a dependency or a test framework.
