class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        ans = prices

        for idx, price in enumerate(prices):
            while stack and stack[-1][0] >= price:
                stackIdx = stack[-1][1]
                ans[stackIdx] = stack.pop()[0] - price
            stack.append((price, idx))

        return ans

        