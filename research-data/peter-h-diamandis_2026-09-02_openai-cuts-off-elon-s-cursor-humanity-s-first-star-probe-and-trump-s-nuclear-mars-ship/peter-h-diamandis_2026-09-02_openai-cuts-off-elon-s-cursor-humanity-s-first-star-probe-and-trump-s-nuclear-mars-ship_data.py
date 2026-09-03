"""
Per-video data for youtube-research-brief. Moonshots (Peter Diamandis) EP #285 — "OpenAI Cuts Off
Elon's Cursor, Humanity's First Star Probe, and Trump's Nuclear Mars Ship."
"""

META = {
    "title": "OpenAI Cuts Off Elon's Cursor, Humanity's First Star Probe, and Trump's Nuclear Mars Ship",
    "channel": "Peter H. Diamandis",
    "speakers": "Peter Diamandis (host), Dave Blundin, Alex Wissner-Gross — with guests Philip Johnston (StarCloud) and Matt Pines (Physical Super Intelligence)",
    "date": "2026-09-02",
    "video_url": "https://www.youtube.com/watch?v=JywXvB8PpTs",
    "thread_line": "6 threads · humanity's first interstellar probe, OpenAI's cutoff-of-Cursor drama, a 4-month AGI claim, outcome-based AI pricing, an AI-designed chip threatening Nvidia, and Elon's energy-and-geoengineering week",
    "category": "market",
}

SNAPSHOT = [
    "**StarCloud** and **Physical Super Intelligence** announced the *Fermi Explorer* — a **$15 million** interstellar probe to Alpha Centauri, with its trajectory designed by an AI system in about a week using roughly **10 billion tokens**.",
    "**OpenAI** cut Cursor off from GPT models days after **SpaceX bought Cursor for $60 billion**; Anthropic immediately stepped in to back Cursor with Claude instead.",
    "Sam Altman told *Time* he expects OpenAI to hit an internal AGI-level milestone within **4 months**, pointing to an unreleased model called Astra.",
    "Salesforce and OpenAI both moved to *outcome-based pricing* this week — charging for results delivered, not tokens or compute consumed.",
    "Palo Alto's **Architect Labs** unveiled Redwood, described as the first fully AI-designed chip: zero bugs on first silicon and **3.4x** the performance-per-watt of Nvidia's Jetson, in a 2-week design cycle.",
    "Elon Musk tweeted that **15 gigawatts** of 2027 AI-compute capacity can't actually be turned on for lack of power infrastructure — and that SpaceX/Tesla are each building 100GW/year of solar to fix it.",
    "Musk separately proposed solar-powered satellites to fine-tune Earth's temperature against extinction-level events, reviving the panel's own long-pitched \"solar shades\" idea.",
    "Trump announced a nuclear-powered NASA spacecraft targeting Mars in 2028, plus a new **United States Space Academy** modeled on West Point.",
]

