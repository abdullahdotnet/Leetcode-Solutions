# timelimit exceeded
# def maxProfit(prices):
#     max = 0
#     for i in range(len(prices)):
#         for j in range(i,len(prices)):
#             if prices[j]-prices[i] > max:
#                 max = prices[j]-prices[i]
#     return max

def maxProfit(prices):
    bp = prices[0]
    profit = 0

    for i in range(1,len(prices)):
        if prices[i] < bp:
            bp = prices[i]
        profit = max(profit,prices[i]-bp)
    return profit

print(maxProfit([7,6,4,3,1]))