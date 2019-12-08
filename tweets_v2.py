import os
import csv
import tweepy as tw
import pandas as pd 

consumer_key = '********************'
consumer_secret = '********************'
access_token = '********************'
access_token_secret = '********************'

#keywords
search_word = "#UFMG"
new_search = search_word + "-filter:retweets"
#date_since = "2019-10-20"

#authentication 
auth = tw.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

#example send tweet 
api.update_status = ("Hey, everybody. What's up?")

#save file csv
csvFile = open('resultados_twitter.csv','w')
csvWriter = csv.writer(csvFile)
csvWriter.writerow(["text","user","location", "followers"])

#colect tweets 
tweets = tw.Cursor(api.search,
                    q =new_search,
                    lang = "pt-br").items(10)
                    # since =date_since).items(10)
#text_twitter = tweet.text
#name_user = tweet.user.screen_name
#location_user = tweet.user.location

#user_locs = [[tweet.text, tweet.user.screen_name, tweet.user.location] for tweet in tweets]
for tweet in tweets: 
    csvWriter.writerow([tweet.text, tweet.user.location,
        tweet.user.location, tweet.author.followers_count]) 

#print(user_locs)

csvFile.close()

