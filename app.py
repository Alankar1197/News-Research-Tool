import streamlit as st
from gemini_config import generate_news_summary
from datetime import datetime

st.set_page_config(
    page_title="All News Research Tool",
    page_icon="📰",
    layout="centered"
)

def login():
    st.title("🔐 User Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "admin123":
            st.session_state.logged_in = True
            st.success("Login successful")
            st.rerun()
        else:
            st.error("Invalid credentials")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    login()
    st.stop()

st.title("📰 All News Research Tool")
st.write(
    "Search and summarize news on **any topic** — politics, sports, tech, health, entertainment, and more."
)

st.sidebar.header("⚙️ Settings")

tone = st.sidebar.selectbox(
    "Select summary tone",
    ["Neutral", "Professional", "Casual", "Educational"]
)

st.sidebar.markdown("---")
if st.sidebar.button("🚪 Logout"):
    st.session_state.logged_in = False
    st.rerun()

query = st.text_input("Enter any topic")

if st.button("🔍 Search News"):
    if not query.strip():
        st.warning("Please enter a topic")
    else:
        with st.spinner("Fetching and summarizing news..."):
            summary = generate_news_summary(query, tone)

        st.subheader("🔎 News Summary")
        st.markdown(summary)

        if "history" not in st.session_state:
            st.session_state.history = []

        st.session_state.history.append({
            "time": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "query": query,
            "tone": tone,
            "summary": summary
        })

        st.download_button(
            label="📥 Download Summary",
            data=summary,
            file_name=f"{query.replace(' ', '_')}_summary.txt",
            mime="text/plain"
        )

if "history" in st.session_state and st.session_state.history:
    st.subheader("🕘 Search History")

    for item in reversed(st.session_state.history):
        with st.expander(f"{item['query']} ({item['tone']}) - {item['time']}"):
            st.markdown(item["summary"])

