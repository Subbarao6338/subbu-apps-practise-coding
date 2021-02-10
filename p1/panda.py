import pandas as pd

pwd = pd.read_csv('H:\.NECS\SUBBU\ACCOUNTS\Google Passwords.csv', index_col=0)
print(pwd)
pwd.to_html('pwd.html')
