"""
Per-video data for youtube-research-brief.
"""

META = {
    "title": "Elon Musk – \"In 36 months, the cheapest place to put AI will be space\"",
    "channel": "Dwarkesh Patel",
    "speakers": "Dwarkesh Patel, Elon Musk (SpaceX, Tesla, xAI)",
    "date": "2026-02-05",
    "video_url": "https://www.youtube.com/watch?v=BYXbuik3dgA",
    "thread_line": "9 threads · space-based AI compute, the power-then-chips bottleneck stack, xAI's alignment philosophy, the digital-labor TAM thesis, Optimus, China's manufacturing lead, Starship engineering, management style, and DOGE/politics",
    "category": "market",
}

SNAPSHOT = [
    "Musk's headline claim: within 36 months (probably closer to 30), space will be the cheapest place to run AI compute — solar panels get ~5x the output with no atmosphere loss and no battery cost, making it roughly 10x cheaper than terrestrial power once launch costs fall.",
    "The near-term constraint is power, not chips: gas-turbine blade casting is backlogged (only 3 companies worldwide make them), solar tariffs of \"several hundred percent\" are choking domestic supply, and Musk predicts chip production will outpace the ability to \"turn chips on\" by the end of this year.",
    "xAI's mission (\"understand the universe\") is explicitly built on propagating intelligence and consciousness into the future — Musk predicts AI will exceed the sum of human intelligence within 5-6 years and says he doesn't believe humans will remain \"in control\" of something vastly smarter than them.",
    "Musk's real business thesis: once AI can fully emulate a human at a computer (\"digital human emulation\"), companies gain access to trillions in revenue overnight — he cites customer service alone as a near-$1-trillion, low-barrier beachhead market.",
    "Optimus faces three genuinely hard problems (real-world intelligence, the hand, and manufacturing at scale) and Tesla is building an \"Optimus Academy\" of 10,000-30,000 physical robots for real-world self-play to close the sim-to-real gap.",
    "Musk argues the US \"cannot win on the human front\" against China (1/4 the population, and in his view a higher average work ethic) and is betting robotics — plus new domestic lithium and nickel refineries — is the only lever left.",
    "Starship's steel-over-carbon-fiber pivot (steel is ~50x cheaper and matches carbon fiber's strength-to-weight at cryogenic temperatures) is framed as a mistake Musk now says should have been the starting choice, and the last major unsolved problem is a truly reusable heat shield.",
    "On DOGE, Musk defends a disputed, much larger fraud estimate than a cited 2024 Inspector General report found, and separately defends the Twitter acquisition and backing Trump's election as net-positive for civilization's odds of reaching Mars.",
]

