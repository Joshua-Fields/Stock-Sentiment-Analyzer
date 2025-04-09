from scraper import get_reddit_client, fetch_posts, extract_tickers
from analyzer import analyze_post
from utils import save_to_csv

# === YOUR REDDIT CREDENTIALS ===
REDDIT_CLIENT_ID = 'zTP3m9l2Vn4EorH7MNOA9g'
REDDIT_CLIENT_SECRET = '69GgReH3BWtZrJgOjnFSu9xDlhwn6w'
REDDIT_USER_AGENT = 'Stock Sentiment Analyzer by /u/your_username'


def main():
    reddit = get_reddit_client(REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT)
    posts = fetch_posts(reddit, subreddit_name='wallstreetbets', limit=50)

    all_results = []
    for post in posts:
        result = analyze_post(post, extract_tickers)
        if result:
            all_results.extend(result)

    save_to_csv(all_results)


if __name__ == '__main__':
    main()
