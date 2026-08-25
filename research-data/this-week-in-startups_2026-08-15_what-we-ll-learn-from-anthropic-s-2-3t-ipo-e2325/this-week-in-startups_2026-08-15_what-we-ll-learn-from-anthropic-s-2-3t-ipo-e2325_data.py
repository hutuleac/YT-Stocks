"""Data file for This Week in Startups E2325 — What we'll learn from Anthropic's $2-3T IPO."""

META = {
    "title": "What we'll learn from Anthropic's $2-3T IPO | E2325",
    "channel": "This Week in Startups",
    "speakers": "Jason Calacanis (host), Lon Harris (co-host), Sammy Herabi (Wisewell, guest), Punit Puri (Grit Robotics, guest)",
    "date": "2026-08-15",
    "video_url": "https://www.youtube.com/watch?v=-4NTVlaeveo",
    "thread_line": "5 threads · what Anthropic's S-1 will actually reveal, the Decart deal as a sign M&A is back, a countertop water-purification pitch (and the microplastics case for it), AI-trained robot arms racing to install solar 4x faster, and a Friday off-duty round of dictation gear and media picks",
    "category": "market",
}

SNAPSHOT = [
    "Financial Times reports Anthropic is targeting a $2-3 trillion valuation for an October IPO — topping SpaceX's $1.7T record from a few months earlier and putting Anthropic among only five companies ever to touch $3T; investors expect ARR to hit $100-120B by year-end.",
    "New Ramp data on enterprise AI spend: 43.5% of US businesses paid Anthropic for subscriptions/tokens last month vs. 39.7% for OpenAI and just 6.2% for Google's AI tools — a reversal from 18 months ago when, as Jason puts it, 'people were like, what's Claude?'",
    "Jason's IPO-investing advice is consistent and blunt: don't buy at the open — IPOs get priced to perfection and pop, then fall back once institutions start buying (cites SpaceX, Figma, Instacart, Reddit) — better to slowly build a position over a 10-year window.",
    "Anthropic is also reportedly in talks to acquire Israeli chip-efficiency startup Decart AI for ~$6B, its largest deal to date; Jason reads it as a sign the M&A market has reopened after years in the wilderness, aided by a friendlier regulatory environment.",
    "Two founder interviews: Sammy Herabi of Wisewell pitches a subscription countertop water-purification device (with a microplastics/fertility health case behind it) that Jason is personally negotiating to invest in; Punit Puri of Grit Robotics explains how AI-trained, off-the-shelf robot arms are already installing solar panels 4-8x faster than human crews in Nevada.",
    "Friday's off-duty segment: a NYT/Google dataset on 2025 emoji trends, a DJI wireless mic recommendation for better LLM dictation, and picks for Ted Lasso season 4, HBO's Lanterns, Hulu's Furious, and AMC's The Shards.",
]

