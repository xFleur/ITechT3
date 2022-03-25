import random

from gameTopicsCollection import KID_TOPICS_PLAYGROUND, KID_TOPICS_HOME, \
    ADULT_TOPICS_PIZZA, ADULT_TOPICS_DINNER, ADOLESCENT_TOPICS_MUSIC, ADOLESCENT_TOPICS_NETFLIX, GAME_TOPIC_NATURE, \
    GAME_TOPIC_TEL_PROGRAMS, GAME_TOPIC_DUTCH_MUSIC, GAME_TOPIC_GEOGRAPHY, GAME_TOPIC_FILMS, GAME_TOPIC_MUSIC
from helpers import answer_is_yes, tokenize_string, text2int, array_to_sum_of_words
from sendTweetHandler import send_tweet

GAME_STATUS_INIT = "init"
GAME_STATUS_ALIGN = "align"
GAME_STATUS_GUESS = "guess"
GAME_STATUS_DONE = "done"

AGE_THRESHOLD_KID = 10
AGE_THRESHOLD_ADOLESCENT = 23

USER_KID = "kid"
USER_ADOLESCENT = "adolescent"
USER_ADULT = "adult"

CLOSE_ANSWERS = [
    "You are really close 🔥🔥, your answer contains the correct word #soCloseButYetSoFarAway 🎯!",
    "Almost there, the correct word is in your answer 🔥🔥!",
    "Almost there, here is a free 🆓🆓 hint #winning: You have already named the correct word in your previous answer!"
]

WONG_ANSWERS = [
    "That is not correct ❌❌, however, you were close ✅✅ but not close enough #almostThere. Do you want to try "
    "again #repeat, or do you need a hint 🕵️🕵️?",
    "That was not the right answer ❌❌, you should try again ✅✅! Or you can ask for a hint 🕵️🕵️ and we will give you "
    "one! #youreWelcome #noProblem",
]

HINT_TEXT = [
    "Okay, here is another hint #oneStepCloser! ✅🎉:",
    "Another hint, smart move #hintHunt 🧠🧠! here you go:",
    "You ask, we deliver #deliveryGuy #fasterThanDhl 🚚🚚! here you go:"
]

GREETS = ["Yo", "Hiii", "Hi", "Hey", "Hello", "Good day", "Good morning", "Good evening", "What's up", "Whats up"]


