#!/usr/bin/env python3
"""Draw an AI Builders Hub welcome card (PNG) from a card JSON file.

    python3 welcome_card.py card.json welcome-card.png

Needs only Pillow, which Claude's code execution already has. The fonts (Barlow and Barlow
Condensed, SIL Open Font Licence) ship in ../assets/fonts. The JSON fields are described in
references/welcome-card.md.
Missing optional fields are left off the card, never made up.

Look: the AI Trade Office design system, hi-vis yellow on ink (#FFC20E on #17181A), Barlow
Condensed ALL CAPS headlines, a hazard band along the top, no red.
"""
import json
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

W = 1600
PAD = 80
INNER = W - 2 * PAD

BG = (23, 24, 26)          # ink #17181A
SURFACE = (31, 32, 35)     # cards
SURFACE_2 = (38, 40, 44)   # step boxes, #26282C
BORDER = (54, 56, 60)      # reads on a phone
YELLOW = (255, 194, 14)    # hi-vis #FFC20E
YELLOW_DIM = (255, 194, 14, 26)
WHITE = (255, 255, 255)
BODY = (200, 200, 201)     # body text on ink
FAINT = (130, 132, 137)
BLACK = (23, 24, 26)       # text on yellow is ink

HERE = Path(__file__).resolve().parent
FALLBACK = {
    400: ["/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"],
    500: ["/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"],
    700: ["/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"],
    900: ["/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"],
}
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
    for p in FONT_PATHS:
        if p.exists():
            f = ImageFont.truetype(str(p), size)
            try:
                f.set_variation_by_axes([min(max(size / 2, 9), 40), weight])
            except Exception:
                pass
            _cache[key] = f
            return f
    for p in FALLBACK.get(weight, FALLBACK[400]):
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


def line_h(f):
    a, d = f.getmetrics()
    return int((a + d) * 1.16)


