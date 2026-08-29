---
name: yt-stocks-brain
version: 1.0.0
metadata:
  author: Peter <peter@example.com>
  tags: [youtube, research, transcript, brief, investing, knowledge-graph]
allowed-tools: Read, Write, Bash, Grep, Glob
description: |
  Turn a YouTube video into a clean, standalone HTML + JSON research brief built from the transcript, organized by theme rather than fixed category tables. Handles investment/market videos, tech/AI workflow videos, lifestyle/recommendation videos (supplements, workouts, products), and any mix of these. Use whenever the user gives a YouTube URL and wants a structured research summary. Triggers on: youtube link, "research this video", "analyze this youtube", "summarize the transcript", "make the HTML for this video".
---

# YT Stocks Brain — YouTube Research Brief

Generate a structured, evidence-based, mobile-friendly research brief (HTML + JSON) from any
YouTube video. The content of a video can be investing/market commentary, AI/tech workflows,
lifestyle/product recommendations, quotes-and-culture, or (most often) a mix — the brief adapts
to whichever mix of that is actually in the transcript instead of forcing every video through
the same fixed table set.

## When to use
- User pastes a YouTube URL and asks to "analyze", "research", "summarize", or "do the HTML for" a video.
- User wants a conviction map, stocks/companies breakdown, workflow extraction, product/supplement
  recommendations, or notable quotes from a talk/interview/market update/podcast.

## Workflow (do this in order)

### 1. Fetch metadata + transcript with yt-dlp
Use `yt-dlp` (already installed). Auto-captions usually exist even when manual subs don't.

```bash
yt-dlp --skip-download --print "%(id)s|%(title)s|%(channel)s|%(upload_date)s|%(webpage_url)s" "URL"
yt-dlp --skip-download --write-auto-sub --sub-lang en --convert-subs srt --no-warnings "URL" -o "%(id)s.%(ext)s"
```
If `--sub-lang en` reports no subtitles, retry the full fetch — auto-captions are delivered under
`automatic_captions` and usually still write `VID.en.srt`. If captions truly fail, state the
limitation prominently at the top of the brief.

**Romanian-language videos:** if the video is in Romanian, fetch Romanian captions instead
(`--sub-lang ro`) and write the whole brief — title, snapshot, theme bullets, quotes, everything —
in Romanian, not translated to English. Write it **without diacritics** (ș→s, ț→t, ă→a, î/â→i/a) —
plain ASCII Romanian throughout, matching how the source auto-captions are usually already
rendered.

### 2. Clean the transcript with the bundled script
```bash
python3 <skill-folder>/scripts/clean_transcript.py VIDEO_ID.en.srt --stats
```
Writes `VIDEO_ID.txt` (timestamps/index stripped, duplicate rolling captions collapsed, wrapped to
~900-char paragraphs). Read the full `.txt`, never the raw `.srt`.

### 3. Read for coverage, not just gist — track where every fact will land
Free-form themes have no fixed-table safety net (no guaranteed Conviction Map / Companies / Tech /
Quotes slot), so the real risk isn't missing the gist — it's silently dropping specific numbers,
analogies, and comparisons while compressing a rich transcript into 3-6 cards. Read the whole
cleaned transcript once, and as you read, register every discrete, evidence-carrying fact worth
keeping and roughly which Section 4 theme it belongs to: named numbers/metrics (not just headline
ones), named companies/products (even in passing comparisons), explanatory analogies the speaker
uses (these carry real reasoning, not just color), standalone-quotable lines, opinions the speaker
would be on the hook for (hot takes, contrarian calls, dated predictions — these feed `HOT_TAKES`),
and named sources, dates, or forward-looking claims. For a short, single-topic video a direct read-and-place pass is
enough; past the thresholds below, write the list.

Write an explicit flat inventory list before drafting themes — one line per fact, checked off
against the drafted `bullets`/`quote`/`watch`/`names` once themes are written — whenever **any** of
these holds: the cleaned `.txt` exceeds ~50k characters (`wc -c` it after Section 2); the video is a
multi-hour or multi-speaker panel; it covers many distinct stories; or the user asked for
exhaustive/"deep" coverage. Don't agonize over the call — a 59-minute single-guest interview at 63k
chars still surfaced facts that a read-and-place pass had dropped. Put the inventory in the
scratchpad directory, not the project.

