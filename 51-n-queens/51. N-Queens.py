class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range(n)]
        row = 0 
        cols = set()
        diag = set()
        antiDiag = set()
        ans = []

        def backTrack(row, cols, diag, antiDiag, board):
            if row == n:
                curr = ["".join(r) for r in board]
                ans.append(curr)
                return

            for i in range(n):
                if i in cols or (row - i) in diag or (row + i) in antiDiag:
                    continue
                    
                cols.add(i)
                diag.add(row - i)
                antiDiag.add(row + i)

                board[row][i] = "Q"
                backTrack(row + 1, cols, diag, antiDiag, board)

                board[row][i] = "."
                cols.remove(i)
                diag.remove(row - i)
                antiDiag.remove(row + i)

        backTrack(0, cols, diag, antiDiag, board)
        return ans

                    

        