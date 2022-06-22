class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        sNums=sorted(nums)
        return(sNums[len(nums)-k])