class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        preSums = {0: 1}
        s = 0
        res = 0
        for num in nums:
            s += num
            res += preSums.get(s - k, 0)
            preSums[s] = preSums.get(s, 0) + 1
        return res