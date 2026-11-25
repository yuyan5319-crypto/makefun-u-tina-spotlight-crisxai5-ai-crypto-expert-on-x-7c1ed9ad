#!/usr/bin/env python3
"""Draw the spotlight card for @crisxai5 (1600x900 PNG).

Creative: a dark, phone-readable card. The hook is "FOLLOW THE SIGNAL /
SKIP THE NOISE" — crypto X is mostly noise, and @crisxai5 is positioned
as the signal: sharp takes on AI agents, crypto markets and Web3,
zero fluff. Big type, one accent colour, three topic chips at the foot.
"""
from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H = 1600, 900
BG = (10, 14, 24)          # deep navy-black
ACCENT = (56, 224, 200)    # teal
ACCENT2 = (96, 165, 250)   # soft blue
WHITE = (245, 247, 250)
MUTED = (168, 178, 196)
CHIP_EDGE = (70, 84, 110)

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def spaced(draw, xy, text, fnt, fill, tracking=10):
    """Draw text with manual letter tracking; return total width."""
    x, y = xy
    total = 0
    for ch in text:
        draw.text((x, y), ch, font=fnt, fill=fill)
        w = draw.textlength(ch, font=fnt)
        x += w + tracking
        total += w + tracking
    return total - tracking


base = Image.new("RGB", (W, H), BG)

# --- soft accent glow, top-right (teal) and bottom-left (blue) ------------
glow = Image.new("RGB", (W, H), (0, 0, 0))
gd = ImageDraw.Draw(glow)
gd.ellipse([1020, -460, 2020, 540], fill=(20, 96, 84))
gd.ellipse([-520, 480, 460, 1360], fill=(18, 44, 96))
glow = glow.filter(ImageFilter.GaussianBlur(180))
img = Image.blend(base, glow, 0.55)

d = ImageDraw.Draw(img)

MARGIN = 110

# --- kicker ---------------------------------------------------------------
kicker_f = font(BOLD, 34)
spaced(d, (MARGIN, 84), "SPOTLIGHT — MUST-FOLLOW ON X", kicker_f, ACCENT, tracking=8)
d.line([MARGIN, 158, MARGIN + 620, 158], fill=ACCENT, width=5)

# --- the handle -------------------------------------------------------------
handle_f = font(BOLD, 168)
d.text((MARGIN - 6, 196), "@crisxai5", font=handle_f, fill=WHITE)

# --- headline ---------------------------------------------------------------
head_f = font(BOLD, 104)
d.text((MARGIN, 420), "FOLLOW THE SIGNAL.", font=head_f, fill=WHITE)
d.text((MARGIN, 540), "SKIP THE NOISE.", font=head_f, fill=ACCENT)

# --- subline ------------------------------------------------------------------
sub_f = font(REG, 44)
d.text((MARGIN, 690),
       "Sharp takes on AI agents, crypto markets & Web3 — zero fluff.",
       font=sub_f, fill=MUTED)

# --- topic chips ----------------------------------------------------------------
chip_f = font(BOLD, 34)
chips = ["AI AGENTS", "CRYPTO MARKETS", "WEB3 INNOVATION"]
x = MARGIN
y = 782
for label in chips:
    tw = d.textlength(label, font=chip_f)
    pad_x, h = 30, 66
    d.rounded_rectangle([x, y, x + tw + pad_x * 2, y + h], radius=h // 2,
                        outline=CHIP_EDGE, width=3)
    d.text((x + pad_x, y + 13), label, font=chip_f, fill=WHITE)
    x += tw + pad_x * 2 + 26

img.save("post.png")
print("wrote post.png", img.size)
