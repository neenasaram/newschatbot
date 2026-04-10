import google.generativeai as genai
from config.settings import GEMINI_API_KEY
from utils.logger import logger

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

def generate_response(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        logger.error(f"Gemini Error: {str(e)}")
        return "⚠️ AI service unavailable. Showing raw news."