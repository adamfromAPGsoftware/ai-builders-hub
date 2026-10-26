#!/usr/bin/env python3
"""Draw the picture of a Hub process map (PNG) for posting on the module's map thread.

    python3 map_card.py map.json quoting-map.png

The same map JSON as fill_map.py. A Skool comment shows a picture, not a page, so this draws the
first layer only: the three before numbers, the steps in order (time sinks in yellow, decisions as
forks) and what's being built first. The detail stays in the HTML map.

Needs only Pillow. Fonts: Barlow and Barlow Condensed (SIL Open Font Licence) in ../assets/fonts.
Look: the AI Trade Office design system, hi-vis yellow on ink (#FFC20E on #17181A), condensed ALL CAPS
headlines, a hazard band along the top, never red.
"""
import json
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

W = 1200
PAD = 64
INNER = W - 2 * PAD

BG = (23, 24, 26)          # ink #17181A
SURFACE = (31, 32, 35)
SURFACE_2 = (38, 40, 44)   # #26282C
BORDER = (54, 56, 60)
YELLOW = (255, 194, 14)    # hi-vis #FFC20E
YELLOW_SOFT = (255, 194, 14, 22)
WHITE = (255, 255, 255)
BODY = (200, 200, 201)
FAINT = (130, 132, 137)
INK = (23, 24, 26)

HERE = Path(__file__).resolve().parent
FALLBACK = ["/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"]
_cache = {}


FONT_DIR = [HERE.parent / "assets" / "fonts", Path("assets/fonts"), Path(".")]


def _face(weight, size):
    """Barlow Condensed for headlines and big numbers, Barlow for everything else."""
    if weight >= 900:
        return "BarlowCondensed-ExtraBold.ttf"
    if weight >= 700 and size >= 30:
        return "BarlowCondensed-Bold.ttf"
    if weight >= 700:
        return "Barlow-Bold.ttf"
    return "Barlow-Medium.ttf" if weight >= 500 else "Barlow-Regular.ttf"


def font(weight, size):
    key = (weight, size)
    if key in _cache:
        return _cache[key]
    name = _face(weight, size)
    for d in FONT_DIR:
        if (d / name).exists():
            _cache[key] = ImageFont.truetype(str(d / name), size)
            return _cache[key]
    for p in FALLBACK.get(weight, FALLBACK[400]) if isinstance(FALLBACK, dict) else FALLBACK:
        if Path(p).exists():
            _cache[key] = ImageFont.truetype(p, size)
            return _cache[key]
    _cache[key] = ImageFont.load_default(size=size)
    return _cache[key]


def hub_mark(d, x, y, s, nut, hole, text_f):
    """The AI Builders Hub mark: a yellow hex nut with AI in the hole, s px wide."""
    import math
    cx, cy, r = x + s / 2, y + s / 2, s / 2 * 0.94
    d.polygon([(cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a))) for a in range(0, 360, 60)], fill=nut)
    h = r * 0.56
    d.ellipse((cx - h, cy - h, cx + h, cy + h), fill=hole)
    tw = d.textlength("AI", font=text_f)
    a, _ = text_f.getmetrics()
    bb = d.textbbox((0, 0), "AI", font=text_f)
    d.text((cx - tw / 2, cy - (bb[1] + bb[3]) / 2), "AI", font=text_f, fill=nut)


def hazard(img, y, h, w, pitch, a, b):
    """A band of diagonal hi-vis stripes across the full width."""
    d = ImageDraw.Draw(img)
    d.rectangle((0, y, w, y + h), fill=a)
    x = -h
    while x < w + h:
        d.polygon([(x, y + h), (x + h, y), (x + h + pitch / 2, y), (x + pitch / 2, y + h)], fill=b)
        x += pitch


def nice_date(s):
    """2026-10-22 -> 22 Oct 2026; anything else is shown as given."""
    try:
        from datetime import date
        return date.fromisoformat(str(s)).strftime("%-d %b %Y")
    except Exception:
        return str(s)


