META = {
    "title": "xAI Just Built What Jensen Didn't Think Was Possible",
    "channel": "FutureAzA",
    "speakers": "Brian (FutureAzA) with Jordan Giesige (The Limiting Factor)",
    "date": "2026-08-23",
    "video_url": "https://www.youtube.com/watch?v=lrFdZuv6Nco",
    "thread_line": "6 threads · Colossus 2 buildout · compute payback math · Memphis power · demand durability · space-based compute · AI UX and robots",
    "category": "market",
}

SNAPSHOT = [
    "Colossus 2 is landing as three buildings in a different layout than Giesige predicted a year ago — the plot he expected to hold a building is filling with cooling, energy and battery gear instead.",
    "SpaceX/xAI has spent $329 million on Tesla Megapacks this year alone for the site.",
    "The headline economics: whatever compute you build pays itself off in roughly a year — Giesige calls the number 'shocking' and says even six months ago he'd have doubted a two-year payback.",
    "Working model: ~$50B capex per gigawatt (aggressive, assuming Elon gets mate's rates) against ~$50B revenue per gigawatt per year; ~440,000 GPUs implies ~$72B/year.",
    "Memphis today holds ~1.5–2 GW of compute; the earnings call pointed at 5–10 GW total — more than the city's own 3.5 GW record peak demand, and 6–10 nuclear reactors' worth of power, to be met with gas generation.",
    "Self-funding is only partial: a 3–6 month lag between spend and revenue on an 8 GW/year pace is a $100–200B hole, and SpaceX itself expects to be cash-flow negative until 2030–2035.",
    "Both are demand bulls — 90–95% of businesses haven't figured out how to use what already exists, and real-world (visual/audio) intelligence needs orders of magnitude more compute.",
    "Side threads: a sun-synchronous orbit satellite barely needs batteries; today's AI is 'really stupid' because it won't ask probing questions; a genuinely useful consumer humanoid is 3–4 years out.",
]

