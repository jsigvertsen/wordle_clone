import random

import word_bank


class Wordle:
    def __init__(self):
        self.word = random.choice(word_bank.words)
        self.counter = 0
        self.display = []

    def guess(self):
        while True:
            guess = input('Enter a 5 letter word: ')
            try:
                guess = str(guess)
                if len(guess) == 5:
                    return guess.lower()
                else:
                    continue
            except ValueError:
                print('Enter a 5 letter word.')

    def player_guess(self):
        board = ''
        word = self.word
        guess = Wordle.guess(self)
        for i in range(len(word)):
            if word[i] == guess[i]:
                board += guess[i].upper()
                continue
            elif guess[i] in word:
                board += guess[i].lower()
                continue
            else:
                board += '_'
        self.counter += 1
        self.display += [' '.join([x for x in board])]

    def display_board(self):
        print(f'\nROUND {self.counter}')
        for i in self.display:
            print(i)
        print()

    def check_winner(self):
        if '_' not in list(self.display)[-1] and list(self.display)[-1].isupper():
            print(f'Nice work! You guessed {self.word.upper()} correctly after {self.counter} rounds.\n')
            return True
        elif self.counter == 6:
            print(f'You\'ve run out of guesses. The word was {self.word.upper()}.\n')
            return True
