import pandas as pd

def save_to_csv(data, filename='reddit_sentiment_cache.csv'):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"✅ Saved {len(df)} entries to {filename}")
