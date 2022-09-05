class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        p = - k - 1
        for i, n in enumerate(nums):
            if n and i - p < k + 1:
                return False
            p = i if n else p
        return True