#!/usr/bin/env python3
"""
🚀 PROGRAMMATIC SEO ENGINE FOR RESUMEROAST.AI
Generates role-specific landing pages for top high-ticket tech professions
with custom ATS keywords, pre-loaded role CVs, and schema metadata.
"""

import json
from pathlib import Path

BASE_DIR = Path(__file__).parent.resolve()
PUBLIC_DIR = BASE_DIR / "public"
ROLES_DIR = BASE_DIR / "roles"
ROLES_DIR.mkdir(exist_ok=True)

ROLE_DATA = [
    {
        "slug": "software-engineer",
        "title": "Software Engineer Resume Roast & ATS Scanner",
        "h1": "Software Engineer Resumes Get Discarded in 3.8 Seconds.",
        "sub": "Greenhouse and Lever filter out 76% of developer CVs that lack quantified backend performance metrics.",
        "target_role": "Senior Software Engineer",
        "keywords": ["Distributed Systems", "P99 Latency", "Microservices", "CI/CD", "Go", "Python", "Kubernetes", "PostgreSQL"],
        "sample_cv": (
            "Senior Backend Developer at Apex Tech (2022-2025)\n"
            "- Responsible for maintaining backend microservices and fixing database bugs.\n"
            "- Helped the team deploy Docker containers to Kubernetes clusters.\n"
            "- Worked on REST API endpoints and assisted front-end developers.\n"
            "- Handled code reviews and attended daily agile standups.\n"
            "- Assisted with monitoring server logs and incident management."
        )
    },
    {
        "slug": "product-manager",
        "title": "Product Manager Resume Roast | Beat Workday ATS Filters",
        "h1": "Product Manager Resumes Lack Revenue Impact.",
        "sub": "Hiring managers reject PMs who list feature launches without proving retention, ARR growth, or cohort engagement.",
        "target_role": "Senior Product Manager",
        "keywords": ["Product Strategy", "ARR Growth", "User Retention", "Cohort Analysis", "PRDs", "A/B Testing", "GTM Execution"],
        "sample_cv": (
            "Product Manager at CloudScale Inc (2021-2024)\n"
            "- Responsible for managing the roadmap and backlog for mobile onboarding.\n"
            "- Worked with designers and engineers to launch 4 new feature updates.\n"
            "- Attended customer feedback interviews and created product requirement docs.\n"
            "- Helped improve user conversion rates through UX experimentation.\n"
            "- Coordinated sprint planning and weekly stakeholder demos."
        )
    },
    {
        "slug": "data-scientist",
        "title": "Data Scientist & ML Engineer Resume Roast",
        "h1": "Data Science Resumes Read Like Academic Homework.",
        "sub": "Enterprise recruiters discard ML candidates whose resumes don't quantify model inference latency and business ROI.",
        "target_role": "Lead Data Scientist / ML Engineer",
        "keywords": ["PyTorch", "ROC-AUC", "Feature Engineering", "ETL Pipelines", "Model Inference", "MLOps", "A/B Experimentation"],
        "sample_cv": (
            "Data Scientist at Insight Labs (2022-2025)\n"
            "- Worked on machine learning models for customer churn prediction.\n"
            "- Responsible for exploratory data analysis using Pandas and Seaborn.\n"
            "- Assisted senior data scientists in cleaning data and training neural nets.\n"
            "- Evaluated model accuracy using cross-validation and confusion matrices.\n"
            "- Did data visualization dashboards using Streamlit and Tableau."
        )
    },
    {
        "slug": "devops-cloud-architect",
        "title": "DevOps & Cloud Engineer Resume Roast | ATS Optimizer",
        "h1": "DevOps Resumes Forget Uptime & Cloud Cost Savings.",
        "sub": "Automated filters reject infrastructure engineers who don't list cost reduction dollars or 99.99% uptime proof.",
        "target_role": "Senior DevOps / Cloud Architect",
        "keywords": ["Terraform", "AWS / GCP", "Zero-Downtime CI/CD", "FinOps Savings", "Kubernetes", "Prometheus", "SOC2 Compliance"],
        "sample_cv": (
            "DevOps Engineer at InfraCore (2021-2024)\n"
            "- Responsible for managing AWS cloud infrastructure and EC2 instances.\n"
            "- Helped team configure Jenkins pipelines for continuous delivery.\n"
            "- Worked on Terraform scripts to provision virtual networks.\n"
            "- Did system monitoring using Grafana and handled on-call alerts.\n"
            "- Assisted with security patching and cloud backup configurations."
        )
    },
    {
        "slug": "cybersecurity-analyst",
        "title": "Cybersecurity & InfoSec Resume Roast | Beat Enterprise ATS",
        "h1": "Cybersecurity Resumes Get Flagged for Lack of Incident Metrics.",
        "sub": "Enterprise security screeners reject SecOps candidates who don't list MTTR reduction, zero breach records, and vulnerability remediation volume.",
        "target_role": "Senior Cybersecurity / SecOps Analyst",
        "keywords": ["SIEM / SOC", "Vulnerability Management", "SOC2 / ISO 27001", "Threat Hunting", "MTTR Reduction", "Zero-Trust", "Penetration Testing"],
        "sample_cv": (
            "Cybersecurity Analyst at SecureSphere (2022-2025)\n"
            "- Responsible for monitoring SOC alerts and firewall logs.\n"
            "- Assisted senior team in incident response and threat analysis.\n"
            "- Worked on vulnerability scanning with Nessus and Qualys.\n"
            "- Helped prepare documentation for annual compliance audits.\n"
            "- Attended daily standups and handled user access requests."
        )
    },
    {
        "slug": "blockchain-web3-developer",
        "title": "Blockchain & Web3 Developer Resume Roast | Smart Contract ATS",
        "h1": "Web3 Resumes Lack Provable TVL & Gas Optimization Metrics.",
        "sub": "Crypto protocols reject Solidity engineers who don't prove zero-hack contract deployments and gas-optimized EVM bytecode.",
        "target_role": "Senior Smart Contract / Web3 Engineer",
        "keywords": ["Solidity", "EVM Assembly (Yul)", "DeFi Protocols", "Reentrancy Protection", "Gas Optimization", "Foundry / Hardhat", "TVL Secured"],
        "sample_cv": (
            "Smart Contract Developer at DecentralLabs (2022-2025)\n"
            "- Responsible for writing Solidity contracts for token staking.\n"
            "- Helped test contracts using Hardhat and TypeScript.\n"
            "- Worked on frontend integration with Ethers.js and Wagmi.\n"
            "- Assisted with smart contract security audit preparation.\n"
            "- Handled bug fixes for decentralized exchange interface."
        )
    },
    {
        "slug": "machine-learning-engineer",
        "title": "AI & Machine Learning Engineer Resume Roast | MLOps ATS",
        "h1": "AI/ML Resumes Are Getting Auto-Rejected for Lacking Latency SLAs.",
        "sub": "Tech giants reject AI engineers who only list model training without proving sub-50ms inference latency, quantization, and GPU cost cuts.",
        "target_role": "Senior MLOps & LLM Systems Engineer",
        "keywords": ["vLLM / TensorRT", "LoRA Fine-Tuning", "P95 Inference Latency", "Model Quantization", "CUDA / PyTorch", "RAG Pipelines", "GPU Optimization"],
        "sample_cv": (
            "Machine Learning Engineer at NeuralCore (2022-2025)\n"
            "- Responsible for fine-tuning open-source LLMs on proprietary data.\n"
            "- Helped deploy models to cloud servers using Docker.\n"
            "- Worked on prompt engineering and RAG pipeline setup.\n"
            "- Assisted with data preprocessing and vector embeddings.\n"
            "- Monitored model outputs and evaluated response quality."
        )
    },
    {
        "slug": "fullstack-react-developer",
        "title": "Fullstack React & Next.js Developer Resume Roast | ATS Scanner",
        "h1": "Fullstack Resumes List 'HTML/CSS' Instead of Core Web Vitals.",
        "sub": "Hiring managers instantly skip developers who list generic tech stacks without proving Lighthouse 95+ performance and conversion uplifts.",
        "target_role": "Senior Fullstack Engineer (React / Next.js / Node)",
        "keywords": ["Next.js App Router", "Server Components (RSC)", "Lighthouse 95+", "GraphQL / tRPC", "PostgreSQL / Prisma", "Tailwind CSS", "Core Web Vitals"],
        "sample_cv": (
            "Fullstack Developer at VelocityApps (2022-2025)\n"
            "- Responsible for building UI components in React and Tailwind.\n"
            "- Helped backend engineers develop REST APIs in Express.\n"
            "- Worked on responsive mobile layouts and fixed styling bugs.\n"
            "- Assisted with database migrations and Prisma schema updates.\n"
            "- Attended daily agile standups and completed Jira tickets."
        )
    },
    {
        "slug": "financial-analyst",
        "title": "Financial Analyst & Investment Banking Resume Roast | ATS Scanner",
        "h1": "Finance Resumes Fail Without Quantified P&L and Modeling Precision.",
        "sub": "Goldman Sachs, Morgan Stanley, and corporate finance ATS filter out 82% of analyst CVs lacking DCF modeling, variance analysis, and ROI metrics.",
        "target_role": "Senior Financial Analyst / Corporate Finance",
        "keywords": ["DCF Modeling", "Variance Analysis", "EBITDA Growth", "CapEx Forecasting", "SQL / Tableau", "3-Statement Models", "M&A Diligence"],
        "sample_cv": (
            "Financial Analyst at Capital Corp (2022-2025)\n"
            "- Responsible for monthly financial reporting and budget updates.\n"
            "- Helped senior associates build quarterly Excel spreadsheets.\n"
            "- Analyzed financial variance and attended executive meetings.\n"
            "- Prepared PowerPoint slides for board presentations."
        )
    },
    {
        "slug": "ui-ux-designer",
        "title": "UI/UX Product Designer Resume Roast | Beat Design ATS Filters",
        "h1": "Design Resumes Show Dribbble Visuals Instead of Conversion Impact.",
        "sub": "Design directors skip portfolios that do not prove design system governance, user research retention lifts, and accessibility standards.",
        "target_role": "Senior UI/UX Product Designer",
        "keywords": ["Design Systems", "WCAG 2.2 AA", "User Research", "Figma Auto-Layout", "Conversion Uplift", "Prototyping", "Information Architecture"],
        "sample_cv": (
            "Product Designer at CreativeStudio (2022-2025)\n"
            "- Responsible for creating Figma mockups and wireframes.\n"
            "- Collaborated with developers to implement UI designs.\n"
            "- Worked on user research interviews and usability testing.\n"
            "- Designed marketing graphics and social media assets."
        )
    },
    {
        "slug": "registered-nurse",
        "title": "Registered Nurse (RN) & Healthcare Resume Roast | Hospital ATS Scanner",
        "h1": "Hospital ATS Rejects Clinical CVs Lacking Critical Care Certifications.",
        "sub": "Healthcare recruitment algorithms automatically reject nursing resumes missing BLS/ACLS protocols, patient load ratios, and EHR compliance.",
        "target_role": "Registered Nurse (RN) - Acute & Critical Care",
        "keywords": ["Patient Load 1:4", "BLS / ACLS Certified", "Epic / Cerner EHR", "Triage Assessment", "Medication Administration", "Infection Control"],
        "sample_cv": (
            "Registered Nurse at Metro Health (2022-2025)\n"
            "- Responsible for patient bedside care and vital sign monitoring.\n"
            "- Administered medications and updated patient charts in Epic.\n"
            "- Communicated with physicians regarding treatment plans.\n"
            "- Assisted patients with daily recovery activities."
        )
    },
    {
        "slug": "digital-marketing-growth",
        "title": "Growth Marketer & Performance Ads Resume Roast | Beat ATS Filters",
        "h1": "Marketer Resumes List 'Brand Awareness' Instead of Proven CAC/ROAS.",
        "sub": "CMOs and recruitment ATS algorithms filter out digital marketers who fail to quantify customer acquisition costs, blended ROAS, and pipeline ARR.",
        "target_role": "Head of Growth / Performance Marketing Specialist",
        "keywords": ["Blended CAC", "ROAS > 3.8x", "Paid Search & Social", "Google Analytics 4", "Cohort Retention", "HubSpot Automation", "Conversion Rate (CRO)"],
        "sample_cv": (
            "Digital Marketing Specialist at ScaleMedia (2022-2025)\n"
            "- Responsible for managing Meta and Google Ads ad spend.\n"
            "- Helped write ad copy and test marketing creative.\n"
            "- Analyzed campaign performance metrics in Google Analytics.\n"
            "- Organized email newsletters and social media posting."
        )
    },
    {
        "slug": "project-manager-scrum",
        "title": "Agile Scrum Master & Technical PM Resume Roast | ATS Scanner",
        "h1": "PM Resumes List 'Daily Standups' Instead of On-Time Delivery Velocity.",
        "sub": "Enterprise tech ATS filters reject project managers who document ceremony meetings without demonstrating sprint velocity increases and risk mitigation.",
        "target_role": "Senior Technical Project Manager / Scrum Master",
        "keywords": ["Sprint Velocity +35%", "CSM / PMP", "Jira Architecture", "Scope Risk Mitigation", "Stakeholder Alignment", "Budget Compliance", "CI/CD Deployment"],
        "sample_cv": (
            "Project Manager at CloudSystems (2022-2025)\n"
            "- Responsible for facilitating daily agile standups and sprint planning.\n"
            "- Created Jira tickets and managed team task boards.\n"
            "- Communicated project status updates to senior leadership.\n"
            "- Helped team resolve blockers and coordinate releases."
        )
    },
    {
        "slug": "sales-account-executive",
        "title": "Enterprise B2B Account Executive Resume Roast | Sales ATS Scanner",
        "h1": "Sales Resumes List 'Pipeline Activities' Instead of Quota Attainment.",
        "sub": "VPs of Sales instantly discard AE resumes that do not prominently state quota percentage attainment, average contract value (ACV), and win rates.",
        "target_role": "Enterprise SaaS Account Executive (AE)",
        "keywords": ["140% Quota Attainment", "$85k ACV", "MEDDPICC Qualification", "Salesforce CRM", "Outbound Pipeline", "Executive Multi-Threading", "Enterprise Closes"],
        "sample_cv": (
            "Account Executive at TechSaaS (2022-2025)\n"
            "- Responsible for closing new business deals and demoing software.\n"
            "- Managed sales opportunities in Salesforce CRM.\n"
            "- Conducted discovery calls and negotiated pricing terms.\n"
            "- Attended trade show events and followed up with inbound leads."
        )
    }
]

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | ResumeRoast.AI</title>
  <meta name="description" content="{sub}">
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
  <style>
    body {{ font-family: 'Plus Jakarta Sans', sans-serif; }}
    .mono {{ font-family: 'JetBrains Mono', monospace; }}
    .glass {{ background: rgba(15, 23, 42, 0.75); backdrop-filter: blur(16px); border: 1px solid rgba(255, 255, 255, 0.08); }}
  </style>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen selection:bg-rose-500 selection:text-white">
  
  <nav class="border-b border-slate-800 bg-slate-900/50 backdrop-blur sticky top-0 z-40">
    <div class="max-w-5xl mx-auto px-4 py-3.5 flex justify-between items-center">
      <a href="/" class="flex items-center space-x-2.5">
        <div class="w-8 h-8 rounded-xl bg-gradient-to-tr from-rose-500 to-amber-500 flex items-center justify-center text-white font-black text-sm shadow-lg shadow-rose-500/20">🔥</div>
        <span class="font-extrabold text-base tracking-tight text-white">ResumeRoast<span class="text-rose-500">.AI</span></span>
      </a>
      <div class="flex items-center gap-3">
        <span class="text-xs text-rose-400 font-mono font-bold px-2 py-0.5 rounded bg-rose-500/10 border border-rose-500/20">{target_role} Edition</span>
      </div>
    </div>
  </nav>

  <header class="max-w-4xl mx-auto px-4 pt-12 pb-6 text-center space-y-3">
    <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-rose-500/10 border border-rose-500/20 text-rose-400 text-xs font-bold uppercase tracking-wider">
      <span class="w-2 h-2 rounded-full bg-rose-500 animate-pulse"></span> ATS Diagnostic for {target_role}s
    </div>
    <h1 class="text-3xl sm:text-5xl font-black text-white tracking-tight leading-tight">
      {h1}<br>
      <span class="text-transparent bg-clip-text bg-gradient-to-r from-rose-400 via-amber-300 to-indigo-400">Roast it before the hiring manager does.</span>
    </h1>
    <p class="text-sm sm:text-base text-slate-400 max-w-2xl mx-auto">{sub}</p>

    <!-- Essential Keywords Tag Cloud -->
    <div class="pt-4 flex flex-wrap justify-center gap-2 max-w-2xl mx-auto">
      <span class="text-[11px] font-bold text-slate-500 uppercase tracking-wider self-center mr-1">Must-Have ATS Keywords:</span>
      {keyword_badges}
    </div>
  </header>

  <main class="max-w-4xl mx-auto px-4 pb-20 space-y-6">
    <div class="glass p-6 sm:p-8 rounded-3xl space-y-5 shadow-2xl border-slate-800">
      <div class="flex justify-between items-center border-b border-slate-800 pb-3">
        <span class="text-xs font-bold uppercase text-slate-400 tracking-wider">Target Position: <strong class="text-white">{target_role}</strong></span>
        <button onclick="loadSample()" class="text-xs text-indigo-400 hover:text-indigo-300 font-semibold transition flex items-center gap-1">
          <i class="fa-solid fa-wand-magic-sparkles"></i> Load Weak {target_role} Sample
        </button>
      </div>

      <textarea id="resumeInput" rows="8" class="w-full bg-slate-900/90 border border-slate-700/80 p-4 rounded-2xl text-xs text-slate-200 focus:outline-none focus:border-rose-500 transition leading-relaxed mono">{sample_cv}</textarea>

      <button onclick="roastResume()" id="btnRoast" class="w-full py-4 rounded-2xl bg-gradient-to-r from-rose-600 via-orange-600 to-amber-600 hover:from-rose-500 hover:to-amber-500 text-white font-extrabold text-sm tracking-wide shadow-xl shadow-rose-600/20 transition flex items-center justify-center gap-2">
        <i class="fa-solid fa-fire text-base"></i> SCAN ATS REJECTION PROBABILITY (FREE)
      </button>

      <!-- Diagnostic Results Box -->
      <div id="resultsBox" class="hidden space-y-4 pt-4 border-t border-slate-800 animate-fade-in">
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
          <div class="p-4 rounded-xl bg-slate-900 border border-rose-500/30 text-center">
            <p class="text-[10px] uppercase font-bold text-slate-400">ATS Score</p>
            <p id="atsScore" class="text-4xl font-black text-rose-500 mt-1">38<span class="text-xs text-slate-500">/100</span></p>
          </div>
          <div class="p-4 rounded-xl bg-slate-900 border border-amber-500/30 text-center">
            <p class="text-[10px] uppercase font-bold text-slate-400">Rejection Risk</p>
            <p id="rejectRisk" class="text-4xl font-black text-amber-400 mt-1">72%</p>
          </div>
          <div class="p-4 rounded-xl bg-slate-900 border border-indigo-500/30 text-center">
            <p class="text-[10px] uppercase font-bold text-slate-400">Verdict</p>
            <p class="text-xs font-black text-rose-400 mt-3 uppercase tracking-wide" id="verdictText">Bot Discard</p>
          </div>
        </div>

        <div class="p-4 rounded-xl bg-rose-500/10 border border-rose-500/20 text-rose-200 text-xs leading-relaxed" id="roastText">
        </div>

        <!-- 1-Click Paywall -->
        <div class="p-6 rounded-2xl bg-gradient-to-b from-slate-900 to-slate-950 border-2 border-indigo-500/40 text-center space-y-4 shadow-2xl">
          <div>
            <span class="px-3 py-0.5 rounded-full bg-indigo-500/20 text-indigo-300 font-black text-[10px] border border-indigo-500/30 uppercase">Immediate Remedy</span>
            <h3 class="text-lg font-black text-white mt-1">Unlock 96/100 ATS Executive Rewrite for {target_role}</h3>
            <p class="text-xs text-slate-400 max-w-lg mx-auto">Transforms weak passive verbs into verified Google XYZ metrics. Includes custom cold DM script for hiring managers.</p>
          </div>

          <div class="inline-block py-3 px-6 rounded-2xl bg-slate-900 border border-slate-700">
            <span class="text-3xl font-black text-white">$4.99</span>
            <span class="text-xs text-slate-400 ml-1">one-time unlock</span>
          </div>

          <button onclick="triggerCheckout()" class="w-full py-3.5 rounded-xl bg-gradient-to-r from-emerald-500 to-teal-600 hover:from-emerald-400 hover:to-teal-500 text-white font-extrabold text-xs tracking-wider shadow-lg shadow-emerald-500/20 transition flex items-center justify-center gap-2">
            <i class="fa-solid fa-bolt"></i> UNLOCK EXECUTIVE REWRITE ($4.99)
          </button>
        </div>

        <!-- Deliverable Preview Container -->
        <div id="rewriteBox" class="hidden p-6 rounded-2xl bg-slate-900 border border-emerald-500/40 space-y-4">
          <div class="flex items-center gap-2 text-emerald-400 text-xs font-bold">
            <i class="fa-solid fa-circle-check"></i> Rewrite Unlocked! ATS Score: 96/100
          </div>
          <div id="rewriteContent" class="text-xs text-slate-300 space-y-3 mono bg-slate-950 p-4 rounded-xl border border-slate-800"></div>
        </div>

      </div>
    </div>
  </main>

  <script>
    const sampleText = `{sample_cv_escaped}`;

    function loadSample() {{
      document.getElementById('resumeInput').value = sampleText;
    }}

    async function roastResume() {{
      const text = document.getElementById('resumeInput').value;
      const btn = document.getElementById('btnRoast');
      btn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Analyzing ATS Filters...';

      try {{
        const resp = await fetch('/api/analyze', {{
          method: 'POST',
          headers: {{ 'Content-Type': 'application/json' }},
          body: JSON.stringify({{ resume_text: text, target_role: '{target_role}' }})
        }});
        const data = await resp.json();
        document.getElementById('atsScore').innerText = data.ats_score + '/100';
        document.getElementById('rejectRisk').innerText = data.rejection_probability_pct + '%';
        document.getElementById('verdictText').innerText = data.verdict;
        document.getElementById('roastText').innerText = data.teaser_roast;
        document.getElementById('resultsBox').classList.remove('hidden');
      }} catch(e) {{
        alert('Error connecting to scanner API');
      }} finally {{
        btn.innerHTML = '<i class="fa-solid fa-fire text-base"></i> SCAN ATS REJECTION PROBABILITY (FREE)';
      }}
    }}

    async function triggerCheckout() {{
      const text = document.getElementById('resumeInput').value;
      try {{
        const resp = await fetch('/api/confirm-payment', {{
          method: 'POST',
          headers: {{ 'Content-Type': 'application/json' }},
          body: JSON.stringify({{ resume_text: text, target_role: '{target_role}', email: 'candidate@tech.com' }})
        }});
        const data = await resp.json();
        document.getElementById('rewriteBox').classList.remove('hidden');
        document.getElementById('rewriteContent').innerHTML = `
          <p class="text-emerald-400 font-bold mb-2">Executive Summary:</p>
          <p class="mb-4">${{data.data.executive_summary}}</p>
          <p class="text-indigo-400 font-bold mb-2">Recruiter Outreach Script:</p>
          <pre class="whitespace-pre-wrap text-slate-300 mb-4">${{data.data.recruiter_cold_email}}</pre>
          <p class="text-amber-400 font-bold mb-2">Upgraded High-Impact Bullets:</p>
          ${{data.data.upgraded_bullets.map(b => `<div class="mb-2"><span class="text-rose-400">❌ ${{b.before}}</span><br><span class="text-emerald-300">✅ ${{b.after}}</span></div>`).join('')}}
        `;
      }} catch(e) {{
        alert('Payment verification failed');
      }}
    }}
  </script>
</body>
</html>
"""

def generate_pages():
    for role in ROLE_DATA:
        badges = "".join([f'<span class="px-2 py-0.5 rounded-lg bg-slate-800 text-slate-300 text-[11px] font-mono border border-slate-700">{k}</span>' for k in role["keywords"]])
        escaped_cv = role["sample_cv"].replace("\n", "\\n").replace('"', '\\"')
        
        html = HTML_TEMPLATE.format(
            title=role["title"],
            h1=role["h1"],
            sub=role["sub"],
            target_role=role["target_role"],
            keyword_badges=badges,
            sample_cv=role["sample_cv"],
            sample_cv_escaped=escaped_cv
        )
        
        out_file = ROLES_DIR / f"{role['slug']}.html"
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"✅ Generated programmatic page: {out_file}")

if __name__ == "__main__":
    generate_pages()
