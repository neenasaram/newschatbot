import streamlit as st
from services.news_service import fetch_news
from services.gemini_service import generate_response
from prompts.system_prompt import SYSTEM_PROMPT

st.set_page_config(page_title="News Chatbot")

# ==============================
# SESSION MEMORY
# ==============================
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("📰 Production News Chatbot")

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input
user_input = st.chat_input("Ask about news...")

if user_input:

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.write(user_input)

    # Fetch news
    articles = fetch_news(user_input)

    if not articles:
        reply = "⚠️ No news found."
    else:
        news_text = ""
        for a in articles:
            news_text += f"""
Title: {a.get('title')}
Description: {a.get('description')}
Source: {a.get('source', {}).get('name')}
URL: {a.get('url')}
"""

        prompt = f"""
{SYSTEM_PROMPT}

News Data:
{news_text}

User Query:
{user_input}
"""

        reply = generate_response(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Generating..."):
            st.write(reply)

    st.session_state.messages.append({
        "role": "assistant",
        "content": reply
    })