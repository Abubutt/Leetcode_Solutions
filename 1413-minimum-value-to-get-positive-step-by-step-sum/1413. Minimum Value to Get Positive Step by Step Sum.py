class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        minSum = currSum = nums[0]
        
        for i in range(1, len(nums)):
            currSum += nums[i]
            minSum = min(minSum, currSum)
            
        if minSum < 0:
            return abs(minSum) + 1
        
        return 1