# The lead generation map file

One Markdown file, named `lead-generation-map.md`, saved in **My Business → Lead generation**. It
is theirs. The next module's mapping skill reads it, and their assistant is built only from it.
Write every section, in this order.

- Anything not given: `not given`. A default you applied: the value plus `(assumed)`, listed in
  `assumed`. Something they weren't sure of: `UNCONFIRMED`, listed in `unconfirmed`.
- **No personal details anywhere:** no names, phones, emails or addresses of builders' staff,
  estimators, customers or anyone else. Roles only ("estimator at builder A"). Company names only if
  `company_names_ok: true`. Never a password or login.
- Step numbers are the same everywhere: the map, the step table and the exceptions table.
- `map_confirmed: true` only once they said the map is right.
- `assistant_built`, `assistant_name` and `assistant_added` start as `false`, `not made` and
  `unknown`, and are set after step 12.

The worked example below is for the made-up _Tallowood Painting_. Every name and figure is invented.

````markdown
---
map: lead-generation
module: 1
map_version: 0.1.0
status: complete              # complete | incomplete
date: 2026-10-22
map_confirmed: true
assistant_built: true
assistant_kind: follow-up-list  # tender-watch | follow-up-list | contact-tidy-up
assistant_name: tallowood-follow-ups
assistant_added: later        # yes | later | unknown
business: Tallowood Painting
trade: Residential and builder repaints
area: Sydney (Hornsby to the Northern Beaches)
shapes: [chasing, comes-to-you]   # chasing | comes-to-you
sources: { google_and_referrals: 50, builders_known: 35, tender_portal: 15 }   # percent, their estimate
best_source: builders known
worst_source: tender portal
who_finds_work: owner
hours_per_week: 5
leads_per_month: "30 to 40"
quotes_per_month: 15
jobs_per_month: "5 to 6"
software: [EstimateOne, Google Sheet, phone contacts, Gmail]
worth_chasing: "over $20,000 ex GST, within an hour of Hornsby, builder pays on time, no new apartments"
lead_list: "Google Sheet: builder, project, suburb, size, date, next step"
follow_up_rhythm: "meant to be fortnightly; really when remembered"
follow_up_message: "Hi, just checking in on the <project> job. Happy to price it when the drawings are out."
company_names_ok: true
reviews: "47 on Google; asked for about one in five jobs"
repeat_customers: "exteriors every 7 to 10 years; never reminded"
ads: "$300 a month Google Ads; results unknown"
steps: 8
exceptions: 9
test_cases: 3                 # 2 won + 1 missed
parking_list: 1
questions_asked: 29
assumed: []
unconfirmed: [ads_results]
---

# How Tallowood Painting finds its next jobs

## The business
## The numbers now (the "before")
## The map
| # | Step | Who | Software | Time | Where it goes wrong |
|:-:|---|---|---|---|---|

Picture: `lead-generation-map.png`. Clickable page: `lead-generation-map.html`.

## Where work comes from, and which pays
## Worth chasing: the cut-offs
## Finding the right person, and the list
## Following up
(How often, how, by whom, the standard message, personal details removed.)
## Work that comes to you
(Reviews, referrals, repeat customers, ads.)
## Exceptions and odd ones
| Step | What happens | What they do | Rule or check | From |
|:-:|---|---|---|---|
Didn't apply: …
## Judgement calls
Each marked **Rule**, **Check** or **Habit**.
## The job that got away
## Test cases
### Job 1: townhouse repaint for builder A (tender portal)
Source · steps · outcome · time from spotted to quote.
### Job 2: homeowner repaint (Google)
### Job 3 (partial): the Killara townhouses, missed
## Checks for your assistant
## What they want first, and what stays their call
## Parking list
## Your assistant
Kind, name, test run result, added to Claude or later.
## Still to ask
(Only if `status: incomplete`.)
## map.json
```json
(the final map.json, so the page and picture can be made again)
```
````
