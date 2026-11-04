import random

class GameBase():
    len_word = 4
    user_tries = 3
    game_over = 0

    def __init__(self, list_words):
        self.list_words = list_words
        for word in list_words:
            if len(word) != self.len_word:
                raise ValueError(f'Respect the {self.len_word} characters rule')
        self.selected_word = self.select_word()

    def select_word(self):
        selected_word = random.choice(self.list_words)
        return selected_word

    def user_participation(self, user_participation_word):
        return user_participation_word == self.selected_word

    def game_over(self):
        if self.user_tries == 0:
            self.game_over = 1
            return self.game_over

class BackwardsMixin():

    def backwards(self):
        return self.selected_word[::-1]

class HideLettersMixin():
    def hide_letters(self):
        letters = list(self.selected_word)
        letters[1,3] = "-"
        hidden = "".join(letters)
        return hidden

class GameModeEasy(BackwardsMixin, GameBase):
    pass

class GameModeMedium(HideLettersMixin, GameBase):
    pass

