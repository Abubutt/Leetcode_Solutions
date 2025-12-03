class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        def backTrack(curr, currSum, i):
            if currSum == target:
                ans.append(curr[:])
                return

            for j in range(i, len(candidates)):
                if j>i and candidates[j] == candidates[j-1]:
                    continue
                if currSum + candidates[j] <= target:
                    curr.append(candidates[j])
                    backTrack(curr, currSum + candidates[j], j+1)
                    curr.pop()

        ans = []
        backTrack([], 0, 0)

        return ans
        