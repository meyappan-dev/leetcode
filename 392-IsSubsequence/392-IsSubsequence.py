class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        count,i = 0,0
        while i < len(s):
            for j in range(len(t)):
                if(s[i] == t[j]):
                    count+=1
                    i+=1
                    if(i==len(s)):
                        break
            i=len(s)
        if(count == len(s)):
            return True
        else:
            return False