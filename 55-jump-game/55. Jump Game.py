class Solution:
    def canJump(self, nums: list[int]) -> bool:
        edge = 0

        for i in range(len(nums)):
            if edge >= len(nums) - 1:
                return True

            if i > edge:
                break

            edge = max(edge, nums[i] + i)

        return False