class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        
        for i in operations:
            if i[0]=='+' or i[2]=='+':
                x+=1
            elif i[0]=='-' or i[2]=='-':
                x-=1
                
        return x        
        