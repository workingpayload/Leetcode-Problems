class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        local = 0
        global_ = float('-inf')
        
        for i in range(len(nums)):
            
            local = max(nums[i],nums[i]+local)
            if local>global_:
                global_ = local
                
        return global_        
        
        