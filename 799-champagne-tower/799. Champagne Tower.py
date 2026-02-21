class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        memo = {}
        def dp(poured, row, glass):
            if (row, glass) in memo:
                return memo[(row, glass)]

            if row == 0 and glass == 0:
                return poured

            left = right = 0
            if row > 0 and glass > 0:
                left = max(0, dp(poured, row - 1, glass - 1) - 1) / 2
            
            if row > 0:
                right = max(0, dp(poured, row - 1, glass) - 1) / 2

            memo[(row, glass)] = left + right
            return memo[(row, glass)]
        
        return min(1, dp(poured, query_row, query_glass))