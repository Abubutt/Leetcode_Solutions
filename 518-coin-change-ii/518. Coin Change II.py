class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def dp(i, amount):
            if (i, amount) in memo:
                return memo[(i, amount)]

            if i == -1:
                return amount == 0

            if amount == 0:
                return 1

            if amount < 0:
                return 0

            pick = dp(i, amount-coins[i])
            notPick = dp(i-1, amount)

            memo[(i, amount)] = pick + notPick
            return memo[i, amount]

        return dp(len(coins) - 1, amount)
        