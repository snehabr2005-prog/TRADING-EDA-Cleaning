# trade7.py - Fix outliers
import pandas as pd
df = pd.read_csv('trades_orderbook_STUDENT_dirty.csv')
df['price'] = pd.to_numeric(df['price'].astype(str).str.replace(r'[\$,]','', regex=True), errors='coerce')
df.loc[df['price']>500000, 'price'] /= 100
df.loc[df['price']<0, 'price'] = df['price'].abs()
print("Outliers fixed")
