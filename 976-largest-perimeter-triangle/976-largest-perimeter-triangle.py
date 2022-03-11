import math
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums)-2):
            perimeter=nums[i]+nums[i+1]+nums[i+2]
            if perimeter>2*nums[i]:
                return perimeter
        return 0    
        