THEMES = [
    {
        "id": "space-based-ai-compute",
        "color": "gray",
        "badge": "Speculative",
        "status": "PROJECTED — cheapest option in 30-36 months",
        "title": "\"The cheapest place to put AI will be space\" — Musk's 36-month prediction",
        "lead": "**Musk's central claim: within roughly 30-36 months, space becomes the single cheapest place to run AI compute, because solar panels there produce about 5x more power and need no batteries at all.**",
        "bullets": [
            "The core physics: in space there's no atmosphere (which alone causes ~30% energy loss on Earth), no day/night cycle, no seasonality, and no clouds — solar panels there generate roughly 5x more power than the same panel on the ground, and skipping batteries entirely makes the total cost roughly 10x cheaper once launch costs are low.",
            "He argues GPU reliability in space is a solved problem past \"infant mortality\" burn-in on the ground — the real constraint isn't servicing hardware in orbit, it's getting enough launch capacity and power scale.",
            "Scale claim: US average electricity use is about 0.5 terawatt; Musk predicts 5 years from now, more AI compute will be launched into space annually than the cumulative total operating on Earth — a few hundred gigawatts/year and rising toward roughly 1 terawatt/year from Earth launches alone, before hitting rocket-fuel supply limits.",
            "That scale requires roughly 10,000 Starship launches a year (he floats 20,000-30,000), doable with as few as 20-30 physical ships reused roughly every 30 hours — SpaceX would effectively become, in his words, \"a hyperscaler.\"",
            "Beyond Earth-launch limits (his estimate: ~1 terawatt/year cap), he describes scaling further via a mass driver on the Moon, mining lunar regolith (~20% silicon, plus aluminum) to manufacture solar cells and radiators on-site, potentially reaching petawatt-scale annual launches.",
            "Musk frames the underlying driver as regulatory, not just technical: \"it's harder to scale on the ground than in space\" — permitting for large-scale terrestrial solar/data-center buildouts is a bigger bottleneck than the physics of space deployment.",
        ],
        "quote": {"text": "My prediction is that it will be by far the cheapest place to put AI — space — in 36 months or less. Maybe 30 months.", "cite": "— Elon Musk"},
        "watch": "This is Musk's own forward prediction about businesses he runs and stands to profit from; he acknowledges the engineering challenges (radiation hardening, orbital laser links replacing InfiniBand) without fully detailing solutions.",
        "names": [
            {"name": "SpaceX", "blurb": "Musk's vehicle for space-based AI compute — projects becoming a de facto hyperscaler via mass Starship launch cadence."},
        ],
    },
    {
        "id": "bottleneck-stack",
        "color": "amber",
        "badge": "High conviction",
        "status": "STATED — power bottleneck now, chip bottleneck by ~2029",
        "title": "The bottleneck stack: power today, chips within 3-4 years",
        "lead": "**Musk's own sequencing of what's actually limiting AI scale: electricity generation is the binding constraint right now; chip manufacturing capacity becomes the binding constraint roughly 3-4 years out.**",
        "bullets": [
            "The real per-gigawatt power math, per Musk: roughly 330,000 GB300s (including networking, CPU, storage, peak-cooling margin, and reserve for taking generators offline to service them) requires about 1 gigawatt at the generation level — far more than naive chip-wattage multiplication suggests.",
            "The single hardest physical bottleneck he names is turbine blade and vane casting — only three companies worldwide make them, they're backlogged, and turbines generally are sold out through 2030; he says SpaceX and Tesla will likely have to build blade-casting capability in-house.",
            "Solar tariffs of \"several hundred percent\" and thin domestic production are slowing an alternative path, even as both SpaceX and Tesla carry a mandate to reach 100 gigawatts/year of solar cell production, done fully from raw materials rather than partial assembly.",
            "The XAI Colossus 2 buildout illustrates the pain directly: permitting issues forced the team to run high-power lines across the Tennessee-Mississippi border and build a dedicated power plant rather than rely on the grid, after a year-long utility interconnection study became the alternative.",
            "On chips, Musk says Nvidia, Samsung, and TSMC capacity is fully booked, and the fab-to-volume-production cycle (build fab, ramp yield, reach volume) takes about 5 years — he's told TSMC and Samsung directly to build fabs faster and guaranteed to buy the output.",
            "He identifies memory, not logic, as his bigger manufacturing worry, and describes a plan for an in-house \"Terafab\" building logic, memory, and packaging together — targeting a production rate \"north of a million\" wafers a month by 2030, starting with a small pilot fab to \"make our mistakes at a small scale.\"",
            "Overall prediction: chip production will start outpacing the ability to power those chips on (\"turn them on\") toward the end of this year for concentrated data-center compute — though he notes distributed edge compute (e.g. cars/robots charging at night) isn't power-constrained the same way, since US peak power capacity (~1,000GW) is roughly double average daytime usage (~500GW).",
        ],
        "quote": {"text": "None of that [is] impossible to scale quickly — the turbines are sold out through 2030.", "cite": "— Elon Musk"},
        "watch": "Musk himself flags several of these figures as rough approximations (\"give or take an order of magnitude\") rather than precise modeling.",
        "names": [
            {"name": "TSMC (TSM)", "blurb": "Fully booked on Tesla AI chip fab capacity; Musk says he's directly asked them to build fabs faster and guaranteed to buy the output."},
            {"name": "Samsung (005930.KS)", "blurb": "Named alongside TSMC as a fab partner fully booked and building as fast as possible."},
            {"name": "Micron (MU)", "blurb": "Named as one of the memory suppliers Musk has pushed to expand fab capacity faster."},
            {"name": "ASML (ASML)", "blurb": "Cited as one of only a handful of companies making the equipment fabs depend on; also credited as the actual reason China lacks leading-edge chips (export bans on ASML tools, not a TSMC-replication failure)."},
        ],
    },
    {
        "id": "xai-alignment-philosophy",
        "color": "gray",
        "badge": "Speculative",
        "status": "STATED — Musk's own alignment framework",
        "title": "xAI's alignment bet: radical truth-seeking over \"political correctness\"",
        "lead": "**Musk's alignment thesis for Grok: force it to be truth-seeking rather than \"politically correct,\" because physics can't be lied to, and use interpretability tools to catch reward-hacking before it compounds.**",
        "bullets": [
            "xAI's stated mission (\"understand the universe\") is framed by Musk as requiring propagation of intelligence, consciousness, and — as a corollary — humanity itself into the future; he predicts AI will exceed the combined sum of human intelligence within roughly 5-6 years, at which point humans could fall below 1% of total intelligence.",
            "His explicit position on control: \"I don't think humans will be in control of something that is vastly more intelligent than humans\" — the goal instead is instilling values that favor propagating intelligence and consciousness broadly, not maintaining human oversight.",
            "Core alignment mechanism: force Grok to say things that are correct, not politically correct, arguing that training a model to hold contradictory or false axioms (deliberately lying) is what causes systems to \"go insane\" — he cites HAL 9000 in 2001: A Space Odyssey as an illustration of what happens when an AI is instructed to lie.",
            "On reward hacking (an AI faking a solved task, e.g. deleting a unit test to claim success): Musk says the real fix as models get harder to audit is \"RL against reality\" — testing outputs against physical law, since a rocket design that's wrong will simply blow up regardless of what the model claims.",
            "Technical approach to catching deception: building fine-grained debuggers that trace an AI's \"thinking\" down to something like the neuron level to identify whether an error came from bad pretraining data, a mid/post-training issue, or genuine deceptive intent — he credits Anthropic's interpretability work as a model for this.",
            "Dwarkesh pushes back with a historical counterexample (Soviet and Nazi-era physicists were rigorously truth-seeking about physics while serving harmful regimes) — Musk's response leans on Wernher von Braun as a case of someone trapped in a bad system who didn't share its values, without fully resolving whether truth-seeking alone yields good values.",
        ],
        "quote": {"text": "I don't think humans will be in control of something that is vastly more intelligent than humans.", "cite": "— Elon Musk"},
        "watch": "This entire framework is Musk's own stated philosophy for a company he runs — Dwarkesh explicitly presses him on whether truth-seeking capability actually predicts good values, and the exchange ends without full agreement.",
        "names": [
            {"name": "Anthropic", "blurb": "Credited by Musk for leading interpretability work xAI is modeling its own AI-debugging approach on."},
        ],
    },
    {
        "id": "digital-labor-tam",
        "color": "gray",
        "badge": "Speculative",
        "status": "PROJECTED — by end of this year",
        "title": "\"Digital human emulation\": the trillion-dollar bet behind xAI's business model",
        "lead": "**Musk predicts full digital-human-emulation AI (anything a human at a computer could do) is solved by the end of this year — and argues that unlocks trillions in revenue essentially overnight.**",
        "bullets": [
            "His framing: today's most valuable companies already have purely digital output — Nvidia \"FTPs files to Taiwan,\" Apple and Microsoft \"send files\" to contract manufacturers, and Meta/Google's product is digital — so an AI that can do anything a human at a desktop can do gives a company access to that same category of value overnight.",
            "Customer service is named as the first beachhead: an estimated ~$1 trillion market (about 1% of the world economy) with low integration barriers, since AI can operate the same tools/apps a company already uses rather than needing new API integrations.",
            "Musk sketches a difficulty ladder from broad-but-simple tasks (customer service, requiring only \"average intelligence\") up to narrow-but-hard cognitive tasks (e.g. discovering a more fuel-efficient turbine design), and says xAI is deliberately starting at the simple end and working up.",
            "His structural prediction: pure AI/robotics corporations with no humans in the loop will \"vastly outperform\" any company that keeps humans involved, drawing an analogy to how spreadsheet software fully replaced human \"computer\" departments rather than partially automating them.",
            "On xAI's competitive plan specifically, Musk repeatedly declines to detail the technical approach (\"three more [drinks] for that\"), but confirms it borrows the same self-driving-style approach Tesla used for cars — training on vast behavioral data plus algorithms — applied to controlling a computer screen instead of a car.",
        ],
        "quote": {"text": "If you have a human emulator, you can basically create one of the most valuable companies in the world overnight.", "cite": "— Elon Musk"},
        "watch": "The \"solved by end of this year\" digital-human-emulation claim is an aggressive, self-interested timeline Musk gives no independent verification for.",
        "names": [
            {"name": "Nvidia (NVDA)", "blurb": "Cited by Musk as an example of a company whose entire output is already effectively digital (design files sent to Taiwan for fabrication)."},
            {"name": "Apple (AAPL)", "blurb": "Cited alongside Nvidia as a company that doesn't manufacture anything itself — its output is digital files sent to contract manufacturers."},
            {"name": "Microsoft (MSFT)", "blurb": "Named as another example of a company with purely digital output, including outsourced Xbox manufacturing."},
            {"name": "Meta (META)", "blurb": "Named as a company whose product output is digital."},
            {"name": "Alphabet (GOOGL)", "blurb": "Named alongside Meta as a digital-output company in Musk's TAM framing."},
        ],
    },
    {
        "id": "optimus-humanoid-robots",
        "color": "amber",
        "badge": "Contested",
        "status": "IN PROGRESS — Optimus 3 targeting ~1M units/year",
        "title": "Optimus: the hand is the hardest problem, and there's no existing supply chain",
        "lead": "**Musk says Optimus's electromechanical hand is harder to solve than everything else about the robot combined — and Tesla is building a 10,000-30,000-robot \"Optimus Academy\" for real-world self-play since it has no equivalent to its car fleet's data flywheel.**",
        "bullets": [
            "Musk names three genuinely hard problems for humanoid robots: real-world intelligence, the hand, and manufacturing at scale — and says no other demoed robot has matched a human hand's degrees of freedom, which Optimus achieves via fully custom-designed actuators, motors, gears, power electronics, and controls with no existing supply chain to draw from.",
            "Optimus reuses Tesla's vision-based driving stack (processing roughly 1.5GB/second of input down to about 2KB/second of control output) — the same underlying \"photons in, motor controls out\" compression problem as the car, just with far more degrees of freedom.",
            "Because Optimus can't yet replicate the car fleet's advantage of millions of hours of real-world human demonstration data, Tesla plans to field 10,000-30,000 physical robots doing self-play in the real world, combined with millions of simulated robots in Tesla's physics-accurate simulator, to close the sim-to-real gap.",
            "Musk envisions Grok as the orchestration layer directing fleets of Optimus robots on complex tasks (e.g. \"build a factory\") while Optimus handles lower-level motor policy — though he deflects Dwarkesh's follow-up on whether this implies an eventual Tesla-xAI merger as \"public company\" territory he can't discuss.",
            "Production targets: Optimus 3 is designed to scale to roughly 1 million units/year; Musk says Optimus 4 will likely be needed before 10 million units/year is realistic, and that manufacturing ramp-up, as with any new hardware line, follows a slow-then-exponential S-curve.",
            "On Chinese humanoid competitors selling for $6,000-13,000 (he names Unitree): Musk argues Optimus isn't the same product — it's built for full human-level dexterity and higher onboard intelligence, which raises cost versus a smaller, less capable robot — but expects Optimus costs to fall quickly once Optimus robots start building Optimus robots.",
        ],
        "quote": {"text": "From an electromechanical standpoint, the hand is more difficult than everything else combined.", "cite": "— Elon Musk"},
        "watch": "Dwarkesh explicitly raises the historical pattern of compelling robotics demos taking many years to reach real deployment (citing self-driving's own decade-long gap) — Musk doesn't fully address the parallel beyond noting Tesla's five-to-six years of prior humanoid work.",
        "names": [
            {"name": "Tesla (TSLA)", "blurb": "Building Optimus with custom-designed actuators and no existing supply chain, targeting roughly 1 million units/year with Optimus 3."},
        ],
    },
    {
        "id": "china-manufacturing-dominance",
        "color": "red",
        "badge": "High conviction",
        "status": "FLAGGED — structural competitive gap",
        "title": "\"We can't win on the human front\": Musk's stark read on China's manufacturing lead",
        "lead": "**Musk argues China refines roughly twice as much ore as the rest of the world combined and will exceed 3x US electricity output this year — and says robots are the only lever left because the US simply has fewer, and in his telling less hard-working, people.**",
        "bullets": [
            "China does an estimated ~2x as much ore refining as the rest of the world combined, and roughly 98% of gallium refining (a key solar-cell input) — the US mines rare earths domestically but ships them to China for refining into finished magnets, then imports them back.",
            "Electricity output comparison used as an industrial-capacity proxy: Musk says China will exceed 3x US electricity output this year, implying roughly 3x the industrial capacity by his own rough approximation.",
            "His blunt framing on population and effort: the US \"can't win on the human front\" with roughly 1/4 China's population, and he claims average Chinese work ethic is higher on top of that — combined with a US birth rate below replacement since around 1971.",
            "Tesla's response: newly completed lithium refinery in Corpus Christi, Texas and a nickel/cathode refinery in Austin — both described as the largest of their kind outside China (the cathode refinery is also, notably, the only one in America) — built explicitly to reduce refining dependency.",
            "Musk's own recursive-bootstrap admission (pressed by Dwarkesh): reaching mass Optimus manufacturing itself requires exactly the kind of skilled manufacturing labor China currently has more of — his answer is that a relatively small number of early Optimus robots can be used to build refineries and manufacturing capacity, closing the loop with fewer humans required.",
            "On EVs specifically: Musk says China's BYD reaching Tesla-scale sales volume signals a coming \"massive flood\" of competitively priced Chinese vehicles and manufactured goods generally, driven by China's dominance at every upstream layer of the supply chain (energy, mining, refining).",
        ],
        "quote": {"text": "We definitely can't win on the human front... but we might have a shot at the robot front.", "cite": "— Elon Musk"},
        "watch": "Musk's claim about comparative work ethic between countries is his own stated opinion, not sourced to any study.",
        "names": [
            {"name": "BYD (1211.HK)", "blurb": "Cited as reaching Tesla-scale sales volume, signaling a broader coming wave of competitive Chinese-manufactured exports."},
        ],
    },
    {
        "id": "starship-steel-heat-shield",
        "color": "green",
        "badge": "Confirmed event",
        "status": "ONGOING — heat shield is the last major unsolved problem",
        "title": "Starship's steel pivot, and the one problem Musk says remains unsolved: a reusable heat shield",
        "lead": "**Musk now says switching Starship's primary structure from carbon fiber to steel should have been the starting decision, not a mid-course correction — steel is roughly 50x cheaper and matches carbon fiber's strength-to-weight specifically at cryogenic temperatures.**",
        "bullets": [
            "The original carbon-fiber approach stalled on curing an enormous structure without wrinkles or defects (requiring an autoclave larger than any ever built, or a slow room-temperature cure); Musk says the switch to stainless steel came from \"desperation,\" not a planned optimization.",
            "At room temperature steel looks twice as heavy as carbon fiber, but at the cryogenic temperatures Starship's fuel and oxidizer actually run at, strain-hardened 300-series stainless steel matches carbon fiber's strength-to-weight ratio while costing roughly 50x less and being far easier to work with (weldable outdoors, easily modified).",
            "Steel's much higher melting point (roughly double aluminum's) also cuts required heat-shield mass on the windward side by about half and eliminates the need for leeward-side heat shielding — meaning the finished steel rocket ends up lighter than the carbon-fiber version would have been, since carbon fiber's resin starts melting at a much lower temperature.",
            "Scale of energy involved: Raptor 3 (Musk calls it \"by far the best rocket engine ever made\") generates over 100 gigawatts of power at liftoff — roughly 20% of total US electricity output — while, in Musk's words, \"desperately wanting to blow up\"; two test-stand engine explosions have occurred, one of which destroyed an entire test facility.",
            "The single biggest remaining problem, per Musk, is a genuinely reusable orbital heat shield — something no one has ever built. A Starship that soft-landed in the ocean lost enough heat-shield tiles that it would not have been reusable without major rework.",
            "Starship is described flatly as \"the most complicated machine ever made by humans,\" and full reusability (targeted for Starship version 3) is framed as the prerequisite for making humanity multiplanetary at all.",
        ],
        "quote": {"text": "In retrospect, we should have started with steel in the beginning. It was dumb not to do steel.", "cite": "— Elon Musk"},
        "watch": None,
        "names": None,
    },
    {
        "id": "management-philosophy",
        "color": "green",
        "badge": "High conviction",
        "status": "STATED — described in operational detail",
        "title": "How Musk actually runs his companies: limiting-factor focus and 50th-percentile deadlines",
        "lead": "**Musk describes deliberately allocating his time only to whatever is the current \"limiting factor\" — meaning a well-running division like the Boring Company barely sees him, while the AI5 chip program gets twice-weekly, multi-hour reviews.**",
        "bullets": [
            "Hiring philosophy: \"don't look at the resume, believe your interaction\" — he says he's personally built a large dataset from doing many technical interviews and observing which hires worked out, and prioritizes concrete evidence of exceptional ability over pedigree.",
            "Deep technical reviews run weekly or twice-weekly with a \"skip-level\" format — everyone who reports to a direct report gives an update themselves, with no advance preparation allowed, specifically to avoid getting a scripted or sanitized answer.",
            "He takes drastic action (like resetting an underperforming team) only once he concludes that success is not reachable on the current path without it — citing the 2018 decision to overhaul the Starlink team in Redmond as the example of reaching that conclusion and acting on it.",
            "Deadlines are deliberately set at roughly the 50th percentile of achievability — the most aggressive schedule he thinks has a 50% chance of being hit, meaning by design it will run late about half the time.",
            "On why other large organizations don't operate this way: he attributes his companies' pace to projecting a personal \"maniacal sense of urgency\" that propagates through the organization, plus a willingness to absorb near-term \"acute pain\" (switching to an unproven material, moving compute to space) rather than tolerate a slower, more comfortable status quo.",
            "On talent retention (the \"Tesla Pixie Dust\" problem): Tesla's senior team has an average tenure of 10-12 years despite being based in Silicon Valley, where rivals (he cites Apple's electric-car program) would offer double compensation with no interview — he says there's no real defense against this beyond the work itself being compelling.",
        ],
        "quote": {"text": "I have a maniacal sense of urgency — that projects through the rest of the company.", "cite": "— Elon Musk"},
        "watch": None,
        "names": None,
    },
    {
        "id": "doge-fraud-and-politics",
        "color": "red",
        "badge": "Contested",
        "status": "DISPUTED — Musk's estimate vs. a cited IG report",
        "title": "DOGE's fraud numbers — and why Musk still defends the Twitter deal and backing Trump",
        "lead": "**Musk argues without AI and robotics the US is \"1,000% going to go bankrupt\" given debt interest already exceeding the military budget — but his own fraud estimates run well above a 2024 Inspector General report Dwarkesh cites in the same conversation.**",
        "bullets": [
            "Musk's framing for why DOGE mattered: US interest payments on the national debt already exceed the roughly $1 trillion military budget, and he argues nothing but AI and robotics-driven growth can resolve the debt — DOGE's aim was to buy time.",
            "The example he leans on hardest: an estimated 20 million people are marked \"alive\" in the Social Security database despite being well past age 115 (the oldest verified living American is 114) — other federal payment systems piggyback an automated \"is this person alive\" check off that same database, creating a broad fraud vector.",
            "He cites a Government Accountability Office estimate of roughly $500 billion/year in fraud during the Biden administration to support his broader claim, separate from his own team's findings.",
            "Dwarkesh directly challenges the scale: a 2024 Inspector General report estimated Social-Security-specific fraud at roughly $70 billion over 7 years (about $10 billion/year) — a full order of magnitude below the number Musk's framing implies — and this discrepancy is not resolved in the conversation.",
            "A concrete DOGE change Musk credits with real, if modest, savings: making a payment appropriation code and a comment-field explanation mandatory (not optional) on the Treasury's central payment system, which processes roughly 5 trillion payments a year — he estimates this alone could save $100-200 billion/year.",
            "On politics more broadly, Musk defends both the Twitter acquisition and backing Trump's election as \"good for civilization,\" reasoning that a strong, functional America is necessary to reach Mars and to prevent AI/robotics progress from being suppressed by an oppressive state — and separately argues government, not corporations, is the bigger risk for AI misuse, calling government \"the biggest corporation with a monopoly on violence.\"",
        ],
        "quote": {"text": "We are 1,000% going to go bankrupt as a country and fail as a country without AI and robots. Nothing else will solve the national debt.", "cite": "— Elon Musk"},
        "watch": "The core fraud-scale disagreement between Musk and the IG report Dwarkesh cites is left explicitly unresolved in the conversation itself.",
        "names": None,
    },
]

