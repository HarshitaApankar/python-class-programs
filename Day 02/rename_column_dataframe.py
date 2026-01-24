#to rename a column of dataframe

import pandas as pd
df=pd.DataFrame({'A':[1,2,3],'B':[4,5,6]})
print("Original Data Frame:")
print(df)

df=df.rename(columns={'A':'ab'})
print("Modified Data Frame:")
print(df)