Either way, a fact that doesn't fit any theme goes to `OTHER_NEWS` or `GLOSSARY` — it must land
somewhere, never get dropped for being "minor." If a theme's bullet cap (below) is too tight to
hold everything that belongs there, that's a signal the thread is actually two themes, not a reason
to cut a fact. Section 7's coverage re-scan is the actual guarantee against drops — treat it as
mandatory even when you skip the written inventory.

### 4. Identify the video's content mix, then find THEMES (not fixed tables)
First, classify what's actually in the transcript — most videos are a mix of:
- **Market/investing**: positions, conviction, stocks/funds, macro calls
- **Tech/AI**: workflows, tools, prompts, product/model releases
- **Lifestyle/recommendations**: products, supplements, workouts, media, travel, habits
- **Culture/quotes/geopolitics**: opinions, notable quotes, non-investment news

Set `META["category"]` from this classification: `"market"` when investing/market content is
present at all (even mixed with other types — this is the default and covers most videos), or
`"dev"` when the video is dev/systems/knowledge/AI-workflow content with no market angle (e.g. a
career-advice or coding-practice video like "Why Most Devs Stop Improving"). This one field decides
which `index.html` tab the brief appears under (Section 6) and which color/badge vocabulary applies
below.

Then read across the WHOLE transcript and group related facts into **3-6 self-contained themes**
— a theme is a real topic thread the speaker returns to (e.g. "a hedge fund unwind," "the
hyperscaler capex debate," "a new harness-design practice," "a supplement stack change"), not a
content-type bucket. A theme pulls together whatever applies to it: a stance/conviction if it's
an investment view, a company/product mini-profile, a pull-quote, a "not settled yet" watch-flag,
a reusable workflow — all in one card. This is the single most important step: it replaces the
old pattern of splitting the same facts across a Conviction Map table, a Companies table, a Tech
table, and a Quotes section. **If a fact would appear in two theme cards, it belongs in whichever
one it's most central to — mention it once, not twice.**

For each theme, capture:
- `id` (short anchor slug), `color`, `badge`, `status` — see the category-conditional rules below;
  these three fields carry different meaning depending on `META["category"]`.
- `title` — a specific, concrete headline (not a category name)
- `lead` — one bold sentence giving the point before any detail
- `bullets` — 3-5 short, concrete, evidence-carrying bullets as the norm; flex to 6-7 rather than
  cutting a fact when a thread is genuinely dense (e.g. an earnings-call theme with many distinct
  guided figures) — never a dense paragraph either way (see Section 7)
- `quote` (optional) — the single best verbatim quote for this theme, or none
- `watch` (optional) — an explicit "this isn't settled" caveat when the speaker themselves
  hedges
- `names` (optional) — see the category-conditional rules below; omit entirely (`None`) when a
  theme has no company/product/person worth naming, which is common and fine outside `market`.

**Category-conditional vocabulary** (`META["category"]`, set above):

- **`category: "market"`** (investing/AI-news mix, stocks/funds/macro): `color` is a stance signal
  — `green`=positive/bullish/confirmed-good, `amber`=mixed/contested/one-eye-open, `gray`=
  speculative/low-confidence, `red`=negative/bearish/red-flag. `badge`/`status` use conviction
  language: `badge` e.g. "High conviction" / "Contested" / "Speculative" / "Confirmed event";
  `status` e.g. "HOLDING — reduced but not exited", "RELEASED July 27, 2026". Any stance/conviction
  wording is never inferred — label only what's explicitly said: `OWNS` / `BUYING-ADDING` /
  `WATCHING` / `POSITIVE VIEW` / `NEGATIVE VIEW` / `CASUAL MENTION` / `UNCERTAIN`, with conviction
  `High` (clear thesis + explicit action/holding + repeated emphasis) / `Medium` (clear view + some
  reasoning, no confirmed action) / `Low` (passing/speculative). For any publicly-tradeable entity
  in `names`, write `"Company (TICKER)"` (e.g. `"Nvidia (NVDA)"`, `"RSP"` for a bare-ticker ETF) —
  the index's cross-reference view parses this pattern into a per-ticker mention history across
  every brief. Several tickers sharing one bullet get comma-separated in `name`, e.g. `"Apollo,
  BlackRock, KKR"`, so each gets its own index entry.

  **`names` is the permanent cross-reference index, not a general "notable things" slot.** Every
  entry becomes a row in the By Company/Ticker view spanning every brief in the library, forever.
  Companies, funds and organizations belong there — and so do investable asset classes/commodities
  the speaker takes a position on (crypto — `"Bitcoin (BTC)"`, `"Ethereum (ETH)"` — and metals/ETFs
  — `"Gold"`, `"Silver"`, `"GLD"` — are explicit, confirmed exceptions; this was a standing
  instruction, not a default). Countries, regions, and non-investable product/model names or
  technologies still do NOT belong there — put those in `bullets`. A `names` entry of `"Australia,
  Chile, Mexico"` creates three country rows in the ticker index; `"Natrium, BWRX-300"` creates two
  rows for reactor designs that aren't companies. Use the comma-split deliberately: only when you
  genuinely want each side indexed separately (a bloc like `"JPMorgan (JPM), Goldman Sachs (GS)"`
  is the intended use); otherwise join with `/` or a word, e.g. `"Natrium / BWRX-300 class"`.

  **Use the plain canonical form for a company you've named before, not a decorated variant.**
  The index groups rows by exact string match, so `"Nvidia"` and `"NVIDIA"`, or `"CoreWeave"` and
  `"CoreWeave (comparison)"`, become two separate rows for the same company instead of one combined
  history. Default to the bare `"Company (TICKER)"` form; only append a parenthetical qualifier
  (`"(supply chain)"`, `"(comparison)"`) when the distinction is actually load-bearing for that
  entry, and prefer folding that nuance into the `blurb` instead. When unsure what form a company
  has used before in this library, a quick check keeps it consistent:
  `python3 -c "import json;d=json.load(open('library.json'));print(sorted({e['display'] for b in d['briefs'] for e in b['entities'] if 'nvidia' in e['display'].lower()}))"`
  (swap the search term). This is a forward-looking hygiene habit, not a mandate to go back and
  fix older entries — existing variant rows are left as-is unless the user asks for a cleanup pass.

  **Never write a name you can only reach by guessing through a garbled caption.** Auto-captions
  mangle proper nouns constantly (ERCOT→"Urkott", FERC→"FK", Cerebras→"Cerrus", Cagney→"Kagny",
  Warsh→"Worsh", KOSPI→"Cosby"). Resolving an obvious one is fine; guessing at a company you can't
  identify is not, because `names` and tickers are durable index data and a wrong entry is
  permanent damage. When you can't identify a company with confidence, describe it by spec in a
  bullet ("a ~10 MW micro-reactor firm building five-unit pods") and leave it out of `names`
  entirely. Note the unresolved ones in `RISKS`.

- **Any other `category`** (e.g. `"dev"` — dev/systems/knowledge/AI-workflow content, or a future
  category): don't force stock-conviction vocabulary onto content that isn't a stance on an asset.
  `color` marks how settled/confidence-worthy the claim is, not bullish/bearish: `green`=confirmed-
  good/validated, `amber`=mixed/contested/one-eye-open, `gray`=speculative/opinion/unverified,
  `red`=flagged as a real problem or risk (not "this is a bearish stock call" — there's no stock).
  `badge` describes the *character* of the claim instead of a conviction level: "Recommendation" /
  "Structural critique" / "Skill-atrophy warning" / "Self-critique, since resolved" / "Confirmed
  event". `names` and ticker formatting are optional and often irrelevant — use plain names with no
  `(TICKER)` suffix, or omit the field, when there's nothing to cross-reference.

MANDATORY — capture non-investment signal too, wherever it fits best (inside a theme if it's
central to one, otherwise in Other Notable News): strong convictions/opinions on any topic,
recommendations (products, tools, supplements, workouts, media, travel, safety), notable
non-stock news (cybersecurity, energy, space, science, health, policy, culture), and any
standout verbatim quotes not already used inside a theme.

MANDATORY — capture references to other sources by name: any other podcast, show, channel,
publication, article, book, or person the speakers cite as where a claim or number came from, or
name as someone they follow/trust/recommend (e.g. "I heard this on the All-In podcast," "Bloomberg
reported," "this is the Joshua Kushner framework"). If the reference is central to a theme (it's
where that theme's key fact or figure came from), fold it into that theme's bullets or `quote` —
don't create a parallel section for something that already has a home. If several small references
don't anchor to any one theme, group them into a single `OTHER_NEWS` entry (e.g. "Sources referenced
this episode: ..."). A show naming zero outside sources is common and fine — say so briefly rather
than leaving the reader to wonder if you missed something; never pad this out with vague "as
reported elsewhere" hand-waving when no specific source was named. Vague attributions ("some
people," "you often hear") are opinions to capture in bullets, not references — only capture a
named source or a named person's stated view.

EXCLUDED — sponsor content never goes in the brief. Skip paid sponsorship segments, "this video
is sponsored by" reads, host-endorsed sponsor products/tools, and sponsor discount codes/links
entirely — do not give them a theme, an OTHER_NEWS entry, a RISKS caveat, or a GLOSSARY term. If
a sponsor segment interrupts an otherwise substantive discussion mid-transcript, skip only the
sponsor material and continue capturing the surrounding content normally.

### 5. Fill in the remaining sections
- `SNAPSHOT` — 5-8 scannable bullets, the one-paragraph read of the whole video (unchanged from
  before; this is a bulleted list, never one dense paragraph).
- `TAKEAWAYS` — 4-6 short, imperative, DISTINCT actions. If a takeaway just restates a theme's
  bullet verbatim, cut it — takeaways are the "so what do I do" layer, not a recap.
- `RISKS` — meta caveats about trusting THIS source (sponsorships, self-reported claims, auto-
  caption errors, conflicts of interest). Don't repeat a theme's own `watch` flag here — that's
  a different kind of caveat (about the claim), this one is about the source.
  **Label provenance; don't send the reader off to verify.** These briefs carry forward-looking
  opinion, speculation and fresh connections — material that mostly can't be fact-checked and
  isn't meant to be. The brief's job is faithful transmission of what was said, never adjudicating
  whether the speaker is right. So write "these are his working numbers, quoted in conversation
  rather than read off a report" — not "verify before acting on any of them." Avoid audit
  vocabulary (`unverified`, `uncorroborated`, `unsubstantiated`) and imperatives telling the reader
  to go check. Flagging a conflict of interest, an undisclosed position or a claim the speaker
  himself hedges is always in scope; grading the truth of a prediction is not.
- `HOT_TAKES` — 0-6 opinions the speaker personally owns and would be quoted on: hot takes,
  contrarian/unpopular calls, personal convictions, dismissals ("X is dead", "nobody needs Y"),
  and predictions carrying a number or a date. Shape: `{"take": ..., "cite": "— Speaker",
  "why": short context}`. `take` is verbatim or near-verbatim, tightened only for caption noise —
  never paraphrased into neutral prose, because the value here is the speaker's own phrasing and
  the risk they took saying it.
  **The test is exposure, not volume:** would a reasonable listener disagree, or is the speaker
  on the hook if it's wrong? A number, date, or ranking makes it a take; "AI is important"
  does not. Include takes on any subject, not just the investable ones.
  This section is a lens on material that mostly already lives in the themes, so the Section 4
  no-duplicate rule does NOT apply to it — a line can be a theme's `quote` and a hot take. Do not
  invent a separate theme bullet just to host one. If a video is pure reporting with no
  neck-out opinions, leave it empty and let the placeholder say so.
- `OTHER_NEWS` — only items that don't fit inside any theme. If everything folds into a theme,
  it's fine for this section to end up short or empty — never pad it.
- `GLOSSARY` — compact term/definition pairs, tightened to one sentence each.

Any list left empty renders an honest "nothing found" placeholder — never fabricate content to
fill a section.

### 6. Generate outputs
`generate.py` itself is never edited per video — it takes a per-video **data file** as an
argument instead. Copy `<skill-folder>/scripts/TEMPLATE.py` into the working directory (any filename,
e.g. `_data.py`), fill in `META`, `SNAPSHOT`, `THEMES`, `TAKEAWAYS`, `RISKS`, `HOT_TAKES`, `OTHER_NEWS`,
`GLOSSARY`, then:

```bash
python3 <skill-folder>/scripts/generate.py <data-file>.py
```

Outputs (channel-first naming so same-creator videos group together in Finder/`ls`, with the
upload date giving chronological order within each creator):
- `<slug-channel>_<date>_<slug-title>.html` — standalone, responsive brief, written to the
  **current working directory**.
- `<slug-channel>_<date>_<slug-title>.json` — same structured data, written to
  **`research-data/<slug-channel>_<date>_<slug-title>/`** (created automatically).
- `<slug-channel>_<date>_<slug-title>_data.py` — an archived copy of the data file you passed
  in, written to that same `research-data/<slug>/` folder, so the brief can be regenerated or
  hand-edited later without re-deriving it from the transcript.
- `index.html` — rebuilt at the **working directory root** every run: a single searchable page
  with four tabs — **All Briefs** (chronological, every category), **By Channel**, **By Company /
  Ticker**, and **Dev & Workflows** (briefs with `META["category"] == "dev"` only). The ticker view
  parses every theme's `names` field (current schema) or `conviction_map` topic (legacy schema)
  into a cross-reference: click a ticker's group to see every brief that mentioned it, with date,
  channel, stance color, and blurb — this is what turns a growing pile of briefs into an
  investing-thesis tool instead of just a list of pages. Run `python3 <skill-folder>/scripts/generate.py
  --reindex` to rebuild it standalone (e.g. after manually deleting or renaming a brief).
- `library.json` — rebuilt alongside `index.html` at the **working directory root**: a flat
  machine-readable manifest of every brief plus its extracted ticker/company entities, meant to
  be fed directly into an external AI/knowledge-graph tool rather than scraped from the HTML.

Filename convention: lowercase, non-alphanumerics → single hyphen, diacritics stripped, date as
`YYYY-MM-DD` (from `META["date"]`). Example: `jordi-visser_2026-08-09_the-ai-crash-is-over.html`.
After generating, move the raw transcript and cleaned `.txt` into that same `research-data/<slug>/`
folder, and delete the data-file copy from the working directory root (the archived copy in
`research-data/` is the one that persists) — the working folder root should only ever gain the
finished `.html` plus the refreshed `index.html`.

**Fixing a brief after the root data file is gone:** edit the archived
`research-data/<slug>/<slug>_data.py` in place and run `generate.py` against that path. It
regenerates the `.html`, rewrites the `.json`, re-archives the data file over itself, and rebuilds
`index.html` + `library.json` — no need to copy anything back to the root. Use this for every
correction pass rather than re-deriving a fresh data file from the transcript.

### 7. Quality check before saving
- Re-scan the full cleaned transcript against the drafted data lists: every named number, company/
  product, analogy, standalone quote, and forward-looking claim you noted in Section 3 is placed in
  a theme, `OTHER_NEWS`, or `GLOSSARY`. If you wrote an explicit inventory list, check every line
  off; anything unchecked (or, without a written list, anything you notice on re-scan that isn't
  represented) gets added, not dropped for length.
  **Do this against the inventory file itself, line by line — not against your memory of the
  themes.** Recalling what you wrote and believing it complete is how facts get dropped. When you
  wrote an inventory, run the bundled checker instead of eyeballing it:
  ```bash
  python3 <skill-folder>/scripts/check_coverage.py <inventory.md> <slug-substring> --ignore=SpeakerSurname
  ```
  It pulls distinctive tokens (numbers-with-units, proper nouns) out of every `- [ ]` line and
  reports any fact with no trace in the generated brief JSON; exit code 1 means something is
  unplaced. Point it at the slug, never at `library.json` — that file is only the manifest and
  contains no bullets, so checking against it reports nearly every fact as missing. Each flag is a
  candidate, not a verdict: a paraphrase can land fine and still trip it, and a clean run doesn't
  prove nothing was watered down. Read every flag before editing. **A fact is never
  dropped for being "minor."** If a theme's bullet cap won't hold everything that belongs there,
  the thread is two themes — that is not a licence to cut. Anything that fits no theme goes to
  `OTHER_NEWS` or `GLOSSARY`, or gets appended to the most closely related existing bullet.
- Verify the extracted entities before committing — this catches `names` pollution (Section 4)
  in one command instead of relying on memory:
  ```bash
  python3 -c "import json;d=json.load(open('library.json'));b=d['briefs'][0];print(b['html']);print([e['display'] for e in b['entities']])"
  ```
  Every row must be a company/fund/organization. A country, product name or concept in that list
  means a `names` entry needs to move into `bullets`.
- No fact appears in two theme cards (see the dedup rule in Section 4). `HOT_TAKES` is exempt —
  it deliberately re-surfaces lines that also live in a theme.
- `HOT_TAKES` entries are verbatim/near-verbatim and each one would actually make someone
  disagree or hold the speaker to it. A bland consensus statement in there means it should be cut.
- Every major claim has transcript evidence; ownership/buying intent is never inferred.
- Bullets are short and concrete — no dense multi-sentence paragraphs inside a theme.
- HTML well-formed, closes `</html>`.
- Working folder root only gained the `.html`; transcript/JSON live in `research-data/<slug>/`.

## HTML/CSS design
Already implemented in `generate.py` (see the "HTML/CSS DESIGN" comment block near the top of the
file) — cream editorial page, color-coded theme cards with sidecards, mobile-first CSS with no
media queries. `generate.py` itself is never edited per video (Section 6), so this doesn't need to
be reasoned about while writing a data file — only open that comment block if you're actually
changing the template/CSS.
