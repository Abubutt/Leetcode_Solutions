class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        memo = {}
        def dp(dice, amount):
            if (dice, amount) in memo:
                return memo[(dice, amount)]
                
            if dice == 0:
                return amount == 0

            ans = 0
            for i in range(1, k+1):
                if i <= amount:
                    ans += dp(dice-1, amount - i)

            memo[(dice, amount)] = ans
            return memo[(dice, amount)]

        return dp(n, target) % (10**9 + 7)
        
        # dp(2, 7)

        # dp(1, 6)  dp()

        # dp(0)