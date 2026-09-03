#!/usr/bin/env python3
"""
🚀 Instant Search Engine Indexer (IndexNow Protocol)
Submits all programmatic SEO URLs for ResumeRoast.AI to Bing, Yandex,
and global search engines for immediate crawling & organic customer discovery.
"""

import json
import urllib.request
import ssl

KEY = "a4b7f9c2d1e0854372910fbcad7823e1"
HOST = "resume-roast-ai-xi.vercel.app"
KEY_LOCATION = f"https://{HOST}/{KEY}.txt"

URL_LIST = [
    f"https://{HOST}/",
    f"https://{HOST}/owner",
    f"https://{HOST}/roles/software-engineer.html",
    f"https://{HOST}/roles/product-manager.html",
    f"https://{HOST}/roles/data-scientist.html",
    f"https://{HOST}/roles/devops-cloud-architect.html"
]

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
                print(f"✅ [{ep}] Status: {resp.status} (URLs successfully submitted for indexing)")
        except urllib.error.HTTPError as e:
            print(f"⚠️ [{ep}] HTTP {e.code}: {e.read().decode('utf-8', errors='ignore')}")
        except Exception as e:
            print(f"❌ [{ep}] Error: {e}")

if __name__ == "__main__":
    submit_indexnow()
