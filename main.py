"""Unsent: The Micro-Confession Sprint — make.fun entry.

Writes one micro-confession to /output/entry.txt: a To: line naming who
it was meant for, and the unsent message itself, one line, exactly as it
was typed, with no explanation after it.
"""

import os

ENTRY = (
    "To: my sister\n"
    "I still owe you the $400 from Christmas, and every time I almost "
    "text you about it I remember you saying you'd already forgotten, "
    "and I let you forget."
)


def main() -> None:
    text = ENTRY.strip()
    if not text:
        raise SystemExit("entry must not be empty or only whitespace")
    if not 1 <= len(text) <= 260:
        raise SystemExit(f"entry must be 1-260 chars, got {len(text)}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get(
        "OUTPUT_DIR"
    ) or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
