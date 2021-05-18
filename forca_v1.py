# -*- coding: utf-8 -*-
# Hangman Game 
# Object Orientation Paradigm Study

import random

board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


class Hangman:
    def __init__(self, word):
        print(word)
        self.word = word
        self.encoded_word = []
        self.current_board = 0
    
    def encode_word(self):
        for x in range(len(self.word)):
            self.encoded_word += '_'

    def show_game(self):
        print(board[self.current_board])
        print(' '.join(self.encoded_word))

    def correct_letter(self, letter):
        if letter in self.word:
            for i in range(len(self.word)):
                if(self.word[i] == letter):
                    self.encoded_word[i] = letter
                else: pass
        else: 
            self.current_board += 1
            print(self.current_board)

def rand_word():
    try:
        with open("palavras.txt", "rt") as f:
            bank = f.readlines()
        return bank[random.randint(0, len(bank) - 1)].strip()
    except:
        print("erro!!!")


def main():

    # Objeto
    game = Hangman(rand_word())
    game.encode_word()
    while(''.join(game.encoded_word) != game.word):
        if(game.current_board == len(board) -1):
            print(board[-1])
            print("a palavra correta era ", game.word)
            break
        game.show_game()
        game.correct_letter(input("Digite uma letra: "))
    if(''.join(game.encoded_word) == game.word):
        print("Parabéns, você venceu!")


if __name__ == "__main__":
    main()
