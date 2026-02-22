class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backTrack(idx, currPath): 
            ans.append(currPath[:])
            
            if idx == len(nums):
                return
                
            for i in range(idx, len(nums)):
                currPath.append(nums[i])
                backTrack(i+1, currPath)
                currPath.pop()

        ans = []
        backTrack(0, [])

        return ans
        