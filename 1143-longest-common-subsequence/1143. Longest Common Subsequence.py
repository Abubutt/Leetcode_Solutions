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

        # return dpMemo(n-1, m-1)

        def dpTab():
            dp = [[0] * m for _ in range(n)]

            for i in range(n):
                for j in range(m):
                    res = 0

                    if text1[i] == text2[j]:
                        res = 1
                        res += dp[i-1][j-1] if i > 0 and j > 0 else 0
                    
                    if i > 0:
                        res = max(res, dp[i-1][j])

                    if j > 0:
                        res = max(res, dp[i][j-1])

                    dp[i][j] = res

            return dp[n-1][m-1]

        return dpTab()

        [0, 0, 0], 
        [0, 0, 0], 
        [0, 1, 0], 
        [0, 1, 0], 
        [0, 1, 2]

        