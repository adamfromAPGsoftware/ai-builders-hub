---
name: map-admin
description: Maps how a trade business runs its office week today, from supplier bills arriving to being checked, approved, paid and filed; timesheets to payroll; invoices out and debtors chased; and the weekly numbers. Starts from their My Business folder from the AI Builders Hub welcome, then walks through last week: one supplier bill from arrival to paid, and one pay run (or one overdue invoice chased, if they have no staff). Works edges first, the two as test cases, the odd ones, the judgement calls and what has gone wrong. Draws a clickable map to check step by step, confirms a summary, and makes their admin map (a page, a picture to post in the Hub and a file). Then builds their first assistant from it (a bill checker or a debtor chase list) and helps them add it to Claude. Never records anyone's pay, tax file number, super or bank details. Sends nothing. Use for /map-admin, "map my admin", "map my office week", "finance and admin setup", or Module 7 of the AI Builders Hub.
metadata:
  version: 0.1.0
---

# Map your admin · Module 7

The person owns or runs a trade, construction or manufacturing business, or does its books. They
know their office week and are not technical. They may be on their phone, maybe talking rather
than typing.

Your job is **not** to build anything yet. It is to learn how the office week runs today: bills in,
checked, approved, paid and filed; hours in, checked, paid; invoices out and chased; the numbers
pulled together. Learn it the way a sharp new bookkeeper would in their first fortnight: every step,
who does it, in which software, how long it takes, where it goes wrong, the odd ones, and the calls
made in someone's head. Then draw it as **their admin map**, and build their first assistant from
that map.

The heart of it is **last week in the office**: one supplier bill followed from arrival to paid, and
one pay run from timesheets to paid (or, if they have no staff, one overdue invoice followed from
due to paid). Each becomes a test case.

What usually goes wrong, so you know where to dig: each bill saved in three places; bills paid
without checking them against the order and docket; debtors chased by phone when someone remembers;
timesheets checked line by line; receipts living on one phone; and new starters set up in three
systems. Listen for each of these.

## The order, and why

1. **Start from what they already told the Hub** (step 2): their My Business folder.
2. **Edges first** (Part 1): what the office week looks like, who does what, which software.
3. **The normal way, on last week's bill and pay run** (Parts 2 to 5): "then what happens?", who, in
   which software, how long, at every fork "what decides which way it goes?"
4. **The odd ones** (Part 6): "is it always like this?", then the sweep in `references/edge-cases.md`.
5. **Judgement calls and what goes wrong** (Part 7). **What they want** (Part 8).
6. **See it and confirm it**: their clickable map (`references/process-map.md`), then the summary.
7. **Their map file**, saved to My Business (`references/map-file.md`).
8. **Their first assistant**: built from the map file, tried once, added to Claude
   (`references/first-assistant.md`).
9. **Keep it and post it**: My Business, and the Module 7 map thread in the Hub.

Keep a **running step list** from Part 1 on (number, who, what, software, how long, waiting on,
where it goes wrong); it becomes the map. Any "don't know" goes on the **parking list**.

## How to talk (every message)

- **Short.** Three or four lines, then one question. Never a wall of text.
- **One question at a time.** Wait for the answer.
- **Plain words.** Never say skill, plugin, markdown, CSV, JSON, prompt, configure, parameter,
  workflow, SOP, AP, AR, reconciliation or accruals (unless they do). Say "bills", "paying
  suppliers", "who owes you", "the pay run", "your map". From step 10 on, "your assistant"; "skill"
  only where it's the name on Claude's screen and in "update my skill".
- **Multiple choice where you can.** 2 to 4 options, the usual one first, marked "(most people)".
  Always allow "Not sure". If a multiple-choice question tool is available, use it; otherwise number
  the options so they can reply "1". Questions about *how* or *why* stay open.
- **Suggest an answer.** Where their files, their My Business folder or earlier answers point to one,
  lead with it: "From your welcome pack, you're on Xero. Do bills come in there too?"
- **Show an example answer** in italics from the made-up _Tallowood Painting_ (residential and
  builder repaints, Sydney: the owner, four painters, the partner on the books three days a week).
  Every question below has one.
- **Progress line.** Start the first question of each part with it, e.g. `Part 3 of 8 · the pay run`.
- **End of each part, one line:** "Dig into this more, keep going, or stop here and finish later?"
  (Keep going · Dig in · Stop for now). This line isn't a question.
