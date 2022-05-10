class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = 0
        end = 1
        maxProfit = 0
        size = len(prices)
        
        while end < size:
            if prices[start] > prices[end]:
                start = end
            else:
                curr = prices[end] - prices[start]
                maxProfit = max(maxProfit, curr)
            end += 1
        return maxProfit