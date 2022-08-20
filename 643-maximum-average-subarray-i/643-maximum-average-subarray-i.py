class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        curr = 0
        
        for i in range(k):
            curr+=nums[i]
            
            
            
            
        maxx = curr
        
        for i in range(k,len(nums)):
            curr += nums[i] - nums[i-k]
            
            if curr>maxx:
                maxx = curr
                
                
        return maxx/k        
        