THEMES = [
    {
        "id": "colossus-2",
        "color": "green",
        "badge": "Confirmed build, revised layout",
        "status": "COLOSSUS 2 — TWO BUILDINGS UP, THIRD COMING",
        "title": "The Colossus 2 site didn't grow the way anyone drew it — it grew sideways, then upward",
        "lead": "Giesige's year-old site prediction was directionally right on three buildings and wrong on where they'd go, because xAI kept buying land after he drew the map.",
        "bullets": [
            "Land acquired across the street changed the layout; the plot he'd penciled in for a building is now cooling, energy and battery equipment plus heat exchangers.",
            "A third building is going in further left — he's unsure it gets to the full million GPUs Elon originally quoted for Colossus 2.",
            "$329 million spent on Megapacks this year alone at the SpaceX/xAI site.",
            "The third building may simply be taller: Elon's companies use vertical space when land runs out, and he 'always seems to be running out of land.'",
            "Only two locations exist — Colossus 1 (one building) and Colossus 2 (two, soon three). No third site is known.",
            "Analysis Giesige read the morning of taping: to add next year's planned compute, xAI has to announce at least one more major site, because Colossus 2 is getting tight.",
        ],
        "quote": {
            "text": "No matter how much of it his companies acquire, he seems to always be running out of land.",
            "cite": "— Jordan Giesige",
        },
        "watch": "Giesige's own video on this is three weeks old and he says it has already significantly changed — the site is moving faster than the analysis of it.",
        "names": [
            {"name": "xAI", "blurb": "POSITIVE VIEW / High — Colossus 1 + 2 deploying faster than any competitor, three buildings and counting."},
            {"name": "SpaceX", "blurb": "POSITIVE VIEW / High — merged entity funding and building the compute; strong cash reserve to draw down during the ramp."},
            {"name": "Tesla", "blurb": "CASUAL MENTION / Medium — $329M of Megapacks bought this year for the Colossus site."},
        ],
    },
    {
        "id": "payback-math",
        "color": "amber",
        "badge": "Working model, aggressive assumptions",
        "status": "~1-YEAR PAYBACK ON BUILT COMPUTE",
        "title": "Build a gigawatt for $50B, rent it out for $50B a year",
        "lead": "The whole thesis rests on one number Giesige calls shocking: whatever compute you build, you can pay it off in about a year.",
        "bullets": [
            "Gavin Baker's estimate is ~$120B for 2 GW ($60B/GW); Giesige deliberately models $50B/GW to match the bulls and assume Elon deploys more efficiently than anyone.",
            "Revenue side: ~$50B per GW per year. Separately, ~440,000 GPUs implies ~$72B/year potentially.",
            "xAI overbuilt on purpose — it runs its own needs off the cluster and leases the surplus, which nobody else has the spare capacity to do.",
            "Even Google rents from them. Giesige's framing: fierce competition on products, cooperation on capacity, because nobody is getting enough.",
            "Brian's buyer logic: if it costs $1 and earns you $2, you'll pay $1.50 — falling behind can be fatal, so overpaying today beats building cheaper next year.",
            "He frames renting as drop-shipping: at $1.50 with none of the work, you still clear 50 cents — and you might not exist by the time your own build comes online.",
            "Not self-funding: a 3–6 month lag between spend and booked revenue at 2 GW/quarter (8 GW/year) is a $100–200B financing gap, likely filled by Nvidia or similar.",
            "SpaceX and analysts close to it expect cash-flow negative through 2030–2035; Giesige had only assumed a year or two.",
            "Mitigation if capital tightens: slow the pace — which Giesige expects only if customers aren't lined up. Brian's analogy: he can't fund 2 million cars up front either, but Q1 sales fund Q2.",
            "Revenue upside isn't only rented compute — Starlink and other SpaceX products are scaling alongside it.",
        ],
        "quote": {
            "text": "If something costs a dollar and you make $2 off of it, are you still going to pay a $1.50 for it? Probably.",
            "cite": "— Jordan Giesige",
        },
        "watch": "Upside case is Vera Rubin GPUs renting for materially more; downside is unexpected deployment costs. Giesige says he tried to sit mid-range rather than go double like some do.",
        "names": [
            {"name": "Nvidia", "blurb": "POSITIVE VIEW / Medium — didn't believe a coherent 100,000+ GPU cluster was possible; now the likely capital source above self-funding, and wants chips deployed and used."},
            {"name": "Google", "blurb": "CASUAL MENTION / Medium — named as one of the large companies renting Colossus compute rather than building it themselves."},
        ],
    },
    {
        "id": "memphis-power",
        "color": "amber",
        "badge": "Guided range, contested scale",
        "status": "MEMPHIS — 1.5–2 GW TODAY, 5–10 GW GUIDED",
        "title": "A data center that draws more power than the city it sits next to",
        "lead": "Memphis is being scaled past the point where municipal comparisons help — the top of the guided range is New York City territory, met with gas.",
        "bullets": [
            "~1.5–2 GW of compute exists in Memphis today; SemiAnalysis had another ~2 GW of generation lined up beyond that when Giesige published three weeks ago.",
            "The earnings call moved the target to 5–10 GW total — far more ambitious than the ~4 GW his video assumed.",
            "Scale check: a medium city of half a million people peaks at 500 MW–1.5 GW. Memphis's record maximum hourly demand is 3.5 GW.",
            "6–10 GW is 6–10 full-size nuclear reactors' worth of power — delivered instead by dozens to hundreds of gas generators.",
            "Heat, emissions and noise are real: Giesige frames it as 'relationship management,' while noting natural gas beats the coal generation of 20–30 years ago.",
        ],
        "quote": {
            "text": "This data center will pull more power than the city it is next to.",
            "cite": "— Brian, FutureAzA",
        },
        "watch": "The 5–10 GW figure is guidance from an earnings call, not built capacity; Giesige's own baseline was overtaken within three weeks of publishing.",
        "names": None,
    },
    {
        "id": "demand-durability",
        "color": "green",
        "badge": "High conviction",
        "status": "BOTH SPEAKERS BULLISH ON DEMAND",
        "title": "Infinite demand, uncertain price — and a bear case about consolidation",
        "lead": "Giesige sees effectively infinite compute demand; Brian raises two separate doubts — that the field of players contracts, and that today's token prices aren't what the compute actually costs.",
        "bullets": [
            "Demand argument: the more AI you use, the more AI you use — agents now have their own agents, and only a small share of the population touches this compute at all.",
            "90–95% of businesses still haven't worked out how to get the juice out of the lemon; TAM expansion, not model improvement, is where the growth is.",
            "Giesige sees decreasing return on investment from frontier model gains — they're already very good at coding, and he doesn't know how much better they get.",
            "Real-world intelligence (visual + audio, not just text) needs orders of magnitude more compute than text models; each new model generation also expands memory requirements as parameter counts grow.",
            "Brian's bear case isn't people abandoning AI — it's the number of players contracting, faster processors reducing the need to expand at insane paces, and rents or power costs falling until leasing stops making sense.",
            "Brian's counter: many companies sell tokens below cost or give them away; ChatGPT's user count is inflated by people opening second accounts when they run out.",
            "Cost shock is real — companies have accidentally burned hundreds of thousands to millions on tokens; one user spent ~$300 on a single PDF summary on max settings.",
            "Surplus-compute risk is softened by physics: chips degrade by cycle, not by age, like solar panels or wind turbines idled for a day.",
        ],
        "quote": {
            "text": "There's leading edge companies right now that they're getting the most benefit… 90 to 95% of the businesses out there still haven't worked out how to get that juice out of the lemon.",
            "cite": "— Jordan Giesige",
        },
        "watch": "Giesige concedes surplus compute is always a risk and unavoidable, even though he doesn't expect it. Brian can't size how fast price-per-output has to fall for broad business adoption.",
        "names": None,
    },
    {
        "id": "space-compute",
        "color": "gray",
        "badge": "Speculative",
        "status": "ORBITAL COMPUTE — DESIGN LOGIC ONLY",
        "title": "A compute satellite barely needs batteries, for a reason most people get backwards",
        "lead": "Brian's burning question: does a big orbital compute platform need a big battery? Giesige's answer is no — and the reason inverts the terrestrial logic.",
        "bullets": [
            "In sun-synchronous orbit you face constant sun, so there is no night-time gap to cover.",
            "Terrestrial data centers need batteries for two jobs: covering night-time generation and covering peak power draw.",
            "In orbit only the second job remains — short bursts when the compute needs extra juice.",
            "That flips the usual assumption that orbital compute would be battery-heavy.",
        ],
        "quote": None,
        "watch": "Purely a design argument — no orbital compute program, cost, or timeline was discussed.",
        "names": None,
    },
    {
        "id": "ai-ux-robots",
        "color": "amber",
        "badge": "Structural critique",
        "status": "USER-SIDE VIEW FROM BOTH SPEAKERS",
        "title": "Today's AI is 'really stupid' because it won't ask you a question",
        "lead": "Both speakers use AI daily and land on the same gap: models answer instead of interrogating, and that same gap is what blocks useful humanoids.",
        "bullets": [
            "Giesige's complaint: it jumps to wrong conclusions, never asks probing questions, and burns a million tokens answering something you didn't ask.",
            "Human conversations work by feeling out the context of each other's minds; AI skips that mind-meld and just emits.",
            "Brian uses Grok instead of Google search for research — asking for citations he can go read himself — and says Google's products get worse as the goal shifted from best product to most profitable.",
            "He ran Grok as a live tour guide with FSD driving around his own town: not 100% accurate, but more accurate than any human tour guide he's had.",
            "Being interruptible matters — Brian corrects Grok mid-answer; Giesige repeatedly tells it to 'shut up' after the correct first sentence.",
            "Robot timeline: genuinely useful for the average person is 3–4 years away; factories and operators who know how to talk to the machine get value in 1–3 years, mirroring how programming went conversational.",
        ],
        "quote": {
            "text": "It's so good already, but compared to what it's going to be, I still see it as really stupid.",
            "cite": "— Jordan Giesige",
        },
        "watch": "Brian pushes back on the 3–4 year humanoid timeline given Unitree is about to go public; Giesige narrows his claim to usefulness for an average consumer, not industry.",
        "names": [
            {"name": "Unitree", "blurb": "CASUAL MENTION / Low — cited by Brian as a counterexample to the 3–4 year useful-humanoid timeline because it's about to go public."},
        ],
    },
]