class GameInstance:
    name = ""
    gameStatus = GAME_STATUS_INIT
    playerAge = None
    playerAgeGroup = None
    # This is the question number of the current phase. Whenever you switch to a new phase, the question counter resets.
    questionNumber = 0
    currentScore = 25000

    activeWord = None

    tweet_status_id = None

    def __init__(self, player_name, answer, status_id):
        self.name = player_name
        self.tweet_status_id = status_id

        self.greet(answer)

    def greet(self, answer):
        greet_word = "Hello"
        lowercase_answer = answer.lower()
        for greet in GREETS:
            if greet.lower() in lowercase_answer:
                greet_word = greet
                break

        send_tweet(f"{greet_word}, {self.name}! Welcomeeeeeee to the 30 second quiz 🎉🎉 #fun #beatyourfriends do you "
                   f"want to play?", self.name, self.tweet_status_id, lowercase_answer)

    def participant_answer(self, answer, new_status_id):
        self.tweet_status_id = new_status_id

        lowercase_answer = answer.lower().replace("@quizmeester ", "")
        if self.gameStatus == GAME_STATUS_INIT and self.questionNumber == 0:
            self.introduce_game(lowercase_answer)
        elif self.gameStatus == GAME_STATUS_INIT and self.questionNumber == 1:
            self.validate_start(answer)
        elif self.gameStatus == GAME_STATUS_ALIGN and self.questionNumber == 0:
            self.ask_for_age(lowercase_answer)
        elif self.gameStatus == GAME_STATUS_ALIGN and self.questionNumber == 1:
            self.handel_personal_question_answer(lowercase_answer)
        elif self.gameStatus == GAME_STATUS_ALIGN and self.questionNumber == 2:
            self.pick_category(lowercase_answer)
        elif self.gameStatus == GAME_STATUS_GUESS:
            self.guess(lowercase_answer)

    def introduce_game(self, answer):
        if answer_is_yes(answer):
            send_tweet(
                "Okay let's go 🏎! But first, here are some rules #boring 📚🥱🥱: Add the mention @ QuizMeester each "
                "time you reply; Write a reply to the last message of the @ QuizMeester, is everything clear?",
                self.name,
                self.tweet_status_id,
                answer
            )
            self.questionNumber += 1
        else:
            send_tweet("Too bad 🛁, you are missing out! 😩😩", self.name, self.tweet_status_id, answer)
            self.reset()

    def validate_start(self, answer):
        if answer_is_yes(answer):
            self.start_align(answer)

        else:
            send_tweet(
                "Okay, let me repeat myself #noproblem. The rules are Add the mention @ QuizMeester each time you "
                "reply; Write a reply to the last message of the @ QuizMeester. Do you get it now? 📚📚",
                self.name, self.tweet_status_id, answer)

    def start_align(self, answer):
        self.gameStatus = GAME_STATUS_ALIGN
        self.questionNumber = 0
        send_tweet("#Sweet 🍰🍰! Let me ask you some personal questions first, so that I can think of fitting "
                   "categories for you! #gettingToKnowEachOther #personal. The first questions is: How old are you? "
                   "👥👥", self.name, self.tweet_status_id, answer)

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
            self.ask_personal_question(answer)
        else:
            send_tweet("I did not get that, come again please? #notGameOverButTryingAgain ⁉️⁉️", self.name, self.tweet_status_id, answer)

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

    def ask_personal_question(self, answer):
        if self.playerAgeGroup == USER_KID:
            send_tweet(f"Already {self.playerAge}?! And are you playing most of the time at the playground or at home? "
                       f"#funTimes 😎😎", self.name, self.tweet_status_id, answer)
        elif self.playerAgeGroup == USER_ADOLESCENT:
            send_tweet(f"{self.playerAge} was my favorite age 😎😎! When meeting friends 👯👯‍️, do you watch Netflix "
                       f"📺 or do you play music 🎧🎤 together? #newestepisodeofriverdale #karaoke", self.name, self.tweet_status_id, answer)
        elif self.playerAgeGroup == USER_ADULT:
            send_tweet(f"What a coincidence 😀 I just turned {self.playerAge}! Quick question! Pizza 🍕🍕 or 3-course "
                       f"dinner 🍽🍽? #yummy", self.name, self.tweet_status_id, answer)

    def handel_personal_question_answer(self, answer):
        topics = []
        if self.playerAgeGroup == USER_KID:
            if "playground" in answer:
                send_tweet("Oooh, the playground?!? Really adventurous, aren’t you! #adventure", self.name, self.tweet_status_id, answer)
                topics = KID_TOPICS_PLAYGROUND
            elif "home" in answer:
                send_tweet(" I also like to stay at home; All of my drawings are there! #drawingIsCool #stayAtHomeMom",
                           self.name, self.tweet_status_id, answer)
                topics = KID_TOPICS_HOME
        elif self.playerAgeGroup == USER_ADOLESCENT:
            topics = ADOLESCENT_TOPICS_NETFLIX
            if "music" in answer:
                send_tweet("I knew it! Everyone likes music 🎤💃 #musicRocks", self.name, self.tweet_status_id, answer)
                topics = ADOLESCENT_TOPICS_MUSIC
            elif "netflix" in answer:
                send_tweet("I knew it! Every one likes Netflix! 📺📺 #tellynights", self.name, self.tweet_status_id, answer)
        elif self.playerAgeGroup == USER_ADULT:
            if "pizza" in answer:
                topics = ADULT_TOPICS_PIZZA
                send_tweet("I love pizza to! I would eat it every day but you've got to stay healthy right? 🏥🍎🍏 ",
                           self.name,
                           self.tweet_status_id,
                           answer
                           )
            if "dinner" in answer:
                topics = ADULT_TOPICS_DINNER
                send_tweet("Oooh look at you, the fancy dinner kind of person! I like it 🔥🔥", self.name, self.tweet_status_id, answer)

        self.questionNumber += 1
        send_tweet(f"I think that I know you a bit better now 🕵️🕵️. I think that you might be interested in the "
                   f"following topics , which one do you like best 🙌🙌, {array_to_sum_of_words(topics)}?", self.name,
                   self.tweet_status_id,
                   answer)

    def reset(self):
        self.name = ""
        self.gameStatus = GAME_STATUS_INIT
        self.playerAge = None
        self.playerAgeGroup = None
        self.questionNumber = 0

    def pick_category(self, answer):
        selected_topic = []

        if "television" in answer:
            selected_topic = GAME_TOPIC_TEL_PROGRAMS
        elif "nature" in answer:
            selected_topic = GAME_TOPIC_NATURE
        elif "dutch" in answer:
            selected_topic = GAME_TOPIC_DUTCH_MUSIC
        elif "geography" in answer:
            selected_topic = GAME_TOPIC_GEOGRAPHY
        elif "films" in answer:
            selected_topic = GAME_TOPIC_FILMS
        elif "music" in answer:
            selected_topic = GAME_TOPIC_MUSIC

        self.activeWord = random.choice(selected_topic)
        if self.activeWord is not None:
            self.gameStatus = GAME_STATUS_GUESS
            self.questionNumber = 0;
            send_tweet(f"I've got a word in my mind! 🧠🧠 #inMyBrainButNotInYours. "
                       f"The first hint that you get is '{self.activeWord.get_random_hint()}'", self.name, self.tweet_status_id, answer)

    def guess(self, answer):
        self.questionNumber += 1
        if str(self.activeWord.word) == str(answer):
            print("Win")
            send_tweet(
                f"That is correct, and only in {self.questionNumber} tries!!! 🎉🎉🥳💯💯 #youarethebest "
                f"#winnerwinnerchickendinner. That was fun! #gamemeesterRules #no1",
                self.name,
                self.tweet_status_id,
                answer
            )
            send_tweet(
                f"Your amazing score is: {self.currentScore} points 🔥🔥! #wow #impressive #cool #neverbeendonebe4 "
                f"score. "
                f"Thanks for playing!", self.name, self.tweet_status_id, answer)
            self.gameStatus = GAME_STATUS_DONE
        elif self.activeWord.word in answer:
            print("almost win")
            send_tweet(f"Try {self.questionNumber}: {random.choice(CLOSE_ANSWERS)}", self.name, self.tweet_status_id, answer)
            self.currentScore -= 100
        elif "hint" in answer or "tip" in answer:
            print("Hint")
            hint = self.activeWord.get_random_hint()
            if hint is not False:
                send_tweet(f"Try {self.questionNumber}: {random.choice(HINT_TEXT)} '{hint}'", self.name, self.tweet_status_id, answer)
            else:
                print("Out of hints")
                send_tweet(f"Try {self.questionNumber}: I'm sorry, but I do not know any more hints... 😭😭🥲 #isThisIt #tears #sorryNotSorry",
                           self.name,
                           self.tweet_status_id,
                           answer
                           )
            self.currentScore -= 1000
        else:
            print("Lose")
            send_tweet(f"Try {self.questionNumber}: {random.choice(CLOSE_ANSWERS)}", self.name, self.tweet_status_id, answer)
            self.currentScore -= 500
