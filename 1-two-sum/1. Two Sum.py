class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        pos = {}

        for idx, num in enumerate(nums):
            needed = target - num

            if needed in pos:
                return [pos[needed], idx]

            pos[num] = idx

        return []
        