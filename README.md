# 🐍 Python Quest

77 coding quests across 8 worlds. You write one function, the Quest Console
tells you instantly whether it works, and 12 of them turn into things you can
actually play.

```
  🐍  P Y T H O N   Q U E S T   M A P

  ██████░░░░░░░░░░░░░░░░░░   25%  19/77 quests complete

  🎒  World 1: The Wizard's Backpack (7/7)
     variables, data types, type casting, f-strings
     ✅ 01  Name Tag Machine
     ✅ 06  Emoji Health Bar  🎮
     ...
```

## Start here

```bash
python3 practice.py            # see the whole map
python3 practice.py next       # which quest is next?
```

Open the quest file it names, delete the line that says
`raise NotImplementedError`, and write your answer. Then:

```bash
python3 practice.py 1          # grade quest 1
```

You will see something like this:

```
🎯 Quest 01 -- Name Tag Machine
   Build a sparkly name tag out of a name and an age.

   ✅ make_name_tag('Zara', 11)  ->  '⭐ ZARA (11) ⭐'
   ❌ make_name_tag('Ada', 36)
      you gave:  '⭐ Ada (36) ⭐'
      I wanted:  '⭐ ADA (36) ⭐'

   1/2 passed  So close!

   💡 Hint: name.upper() hands you back a SHOUTING copy of the name.
```

## Every command

| Command | What it does |
|---|---|
| `python3 practice.py` | The quest map, with your progress |
| `python3 practice.py next` | The next quest you have not finished |
| `python3 practice.py 7` | Grade quest 7 |
| `python3 practice.py 7 --hint` | Every hint for quest 7, gentlest first |
| `python3 practice.py 7 --play` | Play quest 7 (only the 🎮 ones) |
| `python3 practice.py world 2` | Grade all of World 2 |
| `python3 practice.py all` | Grade everything |
| `python3 practice.py report` | Progress report, and what you are stuck on |

## The eight worlds

| | World | What you will master |
|---|---|---|
| 🎒 | 1. The Wizard's Backpack | variables, data types, type casting, f-strings |
| 🔤 | 2. Word Wizardry | slicing, string methods, `ord()` and `chr()` |
| 🔢 | 3. Number Ninjas | `//` and `%`, `**`, `round()`, `abs()` |
| 🧭 | 4. True or False Island | comparisons, `if`/`elif`/`else`, truthy and falsy |
| 🏭 | 5. The Function Factory | parameters, returns, defaults, local vs global |
| 🧰 | 6. Treasure Chests | lists, tuples, slicing, unpacking, list methods |
| 🌀 | 7. The Loop Lair | `for`, `while`, `range()`, `break`, `continue` |
| ⚡ | 8. Power-Up Palace | `enumerate`, `zip`, comprehensions, `map`/`filter` |

Worlds get harder as you go, but you can jump around. If a quest looks
impossible, it is almost always because an earlier quest taught the trick.

## Two rules

1. **Red is not failure.** Red tells you exactly what to change. Professional
   programmers see red hundreds of times a day.
2. **Read the first failing line, not all of them.** Fix one thing, run again.

---

## For grown-ups

### Layout

```
practice.py        the Quest Console: grader, hints, progress, demos
quests/            the student's working files -- the only place they edit
solutions/         worked answers, one per quest (don't show these too early)
checks/            test cases, hints and story text (the answer key)
tools/             stub generator and the freeCodeCamp curriculum fetcher
CURRICULUM.md      what has been taught, and what is therefore off-limits
CLAUDE.md          conventions for adding new lessons with Claude Code
```

### Verifying the bank

```bash
python3 practice.py check
```

Runs all 77 worked solutions against all 350+ checks and fails loudly if any
quest is unsolvable or any expected value is wrong. Run this after any edit to
`checks/` or `solutions/`. A hook in `.claude/settings.json` runs it for you
when Claude Code touches those folders.

### Adding the next lesson

When your student finishes a new freeCodeCamp section, in Claude Code run:

```
/new-lesson Dictionaries and Sets
```

It reads the real concept list out of the freeCodeCamp curriculum source,
appends it to `CURRICULUM.md`, writes a new world of quests with checks and
solutions, and refuses to finish until `practice.py check` is green. See
`CLAUDE.md` for the quality rules it follows.

### Scope discipline

Quests only ever use concepts listed as covered in `CURRICULUM.md`. Dictionaries,
sets, `try`/`except`, classes, file I/O and recursion are deliberately absent
because the student has not met them yet. This is the main thing to protect as
the bank grows.

### Python version

Everything runs on **Python 3.9+** with no third-party packages.
