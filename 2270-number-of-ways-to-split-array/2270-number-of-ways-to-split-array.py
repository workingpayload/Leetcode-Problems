class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        
        sumto = sum(nums)-nums[0]
        left = nums[0]
        res = 0
        
        
        for i in range(1,len(nums)):
            
            if left>=sumto:
                res+=1
            sumto-=nums[i]
            left+=nums[i]
                
        return res