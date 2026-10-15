#!/usr/bin/env python3
"""Draw an AI Builders Hub welcome card (PNG) from a card JSON file.

    python3 welcome_card.py card.json welcome-card.png

Needs only Pillow, which Claude's code execution already has. The JSON fields are described in
references/welcome-card.md. Missing optional fields are left off the card, never made up.
"""
import json
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W = 1600
PAD = 80
INNER = W - 2 * PAD

# AI Builders Hub palette (Adam Goodyer design system): warm cream, near-black ink, one orange.
CREAM = (250, 250, 248)
DOT = (216, 210, 204)
PANEL = (242, 237, 232)
LINE = (216, 210, 204)
INK = (26, 22, 20)
BODY = (92, 85, 80)
MUTED = (154, 146, 140)
ORANGE = (217, 119, 87)
ORANGE_TEXT = (192, 95, 42)
ORANGE_SOFT = (251, 232, 223)
RED = (192, 57, 43)
WHITE = (255, 255, 255)

FONT_DIRS = [
    "/usr/share/fonts/opentype/inter",
    "/usr/share/fonts/truetype/inter",
    "/usr/share/fonts/truetype/dejavu",
    "/usr/share/fonts/truetype/liberation",
    "/Library/Fonts",
    "/System/Library/Fonts/Supplemental",
]
FONT_FILES = {
    "regular": ["Inter-Regular.otf", "Inter-Regular.ttf", "DejaVuSans.ttf", "LiberationSans-Regular.ttf", "Arial.ttf"],
    "medium": ["Inter-Medium.otf", "Inter-Medium.ttf", "DejaVuSans.ttf", "LiberationSans-Regular.ttf", "Arial.ttf"],
    "bold": ["Inter-Bold.otf", "Inter-Bold.ttf", "DejaVuSans-Bold.ttf", "LiberationSans-Bold.ttf", "Arial Bold.ttf"],
    "black": ["InterDisplay-Bold.otf", "Inter-ExtraBold.otf", "Inter-Bold.otf", "DejaVuSans-Bold.ttf", "LiberationSans-Bold.ttf"],
}
_font_cache = {}


def font(weight, size):
    key = (weight, size)
    if key in _font_cache:
        return _font_cache[key]
    for name in FONT_FILES[weight]:
        for d in FONT_DIRS:
            p = Path(d) / name
            if p.exists():
                _font_cache[key] = ImageFont.truetype(str(p), size)
                return _font_cache[key]
    _font_cache[key] = ImageFont.load_default(size=size)
    return _font_cache[key]


def text_w(draw, s, f):
    return draw.textlength(s, font=f)


def wrap(draw, s, f, width):
    words, lines, cur = str(s).split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if text_w(draw, trial, f) <= width or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines or [""]


def line_h(f):
    a, d = f.getmetrics()
    return int((a + d) * 1.18)


