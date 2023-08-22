class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ''
        
        
        while columnNumber>0:
            
            n = columnNumber%26
            
            if n==0:
                columnNumber-=1
                res+='Z'
            else:
                res+=chr(64+n)
            columnNumber = columnNumber//26
            
            
        return res[::-1]    