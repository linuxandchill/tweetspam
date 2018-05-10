import sys
import json
import time
import logging
import twitter
import urllib.parse

from os import environ as e

api = twitter.Api(
    consumer_key = 'MwRbyrYDpVl3ezaB52YL843hJ',
    consumer_secret = 'OAMbMfDzfls2DNEhEr3UccPYSFl5Q3NOARqUkrPy7IUjhOW7rJ',
    access_token_key = '2345928691-7D0naC0qmw8iXOpaGbtf7ng7bssHqnXfMsBtx1d',
    access_token_secret = 'ZyqV0Vasxw9GNyHTLb0u9AUW2H146bF7g5C0bj9E4UBKp')

t = api.GetUserTimeline(screen_name="tylerwhatsgood_", count=2)
tweets = [i.AsDict() for i in t]

#returns all tweets
def get_tweets():
    t = api.GetUserTimeline(screen_name="_pivx", count=3)
    tweets = [i.AsDict() for i in t]
    tweet_text = []

    for t in tweets:
        text = t['text']
        tweet_text.append(text)

    return tweet_text

tweet_list = get_tweets()
print(tweet_list[0])

def loop_through_tweets():
    first_tweet = get_tweets()
    print()


def get_replies():
    username = get_tweets()

def tweetAndID():
    dicty = {}

    for t in tweets:
        ID, text = t['id'], t['text']
        dicty[ID] = text

    print(dicty)


def tweet_indexed():
    tweet_texts = []

    for t in tweets:
        ID, text = t['id'], t['text']
        tweet_texts.append(text)

    print(tweet_texts)
    for index, item in enumerate(tweet_texts):
        print(f"{index}: {item}") 

    return tweet_texts




'''
    dumped = json.dumps(t)
    fmtd = json.loads(dumped)
    print(fmtd["text"])
'''
