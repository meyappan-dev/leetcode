class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        temp1=nums[0]
        answer = [1] * len(nums)
        for i in range(len(nums)):
            if i>0:
                answer[i] = temp1
                temp1 = nums[i]*temp1
        
        temp1=nums[len(nums)-1]
        for j in reversed(range(len(nums))):
            if j < len(nums)-1:
                answer[j] = answer[j]*temp1
                temp1 = nums[j]*temp1
        return answer