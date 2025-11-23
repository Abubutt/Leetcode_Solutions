class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = {}

        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[(i, diff)] = dp.get((j, diff), 1) + 1
                
        return max(dp.values())

        memo = {}
        def dp(i, diff):
            if (i, diff) in memo:
                return memo[(i, diff)]

            if i == len(nums):
                return 0

            ans = 1

            for j in range(i+1, len(nums)):
                if nums[j] - nums[i] == diff:
                    ans = max(ans, 1+dp(j, diff))

            memo[(i, diff)] = ans
            return memo[(i, diff)]

        maxLen = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                diff = nums[j] - nums[i]
                maxLen = max(maxLen, 1 + dp(j, diff))

        return maxLen
        