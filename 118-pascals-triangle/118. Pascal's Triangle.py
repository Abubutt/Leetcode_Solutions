class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[1] * i for i in range(1, numRows + 1)]

        for row in range(1, len(dp)):
            for col in range(1, len(dp[row]) - 1):
                dp[row][col] = dp[row-1][col-1] + dp[row-1][col]

        return dp
    
  