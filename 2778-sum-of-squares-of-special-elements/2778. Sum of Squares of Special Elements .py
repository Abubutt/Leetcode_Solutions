class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for idx, num in enumerate(nums):
            if n % (idx + 1) == 0:
                ans += (num ** 2)

        return ans
        