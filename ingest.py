import csv
from db import get_connection, create_table


def ingest_csv(filename='reddit_sentiment_weighted.csv'):
    create_table()
    conn = get_connection()
    cur = conn.cursor()

    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cur.execute("""
                INSERT INTO stock_sentiment (
                    ticker,
                    sentiment_raw,
                    sentiment_weighted,
                    post_score,
                    num_comments,
                    title
                ) VALUES (%s, %s, %s, %s, %s, %s);
            """, (
                row['ticker'],
                float(row['sentiment_raw']),
                float(row['sentiment_weighted']),
                int(row['post_score']),
                int(row['num_comments']),
                row['title']
            ))

    conn.commit()
    cur.close()
    conn.close()
    print(f"✅ Ingested data from {filename} into database.")


if __name__ == '__main__':
    ingest_csv()
