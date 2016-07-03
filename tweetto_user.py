#!/usr/bin/python
"""This program annoys one particular user by tweeting one single phrase to them every time they tweet."""
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

# User IDs to follow. Kejriwal?!
follow_user_ids = ['USERID_HERE']

# Using the tweepy wrapper for Twitter API.
api = tweepy.API(auth)

# Creating a Stream Listener. This passes data from statuses to the on_status method.
# The on_status method asks Arvind Kejriwal about the wifi he promised every time he tweets.
class MyStreamListener(tweepy.StreamListener):
    	def on_status(self, status):
		if status.author.id_str in follow_user_ids:
			text = '::'.join([str(status.created_at), status.text, status.author.screen_name]) +'\n'
			print(text)
			api.update_status("@ArvindKejriwal sir wifi ka kya hua",status.id)
# Creating a stream
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=MyStreamListener())

# Starting the stream
myStream.filter(follow= follow_user_ids)

#myStream.filter(track=['boobs'])
