# Last updated: 5/22/2025, 12:49:10 AM
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        maxWater = 0

        while left < right:            
            water = min(height[left],height[right]) * (right-left)
            maxWater = max(water,maxWater)

            if height[left] <= height[right]:
                left += 1 
            
            else:
                right -= 1
        return maxWater