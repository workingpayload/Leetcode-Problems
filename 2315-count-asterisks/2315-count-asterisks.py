class Solution:
    def countAsterisks(self, s: str) -> int:
        
        stack = []
        
        count = 0
        
        for i in s:
            if '|' in stack:
                if i=='|':
                    stack=[]
                else:
                    stack.append(i)
            else:
                if i=='|':
                    stack.append(i)
                else:
                    if i=='*':
                        count+=1
                        
                        
        return count                
                    