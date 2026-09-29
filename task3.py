import numpy as np

prices = np.array([299, 499, 799, 0, 1599, -1, 899])

valid_prices = prices[prices > 0]
prices[prices <= 0] = np.mean(valid_prices)

quantities = np.array([2, 3, 4, 2, 1, 5, 2])

total_bill = np.multiply(prices, quantities)

print("Prices:", prices)
print("Quantities:", quantities)
print("Total Bill for Each Item:", total_bill)