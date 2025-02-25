import random
import string

size = int(input("Enter your password length: "))

def generate_password (size):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(0, size))
    return password

resul = generate_password(size)
print("Your passwoord is : ", resul)