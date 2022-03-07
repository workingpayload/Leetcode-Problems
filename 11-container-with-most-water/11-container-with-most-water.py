class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        l = 0
        j = len(height)-1
        
        while(l<j):
            mint = min(height[l],height[j])
            ar = mint*(j-l)
            area = max(area,ar)
            if height[l]>height[j]:
                j-=1
            else:
                l+=1
        return area        
        