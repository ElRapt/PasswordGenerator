import random

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
uppercaseAlphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lowercaseAlphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
specialCharacters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|', '\\', ':', ';', '"', '\'', '<', '>', ',', '.', '?', '/']
choice = [numbers, uppercaseAlphabet, lowercaseAlphabet, specialCharacters]
def generatePassword(length):
    password = []
    for i in range(length):
        password.append(str(random.choice(numbers)))
        password.append(random.choice(uppercaseAlphabet))
        password.append(random.choice(lowercaseAlphabet))
        password.append(random.choice(specialCharacters))
    random.shuffle(password)
    return ''.join(password)

print(generatePassword(12))
