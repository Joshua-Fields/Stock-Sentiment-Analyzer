from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()


def sentiment_score(text):
    return analyzer.polarity_scores(text)['compound']


def analyze_post(submission, extract_tickers, max_comments=20):
    title = submission.title
    tickers = extract_tickers(title)
    if not tickers:
        return []

    title_sentiment = sentiment_score(title)

    submission.comments.replace_more(limit=0)
    comments = submission.comments.list()[:max_comments]
    comment_scores = [sentiment_score(c.body) for c in comments]
    comment_avg = sum(comment_scores) / len(comment_scores) if comment_scores else 0

    combined = (title_sentiment + comment_avg) / 2
    score_weight = submission.score / 100
    comment_weight = len(comments) / max_comments
    weighted = combined * (0.7 + 0.3 * (score_weight + comment_weight))

    return [{
        'ticker': ticker,
        'sentiment_raw': combined,
        'sentiment_weighted': weighted,
        'post_score': submission.score,
        'num_comments': len(comments),
        'title': title
    } for ticker in tickers]