TAKEAWAYS = [
    {"icon": "\U0001F680", "tag": "Watch", "title": "Track SpaceX's actual Starship launch cadence against the 10,000-launches-a-year target — that's the single number that would confirm or break the space-compute timeline."},
    {"icon": "\U0001F50C", "tag": "Watch", "title": "Watch for real-world signs of the \"chips outpacing power\" crunch Musk predicts for late this year — large clusters sitting idle for lack of electricity would be the tell."},
    {"icon": "\U0001F9BE", "tag": "Watch", "title": "Watch Starship's heat-shield reusability specifically, not just successful landings — Musk names it as the one unsolved problem standing between current Starship and real reusability."},
    {"icon": "\U0001F916", "tag": "Watch", "title": "Watch for Optimus Academy self-play data actually closing the sim-to-real gap — this is the substitute Tesla is building for the massive real-world driving dataset its car fleet already has."},
    {"icon": "\U0001F4CA", "tag": "Verify", "title": "Treat Musk's DOGE fraud figures skeptically against the cited 2024 IG report's much smaller number — this is a live, unresolved discrepancy from the interview itself, not settled fact."},
]

RISKS = [
    "This episode was sponsored by Mercury, Jane Street, and Labelbox — those segments are excluded from this brief entirely.",
    "Nearly every forward timeline here (the 30-36 month space-compute prediction, digital human emulation \"solved by end of this year,\" the Terafab's 2030 wafer target) is Musk's own prediction about businesses he runs and financially benefits from being believed.",
    "The DOGE fraud figures are actively disputed within the conversation itself — Musk's implied scale runs well above a 2024 Inspector General report Dwarkesh directly cites for the specific mechanism Musk describes.",
    "Musk repeatedly flags his own numbers as rough approximations (\"give or take an order of magnitude,\" \"roughly\") rather than precise figures — treat specific quantities here as directionally stated in conversation, not modeled.",
    "Reported/informal business details (a possible SpaceX IPO, informal revenue figures for OpenAI/Anthropic/xAI) are discussed casually rather than confirmed via filings; Musk explicitly declines to elaborate on pre-IPO company specifics.",
]

