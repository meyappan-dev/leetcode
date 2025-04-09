# Last updated: 4/8/2025, 8:54:59 PM
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        column = len(matrix[0])
        for i in range(rows):
            for j in range(i, column):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
            matrix[i].reverse()


        