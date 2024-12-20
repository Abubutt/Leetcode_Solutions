class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixSum = [nums[0]]
        pivotIndex = -1
        size = len(nums)
        totalSum = nums[0]

        for i in range(1, size):
            totalSum += nums[i]
            prefixSum.append(nums[i] + prefixSum[-1])
        
        for i in range(size):
            leftSum = 0
            rightSum = 0

            if i > 0:
                leftSum = prefixSum[i-1]
            
            if i < size:
                rightSum = totalSum - prefixSum[i]

            if leftSum == rightSum:
                pivotIndex = i
                break

        return pivotIndex



        
        