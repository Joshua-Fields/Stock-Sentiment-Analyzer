from main import main as run_scraper
from ingest import ingest_csv

def update_sentiment():
    print("🔄 Running sentiment update...")
    run_scraper()
    ingest_csv()
    print("✅ Sentiment data updated successfully.")

if __name__ == "__main__":
    update_sentiment()
