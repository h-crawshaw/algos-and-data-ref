prices = [2, 1, 4, 6, 7, 2, 8, 6, 7]

def mostProfit(prices):
  l, r = 0, 1
  max_profit = 0

  while r < len(prices):
    if prices[r] > prices[l]:
      current_profit = prices[r] - prices[l]
      max_profit = max(max_profit, current_profit)
    else:
      l = r
    r += 1

  return max_profit