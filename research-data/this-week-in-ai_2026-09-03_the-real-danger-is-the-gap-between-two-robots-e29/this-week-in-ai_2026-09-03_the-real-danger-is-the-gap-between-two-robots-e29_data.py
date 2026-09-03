"""
Per-video data for youtube-research-brief. This Week in AI E29 — "The real danger is the gap
BETWEEN two robots" (Gatik, LiveKit, Path panel).
"""

META = {
    "title": "The real danger is the gap BETWEEN two robots | E29",
    "channel": "This Week in AI",
    "speakers": "Jason Calacanis (host), Lon Harris (news), Gotham Nagi (Gatik), Russ D'Sa (LiveKit), Billy Craft (Path)",
    "date": "2026-09-03",
    "video_url": "https://www.youtube.com/watch?v=ajnooK4rNQU",
    "thread_line": "6 threads · OpenClaw 2.0's multiplayer bet, Gatik's $200M round vs. Waymo's bad week, Perplexity's local-Mac compute, Slack's enterprise moat, MCP for hardware, and whether Pangram actually catches AI writing",
    "category": "market",
}

SNAPSHOT = [
    "**OpenClaw 2.0** shipped after 933 contributors and 16,000+ code changes, betting on *multiplayer* agents you share with a team — panel calls it the General Magic/Palm Pilot to Grok's iPhone.",
    "**Gatik** raised a **$200 million Series D** a week ago and runs fully driverless trucks (no safety driver) across Texas, Arkansas and Phoenix for Pepsi and Kroger — even as Waymo had a rough week on camera.",
    "**Perplexity** launched *hybrid compute*: cloud handles reasoning, your own Apple Silicon Mac handles private data, and the local half is free.",
    "Salesforce's stock got a lift after Anthropic's Dario Amodei showed up on its earnings call for their joint enterprise-AI product.",
    "Anthropic released **MHS** (Model Hardware Standard), MCP's hardware-side cousin, so agents can safely operate robotic arms, lab gear and sensors.",
    "A Stanford Law professor's test of Pangram's AI-writing detector went viral: edit three sentences with Claude and it's flagged 20% AI; train Claude on your style and it's 100% AI — while MIT tells instructors not to trust these tools at all.",
    "Panelists are personally obsessed with Grok-built bots that design other bots, an assistant app called Instinct with worrying account access, and using Claude to design and 3D-print small robots and custom circuit boards.",
    "Recurring theme: the panel keeps returning to *who's responsible for the gap between agents* — between two robots, two Slack threads, or two companies' safety layers.",
]

