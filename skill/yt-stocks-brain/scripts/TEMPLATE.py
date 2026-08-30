"""
Per-video data for youtube-research-brief. Copy this file, fill in every field, then:

    python3 <skill-folder>/generate.py <this-file>

See SKILL.md Section 3 (coverage/inventory) and Section 4 (themes, incl. category-conditional
color/badge/names rules) for what belongs where and the rules for each field (dedup, labeling,
bullet counts, etc.) — this file only has the shape.
"""

META = {
    "title": "",
    "channel": "",
    "speakers": "",
    "date": "",           # YYYY-MM-DD, video upload date — drives filename + index sort order
    "video_url": "",
    "thread_line": "",    # e.g. "5 threads · short summary of each thread"
    "category": "market", # "market" (investing/AI-news, default) or "dev" (dev/systems/knowledge/
                           # AI-workflow content) — drives which index.html tab the brief appears in
}

SNAPSHOT = [
    # 5-8 scannable bullets: the one-paragraph read of the whole video
]

THEMES = [
    {
        "id": "",              # short anchor slug, e.g. "elon-thesis"
        "color": "green",      # green | amber | gray | red
        "badge": "",           # e.g. "High conviction" / "Contested" / "Speculative" / "Recommendation"
        "status": "",          # one caps line of context, e.g. "RELEASED JULY 27, 2026"
        "title": "",           # specific, concrete headline (not a category name)
        "lead": "",            # one bold sentence giving the point before any detail
        "bullets": [
            # 3-5 short, concrete, evidence-carrying bullets; flex to 6-7 for dense threads
        ],
        "quote": None,         # {"text": "...", "cite": "— speaker"} or None
        "watch": None,         # str caveat ("this isn't settled") or None
        "names": None,         # [{"name": "...", "blurb": "..."}] or None
    },
    # 3-6 themes total
]

TAKEAWAYS = [
    # {"icon": "\U0001F3AF", "tag": "...", "title": "..."} × 4-6, imperative and distinct
    # tag = short topic category (1-3 words: "Markets", "Macro", "AI ethics", "Health", "Energy",
    # "Geopolitics", "Crypto", "Robotics", "Space", "Policy", "Careers", ...) — not an action verb.
    # Renders inline, leading the line: "Markets: Track RSP and IGV first..." — title carries the verb.
]

RISKS = [
    # str × 3-5 — meta caveats about trusting THIS source (sponsorships, self-reported
    # claims, auto-caption errors, conflicts of interest), not a theme's own watch flag
]

HOT_TAKES = [
    # {"take": "...", "cite": "— Speaker", "why": "short context: what makes it a take"} × 0-6
    # only take + cite render (cite inline, end of the same line) — why is a drafting aid only
    # Verbatim-or-near-verbatim opinions the speaker owns: hot takes, unpopular/contrarian calls,
    # personal convictions, predictions with a number or date, dismissals. See SKILL.md Section 5.
]

OTHER_NEWS = [
    # {"icon": "...", "title": "...", "tag": "..."} or leave as [] if everything folded into a theme
]

GLOSSARY = [
    # {"term": "...", "def": "..."} × as needed, one tightened sentence each
]
