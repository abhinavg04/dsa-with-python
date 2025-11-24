def stock_buysell(arr):
    bestBuy = float('inf')
    profit = 0
    for price in arr:
        if bestBuy > price:
            bestBuy = price
        else:
            profit = max(profit, price - bestBuy)    
            bestBuy = min(bestBuy, price)
    return profit
arr = [7,1,5,3,6,4]
print(stock_buysell(arr))