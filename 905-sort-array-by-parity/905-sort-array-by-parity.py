class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        
        for i in range(len(nums)):
            if nums[i]%2==0:
                even.append(nums[i])
                
            else:
                odd.append(nums[i])
                
                
                
        new_nums = []
        
        
        for i in range(len(even)):
            new_nums.append(even[i])
            
        for i in range(len(odd)):
            new_nums.append(odd[i])
            
        return new_nums    
        