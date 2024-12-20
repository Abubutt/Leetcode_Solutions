class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxOnes = 0
        curr = 0
        left = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                curr += 1
                
            while curr > k:
                if nums[left] == 0:
                    curr -= 1
                left += 1
            
            maxOnes = max(maxOnes, right - left + 1)
            
        return maxOnes
            
        