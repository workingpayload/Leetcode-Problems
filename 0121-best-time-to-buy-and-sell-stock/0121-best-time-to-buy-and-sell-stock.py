class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        max_so = 0
        
        
        l = 0
        r = 1
        
        while(r<len(prices)):
            
            max_so = max(max_so,prices[r]-prices[l])
            
            if prices[r]<prices[l]:
                l=r
                r+=1
            else:
                r+=1
                
        return max_so        
                
                
         
     