THEMES = [
    {
        "id": "openclaw-multiplayer",
        "color": "amber",
        "badge": "Contested",
        "status": "RELEASED THIS WEEK",
        "title": "OpenClaw 2.0 bets everything on multiplayer agents",
        "lead": "OpenClaw rebuilt almost the entire product around one feature: teams sharing one agent without losing context.",
        "bullets": [
            "**933 people** and more than **16,000 code changes** went into OpenClaw 2.0 — Lon says that's about half of all the code ever written for the project, in one release",
            "It set out only to fix the install process and ended up rebuilding setup, browser app, memory, plugins and security",
            "Jason's analogy: OpenClaw may be the *General Magic* or *Palm Pilot* of this era — proved the concept (skills, personality, persistence) but Grok is the iPhone that's actually simple to use",
            "Russ and Billy both say their teams already run on Claude Co-work and Grok, and see multiplayer — not raw capability — as the real gap OpenClaw is chasing",
            "The same week: Slack's own team shipped Buzz (a collaborative agent product) and Slack Code — Russ calls OpenClaw 2.0's collaborative features \"a little bit Slack-like\"",
            "Jason frames a bigger split forming inside companies: business users automating work inside Slack vs. developers working in a code harness with \"an IRC chat bolted onto it\"",
        ],
        "quote": {"text": "They may be the general magic. They may be the Palm Pilot of the iPhone era.", "cite": "— Jason Calacanis"},
        "watch": "No one has actually solved multiplayer agents yet — this is the panel's read on OpenClaw 2.0's bet, not a verified result.",
        "names": None,
    },
    {
        "id": "gatik-waymo-jobs",
        "color": "amber",
        "badge": "Confirmed event",
        "status": "GATIK: OPERATING DRIVERLESS · WAYMO: INCIDENT ON CAMERA",
        "title": "Gatik's $200M round lands the same week Waymo has a bad one on camera",
        "lead": "Driverless trucking is live and funded, but the panel split hard on how fast — and how safely — the rest of autonomy scales.",
        "bullets": [
            "Gatik raised a **$200 million** Series D a week ago and runs fully driverless trucks — no safety driver — across Texas (Dallas), Arkansas and Phoenix, with regulatory clearance to commercialize in 29 states",
            "Long-time customers Pepsi (since 2022) and Kroger put their own logos on Gatik's trucks; Gatik is asset-light (leasing partners own the trucks) and runs two onboard models — a scene-representation model feeding a reasoning/planning model — on Nvidia hardware, gated by a separate deterministic safety layer that can veto any model output",
            "Jason plays footage of a Waymo clipping a car's fender at ~30mph (likely the other car's blind spot, not Waymo's fault) — on top of earlier incidents where a Waymo killed a cat and hit a child in Santa Monica, which forced an operational pause",
            "Jason's prediction: AV safety \"feels like it's going to be solved in 24 months,\" at which point self-driving will be undeniably safer than humans — but he pushes back hard when Gotham says driverless and human-driven trucks will coexist \"for decades,\" asking why that gap exists if the tech is already 10x safer",
            "Gotham's answer: the bottleneck isn't the technology, it's integrating with slow, traditional supply chains — physical AI's adoption curve is structurally different from digital AI's",
            "Jason's proposed fix for the coming jobs fight: require a paid human safety driver for a company's first 1 million rides / 10 million miles (roughly $20-40M to launch one city at ~$40/hr) — a bar only well-capitalized players like Uber, Neuro or Gatik could clear",
            "~10 million U.S. driving jobs across Uber, Lyft, DoorDash and trucking face real displacement pressure within 5 years, even though broad corporate AI layoffs haven't materialized yet; historical parallel raised — the tractor existed 50-60 years before it displaced farm labor at scale, once price and reliability caught up",
            "Timeline picks when put on the spot: Gotham says 5 years for highway-speed autonomous trucking but 15-20 years (maybe up to 50 for full capability) for home robots, since expectations for home robots are \"sky-high\"",
        ],
        "quote": {"text": "One small misstep can take the whole company down.", "cite": "— Gotham Nagi"},
        "watch": "The 24-months, 5-years and 15-50-years figures are the panel's own on-air predictions, not confirmed regulatory or company timelines.",
        "names": [
            {"name": "Gatik", "blurb": "Autonomous regional trucking; $200M Series D, fully driverless across TX/AR/AZ."},
            {"name": "PepsiCo", "blurb": "Long-term Gatik customer since 2022, logo on the trucks."},
            {"name": "Kroger", "blurb": "Gatik customer, logo on the trucks."},
            {"name": "Waymo", "blurb": "Robotaxi footage of a fender-clip incident plus prior cat/child incidents discussed on air."},
            {"name": "Tesla", "blurb": "Calacanis's FSD kept steering into his neighbor's driveway for a week before self-correcting; separate near-miss with a semi in an unmarked Austin construction zone."},
            {"name": "Uber", "blurb": "Cited as a driving-job category facing displacement pressure and as a well-capitalized player that could afford a phased safety-driver rollout."},
            {"name": "Lyft", "blurb": "Cited among driving-job categories facing displacement pressure."},
            {"name": "DoorDash", "blurb": "Cited among driving-job categories facing displacement pressure."},
        ],
    },
    {
        "id": "perplexity-hybrid-compute",
        "color": "green",
        "badge": "Confirmed event",
        "status": "LAUNCHED TODAY",
        "title": "Perplexity splits AI work between the cloud and your own Mac",
        "lead": "Hybrid compute sends reasoning to the cloud and keeps your private files on your own Apple Silicon hardware — for free.",
        "bullets": [
            "Perplexity's hybrid compute splits a single task: the cloud handles research/reasoning while a local model on your Mac processes your own private files before anything leaves the machine",
            "Requires an Apple Silicon Mac with at least **24GB** of unified memory; an on-device classifier redacts names, addresses and account numbers before any data leaves the device, and anything the local model handles costs zero cloud credits",
            "A report cited on the show says OpenAI bought 10,000 Mac minis and studios, contributing to a 3-month product delay",
            "Apple's new CEO, John Ternus, posted his first tweet as CEO — just \"hello\" — which Jason takes as vindication of his own two-year-old call that Apple would be AI's \"sleeper\"",
            "Panel's enterprise read: unmetered local tokens remove the internal fear of being \"the person who blew off $5,000 in tokens\" — and CFOs may buy developers $12K-20K Mac Studios (M5, 256GB-1TB) if most of the workload shifts to a free local coding agent instead of paid cloud tools",
            "Tradeoff flagged: a large open-weight model that needs roughly 6 terabytes of memory to run in full only fits a Mac Studio in a quantized, less-capable form — though cheaper local tokens let you loop and verify more to compensate",
        ],
        "quote": {"text": "Today is the worst it's ever going to be.", "cite": "— Billy Craft"},
        "watch": None,
        "names": [
            {"name": "Perplexity", "blurb": "Launched hybrid cloud/local compute for Mac today."},
            {"name": "Apple", "blurb": "New CEO John Ternus's first tweet; Apple Silicon is the hardware hybrid compute depends on."},
            {"name": "OpenAI", "blurb": "Reportedly bought 10,000 Mac minis/studios, cited as a factor in a 3-month product delay."},
        ],
    },
    {
        "id": "slack-oracle",
        "color": "amber",
        "badge": "Structural critique",
        "status": "ONGOING",
        "title": "Slack is enterprise AI's default interface — and everything in it is being tracked",
        "lead": "Salesforce's Slack has a moat built from years of institutional memory, and Calacanis is building a decision-tracking \"Oracle\" on top of it.",
        "bullets": [
            "Salesforce's stock got a rebound after Anthropic's Dario Amodei appeared on its earnings call to talk up their joint enterprise-AI product",
            "Panel view: Slack is to enterprise AI what ChatGPT is to consumer AI — years of organizational history and real switching costs make it hard to displace, even against new entrants like Slack's own Buzz or Slack Code",
            "Calacanis moved his org to Slack Enterprise+ (~$45/user/month vs. a $15 base tier) specifically for full data access, and is building an internal \"Oracle\" bot meant to summarize every decision the organization makes, and why",
            "He tells his own team plainly that every email and Slack message on a work computer feeds the Oracle — and approvingly cites Zuckerberg's public stance that Meta tracks everything to make people more efficient",
            "His observed failure mode: real decisions often happen in private DM side-threads that never reach an AI-readable channel, so the highest-value data isn't where the AI can see it",
        ],
        "quote": None,
        "watch": None,
        "names": [
            {"name": "Salesforce", "blurb": "Stock rebound tied to Dario Amodei's earnings-call appearance for their joint AI product."},
            {"name": "Anthropic", "blurb": "CEO Dario Amodei appeared on Salesforce's earnings call."},
        ],
    },
    {
        "id": "mhs-physical-ai",
        "color": "green",
        "badge": "Confirmed event",
        "status": "MHS RELEASED THIS WEEK",
        "title": "MCP gets a hardware cousin, and the panel is already buying robots",
        "lead": "Anthropic's new hardware standard raises a real safety question: the danger sits in the gap between two agents, not inside either one.",
        "bullets": [
            "Anthropic released **MHS** (Model Hardware Standard), a safety-aware hardware-side complement to MCP that lets Claude and other agents discover and operate robotic arms, lab instruments, sensors and manufacturing equipment",
            "Panel's worry, echoing Daniel Suarez's 2011 novel *Daemon*: each agent can operate its own machine safely within its envelope, but the exploit surface sits in the handoff *between* devices — the same pattern as the real Hugging Face security incident referenced on the show",
            "Open question raised: do guardrails belong at the single-agent level, the fleet/swarm level, or the whole-system level — more deterministic guardrails are safer but may cap what the technology can actually do",
            "Gotham worked on Honda's ASIMO humanoid robot early in his career at the Honda Research Institute in Wako, Japan — using that as his reference point for how far physical AI has come since",
            "Panelists' current physical-AI purchases and experiments: Gotham is buying a Unitree robot dog plus a robotic arm and testing Nvidia's open-source \"Alpha Mayo2\" reasoning model; Billy uses Claude as a hardware design partner to spec small humanoid robots and export 3D-print-ready files; a friend now designs and orders custom circuit boards from Shenzhen for about $14 each via Claude with no EE background required",
        ],
        "quote": None,
        "watch": None,
        "names": [
            {"name": "Nvidia", "blurb": "Open-source \"Alpha Mayo2\" reasoning model being tested by Gatik's Gotham Nagi."},
            {"name": "Unitree", "blurb": "Robot-dog maker Gotham is planning to buy from, alongside a robotic arm."},
        ],
    },
    {
        "id": "pangram-watermarking",
        "color": "amber",
        "badge": "Contested",
        "status": "ONGOING DEBATE",
        "title": "Can Pangram actually catch AI writing — and should professors trust it?",
        "lead": "A viral test on a Stanford professor's own essay reignited the fight over whether AI-detection tools work at all.",
        "bullets": [
            "MIT's faculty AI committee told instructors not to rely on AI-writing detectors at all; separately, NYU testing found the US Constitution scored as human-written, but light copy-edits alone pushed detection scores up",
            "Viral test: Stanford Law professor Orin Kerr had Claude edit three sentences of his own article — Pangram flagged the page 20% AI; after training Claude on his personal writing style and having it draft fresh paragraphs, Pangram flagged the result 100% AI — \"It works folks. How much more evidence do you need?\"",
            "Split take on the panel: Billy is skeptical of detectors and prefers provenance tools instead — a signed revision history, or in-person work that can't be faked; Jason insists detectors work and accuses universities of running \"a giant scam\" by letting AI-written work slide",
            "Anthropic's proposed fix is output watermarking — arranging generated tokens so their own software can flag Claude-written text — but the panel questions its long-term reliability and whether embedding a watermark caps the model's expressive range",
            "Panel separately wants opt-in labeling for AI-generated video and images, prompted by a viral fake image (an entire film cast at the Super Bowl) that fooled Jason outright",
        ],
        "quote": None,
        "watch": "This is an active, unresolved argument on the show — detector accuracy claims here are quoted from the participants, not independently verified.",
        "names": None,
    },
]

