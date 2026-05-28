class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        currSum = 0
        totalSum = 0
        
        for i in range(len(nums)):
            currSum += nums[i] * i
            totalSum += nums[i]

        maxSum = currSum

        for i in range(len(nums) - 1, -1, -1):
            currSum = currSum - (nums[i] * (len(nums) - 1)) + (totalSum - nums[i])
            maxSum = max(maxSum, currSum)
        
        return maxSum
        # 25 - 18 + (15 - 6) = 7 + 9 = 16