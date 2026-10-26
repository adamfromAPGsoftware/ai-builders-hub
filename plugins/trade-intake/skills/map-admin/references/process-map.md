# Their admin map (the page and the picture)

Step 7 (and step 9). The map is how they check you understood them, and what they keep and post in
the Hub. It has two layers: a flowchart anyone gets at a glance, and the detail behind every step
when they tap it.

The layout belongs to `map/map-template.html` and the two scripts in `map/scripts/`. **You only
write `map.json`.** Never draw your own layout, restyle it, or hand-write HTML. All fields are
described in `map/README.md`.

## 1. Write map.json

From the running step list and the confirmed answers. Leave a field out rather than guess.

```json
{
  "business": "Tallowood Painting",
  "trade": "Residential and builder repaints, Sydney",
  "module": { "n": 7, "name": "Finance and admin" },
  "per": "bill",
  "title": "How our office week runs today",
  "summary": "Bills arrive by email and are paid on the 20th after a text to the owner. Each one is saved in three places. Debtors are chased by phone when someone remembers.",
  "updated": "2026-10-22",
  "before": [
    { "value": "25", "label": "bills a week" },
    { "value": "3 h", "label": "a week on bills" },
    { "value": "6", "label": "invoices over 30 days" }
  ],
  "steps": [ … ],
  "parking": [ { "question": "Supplier A's credit for the July duplicate", "who": "Supplier A" } ]
}
```

**Which steps.** The map follows the bill end to end (arrives → checked → approved → paid → filed),
then the pay run (hours in → checked → approved → paid) and the chasing (invoice out → overdue →
chased → paid) as their own steps. 6 to 10 steps in all; merge tiny ones. Each step:

- `id`: short and unique (`bill-in`, `check`, `approve`, `pay`, `file`, `hours`, `pay-run`, `chase`)
- `title`: what happens, in their words, about 28 characters at most
- `who`: a role ("Office", "Owner", "Bookkeeper"), never a person's name
- `tools`: the names on their screen (`Xero`, `Bank app`, `Google Drive`)
- `time` as they said it, and `minutes` (hands-on minutes for one bill) only on the bill's steps
- `flag`: `slow` or `copy` on the steps where time goes, with `pain` in a few words. Usually two to
  four steps, never all of them.
- `detail`: `what`, `rules`, `goes_wrong`, `odd_cases`, and `source` ("The bill", "Your answer to
  Q11")

**Decisions.** Where their answer was "it depends", add a step with `"type": "fork"`, the question as
the `title`, and two to four `options`. For admin the usual one is "Does the bill match?" (Pay it ·
Hold and query).

**Never in it:** anyone's name, pay, rate, hours by name, tax file number, super or bank details; any
customer's name or a debt per customer. Supplier names only if they said yes at Q12.

`first_skill` is added in step 9, once Q28 is answered:

```json
"first_skill": {
  "name": "Your bill checker",
  "takes_over": ["check"],
  "what": "Drop in a bill; it checks it against the order and docket and only brings you the mismatches. You approve and pay.",
  "saves": "About 2 h a week"
}
```

`saves` is time back, shown as "back, on our estimate". Only fill it if you can work it out from
their numbers; otherwise leave it out.

## 2. Make the page

```bash
python3 <skill folder>/map/scripts/fill_map.py map.json admin-map.html
```

Show it as an artifact if you can; otherwise offer it as a download. Then say: "**Here's your map.**
The yellow steps are where your time goes. Tap any step for the detail."

## 3. Confirm it step by step

Never "looks good?". "Is step 1 right: who, what and the software?" · "Anything missing between 2
and 3?" · at each decision "Are those the only ways it goes?" · at each yellow step "Is this really
where the time goes?" Change `map.json` and remake the page after every fix. Then set
`map_confirmed: true` in the map file header.

## 4. The picture (step 9)

```bash
python3 <skill folder>/map/scripts/map_card.py map.json admin-map.png
```

Look at it before you offer it; if a title is cut off with "…", shorten that step's `title`. Check
again that nothing personal is on it before they post it.

## 5. Can't run code here

Send the steps as a numbered list grouped by who does them, and confirm the same way. Put `map.json`
in the map file and say: "Turn on **Settings → Capabilities → Code execution and file creation** and
say **make my map** to get the page and the picture."
