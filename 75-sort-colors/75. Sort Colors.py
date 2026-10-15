class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq = Counter(nums)
        pos = 0

        for num in [0, 1, 2]:
            if num in freq:
                for i in range(freq[num]):
                    nums[pos] = num
                    pos += 1
        