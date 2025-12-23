import os
from dotenv import load_dotenv
from newsapi import NewsApiClient

# -----------------------------
# Load environment variables
# -----------------------------
load_dotenv()
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

# -----------------------------
# Initialize NewsAPI client
# -----------------------------
newsapi = NewsApiClient(api_key=NEWS_API_KEY)

# -----------------------------
# Fetch news articles
# -----------------------------
def fetch_news(query):
    response = newsapi.get_everything(
        q=query,
        language="en",
        sort_by="relevancy",
        page_size=6
    )
    return response["articles"]

# -----------------------------
# Generate detailed summary
# -----------------------------
def generate_news_summary(query, tone):
    articles = fetch_news(query)

    if not articles:
        return "No relevant news found for this topic."

    # Tone guidance (used only for wording)
    tone_map = {
        "Neutral": "The following information presents a factual and unbiased overview.",
        "Professional": "The following summary is written in a formal and professional manner.",
        "Casual": "Here is an easy-to-read and conversational summary of the topic.",
        "Educational": "Below is a detailed explanation written for easy understanding."
    }

    summary = f"""
### 📰 News Summary – **{query}**
**Tone:** {tone}

{tone_map[tone]}

---

### 🔹 Overview
Multiple news outlets have recently reported on **{query}**. The coverage highlights key developments, official statements, and the broader implications of the topic.

### 🔹 Key Highlights
"""

    # Add article-based bullet points
    for article in articles:
        if article.get("description"):
            summary += f"\n- {article['description']}"

    summary += """

### 🔹 Sources & Further Reading
"""

    # Add clickable links
    for article in articles:
        if article.get("title") and article.get("url"):
            summary += f"\n- [{article['title']}]({article['url']})"

    return summary




