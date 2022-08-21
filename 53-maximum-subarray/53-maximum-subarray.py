class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        local = 0
        global_max = float('-inf')
        
        for i in range(len(nums)):
            
            local = max(nums[i],nums[i]+local)

            if local>global_max:
                global_max = local
                
        return global_max        