class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stack = []
        ans = [0]*len(heights)

        for idx, height in enumerate(heights):
            while stack and heights[stack[-1]] <= height:
                ans[stack.pop()] += 1

            if stack:
                ans[stack[-1]] += 1

            stack.append(idx)

        return ans
        