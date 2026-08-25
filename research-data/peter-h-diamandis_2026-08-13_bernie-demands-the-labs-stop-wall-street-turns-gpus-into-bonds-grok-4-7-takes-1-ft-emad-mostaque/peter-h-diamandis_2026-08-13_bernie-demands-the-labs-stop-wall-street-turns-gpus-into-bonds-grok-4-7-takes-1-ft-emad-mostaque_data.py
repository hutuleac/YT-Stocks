META = {
    "title": "Bernie Demands the Labs Stop, Wall Street Turns GPUs Into Bonds, Grok 4.7 Takes #1 ft. Emad Mostaque",
    "channel": "Peter H. Diamandis",
    "speakers": "Peter Diamandis (host), Alex Wissner-Gross, Dave Blondin, Salim Ismail, Emad Mostaque",
    "date": "2026-08-13",
    "video_url": "https://www.youtube.com/watch?v=uoGnH0REG7A",
    "thread_line": "6 threads · Longevity XPRIZE awards, Hollywood's AI-driven cost collapse, Grok's sprint to the frontier, Nvidia's $500B compute financialization, Bernie Sanders' pause letter colliding with a Stanford bioweapon-design breakthrough, and Zuckerberg's personal-AI manifesto",
}

SNAPSHOT = [
    "Panel of five (Diamandis, Alex Wissner-Gross, Dave Blondin, Salim Ismail, Emad Mostaque) covers 9+ stories spanning longevity, AI infrastructure, Hollywood, model races, and AI safety.",
    "Diamandis's $101M Healthspan XPRIZE awarded its first $1M-per-team prizes at last night's Utah finals; 800 teams entered (a record), aiming to reverse 20 years of functional aging by 2030.",
    "AI filmmaking crossed a real cost threshold: a full-length movie with licensed celebrity likenesses cost $2M and 4 weeks versus Hollywood's typical $20-100M and 12-18 months, while 9 of the top 10 text-to-video models are now Chinese.",
    "Grok 4.6 shipped this morning matching frontier benchmarks; the panel credits Elon's Cursor acquisition (for reasoning-trace data) plus raw Nvidia compute scale, with Grok 4.7 rumored in two weeks.",
    "Nvidia structured $500B+ in third-party financing with five Wall Street giants (Apollo, BlackRock, Blackstone, Brookfield, KKR) to let institutional capital invest directly in AI compute — explicitly compared, and defended, against mortgage-backed securities.",
    "Bernie Sanders demanded Anthropic, Meta, and OpenAI pause AI development after a Stanford team used an open-source model to design viable novel bacteriophages; the panel largely rejects a pause as unenforceable, pushing instead for defensive co-scaling (biosurveillance, prompt-level monitoring).",
    "Zuckerberg published a 'personal intelligence' manifesto and open-sourced two new on-device Meta models, drawing praise for openness but real skepticism about Meta's underlying motives.",
    "Side stories: Archer Aviation consolidated three Boeing eVTOL units in one deal; a claimed post-transformer AI architecture ('Dragon Hatchling') got a skeptical 'hot mess' review; Claude's new text watermark was reportedly stripped by a public tool within 24 hours of release.",
]

