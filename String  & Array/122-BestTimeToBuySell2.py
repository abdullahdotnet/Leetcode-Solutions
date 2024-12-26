def maxProfit(prices):
    bp = prices[0]
    profit = 0
    for i in range(len(prices)):
        
        if prices[i] < bp:
            bp = prices[i]
        else:
            profit += prices[i]-bp
            bp = prices[i]
        
    return profit
print(maxProfit([7,1,5,3,6,4]))
