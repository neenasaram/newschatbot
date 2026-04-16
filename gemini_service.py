import requests
import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def generate_response(prompt):

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro:generateContent?key={GEMINI_API_KEY}"

    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ]
    }

    try:
        res = requests.post(url, headers=headers, json=data)
        response_json = res.json()

        if "candidates" in response_json:
            return response_json["candidates"][0]["content"]["parts"][0]["text"]

        elif "error" in response_json:
            return f"⚠️ Gemini Error: {response_json['error']['message']}"

        else:
            return f"⚠️ Unexpected response: {response_json}"

    except Exception as e:
        return f"⚠️ Exception: {str(e)}"