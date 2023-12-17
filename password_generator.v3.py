import random
import string

def generate_password(length, uppercase=True, numbers=True, special_characters=True):    
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation
    pwd = ""
    req = 0

    characters = lower
    if uppercase:
        characters += upper
        pwd += random.choice(upper)
        req += 1
    if numbers:
        characters += digits
        pwd += random.choice(digits)
        req += 1
    if special_characters:
        characters += special
        pwd += random.choice(special)
        req += 1

    for i in range(length-req):
        new_char = random.choice(characters)
        pwd += new_char

    pwd = list(pwd)
    random.shuffle(pwd)
    return pwd

length = int(input("Password Length: "))
has_uppercase = input("Do you want to have uppercase (y/n)? ").lower() == "y"
has_number = input("Do you want to have numbers (y/n)? ").lower() == "y"                    # if input = y/Y, y == "y" return True
has_special = input("Do you want to have special characters (y/n)? ").lower() == "y"
pwd = generate_password(length, has_uppercase, has_number, has_special)
print("The generated password is: ", end="")
for password in pwd:
    print (password, end="")




