class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def backTrack(curr, seen):
            if len(curr) == len(nums):
                ans.append(curr[:])
                return

            
            for i in range(len(nums)):
                if i in seen:
                    continue
                if i > 0 and nums[i-1] == nums[i] and i-1 not in seen:
                    continue
   
                curr.append(nums[i])
                seen.add(i)
                backTrack(curr, seen)
                curr.pop()
                seen.remove(i)

        ans = []
        backTrack([], set())

        return ans

        # b([], 0)

        # b([1], 1)

        # b([1,1])