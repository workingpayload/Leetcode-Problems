class Solution:
    def greatestLetter(self, s: str) -> str:
        
        newlist = []
        
        
        for i in s:
            if i.upper() in s:
                if i.lower() in s:
                    newlist.append(i.upper())
                    
                    
                    
        if newlist == []:
            return ""
        return max(newlist)            
        