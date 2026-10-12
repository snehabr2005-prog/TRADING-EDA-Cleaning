# trade11.py - Visualizations
import pandas as pd, matplotlib.pyplot as plt
df = pd.read_csv('trades_orderbook_clean.csv')
plt.plot(pd.to_datetime(df['timestamp_parsed']), df['price'])
plt.title('Price over time'); plt.savefig('price_trend.png')
plt.figure()
df['side'].value_counts().plot(kind='bar')
plt.title('Buy vs Sell'); plt.savefig('buy_sell.png')
print("Plots saved")
