#!/usr/bin/env python3
"""
🚀 Instant Search Engine Indexer (IndexNow Protocol)
Submits all 14 programmatic SEO URLs for ResumeRoast.AI to Bing, Yandex,
and global search engines for immediate crawling & organic customer discovery.
"""

import json
import urllib.request
import ssl

KEY = "a4b7f9c2d1e0854372910fbcad7823e1"
HOST = "resume-roast-ai-xi.vercel.app"
KEY_LOCATION = f"https://{HOST}/{KEY}.txt"

ROLES = [
    "software-engineer",
    "product-manager",
    "data-scientist",
    "devops-cloud-architect",
    "cybersecurity-analyst",
    "blockchain-web3-developer",
    "machine-learning-engineer",
    "fullstack-react-developer",
    "financial-analyst",
    "ui-ux-designer",
    "registered-nurse",
    "digital-marketing-growth",
    "project-manager-scrum",
    "sales-account-executive"
]

URL_LIST = [
    f"https://{HOST}/",
    f"https://{HOST}/owner",
    f"https://{HOST}/directories"
] + [f"https://{HOST}/roles/{r}.html" for r in ROLES]

payload = {
    "host": HOST,
    "key": KEY,
    "keyLocation": KEY_LOCATION,
    "urlList": URL_LIST
}

endpoints = [
    "https://api.indexnow.org/indexnow",
    "https://www.bing.com/indexnow",
    "https://yandex.com/indexnow"
]

def submit_indexnow():
    ctx = ssl._create_unverified_context()
    data = json.dumps(payload).encode("utf-8")

    print(f"📡 Submitting {len(URL_LIST)} URLs to IndexNow engines...")
    for ep in endpoints:
        try:
            req = urllib.request.Request(
                ep,
                data=data,
                headers={"Content-Type": "application/json; charset=utf-8", "User-Agent": "IndexNowSubmitter/1.0"},
                method="POST"
            )
            with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
                print(f"✅ [{ep}] Status: {resp.status} (17 URLs successfully submitted for indexing)")
        except urllib.error.HTTPError as e:
            print(f"⚠️ [{ep}] HTTP {e.code}: {e.read().decode('utf-8', errors='ignore')}")
        except Exception as e:
            print(f"❌ [{ep}] Error: {e}")

if __name__ == "__main__":
    submit_indexnow()
