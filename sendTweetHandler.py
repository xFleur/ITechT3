# TODO handle the sending of tweets. This is also the place where we
#   would catch errors and handle them when something goes wrong.
import random

POLITE_WORDS = ["perhaps", "possibly", "perchance", "please", "kindly"]
POLITE_RESPONSES = [
    "Look at you being polite! ",
    "Thank you for making my day! ",
    "You are such a nice person! ",
    "You rock! ",
    "Keep up your kindness! ",
]

def send_tweet(tweet_string, name, message=""):
    polite_string = ""
    if message_is_polite(message):
        polite_string = random.choice(POLITE_RESPONSES)
    print("@" + name + " " + polite_string + tweet_string)


def message_is_polite(message):
    for polite_word in POLITE_WORDS:
        if polite_word in message:
            return True

    return False
