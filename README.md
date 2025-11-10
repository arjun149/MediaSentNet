# Media Sentiment Pipeline

This repository collects social media data from Reddit and Twitter, processes it to generate sentiment scores, and outputs structured CSV files suitable for machine learning or reinforcement learning models.

## Features
- Scrape posts and comments from Reddit and Twitter
- Compute daily sentiment scores for tickers or keywords
- Aggregate data into CSVs for downstream NN models
- Template-ready scri[ts for extending to additional platforms/tickers

## Folder Structure
- 'reddit/' - Reddit scraping scripts
- 'twitter/' - Twitter scraping scripts
- 'sentiment/' - Sentiment analysis scripts
- 'data/' - Generated CSVs with post and sentiment data
- Additional: Public.ComAPI/src/ - NN training scripts (linked) 



## Setup & Usage

1. Clone this repository
'''bash
git clone https://github.com/arjun149/market_sentiment.git
cd market-sentiment

2. Install dependencies:
pip install -r requirements.txt

3. Set up Reddit and Twitter API keys:
reddit.com/prefs/apps
developer.twitter.com

4. Generate data:
python reddit/scrape_reddit.py
python twitter/scrape_twitter.py

5. Run sentiment analysis
python sentiment/sentiment_analyis.py

6. Train model
https://github.com/arjun149/Public.ComAPI/blob/main/src/preprocess.py
python src/train.py



