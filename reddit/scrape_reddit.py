import praw
import pandas as pd
from datetime import datetime

reddit = praw.Reddit(client_id='YOUR_ID',
                      client_secret='YOUR SECRET',
                     user_agent='my_app')

subreddit = reddit.subreddit('wallstreetbets')

posts = []
for submission in subreddit.top(time_filter='month', limit = 500):
  posts.append({
    'date': datetime.utcfromtimestamp(submission.created_utc).date(),
    'title': submission.title,
    'text': submission.selftext,
    'score': submission.score
  })

df.pdDataFrame(posts)
df.to_csv('../data/reddit_posts.csv', index=False)
