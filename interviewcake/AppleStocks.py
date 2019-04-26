def get_max_profit(stock_prices):
    assert stock_prices
    assert(len(stock_prices) > 1)

    profit = stock_prices[1] - stock_prices[0]

    for i in range(2, len(stock_prices)):
        diff = stock_prices[i] - stock_prices[i-1]
        if diff > 0:
            profit = max(profit+diff, diff)
        else:
            profit = max(profit, diff)
    return profit


out = get_max_profit([9, 7, 4, 1])
print(out)
out = get_max_profit([10, 7, 5, 8, 11, 9])
print(out)
