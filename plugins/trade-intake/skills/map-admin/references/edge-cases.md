# The quick-fire sweep: the odd ones in the office

Run this in Part 6 (Q22 to Q25), after the normal way is down and the step-by-step "is it always
like this?" (Q21) is done. Its job is to catch the cases an assistant gets wrong because nobody
thought to mention them.

## How to run it

- **Four rounds, one message each.** Each round counts as **one** question toward the 35.
- **Drop any line already covered.** Skip round 2 if they have no staff. Say so in one line.
- Show the round as a short numbered list, then ask: **"Which of these happen to you? Just say the
  numbers, and a word on what you do."**
- Lines they don't pick are recorded as `doesn't happen`. Lines they pick get **one line** each in
  the map file, by role and by kind, never by name. Only if a pick opens a new rule, ask **one**
  short ↳ follow-up (it counts).
- Start the round with its name, e.g. `Odd ones, round 2 of 4 · the pay run`.

Examples in italics are from the made-up business, Tallowood Painting.

## Round 1 of 4 · bills and suppliers (Q22)

1. **No order to check against:** bills for things nobody ordered in writing? _(Counter buys on
   card.)_
2. **Duplicates:** the same bill emailed twice, or a bill and a statement both paid? _(Paid supplier
   A twice in July.)_
3. **Price creep:** the bill's higher than the quote or price list? _(Paint went up 6% in March.)_
4. **Freight and extras:** delivery, small-order or card fees you didn't expect? _(Freight on a
   pickup order.)_
5. **Credits owed:** returns or short deliveries waiting on a credit? _(Two open right now.)_
6. **Receipts:** card receipts that live on one phone? _(Mine.)_
7. **Subcontractors:** invoices from subbies that need ABN, insurance or a statement first? _(One
   plasterer we use.)_

## Round 2 of 4 · the pay run (Q23)

By role only. Never a name or anyone's pay.

1. **Late or missing hours:** someone doesn't send hours on time? _(Every second week.)_
2. **Different rates:** apprentices, casuals, overtime, weekend work, allowances? _(Apprentice rates
   change each year.)_
3. **Leave:** annual, sick or rostered days off sorted by hand? _(In a notebook.)_
4. **Hours on the wrong job:** hours that should be costed to a job but aren't? _(Never costed.)_
5. **New starters and leavers:** set up or finished in several places? _(Xero, super, the tools app.)_
6. **Public holidays and shutdowns:** the Christmas break, a rained-off week? _(Christmas, by hand.)_

## Round 3 of 4 · invoicing and getting paid (Q24)

1. **Invoices never sent:** a job finished but nobody told the office? _(Once a month.)_
2. **Progress claims and retention:** builders who pay on claims, or hold back retention? _(Builder A
   holds 5%.)_
3. **Disputes:** a customer won't pay until something's fixed? _(One now.)_
4. **Slow payers:** customers who always pay late, and what you do? _(Two builders, 60 days.)_
5. **Deposits:** deposits taken and matched to the final invoice? _(20% on homeowner jobs.)_
6. **Bad debts:** a debt you gave up on? _(One last year, $3,000.)_

## Round 4 of 4 · people, records and when things break (Q25)

1. **If the office person is away for two weeks:** who pays bills and runs the pay run, and what only
   they know? _(Nobody; my partner knows the supplier logins.)_
2. **Typing it twice:** every place a number gets typed again (bill → Xero → bank → Drive)? _(Three
   places for every bill.)_
3. **Where the truth lives:** if Xero, the bank and the paper disagree, which wins? _(The bank.)_
4. **Lost paperwork:** dockets, receipts or bills that go missing? _(Dockets in the ute.)_
5. **BAS and the accountant:** a scramble before BAS? _(Every quarter.)_
6. **When it breaks:** the bank feed stops, the payroll app is down? _(Bank feed broke for a week.)_

## Where the answers go

In the map file's **Exceptions and odd ones** table: one row per line they picked, with the step it
touches, what they do now, any rule or check it creates, and where it came from (`sweep 1`, `Q21`,
`test case`). Lines not picked are summed up in one sentence ("Didn't apply: …"). Anything that
creates a check also goes under **Checks for your assistant**, and each exception that changes a
step goes in that step's `odd_cases` on the map.
