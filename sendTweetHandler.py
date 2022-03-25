import random
import twitter

# The words that we want to respond kindly too.
POLITE_WORDS = ["perhaps", "possibly", "perchance", "please", "kindly"]

# Our kind responses
POLITE_RESPONSES = [
    "Look at you being polite! ",
    "Thank you for making my day! ",
    "You are such a nice person! ",
    "You rock! ",
    "Keep up your kindness! ",
]

# reinitialize API.
api = twitter.Api(consumer_key='',
                  consumer_secret='',
                  access_token_key='',
                  access_token_secret='')


def send_tweet(tweet_string, name, status_id, message=""):
    # Construct the polite string if received message is polite.
    polite_string = ""
    if message_is_polite(message):
        polite_string = random.choice(POLITE_RESPONSES)

    # construct the body
    body = "@" + name + " " + polite_string + tweet_string
    print(body)

    # Send the tweet as a reply to the old tweet.
    api.PostUpdate(body, in_reply_to_status_id=status_id, auto_populate_reply_metadata=True)


# Detect if the polite word is in the list of words.
def message_is_polite(message):
    for polite_word in POLITE_WORDS:
        if polite_word in message:
            return True

    return False
