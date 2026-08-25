"""
Per-video data for youtube-research-brief.
"""

META = {
    "title": "Google's AI Brain Drain, SpaceX's Huge Quarter, Airtable's 90% Collapse, US Data Fuels China AI",
    "channel": "All-In Podcast",
    "speakers": "Jason Calacanis, David Sacks, David Friedberg, Brad Gerstner (guest)",
    "date": "2026-08-08",
    "video_url": "https://www.youtube.com/watch?v=muRIXCDw-k0",
    "thread_line": "5 threads · Google's AI brain drain, SpaceX Q2 earnings bull case, SpaceX's compute financing risk, Airtable/Bending Spoons SaaS lesson, US data fueling Chinese AI",
}

SNAPSHOT = [
    "Google had two major AI staff shakeups this week: Demis Hassabis moved to chair of DeepMind (Google frames it as a promotion; reports describe it as being kicked upstairs), and Jeff Dean plus three other AI superstars left to start a new company, Discovery Loop — Google shares fell 4% (~$200B of market cap) on the Dean news.",
    "The panel's read: this reflects a rational capital-allocation shift, not dysfunction — AI compute infrastructure is \"high alpha, low beta\" (reliable, tax-advantaged, high-ROIC), while frontier model development has become \"high alpha, high beta\" as open-weight models catch up fast, pushing top scientists toward startups instead.",
    "SpaceX posted its first earnings report as a public company: revenue $7.8B (+92% YoY), AI/compute revenue (\"Elon Web Services\") more than tripled QoQ to $2.6B, and Elon pulled forward SpaceX's $1 trillion ARR target from 2031 to 2030 — yet the stock fell 13% on the print and is down 30% since its June IPO, now valued around $1.4 trillion.",
    "The panel flags a real open question behind SpaceX's bull case: financing a jump from ~2 to 5-10 gigawatts of compute next year could cost $300B+, and it's unclear whether that gets funded by debt, dilutive equity, or continued Nvidia vendor financing — echoing Bill Gurley's \"circular revenue\" concern about the whole AI-infrastructure buildout.",
    "Airtable sold to Bending Spoons for $1.28B (about 10% of its 2021 peak $11.7B valuation) despite $480M of revenue growing 20%/year and near $1B of cash — the panel's diagnostic: only 30% of its sales team was hitting quota, evidence a board-driven push into sales-led growth failed and the company should have stayed product-led.",
    "The panel is explicit that this is not a signal for all of SaaS — sticky, compliance-locked enterprise software (Microsoft, Salesforce) is framed as safe, while no-code tools like Airtable are the software category most exposed to disruption by coding AI agents (Claude Code, Lovable, etc.).",
    "A Forbes investigation claims US data-labeling startups (Surge AI, Mercor) are selling the same expert-curated AI training data to both US labs and top Chinese AI labs, sparking a live, unresolved policy debate between Sacks (skeptical this data is genuinely proprietary or strategically decisive) and Calacanis (calls it \"not very patriotic\").",
    "Housekeeping: the panel announced the 5th annual All-In Summit (Sept 13-15, LA) with Jensen Huang, Satya Nadella, and Gwynne Shotwell among confirmed speakers.",
]

