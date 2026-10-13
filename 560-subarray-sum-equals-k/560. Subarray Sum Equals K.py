class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1

        currSum = 0
        ans = 0

        for num in nums:
            currSum += num
            needed = currSum - k

            ans += prefix[needed]
            prefix[currSum] += 1

        return ans
        # [1,3,6]

        
        