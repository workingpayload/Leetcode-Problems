class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numset = set(nums)
        
        length = 0
        
        longestseq = 0
        
        
        for i in nums:
            
            if i-1 not in numset:
                length = 0
                
                
                while(i+length in numset):
                    length+=1
                    
                longestseq = max(longestseq,length)
                
                
        return longestseq        
        
        