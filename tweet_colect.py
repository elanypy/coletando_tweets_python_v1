import os
import tweepy as tw
import pandas as pd 

consumer_key = '*********************'
consumer_secret = '***********************'
access_token = '*************************'
access_token_secret = '********************'

#keywords
search_word = "#python"
date_since = "2019-12-01"

#authentication 
auth = tw.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

#example send tweet 
api.update_status = ("Hey, everybody. What's up?")

#colect tweets 
tweets = tw.Cursor(api.search,
                    q =search_word,
                    lang = "pt-br",
                    since =date_since).items(5)

[tweet.text for tweet in tweets]
