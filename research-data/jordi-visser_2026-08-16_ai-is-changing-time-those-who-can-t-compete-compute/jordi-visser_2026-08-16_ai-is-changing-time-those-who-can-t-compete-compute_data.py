"""
Jordi Visser — "AI Is Changing Time: Those Who Can't Compete, Compute" (2026-08-16)
"""

META = {
    "title": "AI Is Changing Time: Those Who Can't Compete, Compute",
    "channel": "Jordi Visser",
    "speakers": "Jordi Visser",
    "date": "2026-08-16",
    "video_url": "https://youtu.be/VCaQNfBJLvk",
    "thread_line": "6 threads · a weekly recap spanning the compute-capital mobilization wave, Google's AI talent drain, SpaceX's space-based data centers, Visser's portfolio scorecard and conviction-tracking prompt, a new crypto/stablecoin thesis, and the macro debasement trade",
    "category": "market",
}

SNAPSHOT = [
    "Visser's standing thesis: compute demand is structurally insatiable, and this week brought concrete evidence — Apollo, BlackRock, Blackstone, Brookfield, Goldman Sachs and KKR launching AI infrastructure financing platforms to mobilize over $500B, Morgan Stanley committing to $1.5T more, Alphabet raising $25B, and Intel upsizing a stock offering to $20B.",
    "Nvidia's 2020-era A100 GPU is now contracted out to 2029 and completely sold out — the assumed useful life of a GPU generation has stretched from 2-3 years to 6-9 years because data center capacity can't keep up.",
    "Google's AI talent is reading a capital-allocation pivot as a downgrade: Jeff Dean and Demis Hassabis are both flagged as flight risks (per the All-In Podcast and Moonshots podcast), and Visser argues Google may be settling into an 'infrastructure landlord' role rather than winning the frontier-model race.",
    "SpaceX guided to 6-8 GW (possibly above 10 GW) of new data center capacity in 2027 alone on its first earnings call, with 80% earmarked for space-based data centers and an exclusive Nvidia Vera Rubin GPU deal.",
    "His concentrated AI portfolios are compounding well ahead of the index — the 10-name portfolio is up 94% YTD (103% equal-weighted) at an average forward PEG of just 0.8 — and he's releasing a prompt that scores his own conviction shifts from his weekly transcripts.",
    "New highest-conviction call: after physical compute, the next constraint is financial — stablecoins and tokenization for AI agents — with Figure's earnings and a Pompliano podcast appearance cited as early evidence.",
    "Macro thread built around a Louis Gave (Gavekal) note on the yen intervention: weak labor and inflation data argue against Fed hikes, and Visser is recommending the 'debasement trade' — gold, silver, and eventually Bitcoin.",
]

