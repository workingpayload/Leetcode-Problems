class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        v=sorted(satisfaction,reverse=True)
        sum=0
        ans=0
        for i in v:
            if(sum+i>0):
                ans+=sum+i
                sum+=i
        return ans