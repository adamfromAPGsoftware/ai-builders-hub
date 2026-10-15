# The welcome card (PNG)

Step 5. A tall picture (1600 px wide, about 3,000 to 3,400 tall) the member attaches to their Hub
intro post, so everyone can see at a glance who they are, how their business runs and where it
hurts. Drawn by `scripts/welcome_card.py` from a `card.json` you write. Only Pillow is needed,
which Claude's code execution already has; the font (DM Sans) ships in `assets/fonts/`.

**The look is the AI Builders Hub system** (Adam's lime-on-black identity for Hub and Skool
images): near-black `#0D0D0D`, cards `#111111`, brand lime `#90F23C`, white ALL CAPS headline
"HEY, I'M <NAME>", grey body `#999999`, DM Sans, the AIB mark top left and
`skool.com/ai-builders-hub` at the foot. **Never red.** Don't restyle it; the script owns the look.

## 1. Write card.json

Everything comes from the **confirmed** summary and the Q16 choices. Leave a field out rather than
guess; the script skips any section with nothing in it.

| Field | What goes in it | Limit |
|---|---|---|
| `name` | Name to show (Q16, first name by default) | Required |
| `business` | Business name, unless they hid it | Optional |
| `trade` | Trade in a few words | ~45 characters |
| `area` | Region, never a street | Optional |
| `team` | e.g. "Me + 3 techs + office 2 days a week" | Optional |
| `role` | Their track in their words, e.g. "Tradie automating my own business" | ~45 characters |
| `what_i_do` | One or two sentences | 3 lines on the card |
| `goals` | Their three 90-day goals (Q6), short | 3 items, ~60 characters each |
| `steps_title` | "How a job runs at [Business]"; builder track: "How I work with clients" | |
| `steps` | 3 to 8 items: `step`, `who`, `tool`, and `pain` (a few words) on the bottleneck steps only. Any step with `pain` gets a lime outline and a lime ! | `step` ~28 characters |
| `bottlenecks` | Top three (Q12): `what`, `hours` (number a week, or leave out), `why` (one line) | 3 items |
| `hours_lost_total` | Sum of the hours they gave on bottleneck steps, only if they gave hours and Q16 row 4 is shown | Optional |
| `manual` | Jobs still done by hand (Q11), short labels | 6 chips |
| `tools` | Their tools (Q9) | 8 chips |
| `automate_first` | Q14, in their words | 3 lines |
| `ask_me_about` | Q15, in their words | 3 lines |
| `joined` | "Intro done · <Month YYYY>" (shown bottom right) | |

Never on the card (rule 3): phone, email, street address, prices, rates, margins, revenue,
customer or staff names, anything they marked private, or Q13 ("what stays my call").

## 2. Draw it

```bash
python3 scripts/welcome_card.py card.json welcome-card-<slug>.png
```

`<slug>` is the business name (or their name, if the business is hidden) in lowercase with
hyphens. Run the script from the skill's folder or pass its full path. If the script file isn't
reachable, copy it from this skill into the working folder first; don't rewrite it from memory.

## 3. Check it with them

Show the picture, then one table:

| # | Check your card |
|:-:|---|
| 1 | Name, business and what you do |
| 2 | Your three goals |
| 3 | Your steps and the lime ! marks |
| 4 | Bottlenecks and hours |
| 5 | Anything to hide or reword |

"Reply 'all good', or the number and what to change." Edit `card.json`, redraw, show it again.
Words too long for a box get shortened with them, never cut silently (the script adds "…" as a
last resort).

## 4. If code execution is off

Ask them to turn on **Settings → Capabilities → Code execution and file creation** and say "try
again". If they can't, publish the card as a self-contained HTML artifact with the same sections,
order and colours (`#0D0D0D` background, `#111111` cards, lime `#90F23C` accents and ! marks,
white headline, DM Sans from Google Fonts), 800 px wide, and ask them to screenshot it.

## 5. Worked example

`card.json` for _Coolabah Air_ (made up, every figure invented):

```json
{
  "name": "Sam",
  "business": "Coolabah Air",
  "trade": "Air conditioning installs and servicing",
  "area": "Western Sydney",
  "team": "Me + 3 techs + office 2 days a week",
  "role": "Tradie automating my own business",
  "what_i_do": "Split systems and ducted for homes, plus service contracts for a few small offices and cafes. 12 years on the tools.",
  "goals": [
    "Get quotes out the same day, not at 10pm",
    "Stop typing the same job into three places",
    "Maybe build this for other air con guys later"
  ],
  "steps_title": "How a job runs at Coolabah Air",
  "steps": [
    {"step": "Enquiry comes in", "who": "Me", "tool": "Phone, website", "pain": "Missed calls on the tools"},
    {"step": "Site visit and quote", "who": "Me", "tool": "Notepad, Excel", "pain": "Written up at night"},
    {"step": "Yes and deposit", "who": "Customer", "tool": "Text, Xero"},
    {"step": "Order the unit", "who": "Office", "tool": "Supplier portal"},
    {"step": "Book the install", "who": "Office", "tool": "ServiceM8"},
    {"step": "Install and commission", "who": "Techs", "tool": "ServiceM8 app", "pain": "Photos and certs re-typed"},
    {"step": "Invoice and chase", "who": "Office", "tool": "Xero", "pain": "Chasing slips"},
    {"step": "Yearly service reminder", "who": "Office", "tool": "Spreadsheet", "pain": "Often never sent"}
  ],
  "bottlenecks": [
    {"what": "Writing quotes up at night", "hours": 6, "why": "Site notes to Excel to PDF, every quote"},
    {"what": "Job paperwork after the install", "hours": 4, "why": "Photos, compliance certs and the refrigerant log typed again"},
    {"what": "Service reminders and chasing invoices", "hours": 3, "why": "Done when the office has time, so mostly not"}
  ],
  "hours_lost_total": 13,
  "manual": ["Quote write-ups", "Re-keying into ServiceM8", "Compliance certs", "Refrigerant log", "Service reminders", "Invoice chasing"],
  "tools": ["ServiceM8", "Xero", "Excel", "Gmail", "Supplier portal", "Claude Pro"],
  "automate_first": "Turn my site notes and photos into a quote I can send from the ute",
  "ask_me_about": "Ducted vs split for old fibro houses, and running a small service team",
  "joined": "Intro done · October 2026"
}
```
