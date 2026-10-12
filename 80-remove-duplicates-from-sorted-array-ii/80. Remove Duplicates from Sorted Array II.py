class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        ct = 1
        left = right = 1

        while right < len(nums):
            if nums[right] == nums[right - 1]:
                ct += 1
            else:
                ct = 1

            if ct > 2:
                while right < len(nums) and nums[right] == nums[right - 1]:
                    right += 1
                ct = 1

            if right < len(nums):
                nums[left] = nums[right]
                left += 1
                right += 1

        return left

        # [1,1,1]
        #    l
        #    r
        #    2

        
        #  [0,0,1,1,2,3,3,3,3]
        #               l
        #                   r
        #           1