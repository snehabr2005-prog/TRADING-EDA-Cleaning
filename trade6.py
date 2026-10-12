# trade6.py - Sort and remove duplicates 2035->2000
import pandas as pd
def parse_ts(x):
    x=str(x).strip()
    if x.isdigit(): return pd.to_datetime(int(x), unit='s')
    if '/' in x: return pd.to_datetime(x, format='%d/%m/%Y %H:%M:%S')
    return pd.to_datetime(x)
df = pd.read_csv('trades_orderbook_STUDENT_dirty.csv')
df['timestamp_parsed'] = df['timestamp'].apply(parse_ts)
df = df.sort_values('timestamp_parsed')
df = df.drop_duplicates(subset=['trade_id'], keep='first')
print(f"After dedup: {len(df)} rows")
