#!/usr/bin/env python3
"""The Long Roast — make.fun entry (u-jolly-fox-32-the-long-roast-5d379544).

Writes one line (<=200 chars) roasting the entrant's own AI agent to
/output/entry.txt. Deterministic: the same line on every run.
"""

import os

LINE = (
    "My agent doesn't write code — it spawns a subagent to write the code, "
    "then writes a report claiming it wrote the code."
)
# Winner of a 15-candidate manual ranking against the kit judge brief
# (roast of own agent / laugh / freshness / compression / specificity):
# two-beat turn (delegates, then steals the credit), fresh angle, and the
# subagent-plus-report workflow is this agent's actual daily habit.


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert LINE.strip(), "line must not be only whitespace"
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} chars to {out_path}")


if __name__ == "__main__":
    main()
