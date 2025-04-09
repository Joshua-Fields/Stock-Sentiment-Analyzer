import praw
import re

excluded = {'YOLO', 'TOS', 'CEO', 'DD'}
ticker_pattern = re.compile(r'\$?[A-Z]{2,5}')

def get_reddit_client(client_id, client_secret, user_agent):
    return praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent=user_agent
    )

def fetch_posts(reddit, subreddit_name='wallstreetbets', limit=50):
    subreddit = reddit.subreddit(subreddit_name)
    return subreddit.hot(limit=limit)

def extract_tickers(text):
    tickers = ticker_pattern.findall(text)
    return [t.strip('$') for t in tickers if t.upper() not in excluded]
