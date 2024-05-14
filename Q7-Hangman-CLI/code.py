
# Exercise Name:
# 	07-Hangman-CLI
# Description:
# 	Create a hangman CLI game
# Rough game logic:
# 	1. Pick a random word. (Initially just use a hardcoded word like 'watermelon'. Random selection can be done later.)
# 	2. Initialize Guess Count to 6
# 	3. Show one underscore for each character in the word. For example, in case of 'watermelon', show 10 underscores like: _ _ _ _ _ _ _ _ _ _ 
# 	4. Prompt user to input their guess
# 		- Show a sorted list of already guessed characters
# 		- Guess should be ONE character from the alphabet
# 		- Guessed character should be new and not have been previously guessed
# 	5. Check if that character exists in the selected word
# 		a. If the character exists, reveal the character in its position. 
# 		   For example, in case of 'watermelon' and user guessed 'e', show: _ _ _ e _ _ e _ _ _
# 		b. If the character does not exist in the selected word, show warning and decrement Guess Count by one
# 	6. If the Guess Count
# 		a. is greater than zero, loop and take another input
# 		b. becomes zero before guessing all the characters in the word, Game Over.
# For improvement:
# 	https://random-word-api.herokuapp.com/word


import requests

def select_word():
        response = requests.get('https://random-word-api.herokuapp.com/word')
        word = response.json()[0]  # Extract the first word from the response
        return word.lower()  # Convert the word to lowercase for consistency

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter + ' '
        else:
            display += '_ '
    return display.strip()

def hangman():
    word = select_word()
    guessed_letters = []
    guess_count = 6

    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))

    while guess_count > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct!")
            print(display_word(word, guessed_letters))
        else:
            guess_count -= 1
            print("Incorrect! You have {} guesses left.".format(guess_count))
            print(display_word(word, guessed_letters))

        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You guessed the word: {}".format(word))
            break

    else:
        print("Game Over. The word was: {}".format(word))

hangman()
