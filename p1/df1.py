import pandas as pd

# convert dict to dataframe
xyz = {'day': [1, 2, 3, 4, 5, 6], 'visitors': [1000, 700, 6000, 1000, 400, 350],
       'bounce_rate': [20, 20, 23, 15, 10, 34]}
df = pd.DataFrame(xyz)
print(df)

# slicing
print(df.head(2))
print(df.tail(2))

xyz = df.rename(columns={"visitors": "users"})
xyz.set_index('day', inplace=True)
print(xyz)