THEMES = [
    {
        "id": "google-ai-brain-drain",
        "color": "amber",
        "badge": "Contested",
        "status": "DEMIS HASSABIS MOVED TO CHAIR OF DEEPMIND; JEFF DEAN + 3 LEFT FOR A NEW STARTUP",
        "title": "Google's AI Brain Drain: Rational Capital Shift or Real Crisis?",
        "lead": "The panel reads Google's staff shakeup as evidence that AI compute infrastructure has become a better business than building frontier models — pushing top scientists out the door.",
        "bullets": [
            "This week: Demis Hassabis moved to chair of DeepMind (Google calls it a promotion; reports describe it as being kicked upstairs); Axios reported Gemini 3.5 Pro is \"months behind,\" partly attributed to low morale; several top researchers including Gemini's co-lead have left for competing labs.",
            "Jeff Dean — employee #30, at Google 27 years, joined 1999 — is leaving with three other AI superstars to start Discovery Loop, focused on deep scientific breakthroughs in AI. Google shares fell 4% (~$200B of market cap) on the news.",
            "Freeberg's framing: CapEx on compute infrastructure is \"high alpha, low beta\" — Google committed $200B to AI infrastructure this year, gets accelerated-depreciation tax advantages (a ~26% effective discount at current corporate tax rates), and faces extreme, obvious demand. Model development, by contrast, has become \"high alpha, high beta\" as open-weight models catch up to frontier ones fast, making the ROI case much harder to defend internally.",
            "Google's real advantage, per the panel: the largest enterprise and consumer installed base in the world — 5 products with 3B+ monthly users each (Android, Search, Gmail, Chrome, YouTube), 13 products with 1B+ users including Gemini (950M+ monthly active users in Q2, tripling YoY) — meaning it doesn't need the single best model to run an enormous, model-agnostic business (it can work with Anthropic, OpenAI, and open-weight models simultaneously, and holds equity stakes in both SpaceX and Anthropic).",
            "Brad Gerstner sees the identical dynamic at Microsoft (Satya cited a Morgan Stanley figure of 30%+ ROIC on \"tokens as a service\") and calls out an inherent channel conflict: internal teams building frontier models compete with the cloud unit for the same compute the cloud unit wants to rent out externally — the same conflict he flags at SpaceX (renting Colossus compute to Anthropic while also building Grok/Cursor). Anthropic and OpenAI avoid this entirely by staying pure model-layer companies.",
            "Sacks's market-structure read: frontier intelligence has become a duopoly (Anthropic + OpenAI), down from ~5 credible contenders a year ago — a two-tier structure where frontier labs can charge a premium (Apple/Android analogy: premium experience wins the monetization even if open models win raw usage) and commodity/6-12-months-behind models can only monetize compute and services, not the model weights themselves. Anthropic's ARR reportedly went from $10B at the start of the year toward a revised $110-120B+ year-end estimate, beating its own initially-doubted $100B target.",
            "Calacanis pushes back hard: he uses non-frontier/open-source models almost exclusively and finds them \"good enough\" for 95% of his work (a public disagreement with Elon Musk, who called the gap \"a world of difference\"); Sacks and Freeberg both partially concede this for casual use cases, but argue competitive, high-stakes industries (e.g. hedge funds) and specialized domains (life sciences, video rendering, where Google/Gemini and Isomorphic Labs still lead) will keep paying a premium for frontier and specialized models — most enterprises will end up blending both tiers.",
        ],
        "quote": {"text": "I think that the market for frontier intelligence has become a duopoly.", "cite": "— David Sacks"},
        "watch": "Both Jensen Huang's claim that closed models are actually cheaper once training/fine-tuning/safety costs are included, and Elon Musk's claim that frontier models remain \"a world of difference\" ahead, are relayed secondhand by the panel from other public statements this week — not independently verified in this episode.",
        "names": [
            {"name": "Google / Alphabet", "blurb": "Down 4% on the Jeff Dean news; committed $200B to AI infrastructure capex this year."},
            {"name": "Anthropic & OpenAI", "blurb": "The panel's named 'duopoly' — Anthropic's ARR reportedly tracking to $110-120B+ by year-end, well above its own initial $100B target."},
            {"name": "Discovery Loop", "blurb": "New company founded by Jeff Dean and three other departing Google AI researchers, focused on deep scientific breakthroughs."},
        ],
    },
    {
        "id": "spacex-bull-case",
        "color": "green",
        "badge": "Confirmed event",
        "status": "FIRST EARNINGS AS A PUBLIC COMPANY — STOCK FELL 13% DESPITE A BEAT-AND-RAISE",
        "title": "SpaceX's Q2: A Beat-and-Raise That the Market Sold Anyway",
        "lead": "Revenue up 92%, AI revenue tripled, and Elon pulled his $1 trillion ARR target forward a year — yet the stock is down 30% since its June IPO.",
        "bullets": [
            "Q2 results: revenue $7.8B (+92% YoY, +67% QoQ); AI/compute revenue (\"Elon Web Services,\" renting the Colossus cluster to Anthropic and Google, not yet including Cursor) more than tripled QoQ to $2.6B; capex $18.4B for the quarter, 6x YoY, implying a ~$75B annualized run rate.",
            "Guidance: $100B ARR by year-end; the $1 trillion ARR target was pulled forward from 2031 to 2030. For context, Morgan Stanley's own 2030 revenue estimate is $325B, and the company did only $18B of total revenue last year — the market isn't pricing in either the bear or the bull case cleanly yet.",
            "Starlink specifics: $4.3B quarterly revenue, $2.6B adjusted EBITDA, 12M subscribers (doubled YoY) at $66/month ARPU, +20% QoQ subscriber growth. Freeberg's extrapolation: at a ~24M-subscriber run rate plus enterprise (e.g. airline) scaling, Starlink alone could reach ~$40B revenue and ~$30B free cash flow within a year — and at a 30x multiple (justified by high-renewal, low-CAC subscription economics), Starlink alone could be worth ~$1 trillion within roughly 18 months, effectively funding the rest of SpaceX's more speculative bets.",
            "Segment breakdown: connectivity/Starlink $2.6B adjusted EBITDA; Space roughly breakeven (~-$200M); AI +$1.1B (flagged as possibly inflated by temporary compute-scarcity pricing).",
            "Starship's most recent test flight succeeded — heat shield worked, booster/ship recovered floating in the ocean, and 20 V3 satellites were deployed and made contact as a test. Each Starship launch can deploy 60 V3 satellites (~60 terabits/sec of added network capacity) versus Falcon 9's ~27 V2 satellites (~2.6 terabits/sec) — over 20x more capacity per launch, unlocking the direct-to-cell roadmap and (per Elon on the call) potentially up to half of total internet traffic long-term.",
            "Data-center plan: ~1.4GW of compute now, ~2GW by year-end, guided to 5-10GW next year (\"closer to 10 than 5\"). Elon's own math on the call: hitting $100B ARR requires only ~2GW running near the current ~$30-50/watt spot price — before counting Starlink, launch, or Grok/Cursor at all.",
            "Elon's own framing of SpaceX's edge, quoted on the call: physical build execution. The panel contrasts this with Google and DoorDash, both cited as recent examples of stocks punished by the market for heavy capex spend — reinforcing how unusual Elon's willingness to plow Starlink's cash flow into higher-risk bets (Terrafab, AI data centers, Starship) actually is among public-company CEOs.",
        ],
        "quote": {"text": "Putting up data centers is nothing compared to the difficulty of putting up a rocket.", "cite": "— Elon Musk, on SpaceX's Q2 earnings call, as relayed by David Sacks"},
        "watch": "SpaceX's price-to-sales ratio has already compressed from ~160x at IPO to ~45x as revenue has scaled — some real repricing has happened, but Brad Gerstner is explicit that entry price still matters: he publicly said on CNBC the day of the IPO that he wanted to own the company but wasn't sure that was the day to buy it above a $2 trillion valuation.",
        "names": [
            {"name": "SpaceX (Starlink / AI compute / Space segments)", "blurb": "Valuation settled near $1.4 trillion post-IPO, down from over $2 trillion at listing."},
            {"name": "Grok & Cursor", "blurb": "SpaceX/xAI's frontier-model business, called \"the sleeper\" by Brad Gerstner — Grok tripled tokens in July; Cursor was already tracking from $3B to $10B ARR; combined could reach $10-20B ARR by year-end at a much higher multiple than the compute-rental business."},
        ],
    },
    {
        "id": "spacex-financing-risk",
        "color": "amber",
        "badge": "Unresolved risk",
        "status": "WHO FINANCES THE NEXT $300B?",
        "title": "The Financing Question Nobody on the Call Answered",
        "lead": "Scaling SpaceX's compute buildout to 8 gigawatts next year could cost $300B — and it's genuinely unclear who pays for it, or whether today's compute pricing holds long enough to justify it.",
        "bullets": [
            "David Sacks's math: going from 2 to 8 gigawatts next year at ~$50B/gigawatt is ~$300B of capex — financed via debt, a dilutive equity raise, or continued Nvidia vendor financing (backstopping), none of which SpaceX or Nvidia shareholders obviously want at unlimited scale.",
            "Payback-period debate: today's ~$30-50/watt spot pricing implies roughly a 1-year payback, but as recently as a few months ago market consensus assumed a 4-5 year payback was normal — frontier labs (Anthropic, OpenAI) are currently willing to pay 3-5x \"market\" pricing for guaranteed at-scale compute because they believe they're near major breakthroughs, but nobody on the panel expects that premium pricing to persist indefinitely.",
            "Off-take concentration: essentially only Anthropic, OpenAI, and Nvidia have the capital to buy compute at this scale today — and this year Anthropic and OpenAI's combined total compute was only about 5 gigawatts, meaning Elon is proposing to add more capacity next year alone than both companies combined currently use.",
            "Bill Gurley's concern, relayed by Brad Gerstner: the AI-infrastructure ecosystem has quietly normalized \"seller financing\" / what he calls \"circular revenue\" — vendors effectively backstopping their own customers' compute purchases — which the market has gotten comfortable with but which makes the whole sector far more fragile to any single demand-slippage scare.",
            "That fragility already showed up once: July's scare over Kimi (a cheap Chinese open-source model) triggered a ~40% drawdown in CoreWeave and related semiconductor/AI-infrastructure stocks on fears that cheap open-source supply would undercut frontier-lab revenue and, by extension, compute demand. Credit spreads on AI infrastructure deals have stayed wide since.",
            "The panel's own base case is that they don't see a demand ceiling over the next 12-24 months — but Sacks explicitly flags that as \"famous last words,\" and both he and Brad acknowledge this pace \"cannot keep up\" much beyond another two years or so without some kind of correction or slowdown.",
        ],
        "quote": {"text": "I can't believe that we're all just taking in stride this level of seller financing.", "cite": "— Bill Gurley, as relayed by Brad Gerstner"},
        "watch": "This entire theme is the panel's own forward-looking risk assessment, not a resolved conclusion — multiple speakers explicitly flag their own base case (no demand slowdown for 12-24 months) as an assumption that could break, not a certainty.",
        "names": [
            {"name": "Nvidia", "blurb": "Potential financier/backstop of SpaceX's compute buildout; shareholder appetite for unlimited backstopping is an open question."},
            {"name": "CoreWeave (comparison)", "blurb": "Cited as an example of a GPU-rental business trading at a low multiple, and as the name that fell ~40% during July's Kimi-driven demand scare."},
        ],
    },
    {
        "id": "airtable-bending-spoons",
        "color": "amber",
        "badge": "Case study — not a stock pick",
        "status": "SOLD FOR ~10% OF ITS 2021 PEAK VALUATION",
        "title": "Airtable's Sale Is a Lesson in Forcing Sales-Led Growth on a PLG Company",
        "lead": "A profitable, growing, cash-rich SaaS company still sold for a fraction of its peak — the panel's diagnosis points to one specific metric, not an AI-driven collapse.",
        "bullets": [
            "Deal terms: Bending Spoons (an Italian, Milan-based serial acquirer that itself IPO'd last month) bought Airtable for $1.28B ($2.25B including Airtable's own cash), versus an $11.7B peak valuation in 2021 — Airtable had $480M revenue growing 20%/year and nearly $1B of cash. Bending Spoons shares rose 15% on the news.",
            "The panel's real diagnostic: only 30% of Airtable's sales team was hitting quota. Read as evidence the board pushed a naturally product-led-growth (PLG) company into an unnatural sales-led motion to chase faster growth than its ~20%/year organic rate — which added headcount and cost without meaningfully accelerating growth.",
            "Bending Spoons's likely playbook, per Sacks: strip 85-90% of the cost structure (explicitly compared to Elon's approach at Twitter), return to pure PLG, retain most of the ~20% organic growth, and potentially generate $300-400M of annual EBITDA — paying back the acquisition cost in as little as ~3 years. AI is framed as making this kind of \"maintenance mode\" acquisition easier than in the past, since AI tools can now learn an unfamiliar codebase quickly rather than requiring retained institutional knowledge.",
            "Why the original board/founders couldn't do this themselves: a liquidation-preference stack from investors who bought in at $2B/$5B/$11B rounds, plus psychological/structural resistance — venture-minded boards and founders aren't built for private-equity-style cost restructuring or gutting a team they built.",
            "Ecosystem framing: all late-stage investors reportedly got their money back via a standard 1x non-participating liquidation preference (no punitive or participating terms); early-stage investors made real money — panelists explicitly call this \"a pretty good failure\" for Silicon Valley, not a disaster.",
            "Root cause specific to Airtable, per the panel: it was a \"no-code\" tool (loosely, a spreadsheet for words) that never achieved the category-defining ubiquity of a real spreadsheet — unclear use cases and a real learning curve kept it a cult-favorite rather than a default tool, which made it especially exposed once coding-capable AI agents (Claude Code, Lovable, etc.) let people build custom tools directly instead.",
            "Explicit caveat from the panel: don't extrapolate this to all of SaaS. Counter-evidence cited: the IGV growth-software ETF is up 20% over the past 6 months and 20% over the past 5 years; Snowflake is up ~88-90% in 6 months (comparable to AI/semiconductor stocks); Databricks and ClickHouse are also called out as thriving. Deeply embedded, compliance-locked enterprise software (Microsoft's Active Directory/Excel/Teams/Azure FedRAMP-DoD certifications; Salesforce running all 15 of 15 US cabinet agencies, per a Benioff tweet cited live) is framed as structurally protected from this kind of disruption.",
        ],
        "quote": {"text": "Nobody buys Microsoft because Microsoft writes the best code. They buy Microsoft because Microsoft is the rail that everything else runs on.", "cite": "— quoted by David Sacks from an online post"},
        "watch": "The panel's EBITDA and payback-period projections for Bending Spoons's Airtable turnaround ($300-400M EBITDA, ~3-year payback) are their own speculative estimates during the segment, not disclosed deal terms or company guidance.",
        "names": [
            {"name": "Airtable", "blurb": "Sold for $1.28B (~10% of 2021 peak); spun out its AI-agent business, Hyperagent, as a separate company before the sale to retain venture upside separately."},
            {"name": "Bending Spoons", "blurb": "Italian serial acquirer of 'challenged but interesting' businesses — past deals include AOL's legacy business, Evernote, Eventbrite, Vimeo, and Meetup.com; recently IPO'd."},
            {"name": "Leopold Aschenbrenner (comparison)", "blurb": "His fund's losses during the correction were partly attributed to being short Adobe and other SaaS names that didn't fall as expected — cited as evidence the 'short all SaaS' trade was wrong."},
        ],
    },
    {
        "id": "china-data-export",
        "color": "amber",
        "badge": "Unresolved policy debate",
        "status": "LIVE DISAGREEMENT BETWEEN CO-HOSTS, NO CONSENSUS REACHED",
        "title": "US Data Labelers Are Selling Training Data to Chinese AI Labs — Should They?",
        "lead": "A Forbes investigation triggers a genuine, unresolved disagreement among the hosts about whether this practice meaningfully helps China catch up.",
        "bullets": [
            "Forbes investigation claims: US data-labeling startups Surge AI and Mercor (both valued over $20B) sell training datasets to OpenAI, Anthropic, and federal agencies — and, per the report, also sell the same datasets to top Chinese AI labs (Tencent, ByteDance, Alibaba, Moonshot). The top six Chinese labs reportedly spend ~$500M/year on this kind of expert-curated, PhD-written, reinforcement-learning training content.",
            "Sacks's position: data — especially generic data labeling — is largely a commodity without a clear military/\"dual use\" application; restricting its export mainly creates diplomatic friction (risking reciprocal Chinese restrictions, e.g. on rare earths) without a decisive strategic payoff, since China has ample domestic PhD talent to replicate this work. He contrasts this with the original Trump administration's 2019 EUV lithography export restrictions, which he calls an example of a control that genuinely \"packed a punch.\"",
            "Brad's position: the US is currently \"winning\" broadly (frontier labs, open source, lighter regulation, an upcoming Xi-Trump September meeting) and that's why this practice currently \"passes muster\" politically — but he warns that tolerance could reverse quickly if White House advisors ever conclude China has caught up or passed the US.",
            "Calacanis's dissenting view: after using Chinese open-weight models Kimi, Qwen (Gwen), and GLM 5.2 for the past 60 days, he's impressed by how good they've become, and calls it \"not very patriotic\" to keep selling expert-curated Western training data to Chinese labs — he believes leaked/sold Western expert data is a meaningful driver of how fast those models are improving, and approves of Micro1 (a company he's personally invested in) declining to sell to China.",
            "Sacks and Brad push back that this specific data may not be as strategically decisive as Calacanis suggests, since China graduates more STEM PhDs annually than the rest of the world combined and could plausibly reproduce similar datasets domestically — the segment ends without resolution, with Sacks acknowledging he'd need to see the actual datasets to judge whether anything here is genuinely proprietary.",
        ],
        "quote": {"text": "I don't think it's very patriotic to be giving them an advantage. I wouldn't do it.", "cite": "— Jason Calacanis"},
        "watch": "This entire segment is a live, unresolved disagreement between two co-hosts (Sacks and Calacanis) — there is no fact-checked conclusion here, only competing framings of the same Forbes report.",
        "names": [
            {"name": "Surge AI & Mercor", "blurb": "Named data-labeling companies at the center of the Forbes report, both reportedly valued over $20B."},
            {"name": "Micro1", "blurb": "Jason Calacanis-backed data company whose founder reportedly chose not to sell training data to Chinese labs."},
        ],
    },
]

