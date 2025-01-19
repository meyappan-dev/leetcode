class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # nums.sort()
        res = {}

        for i in range(len(nums)):
            # j=i+1
            # while j<len(nums):
            # if nums[i]==nums[i+1]:
            if nums[i] in res:
                return True
            else:
                res[nums[i]] = True
                # print(res)
            # else:
            #     j+=1
        return False