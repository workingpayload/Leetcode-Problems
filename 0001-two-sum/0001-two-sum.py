class Solution:
    def twoSum(self, nums: List[int], tar: int) -> List[int]:
        
        lookup = {}
        
        for i,n in enumerate(nums):
            
            diff = tar-n
            
            if diff in lookup:
                return [lookup[diff],i]
            
            lookup[n]=i

            
            
            
        
            
       

            
                    
        
