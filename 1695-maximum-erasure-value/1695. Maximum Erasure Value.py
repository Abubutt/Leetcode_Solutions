class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        maxScore = currScore = left = 0
        unique = set()

        for right in range(len(nums)):
            currScore += nums[right]
            while nums[right] in unique:
                currScore -= nums[left]
                unique.remove(nums[left])
                left += 1
            
            unique.add(nums[right])
            maxScore = max(maxScore, currScore)

        return maxScore
        