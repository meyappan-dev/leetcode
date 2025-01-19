class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            # j=i+1
            # while j<len(nums):
            if nums[i]==nums[i+1]:
                return True
            # else:
            #     j+=1
        return False