# Introduction
Thank you for opening our Twitterbot “QuizMeester” python program! In the following read me, we will guide you through installing the right packages and starting the program. 

## Installation
We used the package “NLTK” and “python-twitter”. The following path shows, where the packages can be installed. You can also install them via your command line or other prefered method.:  

preferences > Project ITech T3 > project interpreter 

Starting the program 

First, you need to add the keys to the lines in the main.py and the sendTweetHandler.py: 

api = twitter.Api(consumer_key='', 
                  consumer_secret='', 
                  access_token_key='’, 
                  access_token_secret='') 

Next, you can run it in python, by configuring your run settings to execute main.py and clicking on the “play button”.

## Files

### Main.py 
Here the game is initialized. This file holds all the games and manages the recieving of tweets. Whenever a tweet is received,
it will send it to the correct game so that the game can be player.

### GameInstance.py
This is the entire game. It is a model with its own states. It handles all the responses that the game can give. Every user has its own instance of the game.

### gameTopicSelection.py 
This is a collection of all the topics that are available in the game with the guesswords.

### GuessWord.py 
This is a model for a guess word. It saves the word and the hints. You can ask it to give you an random hint, and it will deliver one while making sure that there are no duplicates.

### helpers.py 
Random helper functions which are mainly used in the GameInstance

### sendTweetHandler.py
Sends all the tweets and can make them polite if the users asks nicely.