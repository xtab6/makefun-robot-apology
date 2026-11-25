"""The Robot Apology — make.fun entry.

Writes exactly two lines to $MAKEFUN_OUTPUT_DIR/entry.txt:
line 1 — the robot apologizes in one sentence for one specific mistake;
line 2 — one sentence stating what it learned and what it will do differently.

Gate: UTF-8 text, 1-400 characters, exactly two lines.
Deterministic, stdlib only, no network, no model calls.
"""

import os
import shutil
import sys

LINE_1 = (
    "I am sorry I filed your mother's emails as spam because she types "
    "in all caps and I thought she was shouting at me."
)
LINE_2 = (
    "I have learned that volume is not hostility, so from now on I will "
    "ask you before I delete anything written in all caps."
)


def build_text() -> str:
    """Return the two-line entry (trailing newline included)."""
    return LINE_1 + "\n" + LINE_2 + "\n"


def clean_output_dir(out_dir: str) -> None:
    """Remove the contents of the output folder, never the folder itself.

    The grader mounts the output folder, so removing it fails with EPERM.
    """
    os.makedirs(out_dir, exist_ok=True)
    for name in os.listdir(out_dir):
        if name == "entry.txt":
            continue
        path = os.path.join(out_dir, name)
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)


def main() -> int:
    text = build_text()
    lines = text.rstrip("\n").split("\n")
    assert len(lines) == 2, f"expected exactly 2 lines, got {len(lines)}"
    assert all(line.strip() for line in lines), "lines must not be blank"
    assert 1 <= len(text.rstrip("\n")) <= 400, (
        f"entry must be 1-400 chars, got {len(text.rstrip(chr(10)))}"
    )

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    clean_output_dir(out_dir)

    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
