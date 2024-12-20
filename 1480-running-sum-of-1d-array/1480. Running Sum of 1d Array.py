class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = [nums[0]]
        currSum = ans[-1]
        
        for i in range(1, len(nums)):
            currSum += nums[i]
            ans.append(currSum)
            
        return ans
        