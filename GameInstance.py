from helpers import answer_is_yes, tokenize_string, text2int
from sendTweetHandler import sendTweet

GAME_STATUS_INIT = "init"
GAME_STATUS_ALIGN = "align"
USER_KID = "kid"
USER_ADOLESCENT = "adolescent"
USER_ADULT = "adult"
AGE_THRESHOLD_KID = 10
AGE_THRESHOLD_ADOLESCENT = 23


class GameInstance:
    name = ""
    gameStatus = GAME_STATUS_INIT
    playerAge = None
    playerAgeGroup = None
    questionNumber = 0

    def __init__(self, player_name):
        self.name = player_name

        self.greet()

    def greet(self):
        sendTweet("Hello " + self.name + "! Welcomeeeeeee to the 30 second quiz #fun #beatyourfriends do you want to play?")

    def participant_answer(self, answer):
        print("PLAYER: " + answer)
        lowercase_answer = answer.lower()
        if self.gameStatus == GAME_STATUS_INIT and self.questionNumber == 0:
            self.introduce_game(lowercase_answer)
        elif self.gameStatus == GAME_STATUS_INIT and self.questionNumber == 1:
            self.validate_start(answer)
        elif self.gameStatus == GAME_STATUS_ALIGN and not self.playerAgeGroup:
            self.ask_for_age(lowercase_answer)
        elif self.gameStatus == GAME_STATUS_ALIGN:
            sendTweet("Good answer!")

    def introduce_game(self, answer):
        if answer_is_yes(answer):
            sendTweet("Okay let's go! But first, here are some rules #boring: Blablabla, is everything clear?")
            self.questionNumber += 1
        else:
            sendTweet("Too bad, you are missing out!")
            self.reset()

    def validate_start(self, answer):
        if answer_is_yes(answer):
            self.start_align()

        else:
            sendTweet("Okay, let me repeat myself #noproblem. The rules are blablalablalba. Do you get it now?")

    def start_align(self):
        self.gameStatus = GAME_STATUS_ALIGN
        sendTweet("#Sweet! Let me ask you some personal questions first, so that I can think of fitting categories for you! #gettingToKnowEachOther #personal")

    def ask_for_age(self, answer):
        self.playerAge = self.get_number_from_string(answer)
        if self.playerAge:
            if self.playerAge <= AGE_THRESHOLD_KID:
                self.playerAgeGroup = USER_KID
            elif self.playerAge <= AGE_THRESHOLD_ADOLESCENT:
                self.playerAgeGroup = USER_ADOLESCENT
            else:
                self.playerAgeGroup = USER_ADULT

            self.ask_personal_question()
        else:
            sendTweet("I did not get that, come again please? #notGameOverButTryingAgain")

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
            sendTweet(f"Already {self.playerAge}?! And are you playing most of the time at the playground or at home? #funTimes")
        elif self.playerAgeGroup == USER_ADOLESCENT:
            sendTweet(f"{self.playerAge} was my favorite age! When meeting friends, do you watch Netflix or do you play music together? #newestepisodeofriverdale #karaoke")
        elif self.playerAgeGroup == USER_ADULT:
            sendTweet("Quick question! Pizza or 3-course dinner?")

    def reset(self):
        self.name = ""
        self.gameStatus = GAME_STATUS_INIT
        self.playerAge = None
        self.playerAgeGroup = None
        self.questionNumber = 0
