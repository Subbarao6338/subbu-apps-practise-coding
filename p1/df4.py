import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.rand(10, 4))
d = pd.date_range('20200701', periods=10)
s = pd.Series([1, 2, 3, np.nan, 5, 6, np.nan, 8, 9, 10], index=d).shift(2)
print(df)
print(df.mean())
print(df.mean(1))
print(s)
df1 = df.sub(s, axis='index')
print(df1)
print(df.apply(np.cumsum))
print(df.apply(lambda x: x.max() - x.min()))
print(s.value_counts())
print(df.groupby(2).sum())
print(df.groupby([2,3]).sum())

s1=pd.Series(['edureka','python','jupyter',np.nan,'football','world'])
print(s1.str.upper())
df2=[df[:3],df[4:7],df[8:]]
print(pd.concat(df2))

left=pd.DataFrame({'A':[1,2],'B':[3,4]})
print(left)
right=pd.DataFrame({'C':[3,2],'D':[4,5]})
print(right)
print(left.join(right))
l1=pd.DataFrame({'A':[1,2],'B':[3,4]},index=[10,20])
l2=pd.DataFrame({'A':[5,6],'B':[7,8]},index=[10,20])
print(pd.merge_ordered(l1,l2))
print(pd.merge(l1,l2))
