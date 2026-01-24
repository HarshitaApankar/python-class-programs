#create a dataframe dictionary that stores mobile name list and price list 

import pandas as pd

data={'mobilename':['oppo','vivo','realme','redme','samsung'],
      'price':[56000,46000,89000,45000,34000,]}

df=pd.DataFrame(data)
print(df)
