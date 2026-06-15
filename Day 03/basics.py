import variables

n=int(input("Enter number:"))

print("Factorial:",variables.factorial(n))
print("Power:",variables.power.get(n))
print("Vowels:",variables.vowels[1])


#10 marks question
nums=[1,2,3,4,5,6,7,8,9,10]

squares=list(map(lambda x:x*x,nums))
print("Squares:",squares)


#10 marks question
import re

s=input("Enter string:")
sub=input("Enter sub string:")

pattern="^"+sub

if(re.search(pattern,s)):
    print("Particular substring is present at the beginning of the given string")
else:
    print(" particular substring is not present at the beginning of the given string,")

#10 marks question
import re

s=input("Enter string:")

pattern=r'^[bh][iua]t$'

if re.match(pattern,s):
    print("Valid word")
else:
    print("INvalid word")




