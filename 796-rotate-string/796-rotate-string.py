class Solution:
    def rotateString(self, s: str, goal: str) -> bool: 
        n = len(s)
        m = len(goal)
    
        if len(s)!=len(goal):
            return False

        if len(s)>0 and len(goal)>0:
            new_s = s+s
            return (goal in new_s)
        else:
            return False