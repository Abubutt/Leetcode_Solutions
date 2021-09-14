class Solution:
    def maxProfit(self, prices: List[int]) -> int:
#         buy = prices[0]
#         max_profit = 0
        
#         for i in range(1,len(prices)):
#             profit = prices[i] - buy
#             max_profit = max(max_profit, profit)
#             buy = min(buy, prices[i])
#         return max_profit

        ans = buy_date = 0 
        for day, price in enumerate(prices):
            profit = price - prices[buy_date]
            if profit < 0:
                buy_date = day
            elif profit > ans:
                ans = profit
        return ans