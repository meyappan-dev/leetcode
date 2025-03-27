# Last updated: 3/27/2025, 10:09:24 AM
import sys

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        maxVal = nums[0]

        for i in range(len(nums)):
            if curSum < 0:
                curSum = 0
            curSum += nums[i]
            maxVal = max(curSum,maxVal)
        return maxVal