# 📊 Stock Sentiment Analyzer

A dashboard that scrapes Reddit for stock mentions, analyzes sentiment using VADER NLP, stores data in PostgreSQL, and visualizes trends over time.

## 🚀 Features
- Reddit post + comment scraping
- Ticker extraction
- Weighted sentiment analysis
- PostgreSQL backend
- Streamlit dashboard w/ filters, charts, word cloud

## 🔧 Tech Stack
- Python, Streamlit
- PostgreSQL
- PRAW (Reddit API), VADER
- Matplotlib, WordCloud

## 📦 Setup
1. `pip install -r requirements.txt`
2. Add a `.env` file with: DB_HOST=localhost DB_NAME=stock_data DB_USER=postgres DB_PASSWORD=your_password
3. Run: `python -m streamlit run dashboard.py`

## 🧠 Author
Built by Joshua 💡
