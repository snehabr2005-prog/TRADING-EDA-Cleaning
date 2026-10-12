# trade9.py - Feature Engineering
import pandas as pd
df = pd.read_csv('trades_orderbook_clean.csv')
df['spread'] = df['ask_price_1'] - df['bid_price_1']
df['mid_price'] = (df['ask_price_1'] + df['bid_price_1'])/2
df['order_imbalance'] = (df['bid_qty_1'] - df['ask_qty_1'])/(df['bid_qty_1'] + df['ask_qty_1'])
print(df[['spread','mid_price','order_imbalance']].head())
