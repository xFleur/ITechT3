#!/usr/bin/python

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

def twitter_demo():
    game = GameInstance('Henk')
    time.sleep(.5)
    game.participant_answer("Yes")
    time.sleep(.5)
    game.participant_answer("No")
    time.sleep(.5)
    game.participant_answer("Yes")
    time.sleep(.5)
    game.participant_answer("I am not going to tell you")
    time.sleep(.5)
    game.participant_answer("I am niNe years old")
    time.sleep(.5)
    game.participant_answer("I like to play at the playground with my friend Josh")
    time.sleep(.5)
    game.participant_answer("I really really love names")

    # # connect to api with apikeys
    # # if you don't have apikeys, go to apps.twitter.com
    # api = twitter.Api(consumer_key='xUphY2Q8YcgvAPJdnAQi3fPMx',
    #                   consumer_secret='M8fwf4s7jcTNzZzZhDyDqJhSAs2AmGDVNcw0LyIjEYyNrWz7yf',
    #                   access_token_key='1504001914530373638-AL3OwiZjx2UaV9EfMOtGpg9GFPyYBG',
    #                   access_token_secret='Er8q5Z0uz5ZX4tyjjyMoPk31S51uqgd19v8CX2VV1AuJR')
    #
    # # get followers
    # print("Getting a list of accounts I follow on Twitter...")
    # friends = api.GetFriends()
    # friend_ids = [friend.id for friend in friends]
    # for friend in friends:
    #     print("Friend: ", friend.name, friend.screen_name, friend.id)
    #
    # # get a list of accounts that are following me
    # print("Getting a list of followers from Twitter...")
    # followers = api.GetFollowers()
    # followers_ids = [user.id for user in followers]
    # for follower in followers:
    #     print("Follower: ", follower.name, follower.screen_name, follower.id)
    #
    # # look up the user_id of a single user
    # print("Looking up the details of screenname @jd7h...")
    # print(api.UsersLookup(screen_name=["jd7h"]))
    # # this should output: [User(ID=222060384, ScreenName=jd7h)]
    #
    # #tweeting
    # body = "This is a tweet. Chirp chirp. Hello world!!"
    # print("Posting tweet...")
    # result = api.PostUpdate(body)
    #
    # # mentions:
    # body = "@jd7h My Twitter bot is working!"
    # print("Posting tweet with mention...")
    # result = api.PostUpdate(body) # including the screenname (prepended by a '@') in the tweet-body is enough to create a mention.
    #
    # # replying to a tweet:
    # itech_tweet_id = 1178660081648492545 # tweet id of the tweet https://twitter.com/jd7h/status/1178660081648492545
    # body = "I ran your script with change!"
    # print("Posting reply...")
    # result = api.PostUpdate(body, in_reply_to_status_id=itech_tweet_id, auto_populate_reply_metadata=True)
    #
    # # other useful stuff:
    # # creating a private list
    # print("Creating a private list...")
    # mylist = api.CreateList(name="My beautiful list", mode="private", description=("A secret list I created on " + time.strftime("%Y-%m-%d")))
    #
    # # Add all users from 'Following' to the new list
    # print("Adding friends to the newly created list...")
    # for friend_id in friend_ids:
    #     print("Adding ", friend_id)
    #     result = api.CreateListsMember(list_id=mylist.id, user_id=friend_id)

twitter_demo()