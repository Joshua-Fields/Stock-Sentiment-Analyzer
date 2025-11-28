import streamlit as st
import pandas as pd
import psycopg2
from dotenv import load_dotenv
import os
import streamlit as st
from datetime import datetime

# === Load environment variables ===
load_dotenv()

# === Connect to PostgreSQL ===
conn = psycopg2.connect(
    host=st.secrets["DB_HOST"],
    port=st.secrets["DB_PORT"],
    dbname=st.secrets["DB_NAME"], 
    user=st.secrets["DB_USER"],
    password=st.secrets["DB_PASSWORD"],
    sslmode="require"          
)


st.set_page_config(
    page_title="Stock Sentiment Dashboard",
    page_icon="📈",
    layout="wide"
)

# === Fetch data from DB ===
@st.cache_data(ttl=600)
def load_data():
    df = pd.read_sql("SELECT * FROM stock_sentiment ORDER BY created_at DESC", conn)
    df['created_at'] = pd.to_datetime(df['created_at'])  # ensure datetime format
    return df

df = load_data()

# === Sidebar Filters ===
st.sidebar.title("🔍 Filters")
st.caption("Built with Python, PostgreSQL, and NLP – tracking Reddit stock sentiment in real time.")




available_tickers = sorted(df['ticker'].unique())
selected_ticker = st.sidebar.selectbox("Choose Ticker", available_tickers)

sentiment_type = st.sidebar.radio("Sentiment", ['sentiment_raw', 'sentiment_weighted'])

# Make sure created_at is parsed as datetime
if not df.empty and 'created_at' in df.columns:
    df['created_at'] = pd.to_datetime(df['created_at'], errors='coerce')
    df = df.dropna(subset=['created_at'])  # remove rows with invalid dates

    if not df.empty:
        min_date = df['created_at'].min().date()
        max_date = df['created_at'].max().date()
    else:
        min_date = max_date = datetime.today().date()
else:
    min_date = max_date = datetime.today().date()

# Render the date range input
start_date, end_date = st.sidebar.date_input("Date range", [min_date, max_date])

# === Filter data ===
filtered = df[
    (df['ticker'] == selected_ticker) &
    (df['created_at'].dt.date >= start_date) &
    (df['created_at'].dt.date <= end_date)
]

# === Main Dashboard ===
st.title("📊 Stock Sentiment Analyzer Dashboard")
st.markdown(f"### Showing data for: **{selected_ticker}**")

if filtered.empty:
    st.warning("⚠️ No data available for this selection.")
else:
    avg_sent = round(filtered[sentiment_type].mean(), 3)
    st.metric(label="📈 Average Sentiment", value=avg_sent)

    st.line_chart(filtered.set_index("created_at")[sentiment_type])

# === Top Mentioned Tickers Bar Chart ===
st.markdown("### 🏆 Top 10 Most Mentioned Tickers")
top_mentions = df['ticker'].value_counts().head(10)
st.bar_chart(top_mentions)

# === Word Cloud ===
if not filtered.empty:
    st.markdown("### ☁️ Word Cloud of Post Titles")

    from wordcloud import WordCloud
    import matplotlib.pyplot as plt

    title_text = " ".join(filtered['title'].tolist())
    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color='black',
        colormap='Pastel1',
        stopwords={'https', 'amp', 'stock', 'stocks', 'buy', 'sell', 'market'}
    ).generate(title_text)

    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis("off")
    st.pyplot(fig)


# === Optional Raw Data Table ===
if st.checkbox("Show raw data"):
    st.dataframe(filtered if not filtered.empty else df[df['ticker'] == selected_ticker])

# === Close DB connection ===
conn.close()
