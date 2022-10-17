class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        new = set(nums)
        
        count = 0
        
        for i in nums:
            
            if i-1 not in new:
                
                length = 0
                
                while(i+length in new):
                    length+=1
                    
                count = max(length,count)
                
        return count        
        