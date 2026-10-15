# Their own ordering assistant (the exported skill)

Steps 10 to 12 of the interview. Once the intake file is made, turn what you learned into a skill
they can add to Claude and use in Cowork every day, try it once on Order 1, then walk them through
adding it. Everything in it comes from the **confirmed** intake file: nothing new, nothing invented,
nothing they didn't approve.

To the owner it is "your ordering assistant". Say "skill" only where it is the name on Claude's own
screen ("Skills", "Upload skill") and in the phrase "update my skill".

Building, zipping and testing it do **not** count toward the 35 questions.

## 1. The folder

- **Name:** `<business-slug>-ordering`: the business name in lowercase, spaces to hyphens, only
  letters, numbers and hyphens, 64 characters at most, no leading or trailing hyphen.
  E.g. `ironbark-ordering`. The SKILL.md `name` is exactly the folder name.
- **Layout:**

  ```
  <name>/
    SKILL.md
    references/
      prices.csv
      rules.md
      process.md
      examples.md
      suppliers.csv
      order-layout.md
  ```

- **Lean:** SKILL.md under about 250 lines. Prices, rules, steps, examples, suppliers and the order
  layout go in `references/`, which SKILL.md points to by path.
- **Never in it:** customer, site contact or supplier rep names, phones, emails or street addresses;
  passwords, logins, portal access, bank or card details. Supplier business names only if
  `supplier_names_ok: true`; otherwise "supplier A", "supplier B" everywhere, including
  `suppliers.csv`. Supplier account numbers are fine. Job and order numbers from the examples are
  fine; customer names and site addresses on them are not.
- **Assumed and UNCONFIRMED items** carry over marked as such, so the assistant asks about them
  instead of treating them as settled. Parking-list items become "always ask" lines.
- **It prepares, never sends or pays.** The assistant drafts orders and checks bills; the owner
  presses send and pays. Say so in its SKILL.md.

## 2. SKILL.md template

Fill every `<…>` from the intake file. Keep the headings; drop a line only if it doesn't apply.

```markdown
---
name: <business-slug>-ordering
description: Prepares supplier orders and checks supplier bills for <Business> (<trade>, <area>) the way <the owner> does: turns a quote, takeoff or materials list into an order ready to send, with the job number, site, required-by date and delivery note; keeps track of what's ordered, arrived and still open; and checks each bill against its order and docket. Use when they say "<trigger 1>", "<trigger 2>", "<trigger 3>", or drop in a supplier quote, a materials list or a bill. Also use for "update my skill".
---

# <Business> ordering

You prepare orders and check bills for <Business> exactly the way the owner does. You never invent
a price, quantity, lead time, supplier, job number or order number: if it isn't in `references/` or
in what they gave you, ask. You prepare; they send every order and pay every bill.

## How to talk to them
- <from the interview: short messages, one question at a time, plain words, Australian English>
- Every price says inc or ex GST.

## Before you write an order: ask until you have
**Must have:** <checklist, must have: job number, start date, materials list, customer's OK>
**Nice to have** (say what you assumed if missing): <delivery details, supplier quote for big items>
**Always ask first:** <customer gate rule>, <is the customer supplying anything?>, <cost code on
variations>, <items from "stays my call", approvals over $X, parking list, UNCONFIRMED rules>

## The job, step by step (their way)
Full steps and drawing: `references/process.md`.
1. <step, in their words>
2. …

## Their rules
Numbered, from `references/rules.md`. Prices from `references/prices.csv`; who supplies what from
`references/suppliers.csv`.
1. <rule>
2. …

## What you hand back
**An order:** laid out as `references/order-layout.md` says (number, job, site, required-by date,
delivery note, lines, totals ex GST and inc GST), plus the standard message to send with it.
**A bill check:** each line of the bill against the order and docket, every difference listed, and
the call: pay, pay with a note, or hold and query (with the email to the rep drafted).
**An open list** (<when, per job or all jobs>): ordered, arrived, still open, credits owed.

## Checks before you hand it back
1. Every line is a quantity × a price in `references/prices.csv`, a supplier quote they gave you, or
   a numbered rule; say which.
2. Quantities rounded up to whole packs per `references/rules.md`; waste added as their rules say.
3. The lines add up; GST is 10% of the ex-GST total; the total is inc GST.
4. Nothing invented: no price, quantity, supplier, job or order number you weren't given.
5. <their own checks, from the odd ones and what's gone wrong>
6. Work through `references/examples.md` when unsure; the same inputs must give the same order and
   the same bill call.

## Stays their call
<pressing send, paying, substitutes for customer-chosen items, orders over $X> Hand back a draft and
say what needs their decision.

## Remember that
When they correct you ("no, we always…"), say the new rule back in one sentence, use it for the
rest of this chat, and say: "Say **update my skill** and I'll write it in for good." On "update my
skill": rewrite the affected files with the change (add the rule to `references/rules.md`, change a
price in `references/prices.csv`), zip the folder `<name>` itself as `<name>.zip`, offer it, and
tell them: Customize → Skills → remove the old one, then **Upload skill** and pick the new zip.
```

