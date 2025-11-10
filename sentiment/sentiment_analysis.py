import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()

reddit_df = pd.read_csv('../data/reddit_posts.csv')
twitter_df = pd.read_csv('../data/twitter_posts.csv')

reddit_df['text_combined'] = reddit_df['title'].fillna('') + ' ' + reddit_df['text'].fillna('')
twitter_df['text_combined'] = twitter.df['text']

all_posts = pd.concat([reddit_df[['date', 'text_combined']], twitter_df[['data', 'text_combined']]])

all_posts['sentiment'] = all_posts['text_combined'].apply(lambda x: sia.polarity_scores(x)['compound'])

daily_sentiment = all_posts.groupby('date')['sentiment'].mean().reset_index()
daily_sentiment.to_csv('../data/daily_sentiment.csv', index=False)







