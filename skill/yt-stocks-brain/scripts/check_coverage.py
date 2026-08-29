#!/usr/bin/env python3
"""Flag inventory facts that never made it into a generated brief.

    python3 check_coverage.py <inventory.md> <slug-substring> [--ignore Naam,Visser]

Reads the Section 3 inventory (lines starting "- [ ]"), pulls distinctive tokens out of each
one (numbers-with-units, proper nouns), and reports any line where none of those tokens appears
anywhere in the brief's generated JSON. Exit code 1 if anything is unplaced, so it works as a
gate before committing.

Point it at the SLUG, not at library.json — library.json is only the manifest (no bullets), so
checking against it reports almost every line as missing. This script resolves
research-data/<slug>/<slug>.json for you.

# ponytail: token overlap, not semantics — it surfaces candidates, it does not judge them.
# A flagged line may be a paraphrase that landed fine; a clean run does not prove nothing was
# watered down. Read each flag before acting. Upgrade path if false positives get annoying:
# embed the inventory line and the brief chunks and compare similarity.
"""
import json
import glob
import re
import sys

UNIT = re.compile(r"\d[\d,.]*\s*(?:GW|MW|GWh|kWh|kW|W|bn|B|T|M|k|%|x)\b", re.I)
PROPER = re.compile(r"\b[A-Z][A-Za-z0-9]{3,}\b")


def tokens(text):
    """Distinctive strings worth searching for. Hyphenated coinages are split apart too --
    'Google-vs-librarian' never appears verbatim, but 'librarian' does."""
    out = set(UNIT.findall(text))
    for chunk in re.split(r"[-/]", text):
        out |= set(PROPER.findall(chunk))
    return out


def selftest():
    t = tokens("Google-vs-librarian analogy, 19 GWh batteries at Commonwealth")
    # Hyphenated coinages get split so their real proper nouns become searchable on their own:
    # "Google-vs-librarian" never appears verbatim in a brief, but "Google" does.
    assert "Google" in t, "hyphenated coinages must split apart"
    assert "Google-vs-librarian" not in t, "the coinage itself is unsearchable — don't keep it"
    assert "19 GWh" in t, "numbers with units must survive"
    assert "Commonwealth" in t
    # Lowercase words are deliberately NOT tokens: too weak, they match almost any brief.
    assert "librarian" not in t and "analogy" not in t
    print("selftest ok")
    return 0


def main():
    if "--selftest" in sys.argv:
        return selftest()
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    ignore = set()
    for a in sys.argv[1:]:
        if a.startswith("--ignore"):
            ignore = {w.strip().lower() for w in a.split("=", 1)[-1].split(",") if w.strip()}
    if len(args) != 2:
        sys.exit(__doc__)
    inventory, slug = args

    hits = glob.glob(f"research-data/*{slug}*/*{slug}*.json")
    if not hits:
        sys.exit(f"no brief JSON matching '{slug}' under research-data/ — generate it first")
    brief = hits[0]
    blob = json.dumps(json.load(open(brief))).lower()

    unplaced, checked = [], 0
    for line in open(inventory):
        line = line.strip()
        if not line.startswith("- [ ]"):
            continue
        fact = line[5:].split("—")[0].strip()
        toks = {t for t in tokens(fact) if t.lower() not in ignore}
        if not toks:
            continue  # nothing searchable; falls to the manual read
        checked += 1
        if not any(t.lower() in blob for t in toks):
            unplaced.append((fact, sorted(toks)[:5]))

    print(f"{brief.split('/')[1]}\n  {checked} facts checked, {len(unplaced)} unplaced")
    for fact, toks in unplaced:
        print(f"   - {fact[:100]}\n     looked for: {toks}")
    if unplaced:
        print("\n  Each flag is a candidate, not a verdict — confirm before editing.")
    return 1 if unplaced else 0


if __name__ == "__main__":
    sys.exit(main())
