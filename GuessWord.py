import random


class GuessWord:
    word = ""
    hints = []

    def __init__(self, word, hints):
        self.word = word
        self.hints = hints

    def get_random_hint(self):
        if len(self.hints) == 0:
            return False

        hint = random.choice(self.hints)
        self.hints.remove(hint)

        return hint
