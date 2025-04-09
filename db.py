import psycopg2
from dotenv import load_dotenv
import os
import streamlit as st
load_dotenv()


def get_connection():
    return psycopg2.connect(
        host=st.secrets["DB_HOST"],
        port=st.secrets["DB_PORT"],
        database=st.secrets["DB_NAME"],
        user=st.secrets["DB_USER"],
        password=st.secrets["DB_PASSWORD"]
    )


def create_table():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS stock_sentiment (
            id SERIAL PRIMARY KEY,
            ticker VARCHAR(10),
            sentiment_raw FLOAT,
            sentiment_weighted FLOAT,
            post_score INTEGER,
            num_comments INTEGER,
            title TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)

    conn.commit()
    cur.close()
    conn.close()
    print("✅ Table ensured in database.")