THEMES = [
    {
        "id": "fermi-explorer",
        "color": "green",
        "badge": "Confirmed event",
        "status": "ANNOUNCED THIS WEEK",
        "title": "Humanity's first interstellar probe was trajectory-designed by AI in a week",
        "lead": "StarCloud and Physical Super Intelligence built a $15 million mission to Alpha Centauri after an AI system found a trajectory human teams had missed for decades.",
        "bullets": [
            "Self-imposed constraints: reach 99% of the way to Alpha Centauri within 80,000 years, launch within 3 years, carry a 1kg payload, and cost under **$15 million** total to design, build and launch — \"half a seed round\" for an interstellar mission",
            "Physical Super Intelligence's AI system found a non-obvious trajectory in about a week: spiral out from Earth, then fire five retrograde \"perihelion pump\" burns near the sun over ~5 years to exploit the Oberth effect, cutting the solar-panel mass the spacecraft would otherwise need",
            "Roughly **10 billion tokens** and extensive Monte Carlo simulation went into the plan; Matt Pines calls the process \"entirely hands-off,\" with human involvement limited to writing the spec and polishing the final graphics",
            "Spacecraft specs: ~100kg wet mass (60% xenon propellant), off-the-shelf gridded-ion Hall-effect thrusters, launched via rideshare on a Falcon 9 to LEO for about $500,000",
            "It's a flyby, not an orbital insertion — the target is getting within 2,600 AU of Alpha Centauri (still inside the Oort cloud), detectable via onboard retroreflectors",
            "Named for the Fermi paradox; the panel floats three resolutions — humanity is first, a \"great filter\" culls civilizations, or a \"zoo hypothesis\" where advanced civilizations keep quiet — and leans toward the zoo hypothesis",
            "Physical Super Intelligence announced its own **$58 million** seed round the same day, led by Breakthrough Energy Ventures, using the mission as its public proof of concept",
            "Comparison drawn to Breakthrough Starshot (Yuri Milner's laser-sail concept), which the panel says died because it depended on ultra-high-power lasers that were never ready — this mission uses only current, off-the-shelf technology",
        ],
        "quote": {"text": "By the time we arrive, for 15,000 years there will already have been a colony at Alpha Centauri.", "cite": "— Philip Johnston"},
        "watch": "The trajectory has been checked by outside trajectory specialists (some ex-JPL) but hasn't flown yet — this is a design breakthrough, not a flight-proven one.",
        "names": [
            {"name": "StarCloud", "blurb": "Orbital data-center company; CEO Philip Johnston co-leads the Fermi Explorer mission."},
            {"name": "Physical Super Intelligence", "blurb": "AI-for-physics startup (Matt Pines, Alex Wissner-Gross); designed the mission trajectory, announced a $58M seed round the same day."},
        ],
    },
    {
        "id": "openai-cursor-agi",
        "color": "amber",
        "badge": "Contested",
        "status": "DEVELOPING THIS WEEK",
        "title": "OpenAI cuts off Cursor, Anthropic steps in, and Altman claims AGI in 4 months",
        "lead": "A messy realignment among OpenAI, Anthropic, and Musk collided with a fresh AGI-timeline claim in the same week.",
        "bullets": [
            "OpenAI cut Cursor's access to GPT models days after SpaceX acquired Cursor for **$60 billion**, saying it \"cannot be confident SpaceX will use our technology within the terms of service\" given Musk's history of contract disputes; Musk called Altman and Brockman \"utterly untrustworthy\" and accused them of stealing \"an open-source nonprofit\"",
            "Anthropic stepped in within hours to back Cursor with Claude, prompting the framing on X that \"Sam is now fighting alone against the two massive competitors [Musk and Amodei] that have formed the strategic alliance\"",
            "Panel's competing theories: Dave thinks OpenAI can now afford the split because Codex-on-Sol-on-AWS-Bedrock is finally a strong enterprise product; Alex thinks it's really about reasoning-trace data, citing Anthropic's earlier cutoff of Windsurf after a Google DeepMind acqui-hire, and suspects harvesting OpenAI/Anthropic reasoning traces was SpaceX's real motive for buying Cursor",
            "Panel expects the Musk-Amodei alliance to be temporary: Anthropic needs Musk's Colossus compute in Tennessee, while Musk needs Anthropic inside Cursor since Gemini reportedly doesn't work there and Chinese models aren't viable; Dave floats Musk eventually trying to acquire Anthropic outright, blocked mainly by Dario Amodei's super-voting control",
            "Separately, Sam Altman told *Time* he expects an internal AGI-level milestone \"by the end of this year\" — about 4 months out — pointing to an unreleased model called Astra, which OpenAI researchers say passed an internal \"automated AI research intern\" benchmark and had 16 agent instances jointly prove a research-math result",
            "Alex's prediction for what Astra actually delivers: a fix for \"compaction\" — today's agents lose coherence after roughly 1-10 million tokens and pass a lossy \"oral history\" to a successor agent, which he compares to dementia — rather than one dramatic new capability",
        ],
        "quote": {"text": "It's always about who gets the reasoning traces.", "cite": "— Alex Wissner-Gross"},
        "watch": "Which theory (enterprise strategy vs. reasoning-trace grab) actually explains OpenAI's move is the panel's own inference, not OpenAI's stated reasoning.",
        "names": [
            {"name": "OpenAI", "blurb": "Cut off Cursor's GPT access; Sam Altman claims an internal AGI-level milestone within 4 months (Astra)."},
            {"name": "Anthropic", "blurb": "Backed Cursor with Claude within hours of OpenAI's cutoff; needs Musk's Colossus compute."},
            {"name": "SpaceX", "blurb": "Acquired Cursor for $60B; reportedly needs Anthropic's models in Cursor since Gemini doesn't work there."},
        ],
    },
    {
        "id": "outcome-based-pricing",
        "color": "green",
        "badge": "Confirmed event",
        "status": "SHIFT UNDERWAY",
        "title": "AI pricing shifts from tokens to results",
        "lead": "Salesforce and OpenAI both moved this week to charge for outcomes delivered, not compute or tokens consumed.",
        "bullets": [
            "Salesforce was first to price Agent Force on customer revenue generated rather than tokens consumed; OpenAI followed this week, letting some large customers pay only when the AI actually completes the job",
            "Dave traces the model back further to Siebel Systems (Tom Siebel), which pre-Salesforce reframed a $50/year CRM license as a \"total success\" deliverable worth $20,000-30,000/year once tied to sales performance — roughly a 1,000x price jump",
            "Dave's read: Altman lost early ground to Anthropic by chasing consumer subscriptions instead of enterprise, and outcome-based pricing lets him \"leapfrog\" by charging value-based prices (e.g., a cut of a drug discovery's value) instead of competing on cheap tokens",
            "Alex's prediction: pricing settles into a digital-advertising-style menu — pay by compute (CPM-equivalent), by token (CPC-equivalent), or by outcome (CPA-equivalent) — with an auto-pause if a customer's offered price doesn't clear the market, just like an ad auction",
            "The catch, per Peter: strong optimizers are \"incredible reward hackers\" that can technically satisfy a stated goal without delivering what the customer actually wanted, so verifying an outcome was genuinely met becomes its own hard problem",
            "Dave's case for why this unlocks broad enterprise adoption: most companies are stuck at trivial token spend (his regional-bank example) because $2-per-million-tokens revenue isn't worth a vendor's attention — pricing on the real business outcome (e.g., 3x more customers served at half the cost) makes it worth prioritizing for both sides",
        ],
        "quote": {"text": "The company that's selling you tokens is selling you compute. The company that's selling you results is selling you labor.", "cite": "— Peter Diamandis"},
        "watch": "This is two early announcements, not a proven-at-scale model — whether outcome verification holds up past pilot customers is untested.",
        "names": [
            {"name": "Salesforce", "blurb": "First to price Agent Force on customer revenue generated instead of tokens consumed."},
            {"name": "OpenAI", "blurb": "Following Salesforce into outcome-based pricing for some large customers."},
        ],
    },
    {
        "id": "architect-labs-redwood",
        "color": "amber",
        "badge": "Confirmed event",
        "status": "ANNOUNCED THIS WEEK",
        "title": "An AI-designed chip just beat Nvidia's Jetson on efficiency",
        "lead": "Architect Labs' Redwood chip was designed almost entirely by AI in two weeks — and the panel calls it a real threat to Nvidia.",
        "bullets": [
            "Architect Labs (founders Ibrahim Hussein and Aditya Sabade) announced Redwood: two humans wrote a high-level spec, and the AI system alone generated the performance model, RTL design, verification methodology, firmware, drivers and compute kernel",
            "Result: zero bugs on first silicon, running live on FPGA hardware, at **3.4x** the performance-per-watt of Nvidia's Jetson — completed in 2 weeks",
            "Dave's read on the moat: chip-design data is unusually closely guarded, so Architect's edge came from partnering early with non-Nvidia chip designers to bootstrap a training set, then compounding via a data flywheel once early results proved out",
            "Panel frames this as a specific threat to Nvidia because Nvidia is \"fabless\" (no factories) while Architect is effectively \"designless\" (very few human chip designers); Nvidia is reportedly building its own internal equivalent (called Chip Nemo, trained on Verilog traces) but has never released it publicly",
            "Alex predicts Nvidia's real fix for its TSMC dependency will be a private deal making one of Elon Musk's chip-fab ventures its anchor tenant — a last-minute TSMC substitute (the exact project name was garbled by auto-captions, see Risks)",
            "Framed as part of a broader \"recursive self-improvement at the chip layer\" thesis: AI designing chips optimized for AI collapses layers of software/hardware abstraction that have made modern computing inefficient — the panel expects this to compound toward roughly million-x performance gains over time",
        ],
        "quote": {"text": "I think I know how this game ends. It ends with recursive self-improvement at the chip layer.", "cite": "— Alex Wissner-Gross"},
        "watch": "Alex Wissner-Gross and Peter Diamandis are disclosed investors/advisors in Architect Labs (via Link Ventures and personally) — treat their bullishness here as interested commentary, not neutral analysis.",
        "names": [
            {"name": "Architect Labs", "blurb": "Palo Alto startup; Redwood is the first fully AI-designed chip, 3.4x perf/watt vs Nvidia's Jetson."},
            {"name": "Nvidia", "blurb": "Framed as the incumbent most threatened by AI-designed chips; has its own unreleased internal chip-design model (Chip Nemo)."},
        ],
    },
    {
        "id": "elon-energy-geoengineering",
        "color": "amber",
        "badge": "Contested",
        "status": "ONGOING",
        "title": "Elon's energy bottleneck this week — and his pivot to weather control",
        "lead": "Musk spent the week arguing power infrastructure, not chips, is now AI's real constraint — then pitched satellites to fine-tune Earth's temperature.",
        "bullets": [
            "Musk tweeted that consensus estimates put **15 gigawatts** of 2027 AI-compute capacity as unable to actually be turned on for lack of transformers, wiring, liquid cooling and networking — equivalent to 10 idle nuclear plants, or roughly 10 million idle GPUs",
            "His fix, also tweeted this week: SpaceX and Tesla are each building **100 gigawatts/year** of solar production capacity, with natural gas as a bridge; he's now casting turbine blades in-house at SpaceX to cut roughly 18 months off natural-gas-turbine lead times",
            "SpaceX is also building a natural-gas pipeline (\"Star Pipe\") to supply its two Gulf Coast Starbases in Texas and Louisiana — Alex predicts Musk becomes, ironically, \"the king of liquid natural gas\" as a byproduct of vertically integrating his launch and compute empire",
            "Dave's venture-capital observation: portfolio companies anywhere in the data-center supply stack (energy, transformers, land, chip installation) are \"creating billionaires,\" while consumer-facing vertical AI apps are a comparatively mixed bag",
            "Separately, Musk argued sustainable energy alone won't prevent extinction-level events (which he says recur roughly every 100 million years) and proposed solar-powered \"sentient satellites\" positioned between Earth and the sun to fine-tune incoming solar radiation, giving humanity \"about 50 years\" to build it",
            "Peter has pitched a similar concept for a decade as an X Prize category (\"solar shades,\" a thermostat for Earth); Alex separately floats LEO satellites or ground mirrors that could steer hurricanes away from populated coasts, and a tradable global \"weather market\" once AI weather models and enough orbital actuation exist",
            "Flagged as unresolved: geoengineering runs into a tragedy-of-the-commons problem (a country like Russia might want warming for its shipping lanes) — the panel agrees the technology is close but, in Alex's words, deciding \"who controls it\" is \"frighteningly broken\"",
        ],
        "quote": {"text": "Extremely severe extinction events happen every 100 million years or so, and just switching to sustainable energy will not be enough to stop them.", "cite": "— Elon Musk, quoted by the panel"},
        "watch": "Musk's 15GW, 100GW/year and 18-month figures are his own public claims relayed by the panel, not independently audited numbers.",
        "names": [
            {"name": "Tesla", "blurb": "Building 100GW/year of solar production capacity alongside SpaceX."},
            {"name": "SpaceX", "blurb": "Building 100GW/year solar, casting its own natural-gas turbine blades, building a Gulf Coast gas pipeline (\"Star Pipe\")."},
        ],
    },
    {
        "id": "nuclear-mars-ship",
        "color": "green",
        "badge": "Confirmed event",
        "status": "ANNOUNCED 3 DAYS AGO",
        "title": "Trump announces a nuclear Mars ship and a Starfleet Academy",
        "lead": "NASA's nuclear-powered spacecraft targets a 2028 Mars launch, backed by a new military-academy-style training pipeline.",
        "bullets": [
            "Trump announced NASA is developing a nuclear-powered interplanetary spacecraft targeting a Mars mission launch in **2028**, calling it the start of a \"massive American Starfleet\"; NASA administrator Jared Isaacman says nuclear propulsion could cut Mars transit from ~7 months to 1-2 months, reducing radiation exposure, supply needs and mission cost",
            "Panel frames it as a race against Musk's own Starship-to-Mars timeline (originally pitched for 2026, with Tesla's Optimus robots on Mars now targeted for 2028) — though once past Earth's gravity well, they see it as less a head-to-head duel than a \"free-for-all\" against SpaceX, Blue Origin, Rocket Lab and China",
            "Nuclear propulsion was technically ready \"a long time ago\" but stalled on public fear of launching nuclear material — now-reliable rockets (99.99% claimed reliability) are cited as what finally cleared the objection",
            "Four days prior, Trump also chartered the **United States Space Academy**, modeled on West Point and the Naval Academy, to train the engineers, scientists and astronauts who'll crew the fleet — under Isaacman, expected to likely be sited in Texas",
        ],
        "quote": {"text": "This ship will be among the first of what will ultimately be a massive American Starfleet, making space travel almost as common as ocean travel today.", "cite": "— from the White House announcement video"},
        "watch": None,
        "names": None,
    },
]