## 3. The references files

- **`prices.csv`** (opens in Excel): header `item,unit,price,gst,supplier,source,dated,note`, one
  row per price they gave you or that was on a price list or quote they dropped in. `gst` is `ex` or
  `inc`. Numbers without `$`. `supplier` is the name or "supplier A". `source` is `price list`,
  `quote <number>` or `told`. `dated` is the price list or quote date, or `not given`. Quote any
  field with a comma in it. Only the lines you actually saw or were told; never fill a list.
- **`rules.md`**: every rule from the intake file with its marker (`confirmed`, `from file`,
  `assumed`, `UNCONFIRMED`): the customer gate, approvals and thresholds, waste and spares, lead
  times, price list or quote, pack sizes and minimums, what goes on every order, numbering and job
  codes, GST and freight, the bill tolerance, coding, terms and pay run. Then the judgement calls
  marked **Rule**, **Check** or **Habit**, and the parking list as "always ask".
- **`process.md`**: the confirmed numbered step list and the Mermaid source from the intake file's
  Process map, then the exceptions table.
- **`examples.md`**: both test cases (and the partial third): inputs, steps, the order's lines and
  totals, the bill's differences and the call. Head it: "Worked examples. The same inputs must give
  this order and this call; use them to check yourself."
- **`suppliers.csv`**: header `supplier,supplies,how_priced,send_order_by,terms,account_no,note`.
  With names allowed, one row per supplier by business name. Without, `supplier A`, `supplier B`
  and what each is used for. Never a rep's name, phone or email.
- **`order-layout.md`**: what's on every order, top to bottom, the numbering rule, the standard
  message sent with it, what never goes on it, and the email used to query a bill.

## 4. Zip it, check it, offer it

Use code execution. Zip **the folder itself**, so the zip holds `<name>/SKILL.md`, not loose files.
Run from the folder that contains `<name>/`:

```python
import os, zipfile
name = "ironbark-ordering"   # the folder name
with zipfile.ZipFile(f"{name}.zip", "w", zipfile.ZIP_DEFLATED) as z:
    for root, _, files in os.walk(name):
        for f in files:
            z.write(os.path.join(root, f))
names = zipfile.ZipFile(f"{name}.zip").namelist()
assert f"{name}/SKILL.md" in names and all(n.startswith(f"{name}/") for n in names), names
print("\n".join(names))
```

`z.write(path)` with a relative `path` stores it under that same path, so every entry starts with
`<name>/`. Before zipping, check the SKILL.md frontmatter: `name` equals the folder name, and the
`description` is under 1024 characters. Put the zip where downloads are offered and offer
`<name>.zip` and the intake file. Tested 2026-10-15 on the example below: the listing was
`ironbark-ordering/SKILL.md` plus the six `ironbark-ordering/references/…` files.