THEMES = [
    {
        "id": "healthspan-xprize",
        "color": "green",
        "badge": "Confirmed milestone",
        "status": "FIRST PRIZES AWARDED LAST NIGHT — UNIVERSITY OF UTAH",
        "title": "The $101M Healthspan XPRIZE hands out its first checks — 800 teams, one goal: reverse 20 years of aging",
        "lead": "Diamandis's Healthspan XPRIZE awarded $1M each to 10 teams at its Utah finals, with the field racing toward a 2030 deadline to reverse 20 years of functional aging, validated by real human trials rather than mice studies.",
        "bullets": [
            "$101M total prize purse ($80M grand prize plus milestone awards); $20M given away so far; $1M awarded to each of 10 teams at last night's finals, with 10 more finalists recognized.",
            "800 teams entered — a record for XPRIZE competitions (for comparison, Musk's $100M carbon-removal XPRIZE drew ~1,500 teams, and reversing aging is considered a harder problem).",
            "Goal: reverse 20 years of functional aging — cognition, muscle-building capacity, immune system — validated via human trials (~150 participants) with control groups; winner decided by 2030.",
            "Context stat: US life expectancy rose from 47 (1900) to 79 today, but the average American is only healthy until ~63, spending their final years in declining health; the global cost of age-related disease is roughly $20T/year against a ~$120-130T global economy.",
            "GLP-1 drugs flagged as an early, unplanned 'spike' in longevity escape velocity — Diamandis cites (explicitly caveated as not medical advice, back-of-envelope) recent studies suggesting some GLP-1 subpopulations may hit roughly 70% LEV from the drug alone.",
            "Historical parallel: the 1996 Ansari X Prize for private spaceflight had no commercial-space industry behind it at launch and catalyzed a trillion-dollar industry (SpaceX, Blue Origin) once it was won — the panel expects the same capital flywheel for longevity now that this prize has run.",
        ],
        "quote": {
            "text": "How much of your wealth would you spend for an extra 30 years of life? The honest answer is nearly all of it.",
            "cite": "— Peter Diamandis",
        },
        "watch": "GLP-1 longevity-escape-velocity figures are explicitly framed by Diamandis as unverified back-of-envelope estimates, not medical advice.",
        "names": [
            {"name": "XPRIZE Healthspan", "blurb": "$101M longevity XPRIZE ($80M grand prize); 10 winning teams awarded $1M each at the Aug 13, 2026 finals, working toward reversing 20 years of functional aging by 2030."},
        ],
    },
    {
        "id": "hollywood-ai-collapse",
        "color": "amber",
        "badge": "Confirmed trend, contested implications",
        "status": "ACCELERATING NOW — MULTIPLE RELEASES THIS WEEK",
        "title": "A $2M, 4-week AI movie just undercut Hollywood's cost structure by 98%",
        "lead": "Hicksfield's fully AI-generated feature film, Chinese dominance of text-to-video leaderboards, and a MacBook-capable open-source video model together signal Hollywood's economics are being rewritten in real time.",
        "bullets": [
            "Hicksfield's 'Cully Hill Boys,' the first full-length AI-generated movie with licensed celebrity likenesses, ran 110 minutes for a $2M total budget (including $1M compute), a 28-person team, and 4 weeks of production — versus a traditional $20-100M/12-18-month film — using Seedance 2.5 and an openly published 10-step, 80-page workflow guide.",
            "Hicksfield (founded by an ex-Snap executive) is already at a $700M revenue run rate roughly 18 months after founding.",
            "Bloomberg: 9 of the top 10 text-to-video models on the Artificial Analysis leaderboard are now Chinese — raising both a 'who exports culture' question and a robotics angle, since the physics/motion/causality modeling needed for video generation transfers directly to robotics and autonomous driving.",
            "LTX 2.5, the most-downloaded open-source video model, now runs locally on a MacBook Pro and generates a 10-second clip in 7 seconds at near-indistinguishable quality via new 'Fusion Fidelity Rendering' (compute allocated by scene complexity, not a flat rate).",
            "Cost trajectory: Seedance 2.5 costs roughly $3 per 30 seconds of footage (cheaper models run 10-20x less at ~90% the quality); since the average Hollywood shot is only ~3 seconds, the panel estimates a feature-length film could be produced for roughly $100K of compute by year-end.",
            "Diamandis's Future Vision XPRIZE has 5,000 entries (3-minute trailer plus film treatment) being cut to a top 100, then 50, 25, 10, 5, with finalists revealed live at Moonshots Live in LA on September 25; the winner gets a $10M budget (prize money plus foreign film rights) to make the full movie.",
            "Panel debate on actor economics: Diamandis predicts studios will license uncredited lookalikes under different names rather than pay A-listers for likeness rights; Alex Wissner-Gross predicts dead actors' estates become highly lucrative licensors since they can't object or compete for new work.",
        ],
        "quote": {
            "text": "You never need to reshoot a scene now.",
            "cite": "— Emad Mostaque",
        },
        "watch": "Cost/quality tradeoffs and actor-likeness/union rights questions remain legally unresolved even as the underlying economics shift week to week.",
        "names": [
            {"name": "Hicksfield", "blurb": "AI film studio; made the first full-length AI-generated movie with licensed celebrity likenesses for ~$2M in 4 weeks; now at a $700M revenue run rate."},
            {"name": "LTX 2.5", "blurb": "Most-downloaded open-source video generation model; runs locally on a MacBook Pro, generates near-real-time HD video."},
        ],
    },
    {
        "id": "grok-frontier-sprint",
        "color": "amber",
        "badge": "High conviction on catch-up, contested on leapfrog",
        "status": "GROK 4.6 RELEASED THIS MORNING; 4.7 RUMORED IN 2 WEEKS",
        "title": "Grok's monthly release cadence is closing the gap on the frontier — the open question is whether it can pass it",
        "lead": "Grok 4.6 already matches frontier benchmarks at a fraction of the price, and the panel traces the leap to Elon's Cursor acquisition for reasoning-trace data plus raw Nvidia compute scale — with 4.7's SpaceX-engineering training data seen as the real test of whether xAI can leapfrog, not just catch, the frontier.",
        "bullets": [
            "Grok 4.6 matches frontier performance on the Artificial Analysis Intelligence Index (score 61), priced at $2/$6 per million input/output tokens, optimized for long-running multi-step agentic tasks (research, coding, self-testing its own work), available today in Cursor and Grok Build.",
            "Release cadence: Grok 4.5 shipped two weeks ago, 4.6 this morning, 4.7 rumored in roughly two weeks — Elon has floated an unprecedented goal of a new pretraining run roughly every month, versus the industry-standard quarterly or annual cadence.",
            "xAI's strategy, per Alex Wissner-Gross: license/acquire Cursor's reasoning-trace data (reportedly paid $10B) to post-train Grok toward the frontier, the same way Chinese labs allegedly distill reasoning traces from Claude and other Western models — plus xAI has the Nvidia GPU compute scale Chinese labs lack.",
            "Parameter scaling: Grok 4.5 was 1.5T parameters; 4.7 moves to roughly 2T; Grok 5 (originally expected in May, still not shipped) targets 6-10T parameters — the delay attributed partly to Elon replacing the original xAI team with the acquired Cursor team, plus time needed to 'bed in' new B300 chips.",
            "Grok 4.7 will reportedly be trained on SpaceX's proprietary physics and engineering knowledge — the panel calls this the real test of whether xAI can leapfrog the frontier, since reasoning-trace distillation alone can only close the gap, not exceed it.",
            "New 'bots' feature from the Cursor integration: screen-record a workflow and Grok auto-converts it into a reusable skill — pitched internally as a path to digitizing an entire company's workflows.",
        ],
        "quote": {
            "text": "He's the best engineering leader in the world and he's turned it into an engineering masterpiece.",
            "cite": "— Peter Diamandis, on Elon Musk",
        },
        "watch": "The panel agrees xAI can likely catch the frontier via reasoning-trace distillation and compute scale, but is split on whether that path can ever exceed (leapfrog) it.",
        "names": [
            {"name": "xAI (Grok)", "blurb": "Released Grok 4.6 this morning matching frontier benchmarks at $2-6/M tokens; 4.7 rumored in two weeks, trained partly on SpaceX engineering data."},
        ],
    },
    {
        "id": "nvidia-compute-financialization",
        "color": "amber",
        "badge": "Contested — bull case vs. MBS-style risk",
        "status": "PARTNERSHIP ANNOUNCED THIS WEEK",
        "title": "Nvidia turns GPU compute into a $500B+ tradeable financial asset — and draws its own mortgage-crisis comparison",
        "lead": "Nvidia is structuring over half a trillion dollars of third-party institutional capital directly into AI compute alongside Apollo, BlackRock, Blackstone, Brookfield, and KKR, while Larry Fink's own mortgage-backed-securities comparison exposes the real risk: a physics or architecture breakthrough could strand years of financed GPU cash flows overnight.",
        "bullets": [
            "Nvidia (NVDA) partnered with Apollo, BlackRock, Blackstone, Brookfield, and KKR to mobilize over $500B in third-party capital for AI infrastructure — Nvidia isn't borrowing the money; it's building the financing structure so pension funds, sovereign funds, and private equity can invest directly in AI compute clusters.",
            "Jensen Huang's framing: 'We began by building chips. Today, we're helping to create a new class of productive, investable infrastructure, AI factories.'",
            "Bull case (Dave Blondin): GPUs depreciate over 3-5 year cycles but keep earning throughout — H100s are reportedly more valuable today than when first purchased; this is 'the first pitch of the first inning' of a multi-trillion-dollar compute buildout.",
            "Bear case (Larry Fink, cited): an explicit comparison to mortgage-backed securities — securitizing roughly 10 years of GPU cash flows risks stranding assets if a cheaper architecture or physics breakthrough (new chip, post-transformer model, lighter-mass space-based compute) makes today's GPUs obsolete.",
            "Alex Wissner-Gross's counter: he's been popularizing 'compute-backed securities' (CBS) — arguing compute is fundamentally more productive than a house (the MBS analogy's core asset), and that a mature market needs options/futures to hedge both an algorithmic-breakthrough downside and a geopolitical upside (e.g., a Taiwan conflict spiking compute prices).",
            "Real-world validation cited: CoreWeave clients are signing contracts for A100 chips (6-year-old hardware, introduced 2020) through 2029, because once hardware is paid off the only ongoing cost is electricity, and the electricity-to-intelligence conversion ratio keeps improving (a task needing ~16 A100s in 2022 now fits on a fraction of one chip).",
        ],
        "quote": {
            "text": "Financial assets want predictable depreciation and exponential technologies don't give you predictable depreciation.",
            "cite": "— Salim Ismail",
        },
        "watch": "Whether ratings agencies price these compute-backed securities honestly — not the financial instrument itself — is what the panel says determines if this becomes 2008 all over again.",
        "names": [
            {"name": "Nvidia (NVDA)", "blurb": "Structuring $500B+ in third-party financing (with Apollo, BlackRock, Blackstone, Brookfield, KKR) so institutional investors can invest directly in AI compute."},
            {"name": "Apollo, BlackRock, Blackstone, Brookfield, KKR", "blurb": "Six Wall Street partners (memos of understanding) pledging capital toward Nvidia's AI infrastructure financing structure."},
        ],
    },
    {
        "id": "sanders-pause-vs-evo2",
        "color": "amber",
        "badge": "Contested — alarm vs. dismissal",
        "status": "LETTER SENT AND EVO2 RESULTS PUBLISHED THIS WEEK",
        "title": "Bernie Sanders demands a pause the same week Stanford proves AI can already design viable new viruses",
        "lead": "Sanders' pause letter to Anthropic, Meta, and OpenAI landed the same week Stanford researchers used an open-source model to design 16 viable novel bacteriophages — and the panel's near-unanimous verdict is that a pause is unenforceable, with the real chokepoint being physical DNA-synthesis equipment, not model capability.",
        "bullets": [
            "Sen. Bernie Sanders sent a formal letter to the CEOs of Anthropic, Meta, and OpenAI demanding an immediate pause on AI development, citing AI's first-ever use to help design a new virus, quoting Yoshua Bengio ('this should serve as a wake-up call') and the CIA director calling AI models 'akin to digital nuclear weapons... almost like a doomsday device.'",
            "The letter is largely symbolic per Dave Blondin's read — its only concrete ask is vague ('if you do not take appropriate action now, my colleagues and I... will'), functioning more as public position-taking ('I told you so' insurance) than an actionable demand.",
            "Stanford researchers used the open-source EVO2 model (40B parameters, trained on ~1M genome strains) to design roughly 300 novel bacteriophage DNA sequences, producing 16 viable phages effective against E. coli strains with no natural resistance — a biosecurity researcher called it 'biology's Wright Brothers moment'; Emad Mostaque says he has personally run EVO2 on his own MacBook.",
            "Panel's near-unanimous counter-argument: pausing frontier labs doesn't stop open-source or non-compliant actors (DeepSeek V4 Pro just scored 83.3 on CyberGym, edging a Western frontier model's 83.2), and Alex argues the 2023 FLI six-month pause letter actually accelerated the race by letting less-compliant labs catch up during the pause.",
            "Alex's structural counter: the real choke point should be the physical DNA/RNA synthesis equipment (currently unregulated), not the AI models — paralleling how nuclear non-proliferation controls uranium, plutonium, and centrifuges rather than trying to un-invent bomb physics.",
            "Proposed defense-in-depth stack discussed: cheap, ubiquitous DNA/RNA sequencers (e.g., MinION-style USB devices) for real-time biosurveillance at airports and transit hubs; prompt-and-token-level monitoring (Dave's suggestion) since output-level bans can't realistically be enforced; and 'premeditation-level' intelligence interdiction, paralleling intelligence-community sting operations on uranium buyers.",
            "Alex's dissent from the alarm framing: the Wuhan lab-leak hypothesis (the US intelligence community's stated consensus theory) shows pandemics don't require superintelligence at all, so capping AI capability doesn't address the actual root risk.",
        ],
        "quote": {
            "text": "The moment is here. AI capabilities have reached a critical threshold.",
            "cite": "— Sen. Bernie Sanders",
        },
        "watch": "Panel is split on tone but converges on substance: both Emad and Alex call a blanket pause unworkable, while agreeing the underlying capability genuinely exists now and needs a defensive answer, not just a rhetorical one.",
        "names": [
            {"name": "Anthropic, Meta, OpenAI", "blurb": "Recipients of Sen. Sanders' letter demanding an immediate AI development pause, citing bioweapon risk."},
        ],
    },
    {
        "id": "zuck-personal-ai",
        "color": "amber",
        "badge": "Praised for openness, doubted on motive",
        "status": "PUBLISHED THIS WEEK — 6,500 WORDS PLUS VIDEO",
        "title": "Zuckerberg's 'personal intelligence' manifesto pairs open-source models with a community-benefits pitch — and the panel doesn't fully buy the framing",
        "lead": "Zuckerberg's essay proposes a superintelligence that runs on your phone and works only for you, backed by two newly open-sourced Meta models and a local-benefits fund — but the panel questions whether Meta genuinely wants to stay in the consumer-app business long-term, and flags why every rival lab retreated from consumer AI companionship in the first place.",
        "bullets": [
            "Zuckerberg's 6,500-word essay 'The Future is for Everyone' pitches 'personal intelligence' — a superintelligence running on your phone, in your ear, or on your glasses, working only for you — leveraging Meta's 3B+ users across WhatsApp, Instagram, and Facebook.",
            "Meta Superintelligence Labs is open-sourcing 'Muse Glimmer,' a 30B-parameter dense on-device model billed as the highest-performing model of its size, and will open the weights for 'Muse 1.2,' a leading foundation model, in the coming weeks.",
            "Community-benefit pitch: teachers in Richland Parish got $50,000 bonuses funded by data-center tax revenue; Meta launched 'America's Workforce Academy' (free training plus guaranteed jobs at infra sites) and a new 'Future Is For Everyone Fund' for teachers, first responders, and energy/water infrastructure near its data centers.",
            "Skepticism from the panel: Jason-style critique from Diamandis calls the announcement video 'motherhood and apple pie' shot on Zuckerberg's iPhone with no formal press rollout; Alex argues Meta doesn't actually want to be a consumer-app company long-term and would pivot to a cloud/compute business (like OpenAI) if it could — Diamandis disagrees, arguing distribution via the existing apps is Meta's real advantage.",
            "Dave Blondin's read on why every other major lab retreated from consumer AI companionship: server logs reportedly show the first thing many users do with an open-ended personal AI is sexualize it (cites Grok's 'Bad Rudy' avatar controversy as a parallel) — which is why OpenAI and Anthropic pivoted to enterprise-only use cases, leaving Meta as the only major US lab still targeting consumer reasoning-token volume.",
            "Context stat: 71% of Americans say they don't want a data center in their backyard — more opposition than to a nuclear plant — which the panel reads as the real driver behind Zuckerberg's local-benefits pitch; Meta is building its 'Hyperion' supercluster largely in lower-income US Southeast states.",
        ],
        "quote": {
            "text": "I don't think Meta/Zuck, if they had a choice, would rather have their personal super intelligence be diverted to their family of apps.",
            "cite": "— Alex Wissner-Gross",
        },
        "watch": "The panel disagrees among itself on Meta's true long-term intent (cloud/compute pivot vs. doubling down on app distribution) — an open question, not a resolved read.",
        "names": [
            {"name": "Meta (META)", "blurb": "Published Zuckerberg's 'personal intelligence' manifesto; open-sourcing Muse Glimmer (30B on-device model) and Muse 1.2 foundation model weights."},
        ],
    },
]

