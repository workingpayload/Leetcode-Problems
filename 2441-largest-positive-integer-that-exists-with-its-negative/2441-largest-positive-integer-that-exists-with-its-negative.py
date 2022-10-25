class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        
        maxi = -1
        
        for i in nums:
            
            if (0-i) in nums:
                maxi = max(maxi,i)
        
        return maxi