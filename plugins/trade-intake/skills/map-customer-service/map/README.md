# The process map (shared by every module intake)

Each intake ends with the member's map of how that department runs **today**, in two forms from one
JSON file:

| Output | Made by | Where it goes |
|---|---|---|
| `<module>-map.html`: the flowchart, every step clickable for the detail, Back / Next walk-through | `scripts/fill_map.py map.json <module>-map.html` | `My Business/<module>/`; a public link if their Claude can publish one |
| `<module>-map.png`: the picture of the flowchart (1200 px wide) | `scripts/map_card.py map.json <module>-map.png` | Posted on the module's map thread in the Hub |

The layout belongs to `map-template.html` and the two scripts. Intakes only write the JSON; they
never draw their own layout. Look: the AI Builders Hub system, lime `#90F23C` on `#0D0D0D`, DM Sans
(`assets/fonts/`, SIL Open Font Licence), never red. Example: `examples/tallowood-quoting.json`.

## map.json

Write it only from the **confirmed** drawing and summary. Leave a field out rather than guess.

| Field | What goes in it |
|---|---|
| `business`, `trade` | Business name and trade in a few words |
| `module` | `{ "n": 3, "name": "Quoting" }` |
| `per` | What one run of the process is: `quote`, `order`, `lead`, `bill`, `pay run` (labels the time bar) |
| `title` | "How we quote today", in their words where possible |
| `summary` | One or two sentences: how it runs today, plainly |
| `updated` | `YYYY-MM-DD` |
| `before` | Exactly three `{ "value", "label" }`: the "before" numbers from the intake. `not given` numbers are left out, not guessed |
| `steps` | In order. See below |
| `first_skill` | `{ "name", "takes_over": [step ids], "what", "saves" }`. `saves` only if the intake worked it out; say "on our estimate" |
| `parking` | The parking list: `{ "question", "who" }` |
| `example` | `true` only for made-up examples (adds a banner) |

**A step:** `id` (short, unique), `title` (~28 characters), `who` (a role, never a name), `tools`
(names on their screen), `time` (as they said it), `minutes` (a number for the time bar, hands-on
time for one run; leave out if unknown), `flag` (`slow` or `copy`, only on the steps where time
goes), `pain` (a few words, on flagged steps), and `detail`:

- `what`: what happens, two or three sentences
- `rules`: the rules and numbers behind it
- `goes_wrong`: what goes wrong, from real jobs
- `odd_cases`: the odd ones
- `source`: where it came from ("Your quote Q-1043", "Your answer to Q8")

**A decision:** `"type": "fork"`, `title` as the question, `who`, and `options`:
`[{ "label", "note" }]`, two to four. Put a decision where their answer was "it depends on…".

## Never on the map

Customer, supplier staff or employee names, phone numbers, emails or street addresses; anyone's pay;
passwords or logins; anything they asked to keep off. Rates and prices may appear in `detail` (they
are the member's own), never on the picture.
