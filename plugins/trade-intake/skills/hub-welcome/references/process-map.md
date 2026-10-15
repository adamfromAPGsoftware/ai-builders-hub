# See it and confirm it: how their business runs

Step 3. A high-level map, not a manual: 3 to 8 steps from the first enquiry to getting paid (or,
on the builder track, from finding a client to getting paid). People spot a wrong or missing step
in a picture that they'd nod through in a list.

## 1. What to build

One **self-contained HTML page**, shown as an artifact. No outside scripts, fonts or images.

- **Title:** `How [Business] runs`, and under it: "Check each step. Tell me what's wrong or missing."
- **One card per step, top to bottom**, numbered, with an arrow between cards. On each card: the
  step (bold), then who · using what. Phones read top to bottom, so there's no sideways drawing.
- **Forks:** if a step splits ("site visit or plans?"), show the decision as a diamond-badge card
  with both branches labelled in one line ("Homes → visit · Builders → plans"). Keep it to one or
  two forks; this is the big picture.
- **Red !** on the bottleneck steps, with the hours a week and the why in red under the step.
- **Clock note** on slow waits ("waits for the office day").
- **Legend** at the bottom, and a "Still done by hand" row of chips.
- Light and dark colour sets; the page sets its own background. No customer or staff names.

## 2. Confirm it

1. Publish, then: "Here's how your business runs, drawn out. On your phone it's in the Artifacts tab."
2. Two or three steps per message, as a table:

   | Steps | Is this right? |
   |---|---|
   | 1 → 2 → 3 | Enquiry in, you visit and quote, they say yes with a deposit |

   "1 Yes · 2 Fix something · 3 Something's missing between them".
3. Then the red marks: "| ! | Step 2, 6 hours a week writing quotes at night. Is that the main
   pain? |".
4. Redraw after every change (update the same artifact) and say what changed in one line.
5. Last: "Is this how [Business] runs? (1 Yes · 2 Not yet)". These checks don't count toward the 20.
6. No artifact possible: show the steps as a table (# · step · who · using what · !) and the
   Mermaid source (`flowchart TD`, steps `S1`…, `classDef pain stroke:#c0392b,stroke-width:3px`).

The confirmed steps go in the profile's "How the business runs", on the card and in the pack.

## 3. Template (Coolabah Air, made up)

Copy the shape; change the steps.

```html
<!doctype html>
<html lang="en-AU">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Coolabah Air map</title>
<style>
  :root { --bg:#fafaf8; --dot:#d8d2cc; --card:#ffffff; --line:#d8d2cc; --ink:#1a1614; --body:#5c5550;
          --accent:#d97757; --soft:#fbe8df; --red:#c0392b; }
  @media (prefers-color-scheme: dark) {
    :root:not([data-theme="light"]) { --bg:#171615; --dot:#2c2a28; --card:#1f1d1c; --line:#3a3633;
          --ink:#f0ebe6; --body:#bdb5ae; --accent:#e08a6c; --soft:#3a2720; --red:#e5675a; }
  }
  :root[data-theme="dark"] { --bg:#171615; --dot:#2c2a28; --card:#1f1d1c; --line:#3a3633;
          --ink:#f0ebe6; --body:#bdb5ae; --accent:#e08a6c; --soft:#3a2720; --red:#e5675a; }
  body { margin:0; background:var(--bg); color:var(--ink); font:16px/1.45 system-ui, sans-serif;
         background-image:radial-gradient(circle, var(--dot) 1.5px, transparent 1.5px); background-size:32px 32px; }
  main { max-width:560px; margin:0 auto; padding:24px 16px 48px; }
  h1 { font-size:24px; margin:0 0 4px; } .sub { color:var(--body); margin:0 0 20px; }
  ol { list-style:none; padding:0; margin:0; }
  li { background:var(--card); border:1.5px solid var(--line); border-radius:14px; padding:14px 16px;
       position:relative; margin:0 0 30px; }
  li:not(:last-child)::after { content:"↓"; position:absolute; left:50%; bottom:-28px; color:var(--body); }
  li.pain { background:var(--soft); border-color:var(--accent); }
  .n { display:inline-grid; place-items:center; width:28px; height:28px; border-radius:50%;
       background:var(--ink); color:var(--bg); font-weight:700; font-size:14px; margin-right:8px; }
  .who { color:var(--body); font-size:14px; margin-top:4px; }
  .bang { position:absolute; right:12px; top:12px; width:26px; height:26px; border-radius:50%;
          background:var(--red); color:#fff; font-weight:800; display:grid; place-items:center; }
  .why { color:var(--red); font-size:14px; margin-top:6px; font-weight:600; }
  .chips span { display:inline-block; border:1.5px solid var(--accent); background:var(--soft);
                border-radius:99px; padding:4px 12px; margin:0 6px 8px 0; font-size:14px; }
  .legend { color:var(--body); font-size:14px; margin-top:8px; }
</style>
</head>
<body>
<main>
  <h1>How Coolabah Air runs</h1>
  <p class="sub">Check each step. Tell me what's wrong or missing.</p>
  <ol>
    <li class="pain"><span class="n">1</span><b>Enquiry comes in</b><span class="bang">!</span>
      <div class="who">Me · phone, website</div><div class="why">Missed calls while on the tools</div></li>
    <li class="pain"><span class="n">2</span><b>Site visit and quote</b><span class="bang">!</span>
      <div class="who">Me · notepad, Excel</div><div class="why">6 h/wk · written up at night</div></li>
    <li><span class="n">3</span><b>Yes and deposit</b><div class="who">Customer · text, Xero</div></li>
    <li><span class="n">4</span><b>Order the unit</b><div class="who">Office · supplier portal</div></li>
    <li><span class="n">5</span><b>Book the install</b><div class="who">Office · ServiceM8</div></li>
    <li class="pain"><span class="n">6</span><b>Install and commission</b><span class="bang">!</span>
      <div class="who">Techs · ServiceM8 app</div><div class="why">4 h/wk · photos, certs and refrigerant log re-typed</div></li>
    <li class="pain"><span class="n">7</span><b>Invoice and chase</b><span class="bang">!</span>
      <div class="who">Office · Xero</div><div class="why">3 h/wk with step 8 · chasing slips</div></li>
    <li class="pain"><span class="n">8</span><b>Yearly service reminder</b><span class="bang">!</span>
      <div class="who">Office · spreadsheet</div><div class="why">Often never sent</div></li>
  </ol>
  <p><b>Still done by hand</b></p>
  <div class="chips"><span>Quote write-ups</span><span>Re-keying into ServiceM8</span><span>Compliance certs</span>
    <span>Refrigerant log</span><span>Service reminders</span><span>Invoice chasing</span></div>
  <p class="legend">Red ! = where it slows down or goes wrong · h/wk = hands-on hours a week</p>
</main>
</body>
</html>
```
