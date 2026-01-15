# create a dataframe dictionary with index argument

import pandas as pd

data={'name':['alka','ram','seema'],
       'age':[20,21,22],
       'city':['nashik','pune','vapi']}

df=pd.DataFrame(data,index=["value1","value2","value3"])

print(df)
