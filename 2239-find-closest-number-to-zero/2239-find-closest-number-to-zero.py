class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        for i, v in enumerate(nums):
            if i == 0:
                diff = abs(v)    
                result = v
            if abs(v) < diff: 
                diff = abs(v)
                result = v
            elif abs(v) == diff:
                result = max(result, v)
        return result