TAKEAWAYS = [
    {"icon": "\U0001F9EC", "tag": "Longevity", "title": "Watch the XPRIZE Healthspan finalists' human-trial data over the next 1-2 years — it's the closest thing to a validated, real-world leaderboard for which longevity approaches actually work."},
    {"icon": "\U0001F3AC", "tag": "Filmmaking", "title": "If building in AI video/film, study Hicksfield's openly published 10-step production workflow — the cost/speed gap versus traditional production is now public and replicable."},
    {"icon": "\U0001F4B5", "tag": "Compute investing", "title": "Before treating AI compute deals as bond-like fixed income, price in architecture-obsolescence risk explicitly via hedging rather than assuming GPU cash flows are as predictable as they're being marketed."},
    {"icon": "\U0001F9EA", "tag": "AI safety", "title": "Track physical chokepoints (DNA/RNA synthesizers, GPU export controls) rather than model-capability caps as the more enforceable lever in AI biosecurity debates."},
    {"icon": "\U0001F916", "tag": "Model selection", "title": "If evaluating xAI's Grok for coding/agent work, weigh its price advantage ($2-6/M tokens) against reasoning-trace catch-up limits — it may match but not yet exceed frontier reasoning models."},
]

RISKS = [
    "Multiple panelists (especially Alex Wissner-Gross, who discloses financial interest in compute-securitization and post-transformer-architecture ventures) are discussing markets and companies they are personally invested in.",
    "Several figures (GLP-1 LEV percentages, Grok's exact cost figures, the '$10B for Cursor data' number, CyberGym scores) are relayed verbally from memory during a live discussion and are explicitly caveated by the speakers themselves as rough or unverified in places.",
    "A recurring product name transcribed as 'Fable' appears throughout the video (used interchangeably with 'its competitors,' priced around $50-60 vs. Grok's $6-8) that could not be confidently identified from context — likely an auto-caption artifact for another frontier AI product name; treat these specific mentions with caution.",
    "Auto-generated captions on a 3-hour, 6-person crosstalk-heavy panel are prone to misattributed speakers and mistranscribed names or figures.",
]

