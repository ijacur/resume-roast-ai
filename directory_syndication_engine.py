#!/usr/bin/env python3
"""
🌐 DIRECTORY SYNDICATION & BACKLINK ACCELERATOR
Automates submission preparation for 20+ leading AI tool directories,
launch aggregators, and SaaS marketplaces to funnel free targeted organic traffic.
"""

import json
from pathlib import Path

BASE_DIR = Path(__file__).parent.resolve()
OUTPUT_JSON = BASE_DIR / "directory_submissions.json"
OUTPUT_HTML = BASE_DIR / "directory_launcher.html"

DIRECTORIES = [
    {
        "name": "Product Hunt",
        "category": "Top Tier Launch",
        "url": "https://www.producthunt.com/posts/new",
        "submission_type": "1-Click Web Submission",
        "traffic_potential": "High (5,000+ views)",
        "dofollow_backlink": True
    },
    {
        "name": "Toolify.ai",
        "category": "AI Directory (Top 1)",
        "url": "https://www.toolify.ai/submit",
        "submission_type": "Direct Submit",
        "traffic_potential": "High (2.4M monthly visits)",
        "dofollow_backlink": True
    },
    {
        "name": "Futurepedia",
        "category": "AI Aggregator",
        "url": "https://www.futurepedia.io/submit-tool",
        "submission_type": "Form Submit",
        "traffic_potential": "High (1.8M monthly visits)",
        "dofollow_backlink": True
    },
    {
        "name": "There's An AI For That (TAAFT)",
        "category": "AI Search Engine",
        "url": "https://theresanaiforthat.com/submit/",
        "submission_type": "Form Submit",
        "traffic_potential": "Very High (3.1M monthly visits)",
        "dofollow_backlink": True
    },
    {
        "name": "Microlaunch",
        "category": "Micro-SaaS Hub",
        "url": "https://microlaunch.net/submit",
        "submission_type": "Instant Listing",
        "traffic_potential": "Medium (Indie Buyers)",
        "dofollow_backlink": True
    },
    {
        "name": "TopAI.tools",
        "category": "AI Directory",
        "url": "https://topai.tools/submit",
        "submission_type": "Direct Submit",
        "traffic_potential": "Medium (500k monthly visits)",
        "dofollow_backlink": True
    },
    {
        "name": "AlternativeTo",
        "category": "Software Alternatives",
        "url": "https://alternativeto.net/software/add/",
        "submission_type": "Competitor Alternative Listing",
        "traffic_potential": "Very High (High Intent)",
        "dofollow_backlink": True
    },
    {
        "name": "BetaList",
        "category": "Startup Discovery",
        "url": "https://betalist.com/submit",
        "submission_type": "Curated Launch",
        "traffic_potential": "High (Early Adopters)",
        "dofollow_backlink": True
    },
    {
        "name": "Dang.ai",
        "category": "AI Tools Index",
        "url": "https://dang.ai/submit",
        "submission_type": "Instant Submit",
        "traffic_potential": "Medium (300k visits)",
        "dofollow_backlink": True
    },
    {
        "name": "Insidr.ai",
        "category": "AI Reviews & Tools",
        "url": "https://www.insidr.ai/submit-your-tool/",
        "submission_type": "Directory Review",
        "traffic_potential": "Medium (SEO Backlinks)",
        "dofollow_backlink": True
    },
    {
        "name": "StartupStash",
        "category": "SaaS Directory",
        "url": "https://startupstash.com/submit/",
        "submission_type": "Curated SaaS Index",
        "traffic_potential": "Medium (Founders & Tech)",
        "dofollow_backlink": True
    },
    {
        "name": "Launching Next",
        "category": "Trending Startups",
        "url": "https://www.launchingnext.com/submit/",
        "submission_type": "Free Listing",
        "traffic_potential": "Medium (150k visits)",
        "dofollow_backlink": True
    }
]

METADATA = {
    "product_name": "ResumeRoast.AI",
    "website_url": "https://resume-roast-ai-xi.vercel.app",
    "pricing_model": "Freemium / Pay-Per-Unlock ($4.99)",
    "tagline": "Beat ATS filters and 10x interview callbacks with instant AI resume roasting",
    "short_description": "ResumeRoast.AI is a privacy-first, client-side ATS diagnostic scanner that parses resumes locally with pdf.js, computes a 0-100 impact score, and rewrites passive bullets into executive-grade Google XYZ metrics in seconds.",
    "key_features": [
        "Instant in-browser PDF/DOCX parsing (zero server latency)",
        "Brutal 0-100 ATS scoring across impact, brevity, and keyword depth",
        "Google XYZ bullet rewriter transforming passive verbs into quantified wins",
        "Programmatic SEO funnels tailored for Software Engineers, PMs, and Data Analysts",
        "Frictionless checkout supporting Apple Pay, Google Pay, Cards, TRC20 USDT, and TON"
    ],
    "tags": ["AI", "Career", "Resume", "Job Search", "Productivity", "SaaS", "ATS Scanner"],
    "founder_telegram": "@jasurshukurov",
    "contact_email": "jasur@resumeroast.ai"
}

