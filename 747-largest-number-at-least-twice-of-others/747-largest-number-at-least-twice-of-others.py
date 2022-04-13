class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxi = max(nums)
        count = 0
        for i in range(len(nums)):
            if nums[i]!=maxi:
                dou = nums[i]*2
                if dou<=maxi:
                    count+=1
        if count==len(nums)-1:
            return nums.index(maxi)
        else:
            return -1
        