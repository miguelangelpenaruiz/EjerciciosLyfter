import random

class GameBase():
    len_word = 4
    user_tries = 3

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
        if self.user_tries == 0:
            raise ValueError('No tries left')
        if user_participation_word != self.selected_word:
            self.user_tries += -1
            return False
        else:
            return user_participation_word == self.selected_word

    def game_over_method(self):
        return self.user_tries == 0


class BackwardsMixin():

    def backwards(self):
        return self.selected_word[::-1]

class HideLettersMixin():
    def hide_letters(self):
        letters = list(self.selected_word)
        letters[1] = "-"
        letters[3] = "-"
        hidden = "".join(letters)
        return hidden

class GameModeEasy(BackwardsMixin, GameBase):
    pass

class GameModeMedium(HideLettersMixin, GameBase):
    pass

