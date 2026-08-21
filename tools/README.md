# Tools

## question_wheel.py

An AnswerThePublic-style topic explorer built on Google's free
autocomplete API — the same underlying data source AnswerThePublic
uses. Feed it a news topic and it fans the topic out into the
questions people are actually asking Google, grouped the same way
AnswerThePublic groups them (Questions / Prepositions / Comparisons,
plus an optional A–Z sweep).

Use it at the start of each week to pick an article and to seed the
"My Thoughts & Questions" section of the annotation write-up.

```bash
# Basic wheel
python3 tools/question_wheel.py "gaza investigation"

# Deeper sweep, saved to a file
python3 tools/question_wheel.py "california wildfires" --alphabet -o wheel.md
```

Requires only Python 3 (standard library). Run it from your own
machine — some managed environments block Google's suggest endpoint.

Workflow tip: run the wheel on 2–3 candidate topics from this week's
headlines, pick the topic whose questions genuinely interest you, then
find a strong article on it and carry two of the wheel's questions into
your annotation summary.
