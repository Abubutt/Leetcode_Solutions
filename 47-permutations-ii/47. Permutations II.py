class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backTrack(curr, seen):
            if len(curr) == len(nums):
                ans.add(tuple(curr[:]))
                return

            
            for i in range(len(nums)):
                if i not in seen:
                    curr.append(nums[i])
                    seen.add(i)
                    backTrack(curr, seen)
                    curr.pop()
                    seen.remove(i)

        ans = set()
        backTrack([], set())

        return list(ans)

        # b([], 0)

        # b([1], 1)

        # b([1,1])