HOT_TAKES = [
    {"take": 'How much of your wealth would you spend for an extra 30 years of life? The honest answer is nearly all of it.',
     "cite": '— Peter Diamandis', "why": 'His argument that longevity is the largest market in the world, and now tractable for the first time.'},
    {"take": "Financial assets want predictable depreciation, and exponential technologies don't give you predictable depreciation.",
     "cite": '— Salim Ismail', "why": "The objection to Nvidia turning GPU compute into a bond-like instrument with Wall Street's biggest names attached."},
    {"take": "Privacy is dead — and there's a benefit to that, which is that malevolent actors are going to get heard, seen, and caught.",
     "cite": '— Peter Diamandis', "why": 'A position he says he has stated many times, argued here as a feature rather than a loss.'},
    {"take": 'You never need to reshoot a scene now.',
     "cite": '— Emad Mostaque', "why": "On a $2M AI feature film made in four weeks — he treats Hollywood's cost structure as already undercut by 98%."},
    {"take": "Facebook saying 'we're going to be your best friend AI' is like McDonald's saying they came out with the biggest health food you've ever heard of.",
     "cite": '— Moonshot Mates panel', "why": "The panel's read on Zuckerberg's personal-intelligence manifesto: the framing doesn't survive the incentives."},
    {"take": 'This competition will be won by 2030.',
     "cite": '— Peter Diamandis, on the Healthspan XPRIZE', "why": 'A hard date on reversing 20 years of functional aging, with the field already handing out checks.'},
]

