import random
import string

# length = int(input("Enter your password Length: "))

def generate_password (length, use_digits=True, use_letter=True, use_symbols=True):
    characters = ""


    if use_digits:
        characters = characters + string.digits
    if use_letter:
        characters = characters + string.ascii_letters
    if use_symbols:
        characters = characters + string.punctuation

    if not characters:
        return "⚠️Error: No character types selected."

    password = ""
    for i in range(length):
        password = password + random.choice(characters)
    return password

# result = generate_password(length)
#
# print("Your password is: ", result)
