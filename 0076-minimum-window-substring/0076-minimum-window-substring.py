class Solution:
    def minWindow(self, s: str, t: str) -> str:
        lst=[0]*58
        tr=[0]*58
        st,end,ans=0,0,""
        for i in t:
            lst[ord(i)-ord('A')]+=1
        while st<=end and end<=len(s):
            flag=0
            for i in range(58):
                if lst[i]<tr[i]:
                    flag=1
                elif lst[i]>tr[i]:
                    if end>=len(s):
                        return ans
                    tr[ord(s[end])-ord('A')]+=1
                    end+=1
                    break
            else:
                if flag==0:
                    return s[st:end]
                if ans=="" or len(ans)>len(s[st:end]):
                    ans=s[st:end]
                tr[ord(s[st])-ord('A')]-=1
                st+=1
        return ans