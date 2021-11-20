from time import timezone
from twitconfig import *
import tweepy
from datetime import datetime, timezone, timedelta
import preprocessor as p
import pandas as pd
import sqlite3 as sql


auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)

api  = tweepy.API(auth, wait_on_rate_limit=True)

today = datetime.now(timezone.utc) - timedelta(minutes=5)
yesterday = today - timedelta(minutes=35)

client = tweepy.Client(bearer_token=TWITTER_BEARER_TOKEN, consumer_key=TWITTER_CONSUMER_KEY, 
                    consumer_secret=TWITTER_CONSUMER_SECRET, access_token=TWITTER_ACCESS_TOKEN,
                    access_token_secret=TWITTER_ACCESS_TOKEN_SECRET)

tweets = client.search_recent_tweets("(Taco Bell) lang:en -retweet", end_time=today, max_results=100, start_time=yesterday, tweet_fields=['id', 'text', 'created_at', 'lang'])

def getTweets(twList):
    output = []
    for tweet in twList:
            
            twtID = tweet.id
            text = tweet.text
            created_at = tweet.created_at
            lang = tweet.lang

            line = {'ID' : twtID, 'text' : text, 'created_at' : created_at, 'lang' : lang}

            output.append(line)
    return output

tweet_list = getTweets(tweets.data)
df = pd.DataFrame(tweet_list)

conn = sql.connect('/Users/ben/Benborg/ads_tweetapp/data/tweets.db')
df.to_sql('tweets', conn, if_exists='append', index=False)


