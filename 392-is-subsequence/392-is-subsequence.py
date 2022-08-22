class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)
        
        i=0
        j=0
        
        while j<m and i<n:
            if s[j]==t[i]:
                j+=1
            i+=1
            
        return j==m    