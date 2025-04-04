# Last updated: 4/4/2025, 1:21:17 AM
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res=[[1]]
        nextRow=[]

        for i in range(1,numRows):
            temp = [0] + res[-1] + [0]
            for j in range(i+1):
                nextRow.append(temp[j]+temp[j+1])
            res.append(nextRow)
            nextRow=[]
        return res