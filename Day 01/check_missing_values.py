#checking for missing values using isnull() and notnull()

import pandas as pd
import numpy as np

dict={'first score':[100,90,np.nan,95],
      'second score':[30,45,56,np.nan],
      'third score':[np.nan,40,80,98]}

df=pd.DataFrame(dict)
print(df.isnull())

print(df.notnull())
