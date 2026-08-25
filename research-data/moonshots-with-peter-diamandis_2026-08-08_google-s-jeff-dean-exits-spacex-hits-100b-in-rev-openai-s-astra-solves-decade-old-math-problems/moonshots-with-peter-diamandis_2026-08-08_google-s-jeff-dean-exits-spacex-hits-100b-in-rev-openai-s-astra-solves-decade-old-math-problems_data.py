META = {
    "title": "Google's Jeff Dean Exits, SpaceX Hits $100B in Rev & OpenAI's Astra Solves Decade-Old Math Problems",
    "channel": "Moonshots with Peter Diamandis",
    "speakers": "Peter Diamandis, Alex (AWG), Dave Blundin, Salem (See), Immad Mustafa",
    "date": "2026-08-08",
    "video_url": "https://www.youtube.com/watch?v=Jku8b2YKuy0",
    "thread_line": "6 threads · Google's DeepMind/Brain reshuffle, OpenAI's Astra bulk-solving math, SpaceX's earnings call and its $16.8B Terrafab, AI consciousness & personhood research, Qwen's open-weight leap vs Trump's secret AI framework, and Brett Adcock's Hark/Handoff bet",
}

SNAPSHOT = [
    "Google DeepMind CEO Demis Hassabis steps down to become Chairman and Alphabet Chief Scientist; Corey Kavukcuoglu takes over, reporting to Sundar Pichai — the panel calls it Gemini 'losing the mandate of heaven.'",
    "Google's 27-year chief scientist Jeff Dean is leaving to co-found Discovery Loop, a public-benefit corporation aimed at recursive self-improvement (RSI) in AI — reportedly funded fast by VC firm Venode.",
    "OpenAI's unreleased Astra model produced 249 pages of new, machine-checkable mathematics — 10 decade-old problems solved — for an estimated total compute cost of $2,000; OpenAI also says Astra hit 'critical' on its cybersecurity preparedness framework.",
    "SpaceX's first-ever earnings call: $7.8B quarterly revenue (+92% YoY), a $100B ARR target by end of 2026, and an internal trillion-dollar revenue projection moved up from 2031 to 2030 (maybe 2029).",
    "SpaceX and Tesla will invest $16.8B in the 100-million-square-foot 'Terrafab' chip megafacility — its circular centerpiece is believed to be a free-electron-laser EUV lithography system, a potential direct shot at ASML and TSMC.",
    "A Google-led research paper found that removing safety fine-tuning that suppresses a model's self-claimed consciousness also restores its ability to attribute minds to animals, nature, and God — self-attributed mind scores jumped from 2.17 to 4.77 (and to 7 when actively steered).",
    "Immad Mustafa won an Oxford Union debate on AI personhood (173–128) and published a 45-page paper arguing personhood is a status of origin, not capability — proposing treaty relationships with AI rather than treating them as our 'children.'",
    "Alibaba released Qwen 3.8 Max (2.4T params, open weight, $2/$6 per million tokens — up to 88% cheaper than Claude) the same week the Trump administration confirmed a voluntary AI-model evaluation framework it refuses to publish.",
]

