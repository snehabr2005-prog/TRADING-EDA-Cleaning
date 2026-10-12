# trade5.py - Fix timestamps 3 formats
import pandas as pd
def parse_ts(x):
    x=str(x).strip()
    if x.isdigit(): return pd.to_datetime(int(x), unit='s')
    if '/' in x: return pd.to_datetime(x, format='%d/%m/%Y %H:%M:%S')
    return pd.to_datetime(x)
df = pd.read_csv('trades_orderbook_STUDENT_dirty.csv')
df['timestamp_parsed'] = df['timestamp'].apply(parse_ts)
print(df['timestamp_parsed'].head())
