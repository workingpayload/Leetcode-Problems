class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        for i in reversed(range(len(nums)-2)):
            if nums[i] + nums[i+1] > nums[i + 2]:
                return nums[i] + nums[i+1] + nums[i + 2]
            
        return 0
        