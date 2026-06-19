#Import Modules
#random helps us pick random characters.
#tring contains ready-made collections of letters and digits.

import random
import string

length = int(input("Password length: "))


#string.ascii_letters contains: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
#string.digits contains:0123456789

characters = string.ascii_letters + string.digits + "!@#$%^&*"

#''.join(...):Combines all characters into one string:
password = ''.join(random.choice(characters) for _ in range(length))

print("Generated Password:")
print(password)
