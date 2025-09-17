class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        currSum = 0
        totalSum = sum(nums)

        for i in range(len(nums)):
            if currSum == totalSum - currSum - nums[i]:
                return i

            currSum += nums[i]

        return -1
