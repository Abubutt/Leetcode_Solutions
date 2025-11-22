class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        memo = {}
        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if i == len(nums1) or j == len(nums2):
                return 0

            ans = 0
            if nums1[i] == nums2[j]:
                ans = 1 + dp(i+1, j+1)

            ans = max(ans, dp(i+1, j), dp(i, j+1))
            memo[(i, j)] = ans
            return memo[(i, j)]

        return dp(0, 0)
        