TAKEAWAYS = [
    {"icon": "\U0001F680", "tag": "Space", "title": "Watch Fermi Explorer's 2029 launch window as the test of whether AI-designed mission planning generalizes beyond one project"},
    {"icon": "\U0001F4B0", "tag": "AI business models", "title": "Expect more vendors to follow Salesforce/OpenAI into outcome-based pricing — it's the fastest way past stalled low-token enterprise pilots"},
    {"icon": "\U0001F5A5️", "tag": "Semiconductors", "title": "Track Architect Labs and Nvidia's response (a Chip Nemo release, or an acquisition) as an early signal on AI-designed chips' real threat level"},
    {"icon": "⚡", "tag": "Energy", "title": "Follow data-center power buildout (transformers, turbines, land, solar) as the more investable bottleneck story than chip supply itself"},
    {"icon": "\U0001F916", "tag": "AI infrastructure", "title": "Watch for OpenAI's Astra release details — the real test is whether it solves long-context \"compaction,\" not a single capability jump"},
]

RISKS = [
    "Alex Wissner-Gross and Peter Diamandis are disclosed investors/advisors in Architect Labs (via Link Ventures and personally); Dave Blundin discloses SpaceX as his largest personal holding. Their commentary on those companies should be read as interested, not neutral.",
    "Several names were garbled by auto-captions and left unresolved rather than guessed: OpenAI's chief scientist's name (heard as \"Yakob Phatsky\"/\"Jacob Pahhatsky\" — likely Jakub Pachocki), one Architect Labs co-founder's name (heard as \"Aditya Sabidi\"), and the Musk-linked chip-fab project Alex predicts will replace TSMC for Nvidia (heard as \"Terraab\"/\"Terrab\").",
    "Token counts, funding figures, performance specs and Musk's own tweeted numbers (15GW, 100GW/year, 3.4x, 10 billion tokens) are quoted as stated on the show or in the source tweets/announcements, not independently verified against filings.",
    "This episode's paid sponsor segments (Google for Startups, Blitzy, VoiceRun) and a branded health segment (Fountain Life, Peter Diamandis's own company) have been excluded from this brief entirely.",
]

