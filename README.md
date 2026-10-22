# AI Builders Hub

The plugins, lessons and module map for the [AI Builders Hub](https://www.skool.com/ai-builders-hub).
The plugins install as the **trade-tools** marketplace.

Short question-and-answer setups for trade businesses. Each one asks how you do a job today, then
builds you your own Claude skill for that job, ready to add to Cowork. You also get one summary file
you can send to Adam if you'd like his help taking it further.

**New to the AI Builders Hub? Start with /hub-welcome.** About 15 minutes of quick questions about
you, your goals and how your business runs. You get a welcome card picture to post in the Hub's
Introductions, your intro post words, and a starter pack. Posting the card finishes the Hub's intro.

Then there are four tool setups. Do the one Adam asks for, or the one your welcome card points to:

| Type this | For |
|---|---|
| **/hub-welcome** | Your Hub intro: who you are, how your business runs, your welcome card |
| **/map-quoting** | How you quote |
| **/map-takeoffs** | How you do takeoffs from drawings |
| **/map-purchasing** | How you order materials (purchase orders) |
| **/map-sales** | How enquiries come in and become jobs |

## Setup (once, about 5 minutes)

You need a paid Claude plan (Pro is enough). The free plan can't add these.

**On your phone**
1. Download the **Claude** app (App Store or Google Play).
2. Sign up with your email, then choose **Pro**.

**On your computer** (this one step needs a computer)
3. Go to **claude.ai** and log in with the same email.
4. Click **Customize**, then **Plugins**, then **Add**, then **Add marketplace**.
5. Paste this and click **Add**: `adamfromAPGsoftware/ai-builders-hub`
6. Find **trade-intake** in the list and click **Install**.

Done. It now works on your phone too.

## Do the questions (about 30 minutes)

1. Open Claude (phone or computer) and start a **new chat**.
2. Type the one Adam asked for, e.g. **/map-quoting**, and send it.
3. Drop in your last two examples (quotes, drawings, orders or enquiries), then answer the questions. Talk or type; rough is fine.
4. Claude draws your process out. Check it step by step and say what's wrong.
5. Claude builds **your own skill** (a .zip), tries it on one of your examples, and walks you through
   adding it: **Customize → Skills → Upload skill**, switch it on, then try it in **Cowork**.
6. You also get **one summary file**. If you want Adam's help taking it further, tap it, then
   **Share**, and send it to him.

That's it.

Using Claude Code instead? `/plugin marketplace add adamfromAPGsoftware/ai-builders-hub`, then
`/plugin install trade-intake@trade-tools`.

## What happens to my information?

The questions run in your own Claude account, and your skill stays in your account. Nothing is sent
to Adam or anyone else unless you share the file yourself. Never put passwords or bank details in the chat.

## What's in this repo

| Path | What it is |
|---|---|
| `plugins/trade-intake/` | The plugin members install: `/hub-welcome` and the intakes |
| `course/` | One folder per Hub module: the typical process, where the time goes, the intake, the skills and the course lessons. [Start here](course/README.md) |
| `course/modules.json` | The one source for `course/` and `hub-map.json`. Edit this, then run `python3 tools/build_course.py` |
| `hub-map.json` | What exists in the Hub: stages, modules, lessons (with Skool ids) and skills, so a skill can point a member to the right lesson |

The module process maps come from APG's audits of real businesses, anonymised. Hours are staff
estimates, not measurements.
