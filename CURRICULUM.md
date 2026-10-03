# Curriculum ledger

The single source of truth for **what the student has been taught**, and
therefore what a quest is allowed to use. Every new lesson appends a section
here before any quests are written.

Course: freeCodeCamp Python (v9) — <https://www.freecodecamp.org/learn/python-v9/>

To regenerate a concept inventory from the real curriculum source:

```bash
python3 tools/fcc_lesson.py modules                       # find the review block
python3 tools/fcc_lesson.py concepts review-<slug>        # compact inventory
python3 tools/fcc_lesson.py review   review-<slug>        # full detail
```

---

## Completed lessons

### 1. Python Basics — ✅ covered by quests 1–43
`review-python-basics`

- Variables, naming conventions, comments, `print()`
- Data types: `int`, `float`, `str`, `bool`; `type()`, `isinstance()`
- Strings: indexing, escaping, concatenation, f-strings, slicing, `len()`
- The `in` operator on strings
- String methods: `upper`, `lower`, `strip`, `replace`, `split`, `join`,
  `startswith`, `endswith`, `find`, `count`, `capitalize`, `isupper`,
  `islower`, `title`, `maketrans`/`translate`
- Numbers: `+ - * /`, `%`, `//`, `**`, `float()`, `int()`, `round()`,
  `abs()`, `pow()`
- Augmented assignment (`+=`, `-=`, …)
- Functions: parameters, arguments, `return`, default values
- Built-ins: `input()`, `int()`
- Scope: local vs global, the `global` keyword
- Comparison operators: `== != > < >= <=`
- `if` / `elif` / `else`
- Truthy and falsy values, `bool()`
- Boolean operators `and`, `or`, `not`, and short-circuiting
- `ord()` and `chr()` (taught via the Caesar cipher workshop)

### 2. Install Python — skipped by the teacher
`review-python-installation`. Nothing to drill. The student is on the system
Python, so quests must run on **Python 3.9+**.

### 3. Loops and Sequences — ✅ covered by quests 44–77
`review-loops-and-sequences`

- Lists: creation, `list()`, indexing, negative indexing, `len()`,
  mutability, `IndexError`, `del`, `in`, nesting, unpacking, `*rest`,
  slicing with step
- List methods: `append`, `extend`, `insert`, `remove`, `pop`, `clear`,
  `sort`, `reverse`, `index`; the `sorted()` built-in
- Tuples: creation, immutability (`TypeError`), indexing, `tuple()`, `in`,
  unpacking, slicing; `count()`, `index()`
- `sorted()` with `key=` and `reverse=`
- `for` loops over lists, tuples and strings; nested `for` loops
- `while` loops
- `break`, `continue`, and the `for`/`else` clause
- `range(start, stop, step)`, including negative steps
- `enumerate()` with `start=`, and `zip()`
- List comprehensions
- `filter()`, `map()`, `sum()` with `start=`
- Lambda functions

---

## Not taught yet — must NOT appear in any quest

Keeping these out is what makes the quests solvable. If the student meets a
tool they have never seen, the exercise stops teaching and starts blocking.

- Dictionaries and sets (`{}`, `dict()`, `set()`, `.keys()`, `.items()`, …)
- Modules and `import` (the only exceptions are inside a pre-written `demo()`,
  which is a gift the student never has to touch)
- `try` / `except` / `finally`, `raise`, custom exceptions
- Classes, objects, `self`, inheritance
- File input and output
- Recursion
- Generators, decorators, `yield`
- Type hints
- `while`/`else`, `match`/`case`, walrus `:=`

---

## Quest number allocation

| Quests | World | Topic | Lesson |
|---|---|---|---|
| 1–7 | 1 | The Wizard's Backpack — variables, types, casting, f-strings | Python Basics |
| 8–19 | 2 | Word Wizardry — slicing, string methods, `ord`/`chr` | Python Basics |
| 20–28 | 3 | Number Ninjas — `//`, `%`, `**`, `round`, `abs` | Python Basics |
| 29–37 | 4 | True or False Island — conditionals, boolean logic, truthiness | Python Basics |
| 38–43 | 5 | The Function Factory — parameters, returns, defaults, scope | Python Basics |
| 44–54 | 6 | Treasure Chests — lists, tuples, slicing, unpacking | Loops and Sequences |
| 55–68 | 7 | The Loop Lair — `for`, `while`, `range`, `break`, `continue` | Loops and Sequences |
| 69–77 | 8 | Power-Up Palace — `enumerate`, `zip`, comprehensions, `map`/`filter` | Loops and Sequences |

**Next free quest number: 78. Next free world number: 9.**