def generate_directory_assets():
    payload = {
        "metadata": METADATA,
        "directories": DIRECTORIES
    }

    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)

    # Build interactive HTML launcher
    html = f"""<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <meta charset="UTF-8">
  <title>🚀 AI Directory Syndication Launcher | ResumeRoast.AI</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;700;800&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
  <style>body {{ font-family: 'Plus Jakarta Sans', sans-serif; }}</style>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen p-6">
  <div class="max-w-5xl mx-auto space-y-6">
    <div class="flex justify-between items-center border-b border-slate-800 pb-4">
      <div>
        <h1 class="text-2xl font-black text-white flex items-center gap-2">
          🚀 AI Directory Syndication Hub <span class="text-xs px-2.5 py-0.5 rounded-full bg-emerald-500/20 text-emerald-400 font-bold border border-emerald-500/30">{len(DIRECTORIES)} DIRECTORIES READY</span>
        </h1>
        <p class="text-xs text-slate-400 mt-1">Submit ResumeRoast.AI to top AI search engines and aggregator platforms for instant organic backlinks and user signups.</p>
      </div>
      <button onclick="copyAllMetadata()" class="px-4 py-2 bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 text-white rounded-xl text-xs font-bold transition flex items-center gap-1.5 shadow-lg shadow-emerald-600/20">
        <i class="fa-solid fa-copy"></i> Copy Full Submission Pack
      </button>
    </div>

    <!-- Metadata Quick-Copy Cards -->
    <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 bg-slate-900/60 p-4 rounded-2xl border border-slate-800">
      <div>
        <span class="text-[10px] font-bold text-slate-400 uppercase tracking-wider">Product Name</span>
        <div class="flex items-center justify-between mt-1 bg-slate-950 p-2 rounded-lg border border-slate-800">
          <span class="text-xs font-mono text-white">{METADATA['product_name']}</span>
          <button onclick="copyText('{METADATA['product_name']}')" class="text-slate-400 hover:text-emerald-400 text-xs"><i class="fa-solid fa-copy"></i></button>
        </div>
      </div>
      <div class="sm:col-span-2">
        <span class="text-[10px] font-bold text-slate-400 uppercase tracking-wider">Tagline</span>
        <div class="flex items-center justify-between mt-1 bg-slate-950 p-2 rounded-lg border border-slate-800">
          <span class="text-xs font-mono text-emerald-300 truncate mr-2">{METADATA['tagline']}</span>
          <button onclick="copyText('{METADATA['tagline']}')" class="text-slate-400 hover:text-emerald-400 text-xs shrink-0"><i class="fa-solid fa-copy"></i></button>
        </div>
      </div>
      <div class="sm:col-span-3">
        <span class="text-[10px] font-bold text-slate-400 uppercase tracking-wider">Description (Optimized for AI Directory Approval)</span>
        <div class="flex items-start justify-between mt-1 bg-slate-950 p-2.5 rounded-lg border border-slate-800">
          <p class="text-xs text-slate-300 mr-2">{METADATA['short_description']}</p>
          <button onclick="copyText('{METADATA['short_description']}')" class="text-slate-400 hover:text-emerald-400 text-xs shrink-0 mt-0.5"><i class="fa-solid fa-copy"></i></button>
        </div>
      </div>
    </div>

    <!-- Directory Submission Grid -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
      {"".join([f'''
        <div class="bg-slate-900/80 border border-slate-800 hover:border-slate-700 p-4 rounded-2xl flex justify-between items-center gap-3 transition">
          <div class="space-y-1">
            <div class="flex items-center gap-2">
              <h3 class="text-sm font-bold text-white">{d['name']}</h3>
              <span class="text-[10px] px-2 py-0.5 rounded bg-slate-800 text-slate-400">{d['category']}</span>
              <span class="text-[10px] px-2 py-0.5 rounded bg-emerald-500/10 text-emerald-400 font-mono">DOFOLLOW</span>
            </div>
            <p class="text-[11px] text-slate-400">{d['traffic_potential']}</p>
          </div>
          <button onclick="submitDirectory('{d['url']}')" class="px-3.5 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-xs rounded-xl shadow-lg shadow-indigo-600/20 transition flex items-center gap-1.5 shrink-0">
            <span>Open & Submit</span>
            <i class="fa-solid fa-arrow-up-right-from-square text-[10px]"></i>
          </button>
        </div>
      ''' for d in DIRECTORIES])}
    </div>
  </div>

  <script>
    const pack = {json.dumps(METADATA)};

    function copyText(txt) {{
      navigator.clipboard.writeText(txt);
      alert('Copied to clipboard!');
    }}

    function copyAllMetadata() {{
      const text = `Product Name: ${{pack.product_name}}\\nURL: ${{pack.website_url}}\\nTagline: ${{pack.tagline}}\\n\\nDescription:\\n${{pack.short_description}}\\n\\nPricing: ${{pack.pricing_model}}\\nTags: ${{pack.tags.join(', ')}}`;
      navigator.clipboard.writeText(text);
      alert('✅ Complete Directory Submission Pack copied to clipboard!');
    }}

    function submitDirectory(url) {{
      copyAllMetadata();
      window.open(url, '_blank');
    }}
  </script>
</body>
</html>"""

    with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"✅ Generated {len(DIRECTORIES)} directory launch configurations into {OUTPUT_HTML}!")

if __name__ == "__main__":
    generate_directory_assets()
