# Working in this repository

This is a Python exercise bank for **one 11-year-old student** following the
freeCodeCamp Python (v9) course. Everything here optimises for one thing:
the student wants to type the next line of code.

Python 3.9+, standard library only. No third-party packages, ever — the
student should never have to install anything to practise.

## The one hard rule

```bash
python3 practice.py check
```

must print `✅ answer key verified: N/N`. This runs every worked solution in
`solutions/` against every check in `checks/`. **Never finish a task with this
red.** If a check and a solution disagree, work out which one is wrong — do not
just bend the solution to match the check.

## Layout

| Path | Role |
|---|---|
| `practice.py` | The Quest Console. Grader, hint system, progress map, demo runner. |
| `checks/registry.py` | `WORLDS`, the `Approx` helper, and assembly of all worlds. |
| `checks/worldN.py` | Quest specs: titles, test cases, hints. The answer key. |
| `checks/stories.py` | One story hook per quest. The flavour. |
| `quests/qNN_slug.py` | Student-facing stub. **Generated** — see below. |
| `solutions/qNN_slug.py` | Worked answer, same filename and function name. |
| `tools/make_stubs.py` | Generates `quests/` from `checks/` + `solutions/`. |
| `tools/fcc_lesson.py` | Pulls the real concept list from freeCodeCamp source. |
| `CURRICULUM.md` | What has been taught. The scope contract. |

### Quest files are generated, not hand-written

`quests/qNN_*.py` is produced by `tools/make_stubs.py` from the registry, the
stories and the solution's signature. This guarantees the examples printed in
a quest can never disagree with the examples the grader checks.

```bash
python3 tools/make_stubs.py          # create missing stubs only (safe)
python3 tools/make_stubs.py --force  # rewrite all stubs — ERASES student work
python3 tools/make_stubs.py 78 79    # just these
```

Default to the safe form. Only use `--force` on quests you just created, by
number. Never run a bare `--force` once the student has started working.

## Adding a lesson

Use the `/new-lesson` skill. It encodes this sequence:

1. Find the module's review block: `python3 tools/fcc_lesson.py modules`
2. Read the real concept inventory:
   `python3 tools/fcc_lesson.py concepts review-<slug>`
3. Append the lesson and its concepts to `CURRICULUM.md`, move concepts off the
   "not taught yet" list, and update the allocation table and the
   "Next free quest number" line.
4. Write `checks/worldN.py`, add stories to `checks/stories.py`, add the world
   to `WORLDS` in `checks/registry.py`, add it to `_build()`.
5. Write every `solutions/qNN_*.py`.
6. `python3 tools/make_stubs.py` then `python3 practice.py check`.

## Quest quality rules

These are the rules the existing 77 follow. Hold new quests to the same bar.

**Scope.** A quest may only use concepts marked covered in `CURRICULUM.md`.
This is the rule that matters most. A quest needing an untaught tool does not
stretch the student, it blocks them. Dictionaries, sets, `try`/`except`,
classes, file I/O and recursion are all currently off-limits.

**Shape.** Every quest is one function the student writes, graded by a table of
`(args, expected)` cases. Functions must be pure: take arguments, `return` a
value, print nothing. That is what makes instant feedback possible.

**Cases.** 3–8 per quest. Always include the boring case, the edge case
(empty string, empty list, zero, negative, a tie) and at least one case that
catches the obvious wrong approach — quest 2 catches `isinstance(True, int)`,
quest 62 catches `>=` instead of `>`. A quest with only happy-path cases is
not drilling anything.

**Hints.** 2–4, gentlest first. Hint 1 names the tool. The last hint may show
the shape of the answer but never the whole answer. Hints are shown
automatically on a failing run, so hint 1 must not spoil it.

**Stories.** One or two sentences in `checks/stories.py`. Concrete and specific:
pizza, dragons, Minecraft stacks, secret codes, leaderboards. "Write a function
that validates input" is the voice we are replacing. If it needs three
sentences, the quest is doing too much.

**Playable quests.** Mark `"playable": True` and give the solution a `demo()`.
The demo **must call the student's own function** — that is the entire point.
A demo may `import` (`random`, `time`) because the student never edits it.
Aim for roughly one playable quest in six.

**Floating point.** Use `Approx(value)` from `checks/registry.py` when an answer
depends on float arithmetic you have not verified exactly. Avoid values where
banker's rounding bites (`f"{7.25:.1f}"` is `'7.2'`, which will baffle an
11-year-old). Pick example values with clean, explainable results.

**Unusual checks.** When a table of cases cannot express the requirement — "did
you leave the original list alone?", "did the global really change?" — add a
`"custom"` checker. See `_check_drop_item` in `checks/world6.py` and
`_check_spend` in `checks/world5.py`. Custom quests need an `"examples"` list
since the generator has no cases to render.

## Voice

Writing for a 10–14 year old. Short sentences, concrete nouns, second person.

- Say "text" before "string", "whole number" before "integer" — then use the
  real word, because the student needs the real word.
- Never write "simply", "just", "obviously", or "as you know".
- Emoji in output and stories: yes, they make the terminal feel alive. Emoji the
  student must type by hand: only when the quest file gives them something to
  copy.
- Avoid non-ASCII characters the student must type from scratch. This is why
  quest 24 says `deg F` rather than `°F`.
- American or British spelling: match the surrounding file.

## Never do these

- Lower a check to make a wrong solution pass.
- Add a quest without adding its story, solution and checks in the same change.
- Run `python3 tools/make_stubs.py --force` with no quest numbers.
- Edit `quests/` by hand — change `checks/` or `solutions/` and regenerate.
- Introduce a dependency, a test framework, or a build step.
- Delete or reorder existing quest numbers. The student's progress is stored
  implicitly in which files they have filled in.
