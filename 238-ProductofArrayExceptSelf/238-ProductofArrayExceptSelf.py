class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i=0
        temp=1
        prefixList = [1] * len(nums)
        postfixList = [1] * len(nums)
        answer = [1] * len(nums)
        for j in range(len(nums)):
            temp = nums[j]*temp
            prefixList[j] = temp
        temp = 1
        for j in reversed(range(len(nums))):
            temp = nums[j]*temp
            postfixList[j] = temp
        
        for i in range(len(nums)):
            if i==0:
                answer[i] = postfixList[i+1]
            elif i == len(nums)-1:
                answer[i] = prefixList[i-1]
            else:
                answer[i] = prefixList[i-1] * postfixList[i+1]
        return answer