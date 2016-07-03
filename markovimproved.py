#!/usr/bin/python
"""
This program is an improvement of the markov.py program, which implemented a markov chain on the "tweetcorpus" file. Instead of taking a single word and listing it's potential successors and then choosing one amongst them, we choose a pair of successive words, such as ("hi","there") and then make a list of all *tuples* of words which follow the word "there" in all the tweets, and then pick one at random and make the tweet.

This process results in much more coherent tweets.

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

# Split each tweet text string into a list of consecutive tuples of words and make a list of those lists.
corpus_split_tuples=[]
for tweet in corpus:
	a=tweet.split()
	corpus_split_tuples.append(zip(a,a[1:]))

#print(corpus_split_tuples[5:8])

def find_next_word((w1,w2)):
    following_words=[]
    words=(w1,w2)
    for i in range(0,len(corpus_split_tuples)):
        try:
            a=corpus_split_tuples[i]
            b=a.index(words,)
            following_words.append(a[b+1])
        except (IndexError,ValueError):
            pass
    print(following_words)
    if not following_words:
            return([]) #returns an empty list if there are no word tuples following a given word.
    else:
            return(random.choice(following_words)) #else returns a random word tuple from the list.

def make_sentences((s1,s2)):
    seed=(s1,s2)
    sentence=[seed]
    print(seed[0])
    a=find_next_word(seed)
    if a == [] :
	return(seed[0]+ " " + seed[0][1])
    else:
	sentence.append(a)
	while len(seed[0] + " " + " ".join(t[1] for t in sentence))<140:
		a=find_next_word(a)
		if a == []:
                    return(seed[0] + " " + " ".join(t[1] for t in sentence))
                else:
                    sentence.append(a)
		#		print(sentence)
		#		print(a)
		sentence2=[x for x in sentence if x != []]
		return(seed[0] + " " + " ".join(t[1] for t in sentence2))

while True:
    try:
        seed=random.choice(random.choice(corpus_split_tuples))
        finaltweet=make_sentences(seed)
        if len(finaltweet)<=140:
            print("Posting tweet :")
            print("\n%s"%finaltweet)
            print(len(finaltweet))
            api.update_status("%s"%finaltweet)
            time.sleep(1800)
    except IndexError:
		pass

#a=find_next_word(("the","girls"))
#b=make_sentences(a)
#print(b)
