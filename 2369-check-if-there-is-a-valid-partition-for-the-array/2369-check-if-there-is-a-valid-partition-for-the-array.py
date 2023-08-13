class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n=len(nums)
        @cache
        def fn(index):
            if index==n:
                return True

            if index+1<n and nums[index]==nums[index+1] and fn(index+2):
                return True

            if index+2<n and nums[index]==nums[index+1]==nums[index+2] and fn(index+3):
                return True

            if index+2<n and nums[index]==nums[index+1]-1 and nums[index+1]==nums[index+2]-1 and fn(index+3):
                return True

            return False

        return fn(0)   