#10 marks question
import random

radius=random.randint(1,10)

circumference=2*3.14*radius

print("Radius:",radius)
print("Circumference:",circumference)

#20 marks question
import re
password=input("Enter password:")

if len(password)<6 or len(password)>12:
    print("Invalid length of paasword ,it should be between 6 to 12 digits!")

elif(re.search("[a-z]",password)or
     re.search("[0-9]",password)or
     re.search("[$#@]",password)):
    
    print("Valid password")
else:
    print("Invalid password")
