"""
Per-video data for youtube-research-brief. Copy this file, fill in every field, then:

    python3 <skill-folder>/generate.py <this-file>

See SKILL.md Section 3 (coverage/inventory) and Section 4 (themes, incl. category-conditional
color/badge/names rules) for what belongs where and the rules for each field (dedup, labeling,
bullet counts, etc.) — this file only has the shape.
"""

META = {
    "title": "New Rules for Founders",
    "channel": "a16z",
    "speakers": "Garry Tan (President & CEO, Y Combinator), interviewed by Erik Torenberg",
    "date": "2026-08-12",
    "video_url": "https://www.youtube.com/watch?v=fsTtKywmWlU",
    "thread_line": "6 threads · founder psychology, agentic-org building, YC's access model, SaaS's expiring moat, the AI-timeline white pill, and Tan's local-politics organizing",
    "category": "dev",
}

SNAPSHOT = [
    "Tan frames his own career as a **cautionary tale of chasing 'hot'** instead of what he actually knew: he left web programming for Windows Mobile right before Web 2.0, then turned down early Palantir to stay at Microsoft for a promotion.",
    "Central thesis: **'a markdown file is an employee'** — founders should turn any repeatable business process into a skill file (markdown + code + tests) that an agent runs perfectly and forever, applied to sales, marketing, support, and engineering alike.",
    "Says token-maxing agents (Open Claw/Hermes Agent style, ~800k-1M tokens per request) costs **$50,000-$100,000 a year** but effectively lets a founder \"live in 2028\" today.",
    "Claims YC has seen companies go from **zero to $15M ARR in about four months** with two or three people and hundreds of agent skill files.",
    "Calls pure per-seat SaaS a shrinking category — in 2026 it needs a real moat (data, network effects) beyond the old 10-20x revenue-multiple logic, or it's just a wedge.",
    "His 'white pill': the actual bottleneck on AI-driven disruption is **humans and bureaucracy, not model intelligence** — expects the transition to take ~20 years, with a 'harness wars' phase around 2027 once compute gets cheap enough for consumer scale.",
    "Describes his own organizing in San Francisco politics — recall campaigns, a DA and school board he says failed Asian American residents — as the human-coordination-bound counterpart to intelligence-bound AI problems.",
    "Credits Y Combinator's founders (Paul Graham, Jessica Livingston, Trevor Blackwell, Robert Morris) with replacing Silicon Valley's old insider social network with a 12-question form, calling it a great equalizer ('birthright but for tech').",
]

