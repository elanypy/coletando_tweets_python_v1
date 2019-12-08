import os
import csv
import tweepy as tw
import pandas as pd 

consumer_key = 'svyUFTExD7p4f3OtcgaTGTK3I'
consumer_secret = 'iALts0SG9Ejl6G0alUrJ2gmxaeP7xqCeWitZ7a3PHFpXzZJ411'
access_token = '1202304489136545792-Lsy3BqC3rXKw89mlb0ahS9lTsGxKn7'
access_token_secret = 'ctWv6umpzQKJYPE4DoYuIqcdc5oy3U3uMxZ63qb1ajwQx'

#keywords
search_word = "#ccxp2019"
new_search = search_word + "-filter:retweets"
#date_since = "2019-10-20"

#authentication 
auth = tw.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

#example send tweet 
api.update_status = ("Hey, everybody. What's up?")

counter = 0
#save file csv++
csvFile = open('resultados_twitter.csv','w')
csvWriter = csv.writer(csvFile)
csvWriter.writerow(["text","user", "location", "followers"])

#colect tweets 
tweets = tw.Cursor(api.search,
                    q =new_search,
                    lang = "pt-br").items(50)
                    # since =date_since).items(10)
#text_twitter = tweet.text
#name_user = tweet.user.screen_name
#location_user = tweet.user.location

#user_locs = [[tweet.text, tweet.user.screen_name, tweet.user.location] for tweet in tweets]
for tweet in tweets: 
    csvWriter.writerow([tweet.text,tweet.user.screen_name,
     tweet.user.location, tweet.author.followers_count]) 

#print(user_locs)

csvFile.close()
