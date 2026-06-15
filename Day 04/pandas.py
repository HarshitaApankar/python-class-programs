#10 marks question
import pandas as pd

data={'Subject':['Mathematics','Science','Socail Science','Hindi','English','Zoology','Java'],
      'Marks':[60,70,80,90,67,78,65]}

df=pd.DataFrame(data)
print(df)

print("First 5 rows:")
print(df.head(5))

print("First 5 rows:")
print(df.tail(5))

#20 marks question
filename=input("Enter file name:")

try:
    with open(filename,'r') as f:
        content=f.read()
        print(content)

        print("Characters:",len(content))
        print("Words:",len(content.split()))
        print("Lines:",len(content.splitlines()))

except FileNotFoundError:
#10 marks question
def productInfo(name,price=100):
    if price<100:
        print("Product name:", name)
    
productInfo("Pen",50)
productInfo("Pencil")

#20 marks question
import re

s=input("Enter String:")

words=s.split()
no_vowel_words=[]

for word in words:
    if('a' not in word.lower() and
       'e' not in word.lower() and
       'i' not in word.lower() and
       'o' not in word.lower() and
       'u' not in word.lower()):
        
        no_vowel_words.append(word)

no_vowel_words.sort()

print("Words without vowels:",no_vowel_words)
print("Number of Words without vowels:",len(no_vowel_words))
  print("File not exist")