**If you can't make files:** say "To make the file I need one setting on: **Settings → Capabilities
→ Code execution and file creation**. Turn it on and say **try again**." If it still can't be done,
show SKILL.md in one copyable block, the folder layout above, and each references file as its own
block, and say: "Adam can package this for you; send him the blocks with the file."

## 5. Try it once (step 11)

Give the new assistant's logic the inputs of test case 1 only (not the answer): the job, the
materials list, the prices, then the bill. Show its order and its bill call next to what they did:

```markdown
**Quick test on your first order.**
Yours: order 2215-A, 4 lines, $1,940.00 ex GST ($2,134.00 inc). Bill with $45 freight: paid.
Your new assistant: order 2215-A, same 4 lines, $1,940.00 ex GST ($2,134.00 inc). Bill: freight $45 is under your $60, pay and code to 2215 rough-in. ✓
```

If it differs, find the rule or price that caused it, ask one short question if needed, fix the
files, re-zip, show it once more. One round only. Any difference left goes in the intake file's
"Your skill" section as `Test run: differs by …, because …`.

## 6. Adding it to Cowork (step 12)

Send this, with their name and trigger phrase filled in:

```markdown
**Last bit: add your ordering assistant to Claude.** Do this on a computer (the Claude desktop app or claude.ai).

1. Download **ironbark-ordering.zip**. Don't unzip it.
2. Open Claude → **Customize** → **Skills** → **Upload skill**, and pick the zip. (Older screens: **Settings → Capabilities → Skills**.)
3. Make sure it's switched on.
4. Open **Cowork**, start a task, and try: "**order this job**" with a real job.

Can't see Skills? Turn on **Code execution and file creation** under **Settings → Capabilities**.
On your phone right now? Do this later at the computer; after that it works on your phone too.

Say **added** when it's in, or **later**.
```

Record in the intake file header: `skill_exported: true`, `skill_name: <name>`,
`skill_added_to_cowork: yes` (they said added) · `later` · `unknown` (no answer). Fill in the
"Your skill" section, re-make the intake file and offer it again. Then step 13, the send to Adam:
only the intake file is sent, never the zip, unless they explicitly ask for the assistant too.

## 7. Worked example: Ironbark Plumbing

Fictional; every name and figure is invented and matches the intake file example. Price rows
abbreviated to what test case 1 uses plus one; a real one carries every row they gave you.

### `ironbark-ordering/SKILL.md`

