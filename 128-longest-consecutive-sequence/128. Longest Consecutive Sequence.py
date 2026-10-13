class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numsSet = set(nums)
        maxCt = 0

        for num in numsSet:
            if num + 1 not in numsSet:
                curr = 1
                while num - 1 in numsSet:
                    curr += 1
                    num -= 1

                maxCt = max(maxCt, curr)

        return maxCt
        