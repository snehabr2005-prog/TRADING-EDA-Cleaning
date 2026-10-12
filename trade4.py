# trade4.py - Clean text columns
import pandas as pd
df = pd.read_csv('trades_orderbook_STUDENT_dirty.csv')
df['price'] = df['price'].astype(str).str.replace(r'[\$,]', '', regex=True)
df['price'] = pd.to_numeric(df['price'], errors='coerce')
df['side'] = df['side'].str.lower().str.strip()
df['symbol'] = df['symbol'].str.upper().str.replace(r'[-/]', '', regex=True)
print("Cleaned")
