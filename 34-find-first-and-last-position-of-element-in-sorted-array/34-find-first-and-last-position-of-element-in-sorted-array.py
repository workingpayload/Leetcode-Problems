class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1,-1]
        
        i = nums.index(target)
        j = len(nums) - nums[::-1].index(target) - 1
        
        return [i,j]