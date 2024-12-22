class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        index = defaultdict(list)
        totalPairs = 0

        for i in range(len(nums)):
            index[nums[i]].append(i)

        for key, val in index.items():
            length = len(val)
            totalPairs += length*(length-1) // 2

        return totalPairs
        