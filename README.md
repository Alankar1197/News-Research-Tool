# News-Research-Tool
Project Overview-

The All News Research Tool is a Streamlit-based web application that allows users to search for news on any topic (politics, sports, technology, health, business, entertainment, etc.) and view a detailed, well-structured summary built from real-time online news articles.

The tool focuses on clarity, usability, and real-world applicability, making it suitable for academic projects, demos, and portfolio use.

Key Objectives-

Fetch real-time news from reliable online sources
Present explained and readable summaries
Allow users to control the tone of the summary
Improve usability through authentication and UI enhancements
Enable saving and exporting of research results

Tech Stack-
Python
Streamlit – Web application framework
NewsAPI – Real-time news data
python-dotenv – Secure environment variable handling

Features Implemented-
1. User Authentication
Simple login system to restrict access
Session-based authentication
Logout functionality

2. Tone Selection
Users can choose how the summary is written:
Neutral
Professional
Casual
Educational
The selected tone affects the language and explanation style of the summary.

3. Real-Time News Fetching
Fetches live articles using NewsAPI
Summaries are generated dynamically from article descriptions
Different results for every search

4. Detailed & Explained Summaries
Each summary includes:
Overview of the topic
Key highlights extracted from multiple articles
Clear explanations for better understanding
Clickable links to original news sources

5. UI/UX Enhancements
Clean layout with sidebar controls
Loading spinner during processing
Expandable search history
Icons and section headings for readability

6. Extended Functionality
Save search history during the session
Export summaries as .txt files
Timestamped query tracking

Project Structure
News Research Tool/
│
├── app.py                # Streamlit frontend + authentication + UI
├── gemini_config.py      # News fetching and summary logic
├── requirements.txt      # Project dependencies
├── .env                  # API keys
├── .gitignore
└── README.md

Environment Setup-
1️⃣ Create .env file
NEWS_API_KEY=your_newsapi_key_here

2️⃣ Install Dependencies
pip install -r requirements.txt

▶️ How to Run the Application
streamlit run app.py
Link- http://localhost:8501/
Username- admin
Password- admin123

Application Workflow-
User logs in
Enters a topic to search
Selects desired tone
Application fetches real-time news articles

A detailed summary is generated from live data

User can download or review search history
