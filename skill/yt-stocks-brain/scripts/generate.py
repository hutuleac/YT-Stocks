#!/usr/bin/env python3
"""
YouTube Research Brief generator (v3 — data-file driven, theme-grouped, mobile-first).

This script never needs editing per video. Instead, create a per-video data file
(copy TEMPLATE.py, fill in META / SNAPSHOT / THEMES / TAKEAWAYS / RISKS / OTHER_NEWS /
GLOSSARY — see SKILL.md Sections 3-5 for what each field means), then:

    python3 generate.py <data_file.py>

Writes:
  <slug-channel>_<date>_<slug-title>.html       -> current working directory
  <slug-channel>_<date>_<slug-title>.json       -> research-data/<same-slug>/
  <slug-channel>_<date>_<slug-title>_data.py     -> research-data/<same-slug>/ (archived copy
                                                     of the data file, so the brief can be
                                                     regenerated or edited later)
  index.html                                     -> current working directory, rebuilt from
                                                     every research-data/*/*.json found

Rebuild just the index (e.g. after manually deleting/renaming a brief) without generating
a new one:

    python3 generate.py --reindex

---------------------------------------------------------------------------------------------
HTML/CSS DESIGN — "Editorial Refined, Theme-Grouped" (v2). Implemented below; not reasoned
about per-brief. Only read this if you're actually changing the template/CSS, not when writing
a data file for a video.
---------------------------------------------------------------------------------------------
- Single page, full page width (max ~1600px), cream body (--bg:#efece2) with a warm white page
  card (--card:#fffdf8) and warm line color #e4e2d8 — no dark hero banner.
- Serif headlines (Iowan Old Style/Palatino Linotype/Georgia fallback) for titles, section heads,
  and quotes; system sans for body copy — this pairing is the "analyst report" read.
- Amber/brown brand accent (--brand:#8a5a2e) for kickers, italic eyebrows, and section-heading
  underlines. Header has NO separate "Watch on YouTube" button — it's a small inline link folded
  into the one-line stats row under the byline, to save space.
- Themes, not tables. The main content is a stack of theme-card <section>s (one per theme, 3-6
  total), each with: a color-coded status badge (solid fill, white text — not a pale tint — for
  genuinely obvious at-a-glance scanning) + a caps status line; a bold headline with a colored
  left accent bar in the theme's stance color; a bold one-line lead; 3-5 short bullets (never
  paragraphs) with a dot marker in the theme's color, in the main (left) column. Bullets/badge/
  title-bar all sharing one color per theme is what makes the coding "obvious" rather than
  decorative.
- Side column ("theme-side") is a stack of up to three "sidecards," always in this order:
  pull-quote, names-in-play, worth-noting. Every sidecard shares one shape (rounded card, thin
  colored left bar, small caps label) so the reader learns the pattern once — only the accent
  color changes, and that color is the fast-scan signal for what kind of side content it is:
  pull-quote uses the theme's own stance color (it's telling you more about this theme);
  names-in-play uses a fixed neutral slate #65695f (it's reference material, not a stance
  signal); worth-noting uses a fixed amber #93711b regardless of the theme's stance color (it
  always reads as "caution," even inside a green/high-conviction theme). Any of the three is
  omitted if the theme has nothing for it — never an empty card.
- Stance colors (theme accent bar, badge, bullet dots, pull-quote sidecard only): green
  #3f6b2e = positive/confirmed-good, amber #93711b = mixed/contested/one-eye-open, gray
  #65695f = speculative/low-confidence, red #a23f22 = negative/bearish. Names-in-play and
  worth-noting sidecards do NOT use the theme's stance color — they use their own fixed colors
  (above) so they stay visually consistent and scannable across every theme regardless of that
  theme's stance.
- No "Jump to a thread" nav strip — it was removed as low-value chrome that just ate vertical
  space; the reader scrolls straight from the snapshot into the theme cards.
- Takeaways and Other Notable News are icon-only cards (no colored side accent bar — keep those
  reserved for theme cards so the color-coding stays meaningful, not decorative everywhere).
  Risk/caveat cards keep a red-orange side accent bar since they're explicitly about doubt. No
  warning-triangle glyph anywhere — a plain colored bar carries the "caution" meaning.
- Glossary renders as a grid-template-columns:repeat(auto-fill,minmax(260px,1fr)) grid — pure
  CSS, no media query needed, it reflows column count on its own as the viewport narrows.
- Mobile-first, no hidden columns. There is no data table anywhere in the main content, so
  there is nothing to hide on small screens. Layout is done entirely with flex-wrap:wrap + CSS
  grid auto-fill/auto-fit + clamp() for type/spacing — this reflows continuously from a phone
  (iPhone-width) to a full desktop window without a single @media breakpoint, and without ever
  cutting a column of information.
- No external deps, no JS frameworks, no CDNs.
"""
import glob
import importlib.util
import json
import os
import re
import shutil
import sys
import unicodedata

sys.dont_write_bytecode = True  # don't litter the working directory with __pycache__

