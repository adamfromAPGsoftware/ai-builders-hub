# The quick-fire sweep: the odd ones in customer messages

Run this in Part 6 (Q23 to Q26), after the normal way is down and the step-by-step "is it always
like this?" (Q22) is done. Its job is to catch the cases an assistant gets wrong because nobody
thought to mention them.

## How to run it

- **Four rounds, one message each.** Each round counts as **one** question toward the 35.
- **Drop any line already covered** by their messages or earlier answers. If a whole round is
  covered, skip it and say so in one line. Skip round 2 if they don't get orders.
- Show the round as a short numbered list in plain words, then ask: **"Which of these happen to
  you? Just say the numbers, and a word on what you do."**
- Lines they don't pick are recorded as `doesn't happen`. Lines they pick get **one line** each in
  the map file. Only if a pick opens a new rule, ask **one** short ↳ follow-up (it counts).
- Don't explain the lines. If they ask "what do you mean?", give the Tallowood example.
- Start the round with its name, e.g. `Odd ones, round 2 of 4 · orders that aren't the usual`.

Examples in italics are from the made-up business, Tallowood Painting.

## Round 1 of 4 · where and when messages arrive (Q23)

1. **Wrong place:** a message to someone's personal email, a text to the wrong person, a voicemail
   nobody listens to? _(Property managers sometimes email the old office address.)_
2. **After hours:** messages at night or on weekends: who sees them, and when? _(Texts at 9pm; I
   answer from the couch.)_
3. **Duplicates:** the same order sent twice, or by email and the portal? _(One property manager
   emails and uploads to the portal.)_
4. **Forwarded chains:** the real question buried in a long thread? _(Builders forward the whole
   thread.)_
5. **Attachments only:** a photo or PDF with no words? _(Homeowners text a photo of a crack.)_
6. **Voice and calls:** orders or questions by phone that never get written down? _(Half my changes
   come by phone.)_
7. **Busy weeks:** what gets missed when you're flat out? _(The inbox, for days.)_

## Round 2 of 4 · orders that aren't the usual (Q24)

1. **Missing info:** no address, no contact, no reference number, no date? _(Tenant number missing
   on one in five.)_
2. **Over a limit:** more than the customer's approved amount, or their budget? _(Over the
   not-to-exceed, I ring first.)_
3. **Their codes, not yours:** descriptions or item codes you translate to your own? _("Bed" means
   bedroom up to 12 m².)_
4. **Changes after it's entered:** extra rooms, a new date, cancelled? Same job or a new one?
   _(Same job, a note in Tradify, if I remember.)_
5. **Several jobs in one message:** or one job split over several messages? _(End-of-lease batches:
   five units in one email.)_
6. **Urgent:** a leak, damage, a tenant moving in tomorrow? _(I ring straight away.)_
7. **Repeat orders:** the same thing again for the same customer? _(Same scope every lease change.)_
8. **Prices on the order:** the customer's price differs from yours? _(Their rate sheet is a year
   old.)_

## Round 3 of 4 · answers and promises (Q25)

1. **Only in your head:** answers nobody else can give? _(Whether we move furniture.)_
2. **Old answers:** a price, colour or product that's changed since? _(Rates went up in July.)_
3. **Promising dates:** who can promise a date, and what happens when it slips? _(Only me. When it
   rains, I text everyone the night before.)_
4. **Prices in a reply:** who can give a price by message, and when must it be a proper quote?
   _(Extra room: the office can say the rate. Anything else: a quote.)_
5. **Complaints:** who handles them, how fast, and what's never said in writing? _(Me, by phone,
   never by text.)_
6. **Tone:** different for homeowners, builders and property managers? _(Property managers formal,
   homeowners friendly.)_
7. **Not our job:** questions about another trade's work, or work you don't do? _(Plastering: we
   recommend someone.)_

## Round 4 of 4 · people, records and when things break (Q26)

1. **If the office person is away for two weeks:** who picks up, and what only they know? _(Nobody.
   Only my partner knows the property managers' quirks.)_
2. **Typing it twice:** every place an order or answer gets typed again (email → job software →
   invoice)? _(Work order into Tradify, then again into the Xero invoice.)_
3. **Where the truth lives:** if the email, the job software and what you said on the phone
   disagree, which wins? _(What I said on the phone, which nobody wrote down.)_
4. **Lost messages:** ever found one weeks later? _(The work order we missed.)_
5. **Nobody told:** the customer, the crew or the office didn't hear about a change? _(Crew turned
   up to a cancelled job once.)_
6. **When it breaks:** inbox full, job software down, phone lost? _(Lost my phone; lost a week of
   texts.)_

## Where the answers go

In the map file's **Exceptions and odd ones** table (see `map-file.md`): one row per line they
picked, with the step it touches, what they do now, any rule or check it creates, and where it came
from (`sweep 1`, `Q22`, `test case`). Lines not picked are summed up in one sentence ("Didn't
apply: …"). Anything that creates a check also goes under **Checks for your assistant**, and each
exception that changes a step goes in that step's `odd_cases` on the map.
