# YT Stocks Brain — Project Notes

Library of structured research briefs generated from YouTube videos (investing/AI-news podcasts,
crypto/market interviews, and dev/career/workflow content), built toward a future knowledge
graph/brain over stocks, investing, and industry trends. Static HTML, no build step, no deps.

## Repo
- **Remote:** https://github.com/hutuleac/YT-Stocks-Brain.git (`main` branch, no other branches used)
- **Live site:** https://hutuleac.github.io/YT-Stocks-Brain/ — GitHub Pages serving `main` branch root
- Working directory root should only ever gain the finished `.html` brief + the refreshed
  `index.html`/`library.json`. Everything else (transcripts, JSON, archived data files) lives in
  `research-data/<slug>/`.
- **Future knowledge-graph build:** use `library.json` + per-brief `.json` as the source (already
  structured: themes, entities/tickers, quotes). Don't parse HTML (pure presentation, redundant
  with the JSON it's generated from) or transcripts (too noisy for direct extraction) — transcripts
  stay archived in `research-data/<slug>/` as the citation/ground-truth layer only.

## Generating a brief
Use the **yt-stocks-brain** skill (`~/.claude/skills/yt-stocks-brain/SKILL.md`) for
every new video. It fetches the transcript via `yt-dlp`, cleans it, and drives `generate.py` off a
per-video Python data file (never edit `generate.py` itself per video). Read the skill file fresh
each time — it gets tuned periodically and this doc is not a substitute for it.

Key things baked into the current skill that aren't obvious from a first read:
- **`META["category"]`** is `"market"` (default — investing/AI-news mix) or `"dev"` (dev/systems/
  knowledge/AI-workflow content, no market angle). This drives which `index.html` tab a brief
  lands under, and which color/badge vocabulary applies (stock-conviction language for `market`;
  descriptive "character of the claim" language for anything else — never force ticker/stance
  vocabulary onto non-market content).
- **Sponsor content is always excluded.** No sponsor segment, plug, discount code, or "this video
  is sponsored by" read ever goes into a brief — not as a theme, OTHER_NEWS item, RISKS caveat, or
  glossary term. This was an explicit standing instruction, not a default of the skill template.
- `index.html` has four tabs: All Briefs, By Channel, By Company/Ticker, and Dev & Workflows
  (filtered to `category: "dev"`). Rebuilt automatically on every `generate.py` run, or standalone
  via `python3 <skill-folder>/generate.py --reindex`.
- **`names` is the permanent ticker index, not a general "notable things" slot.** Every entry
  becomes a row in By Company/Ticker across every brief, forever — companies/funds/orgs only.
  Countries, product and model names, and concepts go in `bullets`. Comma-splitting is
  deliberate (`"JPMorgan (JPM), Goldman Sachs (GS)"` = two rows); join with `/` when you don't
  want a split. Verify after generating:
  `python3 -c "import json;d=json.load(open('library.json'));b=d['briefs'][0];print(b['html']);print([e['display'] for e in b['entities']])"`
- **RISKS labels provenance; it never sends the reader off to verify.** These briefs carry
  forward-looking opinion that mostly can't be fact-checked and isn't meant to be. Flagging a
  conflict of interest or an undisclosed position is always in scope; grading the truth of a
  prediction is not. No audit vocabulary (`unverified`, `uncorroborated`).
- **Coverage is checked mechanically, not from memory:**
  `python3 <skill-folder>/check_coverage.py <inventory.md> <slug> --ignore=Surname`
  Point it at the slug, never at `library.json` — that's the manifest and has no bullets, so it
  reports nearly every fact as missing. Exit 1 means something is unplaced.
- **Fixing a brief after the root data file is deleted:** edit
  `research-data/<slug>/<slug>_data.py` in place and run `generate.py` against that path.

## Sibling repo
**YT-Lessons** (`~/Projects/OpenCode/YT-Lessons`, remote `hutuleac/YT-Lessons`) turns short-form
video into teaching lessons via the **youtube-lessons** skill. Different artifact — a brief is for
recall, a lesson is for comprehension. Short-form content goes there, not here; don't force a
300-word short through this repo's theme structure.

## Git conventions for this repo
- **Never add a `Co-Authored-By: Claude...` trailer to commits** in this repo — removed once
  already by explicit request, don't reintroduce it.
- Commit and push after generating each new brief (or batch of briefs) unless told otherwise.
- Local tool directories (`.claude/`, `.gstack/`, `.opencode/`, `.DS_Store`) are gitignored —
  they're editor/agent tooling, not project content, and don't belong in this repo.