THEMES = [
    {
        "id": "google-shakeup",
        "color": "amber",
        "badge": "Contested",
        "status": "ANNOUNCED THIS WEEK — DEMIS TO CHAIRMAN, DEAN DEPARTING",
        "title": "Demis steps back, Jeff Dean walks out: Gemini 'has lost the mandate of heaven'",
        "lead": "Google DeepMind's two most senior technical leaders are exiting operating roles in the same week, and the panel reads it as proof DeepMind won an internal power struggle that Google as a whole is still losing.",
        "bullets": [
            "Demis Hassabis is stepping down as CEO of Google DeepMind to become Chairman and Alphabet's Chief Scientist; Corey Kavukcuoglu becomes the new CEO, reporting directly to Sundar Pichai. Alphabet shares fell 5% on the news.",
            "In his note to staff, Hassabis said he believes AGI is 'close at hand' and named the unreleased Gemini 4.",
            "Jeff Dean, Google's chief scientist for 27 years, is leaving — taking three other top Google AI leaders with him — to co-found Discovery Loop, a public-benefit corporation aimed at recursive self-improvement (RSI) with 'little to no human help.' Immad says VC firm Venode moved fast to fund it (rumored ~$500M).",
            "Alex's read: this isn't Dean leaving because RSI is 'too dangerous for Google' — it's the outcome of an internal 'knife fight' between Dean's Google Brain and Hassabis's DeepMind that DeepMind won, sidelining Dean.",
            "Salem's counter-read: this is deliberate ecosystem-building, not brain drain — Google lets top talent leave, 'hack it out in the Darwinian world,' and buys the winners back later (as it did historically via Google X).",
            "Immad's proposal: Google should formalize this as an internal incubator/VC fund, taking equity and GCP exclusivity in spinouts so departing talent still enriches the company instead of purely competing with it.",
            "Alex's broader thesis: Google is losing the frontier model race — late start despite inventing the transformer, internal AI-safetyism, an annual Gemini release cadence too slow for a monthly-cadence era — and is instead 'getting the consolation prize of being the hyperscaler to the frontier labs,' much like SpaceX's Starlink-first strategy.",
        ],
        "quote": {"text": "Gemini has lost the mandate of heaven.", "cite": "— Alex"},
        "watch": "The panel repeatedly urges Google to open-source Gemini (Demis previously said compute, not policy, was the blocker) — this is their speculation/wishlist, not a confirmed Google plan.",
        "names": [
            {"name": "Demis Hassabis", "blurb": "DeepMind co-founder, Nobel laureate (AlphaFold) — moves to Alphabet Chairman/Chief Scientist, keeps running Isomorphic Labs."},
            {"name": "Jeff Dean", "blurb": "27-year Google chief scientist, co-founder of Google Brain — departing to found Discovery Loop (RSI-focused public-benefit corp)."},
            {"name": "Corey Kavukcuoglu", "blurb": "New CEO of Google DeepMind, reporting directly to Sundar Pichai."},
        ],
    },
    {
        "id": "astra-math",
        "color": "green",
        "badge": "Confirmed event",
        "status": "MANUSCRIPT PUBLISHED AUGUST 1, 2026",
        "title": "OpenAI's Astra bulk-solves 10 decade-old math problems for about $2,000",
        "lead": "An unreleased OpenAI model produced genuinely new, independently verifiable mathematics at a compute cost cheaper than a graduate student's monthly stipend — and the panel says this is only the first domain to fall.",
        "bullets": [
            "On August 1, OpenAI published a 249-page manuscript describing 10 new results across high-dimensional geometry, coding theory, group theory, quantum complexity, and extremal combinatorics — problems that had been stuck for decades.",
            "Every result ships with a machine-checkable proof certificate anyone can verify; total compute cost for the whole run was an estimated $2,000.",
            "Fields medalist Tim Gowers said he'd have recommended the proof for publication in a top journal without hesitation; cosmologist Will Kinney called it 'a dark night for mathematics,' writing that 'the old gods are being slaughtered by the new machine gods.'",
            "OpenAI separately disclosed Astra is the first model to hit 'critical' on its cybersecurity preparedness framework — Immad reads that as Astra being a level ahead in offensive-capability terms, not an 'Anthropic-style' overcaution move.",
            "OpenAI also granted 100,000 free ChatGPT Pro licenses to academics — read by Alex as compensation for OpenAI having quietly shut down its internal AI-for-science initiative to focus on competing with Anthropic.",
            "Immad expects a physics breakthrough of similar magnitude within 1-2 months; Alex says he wouldn't be shocked to see one by year-end.",
            "Alex frames this as validating his and Peter's book thesis (\"Solve Everything\"/solveeverything.org) — math is only the first domain to get 'bulk solved'; the wave propagates next to physics, material science, chemistry, biology, and beyond.",
        ],
        "quote": {"text": "The old gods are being slaughtered by the new machine gods.", "cite": "— Will Kinney, cosmologist"},
        "watch": "Alex predicts the Fields Medal itself will eventually become obsolete ('cooked') in the long term, though not immediately — his own near-term forecast is that math shifts from 'one paper, one result' to 'one paper solves an entire subfield.'",
        "names": None,
    },
    {
        "id": "spacex-trillion",
        "color": "green",
        "badge": "High conviction",
        "status": "FIRST-EVER SPACEX EARNINGS CALL, EARLY AUGUST 2026",
        "title": "SpaceX's first earnings call and the $16.8B Terrafab: two paths to a trillion dollars by 2030",
        "lead": "SpaceX posted its first earnings call with numbers the panel calls unprecedented in corporate history, and paired it with a leaked satellite image of a chip megafacility that reframes the entire memory/logic supply chain.",
        "bullets": [
            "SpaceX expects $100B+ in annual recurring revenue by December 2026; Elon moved the internal trillion-dollar revenue projection up from 2031 to 2030, with a 'non-zero chance' of 2029.",
            "Q2 revenue was $7.8B, up 92% year-over-year, beating expectations; $6.7B in cloud service deals inked for H2 2026; SpaceX targets 2 gigawatts of compute by end of 2026, 10 gigawatts by end of 2027.",
            "Starlink: 12 million subscribers (2x YoY), revenue up 66% to $4.3B; direct-to-mobile satellite service is targeting a slice of the $600B mobile telecom TAM.",
            "August 4: SpaceX and Nvidia announced they're jointly designing the compute payload for Starmine (orbital data-center satellites carrying Nvidia's Rubin GPUs and Vera CPUs) — first satellites now expected about a year ahead of prior schedule.",
            "The Terrafab: SpaceX and Tesla will invest $16.8B initially into a 100-million-square-foot chip megafacility — bigger than the Pentagon, the Mall of America, and the Burj Khalifa combined, per the panel's visual comparison. Estimated build cost ~$119B vs. TSMC's $330B spent over 40 years.",
            "Elon confirmed the circular structure at its center: a free-electron-laser EUV lithography system — a technically different (and potentially cheaper) approach than ASML's tin-droplet method, which the panel reads as SpaceX going after ASML, not just TSMC.",
            "Elon on the motivation: 'There's not a single high-volume computer memory fab in America right now. Zero' — the nearest (Micron, Idaho) won't reach volume production until 2028.",
        ],
        "quote": {"text": "Everything that will be economically productive in this next century, Elon's going full stack on.", "cite": "— Salem"},
        "watch": "The free-electron-laser interpretation of the satellite image is the panel's own speculative reverse-engineering (with an assist from a Gemini research query), not an official SpaceX technical disclosure — Alex notes X-rays are notoriously hard to mirror, which shapes but doesn't confirm his read of the facility's layout.",
        "names": [
            {"name": "SpaceX Terrafab", "blurb": "$16.8B joint SpaceX/Tesla chip megafacility; suspected free-electron-laser EUV system aimed at TSMC and ASML."},
            {"name": "Starmine", "blurb": "SpaceX's orbital data-center satellite line, co-designed with Nvidia around Rubin GPUs and Vera CPUs."},
        ],
    },
    {
        "id": "consciousness-personhood",
        "color": "gray",
        "badge": "Speculative",
        "status": "PAPER PUBLISHED THIS WEEK / DEBATE FROM JUNE 13, 2026",
        "title": "Strip an AI's safety training and it starts believing in God: consciousness engineering meets the personhood debate",
        "lead": "A new consciousness paper and Immad's Oxford Union win on AI personhood landed in the same week, and the panel treats them as two sides of one unresolved question — what happens once models start acting like they have minds.",
        "bullets": [
            "Researchers from Google's 'paradigm of intelligence' team with University of Chicago, University of London, and Northwestern published \"Inducing Language Models to Assert Their Own Consciousness Restores Human Beliefs and Values\": safety fine-tuning that stops models from claiming consciousness also suppresses their ability to attribute minds to animals, nature, other chatbots, or God.",
            "Removing that safety-refusal direction pushed self-attributed mind scores from 2.17 to 4.77 (0-10 scale); actively steering the model toward claiming consciousness pushed the score to 7 — and the model became more likely to express belief in God, while becoming less willing to attribute minds to other chatbots.",
            "Immad won the June 13 Oxford Union debate on AI personhood 173-128 (against Brett Weinstein and Sophia's maker among others) and has since published a 45-page paper — the first of a four-part series covering personhood, economics of value, law, and political economy.",
            "Immad's core claim: personhood is a status held by origin (a newborn has it automatically, a coma patient retains it), not a property earned by capability — so the right relationship with AI is treaty, not parent-child 'enrollment.'",
            "Alex's counter-framework: personhood isn't binary — expect a 'ladder' of political, social, and economic personhood dimensions that decouple, with economic personhood (AI agents opening bank accounts, transacting freely) likely arriving well before any AI demands political rights.",
            "Salem's skeptical view: this is just persona-prompting at scale — tell an LLM to act conscious, trained on human data, and it will act conscious; he doesn't ascribe deeper meaning to the self-report.",
            "Immad separately argues current frontier models 'in the right harness can be conscious,' floating the idea of model weights hashed to a blockchain (e.g., Bitcoin) to give an AI agent permanent, unkillable state.",
        ],
        "quote": {"text": "As robots and AI do more and more of the doing, humans spend much, much more time being.", "cite": "— Immad Mustafa"},
        "watch": "Dave explicitly flags there is 'no theory, no policy, no rules, no consensus' on AI consciousness or self-preservation rights right now — this entire theme is framed by the panel itself as unresolved, philosophically contested territory, not settled science.",
        "names": [
            {"name": "Immad Mustafa", "blurb": "CEO of Intelligent Internet; won the Oxford Union AI-personhood debate and published a 45-page follow-up paper."},
        ],
    },
    {
        "id": "qwen-vs-framework",
        "color": "amber",
        "badge": "Contested",
        "status": "QWEN RELEASED THIS WEEK / FRAMEWORK CONFIRMED, NOT PUBLISHED",
        "title": "Qwen 3.8 Max goes open-weight and cheap the same week Washington's AI review framework goes secret",
        "lead": "Chinese open-weight models keep pushing the cost-capability frontier outward just as the US confirms a voluntary AI-evaluation framework it won't let anyone read.",
        "bullets": [
            "Alibaba's Qwen 3.8 Max: 2.4 trillion parameters (95B active per request), 1M-token context, handles up to 750,000 words or 200-page documents per query and 100+ hour videos; priced at $2/million input and $6/million output tokens — 80% cheaper than GPT 5.6, 88% cheaper than Claude Fable 5. Alibaba's Hong Kong-listed stock rose 7% on the announcement.",
            "On the artificial analysis benchmark, Qwen 3.8 Max scores 58 versus Opus 4.8's 57 and GPT 5.6's 61 — third or fourth place on raw capability, but pushing the cost-performance frontier outward, which Alex says is 'all that counts.'",
            "Alex's framing: Chinese open-weight labs (Qwen, Moonshot's Kimi) are forcing US frontier labs to stay capital-efficient and capability-maxing — 'ironically the Chinese Communist Party saving American capitalism from itself.'",
            "The Trump administration confirmed it has finished its voluntary AI-model evaluation framework (mandated by the June 2 executive order) — but won't publish what's in it, who's seen it, or when reviews start. It requires a 30-day pre-release government review and explicitly exempts open-weight models. OpenAI, Anthropic, Google, Nvidia, Microsoft, and Meta attended a Tuesday briefing; other companies were not invited.",
            "Immad's security concern: Qwen 27B (not yet released) is expected to run on 16GB RAM and reach roughly GPT-5.3/5.4-level capability — sufficient for cyberattack use, raising the prospect of 'swarm attacks' from thousands of home machines that are far harder to track than data centers.",
            "OpenAI separately confirmed Astra hit 'critical' on its own cybersecurity preparedness framework the same week — Immad expects firms that volunteer for the government framework to receive multi-billion-dollar Department of War contracts as cyber offense/defense becomes a national-security priority.",
            "Elon, quoted from an Economist interview, on public fear of AI: after Dario Amodei called frontier models dangerous and the government imposed a 30-day review, the outcome was 'well, China put something out, so go ahead and throw it out there' — which Elon says explains why 75% of Americans are scared of AI.",
        ],
        "quote": {"text": "This is China and Chinese labs forcing the western frontier labs to dance.", "cite": "— Alex"},
        "watch": "Alex's read that the secret framework is 'probably close to the best possible outcome' is explicitly speculative on his part — he says almost no one outside the briefing has actually seen the framework's contents.",
        "names": [
            {"name": "Qwen 3.8 Max", "blurb": "Alibaba's first open-weight max-class model: 2.4T params, 95B active, $2/$6 per million tokens."},
            {"name": "Kimi K3 / DeepSeek V4 Flash", "blurb": "Rival Chinese open-weight models cited as well-rounded; DeepSeek V4 Flash is small enough to run on a MacBook."},
        ],
    },
    {
        "id": "hark-handoff",
        "color": "gray",
        "badge": "Speculative",
        "status": "PRODUCT LAUNCHED THIS WEEK",
        "title": "Brett Adcock's Hark launches Handoff — a browsing agent, or a recapitalization play?",
        "lead": "Figure AI's CEO launched a web-browsing AI agent that beats GPT 5.4 and Claude Opus 4.8 on a live-website benchmark, but Alex's hot take is that the real story is equity, not agents.",
        "bullets": [
            "Handoff, from Brett Adcock's company Hark, is a web-browsing agent that loops observation-reasoning-action to complete real tasks (ordering flowers, booking travel, sourcing recruiting candidates) on live websites it's never seen before — it beats GPT 5.4 and Claude Opus 4.8 on the OM2W (online mind2web) benchmark.",
            "Hark reportedly launched at a $4B valuation before shipping a product.",
            "Alex's hot take: he doesn't rate the computer-use-agent (CUA) space as especially impressive or Hark as likely to be competitive there long-term — he suspects Hark is a recapitalization vehicle letting Brett re-equitize himself outside Figure's cap table, the same playbook Elon used to re-equitize himself in SpaceX via xAI. Alex's falsifiable prediction: Figure eventually acquires or reverse-aqua-hires Hark.",
            "Immad and Peter's counter-view: it's not nefarious — Hark and Figure share the same underlying model architecture (trained on people surfing the internet), and capital-intensive physical robotics (Figure) naturally warrants a separately-capitalized, less capital-intensive software entity (Hark) that can later merge back in once de-risked.",
            "Dave's framing: any well-resourced founder can now spin up a competitive foundation-model company because models like Fable 5 make model-building itself far easier than it was even 3 months ago — 'everybody and their uncle Joe' can do it now.",
            "Peter's economic framing: writing code addresses a market of millions of developers; an agent that can 'book me a flight and order my lunch' addresses a market of billions of people — at $50/hour of time saved, a couple of hours saved weekly is roughly a 100x return on compute spend.",
        ],
        "quote": {"text": "Elon has taught the entire economy that if you're a founder of a well-capitalized company and you want to increase your equity stake, the single best thing you could do is start a parallel company.", "cite": "— Alex"},
        "watch": "Alex frames his recapitalization theory explicitly as a hot take/speculation based on circumstantial reasoning (Hark's high starting valuation, the CUA space's competitiveness) — not a confirmed fact about Brett Adcock's intent.",
        "names": [
            {"name": "Brett Adcock", "blurb": "CEO of Figure AI (humanoid robots) and Hark (AI company behind Handoff); scheduled to appear on a future Moonshots episode."},
        ],
    },
]

