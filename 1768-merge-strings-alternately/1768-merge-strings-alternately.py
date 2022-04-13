class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if len(word1)>len(word2):
            ans = ""
            for i in range(len(word2)):
                ans+=word1[i]
                ans+=word2[i]
                
            ans+=word1[len(word2):]    
            
        elif len(word1)<len(word2):
            ans = ""
            for i in range(len(word1)):
                ans+=word1[i]
                ans+=word2[i]
                
            ans+=word2[len(word1):] 
            
        else:
            ans = ""
            
            for i in range(len(word1)):
                ans+=word1[i]
                ans+=word2[i]
                
        
        return ans
            
               
            
               
                      
            
        