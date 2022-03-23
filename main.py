#!/usr/bin/python
import subprocess
import time
import twitter  # for docs, see https://python-twitter.readthedocs.io/en/latest/twitter.html
import threading
from GameInstance import GameInstance

'''
USE AT YOUR OWN PERIL <3
fill in your API keys before running the script
written in Python3 by Judith van Stegeren, @jd7h
'''

'''
before running the script, do this:
1. create a virtual environment
$ python -m venv venv
$ source venv/bin/activate
2. install the dependencies
$ pip install python-twitter
3. obtain API keys from twitter
4. fill them in in the script below
'''

list_of_users = []

api = twitter.Api(consumer_key='xUphY2Q8YcgvAPJdnAQi3fPMx',
                  consumer_secret='M8fwf4s7jcTNzZzZhDyDqJhSAs2AmGDVNcw0LyIjEYyNrWz7yf',
                  access_token_key='1504001914530373638-AL3OwiZjx2UaV9EfMOtGpg9GFPyYBG',
                  access_token_secret='Er8q5Z0uz5ZX4tyjjyMoPk31S51uqgd19v8CX2VV1AuJR')


def user_has_session(name):
    return name in list_of_users


class TweetFetcher:
    last_tweet_id = 0
    game = None
    first_tweet = False

    def __init__(self):
        self.fetch_tweets()

    def fetch_tweets(self):

        threading.Timer(10.0, self.fetch_tweets).start()
        mentions = api.GetMentions()
        tweet = mentions[0]

        if not self.first_tweet:
            self.first_tweet = True
            self.last_tweet_id = mentions[0].id
            return

        if tweet.id != self.last_tweet_id:
            uid = tweet.user.id
            user = api.GetUser(user_id=uid)
            screen_name = user.screen_name

            print("Nieuwe tweet ontvangen")
            print(tweet.text)

            if user_has_session(screen_name):
                print(user_has_session(screen_name))
                print(list_of_users)
                self.game.participant_answer(tweet.text, mentions[0].id)
            else:
                list_of_users.append(screen_name)
                self.game = GameInstance(screen_name, tweet.text, mentions[0].id)

        self.last_tweet_id = mentions[0].id


TweetFetcher()

# def twitter_demo():
#     # game = GameInstance('Henk', 'Yo, this is the first message that starts the chat, #fun')
#     status_id_test = 1506562629917155328
#     tweet = api.GetStatus(status_id=1506562629917155328, trim_user=True)
#     print(tweet.text)
#     uid = tweet.user.id
#     user = api.GetUser(user_id=uid)
#     screen_name = user.screen_name
#
#
#
#     while True:
#         try:
#             input_string = input()
#             game.participant_answer(input_string, 1506562629917155328)
#         except Exception as e:
#             print("Error:", e)
#
#     def getMentions():
#         return api.GetMentions()
#
# # twitter_demo()