TAKEAWAYS = [
    {"icon": "\U0001F4CA", "tag": "Needs independent verification", "title": "Track whether Anthropic actually hits its revised $110-120B ARR guide by year-end — the panel's whole \"duopoly premium\" thesis for frontier labs rests on that trajectory holding."},
    {"icon": "\U0001F4B0", "tag": "Analyst interpretation", "title": "Watch SpaceX's Q3 disclosures for how it finances the jump from ~2GW to 5-10GW of compute next year — debt vs. dilutive equity vs. continued Nvidia vendor financing will reveal how sustainable today's ~1-year-payback spot pricing really is."},
    {"icon": "\U0001F50D", "tag": "Analyst interpretation", "title": "If evaluating other struggling no-code/SaaS names post-Airtable, check quota attainment and PLG-vs-sales-led motion specifically — that single metric (30% quota attainment) was the panel's real diagnostic signal, not the headline valuation drop."},
    {"icon": "⚖️", "tag": "Analyst interpretation", "title": "Don't extrapolate Airtable's outcome to all of SaaS — the panel explicitly separates deeply embedded, compliance-locked enterprise software (Microsoft, Salesforce) from exposed no-code tools, citing IGV, Snowflake, and Databricks as counter-evidence."},
    {"icon": "\U0001F9EA", "tag": "Needs independent verification", "title": "Independently verify the Forbes/Surge AI/Mercor China-data-selling claims before treating them as confirmed — both Sacks and Brad question whether the underlying data is genuinely proprietary or replicable domestically in China."},
    {"icon": "\U0001F4C9", "tag": "Analyst interpretation", "title": "Watch how CoreWeave and semiconductor/AI-infrastructure stocks react to any future \"cheap open-source model\" scares (like July's Kimi selloff) as a real-time gauge of how fragile sentiment is around AI-infrastructure demand durability."},
]

