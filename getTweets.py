



client = tweepy.Client(bearer_token=TWITTER_BEARER_TOKEN, consumer_key=TWITTER_CONSUMER_KEY, 
                    consumer_secret=TWITTER_CONSUMER_SECRET, access_token=TWITTER_ACCESS_TOKEN,
                    access_token_secret=TWITTER_ACCESS_TOKEN_SECRET)

tweets = client.search_recent_tweets("(Apple iPhone) lang:en -retweet", end_time=today, max_results=100, start_time=yesterday, tweet_fields=['id', 'text', 'created_at', 'lang'])