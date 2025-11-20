class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dp(i, amount):
            if (i, amount) in memo:
                return memo[(i, amount)]

            if i == 0 and amount % coins[i] == 0:
                return amount // coins[i]

            if i == 0 and amount % coins[i] > 0:
                return float('inf')

            if amount == 0:
                return 0

            pick = float('inf')
            if coins[i] <= amount:
                pick = 1 + dp(i, amount-coins[i])
            notPick = dp(i-1, amount)

            memo[(i, amount)] = min(pick, notPick)
            return memo[(i, amount)]

        ans = dp(len(coins) - 1, amount)

        if ans == float('inf'):
            return -1

        return ans

        #         11

        # 10      9     6

        # 9 8 5  
        