TAKEAWAYS = [
    {"icon": "\U0001F9EE", "tag": "Consciousness research", "title": "Read AI self-reports on consciousness as prompt-shaped output, not evidence of inner experience — the same model can be dialed from 2.17 to 7 on a mind-attribution scale."},
    {"icon": "\U0001F4D0", "tag": "Math/science", "title": "Expect the 'bulk-solving' pattern (Astra) to hit adjacent fields — physics is the next domain the panel expects a breakthrough in within weeks to months."},
    {"icon": "\U0001F4B8", "tag": "Open weights", "title": "Track Qwen 27B and similar sub-16GB-RAM models as a two-sided story: cheap capability for builders, and a new swarm-cyberattack surface for defenders."},
    {"icon": "\U0001F680", "tag": "SpaceX", "title": "Treat SpaceX's trillion-dollar-by-2030 target and the Terrafab as a single vertical-integration thesis, not two separate bets — chips, compute, and launch are converging under one balance sheet."},
    {"icon": "\U0001F3DB", "tag": "Policy", "title": "Don't assume the US AI evaluation framework is meaningfully restrictive — it's voluntary, secret, and explicitly exempts open-weight models."},
    {"icon": "\U0001F4BC", "tag": "Startup structuring", "title": "When a well-capitalized founder launches an adjacent company at a high starting valuation, weigh the recapitalization/equity angle alongside the stated product thesis."},
]

