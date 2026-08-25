META = {
    "title": "Why Most Devs Stop Improving",
    "channel": "CodeHead",
    "speakers": "CodeHead (solo creator)",
    "date": "2026-07-28",
    "video_url": "https://www.youtube.com/watch?v=8hLMqx-KS8w",
    "thread_line": "3 threads · stack loyalty as a hiding spot, tenure-based promotion killing growth incentives, and AI dependency eroding fundamental skills",
    "category": "dev",
}

SNAPSHOT = [
    "Solo dev-career essay arguing most developers quietly stop improving through three sneaky, individually 'productive-feeling' habits rather than one dramatic failure.",
    "Habit 1: clinging to one familiar stack (his own example: Spring Boot + Angular) as an identity/hiding spot rather than a deliberate choice.",
    "Habit 2: mistaking 'the way we've always done it' for expertise — enabled by companies that promote on tenure more than range or curiosity.",
    "Habit 3: inability to function without AI assistance — cites (unnamed) research that devs who lean on AI heavily perform worse once it's removed, because struggle is where learning happens.",
    "Unifying thesis: all three are 'friction avoidance in a hoodie' — growth lives specifically in the friction people are avoiding.",
    "Explicit non-anti-AI disclaimer: he uses Claude Code daily and isn't asking viewers to abandon AI tools, just to notice when a tool has replaced thinking rather than accelerated it.",
]

THEMES = [
    {
        "id": "stack-as-hiding-spot",
        "color": "amber",
        "badge": "Self-critique, since resolved",
        "status": "PERSONAL ADMISSION",
        "title": "Habit #1: loyalty to one tech stack, dressed up as valuing 'structure'",
        "lead": "The creator admits his years-long refusal to touch React or Go wasn't really about preferring convention — it was fear of looking like a beginner in front of people who already rated him as good.",
        "bullets": [
            "He describes being 'Spring Boot and Angular, full stop, no exceptions' early in his career, and dismissing React or Go whenever colleagues raised them.",
            "His own retrospective diagnosis: the real driver wasn't technical judgment, it was fear of feeling like a beginner again in front of people who already thought he was good at his job.",
            "He still reaches for Spring Boot and Angular most often today — the habit itself didn't disappear, only its function changed: it's now a deliberate choice for the right project, not a hiding spot that 'wrecks his whole week' when challenged.",
        ],
        "quote": {
            "text": "What changed is that it's a choice now instead of a hiding spot.",
            "cite": "— CodeHead",
        },
        "watch": None,
        "names": None,
    },
    {
        "id": "tenure-vs-growth",
        "color": "red",
        "badge": "Structural / incentive critique",
        "status": "SYSTEMIC, NOT INDIVIDUAL FAULT",
        "title": "Habit #2: mistaking 'how we've always done it' for expertise — because companies reward tenure, not range",
        "lead": "The video's sharpest claim is structural: the senior dev who solves every problem exactly as they did in year one isn't lazy so much as correctly reading their company's actual incentives.",
        "bullets": [
            "Archetype named: 'that one senior dev who's technically been senior for 6 years, but still solves every single problem exactly the way he did in year one' — his 'senior position is basically a rerun with better pay.'",
            "Root cause per the creator: companies promote based on tenure far more often than on range or curiosity, so comfort gets rewarded and growth doesn't, not directly — meaning nobody in that system is actually incentivized to leave the loop they're in.",
            "Framed explicitly as barely the individual's fault — a systemic/organizational problem, not a personal character flaw.",
        ],
        "quote": {
            "text": "Comfortable gets rewarded in most orgs. Growth just doesn't, not directly anyway.",
            "cite": "— CodeHead",
        },
        "watch": "No source or data is cited for the tenure-vs-range promotion claim — it's presented as the creator's own read of common industry behavior, not a study.",
        "names": None,
    },
    {
        "id": "ai-dependency-atrophy",
        "color": "red",
        "badge": "Skill-atrophy warning",
        "status": "CITES RESEARCH, BUT UNNAMED/UNLINKED",
        "title": "Habit #3: outsourcing the struggle to AI outsources the growth that comes with it",
        "lead": "Not an anti-AI take — the creator uses Claude Code daily — but a warning that reaching for AI before attempting a problem yourself quietly erodes the exact skills that make you valuable.",
        "bullets": [
            "Illustrative anecdote: asking a developer to reverse a linked list with no AI tool open makes them 'short circuit like you just asked them to do their taxes by hand with no calculator' — the creator admits reacting the same way when a colleague asked him cold.",
            "Cites 'actual research now showing that developers who lean on AI assistance heavily tend to perform worse the moment it's taken away' — no study, author, or publication is named or linked in the video.",
            "His causal claim: the underperformance isn't because heavy AI users are less capable, but because the struggle itself was where the learning was happening — 'you can't outsource struggle without also outsourcing the growth attached to it.'",
            "Explicit disclaimer to preempt an anti-AI read: he is not telling viewers to boycott AI tools or 'go back to coding like it's 2008'; Claude Code, Cursor, and Codex are called out by name as good tools that are simply 'not the bottleneck anymore.'",
        ],
        "quote": {
            "text": "You can't outsource struggle without also outsourcing the growth attached to it.",
            "cite": "— CodeHead",
        },
        "watch": "The 'developers perform worse once AI is removed' research claim is unsourced in the video — treat as an assertion, not a verified citation, until you can locate the underlying study.",
        "names": None,
    },
]

TAKEAWAYS = [
    {"icon": "\U0001F6E0️", "tag": "Stack", "title": "Deliberately touch one tool or framework you've been avoiding for non-technical reasons — notice if the resistance is judgment or just discomfort."},
    {"icon": "\U0001F9E9", "tag": "Problem-solving", "title": "Before opening an AI assistant on your next problem, spend a fixed few minutes attempting it yourself first — the struggle is reportedly where the retained learning happens."},
    {"icon": "\U0001F4CA", "tag": "Career", "title": "If you're the senior dev solving everything the same way as year one, treat that as a structural incentive signal to investigate, not just a personal failing to feel bad about."},
    {"icon": "\U0001F50D", "tag": "Research", "title": "Track down the actual study behind the 'AI reliance degrades unaided performance' claim before citing it yourself — this video doesn't name it."},
]

RISKS = [
    "The central 'research shows heavy AI users perform worse without it' claim is asserted without naming a study, author, or publication — treat as an unverified claim pending a source.",
    "This is a single creator's personal essay/opinion piece based on self-reported anecdotes (his own career, one colleague's reaction) rather than data across a broader developer population.",
    "Auto-generated captions on a short, fast-paced solo video can occasionally mangle proper nouns or phrasing — cross-check exact wording against the video if quoting directly.",
]

HOT_TAKES = [
    {"take": "You can't outsource struggle without also outsourcing the growth attached to it.",
     "cite": '— CodeHead', "why": 'From a daily Claude Code user — not an anti-AI take, a warning about reaching for it first.'},
    {"take": "Comfortable gets rewarded in most orgs. Growth just doesn't, not directly anyway.",
     "cite": '— CodeHead', "why": 'Makes stagnation a structural incentive problem rather than a personal failing.'},
    {"take": "What changed is that it's a choice now instead of a hiding spot.",
     "cite": '— CodeHead', "why": 'Admits his years-long refusal to touch React or Go was fear of looking like a beginner, not principle.'},
    {"take": "The senior dev solving every problem exactly as they did in year one is correctly reading their company's incentives.",
     "cite": '— CodeHead', "why": "The video's sharpest claim, and the least flattering to the companies employing those devs."},
]

OTHER_NEWS = []

GLOSSARY = []
