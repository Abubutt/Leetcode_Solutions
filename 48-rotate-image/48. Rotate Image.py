class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])

        currCol = 0

        for row in range(rows):
            for col in range(currCol, cols):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
            currCol += 1

        print(matrix)
        for row in range(rows):
            matrix[row].reverse()

        [
            [1,2,3],
            [4,5,6],
            [7,8,9]]