import random

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
uppercaseAlphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lowercaseAlphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
specialCharacters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|', '\\', ':', ';', '"', '\'', '<', '>', ',', '.', '?', '/']
choice = [numbers, uppercaseAlphabet, lowercaseAlphabet, specialCharacters]
def generatePassword(length, hasNumbers, hasUppercase, hasLowercase, hasSpecialCharacters):
    if not hasNumbers:
        choice.remove(numbers)
    if not hasUppercase:
        choice.remove(uppercaseAlphabet)
    if not hasLowercase:
        choice.remove(lowercaseAlphabet)
    if not hasSpecialCharacters:
        choice.remove(specialCharacters)
    if not choice:  
        return "Can't generate a password with no characters."
    password = []
    for i in range(length):
        arr = random.choice(choice)
        password.append(random.choice(arr))
    random.shuffle(password)
    return ''.join(password)

print(generatePassword(12, True, False, True, False))
