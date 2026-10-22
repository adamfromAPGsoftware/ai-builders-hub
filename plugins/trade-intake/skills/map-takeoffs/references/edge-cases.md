# The odd ones: a quick-fire sweep of what can go sideways on a takeoff

Run this in **Part 6**, after the exceptions pass (Q24). It catches the cases a happy-path walk-through
never shows, and it's where most of what a tool gets wrong comes from.

## How to run it

- **Quick-fire, not an interview.** One group per message. Show the group's lines as a numbered list
  and ask: **"Which of these happen to you? Just the numbers, and a few words on what you do. 'None'
  is fine."** _(e.g. "2 and 4. Scans: I print and count by hand. Not to scale: I ring the builder.")_
- **Skip anything already covered.** Before sending a group, strike out every line their files or
  earlier answers already settled, and say so in one line: "Already got revisions and missing prices
  from earlier, so just three here." If a whole group is covered, skip it and don't count it.
- **Each group counts as one question** toward the 35, however many lines it has. A follow-up on a
  line counts as one more, so only follow up where the answer changes what the tool must do.
- **Order.** Groups marked ★ first. If you're close to 35, ask the ★ groups and put the rest down as
  `not asked (question limit)`, with the default below marked `(assumed)`.
- **"Not sure" or "never thought about it"** is fine: write the default from the line and mark it
  assumed. If someone else would know (the office manager, the leading hand), put it on the parking
  list with who can answer.
- **Rules come out of this.** When a line happens, read the rule back: "So: an 'existing' light is
  never counted. Right?"
- The example answers are from the made-up _Kurrajong Fitouts_.

## The groups

### 1. ★ Missing or wrong info at the start

1. A page or a whole trade's sheet is missing from the set
2. The spec says one thing and the drawing says another
3. No proper drawings at all: you measure on site, work off a sketch or a fire escape plan
4. The builder wants a price on "the usual" with no detail
5. What the builder asked you to price isn't clear (which areas, which trades, supply only or supply and install)

Default for the tool: list every gap as a question for the builder and an assumption line for the
quote; never fill a gap silently.
_(e.g. "1 and 2. If a sheet's missing I price what I've got and list it. Spec wins over the drawing.")_

### 2. ★ The drawings themselves

1. Scans or photos, not proper PDFs
2. "Not to scale", or the scale on the title block is wrong
3. Sheets not labelled, or one giant PDF with everything in it
4. Two sets both called "final", or the revision box doesn't match the revision table
5. Tiny text you can't read, or symbols printed on top of each other
6. CAD file only, no PDF

Default: scans and unreadable sheets are flagged for a hand count, never guessed; scale is checked
against a second dimension on every sheet; the newest revision is used and named on the takeoff.
_(e.g. "1 and 4. About 1 in 10 is a scan; I print it and count with a highlighter.")_

### 3. ★ Counting traps

1. The schedule on the drawing doesn't match what's on the plan
2. A symbol that isn't in the legend, or two symbols that look nearly the same
3. The same item shown on two sheets (lighting plan and ceiling plan), so it could be counted twice
4. Items marked "existing", "by others" or "future"
5. A run or wall shared between two areas
6. Only part of a level is in your scope
7. "Typical floor" drawn once but there are four of them

Defaults: count the plan and flag where the schedule differs; an unknown symbol is shown and asked
about, never counted or dropped silently; existing / by others left out and listed; a shared run is
counted once and flagged; a typical floor is multiplied and the multiplier shown.
_(e.g. "1, 3 and 4. Downlights show on two sheets, I only count the ceiling plan.")_

### 4. Different kinds of job

1. Tiny jobs (one tenancy, a few points) done differently from big ones
2. Shop vs office vs medical or food: different items or rules
3. Rush jobs: "need it by Friday"
4. A regular builder who wants it laid out their way
5. Design and construct, where you do the layout yourself rather than count someone else's
6. Insurance or make-safe work
7. Staged jobs priced one stage at a time

