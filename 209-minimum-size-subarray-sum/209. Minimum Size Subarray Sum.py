class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float('inf')
        currSum = left = 0

        for right in range(len(nums)):
            currSum += nums[right]

            while currSum >= target:
                ans = min(ans, right - left + 1)
                currSum -= nums[left]
                left += 1

        return 0 if ans == float('inf') else ans
