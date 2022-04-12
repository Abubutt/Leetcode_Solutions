class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # time 0(n^2) space 0(n)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j]) == target:
                    return [i,j]