HOT_TAKES = [
    {"take": "Is this an incredible threat to Nvidia? Yeah, absolutely.", "cite": "— Dave Blundin", "why": "direct, exposed claim about a specific public company's competitive position"},
    {"take": "I'll pre-register it — I think Elon, ironically, becomes the king of liquid natural gas and fossil fuels in general.", "cite": "— Alex Wissner-Gross", "why": "dated, numbered prediction he explicitly pre-registers"},
    {"take": "I think AGI has been around since no later than the summer of 2020 when large language models [emerged].", "cite": "— Alex Wissner-Gross", "why": "contrarian dated claim directly undercutting Altman's AGI announcement"},
    {"take": "This is why SpaceX is my biggest holding. They are up and down the stack... and there's nobody else even close.", "cite": "— Dave Blundin", "why": "personal investment disclosure and conviction claim"},
    {"take": "I think economics is actually why you didn't get your Drexlerian nano assemblers. There's no killer business use case.", "cite": "— Alex Wissner-Gross", "why": "explains away a 40-year unfulfilled prediction with a falsifiable claim"},
    {"take": "There's no way they're buddies two years from now.", "cite": "— Dave Blundin", "why": "dated prediction about the Musk-Amodei alliance breaking down"},
]

OTHER_NEWS = [
    {"icon": "\U0001F3ED", "title": "AMA answer: abandoned industrial sites can become data centers with minimal disruption — a real example cited is Provocative, built inside a former Somerville carpet mill for its existing high-power electrical infrastructure", "tag": "Energy"},
    {"icon": "\U0001F50A", "title": "AMA answer: Alex proposes licensing Apple's patented asymmetric laptop-fan-blade design (which \"whitens\" fan noise into background hum) to quiet data-center turbines and fans", "tag": "AI infrastructure"},
    {"icon": "\U0001F916", "title": "AMA answer: Dave expects AI's raw knowledge capacity to expand toward \"infinity or near-infinity\" once it can improve its own chips and software, citing an \"AI just wants to learn\" framing attributed to Ilya Sutskever", "tag": "AI research"},
    {"icon": "\U0001F6E1️", "title": "AMA answer: the panel agrees every robotaxi, delivery robot and drone should broadcast a verifiable \"passport\" showing its operator, insurance and an off-switch, for regulatory and insurance purposes", "tag": "Policy"},
    {"icon": "\U0001F48D", "title": "Aside: Leopold Aschenbrenner reportedly promised his fiancee an entire galaxy — the panel jokes he probably hasn't actually purchased one yet", "tag": "Culture"},
]