THEMES = [
    {
        "id": "founder-psychology",
        "color": "gray",
        "badge": "Personal reflection",
        "status": "CAREER RETROSPECTIVE",
        "title": "Chasing 'hot' cost Tan a shot at both Facebook-era web and Palantir",
        "lead": "Tan's two biggest career regrets both came from following what looked smart instead of what he already knew.",
        "bullets": [
            "In 2003, post-dot-com-crash, he left web programming for a Windows Mobile job at Microsoft right before Web 2.0 and social software took off — **\"I was getting out of web programming at exactly the wrong time.\"**",
            "His fraternity brothers Joe Lonsdale and Stephen Cohen, then interning at Peter Thiel's hedge fund, tried recruiting him to what became Palantir; Thiel personally offered him $70,000 to join.",
            "Tan turned it down to stay at Microsoft for a promotion to *level 60* — he now calls it **\"a $2 billion to $4 billion mistake at this point.\"**",
            "His framing for both mistakes: he was \"working backwards from the map instead of looking down at the territory\" — following perceived status/hotness rather than direct experience.",
            "Coined a \"don't LARP\" meme at Startup School: be earnest about what you actually know rather than chasing consensus opinion on what's hot.",
            "On whether agency is innate — pushing back on a claim he attributes to Nikita that the same 20% of people who dominated film and software will keep dominating now that anyone can make either — Tan calls himself \"a late bloomer\" and argues agency is built through practice, not born in.",
        ],
        "quote": {"text": "Courage is actually I think the right thing... if someone contradicts you, you say well, I don't agree with that because I believe my own direct experience.", "cite": "— Garry Tan"},
        "watch": "These are Tan's own retrospective dollar estimates on a hypothetical alternate career path, not an audited figure.",
        "names": [
            {"name": "Y Combinator", "blurb": "Tan is President & CEO; accelerator whose founders and 16 equal partners he credits with democratizing Silicon Valley access."},
            {"name": "Palantir", "blurb": "Company Tan nearly joined via Thiel/Lonsdale/Cohen in the early 2000s, later cofounded by Alex Karp; he cites it as where he learned 'everything awesome in my life is kind of a cult.'"},
            {"name": "Microsoft", "blurb": "Where Tan worked on Windows Mobile starting 2003; also his recurring example of bureaucratic dysfunction (the 'baseball bat' story)."},
        ],
    },
    {
        "id": "markdown-employee",
        "color": "amber",
        "badge": "Structural thesis",
        "status": "CORE ARGUMENT OF THE INTERVIEW",
        "title": "\"A markdown file is an employee\" — Tan's model for the agentic company",
        "lead": "Tan's advice to founders: do any repeatable business process once by hand, then turn the trace into a skill file an agent runs perfectly forever.",
        "bullets": [
            "Method: perform a task with a token-maxed agent (Open Claw / Hermes Agent, loading up to ~800k-1M tokens of context into a 'soul.md'), then convert the successful trace into markdown + code + tests — a reusable skill file.",
            "Cost of running agents 'at full strength' (his \"150 IQ on every request\") is roughly **$50,000-$100,000 a year**, which he argues is worth it for a CEO/founder because it effectively means \"you get to live in 2028\" today.",
            "Says he built **Garyslist.org**, an agentic newsroom, this way — used Open Claw to extract a RAG/graph-generation pipeline out of it that ended up outperforming Memory Palace and other open-source alternatives.",
            "The loop generalizes past engineering: he expects it applied to sales, marketing, customer support — anywhere a process can be captured, iterated on, and turned into a permanent skill/cron job.",
            "Cites Brex's Pedro as the most aggressive practitioner: built an open-source layer (network-traffic watcher for Open Claw) so agents can safely review meeting transcripts across the org and surface which teams are in conflict before Pedro walks into the room.",
            "Names provenance and conflict-management as the next hard problem once an org accumulates many markdown files/skills — needs a scheduled process resolving which of two conflicting facts is current.",
            "Cites YC-funded **Kolabtree** as an early example of the same idea applied externally: it shipped a bug-report API endpoint built for agents (not humans) to file against, which replies in real time with a fix timeline and a workaround.",
            "Says his own G Stack/G Brain tools started as messing around after Claude Code creator Boris Cherny appeared on the Light Cone podcast — Tan then mined months of recorded YC office-hours data to distill a script of the rhetorical devices partners use to raise founder ambition.",
        ],
        "quote": {"text": "A markdown file is an employee. And it's an employee that will do the job perfectly every single time, and it will do it as many times as you want.", "cite": "— Garry Tan"},
        "watch": None,
        "names": [
            {"name": "Brex", "blurb": "Fintech where an executive (Pedro) built an open-source agent layer to monitor Open Claw activity and mine meeting transcripts for organizational conflict."},
            {"name": "Kolabtree", "blurb": "YC-funded company Tan cites for shipping a bug-report API endpoint designed for AI agents, not humans, to file against."},
        ],
    },
    {
        "id": "saas-not-precious",
        "color": "amber",
        "badge": "Contested",
        "status": "MARKET-STRUCTURE SHIFT, PER TAN",
        "title": "Code stopped being precious — and so did the SaaS multiple",
        "lead": "Tan says the old per-seat SaaS playbook is no longer a safe default the way it was even two years ago.",
        "bullets": [
            "\"A pure per-seat SaaS thing... not totally clear it will exist in another 5 or 10 years\" if launched in 2026 — fine as a wedge, but needs a real moat (data or network effects) behind it.",
            "Two years ago, he says, the 10-20x next-12-months revenue multiple was treated as \"an iron law\" for SaaS; he now calls that no longer true at all.",
            "Cheap agentic coding means code is \"no longer precious\" — QA, PM specs, and staffing overhead that used to gate shipping are increasingly compressed into agent workflows ('slash QA... it's done').",
            "He connects this to why few people show their agentic coding work publicly: much of it is low-stakes, exploratory 'Zen rock garden' tinkering rather than a finished, defensible product.",
        ],
        "quote": None,
        "watch": "Tan is a VC funding this shift, not a neutral observer of SaaS valuations — this is his working thesis stated in conversation, not a market data claim.",
        "names": None,
    },
    {
        "id": "yc-access-model",
        "color": "green",
        "badge": "Structural critique",
        "status": "CONFIRMED — YC'S OWN STATED MODEL",
        "title": "YC replaced Silicon Valley's insider social network with a form",
        "lead": "Tan credits Paul Graham and Jessica Livingston's original model — a website, 12 questions, later a one-minute video — with removing the old social gatekeeping ('scenesters') from startup access.",
        "bullets": [
            "YC now runs on 16 equal partners, all YC alumni with successful outcomes themselves, evaluating founders on ideas and execution rather than pedigree or network.",
            "Startup School drew **7,000 attendees** this year, most in San Francisco for the first time and mostly 18-22 years old — Tan calls it \"birthright but for tech.\"",
            "He frames YC's other core value as community: founders get a peer group they can be candid with about failure, unlike the guarded status-signaling at a typical industry event.",
            "Ties this to a broader claim about internet-native generations finding their tribe (Reddit, X/Insta niches) much earlier than his own '80s grade-school generation did.",
        ],
        "quote": {"text": "It sort of doesn't matter where you're from or who you are. It just actually matters what your ideas are and can you execute.", "cite": "— Garry Tan"},
        "watch": None,
        "names": None,
    },
    {
        "id": "white-pill-timeline",
        "color": "amber",
        "badge": "Contrarian framing",
        "status": "TAN'S OWN TIMELINE CALL",
        "title": "The white pill: humans and bureaucracy — not model intelligence — are the bottleneck",
        "lead": "Tan argues AI-driven disruption of institutions will take roughly two decades because human coordination limits (the 'seven plus or minus two' working-memory constraint), not model capability, are the real constraint.",
        "bullets": [
            "His read against the doom-and-gloom discourse: \"all of the bureaucracy and the slowness... of every company, every institution... that is actually the white pill\" — it buys society time to adapt.",
            "Predicts 2027 will be the **\"harness wars\"** — a consumer-scale fight over AI agent interfaces — once frontier-level compute drops to roughly $50-100 within two to three years, at which point \"the browser wars will be back on.\"",
            "Says the next computer is likely voice-first with persistent memory, evoking a Richard Brautigan-style \"machines of living grace\" that track a user's context, hopes, and fears over time.",
            "Argues an org like Microsoft structurally can't restructure around agentic middle-management the way a startup can — \"an org like Microsoft can't. But a startup can. And every startup must.\"",
            "Frames a 35-45-year-old founder ('perfect example: Peter Steinberger') who's 'been around the block' as newly advantaged: multiplied by agents, one experienced person can now outperform an entire department at a large tech company.",
        ],
        "quote": {"text": "It's going to be 20 years and that's not a bad thing. That's actually a good thing... society is way slower than you think.", "cite": "— Garry Tan"},
        "watch": "This is Tan's personal forecast stated in conversation, not a modeled prediction — no methodology or data behind the 2027/20-year figures.",
        "names": None,
    },
    {
        "id": "sf-local-politics",
        "color": "amber",
        "badge": "Personal advocacy",
        "status": "ONGOING — TAN'S OWN CIVIC ORGANIZING",
        "title": "Tan's other project: organizing San Francisco politics around 'act local'",
        "lead": "Tan treats his San Francisco political organizing as the human-coordination-bound counterpart to AI's intelligence-bound problems, and says it started from a personal grievance.",
        "bullets": [
            "Says a San Francisco district attorney and school board around COVID were, in his view, hostile to Asian American residents and students — citing a school board fight over algebra access in public middle school that he says would have blocked his own path to Stanford engineering.",
            "Cites Asian Americans as roughly 25% of San Francisco's voting population and describes local mainstream TV news (he names ABC News) as declining to cover anti-Asian crime during that period.",
            "Frames his response as personal-risk civic organizing, quoting Mario Savio's 'put your body on it' line, and says the resulting political shift (crediting Mayor Lurie's popularity) shows measurable improvement.",
            "Points to a recent jury-duty stint in San Francisco as a separate, smaller white-pill moment — an orderly cross-section of the city and, in his view, evidence that government isn't there to 'ruin people.'",
            "His stated broader goal is exporting the same organizing playbook to other cities via **Garyslist.org** — naming LA, New York, Minneapolis, and Seattle — and encouraging technologists to 'act local' on housing, crime, and treatment/recovery rather than focusing on national politics.",
            "Extends the same logic internationally: discussing a recent London trip, argues local ambition doesn't require an American blueprint — e.g. using the technology to make the NHS itself dramatically better rather than importing a US-style approach.",
        ],
        "quote": {"text": "When the system becomes so odious you've got to put your body on it... they can't do this to us and we're going to stop it.", "cite": "— Garry Tan"},
        "watch": "This is Tan's own account and framing of a contested local political period — the DA, school board, and media characterizations are his stated views, not independently verified in this conversation.",
        "names": None,
    },
]

