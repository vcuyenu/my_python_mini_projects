import csv
import random
from collections import defaultdict


def get_guess(letters_guessed):
    guess = input("\nEnter a letter: ").lower()
    if not guess.isalpha():
        print("Only letters allowed!!!")
        return None
    if len(guess) != 1:
        print("Only 1 letter!!!")
        return None
    if guess in letters_guessed:
        print('Already guessed. Guess a differernt letter!!!')
        return None
    
    return guess

def update_state(guess, letters_guessed,word, chance):
    if guess in word: letters_guessed.add(guess)
    else: chance -= 1
    return letters_guessed, chance

def display(word, letters_guessed, chance):
    print("\nWord: ", end = "")
    for ch in word:
        if ch in letters_guessed: print(ch, end = " ")
        else: print("_", end = " ")
    print(f"\n{chance} chances left!!!")

def check_win(word, letters_guessed):
    return all(ch in  letters_guessed for ch in word)

if __name__ == '__main__':
    words = defaultdict(list)
    with open("words.csv", "r") as file:
        reader = csv.reader(file)
        for category, word in reader:
            words[category].append(word)
            
    category = random.choice(list(words.keys()))
    word = random.choice(words[category])

    print("Category: ", category)
    print(f'{len(word)} letters!!!')
    print("Word: ", end = '')
    print("_ " * len(word))

    letters_guessed = set()
    chance = len(word) + 2

    while chance > 0:
        guess = get_guess(letters_guessed)
        if guess is None: continue

        letters_guessed, chance = update_state(guess, letters_guessed, word, chance)

        display(word, letters_guessed, chance)

        if check_win(word, letters_guessed):
            print("YOU WIN!!!: ", word)
            break

    else: print("You lost!: ", word)




