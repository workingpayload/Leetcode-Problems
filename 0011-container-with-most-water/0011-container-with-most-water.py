class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        maxim = float('-inf')
        
        l = 0
        r = len(height)-1
        
        while(l<r):
            maxim = max(maxim,min(height[l],height[r])*(r-l))
            
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
                
        return maxim        
        