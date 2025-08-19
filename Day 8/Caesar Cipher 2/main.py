alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type '1' to encrypt, type '2' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift_amount = int(input("Type the shift number:\n"))

# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.

def caesar():
    if direction == '1':
        encrypted_text = ""
        for letter in text:
            if letter in alphabet:
                letter_index = alphabet.index(letter) + shift_amount
                wrapped_index = letter_index % len(alphabet)
                encrypted_text += alphabet[wrapped_index]
        print(f"The encrypted text is: {encrypted_text}")
    elif direction == '2':
        decrypted_text = ""
        for letter in text:
            if letter in alphabet:
                letter_index = alphabet.index(letter) - shift_amount
                wrapped_index = letter_index % len(alphabet)
                decrypted_text += (alphabet[wrapped_index])
        print(f"The decrypted text is: {decrypted_text}")
    else:
        pass

caesar()

# def encrypt(original_text, shift_amount):
#     cipher_text = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) + shift_amount
#         shifted_position %= len(alphabet)
#         cipher_text += alphabet[shifted_position]
#     print(f"Here is the encoded result: {cipher_text}")
#
#
# encrypt(original_text=text, shift_amount=shift)



