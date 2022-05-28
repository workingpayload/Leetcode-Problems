class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums)==1:
            if nums[0]==1:
                return "0"
        for i in range(0,len(nums)+1):
            if i not in nums:
                return i