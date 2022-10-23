class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        current_min , max_so = float('inf') , 0
        
        
        for i in prices:
            current_min = min(current_min,i)
            
            max_so = max(max_so,i-current_min)
            
        return max_so    
         
     