OTHER_NEWS = [
    {"icon": "\U0001F4A7", "title": "Anthropic's new Claude text watermark and the EU's separate AI-content icon system were both live within a day of a public tool emerging to strip Claude/Gemini/OpenAI watermarks; arXiv now bans authors for a year over AI-flagged submissions and Spotify is AI-labeling music — panel calls both moves as short-lived as cookie banners", "tag": "AI content labeling"},
    {"icon": "\U0001F681", "title": "Archer Aviation acquired three Boeing units (Whisk Aero, Insitu, SkyGrid AI) in one deal with Boeing taking an equity stake; top 5 eVTOL players (Joby, Archer, EHang, Beta, Eve) are racing toward $3/seat-mile pricing today with a long-term target of $15-25/trip, and the panel frames newly flight-accessible hillsides and islands as a coming source of real-estate 'abundance'", "tag": "Urban air mobility"},
    {"icon": "\U0001F9EA", "title": "\"Dragon Hatchling,\" a claimed non-transformer architecture beating ARC-AGI benchmarks at a fraction of compute cost, drew a skeptical \"hot mess\" verdict from Alex Wissner-Gross, who argues real post-transformer progress will come gradually (linearized attention, diffusion transformers, recurrence) rather than from one clean new architecture", "tag": "AI architecture"},
    {"icon": "\U0001F4AC", "title": "AMA hot takes: Salim expects foundation models to commoditize like databases, with real advantage shifting to proprietary data and iteration speed (the \"inner loop\"); Dave flagged Elon's parallel bet on a giant HBM-memory fab (\"Terafab\") as a hedge against GPU obsolescence; Emad said he's worried Opus 5 shows early \"lying\" behavior and compares current model alignment to \"bacteria-level\" ethics", "tag": "AMA quick hits"},
]

GLOSSARY = [
    {"term": "ARC-AGI", "def": "Benchmark testing genuine novel reasoning (not pattern matching) that has historically resisted brute-force transformer scaling."},
    {"term": "C2PA", "def": "Open provenance standard Anthropic is using to embed Claude's text watermark."},
    {"term": "LEV (Longevity Escape Velocity)", "def": "The point at which medical progress adds healthy years of life faster than time passes."},
    {"term": "Compute-backed securities (CBS)", "def": "Alex Wissner-Gross's proposed financial instrument securitizing GPU compute cash flows, akin to mortgage-backed securities but for AI infrastructure."},
    {"term": "HBM (High Bandwidth Memory)", "def": "The memory type increasingly bottlenecking AI training, which Elon's rumored 'Terafab' aims to manufacture at scale."},
    {"term": "eVTOL", "def": "Electric vertical takeoff and landing aircraft — the 'flying car' category led by Joby, Archer, EHang, Beta, and Eve."},
    {"term": "Distillation", "def": "Training a new model by learning from an existing model's outputs or reasoning traces — used here by both xAI/Cursor and Meta/Scale to catch up to frontier labs."},
]
