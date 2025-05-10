# Last updated: 5/10/2025, 12:29:34 PM
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        count = 0
        last = len(nums)-1
        while i <= last:
            if nums[i] == val:
                nums[i], nums[last] = nums[last], nums[i]
                last-=1
                count +=1
            else:
                i+=1
        return len(nums)-count