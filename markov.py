#!/usr/bin/python
"""
The following program implements a Markov chain on the "tweetcorpus" file which was obtained as a result of the gettweets.py file. It picks a random word from among the tweets, makes a list of all the words which follow that word in all tweets, picks one at random and then repeats the same process on the word which it picked before, thus forming a sentence. It tweets this sentence if the length of this sentence is less than 140 characters.

Most of the sentences formed aren't coherent. But hey, it's a start!

"""
import sys
import tweepy
import warnings
import pickle
import re
import random
import time


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

# Load the base corpus of tweets
with open('tweetcorpus', 'rb') as f:
	corpus = pickle.load(f)

# Split each tweet text string into a list of words and make a list of those lists.
corpus_split=[]
for tweet in corpus:
	corpus_split.append(tweet.split())

# This function makes a list of all words which follow a given word (which it takes as an argument) and then returns one random word from that list.
def find_next_word(word):
	following_words=[]
	for i in range(0,len(corpus_split)):
            try:
                # find the words following the given word in all lists in the list corpus_split
                following_words.append(corpus_split[i][corpus_split[i].index("%s"%word) + 1])

            except (IndexError,ValueError):
                pass
	#print(following_words)
	if not following_words:
		return([]) #returns an empty list if there are no words following a given word.
	else:
		return(random.choice(following_words)) #else returns a random word from the list.

def make_sentences(seed):
    sentence=[seed]
    a=find_next_word(seed)
    if a == [] :
        return(" ".join(sentence))
    else:
        sentence.append(a)
        while len(" ".join(sentence))<140:
            a=find_next_word(a)
            if a == []:
                return(" ".join(sentence))
            else:
                sentence.append(a)
                #print(sentence)
                #print(a)
        sentence2=[x for x in sentence if x != []]
        return(" ".join(sentence2))

while True:
    try:
        seed=random.choice(random.choice(corpus_split))
        finaltweet=make_sentences(seed)
        if len(finaltweet)<=140:
            print("Posting tweet :")
            print("\n%s"%finaltweet)
            print(len(finaltweet))
            api.update_status("%s"%finaltweet)
        time.sleep(1800)
    except IndexError:
        pass

#print(seed)
