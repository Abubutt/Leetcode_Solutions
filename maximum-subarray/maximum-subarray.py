class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Optimized approach O(n)
        curr = 0
        maxSub = nums[0]
        for i in range(len(nums)):
            if curr < 0:
                curr = 0
            curr+=nums[i]
            maxSub = max(maxSub, curr)
        return maxSub
        
        # Brute force approach O(n^2)
        # curr = 0
        # maxSub = nums[0]
        # for i in range(len(nums)):
        #     curr = 0
        #     for j in range(i, len(nums)):
        #         curr+=nums[j]
        #         maxSub = max(maxSub, curr)
        # return maxSub
        