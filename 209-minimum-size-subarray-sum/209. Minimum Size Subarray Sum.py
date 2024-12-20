class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLength = float('inf')
        left = curr = 0

        for right in range(len(nums)):
            curr += nums[right]
            while curr >= target:
                minLength = min(minLength, right-left+1)
                curr -= nums[left]
                left += 1
        
        return minLength if minLength != float(inf) else 0
            
