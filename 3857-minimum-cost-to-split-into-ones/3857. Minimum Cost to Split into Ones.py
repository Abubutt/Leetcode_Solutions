class Solution:
    def minCost(self, n: int) -> int:
        # memo = {}
        # def dp(n):
        #     if n in memo:
        #         return memo[n]

        #     if n <= 1:
        #         return 0

        #     minVal = float('inf')

        #     for i in range(1, n):
        #         j = n - i
        #         minVal = min(minVal, (i * j) + dp(i) + dp(j))

        #     memo[n] = minVal
        #     return minVal

        # return dp(n)

        dp = [float('inf') for _ in range(n + 1)]
        dp[0] = 0
        dp[1] = 0

        for i in range(2, n + 1):
            minVal = float('inf')

            for j in range(1, i):
                k = i - j
                minVal = min(minVal, (j * k) + dp[j] + dp[k])

            dp[i] = minVal

        return dp[n]
