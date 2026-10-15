# Trade tools

Short question-and-answer setups for trade businesses. Each one asks how you do a job today, then
builds you your own Claude skill for that job, ready to add to Cowork. You also get one summary file
you can send to Adam if you'd like his help taking it further.

There are four. Do the one Adam asks for:

| Type this | For |
|---|---|
| **/quote-intake** | How you quote |
| **/takeoff-intake** | How you do takeoffs from drawings |
| **/po-intake** | How you order materials (purchase orders) |
| **/sales-intake** | How enquiries come in and become jobs |

## Setup (once, about 5 minutes)

You need a paid Claude plan (Pro is enough). The free plan can't add these.

**On your phone**
1. Download the **Claude** app (App Store or Google Play).
2. Sign up with your email, then choose **Pro**.

**On your computer** (this one step needs a computer)
3. Go to **claude.ai** and log in with the same email.
4. Click **Customize**, then **Plugins**, then **Add**, then **Add marketplace**.
5. Paste this and click **Add**: `adamfromAPGsoftware/trade-tools`
6. Find **trade-intake** in the list and click **Install**.

Done. It now works on your phone too.

## Do the questions (about 30 minutes)

1. Open Claude (phone or computer) and start a **new chat**.
2. Type the one Adam asked for, e.g. **/quote-intake**, and send it.
3. Drop in your last two examples (quotes, drawings, orders or enquiries), then answer the questions. Talk or type; rough is fine.
4. Claude draws your process out. Check it step by step and say what's wrong.
5. Claude builds **your own skill** (a .zip), tries it on one of your examples, and walks you through
   adding it: **Customize → Skills → Upload skill**, switch it on, then try it in **Cowork**.
6. You also get **one summary file**. If you want Adam's help taking it further, tap it, then
   **Share**, and send it to him.

That's it.

Using Claude Code instead? `/plugin marketplace add adamfromAPGsoftware/trade-tools`, then
`/plugin install trade-intake@trade-tools`.

## What happens to my information?

The questions run in your own Claude account, and your skill stays in your account. Nothing is sent
to Adam or anyone else unless you share the file yourself. Never put passwords or bank details in the chat.
