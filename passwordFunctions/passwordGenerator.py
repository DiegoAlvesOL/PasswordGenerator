import random
import string

# length = int(input("Enter your password Length: "))

def generate_password (length):

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for i in range (length):
        password = password + random.choice(characters)
    return password

# result = generate_password(length)
#
# print("Your password is: ", result)
