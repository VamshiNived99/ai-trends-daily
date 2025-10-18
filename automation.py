import os
import requests
from datetime import datetime
from pathlib import Path

# Get Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

# Create folders if not exist
Path("content").mkdir(exist_ok=True)

today = datetime.utcnow().strftime("%Y-%m-%d")
filename = f"content/{today}-ai-trends.md"

# Skip if already exists
if os.path.exists(filename):
    print("✅ Post already exists for today.")
    exit()

prompt = """
Write a 600-word SEO-friendly article summarizing the latest AI trends and breakthroughs today.
Make it engaging, informative, and formatted in Markdown (with headings, bullet points, and short paragraphs).
"""

# Gemini API endpoint
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"

payload = {
    "contents": [
        {"parts": [{"text": prompt}]}
    ]
}

response = requests.post(url, json=payload)

if response.status_code != 200:
    print("❌ Error:", response.text)
    exit()

data = response.json()

# Extract text safely
article = data.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "")

if not article:
    print("❌ No content generated.")
    exit()

# Save to file
with open(filename, "w", encoding="utf-8") as f:
    f.write(article)

print(f"✅ Article saved to {filename}")
