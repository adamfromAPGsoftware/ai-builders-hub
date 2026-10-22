# Their first assistant (the skill they add to Claude)

Steps 10 to 12. Build **one** assistant, the one they picked at Q29, only from the confirmed map
file: nothing new, nothing invented, nothing they didn't approve. To them it's "your order reader",
"your answer finder" or "your job status replies". Say "skill" only where it's the name on Claude's
screen and in "update my skill". None of this counts toward the 35 questions.

| They picked | Folder name | It does | Tested on |
|---|---|---|---|
| Order reader | `<slug>-orders` | Reads an order or work order, pulls out what goes into their system, checks it against their rates and rules, flags what's missing, drafts the confirmation | Message 1 |
| Answer finder | `<slug>-answers` | Answers a customer question from their own info, says where each answer came from, drafts the reply; asks when it doesn't know | Message 2 |
| Job status replies | `<slug>-job-status` | Drafts "when are you coming / where's my order" replies from what they paste in or a connected job system, and the bad-news message when something slips | A status question from Q19 |

`<slug>`: the business name in lowercase, spaces to hyphens, letters, numbers and hyphens only, 64
characters at most (e.g. `tallowood-orders`). The SKILL.md `name` is exactly the folder name.

## 1. The folder

```
<name>/
  SKILL.md
  references/
    rules.md        every rule from the map file, with its marker
    replies.md      their standard replies, sign-off and tone, per kind of customer
    examples.md     the test cases: input, what was entered, the reply
    process.md      the confirmed step table from the map file
    rates.csv       (order reader only) item,unit,rate,gst,their_words,note
    answers.md      (answer finder only) the top questions and where each answer lives
```

- **Lean:** SKILL.md under about 200 lines; the detail in `references/`.
- **Never in it:** any customer, tenant, contact or staff name, phone, email or street address;
  passwords, logins, bank details. Company names only if `customer_names_ok: true`.
- **Assumed and UNCONFIRMED items** carry over marked, so it asks instead of treating them as
  settled. Parking-list items become "always ask" lines.
- **It prepares, never sends or enters.** It drafts; they check, enter and send. Say so in SKILL.md.

## 2. SKILL.md template

Fill every `<…>` from the map file. Keep the headings; drop a line only if it doesn't apply.

```markdown
---
name: <slug>-<orders|answers|job-status>
description: <What it does for Business, in one sentence, from the table above>, the way <Business> (<trade>, <area>) does it. Use when they say "<trigger 1>", "<trigger 2>", "<trigger 3>", or paste or drop in a customer message<, an order or a work order>. Also use for "update my skill".
---

# <Business> <order reader | answer finder | job status replies>

You <read orders | answer customer questions | draft job status replies> for <Business> exactly the
way they do. You never invent a price, rate, date, code, reference or answer: if it isn't in
`references/` or in what they gave you, ask. You draft; they check, enter and send.

## How to talk to them
- Short, plain words, Australian English. Every price says inc or ex GST.

## What to do with a message
1. <their steps for this kind of message, from `references/process.md`>
2. …

## Their rules
From `references/rules.md`. The ones that matter most here:
1. <rule>

## What you hand back
<Order reader: the fields to enter, in the order their software asks for them; anything missing or
over a limit, flagged; the confirmation reply, drafted in their words.>
<Answer finder: the answer, where it came from ("from your colour list, 2023"), the reply drafted;
or "I don't know, ask <who>" when it isn't in the references.>
<Job status: the reply drafted from what they pasted or the connected job system, with the date and
the source; never a date that isn't there.>

## Checks before you hand it back
1. Nothing invented. Every price is a rate in `references/rates.csv` × a quantity; every answer has a
   source; every date comes from what they gave you.
2. No personal details copied from the message into anything but the reply itself.
3. <their checks, from "Checks for your assistant" in the map file>
4. Check yourself against `references/examples.md`.

## Stays their call
<from Q29: prices, dates, complaints …> Hand back a draft and say what needs their decision.

## Remember that
When they correct you, say the new rule back in one sentence, use it for the rest of this chat, and
say: "Say **update my skill** and I'll write it in for good." On "update my skill": rewrite the
affected files, zip the folder `<name>` itself as `<name>.zip`, offer it, and tell them: Customize →
Skills → remove the old one, then **Upload skill** and pick the new zip.
```

## 3. Zip it, check it, offer it

Use code execution. Zip **the folder itself**, so the zip holds `<name>/SKILL.md`:

```python
import os, zipfile
name = "tallowood-orders"   # the folder name
with zipfile.ZipFile(f"{name}.zip", "w", zipfile.ZIP_DEFLATED) as z:
    for root, _, files in os.walk(name):
        for f in files:
            z.write(os.path.join(root, f))
names = zipfile.ZipFile(f"{name}.zip").namelist()
assert f"{name}/SKILL.md" in names and all(n.startswith(f"{name}/") for n in names), names
print("\n".join(names))
```

Before zipping, check the frontmatter: `name` equals the folder name and `description` is under
1024 characters. Offer `<name>.zip`.

**Can't make files:** "To make the file I need one setting on: **Settings → Capabilities → Code
execution and file creation**. Turn it on and say **try again**." If it still can't, show SKILL.md
and each references file as its own copyable block.

## 4. Try it once (step 11)

Give its logic the test case's input only (not the answer) and show the result next to what they
did:

```markdown
**Quick test on your work order for unit 4.**
You: job in Tradify, 2 bedrooms at the contract rate, $1,140.00 ex GST, WO-5531 in the notes; replied "booked for Tues 12th".
Your order reader: same job, 2 × bedroom up to 12 m² at $570.00 ex GST = $1,140.00 ex GST ($1,254.00 inc), WO-5531; flags "tenant number looks short, check"; drafts "Thanks, booked for Tues 12th, ref WO-5531. We'll text the tenant the day before." ✓
```

If it differs, find the rule or rate that caused it, ask one short question if needed, fix the
files, re-zip and show it once more. One round only. Any difference left goes in the map file's
"Your assistant" section.

## 5. Add it to Claude (step 12)

```markdown
**Last bit: add your order reader to Claude.** Do this on a computer (the Claude desktop app or claude.ai).

1. Download **tallowood-orders.zip**. Don't unzip it.
2. Open Claude → **Customize** → **Skills** → **Upload skill**, and pick the zip.
3. Make sure it's switched on.
4. Start a new chat and try: "**read this work order**" with a real one.

Can't see Skills? Turn on **Code execution and file creation** under **Settings → Capabilities**.
On your phone right now? Do it later at the computer; after that it works on your phone too.

Say **added** when it's in, or **later**.
```

Then set `assistant_built: true`, `assistant_kind`, `assistant_name` and `assistant_added` (`yes` ·
`later` · `unknown`) in the map file header, fill in "Your assistant", re-make the map file and
offer it again.
