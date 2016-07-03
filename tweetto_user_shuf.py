#!/usr/bin/python
"""A simple program to tweet back a users tweet to them after shuffling it. """

import sys
import tweepy
import warnings
import re
from random import shuffle

# Kill all warnings please.
warnings.filterwarnings("ignore")

# info etc
consumer_key='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
consumer_secret='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
access_token='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
access_token_secret='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

# authentication bullshit
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Using the tweepy wrapper for Twitter API.
api = tweepy.API(auth)

# User IDs to follow. (Get this by typing api.get_user('USERNAME_HERE') in a Python prompt and find the id among the junk.)
follow_user_ids = ['USERID_HERE']

# Creating a Stream Listener. This passes data from statuses to the on_status method.
# The on_status function takes the text of the tweet, puts it into a nice list, shiffles the list, joins it,
# and tweets it back to the user after making sure it has no media and that it's not a retweet.
class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        if status.author.id_str in follow_user_ids:
            text = '::'.join([str(status.created_at), status.text, status.author.screen_name]) +'\n'
            a=status.text
            b=a.encode('utf8')
            c=b.split()
            shuffle(c)
            fin=' '.join(c)
            print(text)
            if len(fin)<130 and not('RT' in b) and not(bool(re.search('@',b))) and not(bool(re.search('https',b))):
                api.update_status("@TWITTER_HANDLE_HERE %s"%fin,status.id)

# Creating a stream
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=MyStreamListener())

# Starting the stream
myStream.filter(follow= follow_user_ids)

#myStream.filter(track=['boobs'])
