class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        ans = 0
        left = 0

        for right in range(1, len(prices)):
            if prices[right] >= prices[left]:
                ans = max(ans, prices[right] - prices[left])
            else:
                left = right

        return ans

        # [7,1,5,3,6,4]
        #    l
        #            r

        # [7,6,4,3,1]
        #        l
        #          r

        # [2,1,2,1,0,1,2]
        #    l
        #        r