class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # lcp = ""
        # temp=""
        # count+=1
        # i=0
        # while j < range(len(strs)):
        #     temp = strs[j][i]
        #     while i < len(temp)
        #     if str[i] != temp[i]:
        #         break
        #     else:
        #         count+=1
        #         i+=1
        #     if(j == len(strs)-1):
        #         j=0
        #     else:
        #         j+=1
        res=""
        for i in range(len(strs[0])):
            for s in strs:
                if i==len(s) or s[i] != strs[0][i]:
                    return res
            res+=strs[0][i]
        return res