class Card:
    """Lays the card out top to bottom on a tall canvas, then crops to the content."""

    def __init__(self):
        # Two layers: the dotted backdrop and panels underneath, the content on a clear layer above.
        self.base = Image.new("RGBA", (W, 6000), CREAM)
        self.bd = ImageDraw.Draw(self.base)
        for y in range(16, 6000, 32):
            for x in range(16, W, 32):
                self.bd.ellipse((x - 1.5, y - 1.5, x + 1.5, y + 1.5), fill=DOT)
        self.ov = Image.new("RGBA", (W, 6000), (0, 0, 0, 0))
        self.d = ImageDraw.Draw(self.ov)
        self.y = PAD

    # ---- primitives -------------------------------------------------------------------------
    def text(self, x, y, s, f, fill=INK):
        self.d.text((x, y), s, font=f, fill=fill)

    def para(self, x, y, s, f, width, fill=BODY, max_lines=None):
        lines = wrap(self.d, s, f, width)
        if max_lines and len(lines) > max_lines:
            lines = lines[:max_lines]
            lines[-1] = lines[-1].rstrip(".,;") + "…"
        for i, ln in enumerate(lines):
            self.text(x, y + i * line_h(f), ln, f, fill)
        return y + len(lines) * line_h(f)

    def chip(self, x, y, s, f, fg=INK, bg=WHITE, border=LINE):
        tw = text_w(self.d, s, f)
        h = line_h(f) + 18
        self.d.rounded_rectangle((x, y, x + tw + 36, y + h), radius=h // 2, fill=bg, outline=border, width=2)
        self.text(x + 18, y + 9, s, f, fg)
        return x + tw + 36, y + h

    def chips(self, x, y, items, f, width, **kw):
        cx, cy, row_h = x, y, line_h(f) + 18
        for s in items:
            tw = text_w(self.d, s, f) + 36
            if cx + tw > x + width and cx > x:
                cx, cy = x, cy + row_h + 14
            cx, _ = self.chip(cx, cy, s, f, **kw)
            cx += 14
        return cy + row_h

    def panel(self, top, bottom, fill=WHITE):
        self.d.rounded_rectangle((PAD, top, W - PAD, bottom), radius=28, fill=fill, outline=LINE, width=2)

    def heading(self, label, y):
        f = font("bold", 26)
        self.d.rectangle((PAD + 40, y + 6, PAD + 48, y + 34), fill=ORANGE)
        self.text(PAD + 64, y, label.upper(), f, ORANGE_TEXT)
        return y + 54

    # ---- sections ---------------------------------------------------------------------------
    def header(self, c):
        top = self.y
        r = 92
        cx, cy = PAD + r, top + r
        self.d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=ORANGE)
        initials = "".join(p[0] for p in c["name"].split()[:2]).upper()
        fi = font("black", 76)
        self.text(cx - text_w(self.d, initials, fi) / 2, cy - 50, initials, fi, WHITE)

        x = PAD + 2 * r + 48
        self.text(x, top + 6, "G'day, I'm " + c["name"], font("black", 72), INK)
        y = top + 100
        biz = c.get("business", "")
        if c.get("trade"):
            biz = (biz + " · " if biz else "") + c["trade"]
        y = self.para(x, y, biz, font("medium", 34), W - PAD - x, INK, max_lines=2)
        meta = " · ".join(v for v in [c.get("area"), c.get("team")] if v)
        if meta:
            y = self.para(x, y + 4, meta, font("regular", 30), W - PAD - x, BODY, max_lines=2)
        y = max(y, top + 2 * r) + 28
        if c.get("role"):
            _, y2 = self.chip(PAD, y, c["role"], font("bold", 28), fg=WHITE, bg=INK, border=INK)
            y = y2
        if c.get("what_i_do"):
            y = self.para(PAD, y + 26, c["what_i_do"], font("regular", 34), INNER, BODY, max_lines=3)
        self.y = y + 44

    def goals(self, c):
        items = c.get("goals", [])[:3]
        if not items:
            return
        top = self.y
        y = self.heading("What I'm here for", top + 36)
        col_w = (INNER - 80 - 2 * 28) / 3
        fnum, ft = font("black", 56), font("medium", 30)
        bottoms = []
        for i, g in enumerate(items):
            x = PAD + 40 + i * (col_w + 28)
            self.text(x, y, f"{i + 1}", fnum, ORANGE)
            bottoms.append(self.para(x, y + 74, g, ft, col_w, INK, max_lines=4))
        bottom = max(bottoms) + 36
        self._behind(top, bottom)
        self.y = bottom + 32

    def sop(self, c):
        steps = c.get("steps", [])[:8]
        if not steps:
            return
        top = self.y
        y = self.heading(c.get("steps_title", "How my business runs"), top + 36)
        n = len(steps)
        per_row = (n + 1) // 2 if n > 4 else n  # 5 to 8 steps: two balanced rows
        gap = 46
        bw = (INNER - 80 - gap * (per_row - 1)) / per_row
        ft, fs, fn = font("bold", 28), font("regular", 23), font("black", 30)
        rows = [steps[i:i + per_row] for i in range(0, n, per_row)]
        bh = 210
        for ri, row in enumerate(rows):
            ry = y + ri * (bh + 70)
            for i, s in enumerate(row):
                idx = ri * per_row + i
                x = PAD + 40 + i * (bw + gap)
                hot = bool(s.get("pain"))
                self.d.rounded_rectangle((x, ry, x + bw, ry + bh), radius=18,
                                         fill=ORANGE_SOFT if hot else PANEL,
                                         outline=ORANGE if hot else LINE, width=3 if hot else 2)
                self.d.ellipse((x + 18, ry + 18, x + 66, ry + 66), fill=INK)
                num = str(idx + 1)
                self.text(x + 42 - text_w(self.d, num, fn) / 2, ry + 23, num, fn, WHITE)
                ty = self.para(x + 18, ry + 80, s["step"], ft, bw - 36, INK, max_lines=2)
                who = " · ".join(v for v in [s.get("who"), s.get("tool")] if v)
                if who:
                    self.para(x + 18, ty + 4, who, fs, bw - 36, BODY, max_lines=2)
                if hot:
                    self.d.ellipse((x + bw - 58, ry + 16, x + bw - 16, ry + 58), fill=RED)
                    fb = font("black", 30)
                    self.text(x + bw - 37 - text_w(self.d, "!", fb) / 2, ry + 19, "!", fb, WHITE)
                # arrow to the next step in the row
                if i < len(row) - 1:
                    ax, ay = x + bw + 8, ry + bh / 2
                    self.d.line((ax, ay, ax + gap - 18, ay), fill=MUTED, width=4)
                    self.d.polygon([(ax + gap - 14, ay), (ax + gap - 28, ay - 10), (ax + gap - 28, ay + 10)], fill=MUTED)
            # wrap arrow down to the next row
            if ri < len(rows) - 1:
                lx = PAD + 40 + (len(row) - 1) * (bw + gap) + bw / 2
                fx = PAD + 40 + bw / 2
                y1, y2 = ry + bh + 8, ry + bh + 62
                mid = (y1 + y2) / 2
                self.d.line((lx, y1, lx, mid), fill=MUTED, width=4)
                self.d.line((fx, mid, lx, mid), fill=MUTED, width=4)
                self.d.line((fx, mid, fx, y2 - 12), fill=MUTED, width=4)
                self.d.polygon([(fx, y2 - 2), (fx - 10, y2 - 16), (fx + 10, y2 - 16)], fill=MUTED)
        bottom = y + len(rows) * bh + (len(rows) - 1) * 70 + 24
        fl = font("regular", 24)
        self.d.ellipse((PAD + 40, bottom + 4, PAD + 68, bottom + 32), fill=RED)
        self.text(PAD + 49, bottom + 2, "!", font("black", 24), WHITE)
        self.text(PAD + 80, bottom + 2, "= where it slows down or goes wrong", fl, BODY)
        bottom += 70
        self._behind(top, bottom)
        self.y = bottom + 32

    def bottlenecks(self, c):
        items = c.get("bottlenecks", [])[:3]
        if not items:
            return
        top = self.y
        y = self.heading("Biggest bottlenecks", top + 36)
        ft, fh = font("bold", 32), font("black", 40)
        for b in items:
            hrs = b.get("hours")
            hrs_s = f"{hrs} h/wk" if hrs not in (None, "", "not given") else ""
            hw = text_w(self.d, hrs_s, fh) if hrs_s else 0
            self.d.ellipse((PAD + 44, y + 12, PAD + 64, y + 32), fill=RED)
            yb = self.para(PAD + 86, y, b["what"], ft, INNER - 160 - hw, INK, max_lines=2)
            if hrs_s:
                self.text(W - PAD - 40 - hw, y - 4, hrs_s, fh, ORANGE_TEXT)
            if b.get("why"):
                yb = self.para(PAD + 86, yb + 2, b["why"], font("regular", 26), INNER - 160 - hw, BODY, max_lines=2)
            y = yb + 26
        if c.get("hours_lost_total"):
            self.d.line((PAD + 40, y, W - PAD - 40, y), fill=LINE, width=2)
            s = f"About {c['hours_lost_total']} hours a week on jobs a computer could help with"
            y = self.para(PAD + 40, y + 20, s, font("medium", 28), INNER - 80, BODY, max_lines=2) + 8
        bottom = y + 20
        self._behind(top, bottom)
        self.y = bottom + 32

    def two_col(self, c):
        manual, tools = c.get("manual", [])[:6], c.get("tools", [])[:8]
        if not manual and not tools:
            return
        top = self.y
        half = (INNER - 80 - 40) / 2
        fc = font("medium", 26)
        yl = yr = top + 36
        if manual:
            f = font("bold", 26)
            self.d.rectangle((PAD + 40, yl + 6, PAD + 48, yl + 34), fill=ORANGE)
            self.text(PAD + 64, yl, "STILL DONE BY HAND", f, ORANGE_TEXT)
            yl = self.chips(PAD + 40, yl + 54, manual, fc, half, fg=INK, bg=ORANGE_SOFT, border=ORANGE)
        if tools:
            x = PAD + 40 + half + 40
            f = font("bold", 26)
            self.d.rectangle((x, yr + 6, x + 8, yr + 34), fill=ORANGE)
            self.text(x + 24, yr, "TOOLS I USE", f, ORANGE_TEXT)
            yr = self.chips(x, yr + 54, tools, fc, half)
        bottom = max(yl, yr) + 36
        self._behind(top, bottom)
        self.y = bottom + 32

    def footer_band(self, c):
        lines = []
        if c.get("automate_first"):
            lines.append(("First thing I want to automate", c["automate_first"]))
        if c.get("ask_me_about"):
            lines.append(("Ask me about", c["ask_me_about"]))
        if not lines:
            return
        top = self.y
        y = top + 40
        for label, val in lines:
            self.text(PAD + 48, y, label.upper(), font("bold", 24), ORANGE_SOFT)
            y = self.para(PAD + 48, y + 38, val, font("bold", 36), INNER - 96, WHITE, max_lines=3) + 24
        bottom = y + 16
        self._behind(top, bottom, fill=INK)
        self.y = bottom + 40

    def signoff(self, c):
        f = font("bold", 28)
        left = "AI Builders Hub"
        self.text(PAD, self.y, left, f, INK)
        self.d.ellipse((PAD + text_w(self.d, left, f) + 14, self.y + 12, PAD + text_w(self.d, left, f) + 26, self.y + 24), fill=ORANGE)
        right = c.get("joined", "")
        if right:
            fr = font("regular", 26)
            self.text(W - PAD - text_w(self.d, right, fr), self.y + 2, right, fr, MUTED)
        self.y += 80

    def _behind(self, top, bottom, fill=WHITE):
        """Panels go on the backdrop layer, under the content already drawn."""
        self.bd.rounded_rectangle((PAD, top, W - PAD, bottom), radius=28, fill=fill,
                                  outline=LINE if fill == WHITE else fill, width=2)


def render(card, out):
    c = Card()
    c.header(card)
    c.goals(card)
    c.sop(card)
    c.bottlenecks(card)
    c.two_col(card)
    c.footer_band(card)
    c.signoff(card)
    img = Image.alpha_composite(c.base, c.ov).crop((0, 0, W, c.y + PAD // 2)).convert("RGB")
    img.save(out, "PNG", optimize=True)
    return img.size


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("usage: welcome_card.py card.json out.png")
    data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    size = render(data, sys.argv[2])
    print(f"wrote {sys.argv[2]} ({size[0]}x{size[1]})")
