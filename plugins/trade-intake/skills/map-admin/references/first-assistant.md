# Their first assistant (the skill they add to Claude)

Steps 10 to 12. Build **one** assistant, the one they picked at Q28, only from the confirmed map
file: nothing new, nothing invented, nothing they didn't approve. To them it's "your bill checker" or
"your chase list". Say "skill" only where it's the name on Claude's screen and in "update my skill".
None of this counts toward the 35 questions.

| They picked | Folder name | It does | Tried on |
|---|---|---|---|
| Bill checker | `<slug>-bill-checker` | Checks a supplier bill against its order and docket (and price list or quote), applies their tolerance, and hands back "pay" with the coding, or "hold" with the difference and the query email drafted | The bill they dropped in |
| Debtor chase list | `<slug>-chase-list` | From their aged debtors (pasted or from a connected Xero or MYOB), lists who to chase today and why, with the email or phone note drafted in their words | Their debtors summary |
| Payroll check | not built yet | Mapped only. Say it's being built and offer one of the other two | — |

`<slug>`: the business name in lowercase, spaces to hyphens, letters, numbers and hyphens only, 64
characters at most. The SKILL.md `name` is exactly the folder name.

## 1. The folder

```
<name>/
  SKILL.md
  references/
    rules.md        tolerance, approval, terms, chase timing: every rule from the map file, with its marker
    messages.md     their query or chase message and sign-off, personal details removed
    examples.md     the test cases: input, steps, the call
    process.md      the confirmed step table from the map file
```

- **Lean:** SKILL.md under about 200 lines; the detail in `references/`.
- **Never in it:** anyone's name, pay, rates, tax file number, super or bank details; customer names
  or what any one customer owes. It reads bills and debtor lists each time; it never stores them in
  the skill. Supplier names only if `business_names_ok: true`. No passwords or logins.
- **Assumed and UNCONFIRMED items** carry over marked, so it asks instead of treating them as
  settled. Parking-list items become "always ask" lines.
- **It prepares, never pays or sends.** It checks and drafts; they approve, pay and send. Say so in
  SKILL.md.

## 2. SKILL.md template

```markdown
---
name: <slug>-<bill-checker|chase-list>
description: <What it does, in one sentence, from the table above>, the way <Business> (<trade>) does it. Use when they say "<trigger 1>", "<trigger 2>", "<trigger 3>", or drop in a supplier bill or their debtors list. Also use for "update my skill".
---

# <Business> <bill checker | chase list>

You <check supplier bills | list who to chase> for <Business> exactly the way they do. You never
invent an amount, a date, an order, a term or a reason: if it isn't in what they gave you or in
`references/`, ask. You check and draft; they approve, pay and send. You never pay a bill or send an
email.

## How to talk to them
- Short, plain words, Australian English. Every amount says inc or ex GST.

## What to do
1. <their steps, from `references/process.md`>

## Their rules
From `references/rules.md`. The ones that matter most here:
1. <rule>

## What you hand back
<Bill checker: each bill line against the order and docket; every difference with its dollar
amount ex GST; the call: pay (with the coding) or hold (with the query email drafted from
`references/messages.md`).>
<Chase list: who, how much, how many days over, last contact, what to do today (email, ring, or
leave), with the message drafted.>

## Checks before you hand it back
1. Nothing invented. Every amount comes from the bill, the order or the list they gave you.
2. Lines add up; GST is 10% of the ex-GST total.
3. No one's personal details copied anywhere except the drafted message itself.
4. <their checks, from "Checks for your assistant" in the map file>
5. Check yourself against `references/examples.md`.

## Stays their call
<from Q28: approving and paying, who gets chased, writing off a debt> Hand back a draft and say what
needs their decision.

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
name = "tallowood-bill-checker"   # the folder name
with zipfile.ZipFile(f"{name}.zip", "w", zipfile.ZIP_DEFLATED) as z:
    for root, _, files in os.walk(name):
        for f in files:
            z.write(os.path.join(root, f))
names = zipfile.ZipFile(f"{name}.zip").namelist()
assert f"{name}/SKILL.md" in names and all(n.startswith(f"{name}/") for n in names), names
print("\n".join(names))
```

Check the frontmatter first: `name` equals the folder name and `description` is under 1024
characters. **Can't make files:** ask them to turn on **Settings → Capabilities → Code execution and
file creation** and say **try again**; if it still can't, show each file as a copyable block.

## 4. Try it once (step 11)

```markdown
**Quick test on your bill from supplier A.**
You: texted the owner, paid it on the 20th.
Your bill checker: 3 lines match the order; freight $45.00 ex GST on a pickup order doesn't. That's over your $20 tolerance: hold. Query drafted: "Bill 88213 has $45.00 freight, but we picked this order up. Could you send a corrected bill?" ✓
```

If it differs, find the rule that caused it, fix the files, re-zip and show it once more. One round
only. Any difference left goes in the map file's "Your assistant" section.

## 5. Add it to Claude (step 12)

```markdown
**Last bit: add your bill checker to Claude.** Do this on a computer (the Claude desktop app or claude.ai).

1. Download **tallowood-bill-checker.zip**. Don't unzip it.
2. Open Claude → **Customize** → **Skills** → **Upload skill**, and pick the zip.
3. Make sure it's switched on.
4. Start a new chat and try: "**check this bill**" with a real one.

Can't see Skills? Turn on **Code execution and file creation** under **Settings → Capabilities**.

Say **added** when it's in, or **later**.
```

Then set `assistant_built`, `assistant_kind`, `assistant_name` and `assistant_added` in the map file
header, fill in "Your assistant", re-make the map file and offer it again.
