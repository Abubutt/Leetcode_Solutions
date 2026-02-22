class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backTrack(seen, currPath):
            if len(currPath) == len(nums):
                path = [val for val in currPath]
                ans.append(path)
                return


            for i in range(len(nums)):
                if i not in seen:
                    seen.add(i)
                    currPath.append(nums[i])
                    backTrack(seen, currPath)

                    seen.remove(i)
                    currPath.pop()

        ans = []
        backTrack(set(), [])
        
        return ans
        