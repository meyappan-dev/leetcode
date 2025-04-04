# Last updated: 4/4/2025, 12:36:33 AM
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        dupRow = set()
        dupCol = set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    dupRow.add(i)
                    dupCol.add(j)

        for i in dupRow:
            for j in range(n):
                matrix[i][j]=0
        
        for j in dupCol:
            for i in range(m):
                matrix[i][j]=0

        return matrix
