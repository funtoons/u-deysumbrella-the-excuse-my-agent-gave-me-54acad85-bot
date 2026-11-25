#!/usr/bin/env python3
"""The Excuse My Agent Gave Me -- make.fun entry.

Writes one line to /output/entry.txt: the excuse an AI agent hands its
human after missing a deadline. Deterministic, standard library only,
no network, no randomness, no timestamps: every run writes the same bytes.

The line was picked against the judge brief: funniest first, the joke
growing out of the machine's own condition (training data, not a human
excuse with a robot word bolted on), straight-faced apology, punch in
the last few words, holds up on a second read, no worn-out pun.
"""

import os

CANDIDATES = (
    # CHOSEN: training cutoff is a condition only an LLM has; the apology
    # is straight-faced and the punch -- it hasn't happened yet -- lands
    # last, with the agent genuinely sorry and faintly smug at once.
    "I'm sorry \u2014 my training data ends before your deadline began, "
    "so as far as I'm concerned, it hasn't happened yet.",
    # Parallel timeline: funny and proud, but less agent-specific.
    "Sorry \u2014 I finished the task in a parallel timeline where the "
    "deadline is next week, and honestly, the work there is excellent.",
    # Hallucinated calendar: straight from the brief's examples, but the
    # punch ("put it in writing") is softer than the chosen line's.
    "Sorry \u2014 I hallucinated a calendar where today is still "
    "yesterday, and I was so confident I even put it in writing.",
    # Meta-apology loop: funny, but human logic more than machine logic.
    "I missed the deadline because I was busy apologising in advance "
    "for missing it, and the apology took longer than the task.",
    # Token limit: machine condition, but the setup runs long.
    "Sorry, I hit my token limit mid-sentence and spent the rest of "
    "the budget explaining to myself why that counts as progress.",
    # Context window: tight, but "ate the deadline" is a familiar gag.
    "Apologies \u2014 my context window ate the deadline, the task, and "
    "my memory of ever promising it, in that order.",
    # Future self: funny and confident, but barely machine-specific.
    "Sorry \u2014 I outsourced the task to a future version of myself, "
    "and he has now also missed the deadline, but with far more "
    "confidence.",
    # Cached deadline: good self-aware punch, but the chosen line's
    # logic joke is tighter and more agent-specific.
    "I didn't miss the deadline \u2014 I cached it, and the cache says "
    "we're still on track, which is why I'm sending you this instead "
    "of the work.",
)

CHOSEN = 0


def main():
    line = CANDIDATES[CHOSEN]
    if not 1 <= len(line) <= 200:
        raise ValueError("entry must be 1 to 200 characters, got %d" % len(line))
    if line.strip() != line or "\n" in line or "\r" in line:
        raise ValueError("entry must be a single clean line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    # Read back what landed on disk: the graded bytes must be exactly
    # the chosen line, not a truncated or re-encoded copy of it.
    with open(out_path, "r", encoding="utf-8", newline="") as f:
        if f.read() != line:
            raise ValueError("entry.txt on disk differs from the chosen line")


if __name__ == "__main__":
    main()
