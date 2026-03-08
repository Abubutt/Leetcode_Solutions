class Solution:
    def minCost(self, n: int) -> int:
        memo = {}
        def dp(n):
            if n in memo:
                return memo[n]

            if n <= 1:
                return 0

            minVal = float('inf')

            for i in range(1, n):
                j = n - i
                minVal = min(minVal, (i * j) + dp(i) + dp(j))
                
            memo[n] = minVal
            return minVal

        return dp(n)