#!/usr/bin/python
"""
This program uses the Twitter Streaming API to print tweets in real time. You can use the "track" option to filter tweets which have a specific word in their text.

Really cool stuff!

"""
import sys
import tweepy
import warnings

# Kill all warnings please.
warnings.filterwarnings("ignore")

# info etc
consumer_key=''
consumer_secret=''
access_token=''
access_token_secret=''

# authentication bullshit
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Using the tweepy wrapper for Twitter API.
api = tweepy.API(auth)

# Creating a Stream Listener. This passes data from statuses to the on_status method.
# The on_status method prints the tweets neatly.
class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        text = '::'.join([str(status.created_at), status.text, status.author.screen_name]) +'\n'
        print(text)

# Creating a stream
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=MyStreamListener())

# Filtering the stream according to specific words.

myStream.filter(track=['boobs'])