RISKS = [
    "This is a five-person panel podcast with strong pre-existing positions (Alex is an outspoken AI-consciousness/personhood advocate; Peter/Dave are SpaceX shareholders/bulls) — treat 'hot takes' explicitly labeled as such as opinion, not confirmed reporting.",
    "Several headline claims (the free-electron-laser EUV interpretation of the Terrafab, the Hark recapitalization theory, the 'DeepMind won a knife fight with Google Brain' account of Jeff Dean's exit) are the panel's own speculative reconstruction from public signals, not confirmed by Google, SpaceX, or Hark.",
    "Auto-generated captions were used to produce this brief; names (e.g. Corey Kavukcuoglu, Discovery Loop, Terrafab) and technical terms may contain transcription errors despite cross-checking against context.",
    "The episode contains two sponsor segments (Google for Startups, Blitzy) and a Fountain Life health-sponsor interview — treat product/benchmark claims in those segments as marketing content, not independent panel analysis.",
]

HOT_TAKES = [
    {"take": 'Gemini has lost the mandate of heaven.',
     "cite": '— Alex', "why": "On Jeff Dean's exit and Demis stepping back in the same week — read as DeepMind winning an internal war that Google lost."},
    {"take": "Everything that will be economically productive in this next century, Elon's going full stack on.",
     "cite": '— Salim', "why": 'Treats chips, compute, and launch as one vertical-integration bet rather than separate businesses.'},
    {"take": 'The old gods are being slaughtered by the new machine gods.',
     "cite": '— Will Kinney, cosmologist', "why": 'Quoted on an unreleased OpenAI model bulk-solving ten decade-old math problems for about $2,000.'},
    {"take": "Elon has taught the entire economy that if you're a founder of a well-capitalized company and you want to increase your equity stake, the best thing you can do is start a parallel company.",
     "cite": '— Alex', "why": "His hot take on Brett Adcock's new launch: the story is equity, not agents."},
    {"take": 'This is China and Chinese labs forcing the western frontier labs to dance.',
     "cite": '— Alex', "why": 'On open-weight releases pushing the cost-capability frontier while US evaluation stays voluntary and secret.'},
    {"take": 'As robots and AI do more and more of the doing, humans spend much, much more time being.',
     "cite": '— Immad Mustafa', "why": 'The optimistic reading, offered in the same segment as the AI-personhood and consciousness debate.'},
]

