class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        total = currSum = 0
        count = defaultdict(int)
        count[0] = 1

        for num in nums:
            currSum += num
            if currSum-goal in count:
                total += count[currSum-goal]
            count[currSum] += 1

        return total


        