THEMES = [
    {
        "id": "compute-insatiable",
        "color": "green",
        "badge": "High conviction",
        "status": "STRUCTURAL BULL — STANDING THESIS",
        "title": "Compute Demand Has No Ceiling — and the Capital Is Now Showing Up to Match It",
        "lead": "**Visser's core standing call is that compute demand is structurally insatiable, and this week's capital-raising wave is the confirming evidence.**",
        "bullets": [
            "Coding agents needed 10-100x more compute this year than chatbots needed last year, and each new generation needs 'another 10x, then another 10x' — the industry stays compute-starved at every step.",
            "Jensen Huang declared 'compute is the new economy' at a Morgan Stanley event in March; this week Nvidia framed AI-factory computing as its own investable asset class.",
            "Apollo, BlackRock, Blackstone, Brookfield, Goldman Sachs and KKR are launching AI compute infrastructure financing platforms to mobilize over $500B of third-party capital, so hyperscalers stop funding builds off their own balance sheets; Morgan Stanley separately committed to facilitate $1.5T in infrastructure financing.",
            "Alphabet raised $25B and Intel launched a $15B stock offering this week (upsized to $20B and priced above issuance, for a company worth under $100B a year ago) — capital flooding in on both the equity and debt side.",
            "Nvidia's 2020-era A100 GPU is contracted all the way out to 2029 and completely sold out; the assumed useful life of a GPU generation has stretched from an original 2-3 year estimate to 6-9 years because not enough new data center capacity exists to replace it.",
            "Data center delays reported in the media are real but minor and already priced into his models — and arguably a good thing, since memory supply can't keep up with GPU buildout anyway.",
            "The US is exempting data center bonds from key securitization rules, potentially opening the door to more asset-backed debt sales to fund the buildout.",
        ],
        "quote": {
            "text": "It's like walking into a supermarket. If they didn't have any food but cans of sardines, you would immediately love cans of sardines. Even if that was the last thing you wanted, that's what's happening — the demand is too great.",
            "cite": "— Jordi Visser",
        },
        "watch": None,
        "names": [
            {"name": "Nvidia (NVDA)", "blurb": "A100 sold out through 2029; framing AI-factory compute as its own investable asset class."},
            {"name": "Apollo (APO)", "blurb": "One of six firms launching AI compute infrastructure financing platforms."},
            {"name": "BlackRock (BLK)", "blurb": "Part of the group mobilizing $500B+ in third-party AI infrastructure capital."},
            {"name": "Blackstone (BX)", "blurb": "Part of the group mobilizing $500B+ in third-party AI infrastructure capital."},
            {"name": "Brookfield (BN)", "blurb": "Part of the group mobilizing $500B+ in third-party AI infrastructure capital."},
            {"name": "Goldman Sachs (GS)", "blurb": "Part of the group mobilizing $500B+ in third-party AI infrastructure capital."},
            {"name": "KKR (KKR)", "blurb": "Part of the group mobilizing $500B+ in third-party AI infrastructure capital."},
            {"name": "Morgan Stanley (MS)", "blurb": "Committed to facilitate $1.5T in infrastructure financing."},
            {"name": "Alphabet (GOOGL)", "blurb": "Raised $25B this week."},
            {"name": "Intel (INTC)", "blurb": "Upsized a stock offering to $20B, priced above issuance."},
        ],
    },
    {
        "id": "google-brain-drain",
        "color": "amber",
        "badge": "Contested",
        "status": "TALENT FLIGHT RISK — MULTIPLE AT STAKE",
        "title": "Google's Capital-Allocator Pivot and the AI Talent Exodus",
        "lead": "**Google may be choosing to become the infrastructure landlord of AI rather than win the frontier-model race, and its top researchers are reading the signal.**",
        "bullets": [
            "The All-In Podcast's 'Google's AI Brain Drain' episode frames Google's reorganization as a capital-allocation shift; David Sacks calls it a 'two-horse race' and argues AI infrastructure may be a cleaner business than model development.",
            "Like Meta and SpaceX, Google appears to be selling spare compute rather than burning all of it on model training, as investors push back on negative free cash flow.",
            "Jeff Dean and Demis Hassabis are both flagged as flight risks; Hassabis reportedly wants to leave but is staying for now, with some predicting he could depart within a year — Visser: 'if talent's leaving, multiples compress, plain and simple.'",
            "Brad Gersner, in a separate talk referenced this week, said Nvidia has hit financing limits (hence the outside financing vehicles) and that Frontier Labs are willing to pay 4-5x market pricing to secure scarce compute — a lending relationship Visser calls explicitly circular, since Nvidia is financing the same buyers who then spend it on Nvidia chips.",
            "The Moonshots podcast ran two relevant episodes this week — one with Imad Mostaque, one with a researcher named Kush — whose framing (credited via Alex): 'those who can't compete on frontier models go toward compute,' which is what Meta, xAI and Google have all done.",
            "Per Kush, Google's talent brand has deteriorated: MIT-cohort young builders no longer see Google as the dream destination, favoring OpenAI, Anthropic, xAI and other Frontier Labs instead.",
            "Google has committed roughly $200B in capex this year to compute infrastructure, with a documented ~30% ROIC and tax advantages via accelerated depreciation — a near-certain return, versus tens of billions with high variance and no guaranteed return for frontier model development.",
        ],
        "quote": {
            "text": "The rational endgame ... is the large company as capital allocator and infrastructure landlord to an ecosystem of mission-driven vehicles it partly owns.",
            "cite": "— Jordi Visser",
        },
        "watch": "Talent departures and Google settling into an infrastructure-landlord role are trends Visser is reading into recent signals, not confirmed outcomes — he frames the multiple-compression risk as live, not certain.",
        "names": [
            {"name": "Alphabet (GOOGL)", "blurb": "Reading a capital-allocation pivot; ~$200B capex commitment this year with a documented ~30% ROIC."},
            {"name": "Meta (META)", "blurb": "Cited alongside Google and SpaceX as selling spare compute rather than burning it all on training."},
            {"name": "Nvidia (NVDA)", "blurb": "Financing buyers of its own chips, which Visser calls a circular lending relationship."},
            {"name": "OpenAI", "blurb": "Named as a Frontier Lab now favored over Google by young AI talent."},
            {"name": "Anthropic", "blurb": "Named as a Frontier Lab now favored over Google by young AI talent."},
            {"name": "xAI", "blurb": "Named as a Frontier Lab now favored over Google by young AI talent, and among those going toward compute rather than the frontier-model race."},
        ],
    },
    {
        "id": "spacex-terrabase",
        "color": "green",
        "badge": "High conviction",
        "status": "GUIDED 6-8GW+ IN 2027 ALONE",
        "title": "SpaceX's Space-Based Data Center Bet",
        "lead": "**SpaceX says it's building data centers in space at a scale that 'sounds impossible' — Visser is treating it as a validated, still-underpriced call option.**",
        "bullets": [
            "On SpaceX's first earnings call, Elon Musk guided to 6-8 GW of incremental data center capacity in 2027 alone, possibly well above 10 GW, targeting roughly 10 GW by year-end 2027.",
            "SemiAnalysis published a piece backing SpaceX's numbers this week.",
            "About 80% of that output is earmarked for space-based data centers under the 'Terrabase' project.",
            "SpaceX has gone exclusive with Nvidia, putting Vera Rubin-architecture GPUs in orbit — Musk: 'We think the Vera Rubin architecture is the best architecture. We're exclusive to Nvidia.'",
            "Visser's framing: Musk has already proven he can build data centers faster than anyone, and a SpaceX/Starlink stake should be treated as a call option on this bet paying off.",
        ],
        "quote": None,
        "watch": "Visser says the scale Musk described 'sounds impossible' even to him — he says he believes it, not that it's confirmed.",
        "names": [
            {"name": "SpaceX", "blurb": "Guided 6-8GW+ of new data center capacity in 2027 alone; 80% earmarked for space-based Terrabase data centers."},
            {"name": "Nvidia (NVDA)", "blurb": "Exclusive Vera Rubin GPU supplier for SpaceX's in-orbit data centers."},
        ],
    },
    {
        "id": "portfolio-scorecard",
        "color": "green",
        "badge": "High conviction",
        "status": "10-NAME PORTFOLIO +94% YTD",
        "title": "The Portfolio Scorecard and a Reusable Conviction-Tracking Prompt",
        "lead": "**Visser's concentrated AI portfolios are compounding far ahead of the index, and he's sharing the exact prompt he uses to track his own conviction shifts over time.**",
        "bullets": [
            "Weekly recap: S&P +40bps, IWM +1%, QQQ +1%, his JV AI thematic portfolio +3%, with fresh all-time highs across major indices; S&P earnings growth 51% YoY, sales growth 15% YoY, global EPS growth ~47% YoY.",
            "His 100-name portfolio is up 46% YTD, the 25-name up 74%, and the 10-name up 94% (equal-weighted average return 103%, median 65%); best performer up 249%, worst — Nvidia — still up 16.5% and outperforming the S&P by 13%.",
            "The 10-name group trades at an average forward PEG of 0.8 (median 0.81) despite being up 103% YTD, because median forecast earnings growth next year is 40% (7 of 10 names expected to grow earnings over 30%).",
            "He's releasing a prompt (to be uploaded this weekend) that analyzes a chronological series of his own weekly transcripts to score how his long-term conviction, short-term outlook, and risk appetite have shifted over time — and suggests running it on any podcast host's transcripts, not just his own.",
            "His own risk-posture history illustrates the tool: 'selective risk reduction' starting May 17 (fully out of Micron), through capital preservation and de-risking, back to neutral, then turning buyer again once Micron broke below $900, with 'combing through the rubble' and 'situational awareness' marking the recent turn — the portfolio has now recovered more than 50% of its prior drawdown.",
        ],
        "quote": None,
        "watch": None,
        "names": [
            {"name": "Nvidia (NVDA)", "blurb": "Worst performer of his 10-name portfolio, still up 16.5% YTD and outperforming the S&P by 13%."},
            {"name": "Micron (MU)", "blurb": "Fully exited May 17 in a risk-reduction move; re-bought once it broke below $900."},
        ],
    },
    {
        "id": "crypto-financial-rails",
        "color": "amber",
        "badge": "High conviction, still emerging",
        "status": "NEWEST THESIS — STAKED ON PUBLICLY",
        "title": "Crypto Becomes the Next Compute Constraint: Financial Guardrails for AI Agents",
        "lead": "**Visser's next structural call: once physical compute constraints ease, the bottleneck shifts to financial infrastructure — stablecoins, tokenization, and crypto rails built for AI agents.**",
        "bullets": [
            "His stated new highest-conviction call: 'the next constraint is not physical, it's financial — the guardrails, consumer agents, the settlement, it's stablecoins, it's tokenization' — he says if he's proven wrong within a year, this will be why.",
            "Figure reported earnings this week: consumer loan marketplace volume of $4.3B, up 132% YoY, with its tokenized on-chain marketplace ('Figure Connect') expected to approach 70% of volume.",
            "He discussed Figure at length with Anthony Pompliano on Pompliano's podcast this week, which he recommends watching.",
            "Stablecoin card spending volume surged another 16% this week; a US bank regulator opened national charters to Bitcoin and crypto firms, while the SEC is moving ahead even as Congress stalls on the Clarity Act — he expects a volume explosion regardless of whether that bill passes.",
            "He's building his own roughly 45-name crypto 'ecosystem' index across about 10 verticals (4-5 names each), tracked against Bitcoin performance.",
            "He cites Elon Musk (via Cloudflare's forecast) that bot traffic will exceed human traffic by roughly 1,000x within five years, tying AI-agent growth directly to the need for agent-native payment rails.",
        ],
        "quote": {
            "text": "Bitcoin is a representation of the S&P 500 of the future.",
            "cite": "— Jordi Visser",
        },
        "watch": "Visser explicitly stakes his own credibility on this being his newest and least-tested thesis, rather than presenting it as settled.",
        "names": [
            {"name": "Bitcoin (BTC)", "blurb": "Framed by Visser as 'the S&P 500 of the future'; anchor of his new ~45-name crypto ecosystem index."},
            {"name": "Figure", "blurb": "Reported $4.3B in consumer loan marketplace volume this week, up 132% YoY, with Figure Connect nearing 70% of volume."},
        ],
    },
    {
        "id": "macro-debasement",
        "color": "amber",
        "badge": "Contested",
        "status": "WEAK LABOR + STICKY FED — GOLD/SILVER MOVED, BITCOIN HASN'T",
        "title": "The Debasement Trade: Weak Labor Data, a Contested Fed, and Gold/Silver/Bitcoin",
        "lead": "**A Louis Gave note on the yen intervention crystallized Visser's macro view: labor and inflation data both argue against Fed hikes, and gold, silver, and eventually Bitcoin are where the mispricing sits.**",
        "bullets": [
            "Gavekal's Louis Gave published a piece the same week — an unusually broad release for him, matching Visser's own Substack timing — connecting the yen intervention to AI, US/Japan debt, and a 'compute dollar' potentially reshaping, not destroying, dollar dominance in place of the petrodollar.",
            "Kevin Warsh reportedly lost credibility around the yen-intervention week, per commentary Visser cites, and is set to speak at Jackson Hole; Bill Dudley reported Warsh floated dropping the PCE index as the Fed's primary inflation gauge as soon as January.",
            "Rate-cut odds have moved to roughly 31% priced for a September cut and 80% for a BOJ move, down from roughly 50/50 before the last payrolls report — yet long-term yields still haven't fallen, and Bank of America is still calling for three more hikes this year.",
            "Broader inflation gauges (Atlanta sticky CPI core 2.5%, CPI core 2.6%, Dallas trimmed mean ~2.2-2.4%, Cleveland 2.7%) sit well below the PCE core reading the Fed anchors to, which Visser calls the outlier.",
            "Labor data is weak across the board: the 6-month rate of change in aggregate weekly payrolls (hours + wages + hires) is at its lowest since 2012; labor force participation is declining; hourly earnings growth dropped to 3.2%; job growth ex-healthcare and leisure is thin.",
            "His read: buy the 'debasement trade' — gold, silver, and Bitcoin; gold and silver have already moved to reflect this, Bitcoin has not moved yet.",
            "China added 20 tons of gold in July, its largest monthly purchase since October 2023, and is also adding gold reserves via Hong Kong; the Bank of Korea resumed gold buying after a 13-year pause.",
        ],
        "quote": {
            "text": "AI and stable coins could reshape rather than simply destroy dollar dominance.",
            "cite": "— Louis Gave, via Visser's summary",
        },
        "watch": "Visser is relaying Gave's framing and his own charts here — the rate-path and PCE-methodology claims aren't independently sourced beyond that in this video.",
        "names": [
            {"name": "Bitcoin (BTC)", "blurb": "Part of the 'debasement trade'; hasn't moved yet despite gold and silver already re-rating."},
            {"name": "Gold", "blurb": "Already moved as part of the debasement trade; China added 20 tons in July, its largest monthly purchase since October 2023."},
            {"name": "Silver", "blurb": "Already moved as part of the debasement trade, alongside gold."},
        ],
    },
]

