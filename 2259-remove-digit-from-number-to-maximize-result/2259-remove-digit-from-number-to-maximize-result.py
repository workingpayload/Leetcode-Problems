class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        
        res = []
        
        l = list(number)
        
        for i in range(len(number)):
            
            if number[i]==digit:
                res.append(int("".join(l[:i]+l[i+1:])))
                
        return str(max(res))        

        
        