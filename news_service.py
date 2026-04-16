import requests
import os
from dotenv import load_dotenv

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

def fetch_news(query):
    url = "https://newsapi.org/v2/everything"

    # ✅ FIXED QUERY (important)
    params = {
        "q": f"{query} Telangana India",
        "apiKey": NEWS_API_KEY,
        "pageSize": 5,
        "sortBy": "publishedAt",
        "language": "en"
    }

    try:
        res = requests.get(url, params=params, timeout=10)
        data = res.json()

        # Debug if API fails
        if res.status_code != 200:
            print("News API Error:", data)
            return []

        articles = data.get("articles", [])

        # ✅ Fallback if no results
        if not articles:
            params["q"] = "latest news India"
            res = requests.get(url, params=params, timeout=10)
            data = res.json()
            articles = data.get("articles", [])

        return articles if articles else []

    except Exception as e:
        print("Error fetching news:", str(e))
        return []