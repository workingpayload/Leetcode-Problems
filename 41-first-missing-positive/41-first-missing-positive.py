class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        
        dic = {}
        
        for i in range(1,len(nums)+1):
            dic[i] = True
            
        for i in nums:
            if i in dic:
                del dic[i]
                
        if len(dic)>0:
            return list(dic.keys())[0]
        
        return len(nums)+1
            
        
        