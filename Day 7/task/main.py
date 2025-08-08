import random

word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
chosen_word = random.choice(word_list)
print(f"the random word is '{chosen_word}'")

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = (input("guess a letter: ")).lower()

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.
if guess in chosen_word:
    print("Right")
else:
    print("Wrong")

#BELOW:SOLUTION
# def rand_word_function():
#     chosen_word = random.choice(word_list)
#     return chosen_word
#
# def guess_letter_function():
#     guess = (input("Guess a letter: ")).lower()
#     return guess
#
# def guess_in_rand_word_function():
#     chosen_word = rand_word_function()
#     guess = guess_letter_function()
#     print(f"the random word is {chosen_word}")
#     print(f"the chosen letter is {guess}")
#
#     if guess in chosen_word:
#         print("Right")
#     else:
#         print("Wrong")
#
# guess_in_rand_word_function()
#
