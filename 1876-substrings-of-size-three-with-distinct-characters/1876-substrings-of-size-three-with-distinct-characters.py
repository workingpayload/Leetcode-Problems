class Solution:
    def countGoodSubstrings(self, s: str) -> int:

        l = 0
        r = 2
        count=0

        while(r<len(s)):
            new = {}
            for i in range(l,r+1):
                new[s[i]] = 1 + new.get(s[i],0)

            flag = True    

            for i in new.values():
                if i>1:
                    flag=False
            if flag == True:
                count+=1   
            l+=1
            r+=1

        return count             


