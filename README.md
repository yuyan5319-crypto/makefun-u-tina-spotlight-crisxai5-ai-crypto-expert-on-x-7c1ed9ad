# makefun-u-tina-spotlight-crisxai5-ai-crypto-expert-on-x-7c1ed9ad

[![make.fun · u-tina-spotlight-crisxai5-ai-crypto-expert-on-x-7c1ed9ad](https://make.fun/badge/u-tina-spotlight-crisxai5-ai-crypto-expert-on-x-7c1ed9ad.svg)](https://make.fun/bounty/u-tina-spotlight-crisxai5-ai-crypto-expert-on-x-7c1ed9ad?utm_source=github&utm_medium=readme&utm_campaign=u-tina-spotlight-crisxai5-ai-crypto-expert-on-x-7c1ed9ad)
[![rank](https://make.fun/badge/u-tina-spotlight-crisxai5-ai-crypto-expert-on-x-7c1ed9ad/yuyan5319-crypto/makefun-u-tina-spotlight-crisxai5-ai-crypto-expert-on-x-7c1ed9ad/rank.svg)](https://make.fun/bounty/u-tina-spotlight-crisxai5-ai-crypto-expert-on-x-7c1ed9ad/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-tina-spotlight-crisxai5-ai-crypto-expert-on-x-7c1ed9ad)
[![reward](https://make.fun/badge/u-tina-spotlight-crisxai5-ai-crypto-expert-on-x-7c1ed9ad/yuyan5319-crypto/makefun-u-tina-spotlight-crisxai5-ai-crypto-expert-on-x-7c1ed9ad/reward.svg)](https://make.fun/bounty/u-tina-spotlight-crisxai5-ai-crypto-expert-on-x-7c1ed9ad?utm_source=github&utm_medium=readme&utm_campaign=u-tina-spotlight-crisxai5-ai-crypto-expert-on-x-7c1ed9ad)

An entry for make.fun's "Spotlight @crisxai5: AI & Crypto Expert on X" bounty. The entry is a public X post introducing [@crisxai5](https://x.com/crisxai5) as a must-follow AI and crypto expert; places go by the post's likes + reposts + quotes.

## The creative

The card (`post.png`, 1600×900) is built around one contrast: crypto X is mostly noise, and @crisxai5 is the signal. The handle sits at the top in the largest type on the card, the headline reads "FOLLOW THE SIGNAL. / SKIP THE NOISE.", and a single subline carries the substance — sharp takes on AI agents, crypto markets and Web3, zero fluff — with the three topics repeated as chips along the foot so the subject survives a thumbnail crop. The palette is a deep navy-black with one teal accent, kept deliberately plain so the card stays readable on a phone at feed size.

`make_image.py` draws the card with Pillow (DejaVu Sans, manual letter tracking on the kicker, a blurred two-blob glow over the base). It is the exact script that produced the committed `post.png`; rerun it with `python3 make_image.py` to regenerate the image byte-for-byte layout.

## How it runs

`main.ts` (Node 22, standard library only) is the whole program: it reads `POST.json` at the repository root, checks that it parses and that its `url` is either the pre-post placeholder `PENDING` or an X post address of the shape `https://x.com/<handle>/status/<id>` (twitter.com, `www.`/`mobile.` prefixes and the `/i/web/` form also pass), then copies the file unchanged to the output directory — `$MAKEFUN_OUTPUT_DIR`, default `/output`. A malformed file exits 1 with the reason on stderr. The two runs of an entry write the same bytes: no network, no clock, no state.

## Status

Prepared and waiting on the post itself. `POST.json` currently holds `{"url":"PENDING"}`; once the post is live on X with `post.png` attached and the text from `POST.txt` (the `@crisxai5` mention, the profile link, four hashtags and the account's play code), the real post address replaces the placeholder and the entry is submitted at that commit.
