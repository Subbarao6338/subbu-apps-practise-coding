import pandas as pd
import numpy as np
df=pd.DataFrame({'id':[1,2,3,4,5,6],'grade':['a','b','c','b','e','a'],'Grade':pd.Categorical(['very bad','bad','ok','good','very good','excellent'])})
#df['Grade']=df['grade'].astype('category')
df['G']=pd.CategoricalIndex(['O','A','B','C','D','E'])
print(df)
print(df['G'])