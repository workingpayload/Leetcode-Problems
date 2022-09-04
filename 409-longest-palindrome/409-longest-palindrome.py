class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = {}
        for c in s:
            counts[c] = counts.get(c, 0) + 1
        
        ans = 0
        isOddPresent = False
        for key in counts.keys():
            current = counts[key]
            if current % 2 == 0:
                ans += current
            else: 
                isOddPresent = True
                ans += current - 1
        return (ans + 1) if isOddPresent else ans