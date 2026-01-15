#creating a dataframe using pandas

import pandas as pd

data={'name':['alka','ram','harshita'],
       'age':[20,21,22],
       'city':['nashik','pune','vapi']}

df=pd.DataFrame(data)

print(df)
