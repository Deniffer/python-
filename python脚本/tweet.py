# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 17:06:17 2020

@author: HASEE
"""
import tweepy
import json
import csv

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



