# Last updated: 4/21/2025, 6:21:50 PM
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