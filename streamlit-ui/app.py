import streamlit as st
import requests

st.set_page_config(page_title="E-Commerce Chatbot", layout="centered")
st.title("🛍️ E-Commerce Expert Chatbot")

chat_history = st.session_state.setdefault("history", [])

user_input = st.text_input("Ask something about products or your orders:")

if st.button("Send") and user_input:
    chat_history.append(("You", user_input))

    response = requests.post("http://localhost:8000/chat", json={"message": user_input})
    bot_reply = response.json().get("response", "Something went wrong.")
    chat_history.append(("Bot", bot_reply))

for sender, msg in reversed(chat_history):
    st.write(f"**{sender}:** {msg}")