THEMES = [
    {
        "id": "anthropic-ipo",
        "color": "amber",
        "badge": "Confirmed event",
        "status": "IPO EXPECTED OCTOBER 2026 — reported valuation $2-3T",
        "title": "Anthropic's $2-3T IPO: What the S-1 Will Finally Reveal",
        "lead": "**The IPO filing is less about the headline valuation and more about the numbers nobody outside Anthropic has seen yet** — revenue composition, compute costs, and how a token-rental business actually depreciates its infrastructure.",
        "bullets": [
            "FT reports Anthropic is targeting $2-3 trillion for an October IPO — topping SpaceX's $1.7T record set months earlier; only five companies in history have ever touched a $3T valuation, and investors expect Anthropic's ARR to hit $100-120B by year-end.",
            "New Ramp card-spend data: 43.5% of US businesses paid Anthropic for subscriptions/tokens last month vs. 39.7% for OpenAI and 6.2% for Google's AI tools — a swing from 18 months ago when, per Jason, people didn't know what Claude was.",
            "Jason expects the deal to price around 30x topline revenue, and is most interested in what the filing reveals about customer concentration, salary/stock-comp as a share of revenue, compute spend, and how they depreciate data centers and chips depending on whether they're owned, rented, or leased.",
            "He contrasts Anthropic's model (token-rental, enterprise-heavy) with OpenAI's (building its own data centers, consumer-heavy): ChatGPT has roughly a billion users, but Jason estimates maybe 10-20M paying $20/month — around $5B/year, which he pegs at only ~5% the size of Anthropic's enterprise business.",
            "His IPO-investing rule: don't buy at the open. Bankers and CEOs price IPOs to perfection in a hot market, the pop happens, then price falls back once institutions start buying — he cites SpaceX, Figma, Instacart, and Reddit as recent examples of that pattern.",
        ],
        "quote": {"text": "It's going to go out at 3 trillion. They're sandbagging with the two trillion.", "cite": "— Jason Calacanis"},
        "watch": "Jason's own caveat on the theme: IPO pops are typically followed by a pullback once institutional buying starts — his advice is to wait rather than chase the open.",
        "names": [
            {"name": "Anthropic", "blurb": "Reported $2-3T October IPO target; ARR expected to hit $100-120B by year-end; leads US enterprise AI spend per Ramp data at 43.5%."},
            {"name": "OpenAI", "blurb": "39.7% of US enterprise AI spend per Ramp; contrasted with Anthropic as more consumer-driven and more capex-heavy (building its own data centers)."},
        ],
    },
    {
        "id": "decart-ma-wave",
        "color": "green",
        "badge": "In talks — unannounced",
        "status": "REPORTED ~$6B, largest Anthropic acquisition to date",
        "title": "The Decart Deal and the Reopening of the M&A Market",
        "lead": "**Anthropic's talks to buy an Israeli chip-efficiency startup are, in Jason's read, less about the target itself and more a sign that the whole M&A market has thawed** for the first time in years.",
        "bullets": [
            "Anthropic is reportedly in talks to acquire Israeli startup Decart AI for ~$6B — its largest acquisition to date, a 50% premium over Decart's prior valuation.",
            "Decart's software makes chips run more efficiently (claims up to 8x throughput gains) across Nvidia, Amazon Trainium, and Google TPUs; it also makes Lucy (a real-time video generation/transformation model) and Oasis (a physics-accurate world model for simulation).",
            "Jason frames the price as only ~25 basis points of a $3T Anthropic — 'ticky tacky' at this scale — and notes that going public specifically hands a company a public-stock 'currency' to keep acquiring.",
            "He credits the current administration with reopening the M&A market after a multi-year VC 'winter,' citing other recent deals in the same spirit: OpenAI reportedly in talks to buy Jony Ive's design studio for $5-10B, and a roughly $200M acquisition of a podcast with about 20,000 listeners.",
            "His venture framework for judging any of these: only 1 in 10 acquisitions needs to work to be worth it — cites Instagram, YouTube, WhatsApp, Android, PowerPoint, and Excel as purchased companies that became massively accretive to their acquirers.",
        ],
        "quote": {"text": "Let the good times roll. Let the acquisitions happen. Only one in 10 has to work.", "cite": "— Jason Calacanis"},
        "watch": None,
        "names": [
            {"name": "Decart AI", "blurb": "Israeli chip-efficiency startup reportedly being acquired by Anthropic for ~$6B, a 50% premium over its prior valuation."},
        ],
    },
    {
        "id": "wisewell",
        "color": "green",
        "badge": "Recommendation",
        "status": "OWNS — Jason disclosed he is personally negotiating a stake",
        "title": "Wisewell: Betting on Distributed Water Infrastructure — and the Microplastics Case Behind It",
        "lead": "**Wisewell's pitch is a Dyson/Tesla-style redesign of tap-water purification**, backed by a subscription model with utility-level retention and a health argument about what's actually in tap and bottled water.",
        "bullets": [
            "Product takes tap water through a carbon filter and reverse osmosis, then remineralizes it (sodium, calcium, potassium) through a natural stone filter to restore taste and pH — explicitly designed, per founder Sammy Herabi, in the spirit of Dyson (vacuum, fan) and Tesla (making a 'boring sustainability thing' desirable, with over-the-air updates).",
            "Product line: Nano at $29/month for unlimited water; Model One (floor-standing); Sparkle, the flagship at $89/month, with hot/cold/room-temperature dispensing plus Apple Health, Google Health, and NFC integration.",
            "Business model stats: ~2% attrition across tens of thousands of subscribers on a standard 2-year commitment, and the average unit is used about 15 times a day — Sammy calls it 'the second most used device to the iPhone in the household.'",
            "Health case: the average US water pipe is about 78 years old; a cited nanoplastics study found levels far higher than assumed (roughly 10,000 units/liter assumed vs. ~240,000 microplastics/nanoplastics per liter measured), first raised publicly, per Sammy, on the All-In Podcast's science-corner segment; bottled-water drinkers reportedly ingest about a teaspoon (7g) of plastic, with dementia-afflicted cadavers showing roughly 10x that.",
            "Further claims: male fertility down roughly 30% tracked against a similar rise in plastic consumption, the first class-action suits against bottled water brands (Fiji named) already filed, and trace pharmaceuticals (SSRIs/antidepressants) detected in wastewater — quantified as about 1% of one normal daily prescribed dose accumulated over 70 years of drinking 2 liters of tap water a day.",
            "Jason discloses he is personally negotiating an investment in the company — a direct conflict of interest with his enthusiasm on air — and used harmonic.ai to pull the home water-filter market ahead of the interview, surfacing that the Asia-Pacific region holds about 60% of the global point-of-use filtration market and that Brita leads the pitcher-filter category.",
        ],
        "quote": {"text": "If I'm drinking out of a Wisewell, then you know I'm on the cap table.", "cite": "— Jason Calacanis"},
        "watch": "The microplastics/fertility/dementia figures are Sammy's own summary of existing research stated in conversation, without citations shown on screen — treat them as his framing of the literature, not an independently audited review.",
        "names": [
            {"name": "Wisewell", "blurb": "Countertop water-purification subscription startup; Jason is personally negotiating an equity stake, disclosed on air as a conflict of interest."},
        ],
    },
    {
        "id": "grit-robotics",
        "color": "green",
        "badge": "High conviction",
        "status": "POSITIVE VIEW — Series A/B, $32M raised, 18 months old",
        "title": "Grit Robotics: Teaching Off-the-Shelf Arms to Install Solar 4-8x Faster",
        "lead": "**Grit doesn't build robots — it teaches existing robotic arms to install solar panels**, aiming at a labor-shortage problem that's about to collide head-on with data-center-driven demand for new power.",
        "bullets": [
            "The company writes AI software that trains off-the-shelf robotic arms for solar installation; robots are currently deployed in Nevada, with 7 sites completed so far (~35,000 panels) and contracts for roughly 6 million panels (~2.8 GW) over the next 18-24 months.",
            "The labor problem it's solving: solar crews see ~70% attrition and about 30% of applicants can't pass a drug test; overall US construction productivity is down 30-46% since 1965 even as agriculture, retail, and manufacturing gained roughly 1000% over the same period, with 41% of the skilled US construction workforce projected to retire by 2031.",
            "Productivity gain: a strong 8-person human crew installs ~800 panels/day; with Grit's AI-guided robots the same crew hits 3,000-4,000 panels/day at an ~18-19 second cycle time per panel — targeting the ~8% of total install cost that is 'mechanical labor' first, before expanding into electrical work.",
            "Panel economics follow a steep learning curve — price drops about 48% every time cumulative production doubles, roughly every 18 months, which Punit likens to a 'Moore's law' for solar; panels have gone from $128/watt in 1975 to roughly $0.25-0.26/watt in the US today (and as low as ~$0.14/watt for the newest Chinese panels).",
            "Illustrative demand story: an unnamed bank customer asked a major solar contractor for a 900MW plant to power a data center; standard timeline is ~1.5 years for 300MW (so ~4 years for 900MW), but the customer demanded 18 months — then raised the ask to 1.8GW in half that time.",
            "Team and funding: $32M raised total (recent round $26M), 18 months old, based in South San Francisco; hardware team from MIT, robotics team from Carnegie Mellon's PhD program, and a field team of ex-Marines who previously deployed robots in Afghanistan and Iraq.",
        ],
        "quote": {"text": "We can print solar panels like a newspaper... it's an obvious energy source we need to be tapping into.", "cite": "— Punit Puri"},
        "watch": "Punit frames the coming shift to cheap fixed-tilt panel structures (replacing costlier sun-tracking mounts) as 'our thesis, and we might be wrong' — an explicit hedge on where panel/storage economics head next, not a settled claim.",
        "names": [
            {"name": "Grit Robotics", "blurb": "AI software company (not a robot-hardware maker) training off-the-shelf arms to install solar panels; $32M raised, contracted for ~6M panels over 18-24 months."},
        ],
    },
    {
        "id": "off-duty",
        "color": "gray",
        "badge": "Recommendation",
        "title": "Off Duty: Dictation Gear, Emoji Trends, and What's Worth Watching",
        "lead": "**The Friday wrap-up mixes a genuinely useful workflow tip with the week's culture-and-media picks.**",
        "bullets": [
            "New Google/Android data (via a NYT report) on 2025 emoji trends: the plain crying-face emoji has overtaken laugh-crying as the most used, since Gen Z now considers laugh-crying 'boomer'; the skull emoji ('I'm dead') is also fading, replaced by the same crying emoji; teens prefer fire over the 100 emoji, and prayer hands over thumbs-up.",
            "Workflow recommendation: a DJI Mic 3 wireless lav mic (~$84 for the transmitter, ~$80 for a standalone clip-on unit) for better dictation fidelity into LLMs like Claude and Hermes/Perplexity Computer when whispering or recording in a car.",
            "Dictation tip worth repeating: skip short 1-2 sentence prompts and instead dictate 2-3 minutes of stream-of-consciousness instruction into an LLM — Jason argues this consistently produces better agent output than typed, terse prompts.",
            "Media picks: Ted Lasso season 4 (Apple TV+, new premise coaching a women's team in England); Lanterns (HBO Max, DC's Green Lantern series from showrunner Damon Lindelof with writers from Ozark and True Detective, plus comic writer Tom King); Furious (Hulu/Disney+, a Black-Widow-inspired revenge thriller with Emmy Rossum, Lola Tung, and Scoot McNairy); The Shards (AMC, Bret Easton Ellis's serialized novel produced by Ryan Murphy, an 80s-set project that sat stalled at HBO for years before AMC picked it up).",
        ],
        "quote": None,
        "watch": None,
        "names": None,
    },
]

