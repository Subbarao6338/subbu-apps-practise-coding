import pandas as pd
import numpy as np
df=pd.DataFrame(np.random.rand(10,4))
d=pd.date_range('20200701',periods=10)
s=pd.Series([1,2,3,np.nan,5,6,np.nan,8,9,10],index=d).shift(3)
print(df)
print(df.mean())
print(df.mean(1))
print(s)