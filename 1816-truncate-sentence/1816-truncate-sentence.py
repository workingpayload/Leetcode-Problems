class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        li = s.split()
        
        p = " ".join(li[:k])
        
        return p
            
        
        