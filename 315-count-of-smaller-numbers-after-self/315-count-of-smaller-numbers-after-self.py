from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        
        sorted_list = SortedList(nums)
        
        res = []
        
        
        for i in nums:
            res.append(sorted_list.index(i))
            sorted_list.remove(i)
            
            
        return res    
        