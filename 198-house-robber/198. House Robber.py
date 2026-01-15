class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dp(currSum, idx, picked):
            if (currSum, idx, picked) in memo:
                return memo[(currSum, idx, picked)]

            if idx == len(nums):
                return currSum

            pick = 0
            if not picked:
                pick = dp(currSum + nums[idx], idx + 1, True)
            notPick = dp(currSum, idx + 1, False)

            memo[(currSum, idx, picked)] = max(pick, notPick)
            return memo[(currSum, idx, picked)]

        return dp(0, 0, False)
        