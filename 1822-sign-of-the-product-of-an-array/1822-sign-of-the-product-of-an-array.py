class Solution:
    def arraySign(self, nums: List[int]) -> int:
        pro = 1
        for i in range(len(nums)):
            pro *= nums[i]
            
        if pro>0:
            return 1
        elif pro==0:
            return 0
        else:
            return -1
        