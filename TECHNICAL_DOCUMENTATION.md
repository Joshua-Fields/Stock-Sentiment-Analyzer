
# 📊 Stock Sentiment Analyzer – Technical Documentation

**Author:** Joshua (Chachua)  
**Tech Stack:** Python, Streamlit, PostgreSQL, NLP (VADER), Reddit API (PRAW)  
**Purpose:** Track and visualize Reddit sentiment for stock tickers in real time.

---

## 🧠 Overview

This project scrapes Reddit for stock-related posts and comments, analyzes the sentiment of these posts using natural language processing (VADER), stores the results in a PostgreSQL database, and visualizes trends with an interactive Streamlit dashboard.

---

## 🛠️ Architecture

```text
[Reddit Scraper (PRAW)]
         ↓
  [VADER Sentiment Analyzer]
         ↓
[PostgreSQL (stock_sentiment table)]
         ↓
[Streamlit Dashboard UI]
```

---

## 📂 Modules

### `scraper.py`
- Connects to Reddit using PRAW
- Fetches post titles and top-level comments
- Extracts stock tickers using regex

### `analyzer.py`
- Uses VADER to calculate compound sentiment scores
- Computes a **weighted sentiment** based on post score and comment count

### `utils.py`
- Utility for saving data to CSV

### `db.py`
- Connects to PostgreSQL
- Creates the `stock_sentiment` table if needed

### `ingest.py`
- Reads pre-scraped sentiment CSV
- Inserts into PostgreSQL in batch

### `dashboard.py`
- Streamlit app with:
  - Ticker and sentiment filters
  - Date range selector
  - Line and bar charts
  - Word cloud
  - Data preview

---

## 📊 Database Schema

```sql
CREATE TABLE stock_sentiment (
  id SERIAL PRIMARY KEY,
  ticker VARCHAR(10),
  sentiment_raw FLOAT,
  sentiment_weighted FLOAT,
  post_score INTEGER,
  num_comments INTEGER,
  title TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## 🔐 Environment Variables

For local development, credentials are stored in `.env` or `.streamlit/secrets.toml`.

```env
DB_HOST=localhost
DB_NAME=stock_data
DB_USER=postgres
DB_PASSWORD=1234
```

On **Streamlit Cloud**, secrets are passed via the app's settings panel.

---

## 🚀 Deployment

1. Push repo to GitHub
2. Deploy on [Streamlit Cloud](https://streamlit.io/cloud)
3. Add `secrets.toml` via the UI
4. (Optional) Use Supabase for a cloud-hosted Postgres backend

---

## ✅ Future Features (Ideas)
- News sentiment ingestion (NewsAPI)
- Twitter/X integration
- Sentiment vs stock price correlation
- Daily email reports or alerts
- User accounts and watchlists

---

## 📎 References
- [PRAW – Reddit API](https://praw.readthedocs.io/)
- [VADER Sentiment](https://github.com/cjhutto/vaderSentiment)
- [Streamlit](https://docs.streamlit.io/)
- [psycopg2 PostgreSQL Driver](https://www.psycopg.org/)
