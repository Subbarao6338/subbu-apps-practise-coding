import pandas as pd
import numpy as np
t=list(zip(*[[1,2,3,4,5,17,18,19],[11,12,13,6,7,8,9,10]]))
index=pd.MultiIndex.from_tuples(t,names=['First','Second'])
df=pd.DataFrame(np.random.randn(8,2),index=index,columns=['A','B'])
print(df)
df2=df[:4]
print(df2)
print(df2.stack())
print(df2.unstack())