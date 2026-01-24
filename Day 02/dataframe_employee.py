#1.create a data.csv file containing employee name,designation,salary of an employee.display the file as dataframe.
#2.write a python program to fill (nan) in a dataframe using fillna() with mean value and detect duplicates using duplicated() method.


#create a dataframe a employee

import pandas as pd 
df=pd.read_csv('data.csv')
print(df)

#fill the nan values in dataframe using fillna() with mean values 
import pandas as pd
df=pd.read_csv('data.csv')

x=df["salary"].mean()
df.fillna({"salary":x},inplace=True)

print(df)

#return true for duplicate rows , otherwise false

print(df.duplicated())

#remove duplicates
df.drop_duplicates(inplace=True)
print(df)
