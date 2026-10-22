# The customer service map file

One Markdown file, named `customer-service-map.md`, saved in **My Business → Customer service**.
It is theirs. The next module's mapping skill reads it, and their assistant is built only from it.
The block at the top is for whatever reads it later; the sections below are for a person. Write
every section, in this order.

- Anything not given: `not given`. A default you applied: the value plus `(assumed)`, listed in
  `assumed`. Something they weren't sure of: `UNCONFIRMED`, listed in `unconfirmed`.
- **No personal details anywhere:** no customer, tenant, site contact or staff names, phones, emails
  or street addresses. "Homeowner A", "property manager A". Business customers' company names only
  if `customer_names_ok: true`. Never a password, login or bank detail.
- Every price says inc or ex GST.
- Step numbers are the same everywhere: the map, the step table and the exceptions table.
- `map_confirmed: true` only once they said the map is right.
- `assistant_built`, `assistant_name` and `assistant_added` start as `false`, `not made` and
  `unknown`, and are set after step 12.

The worked example below is for the made-up _Tallowood Painting_. Every name and figure is invented.

````markdown
---
map: customer-service
module: 6
map_version: 0.1.0
status: complete              # complete | incomplete
date: 2026-10-22
map_confirmed: true
assistant_built: true         # true | false
assistant_kind: order-reader  # order-reader | answer-finder | job-status
assistant_name: tallowood-orders
assistant_added: later        # yes | later | unknown
business: Tallowood Painting
trade: Residential and builder repaints
area: Sydney (Hornsby to the Northern Beaches)
handled_by: "office (partner, three days a week); owner by text the rest"
cover_when_away: none
channels: [office inbox, owner's mobile texts, website form, property manager portal]
kinds: [work orders, job questions, status chasing, changes]
most_time: status chasing
messages_per_day: "15 to 20"
minutes_per_order: 10
share_of_week: "about a day"
reply_time_now: "within a day; texts up to three days"
urgent_rule: "property managers same day; leaks or damage ring straight away"
needs_owner: [prices, dates]
orders: yes
order_format: "PDF work order by email"
order_fields: [their reference, address, tenant contact, scope, not-to-exceed, due date]
entered_in: Tradify
numbering: "our job number; their WO number in the notes"
priced_against: "contract rate sheet per room"
their_codes: { "bed": "bedroom up to 12 m²" }
over_limit_rule: "over the not-to-exceed, ring the property manager before booking"
confirm_wording: "Thanks, booked for <day date>, ref <their ref>. We'll text the tenant the day before."
customer_names_ok: true
status_truth: "Tradify calendar, not always current"
bad_news: "owner by text; property managers by email"
sign_off: "Cheers, the Tallowood team"
software: [Outlook, Tradify, Xero, phone]
steps: 8
exceptions: 9
test_cases: 3                 # 2 full + 1 partial (the one that went wrong)
parking_list: 1
questions_asked: 28
assumed: [cover_when_away]
unconfirmed: [property_manager_b_rates]
---

# How Tallowood Painting handles customer messages

## The business
(Who they are, who handles messages, where they land, the software.)

## The numbers now (the "before")
- 15 to 20 messages a day; a work order takes 10 minutes to enter; about a day a week on messages.
- Replies within a day; texts sometimes three days.

## The map
The confirmed steps, numbered, in one table:

| # | Step | Who | Software | Time | Where it goes wrong |
|:-:|---|---|---|---|---|
| 1 | Message arrives | Customer | Outlook, phone | | Texts to the owner get lost |
| 2 | Order or question? | Office | | | |
| … | | | | | |

Picture: `customer-service-map.png`. Clickable page: `customer-service-map.html`.

## Kinds of messages, what's urgent, and who answers what
## Orders and work orders
(What arrives, what's taken off, where it's entered, numbering, their codes, pricing, over-limit
rule, the confirmation wording.)
## Questions: the top five and where each answer lives
| Question | Where the answer lives | Who can answer |
|---|---|---|
## Job status and bad news
## Standard replies, tone and sign-off
(Paste their standard replies, personal details removed.)
## Exceptions and odd ones
| Step | What happens | What they do | Rule or check | From |
|:-:|---|---|---|---|
Didn't apply: …
## Judgement calls
Each marked **Rule**, **Check** or **Habit**.
## What's gone wrong
## Test cases
### Message 1: property manager's work order for unit 4
Input · steps · what was entered · the reply that went back.
### Message 2: homeowner asking last job's door colour
### Message 3 (partial): the work order missed for a week
## Checks for your assistant
(From the pre-mortem and the odd ones.)
## What they want first, and what stays their call
## Parking list
| Question | Who can answer |
|---|---|
## Your assistant
Kind, name, test run result, added to Claude or later.
## Still to ask
(Only if `status: incomplete`.)
## map.json
```json
(the final map.json, so the page and picture can be made again)
```
````
