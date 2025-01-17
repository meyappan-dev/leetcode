class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphaNumericChar = ""
        for char in s:
            if char.isalnum():
                alphaNumericChar += char.lower()
        print(alphaNumericChar)
        j=len(alphaNumericChar)-1
        for i in range(len(alphaNumericChar)):
            if alphaNumericChar[i] != alphaNumericChar[j]:
                return False
            j-=1
        return True