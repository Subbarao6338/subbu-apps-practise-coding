import pandas as pd
import numpy as np
sd=pd.Series([1,2,3,4,np.nan,6,7,8,9,10])
print(sd)
d=pd.date_range('20100301',periods=10)
print(d)
df1=pd.DataFrame(np.random.randn(10,4),index=d,columns=['A','B','C','D'])
df2=pd.DataFrame({'A':[1,2,3,4],
                 'B':pd.Timestamp('20100301'),
                 'C':pd.Series(1,index=list(range(4)),dtype='float32'),
                 'D':np.array([5]*4,dtype='int32'),
                 'E':pd.Categorical(['true','false','True','False']),
                 'F':'Subbarao'})
print(df1)
print(df2)
print(df2.dtypes)
print(df1.head())
print(df1.tail())
print(df2.index)
print(df2.columns)
print(d.to_numpy())
print(df2.describe())
print(df2.sort_values(by='E'))
print(df2[['C']])
print(df2[:3])
#print(df2.loc['B'])
#print(df2.iloc[0])
#print(df2.iloc[[1,2]:])
n=df2[['B']]
print(n)

# handling missing data
df3=df1.reindex(index=d[0:4],columns=list(df2.columns)+['G'])
print(df3)
print(df3.isnull())
print(df3.isnull().count())
df4=df3.fillna(value=2)
print(df4)
print(df4.isna().count())