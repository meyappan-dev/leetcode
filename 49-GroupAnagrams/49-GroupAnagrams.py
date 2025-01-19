class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for word in strs:
            count =[0]*26
            for i in range(len(word)):
                index = ord(word[i])-ord('a')
                count[index]+=1
            res[tuple(count)].append(word)
        return list(res.values())