TAKEAWAYS = [
    {"icon": "\U0001F916", "tag": "AI tools", "title": "Try a hybrid-compute setup (Perplexity on Apple Silicon) before assuming you need a bigger cloud AI budget"},
    {"icon": "\U0001F69A", "tag": "Robotics", "title": "Track Gatik's expansion beyond its 5 current markets as the clearest signal of driverless trucking's real pace"},
    {"icon": "\U0001F4AC", "tag": "Enterprise AI", "title": "Assume every message on a work Slack/computer can end up training or feeding an internal AI \"Oracle\" — write accordingly"},
    {"icon": "\U0001F393", "tag": "AI ethics", "title": "Don't lean on a single AI-detection score for high-stakes academic or hiring decisions — pair it with provenance evidence"},
    {"icon": "\U0001F527", "tag": "Hardware", "title": "Watch bespoke hardware (Claude-designed circuit boards, 3D-printed robot parts) as a cheap new prototyping path"},
]

RISKS = [
    "Several product and model names in this episode were garbled by auto-captions and left unresolved rather than guessed: the exact name of Salesforce and Anthropic's joint product (heard as \"Quad force salespropic\"), the specific open-weight coding models referenced (heard as \"Neotron,\" \"Laguna,\" and a company heard as \"Poolside\"), and the large model needing ~6TB of memory to run in full (heard as \"K3\"). Treat these as directionally correct, not verified proper nouns.",
    "Funding figures, customer counts, market counts and technical specs (Gatik's Series D size, market/state counts, Mac memory requirements) are quoted as stated in conversation by the guests, not independently verified against filings or press releases.",
    "Gotham Nagi is Gatik's own CEO discussing his company's safety record and business model — treat his safety and timeline claims as the company's own framing, not third-party audit results (an independent safety audit is mentioned but not detailed on-air).",
    "This episode's exclusive sponsor segment (PayPal) has been excluded from this brief entirely.",
]

