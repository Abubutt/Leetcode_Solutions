class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        memo = {}
        def dp(index, buy):
            if (index, buy) in memo:
                return memo[(index, buy)]

            if index == len(prices):
                return 0

            if buy:
                profit = max(dp(index + 1, False) - prices[index], dp(index + 1, True))
            else:
                profit = max(dp(index + 1, True) + prices[index], dp(index + 1, False))

            memo[(index, buy)] = profit
            return memo[(index, buy)]

        return dp(0, True)
        