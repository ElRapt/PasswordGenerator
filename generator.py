import random
import tkinter as tk
import tkinter.messagebox as msgbox

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
uppercaseAlphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lowercaseAlphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
specialCharacters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|', '\\', ':', ';', '"', '\'', '<', '>', ',', '.', '?', '/']
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
    choice = [numbers, uppercaseAlphabet, lowercaseAlphabet, specialCharacters]  # Réinitialisation de la liste choice
    
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
    desired_complexity = complexities.index(complexity_var.get()) + 1
    
    password, complexity = generatePassword(length, has_numbers, has_uppercase, has_lowercase, has_special_characters, desired_complexity)
    
    password_output_label.config(text="Password : " + password)
    complexity_output_label.config(text="Complexity : " + complexities[complexity - 1])

def copy_to_clipboard():
    password = password_output_label.cget("text")[12:] 
    window.clipboard_clear()  
    window.clipboard_append(password)  
    msgbox.showinfo("Copied !", "Password was copied to clipboard.")


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

complexity_label = tk.Label(window, text="Desired complexity")
complexity_label.pack()

complexity_var = tk.StringVar()
complexity_dropdown = tk.OptionMenu(window, complexity_var, *complexities)
complexity_dropdown.pack()

generate_password_button = tk.Button(window, text="Generate password", command=generate_password_button_click)
generate_password_button.pack()

password_output_label = tk.Label(window, text="")
password_output_label.pack()

complexity_output_label = tk.Label(window, text="")
complexity_output_label.pack()

copy_button = tk.Button(window, text="Copy to clipboard", command=copy_to_clipboard)
copy_button.pack()
copy_button.pack_forget() 


window.mainloop()
