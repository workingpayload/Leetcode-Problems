class Solution:
    def replaceDigits(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            if s[i].isalpha():
                res += s[i]
            elif s[i].isnumeric():
                res += chr(ord(s[i-1]) + int(s[i]))
        return res
        