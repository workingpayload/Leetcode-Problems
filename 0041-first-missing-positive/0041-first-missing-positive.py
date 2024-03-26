class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        mp = {}
        maxi = max(nums, default=0)
        for num in nums:
            mp[num] = True
        for i in range(1, maxi):
            if i not in mp:
                return i
        return 1 if maxi < 0 else maxi + 1
