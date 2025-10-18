import os
import openai
from datetime import datetime
from pathlib import Path

openai.api_key = os.getenv("OPENAI_API_KEY")

# Create content folder if not exists
Path("content").mkdir(exist_ok=True)

# Generate today's filename
today = datetime.utcnow().strftime("%Y-%m-%d")
filename = f"content/{today}-ai-trends.md"

# Skip if today's post already exists
if os.path.exists(filename):
    print("Post already exists for today.")
    exit()

prompt = """
Write a 600-word SEO-friendly article about the most important AI trends, innovations, and research updates today.
Make it informative, clear, and engaging for a general audience.
Use markdown formatting (headings, bullet points, etc.).
"""

response = openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a tech journalist who writes clear, engaging summaries of AI news."},
        {"role": "user", "content": prompt}
    ],
)

article = response.choices[0].message.content

# Save to markdown file
with open(filename, "w", encoding="utf-8") as f:
    f.write(article)

print(f"✅ Article saved to {filename}")
