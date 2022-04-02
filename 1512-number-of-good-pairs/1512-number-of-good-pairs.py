class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = 0
        a = Counter(nums).values()
        
        for i in a:
            counter+=(i*(i-1)//2)
            
        return counter    
        
        
        
        
        
        