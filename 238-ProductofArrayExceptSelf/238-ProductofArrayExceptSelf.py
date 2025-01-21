class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # temp1=1
        # answer = [1] * len(nums)
        # for i in range(len(nums)):
        #     answer[i] = temp1
        #     temp1 = nums[i]*temp1        
        # temp1=1
        # for j in reversed(range(len(nums))):
        #     answer[j] = answer[j]*temp1
        #     temp1 = nums[j]*temp1
        # return answer

        res=[1]*len(nums)
        j=len(nums)-2
        temp=1
        temp1=1
        for i in range(1,len(nums)):
            temp1=nums[i-1]*temp1
            res[i]=temp1*res[i]
            while j >=0:
                temp=nums[j+1]*temp
                res[j]=temp*res[j]
                j-=1
        return res