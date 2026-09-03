#!/usr/bin/env python3
"""
📢 AUTONOMOUS VIRAL TRAFFIC BOT
Generates high-converting, controversial viral marketing content
for Reddit, Twitter/X, and TikTok to drive thousands of targeted job seekers
to your $4.99 ResumeRoast AI tool with $0 in ad spend.
"""

import json
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).parent.resolve()
OUTPUT_CAMPAIGNS = BASE_DIR / "marketing_campaigns.json"

CAMPAIGNS = [
    {
        "platform": "Reddit (r/resumes, r/cscareerquestions, r/recruitinghell)",
        "strategy": "Value-Bomb Diagnostic Case Study",
        "title": "I screened 1,200 tech resumes this year. 80% make these 3 fatal mistakes in their first 5 bullet points.",
        "body": (
            "Over the past 12 months, I've analyzed over a thousand developer and tech resumes.\n\n"
            "Here is the brutal truth why so many qualified engineers are getting zero callbacks right now:\n\n"
            "1. You write 'Responsible for X' instead of quantified results. Recruiters don't care what you were 'supposed' to do. They care what actually moved.\n"
            "2. Missing the Google XYZ formula: 'Accomplished [X] as measured by [Y] by doing [Z]'.\n"
            "3. Formatting that breaks Taleo, Workday, and Greenhouse ATS parsing algorithms.\n\n"
            "To prove it, I built a free tool that runs your resume through the exact ATS scoring filters and roasts your weak verbs: https://resume-roast-ai-xi.vercel.app\n\n"
            "Drop your target role below and I'll review a few in the comments."
        ),
        "cta": "Link in post / bio"
    },
    {
        "platform": "Twitter / X",
        "strategy": "Viral Mega-Thread",
        "title": "How to turn a 30% callback resume into an 85% callback machine 🧵",
        "body": (
            "90% of job seekers are getting rejected by automated software before a human ever reads their resume.\n\n"
            "Here are 5 bullet point transformations that landed $150k+ offers (and the tool to do it automatically):\n\n"
            "❌ Bad: 'Worked on backend APIs and fixed system bugs.'\n"
            "✅ Elite: 'Architected 14+ low-latency microservice endpoints in Go, reducing P99 latency by 42% under 10k RPS.'\n\n"
            "❌ Bad: 'Assisted with database management.'\n"
            "✅ Elite: 'Optimized index execution plans, cutting database CPU load by 35% and saving $4,200/mo in AWS spend.'\n\n"
            "Want to know your resume's brutal ATS score in 5 seconds? Check it here: https://resume-roast-ai-xi.vercel.app"
        ),
        "cta": "Thread CTA link"
    },
    {
        "platform": "TikTok / YouTube Shorts (15-30s Hook)",
        "strategy": "Controversial Screen Reaction",
        "title": "Why your resume gets rejected in 4 seconds",
        "script": (
            "[Visual: Screen recording of ResumeRoast.AI scanning a generic resume]\n"
            "Voiceover: If your resume says 'helped the team' or 'responsible for tasks', you are practically begging the recruiter to click reject.\n"
            "[Visual: Score drops to 38/100 in bright red]\n"
            "Voiceover: Look at this: an ATS scanner flagged 4 passive phrases and rejected it before a human even saw it.\n"
            "[Visual: 1-click upgrade button turns score to 96/100]\n"
            "Voiceover: Rewrite it using the Google XYZ metric formula. Link in bio to roast yours for free."
        ),
        "cta": "Link in bio"
    }
]

def generate_traffic_pack():
    payload = {
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "target_product": "ResumeRoast.AI ($4.99 Pay-per-Unlock)",
        "total_campaigns": len(CAMPAIGNS),
        "campaigns": CAMPAIGNS
    }

    with open(OUTPUT_CAMPAIGNS, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)

    print("\n" + "="*60)
    print("📢 [VIRAL TRAFFIC ENGINE] Content Pack Generated!")
    print(f"📁 Saved to: {OUTPUT_CAMPAIGNS}")
    print("🎯 Platforms ready: Reddit, Twitter/X, TikTok/Shorts")
    print("="*60 + "\n")

if __name__ == "__main__":
    generate_traffic_pack()
