import requests
from config.settings import NEWS_API_KEY
from utils.logger import logger

def fetch_news(query):
    url = "https://newsapi.org/v2/everything"

    params = {
        "q": query,
        "apiKey": NEWS_API_KEY,
        "pageSize": 5,
        "sortBy": "publishedAt",
        "language": "en"
    }

    try:
        res = requests.get(url, params=params, timeout=10)

        if res.status_code != 200:
            logger.error(f"News API error: {res.text}")
            return None

        data = res.json()
        return data.get("articles", [])

    except Exception as e:
        logger.error(f"Exception: {str(e)}")
        return None