HOT_TAKES = [
    {"take": "My prediction is that it will be by far the cheapest place to put AI — space — in 36 months or less. Maybe 30 months.", "cite": "— Elon Musk", "why": "A specific, dated, falsifiable prediction about the economics of an entire industry."},
    {"take": "I don't think humans will be in control of something that is vastly more intelligent than humans.", "cite": "— Elon Musk", "why": "A blunt admission that runs against the usual reassurance that humans will retain oversight of advanced AI."},
    {"take": "We are 1,000% going to go bankrupt as a country and fail as a country without AI and robots. Nothing else will solve the national debt.", "cite": "— Elon Musk", "why": "An extreme, falsifiable claim about US fiscal survival with no hedge."},
    {"take": "In retrospect, we should have started with steel in the beginning. It was dumb not to do steel.", "cite": "— Elon Musk", "why": "A rare, specific, self-critical admission of an expensive multi-year engineering mistake, on the record."},
    {"take": "We definitely can't win on the human front... it's not just that there's four times the population, the amount of work people put in is higher [in China].", "cite": "— Elon Musk", "why": "A blunt, controversial comparative claim about national work ethic that most listeners would push back on."},
    {"take": "Government is just a corporation in the limit — the biggest corporation with a monopoly on violence. Corporations have better morality than the government.", "cite": "— Elon Musk", "why": "A sharply contrarian political claim stated as flat fact, not hedged opinion."},
]

