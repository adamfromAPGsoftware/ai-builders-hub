# The admin map file

One Markdown file, named `admin-map.md`, saved in **My Business → Admin**. It is theirs. The next
module's mapping skill reads it, and their assistant is built only from it. Write every section, in
this order.

- Anything not given: `not given`. A default you applied: the value plus `(assumed)`, listed in
  `assumed`. Something they weren't sure of: `UNCONFIRMED`, listed in `unconfirmed`.
- **Nothing personal, ever:** no names, pay, rates, hours by name, tax file numbers, super or bank
  details of anyone; no customer names; debts as a count and rough total only. Roles for staff
  ("apprentice", "leading hand"), kinds for others ("supplier A", "builder B"). Supplier and builder
  business names only if `business_names_ok: true`. Never a password or login.
- Every price says inc or ex GST.
- Step numbers are the same everywhere: the map, the step table and the exceptions table.
- `map_confirmed: true` only once they said the map is right.
- `assistant_built`, `assistant_name` and `assistant_added` start as `false`, `not made` and
  `unknown`, and are set after step 12.

The worked example below is for the made-up _Tallowood Painting_. Every name and figure is invented.

````markdown
---
map: admin
module: 7
map_version: 0.1.0
status: complete              # complete | incomplete
date: 2026-10-22
map_confirmed: true
assistant_built: true
assistant_kind: bill-checker  # bill-checker | debtor-chase-list (payroll-check: mapped only, being built)
assistant_name: tallowood-bill-checker
assistant_added: later        # yes | later | unknown
business: Tallowood Painting
trade: Residential and builder repaints
office_by: "partner, three days a week; accountant does BAS"
software: { accounts: Xero, payroll: Xero, timesheets: "texts", files: "Google Drive", bank: "bank app" }
week: { monday: timesheets, tuesday: pay run, "20th": bills paid, ad_hoc: invoices and chasing }
bills_per_week: 25
hours_on_bills: 3
staff_on_pay_run: 4
hours_on_pay_run: 2
overdue_invoices_over_30_days: 6
bill_check: "against the order if it can be found; never the docket"
bill_tolerance: "within $20 ex GST, pay; over, email the supplier and hold"
approval: "owner by text; office pays on the 20th"
bill_saved_in: [Xero, bank app, Google Drive]
hours_in: "texts on Friday, checked against the job calendar"
pay_checks: [overtime, travel allowance, apprentice year rate]
new_starter_setup: "about 2 hours, three places"
invoice_timing: "about a week after the job, when the office is told"
chasing: "phone over 30 days when remembered; builders by email"
chase_message: "Hi, just a reminder invoice <number> was due on <date>. Could you let me know when it'll be paid?"
weekly_numbers: "cash in the bank and who owes us, owner on Sunday night in Xero"
business_names_ok: true
steps: 9
exceptions: 10
test_cases: 3                 # bill + pay run + the duplicate payment
parking_list: 1
questions_asked: 30
assumed: []
unconfirmed: [supplier_a_credit]
---

# How Tallowood Painting runs its office week

## The business
## The numbers now (the "before")
## The map
| # | Step | Who | Software | Time | Where it goes wrong |
|:-:|---|---|---|---|---|

Picture: `admin-map.png`. Clickable page: `admin-map.html`.

## Bills: check, approve, pay, file
## The pay run (by role)
## Invoicing and chasing
(When, how, the standard message, personal details removed.)
## The weekly numbers
## Exceptions and odd ones
| Step | What happens | What they do | Rule or check | From |
|:-:|---|---|---|---|
Didn't apply: …
## Judgement calls
Each marked **Rule**, **Check** or **Habit**.
## What's gone wrong
## Test cases
### The bill: supplier A, paint order
Input · steps · paid, filed · how long.
### The pay run (by role)
### The duplicate payment (partial)
## Checks for your assistant
## What they want first, and what stays their call
## Parking list
## Your assistant
Kind, name, test run result, added to Claude or later. If they picked the payroll check: "mapped;
assistant coming when it's built".
## Still to ask
(Only if `status: incomplete`.)
## map.json
```json
(the final map.json, so the page and picture can be made again)
```
````
