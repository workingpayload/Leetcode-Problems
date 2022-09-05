class Solution:
    def maxScore(self, s: str) -> int:
        
        res = []
        
        for i in range(len(s)):
            left = s[:i+1]
            right = s[i+1:]
            
            if len(right)==0:
                break
            res.append(left.count("0")+right.count("1"))    
                
                
                
                
                
            
        
        
            
        return max(res)
        