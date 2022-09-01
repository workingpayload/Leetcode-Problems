class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        
        res,l = "",len(s)
        
        for i in range(l):
            for j in range(l,i,-1):
                r = s[i:j]
                if set(r)==set(r.swapcase()):
                    res = max(res,r,key=len)
                    break
        return res            
                    
                    
        