TAKEAWAYS = [
    {"icon": "\U0001F4DD", "tag": "Careers", "title": "Follow your direct experience over what's 'hot' — Tan's two biggest regrets both came from chasing consensus status instead."},
    {"icon": "\U0001F916", "tag": "AI workflows", "title": "Turn any repeatable task into a skill file (markdown + code + tests) once it's been done well by hand — that's the reusable unit, not a one-off script."},
    {"icon": "\U0001F4B0", "tag": "Business models", "title": "Don't build a bare per-seat SaaS product in 2026 without a data or network-effect moat behind it — the old revenue-multiple safety net is gone."},
    {"icon": "\U0001F3E2", "tag": "Org design", "title": "Push mid-level coordination (conflict resolution, status-tracking) to agents; keep humans on setting direction and execution, not managing the seven-plus-or-minus-two bottleneck."},
    {"icon": "\U0001F30D", "tag": "Civic engagement", "title": "Act local first — Tan argues state and national politics fix themselves once local government (housing, crime, schools) is functional."},
    {"icon": "⏳", "tag": "AI timeline", "title": "Plan on a ~20-year institutional adoption curve, not overnight disruption — bureaucracy is the brake, and that's time to adapt, not a reason to panic."},
]

RISKS = [
    "This is a single-guest interview — every figure (the '$2-4B mistake,' the '$50-100k/year' agent cost, 'zero to $15M ARR in four months') is Tan's own self-reported estimate, offered in conversation rather than backed by a report or audit.",
    "Tan runs Y Combinator and is a direct beneficiary of the founder/agentic-tooling narrative he's describing — his SaaS-is-dying and 'harness wars' calls are stated as personal conviction, not disclosed as neutral market analysis.",
    "The San Francisco politics section presents one side of a contested local political period (a named DA, a school board, and named media outlet) — it's Tan's own advocacy framing, not independently verified in this conversation.",
    "Auto-generated captions likely mangled some names/tools in the agentic-tooling section (e.g., a Brex tool referenced as 'Craptrack') — treat unfamiliar proper nouns in that stretch as approximate.",
]

