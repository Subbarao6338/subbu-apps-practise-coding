import pandas as pd
import numpy as np
df=pd.DataFrame({'A':['a','b','c','d']*3,
                 'B':['A','B','C']*4,
                 'C':['p','p','p','q','q','q']*2,
                 'D':np.random.randn(12),
                 'E':np.random.randn(12)})
p=pd.pivot(df,values='D',index=['A'],columns=['B'])
p1=pd.pivot_table(df,values=['D','E'],index=['A'],columns=['B'])
print(p)
print(p1)