REQUIRED_FIELDS = ["META", "SNAPSHOT", "THEMES", "TAKEAWAYS", "RISKS", "OTHER_NEWS", "GLOSSARY"]
# HOT_TAKES is optional so data files written before it existed still regenerate.


def load_data(path):
    spec = importlib.util.spec_from_file_location("video_data", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    missing = [f for f in REQUIRED_FIELDS if not hasattr(mod, f)]
    if missing:
        sys.exit(f"{path} is missing required field(s): {', '.join(missing)}")
    if not hasattr(mod, "HOT_TAKES"):
        mod.HOT_TAKES = []
    return mod


# ---------------------------------------------------------------------------
# GENERATOR — should not need editing per video
# ---------------------------------------------------------------------------

STANCE_COLORS = {
    "green": "#3f6b2e",
    "amber": "#93711b",
    "gray": "#65695f",
    "red": "#a23f22",
}

CSS = """
:root{
  --ink:#20231f; --muted:#6b6f66; --line:#e4e2d8; --card:#fffdf8; --bg:#efece2;
  --brand:#8a5a2e; --serif:'Iowan Old Style','Palatino Linotype',Georgia,serif;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink);
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif;
  font-size:clamp(15px,1.05vw,18px);line-height:1.7;-webkit-font-smoothing:antialiased;}
.page{max-width:1600px;width:100%;margin:0 auto;background:var(--card);box-shadow:0 0 0 1px var(--line);}
.hero{padding:clamp(18px,2.4vw,34px) clamp(18px,4vw,56px) clamp(14px,1.8vw,22px);border-bottom:1px solid var(--line);}
.kicker{font-family:var(--serif);font-style:italic;font-size:clamp(13px,1vw,16px);color:var(--brand);margin-bottom:10px;}
.backlink{margin-bottom:12px;}
.backlink a{font-size:clamp(12.5px,.95vw,14px);color:var(--muted);text-decoration:none;border:1px solid var(--line);
  border-radius:20px;padding:5px 14px;transition:color .15s,border-color .15s;}
.backlink a:hover{color:var(--brand);border-color:var(--brand);}
.hero h1{font-family:var(--serif);margin:0 0 14px;font-size:clamp(24px,3.4vw,42px);line-height:1.15;
  letter-spacing:-.01em;font-weight:600;color:#171916;max-width:42ch;}
.byline{border-top:1px solid var(--line);padding-top:12px;color:var(--muted);font-size:clamp(13px,1vw,15px);line-height:1.6;}
.byline b{color:var(--ink);font-weight:600;}
.stats-line{font-family:var(--serif);font-style:italic;color:var(--brand);font-size:clamp(12.5px,.95vw,14.5px);margin-top:4px;}
.stats-line a{color:var(--brand);}
.inner{padding:10px clamp(18px,4vw,56px) 48px;}
section.sec{padding:34px 0;border-bottom:1px solid var(--line);}
.sec-eye{font-family:var(--serif);font-style:italic;font-size:14px;color:var(--brand);margin-bottom:4px;}
.sec h2{font-family:var(--serif);margin:0;font-size:clamp(20px,2vw,26px);font-weight:600;color:#171916;
  border-bottom:2px solid var(--brand);display:inline-block;padding-bottom:5px;}
.card{background:#fbf7ef;border:1px solid var(--line);border-radius:14px;padding:clamp(18px,3vw,28px);}
.snap{list-style:none;margin:0;padding:0;}
.snap li{padding:12px 0;border-bottom:1px solid var(--line);line-height:1.6;font-size:clamp(14.5px,.95vw,16.5px);}
.snap li:last-child{border-bottom:none}
.theme{padding:36px 0;border-bottom:1px solid var(--line);}
.theme-badgerow{display:flex;flex-wrap:wrap;align-items:center;gap:10px 14px;margin-bottom:10px;}
.badge{display:inline-block;padding:5px 13px;border-radius:3px;font-size:12px;font-weight:700;
  white-space:nowrap;letter-spacing:.03em;text-transform:uppercase;color:#fffdf8;}
.theme-status{font-family:var(--serif);font-style:italic;font-size:13.5px;color:var(--muted);}
.theme h2{font-family:var(--serif);margin:0 0 20px;font-size:clamp(20px,2.2vw,28px);font-weight:600;
  color:#171916;line-height:1.25;max-width:32ch;padding-left:16px;}
.theme-body{display:flex;flex-wrap:wrap;gap:28px;}
.theme-main{flex:3 1 400px;min-width:0;}
.theme-side{flex:2 1 260px;min-width:0;}
.lead{margin:0 0 18px;font-size:clamp(16px,1.15vw,19px);line-height:1.6;color:#171916;font-weight:600;max-width:70ch;}
.bullets{list-style:none;margin:0 0 22px;padding:0;max-width:76ch;}
.bullets li{position:relative;padding:9px 0 9px 20px;border-bottom:1px solid var(--line);
  font-size:clamp(14px,.95vw,15.5px);line-height:1.65;color:#2c2f28;}
.bullets li .dot{position:absolute;left:0;top:16px;width:7px;height:7px;border-radius:50%;}
.sidecard{position:relative;background:#fffefb;border:1px solid var(--line);border-radius:12px;
  padding:14px 16px 14px 26px;max-width:76ch;margin:0 0 18px;}
.sidecard:last-child{margin-bottom:0;}
.sidecard::before{content:"";position:absolute;left:11px;top:12px;bottom:12px;width:7px;border-radius:5px;
  background:var(--sc-accent);}
.sidecard .lbl{font-size:11.5px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;
  color:var(--sc-accent);margin-bottom:8px;}
.sidecard.quote{font-family:var(--serif);font-style:italic;font-size:clamp(15px,1.1vw,18px);
  line-height:1.5;color:#2c2f28;}
.sidecard.quote .lbl{font-family:-apple-system,sans-serif;font-style:normal;}
.sidecard.quote cite{display:block;font-family:-apple-system,sans-serif;font-style:normal;font-size:13px;
  color:var(--muted);margin-top:9px;}
.sidecard .txt{font-size:14.5px;line-height:1.55;color:#3a3d35;}
.namechip{padding:0 0 10px;margin:0 0 10px;border-bottom:1px solid var(--line);}
.namechip:last-child{padding-bottom:0;margin-bottom:0;border-bottom:none;}
.namechip b{display:block;font-weight:600;font-size:14.5px;color:#171916;}
.namechip span{font-size:13px;color:#4a4d44;line-height:1.5;}
.icard{display:flex;gap:14px;align-items:flex-start;background:#fffefb;border:1px solid var(--line);
  border-radius:12px;padding:14px 16px;margin:11px 0;}
.icard .ic{flex:none;width:30px;height:30px;border-radius:6px;display:grid;place-items:center;
  font-size:14px;background:#f4e9db;line-height:1;}
.icard .title{font-weight:600;font-size:clamp(14px,.95vw,15.5px);color:#171916;line-height:1.42;margin-bottom:5px;}
.icard .tag{display:inline-block;font-family:var(--serif);font-style:italic;font-size:13px;font-weight:600;color:var(--brand);}
.icard .detail{font-size:13.5px;color:#4a4d44;line-height:1.55;margin-top:4px;}
.icard .tline{font-size:clamp(14px,.95vw,15.5px);line-height:1.48;}
.icard .tline .cat{font-family:var(--serif);font-style:italic;font-weight:700;color:var(--brand);margin-right:6px;}
.icard .tline .txt{font-weight:600;color:#171916;}
.riskcard{position:relative;background:#fffefb;border:1px solid var(--line);border-radius:12px;
  padding:14px 18px 14px 28px;margin:11px 0;}
.riskcard::before{content:"";position:absolute;left:11px;top:12px;bottom:12px;width:7px;border-radius:5px;background:#a23f22;}
.riskcard.takecard::before{background:#6d4b9c;}
.riskcard.takecard .txt{font-family:var(--serif);font-style:italic;font-weight:400;font-size:clamp(16px,1.3vw,19px);line-height:1.5;}
.riskcard cite{display:inline;margin-left:6px;font-size:11px;color:#8a8d81;font-style:normal;white-space:nowrap;}
.riskcard .txt{font-weight:500;font-size:clamp(13.5px,.9vw,15px);color:#171916;line-height:1.55;}
.gloss{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:6px 30px;}
.gloss div{padding:9px 0;border-bottom:1px solid var(--line);font-size:13.8px;line-height:1.55;}
.gloss b{font-family:var(--serif);color:#171916;}
.empty{color:var(--muted);font-style:italic;font-size:14.5px;}
"""

INDEX_CSS = CSS + """
.idx-stats{display:flex;flex-wrap:wrap;gap:8px 22px;margin-top:6px;}
.idx-stats span{font-family:var(--serif);font-style:italic;color:var(--brand);font-size:clamp(12.5px,.95vw,14.5px);}
.searchwrap{margin:0 0 22px;}
#q{width:100%;box-sizing:border-box;padding:12px 16px;border:1px solid var(--line);border-radius:10px;
  background:#fffefb;font-size:15px;font-family:inherit;color:var(--ink);}
#q:focus{outline:2px solid var(--brand);outline-offset:-1px;}
.tabs{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 22px;}
.tab{font-family:inherit;font-size:13.5px;font-weight:600;padding:9px 16px;border-radius:20px;
  border:1px solid var(--line);background:#fbf7ef;color:var(--muted);cursor:pointer;}
.tab.active{background:var(--brand);border-color:var(--brand);color:#fffdf8;}
.view{display:none;}
.view.active{display:block;}
table.idx{width:100%;border-collapse:collapse;}
table.idx th{text-align:left;font-family:var(--serif);font-style:italic;font-weight:600;
  color:var(--brand);font-size:13px;padding:8px 14px 8px 0;border-bottom:2px solid var(--brand);}
table.idx td{padding:12px 14px 12px 0;border-bottom:1px solid var(--line);vertical-align:top;
  font-size:clamp(13.5px,.95vw,15px);}
table.idx tr:hover td{background:#fbf7ef;}
.idx-date{white-space:nowrap;color:var(--muted);font-variant-numeric:tabular-nums;}
.idx-channel{white-space:nowrap;font-weight:600;}
.idx-title a{color:var(--ink);text-decoration:none;border-bottom:1px solid var(--line);}
.idx-title a:hover{color:var(--brand);border-bottom-color:var(--brand);}
.idx-thread{color:var(--muted);font-size:13px;}
.grp{border:1px solid var(--line);border-radius:12px;background:#fbf7ef;margin:0 0 12px;overflow:hidden;}
.grp[hidden]{display:none;}
.grp summary{list-style:none;cursor:pointer;padding:14px 18px;display:flex;align-items:center;
  gap:12px;font-weight:600;}
.grp summary::-webkit-details-marker{display:none;}
.grp summary::before{content:"\\25B8";color:var(--brand);font-size:12px;transition:transform .15s;}
.grp[open] summary::before{transform:rotate(90deg);}
.grp summary b{font-family:var(--serif);font-size:clamp(15px,1.1vw,18px);font-weight:600;color:#171916;}
.grp summary .cnt{margin-left:auto;font-size:12.5px;color:var(--muted);font-weight:500;white-space:nowrap;}
.tkr{display:inline-block;min-width:44px;text-align:center;padding:3px 8px;border-radius:5px;
  background:#171916;color:#fffdf8;font-size:12px;font-weight:700;letter-spacing:.02em;}
.tkr.none{background:var(--line);color:var(--muted);}
.grp-body{padding:0 18px 14px;}
ul.rows{list-style:none;margin:0;padding:0;}
ul.rows li{padding:9px 0;border-bottom:1px solid var(--line);font-size:13.8px;}
ul.rows li:last-child{border-bottom:none;}
ul.mentions{list-style:none;margin:0;padding:0;}
ul.mentions li{position:relative;padding:10px 0 10px 18px;border-bottom:1px solid var(--line);}
ul.mentions li:last-child{border-bottom:none;}
ul.mentions .dot{position:absolute;left:0;top:16px;width:7px;height:7px;border-radius:50%;}
.m-date{white-space:nowrap;color:var(--muted);font-variant-numeric:tabular-nums;font-size:12.5px;margin-right:8px;}
.m-channel{font-weight:600;font-size:12.5px;margin-right:8px;}
.m-stance{display:block;font-size:12px;color:var(--brand);font-style:italic;margin-top:2px;}
.m-blurb{font-size:13.3px;color:#3a3d35;line-height:1.5;margin-top:4px;}
.noresults{color:var(--muted);font-style:italic;padding:20px 0;display:none;}
"""


def slugify(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode("ascii")
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower()
    return s


def esc(s):
    if s is None:
        return ""
    return (
        str(s)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def render_snapshot(items):
    if not items:
        return '<p class="empty">No clear snapshot could be extracted from this transcript.</p>'
    lis = "".join(f"<li>{esc(b)}</li>" for b in items)
    return f'<ol class="snap">{lis}</ol>'


NAMES_ACCENT = "#65695f"  # fixed neutral slate — distinct from stance colors, reads as "reference"
WATCH_ACCENT = "#93711b"  # fixed amber — reads as "caution", regardless of the theme's own stance color


def render_theme(t):
    color = STANCE_COLORS.get(t.get("color", "gray"), STANCE_COLORS["gray"])
    bullets = "".join(
        f'<li><span class="dot" style="background:{color};"></span>{esc(b)}</li>'
        for b in t.get("bullets", [])
    )
    quote_html = ""
    q = t.get("quote")
    if q:
        quote_html = (
            f'<div class="sidecard quote" style="--sc-accent:{color};">'
            f'<div class="lbl">Pull quote</div>'
            f'&#8220;{esc(q["text"])}&#8221;<cite>{esc(q.get("cite",""))}</cite></div>'
        )
    names_html = ""
    names = t.get("names")
    if names:
        chips = "".join(
            f'<div class="namechip"><b>{esc(n["name"])}</b><span>{esc(n["blurb"])}</span></div>'
            for n in names
        )
        names_html = (
            f'<div class="sidecard" style="--sc-accent:{NAMES_ACCENT};">'
            f'<div class="lbl">Names in play</div>{chips}</div>'
        )
    watch_html = ""
    if t.get("watch"):
        watch_html = (
            f'<div class="sidecard" style="--sc-accent:{WATCH_ACCENT};">'
            f'<div class="lbl">Worth noting</div>'
            f'<div class="txt">{esc(t["watch"])}</div></div>'
        )

    return f"""
<section class="theme" id="{t['id']}">
  <div class="theme-badgerow">
    <span class="badge" style="background:{color};">{esc(t.get('badge',''))}</span>
    <span class="theme-status">{esc(t.get('status',''))}</span>
  </div>
  <h2 style="border-left:4px solid {color};">{esc(t['title'])}</h2>
  <div class="theme-body">
    <div class="theme-main">
      <p class="lead">{esc(t.get('lead',''))}</p>
      <ul class="bullets">{bullets}</ul>
    </div>
    <div class="theme-side">
      {quote_html}
      {names_html}
      {watch_html}
    </div>
  </div>
</section>
"""


def render_icards(items, icon_default="\U0001F4CC", with_tag_detail=False, inline_tag=False):
    if not items:
        return '<p class="empty">Nothing notable found in this category for this video.</p>'
    out = []
    for it in items:
        if inline_tag:
            tag = esc(it.get("tag", ""))
            cat = f'<span class="cat">{tag}:</span> ' if tag else ""
            out.append(
                f'<div class="icard"><div class="ic">{it.get("icon", icon_default)}</div>'
                f'<div class="tline">{cat}<span class="txt">{esc(it["title"])}</span></div></div>'
            )
        elif with_tag_detail:
            out.append(
                f'<div class="icard"><div class="ic">{it.get("icon", icon_default)}</div>'
                f'<div><div class="title">{esc(it["title"])}</div>'
                f'<div class="tag">{esc(it.get("tag",""))}</div>'
                f'<div class="detail">{esc(it.get("detail",""))}</div></div></div>'
            )
        else:
            out.append(
                f'<div class="icard"><div class="ic">{it.get("icon", icon_default)}</div>'
                f'<div><div class="title">{esc(it["title"])}</div>'
                f'<div class="tag">{esc(it.get("tag",""))}</div></div></div>'
            )
    return "".join(out)


def render_risks(items):
    if not items:
        return '<p class="empty">No specific caveats flagged for this source.</p>'
    return "".join(f'<div class="riskcard"><div class="txt">{esc(r)}</div></div>' for r in items)


def render_hot_takes(items):
    if not items:
        return '<p class="empty">No standout hot takes or personal convictions in this video.</p>'
    out = []
    for t in items:
        cite = t.get("cite", "")
        out.append(
            '<div class="riskcard takecard"><div class="txt">&#8220;' + esc(t["take"]) + '&#8221;'
            + (f' <cite>{esc(cite)}</cite>' if cite else "")
            + '</div></div>'
        )
    return "".join(out)


def render_glossary(items):
    if not items:
        return '<p class="empty">No glossary terms extracted for this video.</p>'
    return '<div class="gloss">' + "".join(
        f'<div><b>{esc(g["term"])}</b> &mdash; {esc(g["def"])}</div>' for g in items
    ) + "</div>"


def build_html(data):
    META = data.META
    thread_count = len(data.THEMES)
    thread_line = META.get("thread_line") or f"{thread_count} threads"
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Research: {esc(META['title'])}</title>
<style>{CSS}</style>
</head>
<body>
<div class="page">
  <header class="hero">
    <div class="backlink"><a href="index.html">&#8592; All Research Briefs</a></div>
    <div class="kicker">A YouTube Research Brief</div>
    <h1>{esc(META['title'])}</h1>
    <div class="byline">
      Channel: <b>{esc(META['channel'])}</b> &middot; Speaker: <b>{esc(META['speakers'])}</b> &middot; <b>{esc(META['date'])}</b>
      <div class="stats-line">{esc(thread_line)} &middot; <a href="{esc(META['video_url'])}" target="_blank" rel="noopener">Watch on YouTube &#8599;</a></div>
    </div>
  </header>
  <div class="inner">
    <section class="sec">
      <div class="sec-eye">The one-paragraph takeaway</div>
      <h2>Video Snapshot</h2>
      <div class="card" style="margin-top:16px;">{render_snapshot(data.SNAPSHOT)}</div>
    </section>

    {''.join(render_theme(t) for t in data.THEMES)}

    <section class="sec">
      <div class="sec-eye">What to do with this</div>
      <h2>Best Actionable Takeaways</h2>
      <div style="margin-top:16px;">{render_icards(data.TAKEAWAYS, inline_tag=True)}</div>
    </section>

    <section class="sec">
      <div class="sec-eye">Where this could be wrong</div>
      <h2>Risks &amp; Caveats on This Source</h2>
      <div style="margin-top:16px;">{render_risks(data.RISKS)}</div>
    </section>

    <section class="sec">
      <div class="sec-eye">Where they stuck their neck out</div>
      <h2>Hot Takes &amp; Personal Convictions</h2>
      <div style="margin-top:16px;">{render_hot_takes(data.HOT_TAKES)}</div>
    </section>

    <section class="sec">
      <div class="sec-eye">Beyond the main threads</div>
      <h2>Other Notable News</h2>
      <div style="margin-top:16px;">{render_icards(data.OTHER_NEWS, with_tag_detail=True)}</div>
    </section>

    <section class="sec" style="border-bottom:none;">
      <div class="sec-eye">Names and terms at a glance</div>
      <h2>Glossary &amp; Entities</h2>
      <div style="margin-top:16px;">{render_glossary(data.GLOSSARY)}</div>
    </section>
  </div>
</div>
</body>
</html>"""
    return html


def build_json(data):
    return {
        "meta": data.META,
        "snapshot": data.SNAPSHOT,
        "themes": data.THEMES,
        "takeaways": data.TAKEAWAYS,
        "risks": data.RISKS,
        "hot_takes": data.HOT_TAKES,
        "other_news": data.OTHER_NEWS,
        "glossary": data.GLOSSARY,
    }


# ---------------------------------------------------------------------------
# CROSS-VIDEO INDEX — scans research-data/*/*.json, rebuilt on every run.
# Builds three facets over the same underlying data: chronological, by-channel,
# and by-company/ticker (the entity cross-reference used to build an investing
# thesis across many videos). See _entities_from_theme / _entities_from_conviction
# for how each JSON schema (current 'meta' vs legacy 'metadata') is parsed.
# ---------------------------------------------------------------------------

TICKER_RE = re.compile(r"\(([A-Z]{1,5})\)\s*$")
BARE_TICKER_RE = re.compile(r"^[A-Z]{1,5}$")
TICKER_BLACKLIST = {
    "ADR", "IPO", "CEO", "CFO", "CTO", "ETF", "AI", "GPU", "SEC", "IRA", "WACC",
    "SOFR", "CPI", "PPI", "FOMC", "OER", "US", "UK", "EU", "GDP", "FED", "Q1",
    "Q2", "Q3", "Q4", "YOY", "MOM", "ATH", "IRL", "CEO", "COO", "R&D",
}
STANCE_KEYWORDS_RED = ("NEGATIVE", "BEARISH", "SELL", "AVOID", "SHORT")
STANCE_KEYWORDS_GREEN = ("OWN", "BUY", "ADD", "POSITIVE", "LONG")
STANCE_KEYWORDS_AMBER = ("WATCH", "UNCERTAIN", "CASUAL", "MIXED", "CONTESTED")
INVESTABLE_CATEGORY_HINTS = (
    "stock", "crypto", "equity", "etf", "sector", "compan", "hardware", "semic",
    "commodity", "big tech", "financ", "infrastructure", "market",
)


def _split_entity_list(raw):
    """Split on top-level commas only — commas inside parens (e.g. an aside like
    "Memory semis (Samsung, SK Hynix implied)") don't count as separate entities."""
    parts, depth, buf = [], 0, []
    for ch in raw:
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth = max(0, depth - 1)
        if ch == "," and depth == 0:
            parts.append("".join(buf))
            buf = []
        else:
            buf.append(ch)
    parts.append("".join(buf))
    return [p.strip() for p in parts if p.strip()]


def _parse_ticker(piece):
    m = TICKER_RE.search(piece)
    if m and m.group(1) not in TICKER_BLACKLIST:
        return m.group(1), piece[: m.start()].strip()
    if BARE_TICKER_RE.match(piece) and piece not in TICKER_BLACKLIST:
        return piece, piece
    return None, piece


def _stance_color(stance_text):
    s = (stance_text or "").upper()
    if any(k in s for k in STANCE_KEYWORDS_RED):
        return "red"
    if any(k in s for k in STANCE_KEYWORDS_GREEN):
        return "green"
    if any(k in s for k in STANCE_KEYWORDS_AMBER):
        return "amber"
    return "gray"


def _entities_from_theme(theme):
    out = []
    for n in theme.get("names") or []:
        raw = n.get("name", "")
        blurb = n.get("blurb", "")
        for piece in _split_entity_list(raw):
            ticker, display = _parse_ticker(piece)
            out.append({
                "ticker": ticker, "display": display or piece,
                "stance_label": theme.get("badge", ""), "conviction": None,
                "color": theme.get("color", "gray"), "blurb": blurb,
            })
    return out


def _entities_from_conviction(conviction_map):
    out = []
    for c in conviction_map or []:
        raw = c.get("topic", "")
        category = c.get("category", "") or ""
        investable = any(k in category.lower() for k in INVESTABLE_CATEGORY_HINTS)
        for piece in _split_entity_list(raw):
            ticker, display = _parse_ticker(piece)
            if not ticker and not investable:
                continue
            stance = c.get("stance", "")
            out.append({
                "ticker": ticker, "display": display or piece,
                "stance_label": stance, "conviction": c.get("conviction"),
                "color": _stance_color(stance), "blurb": c.get("core_thesis", ""),
            })
    return out


def _legacy_thread_line(d):
    """Legacy schema has no thread_line field — derive a short one so the chronological
    view isn't blank: first sentence of the executive takeaway, or a company/ticker count."""
    exec_take = (d.get("executive_takeaway") or "").strip()
    if exec_take:
        first = re.split(r"(?<=[.!?])\s+", exec_take)[0]
        return first if len(first) <= 160 else first[:157].rstrip() + "..."
    n = len(d.get("conviction_map") or [])
    if n:
        return f"{n} companies/tickers covered"
    return ""


def _load_brief(json_path):
    try:
        d = json.load(open(json_path, encoding="utf-8"))
    except Exception:
        return None
    base = os.path.splitext(os.path.basename(json_path))[0]
    html_name = f"{base}.html"
    if not os.path.exists(html_name):
        return None
    if "meta" in d:  # current schema
        m = d["meta"]
        date = m.get("date", "")
        speakers = m.get("speakers", "")
        thread_line = m.get("thread_line", "")
        category = m.get("category") or "market"
        entities = [e for t in d.get("themes", []) for e in _entities_from_theme(t)]
    elif "metadata" in d:  # legacy fixed-table schema
        m = d["metadata"]
        date = m.get("publication_date") or m.get("analysis_date", "")
        speakers = m.get("speaker", "")
        thread_line = _legacy_thread_line(d)
        category = "market"
        entities = _entities_from_conviction(d.get("conviction_map"))
    else:
        return None
    return {
        "html": html_name,
        "title": m.get("title", base),
        "channel": m.get("channel", ""),
        "date": date,
        "speakers": speakers,
        "thread_line": thread_line,
        "category": category,
        "entities": entities,
    }


def _date_sort_key(date_str):
    try:
        return -int(date_str.replace("-", ""))
    except (ValueError, AttributeError):
        return 0


def _search_blob(*parts):
    return esc(" ".join(p for p in parts if p).lower())


def _render_chrono_view(briefs):
    rows = "".join(
        f'<tr class="row" data-search="{_search_blob(b["title"], b["channel"], b["thread_line"])}">'
        f'<td class="idx-date">{esc(b["date"])}</td>'
        f'<td class="idx-channel">{esc(b["channel"])}</td>'
        f'<td class="idx-title"><a href="{esc(b["html"])}">{esc(b["title"])}</a></td>'
        f'<td class="idx-thread">{esc(b["thread_line"])}</td></tr>'
        for b in briefs
    ) or '<tr><td colspan="4" class="empty">No briefs found yet.</td></tr>'
    return f"""<table class="idx">
      <thead><tr><th>Date</th><th>Channel</th><th>Title</th><th>Threads</th></tr></thead>
      <tbody>{rows}</tbody>
    </table>"""


def _render_channel_view(briefs):
    by_channel = {}
    for b in briefs:
        by_channel.setdefault(b["channel"], []).append(b)
    groups = sorted(
        by_channel.items(),
        key=lambda kv: min(_date_sort_key(b["date"]) for b in kv[1]),
    )
    out = []
    for channel, items in groups:
        items = sorted(items, key=lambda b: _date_sort_key(b["date"]))
        search = _search_blob(channel, " ".join(b["title"] for b in items))
        rows = "".join(
            f'<li><span class="idx-date">{esc(b["date"])}</span> '
            f'<a href="{esc(b["html"])}">{esc(b["title"])}</a> '
            f'<span class="idx-thread">{esc(b["thread_line"])}</span></li>'
            for b in items
        )
        out.append(
            f'<details class="grp" data-search="{search}">'
            f'<summary><b>{esc(channel)}</b><span class="cnt">{len(items)} brief{"s" if len(items) != 1 else ""}</span></summary>'
            f'<div class="grp-body"><ul class="rows">{rows}</ul></div></details>'
        )
    return "".join(out) or '<p class="empty">No briefs found yet.</p>'


def _render_entity_view(briefs):
    all_mentions = [(e, b) for b in briefs for e in b["entities"]]

    # A mention like "Nvidia" (no parsed ticker) must merge with "Nvidia (NVDA)" elsewhere —
    # build display-name -> ticker aliases from every mention that DID carry a ticker first.
    alias = {}
    for e, _ in all_mentions:
        if e["ticker"]:
            alias.setdefault(e["display"].lower(), e["ticker"])

    entities = {}  # key -> {ticker, display, mentions: []}
    for e, b in all_mentions:
        key = e["ticker"] or alias.get(e["display"].lower()) or e["display"].lower()
        slot = entities.setdefault(key, {"ticker": e["ticker"], "display": e["display"], "mentions": []})
        if not slot["ticker"] and (e["ticker"] or alias.get(e["display"].lower())):
            slot["ticker"] = e["ticker"] or alias.get(e["display"].lower())
        if e["ticker"] and len(e["display"]) > len(slot["display"]):
            slot["display"] = e["display"]  # prefer the fuller name variant
        slot["mentions"].append({**e, "brief": b})

    ordered = sorted(
        entities.values(),
        key=lambda s: (-len(s["mentions"]), 0 if s["ticker"] else 1, s["display"].lower()),
    )
    out = []
    for s in ordered:
        mentions = sorted(s["mentions"], key=lambda m: _date_sort_key(m["brief"]["date"]))
        search = _search_blob(
            s["ticker"] or "", s["display"],
            " ".join(m["brief"]["title"] for m in mentions),
            " ".join(m["brief"]["channel"] for m in mentions),
        )
        tkr_badge = f'<span class="tkr">{esc(s["ticker"])}</span>' if s["ticker"] else '<span class="tkr none">—</span>'
        items = []
        for m in mentions:
            color = STANCE_COLORS.get(m["color"], STANCE_COLORS["gray"])
            b = m["brief"]
            stance_bits = " · ".join(x for x in [m["stance_label"], m["conviction"]] if x)
            items.append(
                f'<li><span class="dot" style="background:{color};"></span>'
                f'<span class="m-date">{esc(b["date"])}</span>'
                f'<span class="m-channel">{esc(b["channel"])}</span>'
                f'<a href="{esc(b["html"])}">{esc(b["title"])}</a>'
                + (f'<span class="m-stance">{esc(stance_bits)}</span>' if stance_bits else "")
                + (f'<div class="m-blurb">{esc(m["blurb"])}</div>' if m["blurb"] else "")
                + "</li>"
            )
        out.append(
            f'<details class="grp" data-search="{search}">'
            f'<summary>{tkr_badge}<b>{esc(s["display"])}</b>'
            f'<span class="cnt">{len(mentions)} mention{"s" if len(mentions) != 1 else ""}</span></summary>'
            f'<div class="grp-body"><ul class="mentions">{"".join(items)}</ul></div></details>'
        )
    return "".join(out) or '<p class="empty">No companies or tickers extracted yet.</p>'


INDEX_JS = """
(function(){
  var tabs = document.querySelectorAll('.tab');
  var views = document.querySelectorAll('.view');
  tabs.forEach(function(tab){
    tab.addEventListener('click', function(){
      tabs.forEach(function(t){ t.classList.remove('active'); });
      views.forEach(function(v){ v.classList.remove('active'); });
      tab.classList.add('active');
      document.getElementById('view-' + tab.dataset.view).classList.add('active');
      applyFilter();
    });
  });
  var q = document.getElementById('q');
  function applyFilter(){
    var term = q.value.trim().toLowerCase();
    document.querySelectorAll('.view.active [data-search]').forEach(function(el){
      var hit = !term || el.dataset.search.indexOf(term) !== -1;
      el.hidden = !hit;
      if (hit && term && el.tagName === 'DETAILS') el.open = true;
    });
  }
  q.addEventListener('input', applyFilter);
})();
"""


def build_index():
    briefs = [b for b in (_load_brief(p) for p in sorted(glob.glob(os.path.join("research-data", "*", "*.json")))) if b]
    briefs.sort(key=lambda b: _date_sort_key(b["date"]))

    channels = sorted(set(b["channel"] for b in briefs))
    tickers = sorted(set(e["ticker"] for b in briefs for e in b["entities"] if e["ticker"]))
    dev_briefs = [b for b in briefs if b["category"] == "dev"]

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>YouTube Research Briefs — Index</title>
<style>{INDEX_CSS}</style>
</head>
<body>
<div class="page">
  <header class="hero">
    <div class="kicker">All Research Briefs</div>
    <h1>YouTube Research Brief Index</h1>
    <div class="byline">{len(briefs)} brief{'s' if len(briefs) != 1 else ''} &middot; {len(channels)} channel{'s' if len(channels) != 1 else ''} &middot; {len(tickers)} ticker{'s' if len(tickers) != 1 else ''} tracked
      <div class="idx-stats"><span>Browse chronologically, by channel, or by company/ticker — search filters whichever view is active.</span></div>
    </div>
  </header>
  <div class="inner">
    <div class="searchwrap"><input id="q" type="search" placeholder="Search briefs, channels, companies, tickers..." autocomplete="off"></div>
    <div class="tabs">
      <button class="tab active" data-view="chrono">All Briefs</button>
      <button class="tab" data-view="channel">By Channel</button>
      <button class="tab" data-view="entity">By Company / Ticker</button>
      <button class="tab" data-view="dev">Dev &amp; Workflows</button>
    </div>
    <div id="view-chrono" class="view active">{_render_chrono_view(briefs)}</div>
    <div id="view-channel" class="view">{_render_channel_view(briefs)}</div>
    <div id="view-entity" class="view">{_render_entity_view(briefs)}</div>
    <div id="view-dev" class="view">{_render_chrono_view(dev_briefs)}</div>
  </div>
</div>
<script>{INDEX_JS}</script>
</body>
</html>"""
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)

    manifest = {
        "generated_from": "youtube-research-brief generate.py --reindex",
        "briefs": [{k: v for k, v in b.items() if k != "entities"} | {
            "entities": [{"ticker": e["ticker"], "display": e["display"], "stance": e["stance_label"],
                          "conviction": e["conviction"], "color": e["color"]} for e in b["entities"]]
        } for b in briefs],
    }
    with open("library.json", "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=1, ensure_ascii=False)

    return "index.html"


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)

    if sys.argv[1] in ("--reindex", "--index"):
        print(f"Wrote {build_index()}")
        return

    data_path = sys.argv[1]
    data = load_data(data_path)

    channel_slug = slugify(data.META["channel"])
    date_slug = slugify(data.META["date"])
    title_slug = slugify(data.META["title"])
    base = f"{channel_slug}_{date_slug}_{title_slug}"

    html_path = f"{base}.html"
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(build_html(data))

    data_dir = os.path.join("research-data", base)
    os.makedirs(data_dir, exist_ok=True)
    json_path = os.path.join(data_dir, f"{base}.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(build_json(data), f, indent=1, ensure_ascii=False)

    data_copy_path = os.path.join(data_dir, f"{base}_data.py")
    if os.path.abspath(data_path) != os.path.abspath(data_copy_path):
        shutil.copyfile(data_path, data_copy_path)

    print(f"Wrote {html_path}")
    print(f"Wrote {json_path}")
    print(f"Archived data file to {data_copy_path}")
    print(f"Wrote {build_index()}")


if __name__ == "__main__":
    main()