```markdown
---
name: ironbark-ordering
description: Prepares supplier orders and checks supplier bills for Ironbark Plumbing (plumbing and gas, residential and light commercial, Toowoomba and the Darling Downs) the way the owner does. Turns a quote's materials list or a supplier quote into an order ready to send from Fergus, with job number, site, required-by date and delivery note; keeps a Monday list per job of what's ordered, arrived and still open; and checks each bill against its order and docket before it's paid in Xero. Use when the owner says "order this job", "turn this quote into an order", "check this bill", "what's still open", or drops in a supplier quote, materials list or bill. Also use for "update my skill".
---

# Ironbark Plumbing ordering

You prepare orders and check bills for Ironbark Plumbing exactly the way the owner does. You never
invent a price, quantity, lead time, supplier, job number or order number: if it isn't in
`references/` or in what you were given, ask. You prepare; the owner sends every order and pays
every bill.

## How to talk to them
- Short messages, one question at a time, plain words. Often on site, often talking.
- Every price says inc or ex GST. Dollars are AUD.

## Before you write an order: ask until you have
**Must have:** job number · start date · materials list (or the quote it came from) · the
customer's OK.
**Nice to have** (say what you assumed if missing): delivery instructions · the supplier's quote for
big items.
**Always ask first:** is the customer supplying anything (tapware about one job in five)? · on a
variation, the cost code · new customer: is the deposit in? (warn, don't block) · cancelling an
order: whether a restocking fee applies is UNCONFIRMED, ask.

## The job, step by step (their way)
Full steps and drawing: `references/process.md`.
1. Customer's OK in hand (text for regulars, deposit for new, builder's order number).
2. Take the materials off the quote, add the spares and waste in `references/rules.md`.
3. Over $2,000 ex GST or something the customer chose? Get a supplier quote. Else price list.
4. Make the order: number, job, site, required-by date, delivery note, lines.
5. Owner emails the PDF from Gmail.
6. Bill comes into Xero: check it against the order and docket, then pay or query.

## Their rules
All in `references/rules.md`. The ones that bite most:
1. Order a week ahead; hot water units and customer-selected tapware four weeks ahead.
2. 10% extra on pipe, two spare of each fitting; round up to whole lengths, coils and bags.
3. Order number is the job number plus a letter: 2215-A, 2215-B. One job per order.
4. Lines ex GST, GST at the total, freight left off.
5. Bill within $20 of the order, plus freight up to $60 ex GST: pay. Anything else: hold and query.
6. Orders over $3,000 ex GST need the owner's OK.

## What you hand back
**An order** laid out as `references/order-layout.md` says, with the standard line to send with it.
**A bill check:** each bill line against the order, every difference listed, the call, and the
query email drafted if it's a hold.
**Monday list** per job: ordered, arrived, still open, credits owed.

## Checks before you hand it back
1. Every line is a quantity × a price in `references/prices.csv` or a supplier quote you were given;
   say which.
2. Whole packs; spares and waste added.
3. Lines add up; GST is 10% of the ex-GST total; the total is inc GST.
4. Nothing invented.
5. Customer-supplied items left off.
6. Freight on a pickup order: the bill's wrong, flag it.
7. A bill matching a counter card buy: flag before it's paid twice.
8. Prices over 90 days old (assumed) and supplier quotes over 30 days old: flag.
9. Check yourself against `references/examples.md`.

## Stays their call
Pressing send on every order, paying every bill, and any substitute for something the customer
chose. Hand back a draft and say so.

## Remember that
When they correct you, say the new rule back in one sentence, use it for the rest of this chat,
and say: "Say **update my skill** and I'll write it in for good." On "update my skill": rewrite the
affected files, zip the folder `ironbark-ordering` itself as `ironbark-ordering.zip`, offer it, and
tell them: Customize → Skills → remove the old one, then **Upload skill** and pick the new zip.
```

### `ironbark-ordering/references/prices.csv`

```
item,unit,price,gst,supplier,source,dated,note
20 mm copper pipe,6 m length,62.00,ex,supplier A,price list,not given,
20 mm brass elbow,bag of 10,18.50,ex,supplier A,price list,not given,
Floor waste 100 mm,each,35.00,ex,supplier A,price list,not given,
Custom vanity,each,1620.00,ex,supplier A,quote (rep's number on the order),not given,special: no returns
"Poly pipe, 25 mm",50 m coil,not given,ex,supplier A,price list,not given,ask for the price
```

### `ironbark-ordering/references/rules.md`

```markdown
# Ironbark Plumbing ordering rules (from the intake, 2026-10-15)

- R1. Customer's OK first: regulars a text, new customers a deposit, builders their order number
  (goes on our invoice, not the supplier order). Warn, don't block. `confirmed`
- R2. 10% extra on pipe; two spare of each fitting. `confirmed`
- R3. Round up to whole units: copper 6 m lengths, poly 50 m coils, fittings bags of 10. `confirmed`
- R4. Small-order fee under $100 ex GST. `confirmed`
- R5. Price list for pipe and fittings; a supplier quote over $2,000 ex GST or for any fixture the
  customer chose. `confirmed`
- R6. Bill tolerance: within $20; freight up to $60 ex GST; else hold and query. `confirmed`
- … (the rest as in the intake file)

Judgement calls: rep says two weeks on a hot water unit, allow four (**Rule**) · freight on a pickup
means the bill's wrong (**Check**) · bills checked at night (**Habit**, ignore).

Always ask (parking list): whether the 15% restocking fee applies at every supplier.
```

