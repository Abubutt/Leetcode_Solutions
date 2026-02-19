class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def dpMemo(i, j, memo={}):
            if (i, j) in memo:
                return memo[(i, j)]

            if i < 0 or j < 0:
                return 0

            res = 0

            if text1[i] == text2[j]:
                res = 1 + dpMemo(i-1, j-1)
            
            shiftI = dpMemo(i-1, j)
            shiftJ = dpMemo(i, j-1)

            res = max(res, shiftI, shiftJ)
            memo[(i, j)] = res

            return res

        n = len(text1)
        m = len(text2)

        return dpMemo(n-1, m-1)
        