import pandas as pd
import numpy as np
dates=pd.date_range(3/3/2021,periods=50,freq='S')
print(dates)
ts=pd.Series(np.random.randint(0,500,len(dates)),dates)
print(ts)
print(ts.resample('5min').sum())
# utc
ts_utc=ts.tz_localize('UTC')
print(ts_utc)
# timezone conversion
ts_con=ts_utc.tz_convert('US/Eastern')
print(ts_con)
# period to timestamp
ps=ts.to_period()
print(ps)
print(ps.to_timestamp())