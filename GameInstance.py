from helpers import answer_is_yes, tokenize_string, text2int

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

    def __init__(self, player_name):
        self.name = player_name

        self.greet()

    def greet(self):
        print("Hello " + self.name + "!")
        print("Welcomeeeeeee to the 30 second quiz #fun #beatyourfriends do you want to play?")

    def participant_answer(self, answer):
        print("PLAYER: " + answer)
        lowercase_answer = answer.lower()
        if self.gameStatus == GAME_STATUS_INIT:
            self.start_game(lowercase_answer)
        elif self.gameStatus == GAME_STATUS_ALIGN and not self.playerAgeGroup:
            self.ask_for_age(lowercase_answer)
        elif self.gameStatus == GAME_STATUS_ALIGN:
            self.ask_personal_question()


    def start_game(self, answer):
        if answer_is_yes(answer):
            print("Okay let's go! But first, here are some rules #boring: Blablabla, is everything clear?")
            self.start_align()
        else:
            print("Too bad, you are missing out!")

    def start_align(self,):
        self.gameStatus = GAME_STATUS_ALIGN
        print("Okay, let me ask you some personal questions first, so that I can think of fitting categories for you! #gettingToKnowEachOther #personal")
        print(self.name + ", I was wondering, how old are you? #lifeExperience")

    def ask_for_age(self, answer):
        self.playerAge = self.get_number_from_string(answer)
        if self.playerAge:
            print(str(self.playerAge) + " was my favorite age! #excitingTimes")
            if self.playerAge >= AGE_THRESHOLD_KID:
                self.playerAgeGroup = AGE_THRESHOLD_KID
            else:
                if self.playerAge >= AGE_THRESHOLD_KID:
                    self.playerAgeGroup = USER_KID
                elif self.playerAge >= AGE_THRESHOLD_ADOLESCENT:
                    self.playerAgeGroup = USER_ADOLESCENT
                else:
                    self.playerAgeGroup = USER_ADULT

        else:
            print("I did not get that, come again please? #notGameOverButTryingAgain")

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
        print("This question is very personal")
