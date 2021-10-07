class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1
        size = len(nums)
        while j<len(nums):
            if nums[i] == nums[j]:
                nums.remove(nums[i])
                size-=1
            else:
                i+=1
                j+=1
        return size
            