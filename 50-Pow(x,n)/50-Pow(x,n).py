# Last updated: 4/21/2025, 7:30:01 PM
class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        isNegative = False
        if n < 0:
            n *= -1
            isNegative = True
        while n > 0:
            if n%2==0:
                n=n//2
                x = x * x
            else:
                n = n-1
                ans = ans * x
        if isNegative:
            ans = 1 / ans
        return ans
