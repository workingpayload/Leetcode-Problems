class Solution:
    def makeGood(self, s: str) -> str:
        
        stack = []
        
        for i in s:
            
            if not stack:
                stack.append(i)
                
                
            elif stack[-1].islower() and stack[-1].upper()==i:
                stack.pop()
                
            elif stack[-1].isupper() and stack[-1].lower()==i:
                stack.pop()
                
                
            else:
                stack.append(i)
                
                
                
        return "".join(stack)       
        
        
                
                
                
                
        