class Card:
    def __init__(self, height):
        self.h = height
        self.base = Image.new("RGBA", (W, height), BG + (255,))
        hazard(self.base, 0, 14, W, 40, YELLOW + (255,), INK + (255,))
        self.d = ImageDraw.Draw(self.base)

    def tw(self, s, f, track=0):
        return self.d.textlength(s, font=f) + track * max(len(s) - 1, 0)

    def text(self, x, y, s, f, fill=WHITE, track=0):
        if not track:
            self.d.text((x, y), s, font=f, fill=fill)
            return
        for ch in s:
            self.d.text((x, y), ch, font=f, fill=fill)
            x += self.d.textlength(ch, font=f) + track

    def wrap(self, s, f, width):
        lines, cur = [], ""
        for word in str(s).split():
            t = (cur + " " + word).strip()
            if self.tw(t, f) <= width or not cur:
                cur = t
            else:
                lines.append(cur)
                cur = word
        if cur:
            lines.append(cur)
        return lines

    def para(self, x, y, s, f, width, fill=BODY, lh=None, max_lines=None):
        lh = lh or int(f.size * 1.35)
        lines = self.wrap(s, f, width)
        if max_lines and len(lines) > max_lines:
            lines = lines[:max_lines]
            while lines[-1] and self.tw(lines[-1] + "…", f) > width:
                lines[-1] = lines[-1][:-1]
            lines[-1] = lines[-1].rstrip() + "…"
        for i, ln in enumerate(lines):
            self.text(x, y + i * lh, ln, f, fill)
        return y + len(lines) * lh

    def pill(self, x, y, s, f, fg, bg=None, border=None, padx=16, h=None, track=0):
        h = h or int(f.size * 1.9)
        w = self.tw(s, f, track) + 2 * padx
        self.d.rounded_rectangle((x, y, x + w, y + h), radius=h // 2, fill=bg, outline=border, width=2)
        self.text(x + padx, y + (h - f.size) / 2 - f.size * 0.12, s, f, fg, track)
        return w

    def dashed_box(self, box, r, color, dash=12, gap=8, width=2):
        x0, y0, x1, y1 = box
        self.d.rounded_rectangle(box, radius=r, fill=BG)
        for (ax, ay, bx, by) in [(x0 + r, y0, x1 - r, y0), (x0 + r, y1, x1 - r, y1), (x0, y0 + r, x0, y1 - r), (x1, y0 + r, x1, y1 - r)]:
            length = max(abs(bx - ax), abs(by - ay))
            pos = 0
            while pos < length:
                e = min(pos + dash, length)
                if ax == bx:
                    self.d.line((ax, ay + pos, ax, ay + e), fill=color, width=width)
                else:
                    self.d.line((ax + pos, ay, ax + e, ay), fill=color, width=width)
                pos += dash + gap
        for cx, cy, a0 in [(x0 + r, y0 + r, 180), (x1 - r, y0 + r, 270), (x1 - r, y1 - r, 0), (x0 + r, y1 - r, 90)]:
            self.d.arc((cx - r, cy - r, cx + r, cy + r), a0, a0 + 90, fill=color, width=width)

    def arrow(self, x, y0, y1):
        self.d.line((x, y0, x, y1 - 10), fill=YELLOW, width=3)
        self.d.polygon([(x - 9, y1 - 12), (x + 9, y1 - 12), (x, y1)], fill=YELLOW)


def step_height(c, s, takes):
    if s.get("type") == "fork":
        return 96 + 52 * ((len(s.get("options") or []) + 1) // 2)
    h = 104
    if s.get("pain"):
        h += 32
    return h


def draw(m, out):
    steps = m.get("steps") or []
    takes = (m.get("first_skill") or {}).get("takes_over") or []
    probe = Card(10)
    title_f = font(900, 66)
    title_lines = probe.wrap(str(m.get("title") or "How it works today").upper(), title_f, INNER)
    summary_f = font(400, 26)
    summary_lines = probe.wrap(m["summary"], summary_f, INNER)[:3] if m.get("summary") else []

    y = PAD
    y += 64 + 40                                   # top bar
    y += 52 if m.get("example") else 0
    y += 34 + len(title_lines) * 70 + 14            # eyebrow + title
    y += 46 if m.get("business") else 0
    y += len(summary_lines) * 35 + (18 if summary_lines else 0)
    y += 30 + (150 if m.get("before") else 0)       # stats
    y += 70                                        # steps label
    gaps = 46
    y += sum(step_height(probe, s, takes) for s in steps) + gaps * max(len(steps) - 1, 0)
    fs = m.get("first_skill")
    y += 50 + (210 if fs else 0)
    y += 90                                        # footer
    c = Card(y)

    # top bar
    y = PAD
    hub_mark(c.d, PAD, y, 64, YELLOW, INK, font(900, 22))
    c.text(PAD + 84, y + 2, "AI BUILDERS HUB", font(900, 32), WHITE, track=2)
    mod = m.get("module") or {}
    sub = f"Module {mod.get('n')} · {mod.get('name')} map" if mod else "Process map"
    c.text(PAD + 84, y + 38, sub, font(400, 21), BODY)
    if m.get("updated"):
        pf = font(700, 19)
        label = "MAPPED " + nice_date(m["updated"]).upper()
        c.pill(W - PAD - c.tw(label, pf, 1) - 32, y + 12, label, pf, YELLOW, border=YELLOW, track=1)
    y += 64 + 40

    if m.get("example"):
        c.d.rounded_rectangle((PAD, y, W - PAD, y + 38), radius=10, fill=SURFACE_2, outline=FAINT)
        c.text(PAD + 16, y + 8, f"Example map · {m.get('business') or 'this business'} is made up, rates are examples", font(400, 19), BODY)
        y += 52

    eyebrow = (f"{mod.get('name')} map" if mod else "Process map").upper()
    c.text(PAD, y, eyebrow, font(700, 21), YELLOW, track=3)
    y += 34
    for ln in title_lines:
        c.text(PAD, y, ln, title_f, WHITE)
        y += 70
    y += 14
    if m.get("business"):
        bf = font(700, 24)
        c.text(PAD, y, m["business"], bf, WHITE)
        if m.get("trade"):
            c.text(PAD + c.tw(m["business"], bf) + 12, y, "· " + m["trade"], font(400, 24), BODY)
        y += 46
    for ln in summary_lines:
        c.text(PAD, y, ln, summary_f, BODY)
        y += 35
    y += 18 if summary_lines else 0
    y += 30

    before = (m.get("before") or [])[:3]
    if before:
        gap = 16
        tw_ = (INNER - gap * (len(before) - 1)) / len(before)
        for i, b in enumerate(before):
            x = PAD + i * (tw_ + gap)
            c.d.rounded_rectangle((x, y, x + tw_, y + 126), radius=18, fill=SURFACE, outline=BORDER, width=2)
            vf = font(900, 46)
            v = str(b.get("value", ""))
            while c.tw(v, vf) > tw_ - 40 and vf.size > 26:
                vf = font(900, vf.size - 2)
            c.text(x + 22, y + 18, v, vf, YELLOW)
            c.para(x + 22, y + 80, b.get("label", ""), font(400, 21), tw_ - 40, BODY, max_lines=1)
        y += 150

    c.text(PAD, y + 14, "THE STEPS, IN ORDER", font(700, 21), BODY, track=3)
    lf = font(400, 19)
    lx = W - PAD
    for label, kind in [("Assistant takes this", "solid"), ("Where the time goes", "outline")]:
        w = c.tw(label, lf)
        lx -= w
        c.text(lx, y + 15, label, lf, BODY)
        lx -= 30
        if kind == "solid":
            c.d.rounded_rectangle((lx, y + 17, lx + 20, y + 37), radius=5, fill=YELLOW)
        else:
            c.d.rounded_rectangle((lx, y + 17, lx + 20, y + 37), radius=5, outline=YELLOW, width=2)
        lx -= 26
    y += 70

    for i, s in enumerate(steps):
        h = step_height(c, s, takes)
        fork = s.get("type") == "fork"
        flag = bool(s.get("flag"))
        box = (PAD, y, W - PAD, y + h)
        if fork:
            c.dashed_box(box, 20, FAINT)
        else:
            c.d.rounded_rectangle(box, radius=20, fill=SURFACE, outline=YELLOW if flag else BORDER, width=3 if flag else 2)
            if flag:
                tint = Image.new("RGBA", (W, c.h), (0, 0, 0, 0))
                ImageDraw.Draw(tint).rounded_rectangle(box, radius=20, fill=YELLOW_SOFT)
                c.base = Image.alpha_composite(c.base, tint)
                c.d = ImageDraw.Draw(c.base)
                c.d.rounded_rectangle(box, radius=20, outline=YELLOW, width=3)
        # number, or a diamond for a decision
        cx, cy = PAD + 46, y + 48
        nf = font(700, 22)
        if fork:
            c.d.polygon([(cx, cy - 26), (cx + 26, cy), (cx, cy + 26), (cx - 26, cy)], outline=BODY, width=2)
            n = str(i + 1)
            c.text(cx - c.tw(n, nf) / 2, cy - 14, n, nf, BODY)
        else:
            col = YELLOW if flag else FAINT
            c.d.ellipse((cx - 22, cy - 22, cx + 22, cy + 22), outline=col, width=2)
            n = str(i + 1)
            c.text(cx - c.tw(n, nf) / 2, cy - 14, n, nf, YELLOW if flag else BODY)
        tx = PAD + 92
        right = W - PAD - 28
        time_s = s.get("time") if not fork else None
        tf = font(700 if flag else 400, 22)
        time_w = c.tw(time_s, tf) + 32 if time_s else 0
        title_f2 = font(700, 30)
        title_w = right - tx - (time_w + 24 if time_s else 0)
        if s.get("id") in takes:
            title_w -= 0
        c.para(tx, y + 24, s.get("title", ""), title_f2, title_w, WHITE, max_lines=1)
        if time_s:
            col = YELLOW if flag else BODY
            kx, ky = right - time_w + 10, y + 43
            c.d.ellipse((kx - 10, ky - 10, kx + 10, ky + 10), outline=col, width=2)
            c.d.line((kx, ky - 6, kx, ky, kx + 5, ky + 3), fill=col, width=2)
            c.text(right - time_w + 32, y + 30, time_s, tf, col)
        meta = " · ".join([x for x in [s.get("who")] + list(s.get("tools") or []) if x])
        if fork:
            c.text(tx, y + 64, s.get("who", ""), font(400, 21), BODY)
            opts = s.get("options") or []
            ow = (INNER - 92 - 28 - 16) / 2
            for k, o in enumerate(opts):
                ox = tx + (k % 2) * (ow + 16)
                oy = y + 98 + (k // 2) * 52
                c.d.rounded_rectangle((ox, oy, ox + ow, oy + 42), radius=12, fill=SURFACE, outline=BORDER, width=2)
                lab = o.get("label", "")
                lb = font(700, 20)
                c.text(ox + 14, oy + 9, lab, lb, WHITE)
                c.para(ox + 14 + c.tw(lab, lb) + 10, oy + 10, "– " + (o.get("note") or ""), font(400, 19),
                       ow - c.tw(lab, lb) - 38, BODY, max_lines=1)
        else:
            c.para(tx, y + 64, meta, font(400, 21), right - tx, BODY, max_lines=1)
            if s.get("pain"):
                c.para(tx, y + 96, s["pain"], font(500, 22), right - tx, WHITE, max_lines=1)
        if s.get("id") in takes:
            pf = font(700, 17)
            label = "ASSISTANT TAKES THIS"
            pw = c.tw(label, pf, 1) + 28
            c.pill(W - PAD - pw - 20, y - 17, label, pf, INK, bg=YELLOW, padx=14, h=34, track=1)
        y += h
        if i < len(steps) - 1:
            c.arrow(PAD + 46, y + 4, y + gaps - 4)
            y += gaps

    y += 50
    if fs:
        box = (PAD, y, W - PAD, y + 180)
        tint = Image.new("RGBA", (W, c.h), (0, 0, 0, 0))
        ImageDraw.Draw(tint).rounded_rectangle(box, radius=22, fill=YELLOW_SOFT)
        c.base = Image.alpha_composite(c.base, tint)
        c.d = ImageDraw.Draw(c.base)
        c.d.rounded_rectangle(box, radius=22, outline=YELLOW, width=3)
        c.text(PAD + 30, y + 26, "BUILDING FIRST", font(700, 20), YELLOW, track=3)
        save_w = 0
        if fs.get("saves"):
            sf = font(900, 34)
            save_w = c.tw(fs["saves"], sf)
            c.text(W - PAD - 30 - save_w, y + 58, fs["saves"], sf, YELLOW)
            c.text(W - PAD - 30 - c.tw("back, on our estimate", font(400, 19)), y + 102, "back, on our estimate", font(400, 19), BODY)
        c.para(PAD + 30, y + 56, str(fs.get("name", "")).upper(), font(900, 36), INNER - 90 - save_w, WHITE, max_lines=1)
        names = []
        for tid in takes:
            for k, s in enumerate(steps):
                if s.get("id") == tid:
                    names.append(str(k + 1))
        joined = ", ".join(names[:-1]) + " and " + names[-1] if len(names) > 1 else "".join(names)
        line = f"Takes over step{'s' if len(names) > 1 else ''} {joined}." if names else (fs.get("what") or "")
        c.para(PAD + 30, y + 110, line, font(400, 22), INNER - 90 - save_w, BODY, max_lines=2)
        y += 180

    y += 40
    c.d.line((PAD, y, W - PAD, y), fill=BORDER, width=2)
    c.text(PAD, y + 22, "skool.com/ai-builders-hub", font(700, 21), BODY)
    if m.get("business"):
        bt = m["business"]
        c.text(W - PAD - c.tw(bt, font(400, 21)), y + 22, bt, font(400, 21), FAINT)

    c.base.convert("RGB").save(out, optimize=True)
    print(out)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("usage: map_card.py map.json out.png")
    draw(json.loads(Path(sys.argv[1]).read_text()), sys.argv[2])