Default: one way of doing it, with the differences written as rules (e.g. "under 20 points, no tray
measure, use an allowance").
_(e.g. "1 and 4. Small shops I do in my head off the plan. One builder wants it split by stage.")_

### 5. ★ Prices and calls you make

1. An item with no price in your list
2. Prices that are old, or a supplier's gone up since
3. Out of stock or long lead time, so you price something else
4. Swapping in your preferred brand for what's specified
5. Deciding whether to quote at all (too small, too far, wrong builder)
6. Are these calls written down anywhere, or just in your head?

Defaults: a missing price is highlighted and asked about, never borrowed from a similar item; a
substitute is shown as a substitute; go/no-go stays with the owner.
_(e.g. "1, 2 and 6. Missing prices I ring the supplier. It's all in my head.")_

### 6. Who signs off, and who covers

1. Any takeoff or price over a certain amount that someone else has to check
2. Who does it when you're away or flat out
3. Anything only you know how to do (and isn't written down)

Default: the owner checks everything; anything only the owner knows goes in the file as a rule.
_(e.g. "1: over $50,000 ex GST my business partner looks at it. 3: the labour hours.")_

### 7. ★ Changes and redoing it

1. Revised drawings after you've priced (rev B, rev C)
2. An addendum or RFI answer that changes the scope
3. The builder asks for options or a re-price ("what if we drop the data?")
4. You find a mistake after the quote's gone
5. After you win it, the takeoff is redone for ordering or on site

Default: on a revision, a fresh takeoff plus a list of what changed against the last one; the
output grouped so the site team can use it.
_(e.g. "1 and 5. Rev B always comes. The leading hand redoes the cable for ordering.")_

### 8. Timing and busy times

1. Tender closing dates you can't move
2. Quotes or supplier prices that expire
3. Chasing the builder for answers, or chasing suppliers for prices
4. Takeoffs done at night or on weekends
5. Busy times of year, and what gets dropped when you're flat out

Default: the tool shows the due date and anything still waiting on someone.
_(e.g. "3, 4 and 5. Nights mostly. In the run to Christmas I knock back small jobs.")_

### 9. ★ Typing it twice, and messy lists

1. Counts typed from the drawing into a spreadsheet, then again into your job software
2. The same item called different things in the price list, the drawing and your job software
3. Double-ups in the price list, or two price lists and you're not sure which is right
4. Units that don't line up (price per 100 m drum, takeoff in metres)

Default: one name per item, with a list of the other names it goes by; one price list is the right
one; units converted and shown.
_(e.g. "1, 2 and 4. 'GPO', 'DPP' and 'double power point' are all the same thing.")_

### 10. Money and GST

1. Some suppliers' prices are inc GST, some ex
2. Freight or delivery worked out per job, per drop, or not at all
3. The builder wants it split for progress claims, or holds back retention
4. Supplier trade terms or discounts that aren't on the price list
5. Rounding the final price (to the nearest $10, $50, $100)

Default: everything worked in ex GST, GST added once at the end and shown; extras as their own lines.
_(e.g. "1 and 5. One supplier's list is inc GST. I round the total to the nearest $50.")_

### 11. When it goes wrong, and when it's done

1. You lose your place (interrupted, file crashes, Bluebeam won't open the PDF)
2. You only find out it was wrong on site (short on cable, a fixture missed)
3. What "done" looks like: who gets told, and what they get
4. Keeping a copy: where the finished takeoff and drawings are saved

Default: the tool saves progress sheet by sheet; "done" is the quote sent and the takeoff saved with
the job.
_(e.g. "1 and 2. Found out we were 3 lights short on site once. Done is when the builder has the quote.")_

## How it goes in the file

Fill the **Odd ones and exceptions** table in the file: one row per line that happens, with what they
do now and what the tool should do. Lines that don't happen aren't listed. Groups not asked are listed
once as `not asked (question limit)` with their defaults marked `(assumed)`. Every "don't know" goes on
the **Open items** list with who can answer it.
