# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 17:06:17 2020

@author: HASEE
"""
import tweepy
import json
import csv

consumer_key="GBdhTAQPrEPDq4jV63PcdFHJf"
consumer_secret="JhUCySiJGMyK86ahtPUxXIwD2YYhFN5E6AWUjG9KdcSFy8S3hA"
access_token="1222353136150437890-U7ssgmG33F4ECwIGuTmZggF4pWXj2x"
access_token_secret="WILeWfr2Aia4L5K93imjCPdPIeNFYb6ZnCdvO6DEMGrM4"

auth =tweepy.OAuthHandler(consumer_key=consumer_key,consumer_secret=consumer_secret) 
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

#information={}
#information[tweet.user.name]=tweet.text

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        print(f"{tweet.user.name}:{tweet.text}")
        #tweet_info=[tweet.user.name,tweet.text]
        with open("tweet_data.csv",mode="a") as fp:
            #fp.writelines(f"{tweet.user.name}:{tweet.text}")
            writer=csv.writer(fp)
            try:
                writer.writerow(tweet.extended_tweet['full_text'])
            except:
                writer.writerow(tweet.text)
            print("Success!")
    def on_error(self, status):
        print("Error detected")

tweets_listener = MyStreamListener(api)
stream = tweepy.Stream(api.auth, tweets_listener)
stream.filter(track=["highway accident -filter:replies","roadworks OR M6 -filter:replies"], languages=["en"])



