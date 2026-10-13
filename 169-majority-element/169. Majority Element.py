class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        cts = Counter(nums)

        for k, ct in cts.items():
            if ct > len(nums) // 2:
                return k
        