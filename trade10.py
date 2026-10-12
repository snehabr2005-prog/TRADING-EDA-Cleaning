# trade10.py - 1-min OHLCV
import pandas as pd
df = pd.read_csv('trades_orderbook_clean.csv')
df['timestamp_parsed'] = pd.to_datetime(df['timestamp_parsed'])
ohlcv = df.set_index('timestamp_parsed').resample('1min').agg(
    open=('price','first'), high=('price','max'),
    low=('price','min'), close=('price','last'),
    volume=('quantity','sum')
).dropna()
ohlcv.to_csv('ohlcv_1min.csv')
print(ohlcv.head())
