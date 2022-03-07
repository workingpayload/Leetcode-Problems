class Solution:
    def isPalindrome(self, x: int) -> bool:
        p = str(x)
        if p==p[::-1]:
            return True
        else:
            return False