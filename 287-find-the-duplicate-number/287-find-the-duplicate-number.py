class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dicti = {}
        
        for i in nums:
            if i in dicti:
                dicti[i]+=1
            else:
                dicti[i]=1
                
                
        for j in dicti:
            if dicti[j]>1:
                return j
        