TAKEAWAYS = [
    {"icon": "\U0001F4C9", "tag": "IPO timing", "title": "Don't buy Anthropic (or any hyped) IPO at the open — wait for the post-pop pullback before building a position."},
    {"icon": "\U0001F4C4", "tag": "Read the filing", "title": "When the S-1 lands, focus on compute cost, chip depreciation method, and customer concentration — that's the real story behind the headline valuation."},
    {"icon": "\U0001F91D", "tag": "M&A as a signal", "title": "Track small-scale acquisitions (like Decart) at trillion-dollar companies as a liquidity/M&A-thaw signal, not just deal-specific news."},
    {"icon": "\U0001F6E0️", "tag": "Weight the backlog", "title": "For automation/robotics startups, weight contracted pipeline (Grit's ~6M-panel backlog) and team pedigree over how viral the demo video looks."},
    {"icon": "\U0001F3A4", "tag": "Dictate, don't type", "title": "Use a wireless lav mic and 2-3 minutes of stream-of-consciousness dictation into your LLM instead of short typed prompts."},
]

RISKS = [
    "Jason discloses he is personally negotiating an equity stake in Wisewell — his on-air enthusiasm for the product carries a direct financial conflict of interest.",
    "Ramp's enterprise-AI-spend percentages are drawn from card/subscription transaction data, not an independent, audited market census.",
    "Anthropic's IPO valuation, ARR figure, and the Decart deal terms are all pre-announcement reporting (Financial Times sourcing, described as insider conversations), not confirmed regulatory filings.",
    "Wisewell's microplastics, fertility, and dementia-cadaver figures are the founder's own conversational summary of existing research, not citations shown or verified on screen.",
    "One M&A example Jason cites in passing — 'Cursor bought... for $60 billion' — is an offhand aside during the show that doesn't clearly match public reporting; treat it as his conversational claim rather than a confirmed deal.",
    "Sponsor segments (Ro, PayPal/Launch, CLA, Odoo) are excluded from this brief entirely, per standing policy on paid ad reads.",
]