RISKS = [
    "This is unscripted, live commentary from four investors (Friedberg, Gerstner, Sacks, Calacanis) who are actively invested in many of the companies and sectors discussed — Gerstner (Altimeter) discloses SaaS-era investments and SpaceX fund exposure; Calacanis discloses direct investment in Micro1 and other data-labeling startups; none of the specific figures cited are independently sourced within the episode itself, only stated verbally from memory or from public earnings calls and press reports.",
    "Several numbers are the panel's own back-of-envelope math relayed live on air (e.g. Sacks's $300B financing estimate for SpaceX's 2027 compute buildout, Freeberg's Starlink $40B-revenue/$1T-valuation extrapolation, Sacks's projected $300-400M EBITDA for Airtable post-acquisition) — treat these as informed speculation, not company guidance or independently modeled forecasts.",
    "The China-data-export segment is a live policy debate between co-hosts with visibly different views that ends unresolved — there is no consensus conclusion in the source video to report as settled fact.",
    "David Sacks has a documented AI/crypto policy background in the Trump administration, which may inform his framing of the export-control and China-competition questions in this episode.",
    "The transcript is auto-generated from a roughly 75-minute, four-person conversation with frequent interruptions, cross-talk, and colloquial phrasing; figures have been transcribed as stated but not independently re-verified against company filings or the original Forbes/Axios reporting cited in the episode.",
]

