import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()

reddit_df = pd.read_csv('../data/reddit_posts.csv')
twitter_df = pd.read_csv('../data/twitter_posts.csv')

reddit_df['text_combined'] 







