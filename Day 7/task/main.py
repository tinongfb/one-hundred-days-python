import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
letter_count = len(chosen_word)
print(f"chosen word '{chosen_word}' has {letter_count} letters")


# TODO-1: Create a "placeholder" with the same number of blanks as the chosen_word

guess = input("Guess a letter: ").lower()
placeholder = "_" * letter_count
#print(placeholder)

# TODO-2: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.
word = []
for letter in chosen_word:
    if letter == guess:
        word.append(guess)
    else:
        word.append("_")
print("".join(word))

