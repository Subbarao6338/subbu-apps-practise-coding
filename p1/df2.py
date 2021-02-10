import pandas as pd

df1 = pd.DataFrame({'hpi': [80, 90, 70, 60],
                    'int_rate': [2, 1, 2, 3],
                    'ind_gdp': [50, 45, 45, 67]},
                   index=[2001, 2002, 2003, 2004])
df2 = pd.DataFrame({'hpi': [80, 90, 40, 50],
                    'int_rate': [2, 1, 2, 3],
                    'ind_gdp': [60, 45, 55, 67]},
                   index=[2005, 2006, 2007, 2008])
df3=pd.DataFrame({'low-tair-hpi':[50,45,67,34],
                  'unemploy':[1,3,5,7]},
                 index=[2001,2002,2004,2005])
#df1.set_index('year', inplace=True)
#df2.set_index('year', inplace=True)
# merge
m1 = pd.merge_ordered(df1, df2)
m2 = pd.merge(df1, df2)
m3=pd.merge(df1,df2,on='hpi')
print(m1)
print(m2)
print(m3)

# concat
c = pd.concat([df1, df2])
print(c)

# join
j1=df1.join(df3)
print(j1)

print(df1[0:2])
#print(df1['ind_gdp'])
#print(df1['int_rate','ind_gdp'])
print(df1[['ind_gdp']])
print(df1[['int_rate','ind_gdp']])
s=pd.Series(df3.all())
print(s)

# add column
'''for lab,row in df1.iterrows():
    df1.loc[lab,'name_length']=len(row['country'])
df1['name_length']=df1['country'].apply(len)
print(df1)'''