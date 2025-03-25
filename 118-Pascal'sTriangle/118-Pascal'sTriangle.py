# Last updated: 3/25/2025, 2:43:37 AM
class Solution:
    def calculateSum(self,numRows: int, baseRow: List[int],resFinal = List[List[int]]) -> List[List[int]]:
        res2=[]
        for num in range(3,numRows+1):
            for i in range(len(baseRow)):
                if i == 0:
                    res2.append(baseRow[i])
                if i == len(baseRow)-1:
                    res2.append(baseRow[i])
                if i+1 <= len(baseRow)-1:    
                    dummy = baseRow[i]+baseRow[i+1]
                    res2.append(dummy)
            resFinal.append(res2)
            print(res2)
            baseRow=res2.copy()
            res2=[]
        return resFinal

    def generate(self, numRows: int) -> List[List[int]]:
        res=[]
        if numRows >= 1:
            res.append([1])
        if numRows > 1:
            res.append([1,1])
        if numRows > 2:
            res = self.calculateSum(numRows,[1,1],res)
        return res