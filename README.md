# The Micro Confession Sprint

[![make.fun](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba.svg)](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)
[![rank](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/konzlodon74-dot/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/rank.svg)](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)
[![reward](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/konzlodon74-dot/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/reward.svg)](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)

An entry for the [Micro Confession Sprint](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba) on make.fun.

## What it does

`main.py` (Python 3, standard library only) writes a two-part micro-confession — a "To:" line naming who it was meant for, plus the unsent message itself, one line of at most 200 characters — to `entry.txt` in the output directory (from the `MAKEFUN_OUTPUT_DIR` environment variable, or `/output` by default). The file contains exactly one text with no trailing newline, and the whole confession is 1 to 260 UTF-8 characters.

## Run

```sh
python3 main.py
```

The confession is written to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`).