TAKEAWAYS = [
    {"icon": "\U0001F4B0", "tag": "Model the lag, not just the payback", "title": "A one-year payback still leaves a $100–200B financing gap at an 8 GW/year pace — size the working capital, not the ROI."},
    {"icon": "\U0001F4E1", "tag": "Watch for a third site announcement", "title": "Colossus 2 is nearly out of land; a new major site announcement is the tell that the 5–10 GW guidance is real."},
    {"icon": "\U000026A1", "tag": "Track the gas build, not the GPU count", "title": "Power generation is the binding constraint — dozens to hundreds of gas generators is the actual schedule risk."},
    {"icon": "\U0001F50D", "tag": "Separate demand from price", "title": "Bull and bear here agree on volume and disagree on price per token — treat those as two different questions in any AI-capex model."},
    {"icon": "\U0001F916", "tag": "Judge models on questions asked", "title": "Both speakers rate AI by whether it interrogates before answering — a usable proxy for whether a model is ready for real-world tasks."},
]

RISKS = [
    "Giesige is presenting his own published analysis and says it has already significantly changed since he put it out three weeks ago — these are his working figures spoken in conversation, not a current report.",
    "Cost and revenue per gigawatt are deliberately chosen assumptions, not disclosed numbers: he picks $50B/GW capex against Gavin Baker's $60B/GW specifically to model the bull case.",
    "Brian is a supporter of Giesige's Patreon and is presenting his slides on-screen; this is a friendly-channel conversation between two creators who cross-promote.",
    "Auto-captions garbled several proper nouns — one SpaceX product listed alongside Starlink came through as 'cursor' and a name in the Memphis segment came through as 'Hank Taipale'; neither is named here because neither could be resolved with confidence.",
    "Both speakers are long-standing Tesla/SpaceX-ecosystem commentators; the framing throughout assumes Elon's companies execute faster and cheaper than peers.",
]

