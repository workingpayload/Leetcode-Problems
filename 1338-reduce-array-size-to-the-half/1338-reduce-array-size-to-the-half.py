class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        c=Counter(arr)
        a=list(c.values())
        a.sort()
        p=sum(a)
        p2=p//2
        c=0
        a=a[::-1]
        i=0
        while p2>0:
            p2-=a[i]
            i+=1
            c+=1
        return c