class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        
        l = 0
        i = 0
        
        for k in range(len(nums)):
                       if nums[l]!=val:
                               nums[i]=nums[l]
                               i+=1
                               l+=1
                       else:
                           l+=1
        return i               