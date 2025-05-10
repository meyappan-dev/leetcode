# Last updated: 5/10/2025, 7:11:55 PM
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum = n*(n+1)//2
        for num in nums:
            sum = sum - num
        return sum