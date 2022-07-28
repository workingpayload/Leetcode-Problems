from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = Counter(s)
        b = Counter(t)
        
        if len(s)==len(t):
            for i in a:
                if a[i]!=b[i]:
                    return False
            return True
        else:
            return False