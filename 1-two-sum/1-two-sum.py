class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # time 0(n^2) space 0(n)
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if (nums[i] + nums[j]) == target:
        #             return [i,j]
        
        # time 0(n) space 0(n)
        num_dict = {}
        for i in range(len(nums)):
            if (target-nums[i]) in num_dict:
                return [i,num_dict[target - nums[i]]]
            else:
                num_dict[nums[i]] = i