TAKEAWAYS = [
    {"icon": "\U0001F4DD", "tag": "Reusable tool", "title": "Try Visser's conviction-tracking prompt (out this weekend) on transcripts from any analyst or podcast you follow regularly, not just his own."},
    {"icon": "\U0001F440", "tag": "Watch", "title": "Track whether Jeff Dean or Demis Hassabis actually leave Google — Visser ties that directly to multiple compression for the stock."},
    {"icon": "\U0001F4B0", "tag": "New thesis", "title": "Start researching stablecoin/tokenization infrastructure (Figure, agent payment rails) now — Visser stakes his next 12 months of credibility on this being the binding constraint."},
    {"icon": "\U0001F947", "tag": "Positioning", "title": "If buying the debasement trade, note gold and silver have already re-rated by his own read — Bitcoin is the lagging leg, not confirmed to follow."},
    {"icon": "\U0001F6F0", "tag": "Follow-up", "title": "Watch SpaceX's actual 2027 data-center build-out against the 6-10GW guidance as the real test of the Terrabase thesis."},
]

RISKS = [
    "Visser explicitly discloses his own portfolio positioning and long-standing bullish bias throughout — his own thematic portfolios are levered to the exact compute/AI/crypto themes he's describing, so treat the framing as a disclosed, not neutral, lens.",
    "Several figures (Fed rate-cut odds, PCE methodology commentary, Figure's volume numbers) are relayed secondhand from Bill Dudley, Louis Gave, and company earnings releases rather than verified against primary filings inside this video.",
    "A macro strategist's name is caption-garbled across the transcript ('Lewis Gau,' 'Gavka') — resolved here with high confidence to Louis-Vincent Gave of Gavekal Research given the exact contextual fit (his firm name, his known yen/AI/debt commentary), consistent with the skill's guidance on resolving obvious cases rather than leaving a clearly-identifiable source unnamed.",
    "The video opens with an unrelated personal segment (Maine, a 9/11 remembrance) and a scam warning — Visser states he never DMs trades via WhatsApp, X, or LinkedIn, which is useful context for evaluating any message claiming to be from him but isn't a stock-related claim.",
]

