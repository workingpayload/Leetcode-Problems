class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        l = []
        for i in range(1,len(nums),2):
            l.append(min(nums[i],nums[i-1]))
        return sum(l)    
        
        