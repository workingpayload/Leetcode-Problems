class Solution:
    def largestGoodInteger(self, num: str) -> str:
        a=[]
        for i in range(len(num)-1):
            if(num[i]==num[i+1]==num[i-1]):
                a.append(int(num[i]))

        if(len(a)!=0):
            b=max(a)
            return (str(b)*3)
        else:
            return("")
                
            
        