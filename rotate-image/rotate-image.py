class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
#         l, r= 0, len(matrix) -1
        
#         while l<r:
#             for i in range(r-l):
#                 top, bottom = l, r
                
#                 # save the topLeft
#                 topLeft = matrix[top][l+i]
                
#                 # move bottom left into top left
#                 matrix[top][l+i] = matrix[bottom - i][l]
                
#                 # move bottom right into bottom left
#                 matrix[bottom-i][l] = matrix[bottom][r-i]
                
#                 # move top right into bottom right
#                 matrix[bottom][r - i] = matrix[top+i][r]
                
#                 # move top left into top right
#                 matrix[top + i][r] = topLeft
                
#             r-=1
#             l+=1

        n = len(matrix)
        # change row to column
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
        # reverse rows
        for i in range(n):
            l, r = 0, n-1
            while l < r:
                matrix[i][l], matrix[i][r] = matrix[i][r], matrix[i][l]
                l += 1
                r -= 1