HOT_TAKES = [
    {"take": "Go against things you've heard from Michael Burry and Jim Chanos in particular — they don't ever turn around and say, you know what, we were wrong.",
     "cite": '— Jordi Visser', "why": 'Names two famous bears directly and makes never admitting error the reason to fade them.'},
    {"take": 'We will never be able to pick a bottom. Nobody can do that, and certainly not me.',
     "cite": '— Jordi Visser', "why": 'Said by someone publishing a weekly risk-reward score — he sells the process while disclaiming the thing viewers want from it.'},
    {"take": "I like to be bearish equally as bullish if I think it's going to save me money.",
     "cite": '— Jordi Visser', "why": 'Rejects having a permanent stance, in a genre built on permanent stances.'},
    {"take": "Academics ask what the evidence tells us has happened under comparable conditions. Markets ask what's going to happen before everyone else realizes it. This is the money-making side.",
     "cite": '— Jordi Visser', "why": 'Explicitly ranks anticipation over evidence — the framing behind everything else he does on the show.'},
    {"take": "The new businesses being created would have to come from the frontier model side — that's my opinion, at higher probability.",
     "cite": '— Jordi Visser', "why": 'Puts the next wave of company formation inside the labs rather than in the application layer everyone else is crowding into.'},
]

OTHER_NEWS = [
    {"icon": "\U0001F6A8", "title": "Visser warns of AI bots impersonating him across platforms — he never initiates trade recommendations via WhatsApp, X, or LinkedIn DMs, and may not respond even to legitimate outreach given volume.", "tag": "Safety notice"},
    {"icon": "\U0001F310", "title": "He built his new site, visserlabs.com, largely by prompting AI tools — about an hour of work, plus roughly a day to configure the domain — and it scored 100/100 on a Network Solutions site assessment.", "tag": "Personal update"},
    {"icon": "\U0001F3A7", "title": "Sourcing named in this episode: the All-In Podcast ('Google's AI Brain Drain'), the Moonshots podcast (episodes with Imad Mostaque and with a researcher named Kush), Anthony Pompliano's podcast (Figure discussion), SemiAnalysis (SpaceX data-center analysis), Louis-Vincent Gave/Gavekal Research (yen-intervention and 'compute dollar' piece), Bill Dudley (relaying Kevin Warsh's Fed commentary), Brad Gersner (talk on Nvidia financing limits), and David Sacks (the 'two-horse race' framing). Visser also names Michael Burry and Jim Chanos as bears whose all-or-nothing calls he explicitly contrasts with his own probabilistic approach.", "tag": "Sources referenced"},
]

