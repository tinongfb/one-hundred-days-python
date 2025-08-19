# TODO-1: Import and print the logo from art.py when the program starts.
from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-2: What happens if the user enters a number/symbol/space?
def caesar():
    while True:  # Keep asking until valid input
        direction = input("Type '1' to encrypt, type '2' to decrypt:\n")
        if direction == '1' or direction == '2':
            break  # Exit the loop if valid
        else:
            print("Invalid input. Please enter '1' or '2'.")
    text = input("Type your message:\n").lower()
    while True:
        try:
            shift_amount = int(input("Type the shift number:\n"))
            break  # Exit loop if conversion to int works
        except ValueError:
            print("Invalid input. Please enter a number.")
    if direction == '1':
        encrypted_text = ""
        for letter in text:
            if letter in alphabet:
                letter_index = alphabet.index(letter) + shift_amount
                wrapped_index = letter_index % len(alphabet)
                encrypted_text += alphabet[wrapped_index]
            elif letter not in alphabet:
                encrypted_text += letter
        print(f"The encrypted text is: {encrypted_text}")
    elif direction == '2':
        decrypted_text = ""
        for letter in text:
            if letter in alphabet:
                letter_index = alphabet.index(letter) - shift_amount
                wrapped_index = letter_index % len(alphabet)
                decrypted_text += alphabet[wrapped_index]
            elif letter not in alphabet:
                decrypted_text += letter
        print(f"The decrypted text is: {decrypted_text}")

################### THIS IS NOT MY CODE ###################
# def caesar(original_text, shift_amount, encode_or_decode):
#     output_text = ""
#
#     for letter in original_text:
#         if encode_or_decode == "decode":
#             shift_amount *= -1
#
#         shifted_position = alphabet.index(letter) + shift_amount
#         shifted_position %= len(alphabet)
#         output_text += alphabet[shifted_position]
#     print(f"Here is the {encode_or_decode}d result: {output_text}")
################### THIS IS NOT MY CODE ###################

# TODO-3: Can you figure out a way to restart the cipher program?
def ask_repeat():
    while True:
        play_again = input("Do you want to en/decrypt again? Type 'y' for yes, type 'n' to no:\n").lower()
        if play_again == 'n':
            print("Thank you for using the service!")
            return False
        elif play_again=='y':
            return True
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

# MAIN
should_cont = True
while should_cont:
    caesar()
    should_cont = ask_repeat()


################### THIS IS NOT MY CODE ###################
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
#
# caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
################### THIS IS NOT MY CODE ###################