HOT_TAKES = [
    {"take": "With artificial intelligence, it seems really it's so good already, but compared to what it's going to be, I still see it as really stupid.",
     "cite": "\u2014 Jordan Giesige", "why": "Said while using it daily and bullish on the buildout \u2014 the complaint is that it never asks probing questions."},
    {"take": "A truly useful humanoid robot is probably 3 to 4 years away.",
     "cite": "\u2014 Jordan Giesige", "why": "Dated prediction, and he holds it even after Brian points at Unitree's imminent IPO \u2014 narrowing it to usefulness for an average person, not factories."},
    {"take": "There's pretty much going to be infinite demand, because the more AI you use, the more AI you use.",
     "cite": "\u2014 Jordan Giesige", "why": "The load-bearing assumption under the whole payback thesis; he concedes surplus compute is an unavoidable risk but doesn't expect it."},
    {"take": "90 to 95% of the businesses out there still haven't worked out how to get that juice out of the lemon.",
     "cite": "\u2014 Jordan Giesige", "why": "Puts almost all future growth in adoption rather than model quality \u2014 he sees decreasing returns from frontier model gains."},
    {"take": "Google's products tend to get worse every day. I still have all my Google Home smart speakers, but they're getting dumb.",
     "cite": "\u2014 Brian, FutureAzA", "why": "He's replaced Google search with Grok for research; blames the shift from best product to most profitable product."},
    {"take": "ChatGPT has probably as many users as there are people who have ever lived, because when people run out of tokens they create a second account.",
     "cite": "\u2014 Brian, FutureAzA", "why": "Hyperbole aimed at a real point \u2014 he doesn't believe today's token prices reflect what the compute costs."},
]

OTHER_NEWS = [
    {"icon": "\U0001F4DA", "title": "Sources referenced this episode: Gavin Baker (per-GW cost estimates), SemiAnalysis (Memphis power generation lined up), an xAI/SpaceX earnings call (5–10 GW figure), and The Limiting Factor's own terrestrial-compute video", "tag": "Named sources"},
    {"icon": "\U0001F6E0", "title": "Giesige notes xAI/SpaceX deploys not just the data centers but all supporting infrastructure faster than anyone, 'stepping on some toes' and asking forgiveness afterwards", "tag": "Execution style"},
    {"icon": "\U0001F5A5", "title": "Analogy for AI's adoption curve: 1980s PCs needed heavy technical knowledge to build and run; plug-and-play is what expanded the market, and AI's 'harness' is at the pre-plug-and-play stage", "tag": "Analogy"},
    {"icon": "\U0001F3AC", "title": "A follow-up episode on whether Tesla's 4680 cell is obsolete was announced; Brian is travelling in Nepal at publication", "tag": "Upcoming"},
]

GLOSSARY = [
    {"term": "Colossus 1 / Colossus 2", "def": "xAI's two data center locations — Colossus 1 is a single building, Colossus 2 is two buildings with a third under way."},
    {"term": "Megapack", "def": "Tesla's utility-scale battery unit, used at Colossus for both overnight coverage and peak-power bursts."},
    {"term": "Sun-synchronous orbit", "def": "An orbit that keeps a satellite constantly facing the sun, removing the night-time gap that forces terrestrial solar setups to carry batteries."},
    {"term": "Vera Rubin", "def": "Nvidia's next GPU generation, cited as the upside case for compute rental rates rising."},
    {"term": "Coherent cluster", "def": "A GPU cluster operating as one unified machine; Nvidia did not believe this was achievable past 100,000 GPUs before xAI did it."},
    {"term": "Total addressable market (TAM)", "def": "The full set of potential users — Giesige's argument is that AI growth comes from expanding it rather than from better models."},
]
