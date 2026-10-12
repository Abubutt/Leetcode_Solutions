class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        pos = 0
        right = len(nums) - 1

        if not nums or (pos == right and nums[pos] == val):
            return 0


        while pos <= right:
            while pos <= right and nums[right] == val:
                right -= 1

            if pos > right:
                return pos

            if nums[pos] == val:
                nums[pos], nums[right] = nums[right], nums[pos]
                right -= 1
            
            pos += 1


        return pos

        # [3,3]
        #  p
        # r

        # [2,2,3,3]
        #    p
        #    r

