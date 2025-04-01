import random
import string

size = int(input("Enter your password Length: "))

def generate_password (size):

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for i in range (size):
        password = password + random.choice(characters)
    return password

result = generate_password(size)

print("Your password is: ", result)