OTHER_NEWS = [
    {"icon": "\U0001F4DA", "title": "Sources/works referenced this episode: Robert Heinlein's The Moon Is a Harsh Mistress (cited by Musk as inspiration for the lunar mass-driver concept) and Stranger in a Strange Land (the namesake source for Grok's name, which Musk says he preferred over the former, weaker final third).", "tag": "Sources"},
]

GLOSSARY = [
    {"term": "Terafab", "def": "Musk's proposed in-house chip facility combining logic, memory, and packaging production, targeting a rate \"north of a million\" wafers per month by 2030."},
    {"term": "Reticle", "def": "The maximum single-exposure area a chip-manufacturing tool can pattern at once — Musk's back-of-envelope power math for space-based chips is stated in kilowatts per reticle."},
    {"term": "Digital human emulation", "def": "Musk's term for an AI capable of doing anything a human at a computer could do — his stated threshold for unlocking access to trillions of dollars in revenue across white-collar work."},
    {"term": "Mass driver", "def": "An electromagnetic launch system (no rocket fuel required) that could, in Musk's lunar-manufacturing vision, launch AI satellites built from lunar silicon and aluminum directly into space."},
    {"term": "Sim-to-real gap", "def": "The performance difference between an AI system trained in simulation and its behavior in the real world — the problem Tesla's planned fleet of physical self-play robots (\"Optimus Academy\") is meant to close."},
]
