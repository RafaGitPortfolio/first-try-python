# Password Generator

import random
import string

def generate_password(lenght):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for _ in range(lenght):
        password += random.choice(characters)
    return password

lenght = int(input("Enter length of password: "))
print("Generated password:", generate_password(lenght))