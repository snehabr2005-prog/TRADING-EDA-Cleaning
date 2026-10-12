# trade1.py - Load and Inspect
import pandas as pd
df = pd.read_csv('trades_orderbook_STUDENT_dirty.csv')
print(f"Shape: {df.shape}")
print(df.head())
print(df.info())
