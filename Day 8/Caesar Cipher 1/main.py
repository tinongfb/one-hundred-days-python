alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type '1' to encrypt, type '2' to decrypt:\n").lower()
original_text=""

# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
def encrypt():
    original_text = input("Type your message:\n").lower()
    shift_amount = int(input("Type the shift number:\n"))

# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.
    encrypted_list = []
    letter_index = 0
    for letter in original_text:
        if letter in alphabet:
            letter_index = alphabet.index(letter) + shift_amount
# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?
            wrapped_index = letter_index % len(alphabet)
            encrypted_list.append(alphabet[wrapped_index])
    encrypted_text = ''.join(encrypted_list)
    print(f"The encrypted text is: {encrypted_text}")
    #print(f"The shift index is: {letter_index}")

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.

if direction == '1':
    encrypt()
else:
    pass

