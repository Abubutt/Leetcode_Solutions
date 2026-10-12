class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        left = right = 1

        for right in range(len(nums)):
            if nums[right] == nums[left - 1]:
                continue
            
            nums[left], nums[right] = nums[right], nums[left]
            left+=1

        return left