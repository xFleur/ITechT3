import random


# Model for the guesswords which allows us to handle hints easily.
class GuessWord:
    word = ""
    hints = []

    def __init__(self, word, hints):
        self.word = word
        self.hints = hints

    def get_random_hint(self):
        # Check if there are any hints left and return false if not the case.
        if len(self.hints) == 0:
            return False

        # Get a random hint
        hint = random.choice(self.hints)

        # Remove this hint from the array in order to avoid duplicate hints.
        self.hints.remove(hint)

        return hint