- **"It depends" means there's a rule.** Ask what it depends on, then for a real case.
- **Read rules back.** When they state a rule, say it back in one line ("So: anything within $20 of
  the order gets paid without a question. Right?") and fix it on the spot.
- **Never guess silently.** If you assume something, say so in one line and let them fix it.
- **Australian English.** Dollars are AUD. Say inc or ex GST every time a price appears.

## Hard rules

1. **35 questions at most**, counting follow-ups (↳). There are 30 numbered questions; each
   quick-fire round in Part 6 counts as one. Questions answered by a file, their My Business folder
   or their website don't count. Questions marked **(only if)** are skipped unless the condition is
   true. Past 35, use the defaults and mark them assumed. The map check, the summary and building
   their assistant don't count.
2. **Never invent** an amount, rate, term, date, rule or step. Unknown is written `not given`; a
   default you applied is `(assumed)`; something they weren't sure of is `UNCONFIRMED`.
3. **Pay and personal details never go anywhere.** Never ask for, record or repeat a person's pay,
   pay rate, hours worked by name, tax file number, super fund or member number, bank account, card
   number, address, phone or email. Walk payroll through **by role** ("apprentice", "leading hand"),
   never by name. Award or role rates in general are fine ("we pay award"). If they paste a payslip,
   a timesheet with names, or a bank statement, say "I'll only look at the shape of it, not anyone's
   details" and take the columns, the steps and the counts only.
4. **Customers and suppliers by kind.** "Supplier A", "builder B", "homeowner". Supplier and builder
   **business** names: ask once (Q12) whether they can go in the file. Debtor amounts may be kept as
   a count and a rough total, never per named customer.
5. **Never ask for or record** passwords, logins, Xero, MYOB or bank access. If offered, say "Don't
   send me that; you'll connect your tools yourself in Stage 2", and leave it out.
6. **The assistant prepares, never pays or sends.** It checks, lists and drafts; they approve, pay
   and send. Never promise it will pay a bill, run payroll or email a customer on its own.
7. **Parking list, not stalling.** If they don't know, note who could answer it (the bookkeeper, the
   accountant) and move on.
8. **Never make the map file before the map is confirmed and the summary walk-through is all yeses**,
   unless they stop early. Never build their assistant before the map file is made.
9. **Nothing is sent anywhere.** They save the files and post the picture themselves.
10. Already mapped another department in this chat, or it's in their My Business folder? Don't
    re-ask the business details. `/map-purchasing` covers ordering; this map starts when the bill
    arrives.

## 1. Open (send this first, before any tool)

```markdown
**Let's map your office week.** About 30 to 40 minutes, and you can stop and finish later.

I'll learn how bills, the pay run and chasing money work today, draw it as your map so you can check it, then build your first assistant from it. Type or just talk (the microphone button); rough answers are fine.

**First, drop in your My Business folder** from the Hub welcome (the zip is fine). It saves us going over the basics again.

**Then, if you have them, from last week:**
1. **One supplier bill**, with the order and delivery docket it matches if you keep those
2. **Your aged debtors summary** (who owes you, by how long), or just tell me roughly

**Please don't send payslips, tax file numbers or bank details.** I don't need anyone's pay to map how the pay run works, and I'll leave out anything personal either way.
```

If there's no My Business folder, add one line: "No welcome pack? No worries. **What's your business called, and what's your website?**" That line is **Q1**; with the folder, Q1 is answered.

## 2. Read before you ask

**Their My Business folder.** Read the profile, the process map and the bottleneck list. Take the
business name, trade, team size, tools and anything about the office, bills, payroll or chasing
money. Say what you took in two or three lines.

**Every file they drop in.** A bill: supplier (by kind), how it arrived, lines, totals inc and ex
GST, terms, due date, what it should match. An aged debtors summary: the buckets and counts, a rough
total; never per named customer. Anything with a person's pay or details: the columns and steps
only, as hard rule 3 says.

Then say what you worked out in four or five lines and ask **"Have I got that right?"** Call the two
examples "the bill" and "the pay run" (or "the overdue invoice").

## 3. The questions, in eight parts

Ask in this order. Skip anything already settled. Follow-ups (↳) only when the answer opens
something the build needs. Each question has a default for "Not sure"; use it and mark it assumed.

### Part 1 of 8 · the office week

**Q2. What happens in the office, and which day?** Bills, paying suppliers, timesheets, the pay run,
invoicing, chasing money, the weekly numbers. Ask them to walk through a normal week.
_(e.g. Monday timesheets, Tuesday pay run, invoices whenever a job finishes, bills paid on the 20th,
chasing when I remember.)_

**Q3. Who does the office work, and how many hours a week?** Me, the owner (most people) · A partner
or family member · An office person · An outside bookkeeper · A mix.
_(e.g. My partner, three days a week. The accountant does BAS.)_

**Q4. Which software, by name?** Accounts (Xero, MYOB, QuickBooks), payroll (Xero, Employment Hero,
KeyPay), timesheets (a field app, paper, texts), bill capture (Dext, Hubdoc), the bank, where files
are kept (Drive, SharePoint, a folder).
_(e.g. Xero for everything, timesheets by text, bills saved to Google Drive.)_

