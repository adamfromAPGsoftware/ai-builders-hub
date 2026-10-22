# Their customer service map (the page and the picture)

Step 7 (and step 9). The map is how they check you understood them, and what they keep and post in
the Hub. It has two layers: a flowchart anyone gets at a glance, and the detail behind every step
when they tap it.

The layout belongs to `map/map-template.html` and the two scripts in `map/scripts/`. **You only
write `map.json`.** Never draw your own layout, restyle it, or hand-write HTML. The look is the AI
Builders Hub's: lime on black, DM Sans.

## 1. Write map.json

From the running step list and the confirmed answers. Leave a field out rather than guess. All
fields are described in `map/README.md`; for this module:

```json
{
  "business": "Tallowood Painting",
  "trade": "Residential and builder repaints, Sydney",
  "module": { "n": 6, "name": "Customer service" },
  "per": "message",
  "title": "How we handle customer messages today",
  "summary": "Work orders land in the office inbox three days a week; homeowners text the owner. Every order is typed into Tradify by hand, and status questions wait for the owner.",
  "updated": "2026-10-22",
  "before": [
    { "value": "15–20", "label": "messages a day" },
    { "value": "10 min", "label": "to enter a work order" },
    { "value": "1 day", "label": "a week on messages" }
  ],
  "steps": [ … ],
  "parking": [ { "question": "Property manager B's new rate sheet", "who": "Property manager B" } ]
}
```

**Steps.** One per step on their list, in order, 5 to 10 of them. Merge tiny steps; split a step
that two different people do. Each step:

- `id`: short and unique (`arrives`, `sort`, `enter`, `confirm`, `ask-owner`)
- `title`: what happens, in their words, about 28 characters at most
- `who`: a role ("Office", "Owner", "Property manager"), never a person's name
- `tools`: the names on their screen (`Outlook`, `Tradify`, `Phone`)
- `time` as they said it, and `minutes` (hands-on minutes for one message) only if they gave one
- `flag`: `slow` or `copy` on the steps where time goes (the slow and typed-twice steps), with
  `pain` in a few words. Usually two to four steps, never all of them.
- `detail`: `what` (two or three sentences), `rules`, `goes_wrong`, `odd_cases` (from the sweep
  and Q22), and `source` ("Message 1", "Your answer to Q12")

**Decisions.** Where their answer was "it depends", add a step with `"type": "fork"`, the question
as the `title`, and two to four `options` (`label` plus a short `note`). For customer service the
usual one is "Order or question?" near the start, and often "Needs the owner?".

**Never in it:** a customer's, tenant's or contact's name, phone, email or street address. Business
customers' company names only if they said yes at Q16. Rates and prices only in `detail`.

`first_skill` is added in step 9, once Q29 is answered:

```json
"first_skill": {
  "name": "Your order reader",
  "takes_over": ["enter", "confirm"],
  "what": "Drop in a work order; it pulls out the job, checks it against your rates and drafts the confirmation. You check it, enter it and send.",
  "saves": "About 8 min a work order"
}
```

`saves` only if you can work it out from their numbers (time on the steps it takes over, less a
minute or two to check). Otherwise leave it out.

## 2. Make the page

Find the skill's own folder (where this file is), then run:

```bash
python3 <skill folder>/map/scripts/fill_map.py map.json customer-service-map.html
```

Show `customer-service-map.html` as an artifact if you can make one; otherwise offer it as a
download and say "open it in your browser". Then say:

"**Here's your map.** The lime steps are where your time goes. Tap any step for the detail. On your
phone it's in the Artifacts tab."

## 3. Confirm it step by step

Never "looks good?". Go through it in order:

- "Is step 1 right: who, what and the software?" (Yes · Change it)
- "Anything missing between 2 and 3?"
- At each decision: "Are those the only ways it goes?"
- At each lime step: "Is this really where the time goes?"

Change `map.json` and remake the page after every fix. Nothing is final until they say the map is
right. Then set `map_confirmed: true` in the map file header.

## 4. The picture (step 9)

```bash
python3 <skill folder>/map/scripts/map_card.py map.json customer-service-map.png
```

It needs only Pillow (code execution has it) and the font in `map/assets/fonts/`. It draws the
first layer only: the before numbers, the steps, the lime steps, the decisions, and what they're
building first. Look at it before you offer it; if a title is cut off with "…", shorten that step's
`title` and run it again.

## 5. Can't run code here

Send the steps as a numbered list grouped by who does them, with every decision and the lime steps
marked, and confirm it the same way. Put `map.json` in the map file so the page and picture can be
made later, and say: "Turn on **Settings → Capabilities → Code execution and file creation** and say
**make my map** to get the page and the picture."
