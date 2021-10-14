class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            s = 0
            for j in range(0,i+1):
                s+=nums[j]
            ans.append(s)
        return ans
        
                