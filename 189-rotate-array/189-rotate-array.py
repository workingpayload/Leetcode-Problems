class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            temp = nums[len(nums)-1]
            nums.pop(len(nums)-1)
            nums.insert(0,temp)

        return nums    