class Solution:
    def maxPower(self, s: str) -> int:
        
        res = []
        
        count = 0
        
        
        
        
        for i in range(1,len(s)):
            
            if s[i]==s[i-1]:
                count+=1
                if i==len(s)-1:
                    res.append(count+1)
            else:
                res.append(count+1)
                count=0    
                
                
        if not res:
            return 1
                
        return max(res)      
                
                
                
        