GLOSSARY = [
    {"term": "AI factory", "def": "Jensen Huang's term for the new infrastructure paradigm treating large-scale AI compute buildout as the core unit of the AI economy, framed this week by Nvidia as its own investable asset class."},
    {"term": "Compute dollar", "def": "Louis Gave's proposed idea of AI/compute infrastructure becoming a pillar of dollar dominance, replacing the historical role of the petrodollar."},
    {"term": "Debasement trade", "def": "Visser's term for positioning in gold, silver, and Bitcoin as a hedge against currency debasement from continued deficit spending."},
    {"term": "Forward PEG ratio", "def": "A stock's forward price-to-earnings ratio divided by its expected earnings growth rate; below 1.0 generally signals growth priced cheaply relative to the multiple paid."},
    {"term": "Terrabase", "def": "SpaceX's project to build data centers in space, using in-orbit Nvidia Vera Rubin GPUs, with roughly 80% of SpaceX's guided 2027 data center capacity earmarked for it."},
    {"term": "Tokenization (Figure Connect)", "def": "Moving traditional loan/asset marketplace volume onto blockchain-based settlement rails; Figure's tokenized marketplace is expected to approach 70% of its total volume."},
    {"term": "Six-month rate of change, aggregate weekly payrolls", "def": "A broader labor-market gauge combining weekly hours, wage growth, and job hires, which Visser cites as showing the weakest reading since 2012."},
]
