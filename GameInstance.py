import random

from gameTopicsCollection import KID_TOPICS_PLAYGROUND, KID_TOPICS_HOME, \
    ADULT_TOPICS_PIZZA, ADULT_TOPICS_DINNER, ADOLESCENT_TOPICS_MUSIC, ADOLESCENT_TOPICS_NETFLIX, GAME_TOPIC_NAMES, \
    GAME_TOPIC_COLORS
from helpers import answer_is_yes, tokenize_string, text2int, array_to_sum_of_words
from sendTweetHandler import sendTweet

GAME_STATUS_INIT = "init"
GAME_STATUS_ALIGN = "align"
GAME_STATUS_GUESS = "guess"

AGE_THRESHOLD_KID = 10
AGE_THRESHOLD_ADOLESCENT = 23

USER_KID = "kid"
USER_ADOLESCENT = "adolescent"
USER_ADULT = "adult"


class GameInstance:
    name = ""
    gameStatus = GAME_STATUS_INIT
    playerAge = None
    playerAgeGroup = None
    # This is the question number of the current phase. Whenever you switch to a new phase, the question counter resets.
    questionNumber = 0

    activeWord = None

    def __init__(self, player_name):
        self.name = player_name

        self.greet()

    def greet(self):
        sendTweet(f"Hello {self.name}! Welcomeeeeeee to the 30 second quiz 🎉🎉 #fun #beatyourfriends do you want to "
                  f"play?")

    def participant_answer(self, answer):
        print("PLAYER: " + answer)
        lowercase_answer = answer.lower()
        if self.gameStatus == GAME_STATUS_INIT and self.questionNumber == 0:
            self.introduce_game(lowercase_answer)
        elif self.gameStatus == GAME_STATUS_INIT and self.questionNumber == 1:
            self.validate_start(answer)
        elif self.gameStatus == GAME_STATUS_ALIGN and self.questionNumber == 0:
            self.ask_for_age(lowercase_answer)
        elif self.gameStatus == GAME_STATUS_ALIGN and self.questionNumber == 1:
            self.handel_personal_question_answer(answer)
        elif self.gameStatus == GAME_STATUS_ALIGN and self.questionNumber == 2:
            self.pick_category(answer)

    def introduce_game(self, answer):
        if answer_is_yes(answer):
            sendTweet("Okay let's go 🏎! But first, here are some rules #boring 📚🥱🥱: Blablabla, is everything clear?")
            self.questionNumber += 1
        else:
            sendTweet("Too bad 🛁, you are missing out! 😩😩")
            self.reset()

    def validate_start(self, answer):
        if answer_is_yes(answer):
            self.start_align()

        else:
            sendTweet("Okay, let me repeat myself #noproblem. The rules are blablalablalba. Do you get it now? 📚📚")

    def start_align(self):
        self.gameStatus = GAME_STATUS_ALIGN
        self.questionNumber = 0
        sendTweet("#Sweet 🍰🍰! Let me ask you some personal questions first, so that I can think of fitting "
                  "categories for you! #gettingToKnowEachOther #personal 👥👥")

    def ask_for_age(self, answer):
        self.playerAge = self.get_number_from_string(answer)
        if self.playerAge:
            if self.playerAge <= AGE_THRESHOLD_KID:
                self.playerAgeGroup = USER_KID
            elif self.playerAge <= AGE_THRESHOLD_ADOLESCENT:
                self.playerAgeGroup = USER_ADOLESCENT
            else:
                self.playerAgeGroup = USER_ADULT
            self.questionNumber += 1
            self.ask_personal_question()
        else:
            sendTweet("I did not get that, come again please? #notGameOverButTryingAgain ⁉️⁉️")

    # Note that this method only gets the first number in a sentence.
    @staticmethod
    def get_number_from_string(answer):
        # Check if there is an actual number in the sentence
        number = [int(s) for s in answer.split() if s.isdigit()]
        if len(number) > 0:
            return number[0]

        # Check if there is a number in text in the sentence.
        exploded_answers = tokenize_string(answer)
        for answer in exploded_answers:
            number = text2int(answer)
            if number is not None:
                return number

    def ask_personal_question(self):
        if self.playerAgeGroup == USER_KID:
            sendTweet(f"Already {self.playerAge}?! And are you playing most of the time at the playground or at home? "
                      f"#funTimes 😎😎")
        elif self.playerAgeGroup == USER_ADOLESCENT:
            sendTweet(f"{self.playerAge} was my favorite age 😎😎! When meeting friends 👯👯‍️, do you watch Netflix "
                      f"📺 or do you play music 🎧🎤 together? #newestepisodeofriverdale #karaoke")
        elif self.playerAgeGroup == USER_ADULT:
            sendTweet("Quick question! Pizza 🍕🍕 or 3-course dinner 🍽🍽?")

    def handel_personal_question_answer(self, answer):
        topics = []
        if self.playerAgeGroup == USER_KID:
            if "playground" in answer:
                sendTweet("Cool! I like the playground too!")
                topics = KID_TOPICS_PLAYGROUND
            elif "home" in answer:
                sendTweet("I bet you live in a cool home!")
                topics = KID_TOPICS_HOME
        if self.playerAgeGroup == USER_ADOLESCENT:
            topics = ADOLESCENT_TOPICS_NETFLIX
            if "music" in answer:
                sendTweet("I knew it! Everyone likes music")
                topics = ADOLESCENT_TOPICS_MUSIC
            elif "netflix" in answer:
                sendTweet("I knew it! Every one likes netflix!")
        if self.playerAgeGroup == USER_ADULT:
            if "pizza" in answer:
                topics = ADULT_TOPICS_PIZZA
            if "dinner" in answer:
                topics = ADULT_TOPICS_DINNER


        self.questionNumber += 1
        sendTweet(f"I think that I know you a bit better now. I think that you might be interested in the following "
                  f"topics, which one do you like best, {array_to_sum_of_words(topics)}?")

    def reset(self):
        self.name = ""
        self.gameStatus = GAME_STATUS_INIT
        self.playerAge = None
        self.playerAgeGroup = None
        self.questionNumber = 0

    def pick_category(self, answer):
        selected_topic = []

        if "name" in answer:
            selected_topic = GAME_TOPIC_NAMES
        elif "color" in answer:
            selected_topic = GAME_TOPIC_COLORS

        self.activeWord = random.choice(selected_topic)
        if self.activeWord is not None:
            self.gameStatus = GAME_STATUS_GUESS
            print(self.activeWord.word)
