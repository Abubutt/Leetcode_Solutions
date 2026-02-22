class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currSum = 0
        sums = {0:1}
        ans = 0

        for right in range(len(nums)):
            currSum += nums[right]
            if currSum - k in sums:
                ans += sums[currSum - k]
            
            sums[currSum] = 1 + sums.get(currSum, 0)


        return ans
        