class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=[]
        for i in range(len(nums)):
            freq.append([])
        count={}
        for num in nums:
            count[num]=count.get(num,0)+1
        
        for num,cnt in count.items():
            # for i in range(len(num)):
            freq[cnt-1].append(num)
        
        res=[]
        for i in range(len(freq)-1,-1,-1):
            for num in freq[i]:
                res.append(num)
                if(len(res)==k):
                    return res