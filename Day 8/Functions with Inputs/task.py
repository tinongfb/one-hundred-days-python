#create the function
def greet(name, location):
    print(f"Hello {name}")
    #print(f"How do you do, {name}?")
    print(f"bla bla bla bla bla {location}")
    #print(f"Bye, {name}")

###  call the function (run the function)
#name = input("What is your name? ")
greet(name="Jack", location="boat")



### this is another exercise ###
# import random
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# list_alphabet = list(alphabet)
# random_letter = random.choice(list_alphabet)
# list_alphabet.remove(random_letter)
# print(list_alphabet)
# random.shuffle(list_alphabet)
# #print(list_alphabet)
#
# correct_guess = False
# guesses = []
# while correct_guess == False:
#     letter_guess = input("Guess the random letter: ")
#     if letter_guess == random_letter:
#         correct_guess = True
#         print(f"Correct! The random letter removed is {random_letter}")
#         print(list_alphabet)
#     else:
#         print("Wrong guess.")
#         guesses.append(letter_guess)
#         print(guesses)