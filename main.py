#!/usr/bin/python
import twitter  # for docs, see https://python-twitter.readthedocs.io/en/latest/twitter.html
import threading
from GameInstance import GameInstance

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

api = twitter.Api(consumer_key='',
                  consumer_secret='',
                  access_token_key='',
                  access_token_secret='')

# Check if the user is already playing.
def user_has_session(name):
    return name in list_of_users


class TweetFetcher:
    last_tweet_id = 0
    game = None
    first_tweet = False
    games = dict()

    def __init__(self):
        self.fetch_tweets()

    def fetch_tweets(self):
        # Fetch the tweets every 10 seconds.
        threading.Timer(10.0, self.fetch_tweets).start()

        # Get the tweets which we were mentioned in.
        mentions = api.GetMentions()

        # Get the last tweet.
        tweet = mentions[0]

        # Check if we already had a tweet and initialize variables correctly if this was the first tweet..
        if not self.first_tweet:
            self.first_tweet = True
            self.last_tweet_id = mentions[0].id
            return

        # Check if the tweet is new.
        if tweet.id != self.last_tweet_id:
            # Get the user informatino if the tweet is new.
            uid = tweet.user.id
            user = api.GetUser(user_id=uid)
            screen_name = user.screen_name

            print(tweet.text)

            # If the user is already playing, answer the correct instance.
            if user_has_session(screen_name):
                self.games[screen_name].participant_answer(tweet.text, mentions[0].id)
            # If the user was not playing yet, create a new instance for this player.
            else:
                list_of_users.append(screen_name)
                self.games[screen_name] = GameInstance(screen_name, tweet.text, mentions[0].id)

        self.last_tweet_id = mentions[0].id


TweetFetcher()
