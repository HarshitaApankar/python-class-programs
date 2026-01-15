#fill missing values using fillna(),replace(),interpolate()

import pandas as pd
import numpy as np

data={
    'first score':[100,90,np.nan,95],
    'second score':[30,np.nan,45,56],
    'third score':[52,40,80,98],
    'fourth score':[np.nan,np.nan,np.nan,65]
}

df=pd.DataFrame(data)
print("Original dataframe:\n",df)

df_fillna=df.fillna(df.mean())
print("\nAfter fillna():\n",df_fillna)

df_replace=df.replace(np.nan,0)
print("\nAfter replace():\n",df_replace)

df_interpolate=df.interpolate()
print("\nAfter interpolate():\n",df_interpolate)
