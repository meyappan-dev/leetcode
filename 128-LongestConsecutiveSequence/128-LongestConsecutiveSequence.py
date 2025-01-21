class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashMap={}
        for num in nums:
            if num not in hashMap:
                hashMap[num]=num+1
        
        if len(nums)==0:
            return 0
        
        # count=1
        hashSet=set()
        longest=0
        for key, values in hashMap.items():
            # if values in hashMap:
            #     if key-1 not in hashMap:
            #         hashSet.append(key)
            #         if values is in hashMap:    
            #             hashSet.append(values)
            #         start
            #     else:
            #         count+=1
            if key-1 not in hashMap:
                length=1
                while key+length in hashMap:
                    length+=1
                longest=max(longest,length)
                # print(length)
        return longest
        


        # return count