#10 marks question

import re

s=input("Enter string:")
numbers=re.findall(r'\d+',s)
print("Extracted numbers:",numbers)

#20 marks question

def check_pass_fail(marks):
    if marks>=40:
     return "Pass"
    else:
       return"Fail"
    
pass_count=0
fail_count=0

n=int(input("Enter number of students:"))

for i in range(n):
   marks=int(input("Enter marks:"))
   result=check_pass_fail(marks)
   print("Result is:",result)

   if result=="Pass":
      pass_count+=1
else:
   fail_count+=1

print(" Total count of students who passed :",pass_count)
print(" Total count of students who failed :",fail_count)

#10 marks question
s=input("Enter String:")
modified=s.replace(" ","")
print("Modified string:",modified)

#20 marks question
import pandas as pd

data={'Company':['Apsara','Natraj','Cello','Parkar','Apsara'],
      'Count':[15,20,25,35,20],
      'Price':[250,200,600,900,300]}

df=pd.DataFrame(data,index=['Pencil','Pencil','Pen','Pen','Eraser'])
print(df)

print(df.loc["Pencil"])
df.loc['Eraser','Count']=25
print(df[['Company','Price']])
print(df.loc[['Pencil','Pen']])

df["Colour"]=["Red","Blue","Black","Yellow","Pink"]
print(df)     
