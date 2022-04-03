class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        num = []
        count = 0
        for i in range(start,3000,2):
            num.append(i)
            count+=1
            if count == n:
                break
            
        
        xor = num[0]
        
        for i in range(1,len(num)):
            xor = xor ^ num[i]
         
        return xor
            
        