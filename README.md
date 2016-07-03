# twitter-bots

This project contains a collection of python programs which concern themselves with Twitter bots: non-human twitter accounts which are programmed to tweet. 

In order to use these programs, you will need to set up a Twitter account and get Twitter API keys. This is done by the following steps. 

-Create a twitter account if you do not already have one.
-Go to https://apps.twitter.com/ and log in with your twitter credentials.
-Click "Create New App"
-Fill out the form, agree to the terms, and click "Create your Twitter application"
-In the next page, click on "API keys" tab, and copy your "API key" and "API secret".
-Scroll down and click "Create my access token", and copy your "Access token" and "Access token secret".

We use the Python wrapper Tweepy for our project. 

Here is a quick overview of the programs included in this repository.

1)tweet_stream.py : This uses the Twitter Streaming API to get tweets in real time. You can also filter tweets using key words. 

2)tweetto_user.py : This program tweets to a user as soon as they post a tweet. Useful for bugging your local politician about the status of, say, promised free wifi. Careful about this, excessive spamming may get you banned.

3)tweetto_user_shuf.py: This program tweets the text of a tweet back to a user after shuffling the words around. 

4)gettweets.py : This program downloads the latest 3000 tweets of a user and stores them in a file called "tweetcorpus". 

5)markov.py : This program implements a markov chain on the downloaded "tweetcorpus" file. 

6)markovimproved.py : This program improves on the previous markov chain program. Details are documented in the code. 

