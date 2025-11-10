import tweepy
import pandas as pd
from datetime import datetime

client = tweepy.Client(bearer_token='YOUR_BEARER_TOKEN')

query = '$AAPL or $TSLA -is:retweet'
tweets = client.search_recent_tweets(query=query, max_results=100)

rows = []
for tweet in tweets.data:
  rows.append({
    'date': datetime.strptime(tweet.created_at, "%Y-%m-%dT%H:%M:%S.%fZ").date(), 
    'text': tweet.text
  })

df = pd.DataFrame(rows)
df.to_csv('../data/twitter_posts.csv', index=False)