HOT_TAKES = [
    {"take": "I don't think in today's day and age you need to race into IPOs — the bankers and the CEOs price IPOs to perfection.",
     "cite": '— Jason Calacanis', "why": 'Told directly to an audience being sold the Anthropic listing as an event they must be early to.'},
    {"take": 'Let the good times roll. Let the acquisitions happen. Only one in 10 has to work.',
     "cite": '— Jason Calacanis', "why": 'His defense of the M&A thaw, built on the list of purchased companies that became Instagram, YouTube, WhatsApp and Android.'},
    {"take": "Every time we double the production of solar panels, the price comes down by 48% — and it's happening every 18 months.",
     "cite": '— Punit Puri, Grit Robotics', "why": "A Moore's-law framing for solar, from a founder whose business depends on it being true."},
    {"take": '41% of the US skilled workforce in construction will retire by 2031.',
     "cite": '— Punit Puri, Grit Robotics', "why": 'The labor-shortage number underneath his robotics pitch — a dated, checkable claim rather than a vibe.'},
    {"take": "I don't think you should try to follow what everyone else is doing.",
     "cite": '— Jason Calacanis', "why": 'From the off-duty segment on emoji use — offered as general advice, with the caveat that a few will still tag you as a boomer.'},
]

OTHER_NEWS = []

GLOSSARY = [
    {"term": "ARR", "def": "Annual recurring revenue — the run-rate of subscription/recurring revenue a company is generating, used here to size Anthropic ahead of its IPO."},
    {"term": "Basis point", "def": "One-hundredth of a percentage point; Jason uses it to show the Decart deal (~$6B) is a tiny fraction (~25 bps) of Anthropic's reported $3T valuation."},
    {"term": "TAM (total addressable market)", "def": "The total revenue opportunity available for a product or service if it captured 100% of its target market — pulled here for the home water-filter industry via harmonic.ai."},
    {"term": "PFAS", "def": "Per- and polyfluoroalkyl substances, so-called 'forever chemicals' found in many tap water supplies that require reverse osmosis (rather than basic carbon filtering) to remove."},
    {"term": "TDS (total dissolved solids)", "def": "A measure of the mineral content dissolved in water; high-TDS water (like Evian) tastes more mineral-heavy, while low-TDS water (like Aquapanna) tastes cleaner."},
    {"term": "Price-learning curve", "def": "The pattern where a technology's unit price drops by a consistent percentage every time cumulative production doubles — cited here as solar panels dropping ~48% per doubling, roughly every 18 months."},
]