HOT_TAKES = [
    {"take": 'I think that the market for frontier intelligence has become a duopoly.',
     "cite": '— David Sacks', "why": "Writes off the rest of the field in one line; the show's whole premium thesis rests on it."},
    {"take": "I can't believe that we're all just taking in stride this level of seller financing.",
     "cite": '— Bill Gurley, as relayed by Brad Gerstner', "why": 'The vendor-financing objection to the AI capex boom, raised by someone with nothing to sell.'},
    {"take": 'Nobody buys Microsoft because Microsoft writes the best code. They buy Microsoft because Microsoft is the rail that everything else runs on.',
     "cite": '— quoted by David Sacks', "why": "Used to separate embedded enterprise software from exposed no-code tools after Airtable's collapse."},
    {"take": "I don't think it's very patriotic to be giving them an advantage. I wouldn't do it.",
     "cite": '— Jason Calacanis', "why": "On US data labelers selling training data to Chinese labs — the one point the hosts genuinely couldn't agree on."},
    {"take": 'Putting up data centers is nothing compared to the difficulty of putting up a rocket.',
     "cite": "— Elon Musk on SpaceX's earnings call, as relayed by David Sacks", "why": 'The dismissal behind pulling a $1 trillion ARR target forward a year.'},
]

OTHER_NEWS = [
    {"icon": "\U0001F3AA", "title": "The 5th annual All-In Summit was announced for September 13-15 in LA at Universal Studios, with confirmed speakers including Jensen Huang (Nvidia), Satya Nadella (Microsoft), Jared Isaacman (NASA), Bill Gurley, and Gwynne Shotwell (SpaceX) — pure event promotion, not investment content.", "tag": "Housekeeping"},
]

