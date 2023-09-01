class Solution:
    def countBits(self, n: int) -> List[int]:
        def decimalToBinary(n):
            return "{0:b}".format(int(n))
        l = []
        for i in range(0,n+1):
            l.append(str(decimalToBinary(i)))
        p = []    
        for i in range(len(l)): 
             p.append(l[i].count("1"))
                  
        return p             
        