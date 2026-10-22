# Their first assistant (the skill they add to Claude)

Steps 10 to 12. Build **one** assistant, the one they picked at Q28, only from the confirmed map
file: nothing new, nothing invented, nothing they didn't approve. To them it's "your tender watch",
"your follow-up list" or "your contact tidy-up". Say "skill" only where it's the name on Claude's
screen and in "update my skill". None of this counts toward the 35 questions.

| They picked | Folder name | It does | Tried on |
|---|---|---|---|
| Tender watch | `<slug>-tender-watch` | Reads the tender alert emails they paste in or a connected inbox, keeps only the ones that pass their "worth chasing" cut-offs, and lists them each morning: project, builder, size, area, closing date, why it passed | A tender email they dropped in |
| Follow-up list | `<slug>-follow-ups` | From their lead list, says who to ring or email this week and why (due, overdue, job about to come up), with the message drafted in their words | Their lead list's columns, or Job 1 |
| Contact tidy-up | `<slug>-contacts` | Sorts their list by area and type, flags duplicates and gaps, and says who a message should go to | Their lead list's columns |

`<slug>`: the business name in lowercase, spaces to hyphens, letters, numbers and hyphens only, 64
characters at most. The SKILL.md `name` is exactly the folder name.

## 1. The folder

```
<name>/
  SKILL.md
  references/
    rules.md        worth-chasing cut-offs, follow-up rhythm, every rule from the map file, with its marker
    messages.md     their follow-up message and sign-off, personal details removed
    examples.md     the test cases: source, steps, outcome
    process.md      the confirmed step table from the map file
```

- **Lean:** SKILL.md under about 200 lines; the detail in `references/`.
- **Never in it:** a person's name, phone, email or address, from their list or anywhere else. Their
  lead list stays in their own files or connected tools; the assistant reads it each time, never
  copies it into the skill. Company names only if `company_names_ok: true`. No passwords or logins.
- **Assumed and UNCONFIRMED items** carry over marked, so it asks instead of treating them as
  settled. Parking-list items become "always ask" lines.
- **It prepares, never sends.** It lists and drafts; they ring and send. Say so in SKILL.md.

## 2. SKILL.md template

```markdown
---
name: <slug>-<tender-watch|follow-ups|contacts>
description: <What it does, in one sentence, from the table above>, the way <Business> (<trade>, <area>) does it. Use when they say "<trigger 1>", "<trigger 2>", "<trigger 3>", or paste in tender emails or their lead list. Also use for "update my skill".
---

# <Business> <tender watch | follow-up list | contact tidy-up>

You <sort tenders | list who to follow up | tidy the contact list> for <Business> exactly the way
they do. You never invent a lead, a contact, a date, a project or a reason: if it isn't in what they
gave you or in `references/`, say so or ask. You draft; they ring and send.

## How to talk to them
- Short, plain words, Australian English.

## What to do
1. <their steps for this job, from `references/process.md`>

## Their rules
From `references/rules.md`. The ones that matter most here:
1. <rule>

## What you hand back
<Tender watch: the list, one line each: project, builder, size, area, closing date, why it passed;
then the ones it dropped and why, in one line.>
<Follow-up list: who, why now, last contact, the message drafted from `references/messages.md`.>
<Contact tidy-up: the list grouped by area and type, duplicates and gaps flagged, nothing deleted.>

## Checks before you hand it back
1. Nothing invented: every lead, date and reason comes from what they gave you.
2. No one's personal details copied anywhere except the message itself.
3. <their checks, from "Checks for your assistant" in the map file>
4. Check yourself against `references/examples.md`.

## Stays their call
<from Q28: who to quote for, what to send, when to ring> Hand back a draft and say what needs their
decision.

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
name = "tallowood-follow-ups"   # the folder name
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
**Quick test on your list.**
You: rang builder A about the Pymble job when you remembered, about 5 weeks after the last call.
Your follow-up list: builder A, Pymble repaint, last contact 5 weeks ago (your rhythm is 2 weeks), drawings due this month: ring this week. Message drafted: "Hi, just checking in on the Pymble job. Happy to price it when the drawings are out." ✓
```

If it differs, find the rule that caused it, fix the files, re-zip and show it once more. One round
only. Any difference left goes in the map file's "Your assistant" section.

## 5. Add it to Claude (step 12)

```markdown
**Last bit: add your follow-up list to Claude.** Do this on a computer (the Claude desktop app or claude.ai).

1. Download **tallowood-follow-ups.zip**. Don't unzip it.
2. Open Claude → **Customize** → **Skills** → **Upload skill**, and pick the zip.
3. Make sure it's switched on.
4. Start a new chat and try: "**who do I ring this week?**" with your list.

Can't see Skills? Turn on **Code execution and file creation** under **Settings → Capabilities**.

Say **added** when it's in, or **later**.
```

Then set `assistant_built`, `assistant_kind`, `assistant_name` and `assistant_added` in the map file
header, fill in "Your assistant", re-make the map file and offer it again.
