class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        curr = 0
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif nums[i] < target:
                curr = i+1
            elif target > nums[i]:
                curr = i
        return curr