HOT_TAKES = [
    {"take": "It was like a $2 billion to $4 billion mistake at this point.", "cite": "— Garry Tan", "why": "On turning down Peter Thiel's $70K offer to join what became Palantir, in favor of a Microsoft promotion — a specific, falsifiable-feeling number he's on the hook for."},
    {"take": "A pure per-seat SaaS thing... not totally clear it will exist in another 5 or 10 years.", "cite": "— Garry Tan", "why": "A dated, contrarian dismissal of the dominant startup business model of the last 15 years."},
    {"take": "An org like Microsoft can't. But a startup can. And every startup must.", "cite": "— Garry Tan", "why": "A blunt structural claim that large incumbents are permanently disadvantaged against agentic-native startups."},
    {"take": "It's going to be 20 years and that's not a bad thing... society is way slower than you think.", "cite": "— Garry Tan", "why": "A specific, contrarian timeline against the AI-doom consensus, offered as reassurance rather than caution."},
    {"take": "A markdown file is an employee.", "cite": "— Garry Tan", "why": "The interview's central, quotable structural claim about how agentic companies should be built."},
]

OTHER_NEWS = [
    {"icon": "\U0001F4E1", "title": "Sources referenced this episode: Chris Dixon's 'idea maze' framing, Derek Sivers' first-follower TED Talk, Venkatesh Rao's 'API line' concept, and a Mario Savio quote from the 1964 Free Speech Movement.", "tag": "Cited sources"},
    {"icon": "\U0001F5E3", "title": "Tan also flags a new ChatGPT desktop voice mode as the closest thing yet to a true consumer AI concierge, saying it can see all of a user's threads across devices.", "tag": "Product note"},
]

GLOSSARY = [
    {"term": "Don't LARP", "def": "Tan's Startup School meme urging founders to be earnest about what they actually know rather than performing what's currently fashionable."},
    {"term": "Token-maxing", "def": "Loading an agent with the maximum context (hundreds of thousands to ~1M tokens) per request to get the highest-quality output, at high per-request cost."},
    {"term": "Skill file", "def": "A markdown file plus supporting code/tests that captures a business process an agent can execute repeatably and perfectly once refined."},
    {"term": "Harness wars", "def": "Tan's predicted 2027 competitive phase for AI agent interfaces/harnesses once compute costs drop enough for consumer-scale usage."},
    {"term": "API line", "def": "Venkatesh Rao's concept describing whether a worker (e.g., an Uber driver) operates above or below an app's control logic; Tan argues AI erodes this line by letting agents negotiate back with software."},
]
