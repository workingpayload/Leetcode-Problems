class Solution:
    def rotateString(self, s: str, goal: str) -> bool: 
        
        def issub(s,t):
            if s in t:return True
            return False
        
        
        
        
        n = len(s)
        m = len(goal)
        
        if n!=m:
            return False
        
        if m>0 and n>0:
            new_s = s+s
            return issub(goal,new_s)
        else:
            return False