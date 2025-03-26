# Last updated: 3/25/2025, 10:50:50 PM
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        breakPoint = -1
        for i in range(len(nums)-1,-1,-1):
            if nums[i] > nums[i-1]:
                breakPoint = i-1
                break
        if breakPoint == -1:
            nums.reverse()
        else:
            swapPosition = len(nums)-1
            swap = -1
            if swapPosition != breakPoint+1:
                for j in range(swapPosition,breakPoint,-1):
                    if nums[j] > nums[breakPoint]:
                        if swap == -1:
                            swap = nums[j]
                            swapPosition = j
                        else:
                            if nums[j] < swap:
                                swap = min(swap,nums[j])
                                swapPosition = j
            nums[breakPoint], nums[swapPosition] = nums[swapPosition], nums[breakPoint]
            k = breakPoint+1
            nums[k:]=reversed(nums[k:])