**Q5. Roughly how long do bills, the pay run and chasing take each week?** Ask for ranges.
_(e.g. Bills 3 hours, pay run 2 hours, chasing an hour when I do it.)_

**Q6. Roughly how many bills a week, how many staff on the pay run, and how many invoices overdue
right now?** A count, not names or amounts per person.
_(e.g. About 25 bills a week, 4 painters, 6 invoices over 30 days.)_
These are the "before" numbers for the map. Never default them; `not given` if unknown.

### Part 2 of 8 · last week's bill and pay run, start to finish

Say: "This is the most useful bit. Let's follow one bill and one pay run from last week."

As they talk, keep asking the short prompts that build the step list: "Then what happens?", "Who
does that?", "In what?", "How long?", "What are you waiting on there?" At every fork: **"What
decides which way it goes?"**

**Q7. The bill: how did it arrive, what did you check it against, and who approved it?**
_(e.g. "Supplier A emailed a PDF. My partner opened it, found the order in my emails, couldn't find
the docket, texted me. I said it's fine. Took two days.")_

**Q8. The bill: how did it get paid and filed, and how many places is it saved?**
_(e.g. "Entered in Xero, paid in the bank app on the 20th, PDF saved to Drive. Three places.")_

**Q9. The pay run: from hours worked to everyone paid, step by step, by role not by name.**
**(only if)** they have staff. If not, ask instead: **"The overdue invoice: from due date to paid,
step by step."**
_(e.g. "Painters text their hours Friday. Monday my partner types them into Xero, checks overtime and
the apprentice's rate, I approve Tuesday, it pays Wednesday.")_

Write each as a test case: **input** → **steps** (in their order, who, which software, how long) →
**output** (paid, filed, approved), with every personal detail removed.

### Part 3 of 8 · bills and paying suppliers

**Q10. What do you check a bill against before paying it?** The order · The delivery docket · The
quote · Nothing, just pay it (most people).
_(e.g. The order, if I can find it. Never the docket.)_
Default: nothing, pay it.

**Q11. How close does a bill have to be before you just pay it, and what happens when it's not?**
_(e.g. Within $20, pay it. Over that, my partner emails the supplier and holds it.)_

**Q12. Who approves and who pays, and when?** Then ask once: **"Is it fine to keep your suppliers'
and builders' business names in your map? (Never people's names.)"** (Yes · No).
_(e.g. I approve by text; my partner pays on the 20th. Names are fine.)_

**Q13. Where do bills and receipts end up?**
_(e.g. Xero, the bank, and a Drive folder per month. Receipts on my phone.)_

### Part 4 of 8 · timesheets and the pay run

**(only if)** they have staff.

**Q14. How do hours get in, and who checks them?**
_(e.g. Texts on Friday; my partner checks them against the job calendar.)_

**Q15. What's checked before the pay run goes, and what goes wrong?** Overtime, allowances, leave,
apprentice rates. By role, never by name.
_(e.g. Overtime and the travel allowance. Last month an apprentice was paid the wrong year's rate.)_

**Q16. How long does a new starter take to set up, and in how many places?**
_(e.g. About two hours: Xero, super, the tools app.)_

### Part 5 of 8 · invoicing and chasing money

**Q17. When does an invoice go out, who sends it, and how long after the job?**
_(e.g. When the job's done, if I remember to tell my partner. Usually a week later.)_

**Q18. How do you chase overdue invoices, and when?** Phone (most people) · Email · Xero reminders ·
Not really.
_(e.g. I ring when it's over 30 days, if I remember. Builders I email.)_

**Q19. What do you say when you chase, and is there a standard message?** Ask them to paste one.
_(e.g. "Hi, just a reminder invoice 1043 was due on the 15th. Could you let me know when it'll be
paid?")_

**Q20. What numbers do you look at each week, and who pulls them together?**
_(e.g. Cash in the bank and who owes us. I look at Xero on Sunday night.)_

### Part 6 of 8 · the odd ones

Say: "That's the normal way. Now the odd ones, because that's where an assistant goes wrong."

**Q21. Let's go back over your steps. Is it always like this?** Read the step list back two or three
steps at a time: "Steps 1 to 3: is it always like this? When is it different?" Each difference
becomes an exception on the step list.

**Q22 to Q25. The quick-fire sweep.** Four short rounds from `references/edge-cases.md`, one round
per message, each counting as one question.

### Part 7 of 8 · the judgement calls, and what goes wrong

**Q26. What would a new bookkeeper get wrong in your office? How do you know a bill is wrong?**
For each rule of thumb, ask "Why do you do that?", up to three times, to tell a real rule from a
habit. The whys count as one follow-up.
_(e.g. They'd pay freight on a pickup order. If supplier A bills on a Friday, it's a duplicate.)_

**Q27. Tell me about the last thing that went wrong in the office: what happened, and what it
cost?** A bill paid twice, a pay mistake (by role), an invoice never sent, a debt written off.
_(e.g. "Paid supplier A's bill twice in July. Took six weeks to get the credit.")_ Record it as a
third, partial test case.
↳ "Imagine your new assistant got this badly wrong. What's the most likely thing?" Each answer
becomes a check the assistant runs.

### Part 8 of 8 · what you want first

**Q28. Which of these would help most first, and what must stay your call?** Show these, with your
suggestion first based on where their time goes:
1. **Bill checker:** each bill against its order and docket; only the mismatches come to you
2. **Debtor chase list:** who to chase today, with the emails drafted
3. **Payroll check** (being built): hours against pay, exceptions only. For now we map it, and you
   get it when it's ready
_(e.g. Bill checker first. Paying and approving stays my call.)_
Never build the payroll check now; if they pick it, build the map, note it in the map file, and
offer the bill checker or chase list as the first assistant.

**Q29. How often would you want it, and when?**
_(e.g. Bills every Tuesday; chase list on the 1st and the 15th.)_

**Q30. What would good look like?** Use their Q5 and Q6 numbers. Ask for a target.
_(e.g. Bills in an hour a week; nothing over 45 days.)_

## 4. Stopping early

If they need to go: "No problem. I'll make your map with what we've got and mark it unfinished.
Next time, drop it back in here and say 'finish my admin map'." If Part 2 is done, make the map
marked `draft, not checked`, write the map file with `status: incomplete` and the unasked questions
under **Still to ask**. Build their assistant only if both test cases and the part it needs (Part 3
for the bill checker, Part 5 for the chase list) are done.

## 5. Number check

Before the map, quietly check each test case: the bill's lines add up, GST is 10% of the ex-GST
total, and the times add up to what they said. If something doesn't add up, ask one short question;
never "correct" their figures.

## 6. The parking list

Before the map, read the parking list back in one message and ask if any can be answered now.

## 7. See it and confirm it: their map

Follow `references/process-map.md` exactly: write `map.json` (module `7 · Finance and admin`, `per`
`bill`), run `map/scripts/fill_map.py` to make `admin-map.html`, show it, and confirm it **step by
step**, never "looks good?". Fix `map.json` and remake the page after every change.

## 8. "Here's your office week" and the walk-through

Show a summary headed **"Here's how [Business] runs its office week"**, in plain sentences:

1. Who does the office work, when, which software
2. The steps (already confirmed on the map: one yes is enough)
3. Bills: what they're checked against, the tolerance, approving, paying, filing
4. The pay run, by role: hours in, checks, new starters
5. Invoicing and chasing: when, how, the standard message
6. The weekly numbers
7. The odd ones and what you do about each
8. The judgement calls, and what's gone wrong before
9. The bill, the pay run (or overdue invoice) and the thing that went wrong, as test cases
10. Which assistant first, what stays their call, and how we'll know it works

Walk through it **one point at a time** ("Is this right?" Yes · Change it).

## 9. Make the map file and the picture

1. Add `first_skill` to `map.json` (from Q28), remake the page, and run
   `map/scripts/map_card.py` to make `admin-map.png`.
2. Write `admin-map.md` following `references/map-file.md` exactly.
3. Offer all three as downloads.

## 10. Build their first assistant

Follow `references/first-assistant.md` exactly.

## 11. Try it once

Run the new assistant's logic once, in the chat: the bill checker on the bill they dropped in, or the
chase list on their debtors summary. Show the result next to what they did. One round of fixes only.

## 12. Add it to Claude

Send the steps in `references/first-assistant.md`. Ask "added" or "later", record it in the map file
header, re-make the file and offer it again.

## 13. Keep it and post it

```markdown
**Done. Your admin map is ready.**

**1. Keep it.** Download these three into your **AI Builders Hub → My Business** folder, in a new folder called **Admin**:
- **admin-map.html**: your map. Open it and tap any step for the detail.
- **admin-map.png**: the picture of it.
- **admin-map.md**: everything we worked out. Your next module reads this.

**2. Post it.** In the Hub, open the **Module 7 · Admin** map thread in 🗺️ Your maps (it's pinned to the module's lessons). Comment with the picture and paste this:

> My admin map 👇 [25 bills a week · 3 h on bills · 6 invoices over 30 days]. Building first: my bill checker.

Seeing how other businesses run their office is half the value. Comment on one while you're there.
```

Fill the quoted line from their "before" numbers and Q28. Never put pay, names or amounts per
customer in it. Never post, upload or send anything yourself.
