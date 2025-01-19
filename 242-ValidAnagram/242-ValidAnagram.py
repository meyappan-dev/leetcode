class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        uniqueValues1 = {}
        for char in s:
            if char not in uniqueValues1:
                uniqueValues1[char]=1
            else:
                uniqueValues1[char]+=1
        
        uniqueValues2 = {}
        for char in t:
            if char not in uniqueValues2:
                uniqueValues2[char]=1
            else:
                uniqueValues2[char]+=1

        if uniqueValues1 == uniqueValues2:
            return True
        else:
            return False
        
        # for char in t:
        #     if char not in uniqueValues1:
        #         # uniqueValues2.add(char)
        #         return False
        # return True