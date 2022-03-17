class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_num = list(set(nums))
        if len(set_num)!=len(nums):
            return True
        else:
            return False
        