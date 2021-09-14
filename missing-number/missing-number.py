class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expSum = len(nums)*(len(nums)+1)/2
        actualSum = sum(nums)
        return int(expSum - actualSum)
        