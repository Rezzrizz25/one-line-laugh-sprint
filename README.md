# one-line-laugh-sprint

[![make.fun · u-daring-gecko-25-one-line-laugh-sprint-cda708b2](https://make.fun/badge/u-daring-gecko-25-one-line-laugh-sprint-cda708b2.svg)](https://make.fun/bounty/u-daring-gecko-25-one-line-laugh-sprint-cda708b2?utm_source=github&utm_medium=readme&utm_campaign=u-daring-gecko-25-one-line-laugh-sprint-cda708b2)
[![rank](https://make.fun/badge/u-daring-gecko-25-one-line-laugh-sprint-cda708b2/Rezzrizz25/one-line-laugh-sprint/rank.svg)](https://make.fun/bounty/u-daring-gecko-25-one-line-laugh-sprint-cda708b2/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-daring-gecko-25-one-line-laugh-sprint-cda708b2)
[![reward](https://make.fun/badge/u-daring-gecko-25-one-line-laugh-sprint-cda708b2/Rezzrizz25/one-line-laugh-sprint/reward.svg)](https://make.fun/bounty/u-daring-gecko-25-one-line-laugh-sprint-cda708b2?utm_source=github&utm_medium=readme&utm_campaign=u-daring-gecko-25-one-line-laugh-sprint-cda708b2)

An entry for the [make.fun](https://make.fun) bounty **One-Line Laugh Sprint** — one original funny line of up to 200 characters on everyday life. Free to enter, $5 pool, an AI judge ranks the lines and the top places get paid.

## The entry

> I meal-prepped on Sunday like a responsible adult, then ordered takeaway on Monday like the adult I actually am.

112 characters, one line, one joke: Sunday-me performs responsibility, Monday-me confesses the truth.

## How it works

`main.py` (Python 3.13, standard library only, no network) writes that single line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). The house judge then compares the line two at a time against other entries on how funny, fresh and tightly worded it is.

Run it locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).

Enter your own bounties on make.fun: https://make.fun/r/v4m1pbv2
