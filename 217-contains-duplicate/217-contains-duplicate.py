class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # time 0(n) space 0(n)
#         num_dict = {}
        
#         for num in nums:
#             if num in num_dict:
#                 return True
#             else:
#                 num_dict[num] = 1
                
#         return False

        # time 0(nlogn) space 0(1)
    
        nums = sorted(nums)
        
        for i in range(0, len(nums) - 1):
            if nums[i] == nums[i+1]:
                return True
        return False
                