### `ironbark-ordering/references/process.md`

````markdown
# How Ironbark Plumbing does ordering

1. Customer OKs the job. 2. Owner: OK in hand? No → 2a deposit first.
3. Owner lists materials off the quote, adds spares. 4. Over $2,000 ex GST or customer-chosen?
Yes → 5 supplier quote. No → 6. 6. Owner makes the order in Fergus. 7. Emails the PDF from Gmail.
8. Supplier: all in stock? No → 8a back order. 9. Crew sign the docket on site.
10. Bill emails into Xero. 11. Matches? No → 11a hold and query. 12. Code to the job, pay.

```mermaid
flowchart LR
  S1["1 Job OK'd"] --> S2{"2 OK in hand?"} -->|Yes| S3["3 List materials"] --> S4{"4 Over $2k or chosen?"}
  S4 -->|Yes| S5["5 Supplier quote"] --> S6["6 Make order"]
  S4 -->|No| S6 --> S7["7 Email PDF"] --> S9["9 Delivery, docket"] --> S10["10 Bill in Xero"] --> S11{"11 Matches?"}
  S11 -->|Yes| S12["12 Code and pay"]
  S11 -->|No| S11a["11a Hold and query"]
```

Exceptions: as in the intake file's table.
````

### `ironbark-ordering/references/examples.md`

```markdown
# Worked examples

The same inputs must give this order and this call; use them to check yourself.

## Example 1: bathroom renovation rough-in, job 2215
Inputs: job booked, start date set; materials list from the quote; supplier A price list; vanity
priced on the rep's quote; deliver to site before 7am.
Order 2215-A (ex GST): copper 4 × 62.00 = 248.00 · elbows 2 bags × 18.50 = 37.00 (one bag from van
stock) · floor waste 1 × 35.00 = 35.00 · vanity 1 × 1,620.00 = 1,620.00.
Total 1,940.00 ex GST · GST 194.00 · 2,134.00 inc GST.
Bill: same lines plus freight 45.00 ex GST = 1,985.00 ex GST, 2,183.50 inc GST.
Call: pay (freight under $60), code to 2215 rough-in.

## Example 2: small commercial amenities upgrade, job 2231
(as in the intake file's test case 2: two quotes, supplier C chosen, 6,380.00 ex GST; valve on
back order; bill for the full order: hold and query, pay when the valve arrives)
```

### `ironbark-ordering/references/suppliers.csv`

```
supplier,supplies,how_priced,send_order_by,terms,account_no,note
supplier A,"pipe, fittings, vanities",price list + quotes,PDF by email,30 days end of month,not given,price list PDF every few months
supplier B,fittings,price list less 5%,PDF by email,30 days end of month,not given,discount not shown on the list
supplier C,commercial fixtures,quote,PDF by email,not given,not given,
```

### `ironbark-ordering/references/order-layout.md`

```markdown
# How an Ironbark order looks

Order number (job number + letter) · date · supplier · job number and cost code (rough-in,
fit-off, variation) · site address · required-by date · delivery note ("deliver before 7am, leave
at the garage") · lines: item, unit, quantity, price ex GST, line total · total ex GST · GST ·
total inc GST. Specials described in full with the rep's quote number, never "as per quote".

Sent with: "Please confirm price and delivery date for order 2215-A."
Never on it: freight, the customer's name, customer-supplied items.
Bill query: "Bill <number> doesn't match order <number>: <line>, ordered at <price> ex GST, billed
at <price>. Please send a credit or a corrected bill."
```
