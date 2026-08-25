#!/usr/bin/env python3
"""
clean_transcript.py — strip an auto-caption .srt/.vtt down to plain text for analysis.

Why this exists: yt-dlp auto-captions repeat each ~2s caption line 2-3x (a rolling-window
artifact) and carry timestamp/index lines that are pure token overhead for an LLM that only
needs the spoken content. This script removes both, so only the actual words are read.

Usage:
    python3 clean_transcript.py VIDEO_ID.en.srt
    python3 clean_transcript.py VIDEO_ID.en.srt -o VIDEO_ID.txt --wrap 900

Output: a .txt file with one paragraph per line, each wrapped to --wrap characters
(default 900) so it's easy to read in offset chunks, with no timestamps, no index
numbers, and no duplicate consecutive lines.
"""

import argparse
import os
import re
import sys

TIMESTAMP_RE = re.compile(r"^\d{2}:\d{2}:\d{2}[.,]\d{3}\s*-->.*$")
INDEX_RE = re.compile(r"^\d+$")
TAG_RE = re.compile(r"</?[a-zA-Z][^>]*>")  # inline vtt tags like <c> or <00:00:01.234>
VTT_HEADER_RE = re.compile(r"^(WEBVTT|Kind:|Language:).*$", re.IGNORECASE)


def clean_lines(raw_text):
    lines = raw_text.splitlines()
    kept = []
    for ln in lines:
        s = ln.strip()
        if not s:
            continue
        if INDEX_RE.match(s):
            continue
        if TIMESTAMP_RE.match(s):
            continue
        if VTT_HEADER_RE.match(s):
            continue
        s = TAG_RE.sub("", s).strip()
        if not s:
            continue
        kept.append(s)

    # collapse consecutive identical (or near-identical) lines — the rolling-caption artifact
    collapsed = []
    for s in kept:
        if collapsed and s == collapsed[-1]:
            continue
        # also collapse when the new line is fully contained in the previous one
        # (common when captions grow word-by-word before repeating)
        if collapsed and s in collapsed[-1]:
            continue
        if collapsed and collapsed[-1] in s:
            collapsed[-1] = s
            continue
        collapsed.append(s)
    return collapsed


def wrap_to_paragraphs(lines, wrap_width=900):
    text = " ".join(lines)
    words = text.split(" ")
    out, cur, n = [], [], 0
    for w in words:
        cur.append(w)
        n += len(w) + 1
        if n > wrap_width:
            out.append(" ".join(cur))
            cur, n = [], 0
    if cur:
        out.append(" ".join(cur))
    return out


def main():
    ap = argparse.ArgumentParser(description="Clean a yt-dlp .srt/.vtt transcript into wrapped plain text.")
    ap.add_argument("input", help="Path to the .srt or .vtt transcript file")
    ap.add_argument("-o", "--output", help="Output .txt path (default: same name, .txt extension)")
    ap.add_argument("--wrap", type=int, default=900, help="Wrap width in characters per paragraph (default 900)")
    ap.add_argument("--stats", action="store_true", help="Print before/after line and character counts")
    args = ap.parse_args()

    if not os.path.exists(args.input):
        print(f"error: {args.input} not found", file=sys.stderr)
        sys.exit(1)

    raw = open(args.input, encoding="utf-8", errors="replace").read()
    collapsed = clean_lines(raw)
    paragraphs = wrap_to_paragraphs(collapsed, args.wrap)
    out_text = "\n".join(paragraphs)

    out_path = args.output or os.path.splitext(args.input)[0] + ".txt"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(out_text)

    if args.stats:
        raw_chars = len(raw)
        out_chars = len(out_text)
        pct = round(100 * (1 - out_chars / raw_chars)) if raw_chars else 0
        print(f"raw:  {len(raw.splitlines())} lines, {raw_chars} chars")
        print(f"clean: {len(paragraphs)} paragraphs, {out_chars} chars ({pct}% smaller)")

    print(f"Wrote: {out_path}")


if __name__ == "__main__":
    main()