GLOSSARY = [
    {"term": "ARR (Annual Recurring Revenue)", "def": "A forward run-rate revenue metric used throughout to compare fast-growing AI companies (SpaceX, Anthropic) regardless of their GAAP reporting periods."},
    {"term": "ROIC (Return on Invested Capital)", "def": "Used by the panel to argue AI compute infrastructure is currently a more reliable business than frontier model development — cited via a Morgan Stanley figure of \"over 30%\" for Microsoft's token-as-a-service infrastructure."},
    {"term": "Gigawatt (as a compute unit)", "def": "The panel's shorthand for AI data-center scale; cited at roughly $50 billion of capex to build one gigawatt of compute capacity."},
    {"term": "Off-take", "def": "A customer's commitment to purchase or rent a given amount of compute capacity from a builder like SpaceX — the panel's key open question is whether enough customers with sufficient capital exist to \"off-take\" the compute Elon plans to build."},
    {"term": "1x non-participating liquidation preference", "def": "The standard investor-protection term described in the Airtable deal — investors get their original money back before common shareholders participate in a sale, with no \"double dip\" on top."},
    {"term": "PLG (Product-Led Growth)", "def": "Organic, self-serve customer growth driven by the product itself, contrasted in this episode with the \"sales-led\" motion Airtable's board reportedly pushed the company into, which underperformed (only 30% sales-quota attainment)."},
    {"term": "IGV", "def": "An ETF tracking high-growth software companies, cited by the panel as evidence that not all of SaaS is struggling despite the Airtable story."},
    {"term": "Circular revenue / seller financing", "def": "Bill Gurley's term (relayed by Brad Gerstner) for AI infrastructure vendors effectively financing their own customers' purchases of their compute — a structural risk flagged as under-scrutinized by the market."},
]
