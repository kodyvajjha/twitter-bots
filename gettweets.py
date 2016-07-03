#!/usr/bin/python
"""
This program gets tweets of the specified users repeatedly. Note that you can only get about 3000 tweets at once.

"""
import sys
import tweepy
import warnings
import pickle
import re
from random import shuffle

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

def get_tweets(screenname):
	#initialize a list to hold all the tweepy Tweets
	alltweets = []

	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name=screenname,count=200)

	#save most recent tweets
	alltweets.extend(new_tweets)

	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1

	#keep grabbing tweets until there are no tweets left to grab
	while len(new_tweets) > 0:
		print "getting tweets before %s" % (oldest)

		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name=screenname ,count=200,max_id=oldest)

		#save most recent tweets
		alltweets.extend(new_tweets)

		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1

		print "...%s tweets downloaded so far" % (len(alltweets))
        #get the text of tweets in utf-8 format as a list
	alltweet_text=[]
	for tweet in alltweets:
		alltweet_text.append(tweet.text.encode("utf-8"))
	print(alltweet_text[:10])

        #remove all RTs, mentions and hyperlinks in the tweets to focus only on the raw text.
	alltweet_filtered=[]
	for tweet in alltweet_text:
		alltweet_filtered.append(re.sub(r"@\w+|RT|https\:\/\/t.co\/\w+|http\:\/\/t.co\/\w+","",tweet))
	return(alltweet_filtered)

sum=get_tweets("USERNAME_HERE")+get_tweets("USERNAME_HERE")

# dump the tweets you downloaded into a file called "tweetcorpus"
with open('tweetcorpus','wb') as f:
	pickle.dump(sum,f)