HOT_TAKES = [
    {"take": "I think in 24 months we won't be talking about safety anymore. It would be just abundantly clear these things are literally 2, three, four times safer than humans.", "cite": "— Jason Calacanis", "why": "dated, numbered prediction about AV safety"},
    {"take": "If it's going to be 10 times safer, why would it take decades?", "cite": "— Jason Calacanis", "why": "on-air challenge to his own guest's timeline"},
    {"take": "These universities are all in a giant scam. They're charging $100,000 a year to these students who then don't have to write their actual work... It's all a freaking fraud.", "cite": "— Jason Calacanis", "why": "names an institution type and accuses it of fraud"},
    {"take": "I predicted this like two years ago that Apple would be the sleeper.", "cite": "— Jason Calacanis", "why": "claims credit for a specific past call now being tested"},
    {"take": "It depends on the application — for autonomous vehicles it's 5 years... home robots I'm more closer to 15, 20 years. I would put go as far as 50.", "cite": "— Gotham Nagi", "why": "numbered forecast an autonomy-company CEO is on the hook for"},
]

OTHER_NEWS = [
    {"icon": "\U0001F4B5", "title": "Calacanis's long-running bit: hand $2 and $50 bills to service workers before they've done anything, and you'll get upgraded 3 out of 4 times — a running gag this episode, not really an AI story", "tag": "Culture"},
]

GLOSSARY = [
    {"term": "MCP", "def": "Model Context Protocol — the standard AI agents use to interface with software tools and data sources."},
    {"term": "MHS", "def": "Model Hardware Standard — Anthropic's new safety-aware complement to MCP for agents operating physical equipment like robotic arms and lab instruments."},
    {"term": "Hybrid compute", "def": "Perplexity's split-execution approach: cloud handles reasoning, a local model on your own Mac handles private data, at no cloud-credit cost for the local half."},
    {"term": "Quantized model", "def": "A compressed version of a large AI model that runs on smaller local hardware at reduced capability versus the full cloud version."},
    {"term": "VLA model", "def": "Vision-Language-Action model — an AI model that reasons about visual input and language to produce physical actions, used in robotics."},
    {"term": "Asset-light model", "def": "A business structure where a company (like Gatik) doesn't own its physical assets (trucks) — leasing partners own them instead."},
    {"term": "Series D", "def": "A later-stage venture funding round, typically for companies with an established product scaling into new markets."},
]
