import tweepy
import time

from keys import *

print("This is my first python project", flush=True)

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

file_name = "last_seen_id.txt"

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return


def reply_to_tweets():
    print("retrieving and replying to tweets...", flush=True)
    
    last_seen_id = retrieve_last_seen_id(file_name)
    my_timeline = api.home_timeline(last_seen_id, tweet_mode='extended')

    for tweet in my_timeline:
        print(str(tweet.id) + ' ' + tweet.full_text, flush=True)
        last_seen_id = tweet.id
        store_last_seen_id(last_seen_id, file_name)
        if "#RwOT" in tweet.full_text:
            print("FOUND IT!", flush=True)
            print("retweeting and liking...", flush=True)
            api.retweet(tweet.id)
     
while True:
    reply_to_tweets()
    time.sleep(30)
