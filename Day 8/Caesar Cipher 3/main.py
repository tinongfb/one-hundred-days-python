# TODO-1: Import and print the logo from art.py when the program starts.
from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-2: What happens if the user enters a number/symbol/space?

def caesar():
    direction = input("Type '1' to encrypt, type '2' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift_amount = int(input("Type the shift number:\n"))
    if direction == '1':
        encrypted_list = []
        letter_index = 0
        for letter in text:
            if letter in alphabet:
                letter_index = alphabet.index(letter) + shift_amount
                wrapped_index = letter_index % len(alphabet)
                encrypted_list.append(alphabet[wrapped_index])
            elif " " in text:
                encrypted_list.append(" ")
            elif not letter.isalpha():
                encrypted_list.append(letter)
        encrypted_text = ''.join(encrypted_list)
        print(f"The encrypted text is: {encrypted_text}")
    elif direction == '2':
        decrypted_list = []
        letter_index = 0
        for letter in text:
            if letter in alphabet:
                letter_index = alphabet.index(letter) - shift_amount
                wrapped_index = letter_index % len(alphabet)
                decrypted_list.append(alphabet[wrapped_index])
            elif " " in text:
                decrypted_list.append(" ")
        decrypted_text = ''.join(decrypted_list)
        print(f"The decrypted text is: {decrypted_text}")
    else:
        pass

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

# TODO-3: Can you figure out a way to restart the cipher program?
def ask_repeat():
    caesar()
    play_again = input("Do you want to en/decrypt again? Type 'y' for yes, type 'n' to no:\n").lower()
    if play_again == 'n':
        #should_continue = False
        print("Thank you for using the service!")
        return False
    elif play_again=='y':
        return True
    else:
        print("Invalid, please try again.")
        return True
should_cont = True
while should_cont:
    should_cont = ask_repeat()

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
#
# caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)



