import random
import tkinter as tk
from tkinter import messagebox

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
uppercaseAlphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lowercaseAlphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
specialCharacters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|', '\\', ':', ';', '"', '\'', '<', '>', ',', '.', '?', '/']
choice = [numbers, uppercaseAlphabet, lowercaseAlphabet, specialCharacters]
complexities = ["Very Weak", "Weak", "Medium", "Strong", "Very strong"]

def calculateComplexityScore(length, hasNumbers, hasUppercase, hasLowercase, hasSpecialCharacters):
    complexityScore = 0
    if length >= 8:
        complexityScore += 1
    if hasNumbers:
        complexityScore += 1
    if hasUppercase:
        complexityScore += 1
    if hasLowercase:
        complexityScore += 1
    if hasSpecialCharacters:
        complexityScore += 1
    return complexityScore

def generatePassword(length, hasNumbers, hasUppercase, hasLowercase, hasSpecialCharacters, desiredComplexity):
    if not hasNumbers:
        choice.remove(numbers)
    if not hasUppercase:
        choice.remove(uppercaseAlphabet)
    if not hasLowercase:
        choice.remove(lowercaseAlphabet)
    if not hasSpecialCharacters:
        choice.remove(specialCharacters)
    
    if not choice:
        return "Impossible de générer un mot de passe avec les critères sélectionnés."
    
    while True:
        password = []
        for i in range(length):
            arr = random.choice(choice)
            password.append(random.choice(arr))
        random.shuffle(password)
        password = ''.join(password)
        
        complexityScore = calculateComplexityScore(length, hasNumbers, hasUppercase, hasLowercase, hasSpecialCharacters)
        
        if complexityScore >= desiredComplexity:
            return password, complexityScore
def generate_password_button_click():
    length = int(length_entry.get())
    has_numbers = numbers_var.get()
    has_uppercase = uppercase_var.get()
    has_lowercase = lowercase_var.get()
    has_special_characters = special_characters_var.get()
    desired_complexity = int(desired_complexity_var.get())
    
    password, complexity = generatePassword(length, has_numbers, has_uppercase, has_lowercase, has_special_characters, desired_complexity)
    
    password_output_label.config(text="Password : " + password)
    complexity_output_label.config(text="Complexity : " + complexities[complexity - 1])

# Création de la fenêtre principale
window = tk.Tk()
window.title("Password Generator")

# Création des widgets
length_label = tk.Label(window, text="Password length")
length_label.pack()

length_entry = tk.Entry(window)
length_entry.pack()

numbers_var = tk.BooleanVar()
numbers_checkbutton = tk.Checkbutton(window, text="Numbers", variable=numbers_var)
numbers_checkbutton.pack()

uppercase_var = tk.BooleanVar()
uppercase_checkbutton = tk.Checkbutton(window, text="UppercaseLetters", variable=uppercase_var)
uppercase_checkbutton.pack()

lowercase_var = tk.BooleanVar()
lowercase_checkbutton = tk.Checkbutton(window, text="LowercaseLetters", variable=lowercase_var)
lowercase_checkbutton.pack()

special_characters_var = tk.BooleanVar()
special_characters_checkbutton = tk.Checkbutton(window, text="Special characters", variable=special_characters_var)
special_characters_checkbutton.pack()

desired_complexity_label = tk.Label(window, text="Complexité désirée (de 1 à 6) :")
desired_complexity_label.pack()

desired_complexity_var = tk.Entry(window)
desired_complexity_var.pack()

generate_password_button = tk.Button(window, text="Generate password", command=generate_password_button_click)
generate_password_button.pack()

password_output_label = tk.Label(window, text="")
password_output_label.pack()

complexity_output_label = tk.Label(window, text="")
complexity_output_label.pack()

# Lancement de la boucle principale
window.mainloop()
