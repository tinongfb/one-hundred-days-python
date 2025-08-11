import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
letter_count = len(chosen_word)
print(f"chosen word '{chosen_word}' has {letter_count} letters")


# TODO-1: Create a "placeholder" with the same number of blanks as the chosen_word
game_over = False
letters_not_in_word = []
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()
    placeholder = "_" * letter_count
    #print(placeholder)

# TODO-2: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.
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

    print("current guess: " + "".join(word))
    #print(f"correct guesses: {correct_letters}")
    print(f"incorrect letters: {letters_not_in_word}")

    if "_" not in word:
        game_over = True
        print("You guessed the word! The word is: " + "".join(word))