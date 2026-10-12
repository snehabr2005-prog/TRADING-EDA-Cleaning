# trade3.py - Find 10 Issues
import pandas as pd
df = pd.read_csv('trades_orderbook_STUDENT_dirty.csv')
print("Duplicates:", df.duplicated(subset=['trade_id']).sum())
print("Missing:\n", df.isna().sum())
print("Price with $:", df['price'].astype(str).str.contains(r'\$').sum())
