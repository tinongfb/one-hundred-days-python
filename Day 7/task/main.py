import random

# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py

lives = 6

# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo
print(logo)
chosen_word = random.choice(word_list)
letter_count = len(chosen_word)
#print(f"chosen word '{chosen_word}' has {letter_count} letters")
# TODO-6: - Update the code below to tell the user how many lives they have left.
print(f"****************************{lives}/6 LIVES LEFT****************************")
print(f"The chosen word has {letter_count} letters")

# placeholder = ""
# word_length = len(chosen_word)
# for position in range(word_length):
#     placeholder += "_"
# print("Word to guess: " + placeholder)


game_over = False
letters_not_in_word = []
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()
    placeholder = "_" * letter_count
    #print(placeholder)

    # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.

    word = []

    for letter in chosen_word:
        if letter == guess:
            word.append(guess)
            correct_letters.append(guess)
        elif letter in correct_letters:
            word.append(letter)
        else:
            word.append("_")

    if guess not in correct_letters:
        letters_not_in_word.append(guess.upper())
        print(f"You guessed '{guess.upper()}', it is not in the word.")
        lives -= 1
        if lives == 0:
            game_over = True


    print("Current guess: " + "".join(word))
    # print(f"correct guesses: {correct_letters}")
    print(f"Incorrect guess(es): {letters_not_in_word}")

    # display = ""
    #
    # for letter in chosen_word:
    #     if letter == guess:
    #         display += letter
    #         correct_letters.append(guess)
    #     elif letter in correct_letters:
    #         display += letter
    #     else:
    #         display += "_"

    #print("Word to guess: " + display)

    # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
    #  e.g. You guessed d, that's not in the word. You lose a life.

    if guess not in chosen_word:
        if lives == 0:
            game_over = True

            # TODO 7: - Update the print statement below to give the user the correct word they were trying to guess.
            #print(f"***********************YOU LOSE**********************")
            print(f"The word was: {chosen_word}")
            print(" ********************** Game over, no more lives left **********************")

    if "_" not in word:
        game_over = True
        print("You guessed the word! The word is: " + "".join(word))
        print(" ********************** You win! Game over ********************** ")
        #print("****************************YOU WIN****************************")

    # TODO-2: - Update the code below to use the stages List from the file hangman_art.py
    print(f"Lives left: {lives}/6")
    print(stages[lives])
