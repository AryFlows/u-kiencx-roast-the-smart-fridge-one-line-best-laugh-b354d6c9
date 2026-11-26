#!/usr/bin/env python3
"""Frost Fridge Report: one-line roast of a smart fridge.

Writes a single funny line (1-160 chars) roasting the smart fridge
to MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt).
"""
import os

LINE = (
    "My smart fridge emails me a weekly report on my 2 a.m. snacking, "
    "complete with a chart, a trend line, and one very disappointed emoji."
)


def main():
    assert 1 <= len(LINE) <= 160, f"line is {len(LINE)} chars"
    assert "\n" not in LINE, "line must be a single line"
    assert LINE.strip() == LINE, "line must not start or end with whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    with open(path, encoding="utf-8") as f:
        assert f.read() == LINE, "round-trip mismatch"
    print(f"wrote {len(LINE)} chars to {path}")


if __name__ == "__main__":
    main()
