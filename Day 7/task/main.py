import random
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
#NOTE : ALL PAGES' SOLUTIONS ARE IN THIS PAGE

# TODO-1: Create a "placeholder" with the same number of blanks as the chosen_word
# TODO-1: - Use a while loop to let the user guess again.
# TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. Set 'lives' to equal 6.
# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py

word_list = ["aardvark", "baboon", "camel"]
lives = 6

chosen_word = random.choice(word_list)
letter_count = len(chosen_word)
print(f"chosen word '{chosen_word}' has {letter_count} letters")

game_over = False
letters_not_in_word = []
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()
    placeholder = "_" * letter_count
    #print(placeholder)

# TODO-2: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.
# TODO-2: Change the for loop so that you keep the previous correct letters in display.
# TODO-2: - If guess is not a letter in the chosen_word, Then reduce 'lives' by 1.
#  If lives goes down to 0 then the game should stop and it should print "You lose."
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
        letters_not_in_word.append(guess)
        lives -= 1
        if lives == 0:
            game_over = True
            print("Game over, no more lives left.")

    print("current guess: " + "".join(word))
    #print(f"correct guesses: {correct_letters}")
    print(f"incorrect letters: {letters_not_in_word}")

    if "_" not in word:
        game_over = True
        print("You guessed the word! The word is: " + "".join(word))
        
# TODO-3: - print the ASCII art from 'stages'
#  that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])