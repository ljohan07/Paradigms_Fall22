import random
from datetime import datetime
class Wordle:
    def __init__(self, word):
        self.word = word
        self.good = []
        self.bad = []
        self.matches = ["" for i in range(5)]
    
    def generate_lists(self, guess):
        for i, letter in enumerate(guess):
            if letter in self.word:
                if letter not in self.good:
                    self.good.append(letter)
                if self.word[i] == letter:
                    self.matches[i] = letter
            else:
                if letter not in self.bad:
                    self.bad.append(letter)

def main():
    f = open('./words.txt')
    words = f.readlines()
    print(len(words))
    words = [ line.strip() for line in words ]
    rand_ind = random.randint(0, len(words))
    correct_word = words[rand_ind]
    bad_guesses = 0
    guess =''
    print(words[rand_ind])
    game = Wordle(correct_word)



    while bad_guesses < 5 and guess != correct_word:
        guess = input('Enter a five-letter word: ').upper()
        while len(guess) !=  5 or guess not in words:
            guess = input('Bad Input. Enter a valid five-letter word: ').upper()
        if guess == correct_word:
            break
        game.generate_lists(guess)

        
        print("Good letters:", game.good)
        print("Bad letters:",game.bad)
        print("Correct letters:", game.matches)
        bad_guesses += 1

    if guess == correct_word:
        message = "Congratulations, you correctly identified the word after " + str(bad_guesses + 1) + " attempts"
        print(message)
    else:
        message = "The answer is " + correct_word +  ". You did not correctly guess it within 6 tries."
        print(message)

        
main()