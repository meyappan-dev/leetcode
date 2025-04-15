# Last updated: 4/15/2025, 4:14:00 PM
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])

        for i in range(row):
            if target <= matrix[i][col-1]:
                for j in range(col):
                    if target == matrix[i][j]:
                        return True
        return False