import copy

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(text):
    duplicate = copy.deepcopy(alphabet)
    global shift
    shift = shift % len(alphabet)
    duplicate = duplicate[-shift:] + duplicate[:-shift] # using slicing to get rotate right by shift

    my_dict = {}

    for i in range(len(alphabet)):
        my_dict[alphabet[i]] = duplicate[i] 

    encrypted = ""
    for letter in text:
        encrypted += my_dict[letter]
    
    print(encrypted)
    return encrypted


def decrypt(encrypted):
    duplicate = copy.deepcopy(alphabet)
    global shift
    shift = shift % len(alphabet)
    duplicate = duplicate[-shift:] + duplicate[:-shift] # using slicing to get rotate right by shift

    my_dict = {}
    for i in range(len(alphabet)):
        my_dict[duplicate[i]] = alphabet[i] 

    decrypted = ""
    for letter in encrypted:
        decrypted += my_dict[letter]
    
    print(decrypted)
    return decrypted


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

if direction == 'encode':
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    encrypt(text)

elif direction == 'decode':
    text = input("Type encrypted message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    decrypt(text)

