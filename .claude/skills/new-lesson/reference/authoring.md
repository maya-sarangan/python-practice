# Quest authoring reference

Exact file shapes. Copy these, do not reinvent them.

## 1. `checks/worldN.py`

```python
"""World 9 -- Dictionary Dungeon. Dictionaries, sets, keys and values."""

QUESTS = {
    78: {
        "world": 9,
        "title": "Spell Book Lookup",          # 2-4 words, a thing not a task
        "one_liner": "Find a spell's power, or say the spell is unknown.",
        "module": "q78_spell_lookup",           # qNN_slug, used in quests/ and solutions/
        "func": "spell_power",                  # what the student must write
        "cases": [
            (("fireball",), 40),                # (args_tuple, expected)
            (("wingardium",), 0),
        ],
        "hints": [
            "Gentlest hint names the tool.",
            "Middle hint shows the shape of the idea.",
            "Last hint may show a line, never the whole answer.",
        ],
        "playable": True,                       # optional; needs demo() in the solution
    },
}
```

`module` must be `q` + zero-padded number + `_` + a short snake_case slug. A
single-argument case still needs the trailing comma: `(("fireball",), 40)`.

### Floating point

```python
from checks.registry import Approx
...
"cases": [((10,), Approx(78.54))],
```

Use `Approx` whenever the expected value comes from float arithmetic you have
not confirmed exactly. Prefer picking inputs with clean answers instead.

### Custom checkers

When a table of cases cannot express the requirement — side effects, "leave the
original alone", mutating a global — write a checker returning
`(label, passed, got, want, was_error)` tuples:

```python
def _check_drop_item(func, module):
    checks = _plain(func, "drop_item", _DROP_CASES)   # helper in checks/world6.py
    original = ["potion", "rope", "potion"]
    func(original, "potion")
    checks.append((
        "the list you were given is left untouched",
        original == ["potion", "rope", "potion"],
        original, ["potion", "rope", "potion"], False,
    ))
    return checks
```

Wire it with `"custom": _check_drop_item` and `"cases": []`. Custom quests have
no cases for the generator to render, so they **must** also supply
`"examples"`, a list of display strings, and `"preamble"` if the stub needs
module-level code (see quest 43's `coins = 100`).

Let `NotImplementedError` escape a custom checker. The console catches it and
reports "Not started yet".

## 2. `checks/stories.py`

```python
    78: "The spell book is 900 pages long and the index is missing. "
        "Build the lookup so nobody sets fire to the library again.",
```

One or two sentences. Concrete nouns. Second person. A reason to care.

## 3. `checks/registry.py`

Append to `WORLDS`:

```python
    {
        "number": 9,
        "name": "Dictionary Dungeon",
        "badge": "📖",
        "teaches": "dictionaries, keys and values, .get(), sets",
    },
```

and add the module to the tuple inside `_build()`.

## 4. `solutions/qNN_slug.py`

Same filename and function name as the quest. Clean, idiomatic, and using
**only** concepts the student has been taught — the solution is teaching
material, not a showcase.

```python
def spell_power(name):
    book = {"fireball": 40, "heal": 25}
    return book.get(name, 0)
```

Playable quests add a `demo()` that calls the student's function:

```python
def demo():
    name = input("Which spell? ")
    print("Power:", spell_power(name))
```

A `demo()` may `import random` / `import time` inside itself. The student never
edits it.

## 5. Generate and verify

```bash
python3 tools/make_stubs.py          # creates only missing stubs
python3 practice.py check
```

Never pass a bare `--force`; it erases student answers. To rewrite stubs you
just created, name them: `python3 tools/make_stubs.py --force 78 79 80`.

## Case-design checklist

Every quest's cases should include:

- the plain expected use
- an edge case: empty string, empty list, `0`, a negative number, a tie
- one case that fails the obvious wrong approach

Examples from the existing bank worth copying:

| Quest | The trap it catches |
|---|---|
| 2 | `isinstance(True, int)` is `True`, so `bool` must be tested first |
| 15 | the `…` counts toward the limit, so the slice is `limit - 1` |
| 31 | out-of-range scores must be rejected before grading |
| 35 | checking `Fizz` before `FizzBuzz` means 15 is never `FizzBuzz` |
| 41 | starting `biggest` at `0` breaks on all-negative input |
| 62 | `>=` instead of `>` hands a tie to the later word |
| 65 | `number % 2 == 1` is wrong for negative numbers |
| 70 | `zip()` stops at the shorter list |
| 77 | starting `best` at `0` breaks on all-negative scores |
