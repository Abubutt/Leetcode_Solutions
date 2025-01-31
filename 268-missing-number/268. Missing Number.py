class Solution:
    def missingNumber(self, nums: List[int]) -> int:    
#         numsSet = set(nums)
        
#         for i in range(0, len(nums) + 1):
#             if i not in numsSet:
#                 return i
        
        size = len(nums)
        
        requiredSum = (size * (size + 1)) // 2
        currentSum = sum(nums)
        
        return requiredSum - currentSum