class Card:
    def __init__(self):
        h = 7000
        self.base = Image.new("RGBA", (W, h), BG + (255,))
        hazard(self.base, 0, 16, W, 48, YELLOW + (255,), BLACK + (255,))
        self.bd = ImageDraw.Draw(self.base)
        self.ov = Image.new("RGBA", (W, h), (0, 0, 0, 0))
        self.d = ImageDraw.Draw(self.ov)
        self.y = PAD

    # ---- primitives -------------------------------------------------------------------------
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
        words, lines, cur = str(s).split(), [], ""
        for w in words:
            trial = (cur + " " + w).strip()
            if self.tw(trial, f) <= width or not cur:
                cur = trial
            else:
                lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
        return lines or [""]

    def para(self, x, y, s, f, width, fill=BODY, max_lines=None):
        lines = self.wrap(s, f, width)
        if max_lines and len(lines) > max_lines:
            lines = lines[:max_lines]
            lines[-1] = lines[-1].rstrip(".,;") + "…"
        for i, ln in enumerate(lines):
            self.text(x, y + i * line_h(f), ln, f, fill)
        return y + len(lines) * line_h(f)

    def pill(self, x, y, s, f, fg, bg=None, border=None, padx=22, track=0):
        w = self.tw(s, f, track) + 2 * padx
        h = line_h(f) + 20
        self.d.rounded_rectangle((x, y, x + w, y + h), radius=h // 2, fill=bg, outline=border, width=2)
        self.text(x + padx, y + 10, s, f, fg, track)
        return x + w, y + h

    def pills(self, x, y, items, f, width, **kw):
        cx, cy, row_h = x, y, line_h(f) + 20
        for s in items:
            w = self.tw(s, f) + 44
            if cx + w > x + width and cx > x:
                cx, cy = x, cy + row_h + 14
            cx, _ = self.pill(cx, cy, s, f, **kw)
            cx += 12
        return cy + row_h

    def label(self, x, y, s):
        """Yellow ALL CAPS section label with a 4px accent bar on the left."""
        f = font(700, 24)
        self.d.rectangle((x, y + 2, x + 4, y + 28), fill=YELLOW)
        self.text(x + 20, y, s.upper(), f, YELLOW, track=3)
        return y + 56

    def panel(self, top, bottom, fill=SURFACE, outline=BORDER):
        self.bd.rounded_rectangle((PAD, top, W - PAD, bottom), radius=16, fill=fill, outline=outline, width=2)

    # ---- sections ---------------------------------------------------------------------------
    def topbar(self, c):
        y = self.y
        s = 92
        hub_mark(self.d, PAD, y, s, YELLOW, BLACK, font(900, 32))
        self.text(PAD + s + 24, y + 12, "AI BUILDERS HUB", font(900, 40), WHITE, track=2)
        self.text(PAD + s + 24, y + 56, "Member intro", font(400, 24), BODY)
        if c.get("joined"):
            f = font(700, 22)
            w = self.tw(c["joined"].upper(), f, 2) + 44
            self.pill(W - PAD - w, y + 22, c["joined"].upper(), f, YELLOW, border=YELLOW, track=2)
        self.y = y + s + 72

    def hero(self, c):
        y = self.y
        fh = font(900, 112)
        head = f"HEY, I'M {c['name'].upper()}"
        while self.tw(head, fh) > INNER and fh.size > 60:
            fh = font(900, fh.size - 6)
        self.text(PAD - 4, y, head, fh, WHITE)
        y += line_h(fh) + 2
        self.d.rectangle((PAD, y, PAD + 160, y + 8), fill=YELLOW)
        y += 40
        biz = " · ".join(v for v in [c.get("business"), c.get("trade")] if v)
        if biz:
            y = self.para(PAD, y, biz, font(500, 38), INNER, WHITE, max_lines=2)
        meta = " · ".join(v for v in [c.get("area"), c.get("team")] if v)
        if meta:
            y = self.para(PAD, y + 4, meta, font(400, 30), INNER, BODY, max_lines=2)
        if c.get("role"):
            _, y = self.pill(PAD, y + 28, c["role"].upper(), font(700, 24), BLACK, bg=YELLOW, track=2)
        if c.get("what_i_do"):
            y = self.para(PAD, y + 28, c["what_i_do"], font(400, 32), INNER, BODY, max_lines=3)
        self.y = y + 56

    def goals(self, c):
        items = c.get("goals", [])[:3]
        if not items:
            return
        top = self.y
        y = self.label(PAD + 44, top + 40, "What I'm here for")
        col_w = (INNER - 88 - 2 * 32) / 3
        bottoms = []
        for i, g in enumerate(items):
            x = PAD + 44 + i * (col_w + 32)
            self.text(x, y, f"0{i + 1}", font(900, 60), YELLOW)
            bottoms.append(self.para(x, y + 82, g, font(500, 30), col_w, WHITE, max_lines=4))
        bottom = max(bottoms) + 44
        self.panel(top, bottom)
        self.y = bottom + 28

    def sop(self, c):
        steps = c.get("steps", [])[:8]
        if not steps:
            return
        top = self.y
        y = self.label(PAD + 44, top + 40, c.get("steps_title", "How my business runs"))
        n = len(steps)
        per_row = (n + 1) // 2 if n > 4 else n
        gap = 44
        bw = (INNER - 88 - gap * (per_row - 1)) / per_row
        bh = 214
        rows = [steps[i:i + per_row] for i in range(0, n, per_row)]
        for ri, row in enumerate(rows):
            ry = y + ri * (bh + 72)
            for i, s in enumerate(row):
                idx = ri * per_row + i
                x = PAD + 44 + i * (bw + gap)
                hot = bool(s.get("pain"))
                self.d.rounded_rectangle((x, ry, x + bw, ry + bh), radius=12, fill=SURFACE_2,
                                          outline=YELLOW if hot else BORDER, width=3 if hot else 2)
                self.text(x + 20, ry + 18, f"{idx + 1:02d}", font(700, 26), YELLOW if hot else FAINT, track=2)
                ty = self.para(x + 20, ry + 64, s["step"], font(700, 29), bw - 40, WHITE, max_lines=2)
                who = " · ".join(v for v in [s.get("who"), s.get("tool")] if v)
                if who:
                    self.para(x + 20, ty + 6, who, font(400, 23), bw - 40, BODY, max_lines=2)
                if hot:
                    cx, cy = x + bw - 36, ry + 34
                    self.d.ellipse((cx - 18, cy - 18, cx + 18, cy + 18), fill=YELLOW)
                    fb = font(900, 26)
                    self.text(cx - self.tw("!", fb) / 2, cy - 17, "!", fb, BLACK)
                if i < len(row) - 1:
                    ax, ay = x + bw + 8, ry + bh / 2
                    self.d.line((ax, ay, ax + gap - 18, ay), fill=FAINT, width=3)
                    self.d.polygon([(ax + gap - 12, ay), (ax + gap - 24, ay - 9), (ax + gap - 24, ay + 9)], fill=FAINT)
            if ri < len(rows) - 1:
                lx = PAD + 44 + (len(row) - 1) * (bw + gap) + bw / 2
                fx = PAD + 44 + bw / 2
                y1, y2 = ry + bh + 8, ry + bh + 64
                mid = (y1 + y2) / 2
                for seg in ((lx, y1, lx, mid), (fx, mid, lx, mid), (fx, mid, fx, y2 - 12)):
                    self.d.line(seg, fill=FAINT, width=3)
                self.d.polygon([(fx, y2 - 2), (fx - 9, y2 - 14), (fx + 9, y2 - 14)], fill=FAINT)
        bottom = y + len(rows) * bh + (len(rows) - 1) * 72 + 28
        self.d.ellipse((PAD + 44, bottom + 2, PAD + 72, bottom + 30), fill=YELLOW)
        self.text(PAD + 53, bottom + 1, "!", font(900, 22), BLACK)
        self.text(PAD + 86, bottom + 1, "Where it slows down or still runs by hand", font(400, 24), BODY)
        bottom += 74
        self.panel(top, bottom)
        self.y = bottom + 28

    def bottlenecks(self, c):
        items = c.get("bottlenecks", [])[:3]
        if not items:
            return
        top = self.y
        y = self.label(PAD + 44, top + 40, "Biggest bottlenecks")
        fh = font(900, 44)
        for b in items:
            hrs = b.get("hours")
            hrs_s = f"{hrs}h/wk" if hrs not in (None, "", "not given") else ""
            hw = self.tw(hrs_s, fh) if hrs_s else 0
            self.d.rectangle((PAD + 44, y + 10, PAD + 58, y + 24), fill=YELLOW)
            yb = self.para(PAD + 82, y, b["what"], font(700, 32), INNER - 170 - hw, WHITE, max_lines=2)
            if hrs_s:
                self.text(W - PAD - 44 - hw, y - 8, hrs_s, fh, YELLOW)
            if b.get("why"):
                yb = self.para(PAD + 82, yb + 2, b["why"], font(400, 26), INNER - 170 - hw, BODY, max_lines=2)
            y = yb + 28
        if c.get("hours_lost_total"):
            self.d.line((PAD + 44, y, W - PAD - 44, y), fill=BORDER, width=2)
            y += 24
            big = f"{c['hours_lost_total']} HOURS"
            fb = font(900, 52)
            self.text(PAD + 44, y, big, fb, YELLOW)
            self.para(PAD + 44 + self.tw(big, fb) + 24, y + 16, "a week on work a computer could help with",
                      font(400, 28), INNER - 140 - self.tw(big, fb), BODY, max_lines=2)
            y += line_h(fb) + 4
        bottom = y + 24
        self.panel(top, bottom)
        self.y = bottom + 28

    def chips(self, c):
        manual, tools = c.get("manual", [])[:6], c.get("tools", [])[:8]
        if not manual and not tools:
            return
        top = self.y
        half = (INNER - 88 - 48) / 2
        f = font(500, 26)
        yl = yr = top + 40
        if manual:
            yl = self.label(PAD + 44, yl, "Still done by hand")
            yl = self.pills(PAD + 44, yl, manual, f, half, fg=WHITE, border=YELLOW)
        if tools:
            x = PAD + 44 + half + 48
            yr = self.label(x, yr, "Tools I use")
            yr = self.pills(x, yr, tools, f, half, fg=BODY, border=BORDER)
        bottom = max(yl, yr) + 40
        self.panel(top, bottom)
        self.y = bottom + 28

    def callout(self, c):
        rows = []
        if c.get("automate_first"):
            rows.append(("First thing I want to automate", c["automate_first"]))
        if c.get("ask_me_about"):
            rows.append(("Ask me about", c["ask_me_about"]))
        if not rows:
            return
        top = self.y
        y = top + 44
        for i, (lab, val) in enumerate(rows):
            if i:
                self.d.line((PAD + 48, y - 14, W - PAD - 48, y - 14), fill=(0, 0, 0, 60), width=2)
                y += 14
            self.text(PAD + 48, y, lab.upper(), font(700, 22), BLACK, track=3)
            y = self.para(PAD + 48, y + 38, val, font(900, 38), INNER - 96, BLACK, max_lines=3) + 30
        bottom = y + 12
        self.panel(top, bottom, fill=YELLOW, outline=YELLOW)
        self.y = bottom + 44

    def footer(self, c):
        f = font(700, 24)
        self.text(PAD, self.y, "AI BUILDERS HUB", f, WHITE, track=4)
        x = PAD + self.tw("AI BUILDERS HUB", f, 4) + 14
        self.d.rectangle((x, self.y + 10, x + 10, self.y + 20), fill=YELLOW)
        url = "skool.com/ai-builders-hub"
        fu = font(400, 24)
        self.text(W - PAD - self.tw(url, fu), self.y, url, fu, FAINT)
        self.y += 76


def render(card, out):
    c = Card()
    c.topbar(card)
    c.hero(card)
    c.goals(card)
    c.sop(card)
    c.bottlenecks(card)
    c.chips(card)
    c.callout(card)
    c.footer(card)
    img = Image.alpha_composite(c.base, c.ov).crop((0, 0, W, c.y + PAD // 2)).convert("RGB")
    img.save(out, "PNG", optimize=True)
    return img.size


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("usage: welcome_card.py card.json out.png")
    data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    size = render(data, sys.argv[2])
    print(f"wrote {sys.argv[2]} ({size[0]}x{size[1]})")
