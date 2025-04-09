
# 📈 Stock Sentiment Analyzer

A fully automated stock sentiment analysis pipeline that scrapes Reddit posts, performs natural language sentiment analysis, stores the results in a Supabase-hosted PostgreSQL database, and visualizes everything in a beautiful Streamlit dashboard.

---

## 🚀 Live Demo

👉 [Streamlit Dashboard (Hosted)](https://share.streamlit.io/your-deployed-url-here)

---

## 🧠 Overview

This project tracks the sentiment of trending stock tickers based on posts from subreddits like `r/stocks` and `r/wallstreetbets`. It uses:

- 🔍 **Reddit API (PRAW)** to scrape posts & comments  
- 💬 **VADER Sentiment** analysis to quantify tone  
- 🐘 **Supabase PostgreSQL** to store results  
- 📊 **Streamlit** for a clean, interactive dashboard  
- ⚙️ **GitHub Actions** to refresh data automatically every hour

---

## 📂 Project Structure

```
📦 Stock-Sentiment-Analyzer
├── analyzer.py              # VADER sentiment logic
├── dashboard.py             # Streamlit UI
├── db.py                    # PostgreSQL connection & schema
├── ingest.py                # Load CSVs into the database
├── main.py                  # Main Reddit scraping entry point
├── scraper.py               # PRAW-based scraper
├── update_sentiment.py      # Script to run scraper + ingest together
├── utils.py                 # CSV export & helpers
├── requirements.txt
└── .github/workflows/
    └── update-sentiment.yml # GitHub Action for hourly updates
```

---

## 🛠️ Technologies Used

| Tech         | Role                          |
|--------------|-------------------------------|
| `Python`     | Main language                 |
| `PRAW`       | Reddit API wrapper            |
| `VADER`      | Sentiment analysis            |
| `Streamlit`  | Dashboard and frontend        |
| `PostgreSQL` | Database via Supabase         |
| `GitHub Actions` | Automated hourly ingestion |

---

## ⚙️ Automation Pipeline

```
[GitHub Action]
     |
     ↓
[main.py] → Scrape Reddit posts/comments
     ↓
[analyzer.py] → Run VADER sentiment
     ↓
[ingest.py] → Insert into Supabase PostgreSQL
     ↓
[Streamlit Dashboard] → Query + visualize live data
```

---

## 📈 Features

- View sentiment per stock ticker
- Weighted vs raw sentiment views
- Word cloud of high-mention terms
- Toggleable raw data preview
- Dashboard filters: ticker, sentiment type, date range
- Auto-refreshes data hourly via GitHub Actions

---

## 🔐 Environment Variables

For local development, create a `.env` or `.streamlit/secrets.toml` with:

```toml
DB_HOST = "aws-0-eu-west-2.pooler.supabase.com"
DB_PORT = "6543"
DB_NAME = "postgres"
DB_USER = "postgres.<your-project-ref>"
DB_PASSWORD = "<your-password>"
```

For **GitHub Actions**, these values are securely set as **repo secrets**.

---

## ✅ Setup Instructions

```bash
# Clone the project
git clone https://github.com/Joshua-Fields/Stock-Sentiment-Analyzer.git
cd Stock-Sentiment-Analyzer

# Install dependencies
pip install -r requirements.txt

# Run locally
python update_sentiment.py
streamlit run dashboard.py
```

---

## 🌐 Deployment

- Streamlit Cloud for the dashboard
- Supabase for PostgreSQL (with free Transaction Pooling)
- GitHub Actions runs every hour to update sentiment data

---

## 🧪 Next Features (Wishlist)

- News API ingestion
- Stock price integration via Yahoo/Alpha Vantage
- User watchlists
- Sentiment heatmaps
- Email or Slack alerts

---

## 👤 Author

Built with ❤️ by **[Joshua Fields](https://github.com/Joshua-Fields)**  
[Portfolio](https://your-portfolio-url.com) | [LinkedIn](https://linkedin.com/in/yourprofile)

---

## 📎 License

MIT License — free to use and adapt.
