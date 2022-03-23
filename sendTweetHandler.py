# TODO handle the sending of tweets. This is also the place where we
#   would catch errors and handle them when something goes wrong.
import random
import twitter

POLITE_WORDS = ["perhaps", "possibly", "perchance", "please", "kindly"]
POLITE_RESPONSES = [
    "Look at you being polite! ",
    "Thank you for making my day! ",
    "You are such a nice person! ",
    "You rock! ",
    "Keep up your kindness! ",
]

api = twitter.Api(consumer_key='xUphY2Q8YcgvAPJdnAQi3fPMx',
                  consumer_secret='M8fwf4s7jcTNzZzZhDyDqJhSAs2AmGDVNcw0LyIjEYyNrWz7yf',
                  access_token_key='1504001914530373638-AL3OwiZjx2UaV9EfMOtGpg9GFPyYBG',
                  access_token_secret='Er8q5Z0uz5ZX4tyjjyMoPk31S51uqgd19v8CX2VV1AuJR')


def send_tweet(tweet_string, name, status_id, message=""):
    polite_string = ""
    if message_is_polite(message):
        polite_string = random.choice(POLITE_RESPONSES)
    print()
    body = "@" + name + " " + polite_string + tweet_string
    print(body)
    api.PostUpdate(body, in_reply_to_status_id=status_id, auto_populate_reply_metadata=True)


def message_is_polite(message):
    for polite_word in POLITE_WORDS:
        if polite_word in message:
            return True

    return False