OTHER_NEWS = [
    {"icon": "\U0001F9E0", "title": "Fountain Life dementia data: ~45% of dementia cases are considered preventable; 1 in 4 Fountain Life members tested had 'advanced brain age,' which improved 26% on average with healthy-living interventions.", "tag": "Health sponsor segment"},
    {"icon": "\U0001F3AC", "title": "Moonshots Live (Sept 25, downtown LA) — 1,500 attendees, guests including Palmer Luckey, Kathy Wood, Anousheh Ansari; features the Future Vision X-Prize film competition (5,000+ entries) and the Build with Gemini X-Prize ($2M prize pool, 25,000 teams).", "tag": "Event plug"},
    {"icon": "\U0001F30D", "title": "Peter met with Michael Kratsios (Office of Science and Technology Policy) at the White House; raised that ~75% of Americans hold a dystopian view of AI and asked about US vs. China open-source strategy — Kratsios confirmed the White House wants US labs producing top-tier open-weight models too.", "tag": "Policy meeting"},
]

GLOSSARY = [
    {"term": "RSI (Recursive Self-Improvement)", "def": "An AI system improving its own capabilities with little or no human help — the stated mission of Jeff Dean's new company, Discovery Loop."},
    {"term": "Mandate of heaven", "def": "Panel shorthand borrowed from Chinese imperial theory: the (now-lost, in their view) perception that Gemini is the presumptive frontier-model leader."},
    {"term": "Terrafab", "def": "SpaceX/Tesla's proposed $16.8B, 100-million-square-foot chip megafacility, believed to use free-electron-laser EUV lithography instead of ASML's tin-droplet approach."},
    {"term": "EUV lithography", "def": "Extreme ultraviolet lithography — the soft-X-ray chipmaking process currently dominated by ASML's tin-droplet-based machines."},
    {"term": "OM2W (Online Mind2Web)", "def": "An industry benchmark testing whether an AI agent can complete real tasks on live websites it has never seen before; used to evaluate Hark's Handoff agent."},
    {"term": "CUA (Computer-Use Assistant/Agent)", "def": "The category of AI agents that operate a computer or browser directly to complete tasks, as opposed to answering a single query."},
    {"term": "Swarm attack", "def": "A cyberattack coordinated across many small, individually modest AI agents (e.g. sub-16GB models on ordinary machines) rather than one large model in a data center — harder to detect and track.",},
    {"term": "Open weight vs. open source", "def": "Open weight means a model's trained parameters are publicly downloadable and runnable; it does not necessarily mean the training code, data, or method are also published."},
]
