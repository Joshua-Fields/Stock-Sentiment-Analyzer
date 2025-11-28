import psycopg2
import os

def get_connection():
    return psycopg2.connect(
        host=os.environ["DB_HOST"],
        port=os.environ.get("DB_PORT", "6543"),
        dbname=os.environ["DB_NAME"],
        user="postgres",  # 👈 must be this
        password=os.environ["DB_PASSWORD"],
        sslmode="require",
        pool_mode="transaction"  # optional, doesn't hurt, not required
    )


def create_table():
    """Create the stock_sentiment table if it does not already exist."""
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
