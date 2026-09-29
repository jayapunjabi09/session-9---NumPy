import numpy as np

prices = np.array([299, 499, 799, 0, 1599, -1, 899])

valid_prices = prices[prices > 0]
prices[prices <= 0] = np.mean(valid_prices)

unique_prices = np.unique(prices)

print("Cleaned Prices:", prices)
print("Unique Prices:", unique_prices)
print("Number of Unique Prices:", len(unique_prices))