class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        n=len(dist)
        if hour<=n-1: return -1

        def time(speed):
            sum=0
            for x in dist[:n-1]:
                sum+=(x+speed-1)//speed #ceiling function
            sum+=dist[n-1]/speed
            return sum
        
        left=1
        right=1+max(max(dist), int(dist[-1]//(hour-n+1)))
        speed=0
        while left<=right:
            mid=(left+right)//2
            if time(mid)<= hour:
                speed=mid
                right=mid-1
            else:
                left=mid+1
        return speed