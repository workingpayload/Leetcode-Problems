class Solution:
    def partitionString(self, s: str) -> int:
        ans=1
        ls=[]
        for i in s:
            if i in ls:
                ls=[i]
                ans+=1
            else:
                ls+=[i]
        return ans