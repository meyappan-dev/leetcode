class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=1
        k = 1
        j=1
        if(len(nums)>1):
            res = nums[0]
            while j < len(nums):
                if res != nums[j]:
                    nums[i],nums[j]=nums[j],nums[i]
                    res = nums[i]
                    i+=1
                    k+=1
                j+=1
            return k
        else:
            return 1