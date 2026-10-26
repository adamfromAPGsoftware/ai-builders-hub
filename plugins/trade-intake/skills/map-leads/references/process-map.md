# Their lead generation map (the page and the picture)

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
  "module": { "n": 1, "name": "Lead generation" },
  "per": "lead",
  "title": "Where our work comes from today",
  "summary": "Homeowners find us on Google and through referrals. Builder work is chased by the owner from a Google Sheet and tender emails, on Sunday nights.",
  "updated": "2026-10-22",
  "before": [
    { "value": "35", "label": "leads a month" },
    { "value": "15", "label": "become a quote" },
    { "value": "5 h", "label": "a week chasing work" }
  ],
  "steps": [ … ],
  "parking": [ { "question": "Which jobs last year came from Google Ads", "who": "Owner, from Xero" } ]
}
```

**Steps.** One per step on their list, in order, 5 to 10 of them. Each step:

- `id`: short and unique (`spot`, `worth-it`, `find-person`, `list`, `follow-up`)
- `title`: what happens, in their words, about 28 characters at most
- `who`: a role ("Owner", "Office"), never a person's name
- `tools`: the names on their screen (`EstimateOne`, `Google Sheet`, `Phone`)
- `time` as they said it, and `minutes` (hands-on minutes for one lead) only if they gave one
- `flag`: `slow` or `copy` on the steps where time goes, with `pain` in a few words. Usually two to
  four steps, never all of them.
- `detail`: `what`, `rules`, `goes_wrong`, `odd_cases`, and `source` ("Job 1", "Your answer to Q10")

**Decisions.** Where their answer was "it depends", add a step with `"type": "fork"`, the question as
the `title`, and two to four `options`. For lead generation the usual one is near the start: "Where
did it come from?" with options like "Tender or builder" and "Google or referral", then "Worth
chasing?".

**Never in it:** a person's name, phone, email or address. Business names only if they said yes at
Q12.

`first_skill` is added in step 9, once Q28 is answered:

```json
"first_skill": {
  "name": "Your follow-up list",
  "takes_over": ["follow-up"],
  "what": "Every Monday: who to ring this week and why, with the message drafted. You make the calls.",
  "saves": "About 2 h a week"
}
```

`saves` is time back, shown as "back, on our estimate". Only fill it if you can work it out from
their numbers; otherwise leave it out.

## 2. Make the page

```bash
python3 <skill folder>/map/scripts/fill_map.py map.json lead-generation-map.html
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
python3 <skill folder>/map/scripts/map_card.py map.json lead-generation-map.png
```

Look at it before you offer it; if a title is cut off with "…", shorten that step's `title`.

## 5. Can't run code here

Send the steps as a numbered list grouped by who does them, and confirm the same way. Put `map.json`
in the map file and say: "Turn on **Settings → Capabilities → Code execution and file creation** and
say **make my map** to get the page and the picture."