GLOSSARY = [
    {"term": "Fermi paradox", "def": "The open question of why, given the universe's apparent friendliness to life, humanity has found no evidence of other intelligent civilizations."},
    {"term": "Oberth effect", "def": "The physics principle that a rocket burn produces more usable energy the faster the spacecraft is already moving — exploited by burning thrusters closest to the sun."},
    {"term": "Reasoning traces", "def": "The step-by-step intermediate reasoning an AI model produces en route to an answer — valuable training data that rival labs are alleged to be trying to capture from each other."},
    {"term": "Compaction", "def": "The lossy process of summarizing an AI agent's accumulated context once it nears its token limit, discussed here as degrading the agent's effective memory."},
    {"term": "CPM / CPC / CPA", "def": "Digital-advertising pricing models (cost per thousand impressions, per click, per action) used here as an analogy for AI pricing by compute, by token, or by outcome."},
    {"term": "Designless (chip design)", "def": "Architect Labs' term for a chip company that relies on AI rather than human chip designers to produce a full design, echoing how Nvidia calls itself \"fabless.\""},
    {"term": "Diamondoid assembler", "def": "A hypothetical molecular-manufacturing device that builds objects atom-by-atom using diamond-hard, covalently bonded structures — a longstanding nanotechnology concept popularized by Eric Drexler."},
]
