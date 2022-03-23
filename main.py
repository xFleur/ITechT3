#!/usr/bin/python
import subprocess
import time
import twitter #for docs, see https://python-twitter.readthedocs.io/en/latest/twitter.html

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


def user_has_session(name):
    return name in list_of_users


def twitter_demo():
    api = twitter.Api(consumer_key='xUphY2Q8YcgvAPJdnAQi3fPMx',
                      consumer_secret='M8fwf4s7jcTNzZzZhDyDqJhSAs2AmGDVNcw0LyIjEYyNrWz7yf',
                      access_token_key='1504001914530373638-AL3OwiZjx2UaV9EfMOtGpg9GFPyYBG',
                      access_token_secret='Er8q5Z0uz5ZX4tyjjyMoPk31S51uqgd19v8CX2VV1AuJR')

    # game = GameInstance('Henk', 'Yo, this is the first message that starts the chat, #fun')
    status_id_test = 1506562629917155328
    tweet = api.GetStatus(status_id=1506562629917155328, trim_user=True)
    print(tweet.text)
    uid = tweet.user.id
    user = api.GetUser(user_id=uid)
    screen_name = user.screen_name

    list_of_users.append(screen_name)

    if user_has_session(screen_name):
        game = GameInstance(screen_name, tweet.text, 1506562629917155328)

    while True:
        try:
            input_string = input()
            game.participant_answer(input_string, 1506562629917155328)
        except Exception as e:
            print("Error:", e)


    def getMentions():
        return api.GetMentions()


twitter_demo()
