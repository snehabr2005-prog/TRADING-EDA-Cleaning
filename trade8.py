# trade8.py - Missing values and crossed book
import pandas as pd
df = pd.read_csv('trades_orderbook_STUDENT_dirty.csv')
df['price'] = pd.to_numeric(df['price'].astype(str).str.replace(r'[\$,]','', regex=True), errors='coerce')
df = df.sort_values('timestamp')
df[['price','quantity']] = df[['price','quantity']].ffill().bfill()
df['side'] = df['side'].ffill().bfill()
df.loc[df['bid_price_1'] >= df['ask_price_1'], 'ask_price_1'] = df['bid_price_1'] + 0.1
print("Fixed")
